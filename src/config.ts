// Set this to the App Store listing when LivingNotes is released.
export const APP_STORE_URL: string | null = null;

// Replace this address with the inbox used for customer support.
export const SUPPORT_EMAIL = "support@livingnotes.app";

// Replace files in public/images/ while keeping these filenames, or update the
// paths and dimensions here when exporting an asset with a different size.
export const SITE_ASSETS = {
  heroPhone: {
    src: "/images/livingnotes-iphone.jpg",
    width: 354,
    height: 768,
    alt: "LivingNotes on iPhone showing a visual garden of note collections",
  },
  decayPhone: {
    src: "/images/livingnotes-decay-cutout.png",
    width: 917,
    height: 1715,
    alt: "LivingNotes on iPhone showing a caterpillar obscuring a vowel in a note and instructions to press and hold it for two seconds",
  },
  decayWorkflow: [
    {
      src: "/images/decay-step-1-garden.png",
      width: 917,
      height: 1715,
      alt: "LivingNotes garden with a yellowing plant indicating a collection that needs attention",
    },
    {
      src: "/images/decay-step-2-open-note.png",
      width: 917,
      height: 1715,
      alt: "An affected note opened in LivingNotes",
    },
    {
      src: "/images/decay-step-3-hold.png",
      width: 917,
      height: 1715,
      alt: "A caterpillar obscuring a vowel with instructions to press and hold it for two seconds",
    },
    {
      src: "/images/decay-step-4-repaired.png",
      width: 917,
      height: 1715,
      alt: "The LivingNotes card repaired with its complete text visible again",
    },
  ],
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

