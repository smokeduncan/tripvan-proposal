# TripVan × Sondri — Proposal

An animated HTML presentation (reveal.js + GSAP + a WebGL dithered Andes background), guided by **Raco**, TripVan's llama mascot.

- 🇨🇱 **Español (Chile):** https://smokeduncan.github.io/tripvan-proposal/es.html
- 🇬🇧 **English:** https://smokeduncan.github.io/tripvan-proposal/

## Presenting

- `←` `→` or space to move between slides · `F` fullscreen · `S` speaker notes · click Raco for a fun fact
- PDF: open the deck with `?print-pdf` (e.g. `es.html?print-pdf`), then print → Save as PDF (static version, no animation)

## Editing

`index.html` (English) is the source. After changing it, regenerate the Spanish version:

```bash
python tools/make_es.py
```

Photos in `assets/` come from tripvan.cl. The cartoon Raco is an original SVG drawn in `index.html`.
