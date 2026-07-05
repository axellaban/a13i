> **Nota de estado (2026-07-05):** este documento es un draft de planning histórico (v4) que explora un modelo de pricing gain-share ("cobramos del ahorro que generamos") para el DFY. Se movió acá desde `a13i-accelerator/docs/` porque describe la landing y el pricing de `a13i-partner`, no del programa DWY. **No coincide con el modelo de pricing vigente en `02-oferta.md`**, que describe un precio fijo no público para el Sistema de Autonomía Operativa, sin fee variable atado a ahorro verificado. No se resolvió cuál de los dos modelos rige hoy — es una decisión de pricing pendiente de Axel, no algo que se infiera del código o del contexto existente. Se conserva como referencia de la mecánica de Diagnóstico de Ahorro pago + partner fee, por si se retoma ese modelo.

# A13I PARTNER — Calculadora de Deuda Operativa (v4)

**El cambio de fondo vs. v3:** ya no vendemos "un plan de IA" genérico. A13I es un **AI Partner**: elegimos con quién trabajamos y cobramos del ahorro que generamos, no de la caja del cliente.

**Lo que recibe el prospecto (framing Arcadia, motor propio):** el entregable es un activo aspiracional — el **Plan de Autonomía Operativa**: tu Índice de Autonomía (0–100), tu posición en el mapa, y las fases exactas para subir. Por debajo corre el motor riguroso (4 dimensiones puntuadas + cálculo de deuda), pero la deuda NO es el regalo: es la urgencia, y aparece después del plan como "el costo de quedarte donde estás". Nadie comparte su deuda; el índice y el plan, sí.

---

## 0. El modelo A13I Partner

### El claim

**"Cobramos del ahorro que generamos, no de tu caja."**

Regla permanente: nunca decir "gratis". La implementación "no sale de tu caja" — sale del ahorro. Gratis atrae al peor cliente y devalúa lo que después cobrás por resultados.

### Cómo se cobra (modelo híbrido)

| Paso | Qué es | Precio |
|---|---|---|
| 1 · Diagnóstico de Ahorro | 5-10 días. Valida los números de la calculadora con datos reales, fija el **baseline contractual** y entrega el plan con ROI estimado. | USD 300–500, se descuenta del deal |
| 2 · Implementación | Construimos el sistema sobre su operación. | USD 0 de su caja |
| 3 · Partner fee | % del ahorro mensual **verificado** contra el baseline. | 25% × 12 meses |

**Cláusulas no negociables (van en el contrato, no en la landing):**
1. **Definición escrita de "ahorro"** en el Diagnóstico: horas de equipo documentadas × costo hora + costos duros eliminados (software, retrabajos, errores). Las horas del founder entran al deal solo si se acuerda su valor en el Diagnóstico. La calculadora pública usa costo de oportunidad (marketing honesto); el contrato usa ahorro verificable (cobro).
2. **Medición automática mensual** vía dashboard (n8n/BI — tu diferencial). El cliente ve el mismo número que vos. Sin dashboard no hay deal.
3. **Fee mínimo mensual si el cliente no implementa lo acordado** (no adopta, no da accesos, no asiste a las revisiones). Protege del modo de fallo clásico del gain-share: sistema instalado que nadie usa.
4. **Techo opcional** de fee total para clientes nerviosos — cede upside, acelera la firma. Usalo solo si traba el cierre.

### Jugada de apertura: los primeros 3–5 clientes

Elegidos a dedo, en modo casi-puro-éxito: Diagnóstico pago + 30% del ahorro (sin más upfront). No es generosidad — es comprar los casos documentados que hoy no tenés, con medición contractual desde el día 1. Cada uno sale con: métrica antes → después, dashboard como evidencia y cita del dueño.

### ICP (sin cambios vs. v3, ahora con un filtro más)

Founder LATAM, operación real, equipo 2+, USD 100K+ anual. **Filtro nuevo del modelo partner: solo entra quien tiene ahorro medible y grande** (volumen repetitivo alto + costo hora identificable). El sorting por rango se mantiene: <100K nurture · 100–300K prioridad · 300K–1M prioridad máxima · +1M Axel entra directo.

