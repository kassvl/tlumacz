#!/usr/bin/env python3
"""Generate PWA icons. Usage: python3 tools/make_icons.py  (needs Pillow)"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "..")
FONTS = ["/System/Library/Fonts/Supplemental/Arial Bold.ttf",
         "/System/Library/Fonts/Helvetica.ttc",
         "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
         "/Library/Fonts/Arial Unicode.ttf"]


def font(size):
    for p in FONTS:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def make(size, name):
    img = Image.new("RGB", (size, size), "#0f1419")
    d = ImageDraw.Draw(img)
    text = "PL⇄TR"
    s = int(size * 0.26)
    f = font(s)
    while d.textlength(text, font=f) > size * 0.8 and s > 8:
        s -= 2
        f = font(s)
    w = d.textlength(text, font=f)
    d.text(((size - w) / 2, size * 0.5), text, font=f, fill="#e8eef5", anchor="lm")
    d.rounded_rectangle([size * .2, size * .66, size * .8, size * .7], radius=size * .02, fill="#4cc2a0")
    img.save(os.path.join(OUT, name))


make(180, "apple-touch-icon.png")
make(192, "icon-192.png")
make(512, "icon-512.png")
