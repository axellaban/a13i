# Arquitectura de sitio — a13i-partner

Repo `axellaban/a13i`. Deploy `a13i-partner.vercel.app`. Rol: DFY + lead magnets.

## Rutas

```
/                → conversión: casos + bio + aplicación + Calendly (portada)
/calculadora     → lead magnet 1, solo por link directo
/ops-canvas      → lead magnet 2, solo por link directo
/quick-wins-ai   → lead magnet 3, solo por link directo (agregado 2026-07-05)
/thankyou        → post-agenda
wa-redirect.html → invisible: arma el mensaje de WhatsApp y dispara webhook n8n
```

## Estado del root (verificado en producción 2026-07-04)

Kicker de ICP arriba del H1 ("Implementación de IA para dueños de eCommerce con equipo operativo"), eyebrow `A13I · Sesión de Mapeo Operativo`, un solo CTA (sin barra superior), link a la calculadora dentro del bloque de aplicación con framing de preparación pre-llamada, anclaje de valor ("la sesión es la primera fase del programa y la hago yo directamente"), línea de capacidad sin promesa vaga ("cuatro operaciones por mes, es lo que permite estar adentro de cada una"), doble descalificación (por caso de uso y por perfil builder), title y metas orientados a "Implementación de IA para operaciones de eCommerce", root indexable (noindex solo en `/thankyou` y `wa-redirect`). Los casos se muestran con la regla de atribución de `02`.

## Lead magnet 3 — `/quick-wins-ai` (agregado 2026-07-05, corregido dos veces el mismo día)

El documento (32 iniciativas de IA para eCommerce en LATAM: 4 verticales × 4 áreas × quick win/big swing, con métrica de impacto, stack recomendado y riesgo principal) se entrega en **PDF, a mano, por WhatsApp**. No es un tool que calcula ni un contenido que se revela en la página.

El PDF ya existe: `a13i-partner/quick-wins-ai-documento.pdf` (9 páginas, generado con WeasyPrint). El script que lo genera está en `a13i-partner/docs/quick-wins-ai-documento-build.py` — corre standalone (`python3 quick-wins-ai-documento-build.py`, requiere `pip install weasyprint`) y regenera el PDF a partir de un diccionario `MATRIX` con las 32 iniciativas hardcodeadas en el propio script. Para editar el contenido del documento (títulos, métricas, stack, riesgo) se edita ese script, no el sitio.

Flujo de la página: paso 1 pide la vertical (grid de 4 tarjetas, sin tag de versión V1-V4, solo nombre y descripción). Paso 2 pide **nombre de la empresa** y **facturación anual aproximada** (select con 5 rangos), ambos obligatorios. **No pide nombre de la persona ni WhatsApp como campos del formulario** — Axel decidió sacarlos el 2026-07-05 porque son redundantes: al abrir WhatsApp para mandar el mensaje, el número del lead ya queda expuesto del lado de Axel sin necesidad de pedirlo antes. Al enviar, arma el mensaje de WhatsApp con empresa + vertical + facturación y redirige a `wa-redirect.html`. Axel manda el PDF manualmente por WhatsApp después de recibir el mensaje.

`wa-redirect.html` lee `sessionStorage.a13i_lm_source` para atribuir la `fuente` del webhook (en vez de asumir siempre `'ops-canvas'`), y reenvía `empresa`, `facturacion` y `vertical` como campos propios del payload del webhook, no solo dentro del texto del mensaje. Como ya no se recolectan nombre ni WhatsApp del lead en esta página, esos dos campos del payload llegan vacíos cuando la fuente es `quick-wins-ai` — es esperado, no un bug. `ops-canvas.html` no fue tocado y sigue cayendo en el fallback (`fuente: 'ops-canvas'`) porque no setea `a13i_lm_source`.

## Pendientes técnicos

1. **Webhook n8n del formulario de aplicación del root.** Sin esto, cada aplicación enviada se pierde. Prioridad máxima del sitio.
2. Webhook n8n de `calculadora-whatsapp.html` si esa versión se activa, alineando las keys de sessionStorage (`a13i_nombre`, `a13i_wa`, `a13i_ahorroMes`, `a13i_ahorroAnual`, `a13i_fuente`) con lo que lee `wa-redirect.html`.
3. Auditoría de terminología en `/calculadora`, `/ops-canvas`, `/quick-wins-ai` y `/thankyou`: "AI" → "IA", sacar "gratis/gratuita", revisar titles y metas.
4. Footer: `axellaban@gmail.com` → email de dominio propio.
5. og:image para previews en WhatsApp y LinkedIn (fondo oscuro, kicker de ICP como texto). `/quick-wins-ai` reutiliza el og-image genérico existente; no se generó uno específico.
6. Dominio viejo (funnel optin → calculadora ROI), si sigue publicado: redirect 301 hacia acá.
7. `/quick-wins-ai` no tiene webhook propio de "primer touch" (no llama a `kona-optin` al cargar, a diferencia de `calculadora.html`). Solo dispara webhook al llegar a `wa-redirect.html` tras el lead form. Si se quiere trackear vistas sin conversión, falta agregarlo.

## Nota técnica

web_fetch sobre deploys de Vercel devuelve solo texto parseado, sin CSS ni imágenes. Para revisión visual hace falta screenshot, HTML/CSS crudo o acceso al repo.