### El funnel completo

```
Contenido / ads → 6 PREGUNTAS (este lead magnet) → Plan de Autonomía: índice + mapa + plan por fases (+ el costo de quedarse)
    → agenda Sesión de Mapeo Operativo (sin costo, 45 min, con aplicación)
        → Diagnóstico de Ahorro (USD 300–500, fija baseline)   ← acá se filtra en serio
            → A13I Partner deal (25% del ahorro verificado × 12 meses)
    → no agenda → 5 emails con SU número + retargeting
```

### Economics — por qué este modelo te cambia el negocio

Ejemplo con los defaults de la calculadora: cliente 100–300K al que le recuperás USD 2.400/mes de ahorro verificado → tu fee: **USD 600/mes × 12 = USD 7.200/año por cliente** (el cliente se queda con 1.800/mes: la venta se defiende sola). Con solo 4 deals activos: ~USD 2.400/mes recurrentes y creciendo. El híbrido convierte a A13I de vender proyectos a **facturación recurrente atada a resultados** — y cada deal fabrica su propio caso de éxito con dashboard como prueba.

---

## 1. Landing (estructura calcada de plan.arcadiamedia.io, pieza por pieza)

**Arriba de todo — prueba compacta:** {3-4 fotos de clientes} + "+{N} dueños de negocio ya tienen su plan" *(slot: arrancá sin contador; se agrega cuando el número sea real)*.

**Headline:**

**Recibí gratis tu Plan de Autonomía Operativa: qué sistemas de IA implementar para recuperar 20+ horas por semana de tu operación... en menos de 60 segundos.**

*(Anatomía Arcadia: entregable con nombre + resultado soñado con número + intervalo. Su "$1M USD" acá es tiempo: para un dueño, las horas SON la plata — y el 20+ sale de la propia matemática de la calculadora, no del aire.)*

**Mockup del plan como imagen** — el mapa de tramos + índice + fases, visible ANTES de contestar nada. El prospecto ve el artefacto que va a recibir. Arcadia hace exactamente esto y es la pieza que más pre-vende.

**Primera pregunta embebida en la landing** (contestar ES empezar — cero fricción):
"¿Cuántas horas por día estás VOS metido en la operación?" → 4 botones.

**Bullets de valor** (sección 3) + footer legal + pixel Meta/Google — la página nace lista para ads.

*(Variantes A/B de headline en "Notas para vos". Se lanza con esta.)*

## 2. La Calculadora (6 preguntas, todas en rangos — nunca campos libres)

Orden pensado para completar: arranca por el espejo (fácil, personal), la facturación va ÚLTIMA — cuando ya está invertido.

| # | Pregunta | Opciones | Alimenta |
|---|---|---|---|
| 1 | ¿Cuántas horas por día estás VOS metido en la operación (responder, aprobar, revisar, apagar incendios)? *(embebida en la landing)* | Menos de 1 / 1–3 / 3–5 / +5 | **Cálculo (horas dueño)** + dimensión Equipo |
| 2 | ¿Cuántas personas trabajan en tu negocio, contándote? | Solo yo / 2–4 / 5–10 / +10 | Contexto Equipo + branch de P3 |
| 3 | ¿Cuántas veces por día tu equipo te consulta algo que ya contestaste antes? *(branch: si P2 = "solo yo" → "¿cuántas consultas repetidas de clientes respondés por día?")* | Casi nunca / 1–5 / 5–15 / +15 | **Cálculo (interrupciones)** + dimensión Decisiones |
| 4 | ¿Dónde vive la información clave de tu operación? | En mi cabeza y chats de WhatsApp / Repartida en planillas y mails que no se conectan / En sistemas (CRM-ERP) pero cargados a mano / En sistemas conectados entre sí | Dimensión Datos |
| 5 | Cuando alguien nuevo entra al equipo, ¿cómo aprende el trabajo? | Mirando y preguntando, no hay nada escrito / Documentos sueltos / Hay manuales-SOPs pero se ejecutan a mano / Los procesos corren en sistemas, la persona supervisa | Dimensión Procesos |
| 6 | ¿Cuánto factura tu negocio por año? (USD o equivalente) | <100K / 100–300K / 300K–1M / +1M | Calificación + tarifa horaria + benchmark |

