\
# -*- coding: utf-8 -*-
from weasyprint import HTML

VERTICALS = [
    {"id": "moda", "name": "Moda y Belleza", "desc": "Indumentaria, calzado, cosmética, accesorios."},
    {"id": "retail", "name": "Electrónica, Retail y Marketplaces", "desc": "Electrónica, hogar, retail generalista, marketplaces."},
    {"id": "cpg", "name": "Supermercados, B2B y CPG", "desc": "Supermercados, distribución B2B, consumo masivo."},
    {"id": "travel", "name": "Travel, Educación y Servicios Online", "desc": "Turismo, cursos online, suscripciones de servicio."},
]

AREAS = [
    {"id": "A", "name": "Infraestructura tecnológica y plataforma"},
    {"id": "B", "name": "Marketing y generación de demanda"},
    {"id": "C", "name": "Operaciones y logística / fulfillment"},
    {"id": "D", "name": "Atención al cliente y CX"},
]

MATRIX = {
    "moda": {
        "A": {
            "qw": {"title": "Búsqueda visual y comprá este look", "desc": "El comprador sube o toca una foto de un producto y el sistema devuelve ítems visualmente similares del catálogo, sin depender de que la descripción tenga las palabras correctas.", "metric": "10 a 20% más conversión en las sesiones que usan búsqueda visual, contra el buscador de texto tradicional.", "stack": "Shopify o VTEX más una app de visual search (Syte, Vue.ai) conectada al feed de productos.", "risk": "Si las fotos del catálogo tienen fondos, ángulos o resoluciones distintas entre sí, el modelo confunde productos parecidos y pierde precisión."},
            "bs": {"title": "Predicción de talle con visión por computadora", "desc": "Un modelo entrenado con el historial de compras y devoluciones sugiere el talle correcto antes de la compra, en vez de después de la devolución.", "metric": "Reducción de 20 a 30% en devoluciones atribuidas a talle incorrecto en las categorías donde se activa.", "stack": "Motor de fit prediction propio o de un partner (True Fit, 3DLOOK) integrado al PIM y alimentado con el historial de devoluciones.", "risk": "Necesita un volumen grande de devoluciones ya etiquetadas por motivo. Sin esa data limpia, el modelo tarda meses en volverse confiable."},
        },
        "B": {
            "qw": {"title": "Generación de copy y variantes de ads con IA", "desc": "Un modelo de lenguaje escribe las descripciones de producto y genera variantes de copy para probar en campañas, a partir de los atributos que ya existen en el catálogo.", "metric": "60 a 80% menos tiempo de producción de copy por SKU, con más variantes disponibles para testear.", "stack": "API de un modelo de lenguaje conectada al catálogo (PIM o planilla) y al administrador de campañas de Meta o TikTok.", "risk": "Sin ejemplos y guías de la voz de marca cargados de antemano, el copy sale genérico y termina sonando igual al de cualquier competidor."},
            "bs": {"title": "Personalización dinámica de creativos por audiencia", "desc": "Un motor genera y combina variantes de creativos automáticamente según la audiencia que los va a ver, en vez de correr los mismos banners para todos.", "metric": "20 a 35% más ROAS en campañas de retargeting.", "stack": "Dynamic Creative Optimization (Meta Advantage+, Google PMax) más un feed de producto enriquecido y generación de variantes con IA.", "risk": "La fatiga creativa exige refresco constante del feed. Sin gobernanza de marca sobre las variantes generadas, el mensaje se degrada con el tiempo."},
        },
        "C": {
            "qw": {"title": "Forecasting de demanda por SKU y talle", "desc": "Un modelo estima cuánto se va a vender de cada combinación de producto y talle en las próximas semanas, para comprar y reponer antes de que falte o sobre stock.", "metric": "15 a 25% menos capital inmovilizado en stock parado, con menos quiebres en los SKU que más venden.", "stack": "Herramienta de forecasting (Lokad, Inventoro) conectada al ERP o WMS y al historial de ventas.", "risk": "Las colecciones cambian rápido, así que un SKU nuevo casi no tiene historia propia. El modelo se apoya en categorías similares mientras junta datos."},
            "bs": {"title": "Ruteo inteligente para picos estacionales", "desc": "Un sistema de optimización de rutas y asignación de pedidos entre depósitos y couriers, pensado para absorber los picos de Black Friday, Día de la Madre o Navidad sin que se caiga el SLA de entrega.", "metric": "20 a 30% menos costo de última milla en los meses pico, con menos entregas fuera de plazo.", "stack": "TMS con ruteo dinámico (Beetrack, Onfleet) integrado a los 3PL y al pronóstico de demanda por zona.", "risk": "La inversión en hubs o micro-fulfillment solo se paga si el volumen de los picos se sostiene. En operaciones muy estacionales puede quedar infrautilizada el resto del año."},
        },
        "D": {
            "qw": {"title": "Bot de WhatsApp para talle, stock y estado de pedido", "desc": "Un asistente conversacional responde las preguntas más repetidas, como si tienen un talle o cuándo llega un pedido, conectado al inventario y al sistema de órdenes en tiempo real.", "metric": "40 a 50% menos tickets de primer nivel, con primera respuesta en segundos en vez de horas.", "stack": "WhatsApp Business API más una plataforma conversacional (Yalo, Landbot) con un modelo de lenguaje conectado al OMS.", "risk": "Si el bot no está conectado al stock real puede confirmar disponibilidad de algo que ya se vendió. La integración en tiempo real no es opcional acá."},
            "bs": {"title": "Asesor de estilo personalizado por IA", "desc": "Un asistente que conoce el historial de compras y las preferencias del cliente y recomienda combinaciones o próximas compras, como haría un vendedor de confianza en el local.", "metric": "15 a 20% más ticket promedio en los clientes que interactúan con el asesor, con mejor tasa de recompra.", "stack": "Modelo de lenguaje con acceso al catálogo y al historial de compra (RAG), integrado al CRM o CDP.", "risk": "Sin una base de datos de clientes limpia y centralizada, el asesor no tiene con qué personalizar y termina dando recomendaciones genéricas."},
        },
    },
    "retail": {
        "A": {
            "qw": {"title": "Enriquecimiento automático de fichas para marketplaces", "desc": "Un modelo genera títulos, atributos y categorización optimizados para cómo buscan los compradores en Mercado Libre o Amazon, a partir de la ficha técnica del producto.", "metric": "10 a 15% más visibilidad en los resultados de búsqueda del marketplace, con 70% menos tiempo de carga de catálogo.", "stack": "Modelo de lenguaje conectado al PIM, con publicación vía la API del marketplace.", "risk": "Los marketplaces cambian su taxonomía de categorías sin aviso. Sin monitoreo, las fichas quedan mal categorizadas de un día para el otro."},
            "bs": {"title": "Repricing dinámico", "desc": "Un motor ajusta el precio de cada producto de forma automática según el precio de la competencia, la demanda y el margen mínimo definido, en vez de que alguien lo revise a mano.", "metric": "5 a 10% más margen bruto y 8 a 12% más tasa de ganar el Buy Box.", "stack": "Motor de repricing (Prisync, RepricerExpress o desarrollo propio) con monitoreo de precios de competencia y reglas de piso de margen.", "risk": "Si varios competidores usan repricing automático al mismo tiempo, se puede entrar en una guerra de precios que erosiona el margen de todos."},
        },
        "B": {
            "qw": {"title": "Campañas de Shopping optimizadas por IA", "desc": "El feed de productos se limpia y optimiza con IA para que las campañas de Google Shopping o Performance Max muestren los productos correctos a la audiencia correcta.", "metric": "15 a 25% más ROAS, con la mitad del tiempo de gestión de campañas.", "stack": "Google Ads Performance Max más una herramienta de feed management (Feedonomics, DataFeedWatch).", "risk": "Performance Max decide por su cuenta dónde gastar el presupuesto. Se gana eficiencia pero se pierde control granular sobre el gasto."},
            "bs": {"title": "Motor de cross-sell y upsell en carrito", "desc": "Un sistema de recomendación sugiere productos complementarios en el carrito y en el email post-compra, basado en qué compran juntos otros clientes parecidos.", "metric": "10 a 18% más ticket promedio y 5 a 8% más ingreso por visitante.", "stack": "Motor de recomendación (Nosto, Algolia Recommend) integrado a la plataforma de eCommerce.", "risk": "Necesita volumen de tráfico y transacciones para entrenar bien. En catálogos chicos las recomendaciones no mejoran mucho respecto de reglas simples."},
        },
        "C": {
            "qw": {"title": "Triage automático de reclamos de garantía", "desc": "Un modelo clasifica cada reclamo entrante, por foto o por texto, según el tipo de falla y la probabilidad de que sea legítimo, antes de que un humano lo revise.", "metric": "30 a 40% menos tiempo de resolución de reclamos, con mejor detección temprana de casos de fraude.", "stack": "Modelo de lenguaje y visión conectado al sistema de tickets (Zendesk, Freshdesk).", "risk": "Un falso positivo de fraude genera fricción con un cliente legítimo. El umbral de confianza necesita ajuste fino antes de automatizar del todo."},
            "bs": {"title": "Optimización de inventario multi-depósito", "desc": "Un motor decide desde qué depósito despachar cada pedido y cómo redistribuir stock entre bodegas para acortar tiempos de entrega y bajar el costo logístico.", "metric": "20 a 25% menos costo logístico, con 1 a 2 días menos de tiempo de entrega.", "stack": "OMS multi-depósito con motor de asignación, integrado a los 3PL y a los programas de fulfillment de cada marketplace.", "risk": "Cada marketplace tiene sus propias reglas de fulfillment. Integrar todo a la vez es un proyecto de varios meses, no de semanas."},
        },
        "D": {
            "qw": {"title": "Asistente de soporte técnico con base de conocimiento", "desc": "Un modelo responde preguntas técnicas pre y post venta apoyándose en los manuales y specs reales del producto, en vez de respuestas genéricas.", "metric": "35 a 45% menos tickets escalados a un humano, con mejora de 10 a 15 puntos en NPS.", "stack": "Modelo de lenguaje con RAG sobre manuales y FAQ, integrado al canal de soporte.", "risk": "Productos que cambian de versión necesitan que alguien mantenga la base de conocimiento al día. Si se desactualiza, el bot empieza a dar información incorrecta."},
            "bs": {"title": "Detección temprana de clientes insatisfechos", "desc": "Un modelo cruza señales de reviews, tiempos de respuesta y devoluciones para detectar clientes en riesgo de irse antes de que se quejen en público, y dispara una acción de retención.", "metric": "15 a 20% menos devoluciones y reclamos recurrentes del mismo cliente.", "stack": "Modelo predictivo sobre un CDP, integrado al CRM con triggers automáticos de retención.", "risk": "Requiere unificar datos que suelen vivir en sistemas separados. Sin esa base unificada, el modelo no tiene señal suficiente."},
        },
    },
    "cpg": {
        "A": {
            "qw": {"title": "Digitalización automática de pedidos B2B", "desc": "Un sistema lee los pedidos que llegan por PDF, WhatsApp o email y los carga directo al ERP, sin que alguien los tipee a mano.", "metric": "80 a 90% menos tiempo de carga manual de pedidos, con muchos menos errores de tipeo.", "stack": "OCR e IA de extracción (Docsumo, Rossum o un modelo de lenguaje con visión) integrado al ERP (SAP Business One, Odoo).", "risk": "Cada cliente B2B manda los pedidos en su propio formato. El sistema necesita ajuste continuo a medida que se suman clientes nuevos."},
            "bs": {"title": "Reordering automático por punto de venta", "desc": "Un modelo predice cuándo cada punto de venta va a necesitar reponer stock y genera el pedido sugerido antes de que el cliente tenga que pedirlo.", "metric": "15 a 20% más frecuencia de recompra, con menos quiebres de stock del lado del cliente.", "stack": "Modelo de forecasting por cliente y SKU, integrado a un portal B2B propio y al ERP o CRM.", "risk": "Promociones, competencia o cambios de temporada alteran el patrón de consumo. El modelo necesita reentrenarse seguido o pierde precisión."},
        },
        "B": {
            "qw": {"title": "Lead scoring para el equipo comercial", "desc": "Un modelo prioriza qué cuentas B2B visitar o llamar primero, según probabilidad de compra y potencial de facturación, en vez de que cada vendedor decida a criterio propio.", "metric": "20 a 30% más productividad por vendedor, medida en pedidos o visitas efectivas.", "stack": "CRM (HubSpot, Salesforce) con modelo de scoring alimentado por el historial de facturación.", "risk": "Si el CRM tiene datos incompletos o desactualizados, el scoring sale poco confiable y el equipo comercial deja de confiar en él."},
            "bs": {"title": "Pricing dinámico B2B por elasticidad", "desc": "Un modelo ajusta precios y promociones por cliente o categoría según qué tan sensible es cada uno al precio, en vez de aplicar la misma lista a todos.", "metric": "5 a 8% más margen sin perder volumen de ventas.", "stack": "Modelo de revenue management integrado al ERP, alimentado con el histórico de elasticidad por cliente.", "risk": "Las relaciones B2B son sensibles a cambios de precio que se perciban como injustos. Necesita comunicación cuidadosa con el equipo comercial antes de activarse."},
        },
        "C": {
            "qw": {"title": "Ruteo dinámico de reparto B2B", "desc": "Un sistema arma las rutas de reparto multi-parada del día optimizando distancia, ventanas de entrega y capacidad del camión.", "metric": "15 a 20% menos costo de flete, con más entregas dentro del horario acordado.", "stack": "TMS con ruteo dinámico (Beetrack, Routific) integrado al ERP o WMS.", "risk": "Muchos clientes B2B solo reciben en ventanas horarias fijas. Eso limita cuánto se puede optimizar por distancia pura."},
            "bs": {"title": "Torre de control de supply chain", "desc": "Una plataforma centraliza la visibilidad de stock, demanda y reposición entre todos los centros de distribución, para anticipar quiebres antes de que pasen.", "metric": "25 a 30% menos quiebres de stock a nivel de toda la cadena, con mejor fill rate.", "stack": "Plataforma de supply chain planning, o desarrollo propio con BI, integrada al ERP, WMS y a los sistemas de los proveedores.", "risk": "El cuello de botella real casi nunca es el modelo de IA: es la integración de datos entre sistemas legacy que no se hablan entre sí."},
        },
        "D": {
            "qw": {"title": "Bot de atención B2B en WhatsApp", "desc": "Un asistente responde consultas de stock, precio y estado de pedido en tiempo real, sin que el cliente tenga que llamar al vendedor para algo que puede resolver solo.", "metric": "40% menos consultas manuales al equipo comercial, con respuesta en segundos en vez de minutos.", "stack": "WhatsApp Business API con un modelo de lenguaje conectado al ERP en tiempo real.", "risk": "Si el ERP no expone esa información en tiempo real, el bot da datos desactualizados y el cliente B2B deja de confiar en el canal."},
            "bs": {"title": "Portal de autoservicio con recomendaciones", "desc": "Un portal B2B propio sugiere qué reponer basado en el mix de compra histórico de cada punto de venta, reduciendo la dependencia del vendedor para los pedidos de rutina.", "metric": "12 a 18% más ticket promedio B2B, con menos carga operativa sobre el equipo comercial.", "stack": "Portal B2B propio, Shopify Plus B2B o VTEX, con motor de recomendación integrado al ERP o CRM.", "risk": "Clientes acostumbrados a pedir por WhatsApp o por el vendedor de siempre tardan en migrar al canal digital. Requiere gestión de cambio, no solo tecnología."},
        },
    },
    "travel": {
        "A": {
            "qw": {"title": "Buscador conversacional de destino, curso o servicio", "desc": "Un asistente conversacional ayuda al usuario a elegir entre las opciones del catálogo respondiendo en lenguaje natural, en vez de que tenga que usar filtros.", "metric": "15 a 20% más conversión de búsqueda a reserva o inscripción.", "stack": "Modelo de lenguaje con RAG sobre el catálogo, integrado al motor de reservas o al LMS.", "risk": "Si el precio o la disponibilidad no están conectados en tiempo real, el asistente puede ofrecer algo que ya no está disponible."},
            "bs": {"title": "Personalización de principio a fin", "desc": "Una plataforma arma itinerarios de viaje o rutas de aprendizaje distintas para cada usuario según su perfil e historial, en vez de mostrar el mismo catálogo a todos.", "metric": "20 a 25% más valor de vida del cliente, con mejor tasa de finalización en educación o de recompra en viajes.", "stack": "Modelo de recomendación con un perfil de usuario enriquecido (CDP), integrado al motor de contenido o de inventario.", "risk": "Con poca profundidad de catálogo o pocos datos de comportamiento, la personalización se siente forzada en vez de relevante."},
        },
        "B": {
            "qw": {"title": "Contenido SEO generado con IA a escala", "desc": "Un modelo produce artículos y guías para las búsquedas de cola larga, como destinos específicos o temas de curso puntuales, que antes no valía la pena escribir a mano.", "metric": "30 a 50% más tráfico orgánico de cola larga en 6 meses.", "stack": "Modelo de lenguaje más una herramienta de SEO (Surfer, Clearscope), integrado al CMS.", "risk": "Publicar en volumen sin revisión editorial daña la autoridad de la marca y puede afectar el posicionamiento en buscadores."},
            "bs": {"title": "Revenue management para cupos limitados", "desc": "Un sistema ajusta el precio de paquetes de viaje o cursos con cupo limitado según la demanda esperada, como hacen las aerolíneas con los asientos.", "metric": "10 a 15% más ingreso por unidad de inventario, sea asiento, cupo o sesión.", "stack": "Sistema de revenue management integrado al motor de reservas, alimentado con el histórico de demanda.", "risk": "El consumidor de un curso o un tour tolera menos el precio dinámico que el pasajero de avión si no se comunica bien. Necesita reglas claras de cara al cliente."},
        },
        "C": {
            "qw": {"title": "Conciliación automática de pagos multicanal", "desc": "Un sistema concilia automáticamente los pagos de reservas o inscripciones que llegan por distintas pasarelas y monedas, en vez de que alguien lo haga a mano en una planilla.", "metric": "60 a 70% menos horas de trabajo administrativo por mes, con menos errores de conciliación.", "stack": "Automatización con IA para matching de pagos, integrada a las pasarelas de pago y al ERP.", "risk": "Múltiples monedas y pasarelas complican el matching automático. Cuanto más fragmentado el cobro, más ajuste necesita el sistema."},
            "bs": {"title": "Predicción de capacidad y staffing", "desc": "Un modelo estima cuántos guías, docentes o agentes de soporte se necesitan en cada período, para armar los turnos con anticipación en vez de reaccionar sobre la marcha.", "metric": "15 a 20% menos costo de staffing sin bajar el nivel de servicio.", "stack": "Modelo de forecasting de demanda integrado al sistema de scheduling o de RRHH.", "risk": "Feriados, temporada y tipo de cambio meten ruido que no siempre está en la data histórica. El modelo necesita ajuste manual en los períodos atípicos."},
        },
        "D": {
            "qw": {"title": "Asistente de soporte 24/7", "desc": "Un asistente conversacional resuelve cambios de reserva y dudas frecuentes en WhatsApp o chat web a toda hora, sin depender de un turno nocturno humano.", "metric": "40 a 50% menos tickets de primer nivel, con disponibilidad las 24 horas.", "stack": "Modelo de lenguaje con RAG sobre políticas y FAQ, integrado al sistema de reservas o al LMS.", "risk": "Políticas de cambio y cancelación complejas generan respuestas incorrectas si el asistente no está bien acotado a la versión vigente de esa política."},
            "bs": {"title": "Retención proactiva contra cancelaciones", "desc": "Un modelo predice qué clientes están por cancelar o abandonar una suscripción o un curso, y dispara automáticamente una acción de recuperación antes de que decidan irse.", "metric": "15 a 25% menos cancelaciones o bajas.", "stack": "Modelo predictivo de churn sobre un CDP, con automatización de email o WhatsApp de retención.", "risk": "Necesita historial de cancelaciones suficiente y limpio. En negocios nuevos con poco historial, el modelo todavía no tiene con qué predecir bien."},
        },
    },
}

