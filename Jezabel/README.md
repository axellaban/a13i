# Portfolio de Dalila Jezabel Arzubi — Artista visual

Sitio web del portfolio, armado a partir del PDF "Portfolio C.V. Jezabel" (selección 2013 – 2026).
Mantiene su estilo: azul petróleo, papel lavanda, marcos blancos y fichas de obra en zigzag.

Está hecho sobre el template libre [Portfolio for Creatives](https://github.com/jamesdneufeld/portfolio-for-creatives)
de James Neufeld: HTML y CSS puros, sin instalar nada.

## Páginas

| Archivo | Qué es |
|---|---|
| `index.html` | Portada (como la tapa del PDF) y grilla con las 6 series |
| `retratos-magicos.html` | Serie 1 — Grafito |
| `composiciones-a-color.html` | Serie 2 — Lápices, acuarelas y fibras |
| `pinturas-al-oleo.html` | Serie 3 — Óleo |
| `texturas.html` | Serie 4 — Óleo sobre cartón corrugado |
| `collage.html` | Serie 5 — Collage |
| `proyectos.html` | Serie 6 — Portadas de disco y libro, con el proceso |
| `sobre-mi.html` | Sobre mí, Formación y Experiencia |
| `includes/header.html` | Menú de arriba (compartido por todas las páginas) |
| `includes/footer.html` | Contacto de abajo (compartido por todas las páginas) |

## Cómo agregar una obra nueva

1. Guardá la foto en `assets/obras/` con un nombre sin espacios ni tildes, por ejemplo `nombre-de-la-obra-2026.jpg`.
   Lo ideal es que el lado más largo mida unos 1600 px.
2. Abrí la página de la serie (por ejemplo `retratos-magicos.html`), copiá un bloque `<article class="obra reveal"> … </article>`
   completo y pegalo donde quieras que aparezca.
3. Cambiá en la copia: la ruta de la imagen (aparece dos veces), el `alt` (una descripción de la obra),
   el `data-title` (lo que se lee al verla en grande) y la ficha (título, año y técnica).

El zigzag (imagen a la izquierda o a la derecha) se acomoda solo.
Para que una obra aparezca sola, grande y centrada, usá `class="obra obra--destacada reveal"`.

## Cómo cambiar el contacto

El mail, el teléfono y el Instagram están en dos lugares: `includes/footer.html` y el final de `sobre-mi.html`.

## Colores y tipografías

Están todos juntos al principio de `styles/jezabel.css` (`--petroleo`, `--papel`, `--tinta`…).
Las tipografías son **Amarante** (títulos) y **Josefin Slab** (textos), ambas de Google Fonts.
El PDF usa "Obra Letra" para los títulos, una fuente de Canva que no se puede usar libre en la web, y Amarante es la más parecida.

## Verlo en la computadora

El menú y el pie se cargan desde `includes/`, así que **no funcionan abriendo el HTML con doble clic**.
Hay que levantar un servidor local desde esta carpeta:

```bash
python3 -m http.server 8080
# y abrir http://localhost:8080
```

## Publicarlo gratis

**GitHub Pages:** subí esta carpeta a un repositorio de GitHub. Después, en Settings → Pages, elegí la rama `main` y la carpeta `/ (root)`.
Queda en `https://<usuario>.github.io/<repositorio>/`.

**Vercel o Netlify:** importá el repositorio y no hace falta configurar nada (no hay build).

## Licencias

- El código del template es GPL-3.0 (ver `LICENSE`). Lightbox2 es MIT (ver `lightbox2/LICENSE`).
- **Las obras, fotos y textos son de Dalila Jezabel Arzubi** y no están cubiertos por esas licencias.
