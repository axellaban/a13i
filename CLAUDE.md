# CLAUDE.md — A13I Partner

> **⚠️ 2026-07-06: `calculadora.html`, `ops-canvas.html`, `quick-wins-ai.html` and `wa-redirect.html` moved to `axellaban/a13i-accelerator`.** Everything below that references those 4 files as living in this repo is stale — treat it as historical/behavioral documentation of the pages (still accurate for how they work), not as a statement of where they live now. This repo (`a13i-partner`) now only contains `sesion.html`, `thankyou.html`, and the `optin.html` redirect stub (which now points cross-domain to `a13i-accelerator.vercel.app/calculadora`). See `arquitectura-sitio.md` for the up-to-date route list and migration notes.

## Project Overview

**A13I Partner** is the conversion site + lead magnets repo for A13I's DFY program (Sistema de Autonomía Operativa). Spanish-language, static HTML/CSS/Vanilla JS, no build tooling, no package manager, no framework. Deployed to Vercel. Business context (ICP, offer, voice, decisions) lives one level up at `../01-estrategia.md` through `../05-decisiones.md` — read those before making copy or strategy calls here. This file is scoped to the technical/code side of this repo only.

**Real flow (not a linear 3-page funnel):**
```
Contenido / Ads ──────────────────────────► sesion.html (aplicación + Calendly inline)
Lead magnets (calculadora / ops-canvas) → wa-redirect.html → WhatsApp → sesion.html / thankyou.html → Calendly → Llamada
```
`sesion.html` (root `/`) and `thankyou.html` (`/thankyou`) each carry their own application-form + inline-Calendly block; they aren't sequential steps of one path.

**External Integrations:**
- **n8n** (self-hosted at `n8n-n8n.fu6abb.easypanel.host`) — handles all webhook data.
- **Meta Pixel** (`1274224524679737`) — on all 5 HTML pages.
- **Google Analytics 4** (`G-FV5WCTFBC3`, gtag.js) — on all 5 HTML pages.
- **Calendly** (`calendly.com/axellaban/30min`) — inline widget (not just a link) in `sesion.html` and `thankyou.html`, with a `message` listener for `calendly.event_scheduled`.
- **No Vimeo / VSL** — the old video-sales-letter step in `thankyou.html` is gone. Don't assume it's still there.
- **Google Fonts** — Inter (400–900) + JetBrains Mono, loaded on every page.

---

## Repository Structure

```
a13i-partner/
├── sesion.html                 # Root "/": conversion page — casos + bio + aplicación + Calendly inline
├── calculadora.html            # "/calculadora": lead magnet 1, operational cost calculator (~69 KB)
├── ops-canvas.html             # "/ops-canvas": lead magnet 2, Ops Canvas (Impacto×Facilidad matrix, ~50 KB)
├── quick-wins-ai.html          # "/quick-wins-ai": lead magnet 3, static reference doc — 32 AI initiatives (4 verticals × 4 pillars), added 2026-07-05
├── thankyou.html                # "/thankyou": post-agenda page, same form+Calendly pattern as sesion.html
├── wa-redirect.html            # invisible utility: builds the WhatsApp message from sessionStorage, fires webhook, redirects to wa.me
├── optin.html                  # legacy redirect stub → calculadora.html (kept for old links only)
├── arquitectura-sitio.md       # routes, verified prod state, pending items — owned doc, keep in sync with root context
├── assets/
│   ├── axel.jpg, av-01..04.webp   # profile + avatar images
│   └── og-image.jpg               # OG preview image (dark, branded)
├── favicon/
├── n8n-workflows/               # current workflow exports — source of truth
│   ├── wf_1_optin.json
│   ├── wf_2_calculator.json
│   ├── wf_3_form.json
│   └── wf_4_calendly.json
├── wf_optin.json, wf_calc.json, wf_form.json, wf_calendly.json   # OLDER duplicate exports at root (Jun 29, stale) — do not import these
├── whatsapp-scripts/            # 6 manual follow-up templates (see below)
├── vercel.json                  # rewrites + cache headers
├── .env.example                 # reference only, values are hardcoded in HTML
├── skills-lock.json / .agents/skills / .claude/skills   # installed agent skills: deploy-to-vercel, frontend-design, seo, accessibility
├── README.md
└── INSTRUCCIONES_EXPERTAS.md    # manual setup notes, written for the original KONA-branded scaffold — steps are still roughly valid but naming is stale
```

