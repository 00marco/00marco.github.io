# LivingNotes landing page

The static marketing site for LivingNotes, built with [Astro](https://astro.build/) and deployed to [00marco.github.io](https://00marco.github.io/) through GitHub Pages.

## Local development

This project requires Node.js 22.12 or newer. npm is included with Node.js.

```sh
npm install
npm run dev
```

Create a production build with:

```sh
npm run build
```

The generated site is written to `dist/`. Pushes to `main` build and deploy that directory through `.github/workflows/astro.yaml`.

Preview the production build locally with:

```sh
npm run preview
```

## Launch configuration

LivingNotes is currently presented as coming soon for iPhone and iPad. When the App Store listing is ready, set `APP_STORE_URL` in `src/config.ts` and update the launch badges in `src/pages/index.astro` to links.

The support inbox is also configured in `src/config.ts`. The support and terms pages both use that value.

## Public URLs

- `/` — LivingNotes landing page
- `/support/` — customer support contact and basic troubleshooting
- `/terms/` — basic website and app-use terms
- `/404.html` — branded not-found page

The included terms are a plain starter, not jurisdiction-specific legal advice. Have qualified counsel review them before relying on them as a custom legal agreement or App Store EULA.

## Editing and replacing images

Browser-ready image assets live in `public/images/`. All images currently used by the homepage are configured in one place: `src/config.ts` under `SITE_ASSETS`.

| File | Where it appears | Format guidance |
| --- | --- | --- |
| `livingnotes-iphone.jpg` | Hero phone | JPEG, sRGB |
| `livingnotes-decay-cutout.png` | Decay/card section | PNG with a genuinely transparent background |
| `decay-step-1-garden.png` | Workflow: yellow garden | PNG, 917 × 1715 px |
| `decay-step-2-open-note.png` | Workflow: opened note | PNG, 917 × 1715 px |
| `decay-step-3-hold.png` | Workflow: hold the caterpillar | PNG, 917 × 1715 px |
| `decay-step-4-repaired.png` | Workflow: repaired note | PNG, 917 × 1715 px |
| `livingnotes-preview.jpg` | Social sharing preview | JPEG, 1200 × 630 px |
| `favicon.svg` | Browser icon | SVG; stored directly in `public/` |

The following files are retained as source/reference screenshots but are not currently rendered on the homepage: `livingnotes-decay.png`, `livingnotes-ipad.jpg`, and `livingnotes-note.jpg`.

### Fastest replacement workflow

1. Open the existing file from `public/images/` in Photoshop.
2. Make your edits, or place your replacement artwork into a document with the same canvas dimensions.
3. Export it back into `public/images/` with the exact same filename, replacing the old exported file.
4. For JPEGs, export in sRGB at roughly 82–88% quality. For the phone cutout, export as PNG with transparency enabled.
5. Run `npm run dev` and refresh the browser. If the old image is cached, do a hard refresh.
6. Run `npm run build` before deploying.

Keeping the same filename and dimensions means no code changes are needed. If you change either, edit the corresponding `src`, `width`, and `height` values in `SITE_ASSETS` inside `src/config.ts`. Width and height should match the exported pixel dimensions; Astro uses them to reserve the correct layout space while the image loads.

The four `decay-step-*.png` files currently use normalized placeholder exports from the available screenshots. Replace them with four exact captures using the same `917 × 1715` canvas and consistent framing. Step 1 should show the yellow garden state, step 2 the affected note, step 3 the caterpillar and hold instruction, and step 4 the same note repaired.

Keep layered Photoshop working files outside `public/`—for example in a local `design-source/` folder—and export only flattened web assets into `public/images/`. Files inside `public/` are copied directly into the deployed website.

The large plant grid in the third section is not an image. Its plants, labels, colors, spacing, and fade are generated in `src/pages/index.astro`; edit `collectionNames` near the top of that file to change its labels.

The plant grid uses the transparent exports in `public/images/plants/`, copied from `ExportedAssets/Plants/`. The page deterministically shuffles foliage stages 0, 2, 3, 4, and 5 across all 5 pot designs, so the arrangement looks varied without jumping around between page loads. Foliage stage 1 is intentionally excluded. Four spaced-out plants use the 10%, 25%, 50%, and 100% decay exports, six additional plants have a randomized selection of yellow leaves, and four hybrids combine the exported pots with the LivingNotes logo seedling.
