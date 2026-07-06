# A13I Partner — DFY + Lead Magnets

Sitio de conversión y lead magnets para el programa DFY de A13I (Sistema de Autonomía Operativa). Repo `axellaban/a13i`. Deploy `a13i-partner.vercel.app`. HTML estático, sin build, sin framework. Contexto de negocio completo en `../README.md` y `../01-estrategia.md` a `../05-decisiones.md` (raíz del proyecto); este README es solo la guía técnica de este repo.

## Páginas

- `sesion.html` (root `/`) — página de conversión: casos + bio + bloque de aplicación + Calendly inline. Es la página que recibe el tráfico principal.
- `thankyou.html` (`/thankyou`) — página post-agenda, con el mismo bloque de formulario + Calendly que `sesion.html`.
- `optin.html` — stub de redirect (compatibilidad con links viejos) que ahora apunta cross-domain a `https://a13i-accelerator.vercel.app/calculadora`, ya que la calculadora se mudó a ese repo (ver abajo).

> **2026-07-06 — Lead magnets migrados a `a13i-accelerator`.** `calculadora.html`, `ops-canvas.html`, `quick-wins-ai.html` y `wa-redirect.html` (con sus assets `av-01..04.webp`) se movieron al repo `a13i-accelerator` (`axellaban/a13i-accelerator`, deploy `a13i-accelerator.vercel.app`) para alinear el funnel con lo documentado en `02-oferta.md`: contenido gratis → lead magnet → DWY (accelerator) → DFY (este repo, partner). `sesion.html` linkea a la calculadora con la URL absoluta `https://a13i-accelerator.vercel.app/calculadora`; `wa-redirect.html` (ahora en accelerator) linkea de vuelta a este repo con `https://a13i-partner.vercel.app/`. `axel.jpg` y `og-image.jpg` siguen viviendo en ambos repos (se duplicaron) porque `sesion.html`/`thankyou.html` también los usan.

## Flujo real

```
Contenido / Ads → lead magnets (a13i-accelerator) → wa-redirect.html (accelerator) → WhatsApp → sesion.html o thankyou.html (este repo) → Calendly → Llamada
```

`sesion.html` y `thankyou.html` corren en paralelo, cada una con su propio bloque de aplicación + Calendly inline.

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
| Meta Pixel ID (`1274224524679737`) | `sesion.html`, `thankyou.html` (y las páginas movidas a `a13i-accelerator`) | `fbq('init', '...')` en el `<script>` del `<head>` |
| GA4 Measurement ID (`G-FV5WCTFBC3`) | `sesion.html`, `thankyou.html` (y las páginas movidas) | `gtag('config', '...')` en el `<head>` |
| Webhook opt-in / primer touch | `calculadora.html` (ahora en `a13i-accelerator`) | `fetch('…/webhook/kona-optin', ...)` |
| Webhook calculadora | `wa-redirect.html` (ahora en `a13i-accelerator`) | `fetch('…/webhook/kona-calculadora', ...)` |
| Webhook formulario de aplicación | `sesion.html`, `thankyou.html` | `fetch('…/webhook/kona-form', ...)` |
| Webhook Calendly (UUID) | `sesion.html`, `thankyou.html` | `fetch('…/webhook/6032da9b-...', ...)` |
| URL de Calendly | `sesion.html`, `thankyou.html` | `Calendly.initInlineWidget({ url: '...' })` |
| Número de WhatsApp | `wa-redirect.html` (ahora en `a13i-accelerator`) | `const WA_NUMBER = '...'` |

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
