#!/usr/bin/env python3
"""Generate the deterministic landing-page Decay animations and repair frame."""

from __future__ import annotations

import colorsys
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "public" / "images"
PLANTS = IMAGES / "plants"

APP_BACKGROUND = (36, 38, 41, 255)
CARD_BACKGROUND = (48, 50, 54, 255)
TEXT_PRIMARY = (246, 246, 247, 255)
TEXT_SECONDARY = (174, 174, 180, 255)
DECAY_ORANGE = (199, 92, 26, 255)

FONT_ROOT = Path("/System/Library/Fonts")
FONT_SUPPLEMENTAL = FONT_ROOT / "Supplemental"
FONT_PATHS = [
    FONT_ROOT / "SFNSRounded.ttf",
    FONT_SUPPLEMENTAL / "Georgia Bold Italic.ttf",
    FONT_ROOT / "SFNSMono.ttf",
    FONT_SUPPLEMENTAL / "SnellRoundhand.ttc",
    FONT_ROOT / "Times.ttc",
    FONT_ROOT / "Noteworthy.ttc",
]


def font(path: Path, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size, index=index)


def decay_font(style: int, size: int) -> ImageFont.FreeTypeFont:
    path = FONT_PATHS[style % len(FONT_PATHS)]
    return font(path, size)


