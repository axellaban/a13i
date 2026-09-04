#!/usr/bin/env python3
"""Cliente XML-RPC minimo para el CRM de Rubicat (Odoo 19 Community, DB: ialab).

Solo stdlib, sin dependencias. Pensado para correrse desde una maquina con acceso
de red al VPS: el sandbox remoto de Claude Code tiene el host bloqueado por
politica de egress (403 en el CONNECT del proxy).

Credenciales por entorno -- nunca hardcodeadas en el repo:

    export ODOO_URL=https://odoo-odoo.b6mgbu.easypanel.host
    export ODOO_DB=ialab
    export ODOO_USER=axellaban@gmail.com
    export ODOO_APIKEY=...      # Ajustes > Usuarios > Claves de API

Uso:
    python3 odoo_cli.py whoami
    python3 odoo_cli.py snapshot > snapshot.json
    python3 odoo_cli.py fields crm.lead
    python3 odoo_cli.py count  crm.lead '[["type","=","opportunity"]]'
    python3 odoo_cli.py read   res.users '[["share","=",false]]' '["name","login","email"]'
    python3 odoo_cli.py exec   crm.lead write '[[12],{"user_id":5}]'
"""

import json
import os
import ssl
import sys
import xmlrpc.client

URL = os.environ.get("ODOO_URL", "https://odoo-odoo.b6mgbu.easypanel.host").rstrip("/")
DB = os.environ.get("ODOO_DB", "ialab")
USER = os.environ.get("ODOO_USER", "")
APIKEY = os.environ.get("ODOO_APIKEY", "")


class Odoo:
    def __init__(self):
        if not USER or not APIKEY:
            sys.exit("Falta ODOO_USER y/o ODOO_APIKEY en el entorno. Ver docstring.")
        ctx = ssl.create_default_context()
        cafile = os.environ.get("SSL_CERT_FILE")
        if cafile and os.path.exists(cafile):
            ctx.load_verify_locations(cafile)
        self._common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common", context=ctx)
        self._models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object", context=ctx)
        self.version = self._common.version().get("server_version", "?")
        self.uid = self._common.authenticate(DB, USER, APIKEY, {})
        if not self.uid:
            sys.exit(f"Autenticacion rechazada para {USER} en la DB '{DB}'.")

    def kw(self, model, method, args=None, kwargs=None):
        return self._models.execute_kw(
            DB, self.uid, APIKEY, model, method, args or [], kwargs or {}
        )

    def search_read(self, model, domain=None, fields=None, **kw):
        return self.kw(model, "search_read", [domain or []], dict(fields=fields, **kw))

    def count(self, model, domain=None):
        return self.kw(model, "search_count", [domain or []])

    def read_group(self, model, domain, fields, groupby, **kw):
        return self.kw(model, "read_group", [domain, fields, groupby], kw)


def _section(out, key, fn):
    """Corre una parte del snapshot sin que un modelo faltante tumbe el resto."""
    try:
        out[key] = fn()
    except Exception as exc:  # noqa: BLE001 - queremos el motivo, no el traceback
        out[key] = {"_error": f"{type(exc).__name__}: {exc}"}


def snapshot(api):
    """Estado del CRM en un JSON, para planificar los proximos pasos sin acceso directo."""
    out = {"servidor": {"url": URL, "db": DB, "version": api.version, "uid": api.uid}}

    _section(out, "modulos_instalados", lambda: api.search_read(
        "ir.module.module", [("state", "=", "installed")], ["name"], order="name"))

    _section(out, "usuarios_internos", lambda: api.search_read(
        "res.users", [("share", "=", False)], ["name", "login", "email", "active"], order="id"))

    _section(out, "etapas_pipeline", lambda: api.search_read(
        "crm.stage", [], ["name", "sequence", "is_won", "fold", "team_id"], order="sequence"))

    _section(out, "equipos_venta", lambda: api.search_read(
        "crm.team", [], ["name", "user_id", "active"]))

    _section(out, "etiquetas_contacto", lambda: api.search_read(
        "res.partner.category", [], ["name", "parent_id", "color"], order="parent_id,name"))

    _section(out, "etiquetas_crm", lambda: api.search_read(
        "crm.tag", [], ["name", "color"], order="name"))

    _section(out, "conteos", lambda: {
        "partners_total": api.count("res.partner", []),
        "partners_empresa": api.count("res.partner", [("is_company", "=", True)]),
        "partners_contacto": api.count("res.partner", [("is_company", "=", False)]),
        "leads": api.count("crm.lead", [("type", "=", "lead")]),
        "oportunidades": api.count("crm.lead", [("type", "=", "opportunity")]),
        "actividades_pendientes": api.count("mail.activity", []),
    })

    _section(out, "oportunidades_por_etapa", lambda: api.read_group(
        "crm.lead", [("type", "=", "opportunity")],
        ["expected_revenue:sum"], ["stage_id"]))

    _section(out, "oportunidades_por_vendedor", lambda: api.read_group(
        "crm.lead", [("type", "=", "opportunity")],
        ["expected_revenue:sum"], ["user_id"]))

    _section(out, "oportunidades_sin_vendedor", lambda: api.count(
        "crm.lead", [("type", "=", "opportunity"), ("user_id", "=", False)]))

    _section(out, "oportunidades_sin_cierre_previsto", lambda: api.count(
        "crm.lead", [("type", "=", "opportunity"), ("date_deadline", "=", False)]))

    _section(out, "oportunidades_sin_actividad", lambda: api.count(
        "crm.lead", [("type", "=", "opportunity"), ("activity_ids", "=", False)]))

    # Higiene de datos que el contexto ya marcaba como pendiente.
    _section(out, "usuarios_sin_email_real", lambda: api.search_read(
        "res.users",
        ["&", ("share", "=", False),
         "|", ("email", "=", False), ("login", "like", "%@rubicat.invalid")],
        ["name", "login", "email"]))

    _section(out, "partners_sin_contacto", lambda: {
        "sin_email": api.count("res.partner", [("email", "=", False)]),
        "sin_telefono": api.count("res.partner", [("phone", "=", False), ("mobile", "=", False)]),
    })

    return out


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    cmd, rest = argv[1], argv[2:]
    api = Odoo()

    if cmd == "whoami":
        me = api.search_read("res.users", [("id", "=", api.uid)],
                             ["name", "login", "email", "groups_id"])
        result = {"uid": api.uid, "db": DB, "version": api.version, "usuario": me}
    elif cmd == "snapshot":
        result = snapshot(api)
    elif cmd == "fields":
        result = api.kw(rest[0], "fields_get", [], {
            "attributes": ["string", "type", "required", "relation", "selection"]})
    elif cmd == "count":
        result = api.count(rest[0], json.loads(rest[1]) if len(rest) > 1 else [])
    elif cmd == "read":
        domain = json.loads(rest[1]) if len(rest) > 1 else []
        fields = json.loads(rest[2]) if len(rest) > 2 else None
        limit = int(rest[3]) if len(rest) > 3 else 200
        result = api.search_read(rest[0], domain, fields, limit=limit)
    elif cmd == "exec":
        args = json.loads(rest[2]) if len(rest) > 2 else []
        kwargs = json.loads(rest[3]) if len(rest) > 3 else {}
        result = api.kw(rest[0], rest[1], args, kwargs)
    else:
        sys.exit(f"Comando desconocido: {cmd}\n{__doc__}")

    json.dump(result, sys.stdout, indent=2, ensure_ascii=False, default=str)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main(sys.argv)