### Scoring de dimensiones (0–3 cada una)

- **Datos** ← P4 (opción 1 = 0 … opción 4 = 3)
- **Decisiones** ← P3 invertida (+15 = 0 … casi nunca = 3)
- **Procesos** ← P5 (opción 1 = 0 … opción 4 = 3)
- **Equipo** ← P1 invertida (+5 hs/día del dueño en operación = 0 … menos de 1 = 3)

**Cuello de botella = la dimensión con menor puntaje.** Empate: desempata en este orden — Decisiones > Datos > Procesos > Equipo (Decisiones es donde el ahorro se verifica más rápido; el desempate va hacia donde la plata aparece antes). Etiquetas: 0–1 crítico · 2 en transición · 3 resuelto.

### El Índice de Autonomía Operativa (la cara del resultado)

**Índice = (Datos + Decisiones + Procesos + Equipo) ÷ 12 × 100.**

| Tramo | Índice | Nombre (el espejo) |
|---|---|---|
| 1 | 0–25 | Todo Pasa por Vos |
| 2 | 26–50 | Interviniendo en Todo |
| 3 | 51–75 | Procesos sin Sistema |
| 4 | 76–100 | A un Paso de la Autonomía |

Los 4 nombres-espejo de la escalera vuelven acá — pero como **lecturas del índice, no como diagnóstico**. La escalera no te cerraba porque etiquetaba con una sola pregunta de autopercepción; el tramo sale de 4 dimensiones puntuadas. Mismo efecto espejo + progresión de Arcadia, motor defendible. Ejemplo verificado: perfil Datos 1 + Decisiones 1 + Procesos 2 + Equipo 1 = 5/12 → **índice 42 → Tramo 2 · Interviniendo en Todo**.

### Fórmula de la deuda (transparente — se muestra al usuario, ES el rigor)

```
Horas tuyas/mes   = punto medio de P1 × 22 días hábiles
Horas equipo/mes  = punto medio de P3 × 10 min por interrupción × 22
Deuda mensual     = (horas tuyas × tarifa founder del rango) + (horas equipo × USD 10)
Deuda anual       = deuda mensual × 12
```

Tarifas founder por rango (costo de oportunidad conservador, editable): <100K → 25/h · 100–300K → 50/h · 300K–1M → 80/h · +1M → 120/h. Tarifa equipo default: USD 10/h LATAM.

**Ejemplo verificado** (rango 100–300K, horas dueño = 3–5, consultas = 5–15): 4 hs × 22 = 88 hs tuyas (USD 4.400) + 10 consultas × 10 min × 22 = ~37 hs de equipo (USD 370) → **~USD 4.770/mes ≈ USD 57.000/año.**

**La jugada de honestidad (clave):** el reporte dice — *"No todo esto es automatizable. Aunque solo la mitad lo sea, son ~USD 28.500 al año que hoy no vuelven."* Recortarle el número al lector antes de que lo haga él sube la credibilidad de todo lo demás.

## 3. El valor (3 frases, formato Arcadia)

- Recibí tu plan personalizado en menos de 60 segundos — con tu índice, tu mapa y tus fases
- Calculado sobre TUS datos con la fórmula a la vista — no un score misterioso ni teoría de gurú
- 100% gratuito, acceso instantáneo. El plan es tuyo, hagas lo que hagas después

---

## 4. Página de resultado — estructura (una por cuello de botella = 4 variantes)

