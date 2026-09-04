# CRM Rubicat — utilidades Odoo

Herramientas para operar el CRM de Rubicat en Odoo 19 Community
(`https://odoo-odoo.b6mgbu.easypanel.host`, DB `ialab`, VPS Hostinger / EasyPanel).

## Por qué existe esto

Las sesiones remotas de Claude Code (claude.ai/code) corren en un contenedor cuyo
egress está restringido por política: tanto el host de Odoo como el del MCP
devuelven **403 en el CONNECT** del proxy, y la IP del VPS por HTTP plano no es
ruteable. Es decir, desde una sesión remota **no hay forma de tocar el CRM**.

`odoo_cli.py` cierra ese hueco: lo corrés vos desde tu máquina (que sí llega al
VPS) y el JSON que devuelve se puede pegar en la sesión para seguir trabajando.

Alternativa: correr Claude Code en local (CLI o app de escritorio), donde el
MCP de Odoo sí es alcanzable.

## Setup

Sin dependencias — solo Python 3 stdlib.

```bash
export ODOO_URL=https://odoo-odoo.b6mgbu.easypanel.host
export ODOO_DB=ialab
export ODOO_USER=axellaban@gmail.com
export ODOO_APIKEY=...        # Ajustes > Usuarios > Claves de API
```

La API key va por entorno a propósito: no se commitea al repo.

## Uso

```bash
python3 odoo_cli.py whoami                 # verifica credenciales y versión
python3 odoo_cli.py snapshot > snapshot.json   # estado completo del CRM
python3 odoo_cli.py fields crm.lead        # esquema de un modelo
python3 odoo_cli.py count crm.lead '[["type","=","opportunity"]]'
python3 odoo_cli.py read res.users '[["share","=",false]]' '["name","login","email"]'
python3 odoo_cli.py exec crm.lead write '[[12],{"user_id":5}]'   # escape hatch
```

`snapshot` es el que importa: junta en un JSON los módulos instalados, usuarios
internos, etapas del pipeline, equipos, etiquetas (contacto y CRM), conteos de
partners/leads/oportunidades, oportunidades agrupadas por etapa y por vendedor, y
los huecos de higiene de datos (sin vendedor, sin cierre previsto, sin actividad,
sin email/teléfono). Cada bloque está aislado: si un modelo falla, el resto sale
igual con un `_error` en esa clave.

## Estado conocido del CRM (según notas, sin verificar contra la instancia)

Cargado desde `CRM_Rubicat_Base_Maestra.xlsx`:

- 103 cuentas, 52 PDV, 21 contactos, 22 oportunidades (~$23,5M)
- 6 usuarios vendedores
- Etiquetas jerárquicas: Tipo de cuenta / Estado / Vendedor / Zona
- Módulos: `crm`, `contacts` — `sale` **no** instalado

Correr `snapshot` es lo que confirma o desmiente todo esto.

## Pendientes

- [ ] **MCP de Odoo expuesto sin autenticación** (`odoo-odoo-mcp.b6mgbu.easypanel.host`).
      Cualquiera con la URL puede operar el CRM. Cerrarlo es lo primero.
- [ ] Los 6 usuarios vendedores tienen logins `@rubicat.invalid` — faltan los
      emails reales. `snapshot` los lista en `usuarios_sin_email_real`.