def rounded_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def draw_decay_glyph(
    image: Image.Image,
    position: tuple[int, int],
    character: str,
    size: int,
    style: int,
) -> int:
    draw = ImageDraw.Draw(image)
    glyph_font = decay_font(style, size)
    bbox = draw.textbbox((0, 0), character, font=glyph_font)
    text_width = max(1, bbox[2] - bbox[0])
    text_height = max(1, bbox[3] - bbox[1])
    width = max(math.ceil(size * 0.78), text_width + max(6, size // 3))
    height = math.ceil(size * 1.22)
    x, y = position
    rounded_rect(draw, (x, y, x + width, y + height), max(4, size // 5), DECAY_ORANGE)
    text_x = x + (width - text_width) / 2 - bbox[0]
    text_y = y + (height - text_height) / 2 - bbox[1]
    draw.text((text_x, text_y), character, font=glyph_font, fill=TEXT_PRIMARY)
    return width


def eligible_indices(text: str) -> list[int]:
    return [index for index, character in enumerate(text) if character in "AEIOUaeiou"]


def draw_wrapped_decay_text(
    image: Image.Image,
    text: str,
    box: tuple[int, int, int, int],
    decayed_count: int,
    style_seed: int,
    size: int,
    line_spacing: int,
) -> None:
    draw = ImageDraw.Draw(image)
    base_font = font(FONT_ROOT / "SFNSRounded.ttf", size)
    selected = set(eligible_indices(text)[:decayed_count])
    x0, y0, x1, _ = box
    x = x0
    y = y0
    line_height = size + line_spacing

    for index, character in enumerate(text):
        if character == "\n":
            x = x0
            y += line_height
            continue

        if index in selected:
            width = max(math.ceil(size * 0.78), size)
        else:
            bbox = draw.textbbox((0, 0), character, font=base_font)
            width = max(1, bbox[2] - bbox[0])

        if character != " " and x + width > x1:
            x = x0
            y += line_height

        if index in selected:
            x += draw_decay_glyph(
                image,
                (int(x), int(y - size * 0.08)),
                character,
                size,
                style_seed + index,
            )
            x += max(2, size // 10)
        else:
            draw.text((x, y), character, font=base_font, fill=TEXT_PRIMARY)
            x += width


def draw_repair_instruction(
    image: Image.Image,
    center_x: int,
    y: int,
    size: int,
    style: int,
) -> None:
    draw = ImageDraw.Draw(image)
    instruction_font = font(FONT_ROOT / "SFNSRounded.ttf", size)
    before = "Tap and hold "
    after = " to repair it"
    before_width = draw.textlength(before, font=instruction_font)
    after_width = draw.textlength(after, font=instruction_font)
    glyph_width = max(math.ceil(size * 0.78), size)
    total = before_width + glyph_width + after_width
    x = center_x - total / 2
    draw.text((x, y), before, font=instruction_font, fill=TEXT_SECONDARY)
    x += before_width
    actual_width = draw_decay_glyph(image, (int(x), int(y - size * 0.08)), "a", size, style)
    x += actual_width
    draw.text((x, y), after, font=instruction_font, fill=TEXT_SECONDARY)


def blur_and_dim_region(image: Image.Image, box: tuple[int, int, int, int]) -> None:
    crop = image.crop(box).filter(ImageFilter.GaussianBlur(radius=1.35))
    shade = Image.new("RGBA", crop.size, (15, 16, 18, 24))
    crop = Image.alpha_composite(crop.convert("RGBA"), shade)
    image.paste(crop, box[:2])


def quantize_frames(frames: list[Image.Image], colors: int = 112) -> list[Image.Image]:
    palette = frames[len(frames) // 2].convert("P", palette=Image.Palette.ADAPTIVE, colors=colors)
    return [
        frame.convert("RGB").quantize(palette=palette, dither=Image.Dither.FLOYDSTEINBERG)
        for frame in frames
    ]


def save_gif(
    frames: list[Image.Image],
    durations: list[int],
    gif_path: Path,
    poster_path: Path,
    poster_index: int,
) -> None:
    frames[poster_index].convert("RGB").save(poster_path, optimize=True)
    indexed = quantize_frames(frames)
    indexed[0].save(
        gif_path,
        save_all=True,
        append_images=indexed[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=1,
    )


def ipad_frame(step: int, frame_index: int) -> Image.Image:
    base = Image.open(IMAGES / "livingnotes-cards-ipad.png").convert("RGBA")
    base = base.resize((944, 656), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(base)

    cards = [
        {
            "instruction": (116, 116, 268, 157),
            "body": (51, 166, 305, 550),
            "center": 192,
            "text": "Lorem ipsum dolor sit amet",
            "count": math.ceil(step * 4 / 10),
        },
        {
            "instruction": (414, 116, 552, 157),
            "body": (349, 166, 597, 550),
            "center": 473,
            "text": "The quick brown fox jumps over the lazy dog",
            "count": step,
        },
        {
            "instruction": (710, 116, 862, 157),
            "body": (646, 166, 894, 550),
            "center": 770,
            "text": "Questions worth returning to later",
            "count": math.ceil(step * 4 / 10),
        },
    ]

    for card_index, card in enumerate(cards):
        instruction = card["instruction"]
        body = card["body"]
        draw.rectangle(instruction, fill=CARD_BACKGROUND)
        draw.rectangle(body, fill=CARD_BACKGROUND)
        count = int(card["count"])
        if count:
            draw_repair_instruction(base, int(card["center"]), 124, 11, frame_index + card_index)
        draw_wrapped_decay_text(
            base,
            str(card["text"]),
            body,
            count,
            frame_index + card_index * 2,
            22,
            10,
        )

    blur_and_dim_region(base, (0, 92, 318, 598))
    blur_and_dim_region(base, (625, 92, 944, 598))
    return base


def generate_ipad_animation() -> None:
    forward = list(range(0, 11))
    reverse = list(range(9, -1, -1))
    steps = forward + reverse
    frames = [ipad_frame(step, frame_index) for frame_index, step in enumerate(steps)]
    durations = [1050] + [420] * 9 + [1300] + [420] * 9 + [1050]
    save_gif(
        frames,
        durations,
        IMAGES / "livingnotes-decay-ipad.gif",
        IMAGES / "livingnotes-decay-ipad-poster.png",
        10,
    )


def yellow_plant(source: Image.Image, amount: float) -> Image.Image:
    image = source.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, alpha = pixels[x, y]
            if alpha < 8:
                continue
            hue, saturation, value = colorsys.rgb_to_hsv(red / 255, green / 255, blue / 255)
            is_green = 0.20 <= hue <= 0.48 and saturation > 0.12 and green > red * 0.92
            if not is_green:
                continue
            target = (224, 166, 43)
            blend = min(0.52, max(0.0, amount) * 0.52)
            pixels[x, y] = (
                round(red + (target[0] - red) * blend),
                round(green + (target[1] - green) * blend),
                round(blue + (target[2] - blue) * blend),
                alpha,
            )
    return image


def mac_frame(progress: float) -> Image.Image:
    base = Image.open(IMAGES / "livingnotes-garden-mac.png").convert("RGBA")
    base = base.resize((930, 746), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(base)
    card_x = [68, 336, 604]
    card_width = 258
    top = 145
    bottom = 647
    plant_files = sorted(PLANTS.glob("plant_foliage-*_pot-*_healthy.png"))
    usable_plants = [path for path in plant_files if "foliage-0" not in path.name]
    labels = [
        "Notes", "Questions", "Ideas", "Drafts", "Reading",
        "Research", "Plans", "Details", "Themes", "Sources",
        "People", "Places", "Threads", "Context", "Review",
    ]
    label_font = font(FONT_ROOT / "SFNSRounded.ttf", 10)

    for section_index, x0 in enumerate(card_x):
        draw.rectangle((x0 + 1, top, x0 + card_width - 1, bottom), fill=CARD_BACKGROUND)
        for slot in range(15):
            column = slot % 3
            row = slot // 3
            global_index = section_index * 15 + slot
            center_x = x0 + 43 + column * 86
            image_y = 164 + row * 94
            stagger = (global_index % 15) / 34
            local_progress = max(0.0, min(1.0, (progress - stagger) / max(0.01, 1 - stagger)))
            source_path = usable_plants[(slot * 7 + section_index * 11) % len(usable_plants)]
            plant = Image.open(source_path).convert("RGBA").resize((61, 63), Image.Resampling.LANCZOS)
            plant = yellow_plant(plant, local_progress)
            base.alpha_composite(plant, (center_x - 30, image_y))
            label = labels[slot]
            label_width = draw.textlength(label, font=label_font)
            draw.text(
                (center_x - label_width / 2, image_y + 62),
                label,
                font=label_font,
                fill=TEXT_PRIMARY,
            )
    return base


def generate_mac_animation() -> None:
    forward = [index / 11 for index in range(12)]
    reverse = [index / 11 for index in range(10, -1, -1)]
    progress_values = forward + reverse
    frames = [mac_frame(progress) for progress in progress_values]
    durations = [1100] + [330] * 10 + [1450] + [330] * 10 + [1100]
    save_gif(
        frames,
        durations,
        IMAGES / "livingnotes-decay-garden-mac.gif",
        IMAGES / "livingnotes-decay-garden-mac-poster.png",
        11,
    )


def generate_phone_repair_frame() -> None:
    image = Image.open(IMAGES / "livingnotes-decay-clean-iphone.png").convert("RGBA")
    draw = ImageDraw.Draw(image)

    draw.rectangle((315, 445, 862, 574), fill=CARD_BACKGROUND)
    draw_repair_instruction(image, 588, 474, 36, 3)

    draw.rectangle((170, 650, 1015, 840), fill=CARD_BACKGROUND)
    body_font_size = 58
    draw_wrapped_decay_text(
        image,
        "The quick brown fox jumps over the lazy dog",
        (180, 656, 1000, 840),
        1,
        1,
        body_font_size,
        16,
    )
    image.convert("RGB").save(IMAGES / "livingnotes-decay-decayed-iphone.png", optimize=True)


def main() -> None:
    generate_ipad_animation()
    generate_mac_animation()
    generate_phone_repair_frame()
    print("Generated landing-page Decay assets.")


if __name__ == "__main__":
    main()