1. **PORTADA — Tu Índice y el mapa** (lo primero que ve, aspiracional): "Tu negocio corre solo al 42%" + la barra de 4 tramos con "▶ ESTÁS ACÁ · Tramo 2 · Interviniendo en Todo" y su rango de facturación. El efecto espejo + progresión de Arcadia, con motor propio.
2. **Tu perfil en 4 dimensiones** (barras: Datos, Decisiones, Procesos, Equipo) + benchmark del rango.*
3. **Tu cuello de botella** (título grande): "Tu freno no es la tecnología. Es {dimensión}." + el bloque táctico de esa dimensión (sección 5).
4. **TU PLAN — qué hacer y en qué orden** (sección 5bis): las fases para subir de tramo. El regalo — el corazón de la página.
5. **El costo de quedarte donde estás** (recién acá aparece la deuda, como urgencia — nunca como titular): "Mientras tanto, esto se lleva ~88 horas tuyas por mes ≈ USD 57.000 al año." + desglose de 3 líneas con la fórmula a la vista + la línea de honestidad (mitad automatizable).
6. **Tu dimensión más fuerte** (1 línea — la palanca: "Tus {X} ya están listos; el plan se apoya ahí").
7. **La división del trabajo** (sección 5ter): nosotros los sistemas de IA — vos la estrategia y el criterio.
8. **La prueba** — caso real del rango (mismo sistema de slots de v3: rubro · proceso · antes → después · cita; fallback actual mientras no haya casos).
9. **Quién está detrás** (3 líneas + foto, igual que v3).
10. **Cómo trabajamos** (sección 6 — el modelo partner).
11. CTA + form de aplicación (sección 7).
12. Para quién NO es (sección 8).

\* Benchmark v1 honesto: "promedio de las operaciones que analizamos" cuando N>50 calculadoras; hasta entonces, sin benchmark — no inventar curvas.

*(Modulación por intento previo: se eliminó la P3 vieja del quiz, pero el form de agenda la captura — el mensaje modulado pasa al mail de confirmación y a la apertura de la sesión.)*

---

## 5. Los 4 cuellos de botella (contenido táctico — recut de lo mejor de v3)

### CUELLO DE BOTELLA · DATOS — "Tu operación no recuerda nada"

**Por qué es tu freno:** tu negocio genera información todo el tiempo (WhatsApp, mail, planillas, CRM si hay), pero vive repartida entre herramientas que no se hablan. Cada dato se usa una vez y se pierde — y alguien lo vuelve a cargar a mano.

**Esta semana:**
1. Contá cuántas herramientas distintas atraviesa UNA tarea de punta a punta (un pedido: WhatsApp → Excel → facturación).
2. Marcá en qué punto se pierde información o se duplica carga manual — ahí está el costo real.
3. Identificá las 3 fuentes de datos que más se repiten en tus decisiones diarias y dónde vive cada una.

**Qué NO hacer:** comprar un ERP nuevo ni centralizar todo. Necesitás que los sistemas que YA tenés compartan un mismo dato — conectar, no reconstruir.

> **Tu mantra:** "El dato que se carga dos veces se paga tres veces."

### CUELLO DE BOTELLA · DECISIONES — "Todo lo repetitivo lleva tu firma"

**Por qué es tu freno:** las decisiones chicas y repetitivas necesitan tu aprobación. Cada persona que contratás hereda tu forma de trabajar pero no tu criterio — así que te sigue preguntando a vos. El cuello de botella no es el volumen de trabajo: son tus interrupciones.

**Esta semana:**
1. Listá las 5 preguntas que tu equipo te hace más seguido.
2. Marcá cuáles tienen SIEMPRE la misma lógica (si pasa X, hacé Y) — esas se automatizan primero.
3. Documentá las últimas 10 consultas de un mismo rol: 7 u 8 van a tener la misma respuesta. Ese es el insumo directo.

**Qué NO hacer:** automatizar decisiones que necesitan tu criterio real. Si no podés escribir la regla, no está lista para IA — y está bien que siga en tus manos.

> **Tu mantra:** "No se trata de automatizar todo. Se trata de sacarte de las 2-3 decisiones que más se repiten."

### CUELLO DE BOTELLA · PROCESOS — "Documentado no es automático"

