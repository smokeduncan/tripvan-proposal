"""Build es.html (Chilean Spanish) from index.html (English).

Run from the tripvan-presentation folder:  python tools/make_es.py
Re-run after any change to index.html so both versions stay in sync.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, DST = ROOT / "index.html", ROOT / "es.html"

LANG_CSS = """#lang{position:fixed;left:18px;top:14px;z-index:6;display:flex;gap:4px;font-family:var(--mono);font-size:12px;letter-spacing:.14em;}
#lang a{color:var(--dim);text-decoration:none;padding:5px 9px;border:1px solid var(--line-strong);border-radius:99px;background:rgba(8,19,19,.6);}
#lang a.on{color:var(--ink);background:var(--gold);border-color:var(--gold);}
html.print-pdf #lang{display:none !important;}
"""

# 1. make sure the English source carries the EN/ES toggle
s = SRC.read_text(encoding="utf-8")
if 'id="lang"' not in s:
    s = s.replace("/* print / pdf: static", LANG_CSS + "/* print / pdf: static")
    s = s.replace('<div id="hint">', '<nav id="lang"><a href="index.html" class="on">EN</a><a href="es.html">ES</a></nav>\n<div id="hint">')
    SRC.write_text(s, encoding="utf-8")

R = [
# head / chrome
('<html lang="en">', '<html lang="es-CL">'),
('<title>TripVan × Sondri — Proposal</title>', '<title>TripVan × Sondri — Propuesta</title>'),
('← → navigate · click Raco · F fullscreen · S speaker view', '← → navegar · haz clic en Raco · F pantalla completa'),
('<span>TripVan × Sondri — Proposal</span>', '<span>TripVan × Sondri — Propuesta</span>'),
('title="Raco — click me"', 'title="Raco — haz clic"'),
('<a href="index.html" class="on">EN</a><a href="es.html">ES</a>', '<a href="index.html">EN</a><a href="es.html" class="on">ES</a>'),
# S1
("data-say=\"¡Hola! I'm Raco — guardian of the Cajón del Maipo. Let me show you around.\"", 'data-say="¡Hola! Soy Raco, guardián del Cajón del Maipo. Acompáñame, te muestro la propuesta."'),
('<div class="eyebrow a-up">A proposal for</div>', '<div class="eyebrow a-up">Una propuesta para</div>'),
('The digital journey — from OTA-dependence to <em>an owned growth engine.</em>', 'El viaje digital: de depender de las OTA a <em>un motor de crecimiento propio.</em>'),
('<b>01</b>Foundation</span><span class="chip"><b>02</b>Acceleration</span><span class="chip"><b>03</b>Efficiency', '<b>01</b>Base</span><span class="chip"><b>02</b>Aceleración</span><span class="chip"><b>03</b>Eficiencia'),
('Prepared for <strong>Hernán, TripVan</strong> · Cajón del Maipo<br/>Chile — Forbes “Destination of the Year”', 'Preparado para <strong>Hernán, TripVan</strong> · Cajón del Maipo<br/>Chile — “Destino del Año” según Forbes'),
# S2
('data-say="This is my home. Twelve stops, one van, zero rush."', 'data-say="Esta es mi casa. Doce paradas, una van y cero apuro, po."'),
('The client · tripvan.cl', 'El cliente · tripvan.cl'),
('TripVan connects the <em>Cajón del Maipo.</em>', 'TripVan conecta el <em>Cajón del Maipo.</em>'),
('An organised passenger route through the Andes outside Santiago. <b style="color:var(--bone)">“We connect the route. You live every stop.”</b> Every stop is a local producer, a landscape or a story.',
 'Un servicio organizado de transporte por la cordillera, a las afueras de Santiago. <b style="color:var(--bone)">“Nosotros conectamos la ruta. Tú vives cada parada.”</b> Cada parada es un productor local, un paisaje o una historia.'),
('connected stops on the Ruta Sostenible', 'paradas conectadas en la Ruta Sostenible'),
('a full mountain day, hotel pickup', 'jornada completa de montaña, con recogida en el hotel'),
('multilingual guiding &amp; content', 'atención y contenido multilingüe'),
('CLP per adult · $50.000 child (4–10)', 'CLP por adulto · $50.000 niño (4–10)'),
('+ yrs</div>', '+ años</div>'),
('on the ground in the Cajón', 'de experiencia en el Cajón'),
('an owned mascot &amp; audio-guide — a brand asset OTAs can’t copy', 'mascota y audioguía propias: un activo de marca que ninguna OTA puede copiar'),
('THE VAN · RUTA SOSTENIBLE', 'LA VAN · RUTA SOSTENIBLE'),
('REAL TRAVELERS · MAY 2026', 'VIAJEROS REALES · MAYO 2026'),
# S3
("data-say=\"Up to 30% to the OTAs? That's a lot of alfalfa…\"", 'data-say="¿Hasta un 30% para las OTA? Eso es mucha alfalfa, cachai…"'),
('<div class="eyebrow a-up">The situation</div>', '<div class="eyebrow a-up">La situación</div>'),
('Today, TripVan <em>rents</em> its demand.', 'Hoy, TripVan <em>arrienda</em> su demanda.'),
('Chile just won Forbes “Destination of the Year” again — demand is rising. But bookings flow through third-party platforms that take a heavy cut on every sale and own the customer relationship.',
 'Chile volvió a ser elegido “Destino del Año” por Forbes y la demanda va en alza. Pero las reservas pasan por plataformas de terceros que se quedan con una comisión alta en cada venta y son dueñas de la relación con el cliente.'),
('commission / booking', 'comisión / reserva'),
('<span>One adult seat · CLP 75.000</span><span>OTA cut 20–30%</span>', '<span>Un pasaje adulto · CLP 75.000</span><span>Comisión OTA 20–30%</span>'),
('<span class="keep">TripVan keeps</span>', '<span class="keep">Lo que queda para TripVan</span>'),
('walks out the door — per adult, per booking.', 'se van por la puerta, por cada adulto y cada reserva.'),
('<b>The risk:</b> every booking loses 20–30% to OTAs — and they, not TripVan, own the customer, the data, and the repeat sale.',
 '<b>El riesgo:</b> cada reserva pierde entre 20 y 30% con las OTA, y son ellas (no TripVan) las dueñas del cliente, de los datos y de la próxima venta.'),
# S4
("data-say=\"If it worked in the Western Ghats, it'll work in the Andes.\"", 'data-say="Si funcionó en los Ghats de la India, ¡en los Andes va a funcionar al tiro!"'),
('<div class="eyebrow a-up">The proven playbook</div>', '<div class="eyebrow a-up">Un modelo probado</div>'),
('We’ve seen this journey work: <em>BMC Adventures.</em>', 'Ya vimos este camino funcionar: <em>BMC Adventures.</em>'),
('A South-India trekking operator that built an owned digital platform — direct booking, content-led acquisition, and a loyal community. The same arc TripVan can take in Chile.',
 'Un operador de trekking del sur de la India que construyó su propia plataforma digital: reserva directa, captación a través de contenido y una comunidad leal. El mismo recorrido que TripVan puede hacer en Chile.'),
('<div class="l">participants</div>', '<div class="l">participantes</div>'),
('<div class="l">members</div>', '<div class="l">miembros</div>'),
('<div class="l">adventure events</div>', '<div class="l">eventos de aventura</div>'),
('<div class="v" style="color:var(--gold)">Direct</div><div class="l">booking engine</div>', '<div class="v" style="color:var(--gold)">Directa</div><div class="l">motor de reservas</div>'),
('SOUTH INDIA · BMC', 'SUR DE LA INDIA · BMC'),
('<span class="lab a-up">What it proves</span>', '<span class="lab a-up">Lo que demuestra</span>'),
('Own the website &amp; booking', 'Ser dueño del sitio y las reservas'),
('Win on SEO / content', 'Ganar en SEO y contenido'),
('Build community</span>', 'Construir comunidad</span>'),
('Land corporate &amp; group clients', 'Captar clientes corporativos y grupos'),
# S5
('data-say="Three camps. One summit. I know every trail up there."', 'data-say="Tres campamentos, una cumbre. Me conozco todos los senderos."'),
('<div class="eyebrow a-up">The solution</div>', '<div class="eyebrow a-up">La solución</div>'),
('Three quadrants. <em>A deepening partnership.</em>', 'Tres cuadrantes. <em>Una alianza que se profundiza.</em>'),
('01 · CAMP ONE</div><div class="t">Foundation</div><div class="s">Digital Strategy</div><div class="d">Website, SEO &amp; AEO — take TripVan on its digital journey.</div><div class="price">$2,500 / month</div>',
 '01 · CAMPAMENTO UNO</div><div class="t">Base</div><div class="s">Estrategia Digital</div><div class="d">Sitio web, SEO y AEO: llevar a TripVan por su viaje digital.</div><div class="price">US$2.500 / mes</div>'),
('02 · CAMP TWO</div><div class="t">Acceleration</div><div class="s">Growth Engine</div><div class="d">Drive bookings directly; shift to a performance share.</div><div class="price">~10% per transaction</div>',
 '02 · CAMPAMENTO DOS</div><div class="t">Aceleración</div><div class="s">Motor de Crecimiento</div><div class="d">Generar reservas directas y pasar a una comisión por resultados.</div><div class="price">~10% por transacción</div>'),
('03 · SUMMIT</div><div class="t">Efficiency</div><div class="s">50/50 Joint Venture</div><div class="d">Co-own the sustainable-farming innovation for farmers.</div><div class="price">50 / 50 split</div>',
 '03 · CUMBRE</div><div class="t">Eficiencia</div><div class="s">Joint Venture 50/50</div><div class="d">Ser co-dueños de la innovación en agricultura sostenible para agricultores.</div><div class="price">50 / 50</div>'),
('Vendor <span class="arr">→</span> Growth partner <span class="arr">→</span> Co-owner <small>The relationship deepens at every stage.</small>',
 'Proveedor <span class="arr">→</span> Socio de crecimiento <span class="arr">→</span> Co-dueño <small>La relación se profundiza en cada etapa.</small>'),
# S6
('data-say="Ask an AI “best day trip from Santiago”… it should say TripVan."', 'data-say="Pregúntale a una IA por “el mejor paseo por el día desde Santiago”… debería decir TripVan."'),
('Quadrant 1 · Foundation', 'Cuadrante 1 · Base'),
('Digital <em>Strategy</em>', 'Estrategia <em>Digital</em>'),
('Take TripVan on the same digital journey that built BMC — off the OTAs, onto an owned platform it controls.', 'Llevar a TripVan por el mismo viaje digital que construyó BMC: salir de las OTA y pasar a una plataforma propia, bajo su control.'),
('<div class="t">Website &amp; direct booking</div></div><div class="d">Turn tripvan.cl — already ES/EN/PT with CLP/USD/BRL — into a conversion engine with <b>real-time availability</b>. No OTA commission on a direct sale.',
 '<div class="t">Sitio web y reserva directa</div></div><div class="d">Convertir tripvan.cl (que ya está en ES/EN/PT y en CLP/USD/BRL) en un motor de conversión con <b>disponibilidad en tiempo real</b>. Sin comisión OTA en la venta directa.'),
('<div class="t">SEO foundation</div></div><div class="d">Destination pages — <b>Cajón del Maipo, Embalse El Yeso, San José de Maipo, snow day trips from Santiago</b> — plus technical SEO, schema &amp; Google Business.',
 '<div class="t">Base SEO</div></div><div class="d">Páginas de destino (<b>Cajón del Maipo, Embalse El Yeso, San José de Maipo, paseos a la nieve desde Santiago</b>), más SEO técnico, schema y Google Business.'),
('<div class="t">AEO — AI search</div></div><div class="d">Answer-Engine-Optimized content so TripVan surfaces in <b>ChatGPT, Gemini &amp; AI Overviews</b>, not just Google.',
 '<div class="t">AEO: búsqueda con IA</div></div><div class="d">Contenido optimizado para motores de respuesta, para que TripVan aparezca en <b>ChatGPT, Gemini y AI Overviews</b>, no solo en Google.'),
('<div class="t">Content engine</div></div><div class="d">Forbes “Destination of the Year” anchor article + an evergreen blog, set up to publish consistently.',
 '<div class="t">Motor de contenido</div></div><div class="d">Artículo ancla sobre el “Destino del Año” de Forbes + un blog atemporal, preparado para publicar con constancia.'),
('<div class="t">Own the audience</div></div><div class="d">WhatsApp booking + email capture &amp; newsletter — a <b>first-party list</b> TripVan keeps, unlike OTA customers.',
 '<div class="t">Audiencia propia</div></div><div class="d">Reservas por WhatsApp + captura de correos y newsletter: una <b>base de datos propia</b> que se queda con TripVan, a diferencia de los clientes de las OTA.'),
('<div class="t">Analytics &amp; tracking</div></div><div class="d">Conversion tracking and a simple dashboard so every channel’s bookings are measurable from day one.',
 '<div class="t">Analítica y medición</div></div><div class="d">Seguimiento de conversiones y un dashboard simple para medir las reservas de cada canal desde el primer día.'),
('<span class="k">Commercial model</span><span class="v"><span>$2,500</span> / month · fixed service retainer</span>', '<span class="k">Modelo comercial</span><span class="v"><span>US$2.500</span> / mes · fee mensual fijo</span>'),
# S7
('data-say="Creators love llamas. Just saying."', 'data-say="A los creadores de contenido les encantan las llamas. Es un dato, nomás."'),
('Quadrant 2 · Acceleration', 'Cuadrante 2 · Aceleración'),
('Pour fuel on <em>the foundation.</em>', 'Echarle bencina <em>a la base.</em>'),
('Once the foundation is driving bookings, Sondri scales demand — and shifts from a flat fee to a cut of the transactions it drives.', 'Cuando la base ya esté generando reservas, Sondri escala la demanda y pasa de un fee fijo a una comisión sobre las transacciones que genera.'),
('<div class="t">Content at scale</div></div><div class="d">Blog, video &amp; social + multi-platform syndication, AI-assisted — with <b>Raco as on-screen guide</b>.',
 '<div class="t">Contenido a escala</div></div><div class="d">Blog, video y redes + distribución multiplataforma, asistido por IA, con <b>Raco como guía en pantalla</b>.'),
('<div class="t">Influencer &amp; creator program</div></div><div class="d">Recruit creators; build the influencer-tourism flow with direct booking.',
 '<div class="t">Programa de influencers</div></div><div class="d">Sumar creadores y armar el flujo de turismo con influencers, con reserva directa.'),
('<div class="t">Data Aggregator App</div></div><div class="d">Providers, tours &amp; creator performance in one booking + analytics hub.',
 '<div class="t">App agregadora de datos</div></div><div class="d">Prestadores, tours y desempeño de creadores en un solo centro de reservas y analítica.'),
('<div class="t">Paid acquisition</div></div><div class="d">Google / Meta campaigns + retargeting to compound the organic base.',
 '<div class="t">Pauta pagada</div></div><div class="d">Campañas en Google y Meta + retargeting para potenciar la base orgánica.'),
('<div class="t">Premium “Stargazing Line”</div></div><div class="d">Launch &amp; market the sustainability tour ($100+/head) under Andean night skies.',
 '<div class="t">Línea premium de astroturismo</div></div><div class="d">Lanzar y promocionar el tour sostenible (US$100+ por persona) bajo el cielo nocturno de la cordillera.'),
('<div class="t">Corporate &amp; group channel</div></div><div class="d">Corporate retreats &amp; group tours — the BMC playbook.',
 '<div class="t">Canal corporativo y grupos</div></div><div class="d">Retiros de empresa y tours grupales: el modelo de BMC.'),
('<div class="ttl">The cut — benchmarked</div>', '<div class="ttl">La comisión, comparada</div>'),
('<span>OTA marketplaces</span>', '<span>Marketplaces OTA</span>'),
('<span>Expedia activities</span>', '<span>Actividades Expedia</span>'),
('<span>Affiliate payout</span>', '<span>Pago a afiliados</span>'),
('<span>Sondri (rec.)</span>', '<span>Sondri (recom.)</span>'),
('<span>10%</span> of each transaction Sondri drives', '<span>10%</span> de cada transacción que genera Sondri'),
('The $2,500 retainer tapers as the cut grows. Top of the affiliate band (we own the whole funnel), far below the 20–30% OTAs charge — so TripVan wins on every booking moved in-house.',
 'El fee de US$2.500 baja a medida que crece la comisión. Es el techo del rango de afiliados (manejamos todo el embudo) y muy por debajo del 20–30% que cobran las OTA: TripVan gana en cada reserva que pasa a ser propia.'),
# S8
('data-say="Equal shares. Equal hay. Very fair."', 'data-say="Mitad y mitad. Mismo pasto para todos. Bien justo, po."'),
('Quadrant 3 · Efficiency', 'Cuadrante 3 · Eficiencia'),
('A <em>50/50</em> joint venture.', 'Un joint venture <em>50/50.</em>'),
('Sondri and TripVan jointly build a sustainable-farming innovation for farmers — equal IP, equal capital, equal upside.', 'Sondri y TripVan construyen juntos una innovación en agricultura sostenible para agricultores: misma propiedad intelectual, mismo capital, mismas ganancias.'),
('>NEW FIRM<', '>NUEVA EMPRESA<'),
('Shared ownership of a new firm — not a service relationship. Both parties co-invest and co-own the IP and the revenue.', 'Propiedad compartida de una nueva empresa, no una relación de servicios. Ambas partes coinvierten y son co-dueñas de la propiedad intelectual y los ingresos.'),
('<div class="t">Sustainable farm innovation</div></div><div class="d">Hydrogel-planting experience + IoT farm tech &amp; water monitoring, built jointly.',
 '<div class="t">Innovación agrícola sostenible</div></div><div class="d">Experiencia de plantación con hidrogel + tecnología IoT y monitoreo de agua, desarrollada en conjunto.'),
('<div class="t">Charge passengers</div></div><div class="d">Premium stargazing + farm &amp; local-producer tours at <b>$100+/head</b>.',
 '<div class="t">Cobro a pasajeros</div></div><div class="d">Astroturismo premium + tours a campos y productores locales a <b>US$100+ por persona</b>.'),
('<div class="t">Charge farmers</div></div><div class="d">Farmers pay to host the tourist-planting experience on their land.',
 '<div class="t">Cobro a agricultores</div></div><div class="d">Los agricultores pagan por recibir la experiencia de plantación turística en su campo.'),
('<div class="t">Govt. funding</div></div><div class="d">Startup Chile + subsidies fund the sustainable-tech build (non-dilutive).',
 '<div class="t">Fondos públicos</div></div><div class="d">Start-Up Chile + subsidios financian el desarrollo de la tecnología sostenible (sin dilución).'),
('<b>WHY 50/50</b>Equal IP and equal capital/risk on a net-new product line — distinct from the Q1 retainer and Q2 revenue share. The deepest tier of the partnership: <span class="gold">co-owner, not vendor.</span>',
 '<b>¿POR QUÉ 50/50?</b>Misma propiedad intelectual y mismo capital y riesgo en una línea de negocio totalmente nueva, distinta del fee del C1 y la comisión del C2. El nivel más profundo de la alianza: <span class="gold">co-dueño, no proveedor.</span>'),
# S9
("data-say=\"¡Vamos! Acompáñame — let's build it together.\"", 'data-say="¡Vamos! Acompáñame, construyámoslo juntos. ¡Va a quedar bacán!"'),
('The partnership, end to end', 'La alianza, de principio a fin'),
('How Sondri <em>grows with</em> TripVan.', 'Cómo Sondri <em>crece junto a</em> TripVan.'),
('<div class="ph">Foundation</div><div class="t">Service provider</div><div class="m">$2,500 / mo</div><div class="d">Website · SEO · AEO</div>',
 '<div class="ph">Base</div><div class="t">Proveedor de servicios</div><div class="m">US$2.500 / mes</div><div class="d">Sitio web · SEO · AEO</div>'),
('<div class="ph">Acceleration</div><div class="t">Growth partner</div><div class="m">~10% / txn</div><div class="d">Drives direct bookings</div>',
 '<div class="ph">Aceleración</div><div class="t">Socio de crecimiento</div><div class="m">~10% / transacción</div><div class="d">Genera reservas directas</div>'),
('<div class="ph">Efficiency</div><div class="t">Co-owner</div><div class="m">50 / 50 JV</div><div class="d">Sustainability innovation</div>',
 '<div class="ph">Eficiencia</div><div class="t">Co-dueño</div><div class="m">JV 50 / 50</div><div class="d">Innovación sostenible</div>'),
('From renting demand<br/>to <em>owning growth.</em>', 'De arrendar la demanda<br/>a <em>ser dueños del crecimiento.</em>'),
('Let’s build TripVan’s digital future together · sondri.ai →', 'Construyamos juntos el futuro digital de TripVan · sondri.ai →'),
# Raco click lines
('"Cajón del Maipo has 12 stops — I\'ve visited all of them. Twice."', '"El Cajón tiene 12 paradas y me las conozco todas. Dos veces."'),
('"Fun fact: llamas hum when they\'re happy. Mmmmm."', '"Dato curioso: las llamas tarareamos cuando estamos felices. Mmmmm."'),
('"El Yeso is turquoise because of glacial minerals. Very photogenic."', '"El Yeso es turquesa por los minerales de los glaciares. Sale regio en las fotos."'),
('"Don\'t tell the OTAs, but I\'m the best guide in the Andes."', '"No le digan a las OTA, pero soy el mejor guía de la cordillera."'),
('"Direct booking = more alfalfa for everyone."', '"Reserva directa = más alfalfa para todos."'),
# speaker notes
('Open: Chile is on a global stage. TripVan has the product; this is about owning the demand.', 'Apertura: Chile está en la vitrina mundial. TripVan tiene el producto; esto se trata de ser dueños de la demanda.'),
('Facts pulled from tripvan.cl: 12-stop route, 05:00–15:30, CLP 75.000 adult / 50.000 child, ES/EN/PT, 10+ years, Raco mascot.', 'Datos de tripvan.cl: ruta de 12 paradas, 05:00–15:30, CLP 75.000 adulto / 50.000 niño, ES/EN/PT, 10+ años, mascota Raco.'),
('CLP math: 20% and 30% of a CLP 75.000 adult seat (tripvan.cl price).', 'Cálculo: 20% y 30% de un pasaje adulto de CLP 75.000 (precio en tripvan.cl).'),
]

missing = []
for a, b in R:
    if a not in s:
        missing.append(a[:80])
    s = s.replace(a, b)
DST.write_text(s, encoding="utf-8")
if missing:
    print("NOT FOUND:\n  " + "\n  ".join(missing)); sys.exit(1)
print(f"wrote {DST.name} ({len(R)} replacements)")