---

## Architecture

### Single-File Pattern
Each HTML page is fully self-contained: `<style>` in `<head>`, `<script>` at the bottom of `<body>`. No external `.css`/`.js` files.

### Page-to-Page Data Flow
No more URL query param handoff. Lead data travels via `sessionStorage`, all keys prefixed `a13i_`:
```
a13i_nombre, a13i_wa, a13i_email, a13i_proceso, a13i_rubro,
a13i_costoAnual, a13i_costoMensual, a13i_recuperable,
a13i_personas, a13i_tasaError, a13i_canvas_msg
```
`calculadora.html` and `ops-canvas.html` write these; `wa-redirect.html`, `sesion.html`, and `thankyou.html` read them. If a page needs to hand off lead data to another, use these keys — don't reintroduce `?wa=` query params.

### Webhook Pattern
```javascript
await fetch('https://n8n-n8n.fu6abb.easypanel.host/webhook/<route>', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ ... })
});
```
Webhook route slugs (`kona-optin`, `kona-calculadora`, `kona-form`) are leftover names from the project's original scaffold, before the A13I rebrand. They are internal identifiers only — no user-facing copy references "KONA" anymore. Changing them requires updating the n8n workflows, not just the HTML.

---

## Design System (verified in code, all 5 HTML pages, 2026-07-05)

This is the **actual current** palette — it does not match the dark theme described in some older project notes. If a request references a dark/red theme for this repo, confirm with Axel before applying it; the live site is a light editorial theme.

### Color Palette
```css
--bg:      #FEFBF2   /* cream/paper page background */
--card:    #FFFFFF
--card-2:  #FDFAF3
--ui:      #F7F0E4
--ui-2:    #F3E7D6
--border:  #EAD9C8
--text:    #1A1410   /* near-black warm */
--muted:   #6B5A4A
--dim:     #8C7A68
--faint:   #B7A692
--accent:  #D4612A   /* burnt orange — CTAs, highlights */
--accent-2:#E15E3F
--green:   #1E8E5A   /* success */
--amber:   #B5790A   /* calculadora/ops-canvas only, mid-severity */
```
`wa-redirect.html` additionally defines `--green-wa: #25D366` for the WhatsApp button.