**Por qué es tu freno:** tenés manuales, checklists, un Notion ordenado. Desde afuera parece madurez — pero cada proceso todavía necesita que una persona lo ejecute paso a paso, todas las veces. Es el freno más subestimado de los cuatro.

**Esta semana:**
1. Elegí el SOP más usado de tu operación (el que más gente consulta por semana).
2. Marcá dónde pide "copiar", "revisar" o "completar a mano" — eso hoy lo hace una persona en lugar de un sistema.
3. Cuantificá cuántas veces por semana se ejecuta a mano. Cuanto más alto, más rápido se paga automatizarlo.

**Qué NO hacer:** arrancar por el proceso más complejo. Arrancá por el que más se repite y menos excepciones tiene. El manual se convierte en el sistema — no en un documento que nadie vuelve a abrir.

> **Tu mantra:** "Un proceso bien documentado es el punto de partida ideal para automatizar, no el destino final."

### CUELLO DE BOTELLA · EQUIPO — "Contrataste capacidad, no autonomía"

**Por qué es tu freno:** pagás sueldos para tener más capacidad, pero la capacidad real no crece porque cada tarea sigue pasando por tu supervisión. Contratar resolvió el volumen, no las decisiones. Es el freno más caro de los cuatro.

**Esta semana:**
1. Antes de la próxima contratación, revisá si el puesto resuelve un cuello de botella real o agrega otra persona esperando tu aprobación.
2. Elegí la tarea repetitiva que tu mejor persona hace más rápido — esa se automatiza primero, porque el estándar ya está definido.
3. Medí cuánto tiempo tuyo (o de un mando medio) se libera por semana. Ese número justifica todo lo demás.

**Qué NO hacer:** contratar a alguien para "sacarte" tareas repetitivas — vas a entrenar a una persona para hacer a mano lo que un sistema sostiene solo.

> **Tu mantra:** "El cuello de botella no era la falta de gente. Era la falta de un sistema que sostuviera las decisiones sin supervisión."

---

## 5bis. TU PLAN — el accionable (se genera con el perfil)

El diagnóstico dice dónde estás. El plan dice exactamente qué hacer y en qué orden, según tu perfil. **Regla de generación: Fase 1 = tu cuello de botella (dimensión más baja) · Fase 2 = tu segunda dimensión más baja · Fase 3 = siempre la misma: tu primer loop.** El orden lo definen tus puntajes — dos negocios con el mismo índice reciben planes distintos. Eso es lo que la escalera no podía hacer.

**La mecánica de progresión (el gancho Arcadia, ahora literal):** cada fase completada sube puntos de una dimensión → tu índice sube → cambiás de tramo. El plan ES el camino al siguiente tramo, y a los 90 días lo re-corrés y lo ves subir. Retención incorporada.

**FASE 1 · Semanas 1–2 — Destrabá {tu cuello de botella}**
Las 3 acciones del bloque de tu cuello (sección 5). Sin tecnología, sin comprar nada: esto lo hacés con tu equipo esta semana. Objetivo: que lo que hoy vive en tu cabeza quede visible y escrito.

**FASE 2 · Semanas 3–4 — Prepará la base: {tu segunda dimensión más baja}**
Las acciones de esa dimensión. Objetivo: terreno firme para que el sistema corra — datos ubicados, reglas escritas, UN proceso elegido.

**FASE 3 · Semanas 5–8 — Tu primer loop**
Acá recién entra la capa de IA: **un agente que ejecuta UNA decisión repetitiva en loop** — lee el dato, decide con TU regla, actúa en la herramienta que tu equipo ya usa, y deriva la excepción a una persona. Uno solo, medido en semanas, con el ahorro visible en un dashboard. Cuando el primer loop corre, el segundo cuesta la mitad.

**El cierre del plan (la línea que eleva):**
*"Fijate lo que NO hay en este plan: vos aprendiendo prompts, comparando herramientas o mirando tutoriales. De los sistemas de IA —los agentes, la arquitectura, los loops— nos encargamos nosotros. Tu trabajo es el que nadie puede hacer por vos: la estrategia y el criterio que forjaste con años de operación. El plan existe para devolverte ahí."*