def card(kind, item):
    kind_label = "QUICK WIN &middot; 0-60 DÍAS" if kind == "qw" else "BIG SWING &middot; 12-36 MESES"
    kind_class = "quick" if kind == "qw" else "big"
    return f"""
    <div class="init-card {kind_class}">
      <span class="init-kind {kind_class}">{kind_label}</span>
      <h4 class="init-title">{item['title']}</h4>
      <p class="init-desc">{item['desc']}</p>
      <div class="init-row"><span class="init-label">Métrica de impacto</span><span class="init-val">{item['metric']}</span></div>
      <div class="init-row"><span class="init-label">Stack recomendado</span><span class="init-val">{item['stack']}</span></div>
      <div class="init-row"><span class="init-label">Riesgo principal</span><span class="init-val risk">{item['risk']}</span></div>
    </div>
    """

def area_block(area, cell):
    return f"""
    <div class="area-block">
      <div class="area-head">
        <span class="area-tag">{area['id']}</span>
        <h3 class="area-title">{area['name']}</h3>
      </div>
      <div class="init-grid">
        {card('qw', cell['qw'])}
        {card('bs', cell['bs'])}
      </div>
    </div>
    """

def vertical_section(v, idx):
    data = MATRIX[v['id']]
    blocks = "".join(area_block(a, data[a['id']]) for a in AREAS)
    page_break = "" if idx == 0 else 'style="page-break-before: always;"'
    return f"""
    <section class="vertical-section" {page_break}>
      <div class="vertical-head">
        <span class="vertical-eyebrow">VERTICAL {idx+1} DE 4</span>
        <h2 class="vertical-title">{v['name']}</h2>
        <p class="vertical-desc">{v['desc']}</p>
      </div>
      {blocks}
    </section>
    """