### Typography
- Body/UI: `Inter` (400–900).
- Labels, chrome, financial figures: `JetBrains Mono` (400–700).
- No Fraunces, no Barlow, no IBM Plex Mono anywhere in this repo's live code.
- Exception: `quick-wins-ai.html`'s `<h1>` uses `Geist` (600–800, loaded from Google Fonts) instead of Inter, to match a13i-accelerator's hero heading exactly (see that page's section below). This is intentional, not a mistake — don't "fix" it back to Inter.

### Layout
Cards with rounded corners, cream card-on-cream-background editorial feel, no dark mode.

---

## calculadora.html — Calculator Logic

Wizard-style form (~69 KB), 7-block cost model.

### Key variables
```javascript
directCost   = baseLabor + errCost                       // annual direct operational cost
grossDirect  = directCost * cobertura * adjComp
netoAnual    = max(0, grossDirect + grossStrategic - opex)
opex         = $600 base + $20 × personas /month, annualized
```

### Zone classification (by `directCost`, `ZONES` array)
| max | class | user-facing label |
|---|---|---|
| 10,000 | `z-elite` | "COSTO BAJO" |
| 25,000 | `z-amateur` | "COSTO MODERADO" |
| 75,000 | `z-sedentario` | "COSTO ALTO" |
| 150,000 | `z-lesionado` | "COSTO MUY ALTO" |
| ∞ | `z-fuera` | "COSTO CRÍTICO" |

CSS class names keep the old gamified naming (`z-elite`, `z-amateur`...) but user-facing copy was changed to plain severity labels — don't rename the classes without checking every page that references them.

---

## quick-wins-ai.html — Mapa de Oportunidades de IA

Lead-qualification page, added 2026-07-05, revised multiple times the same day. **The actual deliverable (a PDF covering 32 AI initiatives across 4 verticals × 4 áreas) is not part of this repo.** Axel builds and sends that PDF manually over WhatsApp after the lead comes in — do not generate, store, or maintain that PDF here. This page's only job is to qualify the lead and hand them off to WhatsApp with useful structured data — do not add a step that reveals the document's content on-page; an earlier version did that and it was deliberately reverted (see `05-decisiones.md`).

Flow (3 steps, changed 2026-07-06 — the old 2-field/2-step version is gone): step 1 asks which vertical the business is in (radio-card grid, `selectVertical()` — cards show name only, no description/tag, trailing `→` arrow). Step 2 asks facturación anual aproximada as a single-column radio-card grid (`selectFacturacion()`, `FACTURACIONES`, 5 fixed ranges — same interaction pattern as step 1, not a `<select>` anymore). Step 3 is the contact form: nombre de la empresa (`bizEmpresa`), tu nombre (`leadNombre`), tu correo (`leadEmail`), tu WhatsApp (`leadWaCode` country-code select + `leadWaNumber`) — no Instagram field. Axel explicitly reversed the 2026-07-05 "no name/WhatsApp field" decision on 2026-07-06 to match a benchmark funnel (Arcadia); name/email/WhatsApp are collected again. `submitLead()` validates all of step 3's fields, builds the WhatsApp message via `buildWaMessage()`, and redirects to `wa-redirect.html`.

**No back/continue buttons, no persistence** (changed 2026-07-06): steps 1 and 2 auto-advance (`setTimeout(nextStep, 260)`) as soon as a card is clicked — there is no "← Atrás" or "Continuar" button anywhere on this page, only the final submit CTA on step 3 ("Recibir mi mapa gratis →"). There is also no `localStorage`/`sessionStorage`-based step persistence — refreshing the page always restarts at step 1. Both were deliberate, explicit calls from Axel; don't reintroduce a back button or a save/restore mechanism without asking first.

**H1 underline/highlight** (changed 2026-07-06): matches a13i-accelerator's hero exactly by using the same library it uses under the hood — [rough-notation](https://github.com/rough-stuff/rough-notation), loaded via `<script src="https://unpkg.com/rough-notation@0.5.1/lib/rough-notation.iife.js">` (pin this version; don't switch to an unpinned `@latest` URL). `#hlUnderline`/`#hlHighlight` spans are annotated on load with the accelerator's exact params (underline: `#D4612A`, strokeWidth 2, 2 iterations; highlight: `rgba(225,94,63,0.22)`, strokeWidth 1, padding 4). If `window.RoughNotation` fails to load (CDN down, ad-blocker), the init function no-ops silently — text stays fully readable, just without the animated decoration. This replaced the old hand-coded SVG `stroke-dasharray` underline animation (that hand-rolled version is gone from this file; sesion.html still uses it and was not touched).

**Value bullets + legal footer** (changed 2026-07-06): the `<ul class="value-bullets">` (3 benefit lines) moved out of step 1 and now sits after all three `.step` divs, so it's visible on every step, not just step 1. The `<footer>` was expanded from a bare "© 2026 A13I" line into a full legal block modeled on the Arcadia benchmark: a data-usage consent paragraph, a divider, a results-disclaimer paragraph, the copyright line, and a "Privacidad • Términos • Cookies" row. **Those three links are plain text, not `<a>` tags** — this repo has no `/privacidad`, `/terminos`, or `/cookies` pages, so linking them would 404. Wire them up if/when those pages exist.

`sessionStorage` handoff: sets `a13i_empresa`, `a13i_nombre`, `a13i_email`, `a13i_wa` (country code + digits, no spaces/punctuation), `a13i_facturacion`, `a13i_vertical` (also mirrored into `a13i_rubro` for `wa-redirect.html`'s generic fallback path), `a13i_canvas_msg` (read by `wa-redirect.html`'s `buildMessage()`), and `a13i_lm_source = 'quick-wins-ai'`. `wa-redirect.html` forwards `empresa`, `facturacion`, `vertical`, and now `email` as their own fields in the n8n webhook payload (`nombre`/`wa` were already forwarded generically, previously always empty for this source — now populated).