## 5ter. La división del trabajo (bloque corto, va en las 4 páginas y se repite en la sesión)

**Nosotros:** los sistemas de IA. Los agentes, la arquitectura, las integraciones, el loop de excepciones. Todo lo que suena a chino, clarificado y funcionando.

**Vos:** la estrategia y el criterio que solo da la experiencia. Las decisiones que ningún sistema puede tomar por vos.

*Los 3 términos que vas a escuchar por todos lados, sin humo:*
- **Sistema de IA:** el conjunto —agentes + integraciones + medición— que sostiene una parte de tu operación sin supervisión constante.
- **Agente de IA:** un programa que ejecuta una decisión repetitiva con TU regla, en TUS herramientas. No un chatbot genérico.
- **Loop:** el ciclo que corre solo: entra el dato → el agente decide → actúa → la excepción va a tu equipo. Lo que se sale de la regla siempre termina en una persona.

*(Por qué funciona: los términos señalan competencia técnica, pero el frame le saca al lector la obligación de entenderlos — "para eso estamos nosotros". Autoridad sin carga evaluativa.)*

---

## 6. Bloque "Cómo trabajamos" (va en las 4 páginas de resultado — el modelo, pre-vendido)

**A13I no es una agencia. Es tu AI Partner.**

Trabajamos distinto, y conviene que lo sepas antes de agendar:

**1 · Diagnóstico de Ahorro (5-10 días).** Validamos tu número de la calculadora con datos reales de tu operación y fijamos el baseline: cuántas horas y cuánta plata se van hoy, medido, no estimado. Es pago (USD 300–500) y se descuenta si avanzamos. Es también nuestro filtro: si el ahorro que vemos no justifica el trabajo, te lo decimos ahí y te quedás con el diagnóstico.

**2 · Implementación sin costo de tu caja.** Si avanzamos, diseñamos la arquitectura y construimos el sistema: agentes de IA que ejecutan tus decisiones repetitivas en loop, conectados a las herramientas que tu equipo ya usa. No pagás la implementación — y no necesitás entender la técnica: para eso estamos.

**3 · Cobramos del ahorro.** Nuestro fee es un % del ahorro mensual verificado contra tu baseline, medido por un dashboard que ves vos también. Mismo número para los dos. **Si tu operación no ahorra, no cobramos.**

Por eso elegimos con quién trabajamos: solo aceptamos negocios donde el ahorro es medible y grande. Tu calculadora es el primer paso de esa evaluación — la sesión es el segundo.

---

## 7. CTA — idéntico en las 4 páginas

**El próximo paso es tu Sesión de Mapeo Operativo.**

45 minutos, sin costo, directo con Axel — la misma persona que después implementa. Revisamos tu número real, tu cuello de botella, y si tu operación califica para el modelo partner. Salís con tu plan priorizado aunque no avancemos.

**Tomamos 4 negocios nuevos por mes.** Aplicá acá →

**Form de aplicación** (nota el verbo: se aplica, no se reserva — coherente con elegir clientes):
1. ¿Qué proceso te gustaría sacarte de encima primero? (campo corto)
2. ¿Ya intentaste resolver esto con IA? (Todavía no / Probé sin resultados / Algo funciona pero no escala)
3. ¿Cuántas horas por semana podés dedicarle a implementar? (menos de 1 / 1–2 / 3+)

*(Con las 6 preguntas + este form quedan los 5 datos duros del scoring completos antes de la call: facturación P6, equipo P2, dolor, intento previo, horas.)*

### Value stack de la sesión

