# A13I Partner — DFY + Lead Magnets

Sitio de conversión y lead magnets para el programa DFY de A13I (Sistema de Autonomía Operativa). Repo `axellaban/a13i`. Deploy `a13i-partner.vercel.app`. HTML estático, sin build, sin framework. Contexto de negocio completo en `../README.md` y `../01-estrategia.md` a `../05-decisiones.md` (raíz del proyecto); este README es solo la guía técnica de este repo.

## Páginas

- `sesion.html` (root `/`) — página de conversión: casos + bio + bloque de aplicación + Calendly inline. Es la página que recibe el tráfico principal.
- `calculadora.html` (`/calculadora`) — lead magnet 1, Calculadora de Costo Operativo. Solo alcanzable por link directo.
- `ops-canvas.html` (`/ops-canvas`) — lead magnet 2, Ops Canvas para eCommerce. Solo alcanzable por link directo.
- `quick-wins-ai.html` (`/quick-wins-ai`) — lead magnet 3, Mapa de Oportunidades de IA (32 iniciativas, 4 verticales × 4 áreas). La página solo pide vertical, nombre de la empresa y facturación, y lo manda a WhatsApp con esos datos. El PDF (`quick-wins-ai-documento.pdf`, en la raíz de este repo) lo manda Axel a mano por WhatsApp después. Solo alcanzable por link directo.
- `thankyou.html` (`/thankyou`) — página post-agenda, con el mismo bloque de formulario + Calendly que `sesion.html`.
- `wa-redirect.html` — invisible, sin ruta propia: arma el mensaje de WhatsApp con los datos de la calculadora y dispara el webhook antes de abrir `wa.me`.
- `optin.html` — stub de redirect a `calculadora.html` (compatibilidad con links viejos, no es parte del funnel activo).

## Flujo real

```
Contenido / Ads → sesion.html (aplicación + Calendly)
Lead magnets (calculadora / ops-canvas) → wa-redirect.html → WhatsApp → sesion.html o thankyou.html → Calendly → Llamada
```

No es un funnel lineal de 3 páginas: `sesion.html` y `thankyou.html` corren en paralelo, cada una con su propio bloque de aplicación + Calendly inline.

---

## Setup

### 1. Clonar el repo
```bash
git clone https://github.com/axellaban/a13i
```

### 2. Reemplazar antes de publicar

> **Nota:** proyecto HTML estático. No hay variables de entorno en runtime.
> Los valores de `.env.example` son solo referencia — deben reemplazarse directamente en los HTML.

| Valor a reemplazar | Archivo(s) | Dónde buscarlo |
|---|---|---|
| Meta Pixel ID (`1274224524679737`) | `sesion.html`, `calculadora.html`, `ops-canvas.html`, `quick-wins-ai.html`, `thankyou.html`, `wa-redirect.html` | `fbq('init', '...')` en el `<script>` del `<head>` |
| GA4 Measurement ID (`G-FV5WCTFBC3`) | las 5 páginas | `gtag('config', '...')` en el `<head>` |
| Webhook opt-in / primer touch | `calculadora.html` | `fetch('…/webhook/kona-optin', ...)` |
| Webhook calculadora | `wa-redirect.html` | `fetch('…/webhook/kona-calculadora', ...)` |
| Webhook formulario de aplicación | `sesion.html`, `thankyou.html` | `fetch('…/webhook/kona-form', ...)` |
| Webhook Calendly (UUID) | `sesion.html`, `thankyou.html` | `fetch('…/webhook/6032da9b-...', ...)` |
| URL de Calendly | `sesion.html`, `thankyou.html` | `Calendly.initInlineWidget({ url: '...' })` |
| Número de WhatsApp | `wa-redirect.html` | `const WA_NUMBER = '...'` |

Los nombres de webhook (`kona-optin`, `kona-calculadora`, `kona-form`) son slugs internos heredados del nombre de proyecto original; la marca pública ya es A13I en todas las páginas. Cambiarlos exige tocar los workflows de n8n, no solo el HTML — no se tocó en esta pasada.

### 3. Conectar a Vercel
1. vercel.com → New Project → importar `axellaban/a13i`.
2. **Framework: Other** (sin build step).
3. Root directory: `/`.
4. Deploy.

### 4. Configurar dominio
Vercel → Settings → Domains → agregar dominio propio.

---

## Desarrollo local

```bash
python3 -m http.server 8080
# Abrir http://localhost:8080/sesion.html
```

---

## n8n Workflows

Fuente de verdad: `n8n-workflows/`. Los archivos sueltos `wf_optin.json`, `wf_calc.json`, `wf_form.json`, `wf_calendly.json` en la raíz del repo son versiones más viejas (Jun 29) que no reflejan los cambios de estos workflows; quedaron sin limpiar. Importar siempre desde `n8n-workflows/`.

| Archivo | Ruta webhook | Disparado por |
|---|---|---|
| `wf_1_optin.json` | `/webhook/kona-optin` | `calculadora.html` (primer touch, con UTMs) |
| `wf_2_calculator.json` | `/webhook/kona-calculadora` | `wa-redirect.html` |
| `wf_3_form.json` | `/webhook/kona-form` | `sesion.html`, `thankyou.html` |
| `wf_4_calendly.json` | UUID interno (`6032da9b-...`) | evento `calendly.event_scheduled` en `sesion.html`/`thankyou.html` |

## Skills instaladas (`.agents/skills`, `.claude/skills`)

`deploy-to-vercel`, `frontend-design`, `seo`, `accessibility` — ver `skills-lock.json` para las fuentes.