`VERTICALS` (4 items: moda, retail, cpg, travel) and `FACTURACIONES` (5 fixed USD/year ranges) are the only content arrays left in this file — both just `{id, name}`, no description/tag fields. The 32-initiative content itself (title/desc/metric/stack/risk per vertical × área) does not live in this repo at all — it's a document Axel maintains and sends separately. Never re-add that matrix to this HTML file or generate a PDF for it here.

---

## Development Workflow

```bash
python3 -m http.server 8080
# then visit http://localhost:8080/sesion.html
```
Push to `main` → Vercel auto-deploys. No test suite, no linter — match existing style by convention.

---

## Environment Variables (`.env.example`, reference only)

| Variable | Current value | File(s) |
|---|---|---|
| `META_PIXEL_ID` | `1274224524679737` | all 5 HTML files |
| `WEBHOOK_URL_OPTIN` | `…/webhook/kona-optin` | `calculadora.html` |
| `WEBHOOK_URL_CALCULADORA` | `…/webhook/kona-calculadora` | `wa-redirect.html` |
| `WEBHOOK_URL_FORMULARIO` | `…/webhook/kona-form` | `sesion.html`, `thankyou.html` |
| `CALENDLY_URL` | `https://calendly.com/axellaban/30min` | `sesion.html`, `thankyou.html` |

(`VIMEO_VIDEO_ID` no longer applies — removed from the funnel.)

---

## Meta Pixel & GA4 Events

| Page | Events |
|---|---|
| `calculadora.html` | `PageView`, `Lead`, `CalculadoraIniciada`, `ClickBotonWA`, `CalculadoraResultadosVistos` |
| `ops-canvas.html` | `PageView`, `OpsCanvasWhatsApp` |
| `quick-wins-ai.html` | `PageView`, `QuickWinsVerticalSelected`, `QuickWinsFacturacionSelected`, `QuickWinsLeadSubmit`, `Lead` |
| `sesion.html` | `PageView`, `FormularioEnviado`, `CalendarioMostrado`, `ClickCalendly`, `LlamadaAgendada` |
| `thankyou.html` | `PageView`, `FormularioEnviado`, `CalendarioMostrado`, `ClickCalendly`, `LlamadaAgendada` |
| `wa-redirect.html` | `PageView`, `WARedirectPageView`, `ClickBotonWA`, `CountdownCompletado` |

Every `fbq('trackCustom', ...)` has a matching `gtag('event', ...)` call with a snake_case name.

---

## WhatsApp Follow-up Scripts (`whatsapp-scripts/`, 6 files, manual — not automated)

- `00-triage-respuesta.txt` — first reply script when a lead's WhatsApp comes in with calculator data.
- `01-el-fantasma.txt` — left WhatsApp at opt-in but never finished the calculator. Wait 2–4h.
- `02-el-asustado.txt` — saw their number, went quiet/scared. References a "6 min video" — stale, no video currently lives in `thankyou.html`; check before sending.
- `02-no-envio-wa.txt` — reached `wa-redirect.html` (webhook fired) but never actually sent the WhatsApp message. Wait 1–2h, message manually using the number captured in the webhook.
- `03-el-indeciso.txt` — sent WhatsApp data but never replied to triage. Send once, 48h later, no follow-up after.
- `04-el-agendado.txt` — call booked. Confirmation + pre-call case study link.

These are manual send templates, not n8n-automated messages — `[nombre]`, `[monto]`, `[proceso]`, `[día]`/`[hora]` are filled in by hand from the n8n sheet/webhook data.

---

## Key Conventions to Follow

1. No build tooling — plain HTML/CSS/JS only.
2. Single-file pages — CSS in `<style>`, JS in `<script>`, no separate asset files unless asked.
3. CSS variables for theming — use the palette above, never hardcode hex inline.
4. Spanish content throughout.
5. Vanilla JS — `fetch`, `async/await`, `sessionStorage`, standard DOM APIs. No frameworks.
6. Webhook calls wrapped in `try/catch` with a user-visible failure message.
7. Meta Pixel + GA4 fire together on every meaningful event — keep both in sync when adding one.
8. Lead-data handoff between pages goes through `sessionStorage` (`a13i_*` keys), not query params.
9. No test suite, no linter — match existing style by convention.

---

## Git

Production branch: `main`. Working tree is normally clean; ignore the many zero-byte `*.lock.bak*`/`*.lock.pre_*` files under `.git/` — leftovers from an external backup tool, not real git locks.
