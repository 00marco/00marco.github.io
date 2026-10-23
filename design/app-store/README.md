# LivingNotes App Store listing artwork

Editable SVG sources for App Store product-page screenshots. Import an SVG into Figma and ungroup it to edit the typography, shapes, plant motifs, colors, and device frame.

## Artboards

### iPhone 6.9-inch portrait — 1320 × 2868

- `iphone/01-private-garden.svg`
- `iphone/02-shape-of-thinking.svg`
- `iphone/03-think-for-yourself.svg`

### iPad 13-inch landscape — 2752 × 2064

- `ipad/01-living-collection.svg`
- `ipad/02-space-to-think.svg`
- `ipad/03-no-competition.svg`

These dimensions are accepted by App Store Connect as of October 2026. Apple accepts one to ten screenshots per device group, but upload files must be PNG or JPEG without transparency—not SVG.

## Editing in Figma

1. Keep each SVG beside the `assets/` folder when first importing it. The SVGs reference the JPEG screenshots using relative paths.
2. Drag an SVG into Figma, then ungroup it.
3. Edit copy, colors, positioning, and vector plant shapes normally.
4. To replace an app screen, select the screenshot layer and replace its image fill in Figma.
5. Export at `1x` as PNG with a solid background and no alpha channel.

The source uses Georgia and Arial so text remains editable without requiring paid fonts. Swap them for your chosen brand typefaces inside Figma if desired.

## Art direction

The set follows the “Botanical Austerity” direction:

- deep forest-black backgrounds
- restrained chalk, moss, clay, and amber colors
- specimen-style plants and measured garden grids
- sparse, self-assured copy
- privacy, attention, and independent thought rather than productivity hype

Only the product screenshots are raster images. All presentation elements are vector and editable.
