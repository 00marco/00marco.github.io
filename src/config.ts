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

