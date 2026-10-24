#!/usr/bin/env python3
"""Generate portable Living Notes plant art and listing-screen PNGs."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

ROOT = Path(__file__).resolve().parent
PLANTS = ROOT / "Plants"
SCREENS = ROOT / "Screens"
PLANTS.mkdir(parents=True, exist_ok=True)
SCREENS.mkdir(parents=True, exist_ok=True)

BG = (36, 38, 41)
CARD = (48, 50, 54)
BORDER = (94, 98, 107)
WHITE = (245, 245, 247)
MUTED = (171, 174, 181)
GREEN = (113, 140, 105)
YELLOW = (232, 176, 51)
ORANGE = (199, 92, 26)


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Geneva.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size, index=1 if bold and path.endswith(".ttc") else 0)
        except OSError:
            pass
    return ImageFont.load_default()


def mix(a, b, amount):
    return tuple(round(a[i] + (b[i] - a[i]) * amount) for i in range(3))


def rounded_gradient(image, box, radius, top, middle, bottom, outline=None, rotation=0):
    x0, y0, x1, y1 = map(int, box)
    w, h = max(1, x1 - x0), max(1, y1 - y0)
    pad = max(w, h)
    layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    mask = Image.new("L", layer.size, 0)
    md = ImageDraw.Draw(mask)
    inner = (pad, pad, pad + w, pad + h)
    md.rounded_rectangle(inner, radius=radius, fill=255)
    grad = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(h):
        p = y / max(1, h - 1)
        if p < .48:
            c = mix(top, middle, p / .48)
        else:
            c = mix(middle, bottom, (p - .48) / .52)
        gd.line((pad, pad + y, pad + w, pad + y), fill=(*c, 255))
    layer.alpha_composite(Image.composite(grad, Image.new("RGBA", layer.size), mask))
    if outline:
        ImageDraw.Draw(layer).rounded_rectangle(inner, radius=radius, outline=outline, width=max(1, w // 22))
    if rotation:
        layer = layer.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True)
    px = int((x0 + x1 - layer.width) / 2)
    py = int((y0 + y1 - layer.height) / 2)
    image.alpha_composite(layer, (px, py))


LEAVES = {
    1: [(44, 64, 17, 11), (60, 61, 18, 12)],
    2: [(52, 27, 22, 15), (38, 43, 27, 17), (66, 45, 27, 17)],
    3: [(52, 24, 24, 17), (34, 39, 31, 20), (70, 40, 30, 20), (46, 55, 34, 21)],
    4: [(52, 20, 28, 19), (31, 35, 36, 22), (74, 37, 34, 22), (39, 54, 39, 24), (68, 56, 38, 24)],
    5: [(53, 17, 32, 21), (29, 31, 39, 24), (77, 33, 37, 23), (20, 50, 36, 23), (52, 48, 43, 26), (82, 52, 36, 23), (39, 67, 45, 25)],
}


def plant_image(foliage, pot_stage, decay=0, variant=0, output_size=624):
    s = 6
    im = Image.new("RGBA", (104 * s, 108 * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pot_top = (80 - min(4, pot_stage)) * s
    leaves = LEAVES.get(foliage, [])
    if foliage:
        trunk = (120, 77, 51, 255)
        d.line((52*s, pot_top+2*s, 52*s, (59 if foliage == 1 else 26)*s), fill=trunk, width=(15 if foliage < 4 else 19))
        if foliage != 1:
            for cx, cy, _, _ in leaves:
                d.line((52*s, min(pot_top, (cy+5)*s), cx*s, cy*s), fill=trunk, width=10)
        damaged = max(1, math.ceil(len(leaves) * decay / 100)) if decay else 0
        order = sorted(range(len(leaves)), key=lambda i: (i*37 + variant*17) % max(1, len(leaves)))
        damaged_set = set(order[:damaged])
        for i, (cx, cy, w, h) in enumerate(leaves):
            color = GREEN
            if i in damaged_set:
                color = mix(YELLOW, ORANGE, min(1, decay / 35))
            top = mix(color, (0, 0, 0), .12)
            bottom = mix(color, (255, 255, 255), .14)
            if foliage == 1:
                # Compact pointed seedling leaves.
                leaf = Image.new("RGBA", (w*s*3, h*s*3), (0, 0, 0, 0))
                ld = ImageDraw.Draw(leaf)
                pts = [(w*s, h*s*1.5), (w*s*1.55, h*s*.55), (w*s*2, h*s*1.5), (w*s*1.45, h*s*2.45)]
                ld.polygon(pts, fill=(*color, 255), outline=(0, 0, 0, 34))
                leaf = leaf.rotate(-16 if i == 0 else 16, resample=Image.Resampling.BICUBIC, expand=True)
                im.alpha_composite(leaf, (int(cx*s-leaf.width/2), int(cy*s-leaf.height/2)))
            else:
                rounded_gradient(im, ((cx-w/2)*s, (cy-h/2)*s, (cx+w/2)*s, (cy+h/2)*s), h*s*.45, top, color, bottom, (0, 0, 0, 34))

    widths = [(57, 41), (61, 43), (65, 46), (69, 49), (73, 52)]
    rim_w, base_w = widths[max(0, min(4, pot_stage))]
    palettes = [(110,97,87), (130,94,74), (153,99,69), (173,107,69), (194,120,74)]
    clay = palettes[max(0, min(4, pot_stage))]
    pts = [((52-rim_w/2+4)*s, (pot_top/s+6)*s), ((52+rim_w/2-4)*s, (pot_top/s+6)*s), ((52+base_w/2)*s, 103*s), ((52-base_w/2)*s, 103*s)]
    d.polygon(pts, fill=(*clay,255), outline=(0,0,0,42))
    d.rounded_rectangle(((52-rim_w/2)*s, pot_top, (52+rim_w/2)*s, pot_top+10*s), radius=4*s, fill=(*mix(clay,(255,255,255),pot_stage*.025),255), outline=(0,0,0,40), width=4)
    if pot_stage >= 1:
        d.rounded_rectangle(((52-base_w/2+4)*s, 102*s, (52-base_w/2+17)*s, 107*s), radius=2*s, fill=(*clay,235))
        d.rounded_rectangle(((52+base_w/2-17)*s, 102*s, (52+base_w/2-4)*s, 107*s), radius=2*s, fill=(*clay,235))
    if pot_stage >= 2:
        d.arc(((52-base_w/2+3)*s, (pot_top/s+10)*s, (52+base_w/2-3)*s, (pot_top/s+22)*s), 5, 175, fill=(255,255,255,45), width=5)
    if pot_stage >= 3:
        d.line(((52-base_w/2+5)*s, (pot_top/s+23)*s, (52+base_w/2-5)*s, (pot_top/s+23)*s), fill=(0,0,0,36), width=5)
    if pot_stage >= 4:
        cx, cy = 52*s, (pot_top/s+25)*s
        d.polygon([(cx,cy-30),(cx+30,cy),(cx,cy+30),(cx-30,cy)], outline=(255,255,255,70), width=6)
    if output_size != im.width:
        im = im.resize((output_size, round(output_size * 108/104)), Image.Resampling.LANCZOS)
    return im


def fit_text(draw, text, box_width, start_size, bold=False):
    size = start_size
    while size > 12:
        f = font(size, bold)
        if draw.textbbox((0,0), text, font=f)[2] <= box_width:
            return f
        size -= 2
    return font(size, bold)


def draw_toolbar(im, title, right="search_plus", back=False):
    d = ImageDraw.Draw(im)
    w = im.width
    y = int(im.height*.045)
    if back:
        d.ellipse((32,y-28,88,y+28), fill=(25,27,29), outline=(70,73,78), width=2)
        d.line((63,y-12,51,y,63,y+12), fill=WHITE, width=5, joint="curve")
    else:
        d.ellipse((32,y-28,88,y+28), fill=(25,27,29), outline=(70,73,78), width=2)
        d.ellipse((52,y-10,68,y+6), outline=WHITE, width=4)
        d.line((60,y-18,60,y+14), fill=WHITE, width=4)
    f = font(max(28,int(w*.025)), True)
    bbox=d.textbbox((0,0),title,font=f); d.text(((w-bbox[2])/2,y-bbox[3]/2),title,font=f,fill=WHITE)
    if right == "search_plus":
        x=w-118
        d.rounded_rectangle((x-38,y-30,w-28,y+30),radius=28,fill=(25,27,29),outline=(70,73,78),width=2)
        d.ellipse((x-18,y-12,x+4,y+10),outline=WHITE,width=4); d.line((x,y+7,x+13,y+20),fill=WHITE,width=4)
        d.line((w-61,y-13,w-61,y+13),fill=WHITE,width=4); d.line((w-74,y,w-48,y),fill=WHITE,width=4)
    elif right == "settings_plus":
        x=w-122
        d.rounded_rectangle((x-28,y-30,w-28,y+30),radius=28,fill=(25,27,29),outline=(70,73,78),width=2)
        d.ellipse((x-4,y-10,x+16,y+10),outline=WHITE,width=4)
        d.line((w-61,y-13,w-61,y+13),fill=WHITE,width=4); d.line((w-74,y,w-48,y),fill=WHITE,width=4)


def card_box(im, top, bottom, margin):
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((margin,top,im.width-margin,bottom),radius=34,fill=CARD,outline=BORDER,width=2)
    return (margin,top,im.width-margin,bottom)


def paste_plant(im, x, y, stage, pot, decay=0, size=150):
    p=plant_image(stage,pot,decay,variant=x+y,output_size=size)
    im.alpha_composite(p,(int(x-p.width/2),int(y-p.height/2)))


def garden_screen(size):
    w,h=size
    im=Image.new("RGBA",size,(*BG,255))
    glow=Image.new("RGBA",size,(0,0,0,0)); gd=ImageDraw.Draw(glow); gd.ellipse((w*.58,-h*.1,w*1.15,h*.45),fill=(35,88,51,70)); glow=glow.filter(ImageFilter.GaussianBlur(w*.12)); im.alpha_composite(glow)
    draw_toolbar(im,"", "search_plus")
    top=int(h*.14); bottom=int(h*.86); margin=int(w*.075)
    x0,y0,x1,y1=card_box(im,top,bottom,margin); d=ImageDraw.Draw(im)
    header=int((y1-y0)*.09); d.line((x0+35,y0+header,x1-35,y0+header),fill=mix(CARD,WHITE,.16),width=2)
    title="Ideas"; tf=font(int(w*.043),True); tb=d.textbbox((0,0),title,font=tf); d.text(((w-tb[2])/2,y0+header*.28),title,font=tf,fill=WHITE)
    names=["Essays","Project Notes","Watchlist","Builds","Venture Ideas","Todo","Recipes","Reading","Design","Journal","Research","Trips"]
    stages=[5,4,2,3,4,1,3,2,5,1,4,2]
    cols=4; cellw=(x1-x0-70)/cols; cellh=(y1-y0-header-110)/5
    pf=font(max(16,int(w*.027)),True)
    for i,(name,stage) in enumerate(zip(names,stages)):
        row,col=divmod(i,cols); cx=x0+35+cellw*(col+.5); cy=y0+header+cellh*(row+.40)
        paste_plant(im,cx,cy,stage,(i+1)%5,25 if i in (2,6) else 0,size=int(min(cellw*.65,130)))
        label_y=cy+cellh*.30; f=fit_text(d,name,cellw-8,pf.size,True); bb=d.textbbox((0,0),name,font=f); d.text((cx-bb[2]/2,label_y),name,font=f,fill=WHITE)
    footer=y1-int((y1-y0)*.07); d.line((x0+35,footer,x1-35,footer),fill=mix(CARD,WHITE,.16),width=2)
    d.text((x0+30,footer+22),"□",font=font(int(w*.035)),fill=MUTED); frac="1 / 3"; ff=font(int(w*.026),True); fb=d.textbbox((0,0),frac,font=ff); d.text((x1-35-fb[2],footer+26),frac,font=ff,fill=MUTED)
    dots_y=int(h*.93)
    for i in range(3): d.ellipse((w/2-24+i*22,dots_y,w/2-14+i*22,dots_y+10),fill=WHITE if i==0 else (100,102,106))
    return im


def caterpillar(draw,x,y,r):
    red=(196,91,73); width=max(2,r//4)
    for offset,scale in [(-.62,.68),(0,.82),(.70,.62)]:
        rr=r*scale; cx=x+r*offset
        draw.ellipse((cx-rr,y-rr,cx+rr,y+rr),fill=(20,21,22),outline=red,width=width)
    draw.line((x+r*.92,y-r*.42,x+r*1.24,y-r*.85),fill=red,width=width)
    draw.line((x+r*.92,y-r*.42,x+r*1.35,y-r*.28),fill=red,width=width)


def note_screen(size):
    w,h=size; im=Image.new("RGBA",size,(*BG,255)); draw_toolbar(im,"Project Notes","settings_plus",back=True)
    top=int(h*.14); bottom=int(h*.86); margin=int(w*.075); x0,y0,x1,y1=card_box(im,top,bottom,margin); d=ImageDraw.Draw(im)
    control=int(w*.047); cy=y0+65
    control_fill=mix(CARD,WHITE,.07)
    d.ellipse((x0+28,cy-control,x0+28+control*2,cy+control),fill=control_fill); d.text((x0+48,cy-control*.52),"•••",font=font(int(control*.75),True),fill=WHITE)
    d.ellipse((x1-28-control*2,cy-control,x1-28,cy+control),fill=control_fill); d.line((x1-28-control*1.32,cy+control*.25,x1-28-control*.68,cy-control*.38),fill=WHITE,width=5)
    helper_left="Tap and hold a"; helper_right="for 2 seconds to repair it."; hf=font(int(w*.027),True)
    lw=d.textbbox((0,0),helper_left,font=hf)[2]; rw=d.textbbox((0,0),helper_right,font=hf)[2]; icon_gap=max(30,int(w*.045)); hx=(w-lw-icon_gap-rw)/2
    d.text((hx,cy-hf.size*.5),helper_left,font=hf,fill=MUTED); caterpillar(d,int(hx+lw+icon_gap*.45),cy,max(7,int(w*.010))); d.text((hx+lw+icon_gap,cy-hf.size*.5),helper_right,font=hf,fill=MUTED)
    d.line((x0+35,cy+62,x1-35,cy+62),fill=mix(CARD,WHITE,.16),width=2)
    body="Ideas become clearer when they have room to grow. Capture the thought, revisit it tomorrow, and let the useful parts take root."
    bf=font(int(w*.048)); maxw=x1-x0-76; words=body.split(); lines=[]; line=""
    for word in words:
        test=(line+" "+word).strip()
        if d.textbbox((0,0),test,font=bf)[2]>maxw: lines.append(line); line=word
        else: line=test
    lines.append(line); tx=x0+38; ty=cy+96
    for li,line in enumerate(lines):
        d.text((tx,ty+li*int(w*.065)),line,font=bf,fill=WHITE)
    # A few soft-red caterpillars aligned with the text flow.
    for ox,oy in [(tx+maxw*.25,ty+5),(tx+maxw*.72,ty+int(w*.065)+5),(tx+maxw*.42,ty+int(w*.13)+5)]: caterpillar(d,int(ox),int(oy),int(w*.015))
    frac="1 / 4"; ff=font(int(w*.028),True); fb=d.textbbox((0,0),frac,font=ff); d.text((x1-35-fb[2],y1-55),frac,font=ff,fill=MUTED)
    dots_y=int(h*.93)
    for i in range(4): d.ellipse((w/2-36+i*22,dots_y,w/2-26+i*22,dots_y+10),fill=WHITE if i==0 else (100,102,106))
    return im


def search_screen(size):
    w,h=size; im=Image.new("RGBA",size,(*BG,255)); d=ImageDraw.Draw(im)
    u=min(w,h*.72)
    title="Search"; tf=font(int(u*.042),True); tb=d.textbbox((0,0),title,font=tf); d.text(((w-tb[2])/2,int(h*.055)),title,font=tf,fill=WHITE); d.text((35,int(h*.055)),"Cancel",font=font(int(u*.034)),fill=WHITE)
    sx,sy,sw,sh=int(w*.05),int(h*.115),int(w*.90),int(h*.065); d.rounded_rectangle((sx,sy,sx+sw,sy+sh),radius=sh//2,fill=(55,57,62)); d.ellipse((sx+24,sy+sh*.28,sx+24+sh*.32,sy+sh*.60),outline=MUTED,width=4); d.line((sx+24+sh*.25,sy+sh*.55,sx+24+sh*.42,sy+sh*.72),fill=MUTED,width=4); d.text((sx+70,sy+sh*.22),"project",font=font(int(u*.034)),fill=WHITE)
    y=sy+sh+55; sections=[("Section 1",[("Project Notes","Design decisions and next steps · 2 / 5"),("Builds","Project launch checklist · 1 / 3")]),("Section 3",[("Venture Ideas","A small project for thoughtful teams · 4 / 6")])]
    for sec,rows in sections:
        d.text((sx,y),sec.upper(),font=font(int(u*.023),True),fill=MUTED); y+=42
        for idx,(name,sub) in enumerate(rows):
            rh=int(h*.082); d.rounded_rectangle((sx,y,sx+sw,y+rh),radius=18,fill=CARD,outline=(78,81,87),width=2)
            d.text((sx+30,y+rh*.18),"●",font=font(int(u*.032)),fill=GREEN); d.text((sx+76,y+rh*.12),name,font=font(int(u*.034),True),fill=WHITE); d.text((sx+76,y+rh*.55),sub,font=font(int(u*.025)),fill=MUTED); d.text((sx+sw-42,y+rh*.26),"›",font=font(int(u*.045)),fill=MUTED); y+=rh+14
        y+=30
    return im


def save_exports():
    for foliage in range(6):
        for pot in range(5):
            plant_image(foliage,pot,0,foliage*10+pot).save(PLANTS/f"plant_foliage-{foliage}_pot-{pot}_healthy.png")
    for decay in (10,25,50,100):
        plant_image(5,4,decay,42).save(PLANTS/f"plant_foliage-5_pot-4_decay-{decay}.png")
    yellow_variants = [
        (2, 0, 25, 11),
        (3, 2, 25, 22),
        (4, 1, 25, 33),
        (5, 3, 25, 44),
        (3, 4, 50, 55),
        (4, 0, 50, 66),
    ]
    for foliage, pot, decay, variant in yellow_variants:
        plant_image(foliage, pot, decay, variant).save(
            PLANTS / f"plant_foliage-{foliage}_pot-{pot}_decay-{decay}.png"
        )

    sheet=Image.new("RGBA",(6*220,5*235),(28,30,32,255)); sd=ImageDraw.Draw(sheet)
    for pot in range(5):
        for foliage in range(6):
            p=plant_image(foliage,pot,0,foliage*10+pot,180); x=foliage*220+20; y=pot*235+8; sheet.alpha_composite(p,(x,y)); label=f"{foliage} note{'s' if foliage != 1 else ''} · pot {pot}"; f=font(20,True); bb=sd.textbbox((0,0),label,font=f); sd.text((foliage*220+110-bb[2]/2,pot*235+205),label,font=f,fill=WHITE)
    sheet.save(PLANTS / "plant_contact_sheet.png")

    devices={"iphone-15":(1179,2556),"ipad-11-landscape":(2388,1668)}
    makers={"01-garden":garden_screen,"02-note-thread":note_screen,"03-search":search_screen}
    for device,size in devices.items():
        for name,maker in makers.items(): maker(size).convert("RGB").save(SCREENS/f"{device}_{name}.png",quality=95)


if __name__ == "__main__":
    save_exports()
    print(f"Exported assets to {ROOT}")