sections = "".join(vertical_section(v, i) for i, v in enumerate(VERTICALS))

html_doc = f"""
<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<style>
  @page {{
    size: A4;
    margin: 22mm 18mm 20mm 18mm;
    @bottom-center {{
      content: "A13I — Mapa de Oportunidades de IA para eCommerce · página " counter(page) " de " counter(pages);
      font-family: 'DejaVu Sans Mono', monospace;
      font-size: 8px;
      color: #B7A692;
      letter-spacing: 0.06em;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'DejaVu Sans', sans-serif;
    color: #1A1410;
    font-size: 10.2px;
    line-height: 1.5;
  }}
  .cover {{
    text-align: center;
    padding-top: 60mm;
  }}
  .cover .eyebrow {{
    display: inline-block;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 10px; font-weight: bold; letter-spacing: 0.16em;
    color: #E15E3F;
    border: 1px solid #E8B79A;
    border-radius: 100px;
    padding: 6px 16px;
    margin-bottom: 26px;
  }}
  .cover h1 {{
    font-size: 30px;
    font-weight: 900;
    letter-spacing: -0.02em;
    line-height: 1.15;
    margin: 0 0 18px;
    color: #1A1410;
  }}
  .cover .sub {{
    font-size: 13px;
    color: #6B5A4A;
    max-width: 120mm;
    margin: 0 auto 40px;
    line-height: 1.6;
  }}
  .cover .legend {{
    display: inline-block;
    text-align: left;
    border: 1px solid #EAD9C8;
    border-radius: 12px;
    padding: 18px 24px;
    background: #FDFAF3;
    margin-bottom: 30px;
  }}
  .cover .legend p {{ margin: 6px 0; font-size: 11px; color: #1A1410; }}
  .cover .legend b {{ color: #D4612A; }}
  .cover .author {{
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 10px; letter-spacing: 0.08em; color: #8C7A68;
    margin-top: 40px;
  }}
  .vertical-head {{ margin-bottom: 14px; }}
  .vertical-eyebrow {{
    display: inline-block;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 9px; font-weight: bold; letter-spacing: 0.14em;
    color: #FFFFFF; background: #D4612A;
    border-radius: 6px; padding: 4px 10px;
    margin-bottom: 8px;
  }}
  .vertical-title {{
    font-size: 19px; font-weight: 900; letter-spacing: -0.01em;
    margin: 6px 0 4px; color: #1A1410;
  }}
  .vertical-desc {{ font-size: 10.5px; color: #6B5A4A; margin: 0 0 6px; }}
  .area-block {{ margin-bottom: 14px; page-break-inside: avoid; }}
  .area-head {{ margin-bottom: 6px; }}
  .area-tag {{
    display: inline-block;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 9px; font-weight: bold; letter-spacing: 0.1em;
    color: #D4612A; border: 1px solid #EAD9C8; border-radius: 6px;
    padding: 3px 8px; margin-right: 8px;
  }}
  .area-title {{ font-size: 12.5px; font-weight: bold; color: #1A1410; display: inline; }}
  .init-grid {{ width: 100%; }}
  .init-card {{
    display: inline-block;
    width: 47.7%;
    vertical-align: top;
    border: 1px solid #EAD9C8;
    border-radius: 8px;
    padding: 10px 12px;
    margin-bottom: 8px;
  }}
  .init-card.quick {{ border-left: 3px solid #D4612A; margin-right: 3%; }}
  .init-card.big {{ border-left: 3px solid #8C7A68; }}
  .init-kind {{
    display: inline-block;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 7.3px; font-weight: bold; letter-spacing: 0.08em;
    padding: 2px 7px; border-radius: 100px; margin-bottom: 5px;
  }}
  .init-kind.quick {{ color: #B84A1F; background: #FBEBE2; }}
  .init-kind.big {{ color: #6B5A4A; background: #F3E7D6; }}
  .init-title {{ font-size: 11px; font-weight: bold; margin: 0 0 4px; color: #1A1410; }}
  .init-desc {{ font-size: 9.2px; color: #6B5A4A; margin: 0 0 6px; line-height: 1.45; }}
  .init-row {{ padding: 3px 0; border-top: 1px solid #F3E7D6; }}
  .init-label {{
    display: block;
    font-family: 'DejaVu Sans Mono', monospace;
    font-size: 6.8px; font-weight: bold; letter-spacing: 0.08em; text-transform: uppercase;
    color: #8C7A68; margin-bottom: 2px;
  }}
  .init-val {{ font-size: 8.8px; color: #1A1410; line-height: 1.4; }}
  .init-val.risk {{ color: #6B5A4A; }}
</style>
</head>
<body>

<div class="cover">
  <span class="eyebrow">A13I &middot; MAPA DE OPORTUNIDADES IA</span>
  <h1>El mapa de oportunidades de IA<br>para tu eCommerce en LATAM</h1>
  <p class="sub">32 iniciativas organizadas en 4 verticales y 4 áreas. Para cada una: qué es, qué mueve en el negocio, con qué se implementa y cuál es el riesgo principal a tener en cuenta.</p>
  <div class="legend">
    <p><b>Quick win</b> &middot; implementable en 0 a 60 días con SaaS o APIs existentes, ROI rápido.</p>
    <p><b>Big swing</b> &middot; 12 a 36 meses de construcción, ventaja difícil de copiar.</p>
  </div>
  <p class="author">A13I &middot; Axel Laban Arzubi</p>
</div>

{sections}

</body>
</html>
"""

with open("/tmp/quick-wins-ai-preview.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

HTML(string=html_doc).write_pdf("quick-wins-ai-documento.pdf")
print("PDF generado")