**01 · Validación de tu número** *(valor USD 150)* — revisamos tu deuda operativa con tus datos reales, no autopercepción.
**02 · Tu mapa de decisiones y datos** *(valor USD 300)* — las 2-3 automatizaciones de mayor ROI en tu operación, priorizadas por impacto y esfuerzo.
**03 · Veredicto honesto** — si tu operación califica para el modelo partner. Si no, te lo decimos y te quedás con todo lo anterior.
**Bonus por aplicar esta semana: Score de Madurez de IA generado en vivo** *(valor USD 150)* — el diagnóstico de 9 niveles corrido con IA sobre tu operación, delante tuyo, con benchmark de tu rango.

## 8. Para quién NO es (+ manejo de objeción)

**Esto no va a ser la típica llamada de ventas — literalmente: nosotros también estamos evaluando.**

Cobramos del ahorro que generamos. Eso significa que solo nos sirve trabajar con negocios donde el ahorro va a ser real, grande y medible. Si tu operación no está ahí todavía, te lo decimos en la sesión y te llevás el plan igual.

**No apliques si:**
- Todavía no tenés un negocio operando (idea, pre-lanzamiento, validación).
- Buscás un curso de IA. Esto es implementación, no formación.
- No podés dedicarle ni 1 hora por semana — sin tu lado, no hay adopción, y sin adopción no hay ahorro para nadie.

---

## 9. Sistema de seguimiento (ajustado al número)

**9a. Emails post-calculadora (5, con SU número en el asunto):**
- Mail 0 (inmediato): tu Plan de Autonomía completo — asunto: "Tu negocio corre solo al {índice}%" + open loop ("mañana te muestro qué separa a los que suben de tramo de los que no").
- Mail 1 (día 1): la historia de Axel — {slot: el momento concreto en que viste a un dueño real pagar esta deuda sin saberlo}.
- Mail 2 (día 2): caso del rango del lead (slot de la prueba) — antes → después.
- Mail 3 (día 3): la cuenta hacia adelante: "tu deuda son ~USD {X}/mes. En los 12 meses que dura un partner deal, son USD {12X} que no vuelven. Comparalo con lo que cuesta el Diagnóstico."
- Mail 4 (día 5): cierre honesto: "quedan {n} de los 4 lugares del mes."

**9b. Anti no-show:** confirmación con micro-tarea ("traé las 3 preguntas que más te hizo tu equipo esta semana") → WhatsApp 24 h antes con reconfirmación → WhatsApp 1 h antes con link.

**9c. Post-sesión sin cierre (5 pasos):** D+1 resumen con SUS números · D+3 caso relevante · D+7 pregunta directa sobre el proceso que nombró · D+14 última pieza de valor · D+30 breakup suave.

**9d. Retargeting (hizo el plan y no aplicó):** creativo 1 = el mapa de tramos ("¿seguís en el Tramo 2?") · creativo 2 = caso · creativo 3 = CTA directo.

## 10. Distribución — la calculadora ES el contenido

- **Pilar:** "la deuda operativa que nadie factura" (post fuerte + carrusel con la fórmula a la vista + video corto).
- **Micro:** 4 cuellos de botella × (por qué es tu freno / 3 acciones / qué NO hacer) = 12 posts + 4 mantras + 3 posts "sin humo" (sistema de IA, agente, loop — el glosario de 5ter como serie) = ~4 semanas a 5/semana con axel-linkedin-voice.
- **Documentar, no crear:** cada Diagnóstico de Ahorro es contenido (el antes → después del baseline, sin nombre si no autoriza). Cada dashboard de partner deal, también.
- CTA fijo en todo: la calculadora.

## 11. Tablero de métricas (6 números, semanal)

| # | Métrica | Referencia de arranque* |
|---|---|---|
| 1 | Visitas → inicio calculadora | 30–50% |
| 2 | Inicio → completada | 55–75% (6 preguntas) |
| 3 | Completada → aplicación | 5–12% |
| 4 | Show rate | 60–80% con protocolo 9b |
| 5 | Sesión → Diagnóstico pago | tu baseline (el número más importante del funnel) |
| 6 | Diagnóstico → Partner deal | esperable 60–90% (el diagnóstico pre-vende solo) |

