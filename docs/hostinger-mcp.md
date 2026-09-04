# Hostinger MCP en Claude Code

Los 7 servidores MCP de Hostinger (`hostinger-api-mcp`), instalados a **scope `user`** —
o sea globales: quedan disponibles en todos los proyectos, no solo en este repo.

## Instalación

```bash
HOSTINGER_API_TOKEN=tu-token bash docs/setup-hostinger-mcp.sh
```

O a mano, uno por uno:

```bash
claude mcp add hostinger-hosting -s user -e HOSTINGER_API_TOKEN=tu-token \
  -- npx --package=hostinger-api-mcp@latest hostinger-hosting-mcp
```

…y lo mismo para `domains`, `dns`, `billing`, `reach`, `vps`, `ecommerce`.
El nombre del binario siempre es `hostinger-<área>-mcp`.

Después de agregarlos hay que **reiniciar Claude Code** para que cargue las herramientas.
Verificar con `claude mcp list` (debe decir `✓ Connected` en los 7).

## Los 7 servidores

| Nombre | Binario | Para qué |
|---|---|---|
| `hostinger-hosting` | `hostinger-hosting-mcp` | Hosting compartido, sitios |
| `hostinger-domains` | `hostinger-domains-mcp` | Dominios, portfolio, disponibilidad |
| `hostinger-dns` | `hostinger-dns-mcp` | Zonas y records DNS |
| `hostinger-billing` | `hostinger-billing-mcp` | Suscripciones, facturación |
| `hostinger-reach` | `hostinger-reach-mcp` | Email marketing (Reach) |
| `hostinger-vps` | `hostinger-vps-mcp` | VPS, máquinas virtuales |
| `hostinger-ecommerce` | `hostinger-ecommerce-mcp` | Tiendas, productos, órdenes |

El paquete `hostinger-api-mcp` también trae `agency-hosting`, `horizons`, `mail` y
`wordpress`, más un `hostinger-api-mcp` que los junta todos en un solo servidor.

## Notas

- **Variable de entorno:** `HOSTINGER_API_TOKEN`. Es la única que lee el paquete.
- **Dónde queda la config:** `~/.claude.json`, en la clave `mcpServers` de nivel raíz
  (scope `user`). No confundir con `mcpServers` dentro de `projects.<ruta>`, que es
  scope `local` y aplica a un solo proyecto.
- **Hosts que usa:** `developers.hostinger.com` (API), más `auth.hostinger.com`,
  `hpanel.hostinger.com` y `api.mail.hostinger.com`. En entornos con política de red
  restrictiva (por ejemplo Claude Code on the web) esos hosts pueden estar bloqueados:
  los servidores levantan y conectan igual, pero cada llamada real a la API falla.
  En una máquina local no hay ese problema.
- **El token no va acá.** Ni en este archivo ni en el `.sh`. Se pasa por variable de
  entorno al correr el script.
