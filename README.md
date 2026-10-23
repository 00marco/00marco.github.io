# LivingNotes landing page

The static marketing site for LivingNotes, built with [Astro](https://astro.build/) and deployed to [00marco.github.io](https://00marco.github.io/) through GitHub Pages.

## Local development

This project requires Node.js 22.12 or newer and pnpm 10.

```sh
pnpm install
pnpm dev
```

Create a production build with:

```sh
pnpm build
```

The generated site is written to `dist/`. Pushes to `main` build and deploy that directory through `.github/workflows/astro.yaml`.

## Launch configuration

LivingNotes is currently presented as coming soon for iPhone and iPad. When the App Store listing is ready, set `APP_STORE_URL` in `src/config.ts` and update the launch badges in `src/pages/index.astro` to links.

The support inbox is also configured in `src/config.ts`. The support and terms pages both use that value.

## Public URLs

- `/` — LivingNotes landing page
- `/support/` — customer support contact and basic troubleshooting
- `/terms/` — basic website and app-use terms
- `/404.html` — branded not-found page

The included terms are a plain starter, not jurisdiction-specific legal advice. Have qualified counsel review them before relying on them as a custom legal agreement or App Store EULA.

## Screenshots

Optimized site images live in `public/images/`:

- `livingnotes-iphone.jpg` — main iPhone collection screen
- `livingnotes-ipad.jpg` — iPad collection screen
- `livingnotes-note.jpg` — focused iPhone note screen
- `livingnotes-preview.jpg` — social sharing preview

Preserve the filenames to replace an image without changing the page source. Export replacement JPEGs in sRGB at a quality of roughly 82–88%.
