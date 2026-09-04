#!/usr/bin/env bash
# Instala los 7 servidores MCP de Hostinger en Claude Code a scope "user" (global,
# disponible en todos los proyectos). Idempotente: se puede correr las veces que haga falta.
#
#   HOSTINGER_API_TOKEN=xxxxx bash docs/setup-hostinger-mcp.sh
#
# El token se saca de hPanel -> Cuenta -> API -> Generar token.
# NO hardcodear el token en este archivo: queda commiteado en git.

set -euo pipefail

SERVERS=(hosting domains dns billing reach vps ecommerce)

if [ -z "${HOSTINGER_API_TOKEN:-}" ]; then
  read -rsp "HOSTINGER_API_TOKEN: " HOSTINGER_API_TOKEN
  echo
fi

if [ -z "$HOSTINGER_API_TOKEN" ]; then
  echo "Error: falta HOSTINGER_API_TOKEN." >&2
  exit 1
fi

command -v claude >/dev/null || { echo "Error: no se encontro el CLI 'claude' en el PATH." >&2; exit 1; }

for s in "${SERVERS[@]}"; do
  claude mcp remove "hostinger-$s" -s user >/dev/null 2>&1 || true
  claude mcp add "hostinger-$s" -s user \
    -e "HOSTINGER_API_TOKEN=$HOSTINGER_API_TOKEN" \
    -- npx --package=hostinger-api-mcp@latest "hostinger-$s-mcp"
done

echo
echo "Listo. Verificando conexion (la primera vez npx baja el paquete, puede tardar):"
claude mcp list
