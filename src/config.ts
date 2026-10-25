// Set this to the App Store listing when LivingNotes is released.
export const APP_STORE_URL: string | null = null;

// Replace this address with the inbox used for customer support.
export const SUPPORT_EMAIL = "support@livingnotes.app";

// Replace files in public/images/ while keeping these filenames, or update the
// paths and dimensions here when exporting an asset with a different size.
export const SITE_ASSETS = {
  heroPhone: {
    src: "/images/livingnotes-garden-iphone.png",
    width: 1206,
    height: 2622,
    alt: "LivingNotes on iPhone showing a visual garden of note collections",
  },
  heroTablet: {
    src: "/images/livingnotes-overview-ipad.png",
    width: 2360,
    height: 1640,
    alt: "LivingNotes on iPad showing three garden sections",
  },
  heroMac: {
    src: "/images/livingnotes-garden-mac.png",
    width: 2326,
    height: 1864,
    alt: "LivingNotes on Mac showing Ideas, Projects, and Life gardens",
  },
  decayPhone: {
    src: "/images/livingnotes-decay-cutout.png",
    width: 917,
    height: 1715,
    alt: "LivingNotes on iPhone showing a caterpillar obscuring a vowel in a note and instructions to press and hold it for two seconds",
  },
  decayWorkflow: [
    {
      src: "/images/livingnotes-garden-iphone.png",
      width: 1206,
      height: 2622,
      alt: "LivingNotes garden with a yellowing plant indicating a collection that needs attention",
    },
    {
      src: "/images/livingnotes-decay-before-iphone.png",
      width: 1206,
      height: 2622,
      alt: "A LivingNotes card with a caterpillar covering a vowel and instructions to press and hold it",
    },
    {
      src: "/images/livingnotes-decay-after-iphone.png",
      width: 1206,
      height: 2622,
      alt: "The LivingNotes card repaired with its complete text visible again",
    },
  ],
  featureCards: {
    src: "/images/livingnotes-cards-ipad.png",
    width: 2360,
    height: 1640,
    alt: "LivingNotes on iPad showing several short note cards in a horizontal rail",
  },
  featureGarden: {
    src: "/images/livingnotes-garden-mac.png",
    width: 2326,
    height: 1864,
    alt: "LivingNotes on Mac showing three finite garden plots with open slots",
  },
  socialPreview: {
    src: "/images/livingnotes-preview.jpg",
    width: 1200,
    height: 630,
    alt: "LivingNotes social sharing preview",
  },
  favicon: {
    src: "/favicon.svg",
  },
} as const;

