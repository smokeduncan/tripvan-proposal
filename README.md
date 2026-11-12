# TripVan × Sondri — Proposal

An animated HTML presentation (reveal.js + GSAP + a WebGL dithered Andes background), guided by **Raco**, TripVan's llama mascot.

- 🇨🇱 **Español (Chile):** https://smokeduncan.github.io/tripvan-proposal/es.html
- 🇬🇧 **English:** https://smokeduncan.github.io/tripvan-proposal/

## Presenting

- `←` `→` or space to move between slides · `F` fullscreen · `S` speaker notes · click Raco for a fun fact
- PDF: open the deck with `?print-pdf` (e.g. `es.html?print-pdf`), then print → Save as PDF (static version, no animation)

## Editing in the browser

Press **E** (or click **✎ Edit** / **✎ Editar**) on any slide, click any text and type.
The toolbar has **◀ ▶** to move between slides, a box for what Raco says on that slide,
**⬇ Download HTML** (saves a copy of the deck with your edits built in) and **↺ Reset**.
Edits auto-save in your browser only. To publish them, replace `index.html` / `es.html`
in this repo with the downloaded file.

## Editing the source

`index.html` (English) is the source. After changing it, regenerate the Spanish version:

```bash
python tools/make_es.py
```

Photos in `assets/` come from tripvan.cl. The cartoon Raco is an original SVG drawn in `index.html`.

## The Blueprint (action plan & timeline)

`blueprint.html` is the second page: the three phases as a house being built, the TripVan Social
app mockups, the action items and the booking link. It holds both languages in one file
(`blueprint.html?lang=es` for Spanish). Reach it from the **Action plan & timeline →** button at
the top of the proposal, or the **The Blueprint →** button on its last slide. Press `I` to replay the intro.