*Referencias para arrancar; a los 30 días manda tu baseline. La métrica 5 es la que define si el modelo funciona: es tu close rate de plata real.

---

## Notas para vos (no van al prospecto)

### Qué se decidió en esta versión
- Escalones eliminados → **calculadora (deuda en horas/plata) + perfil de 4 dimensiones + cuello de botella**. Diagnóstico defendible: aritmética con fórmula a la vista + assessment multidimensional, mismo framework de punta a punta (calculadora → sesión → Diagnóstico → dashboard del deal).
- Posicionamiento: **A13I Partner**, claim "cobramos del ahorro que generamos, no de tu caja". Modelo híbrido: Diagnóstico USD 300–500 descontable + 25% del ahorro verificado × 12 meses (30% en los primeros 3–5 deals de apertura).
- El CTA pasó de "agendá" a **"aplicá"** — selectividad real, no pose: el modelo te obliga a elegir clientes con ahorro medible.
- **TU PLAN (5bis):** el resultado vuelve a ser un accionable, no solo un diagnóstico — 3 fases secuenciadas por el perfil (el orden de tus puntajes ES la personalización). Fases 1-2 las puede hacer solo (valor standalone); la Fase 3 (el primer loop) es donde A13I entra natural.
- **Vocabulario técnico con frame de descarga (5ter):** sistemas de IA, agentes, arquitectura y loop aparecen siempre pegados a "de eso nos encargamos nosotros — vos ponés la estrategia y el criterio". Señala competencia sin pedirle al lector que la entienda.
- **Reframe Arcadia (tras ver plan.arcadiamedia.io):** el entregable dejó de ser "tu deuda" (mala noticia que nadie comparte) y pasó a ser el **Plan de Autonomía Operativa** — índice 0-100 + mapa de 4 tramos + fases. Los 4 nombres-espejo de la escalera vuelven como tramos del índice (ahora derivados de dimensiones puntuadas = defendibles). La deuda quedó como "el costo de quedarte donde estás", después del regalo. De Arcadia se calcaron además: headline con entregable + número + intervalo, mockup del plan visible antes de contestar, primera pregunta embebida en la landing, y footer legal + pixel listo para ads.

### Defaults editables (todos en un solo lugar)
- Tarifas founder: 25 / 50 / 80 / 120 USD/h por rango · equipo USD 10/h · 10 min por interrupción · 22 días hábiles · factor honestidad "mitad automatizable".
- Deal: 25% × 12 meses · apertura 30% · Diagnóstico 300–500 · fee mínimo por no-adopción (definí el número con el primer contrato) · techo opcional.
- Stack: 150/300/150.

### Lo que me tenés que pasar (sin cambios vs. v3)
1. **Casos** con la spec: rubro · país · rango · proceso · métrica antes → después · tiempo · cita. Mínimo 3, uno por rango.
2. **Tu historia para el Mail 1** (4 líneas: cuándo, qué negocio, qué viste).
3. **Foto** para "Quién está detrás".

### Pendientes de implementación
- Calculadora como página (la fórmula es simple: se hace con un HTML como los del repo o un form + n8n). El branch de P4 para "solo yo" está especificado en la sección 2.
- Dashboard de medición del ahorro (n8n/BI) — sin esto no hay modelo partner; es LA pieza.
- Contrato marco del partner deal con las 4 cláusulas de la sección 0.
- Score de Madurez en vivo para la sesión (igual que v3).

### Variantes de headline para A/B (después de lanzar)
- B (dolor): "¿Cuánto te cuesta por año que tu operación dependa de vos? Descubrilo en 60 segundos — y llevate el plan para recuperarlo."
- C (número): "88 horas por mes. Eso le cuesta al dueño promedio que todo pase por él. Recibí tu plan para recuperarlas."

### Nota sobre el "20+ horas por semana" del headline
Sale de la matemática propia: respuesta modal 3–5 hs/día del dueño → ~88 hs/mes ≈ 20/semana. Cuando tengas casos reales, reemplazalo por el número documentado (mejor un 14 real que un 20 estimado).
