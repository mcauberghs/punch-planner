"""
Punch Planner - logo / app icon generator
Version 1.3.0 (2026-11-07) - Mickael Cauberghs

Mickael Cauberghs, 2026-11-07: the logo shows a laser beam writing "8:00" on
a time card (I work in the laser industry). In v1.3.0 the time card and the
laser are much bigger, with less blue background around them, because the
icon looked too small on my phone's home screen.

Usage:  python3 tools/make_logo.py   (run from the repository folder)
Output: icon-192.png, icon-512.png, icon-maskable-512.png
"""
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
WORK = 2048            # draw large, then shrink (smooth edges)
K = WORK / 512.0       # 512-unit design grid -> working pixels

BLUE = (31, 95, 214, 255)
CARD = (247, 244, 236, 255)
INK = (150, 18, 12, 255)


def _blur_layer(img, draw_fn, radius):
    """Draw on a transparent layer, blur it, and put it on top of img."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(layer))
    return Image.alpha_composite(img, layer.filter(ImageFilter.GaussianBlur(radius)))


def draw_logo(size, scale=1.0):
    """Return the logo as an RGB image of size x size pixels.

    scale < 1 shrinks the drawing around the center, for the Android
    "maskable" icon that the launcher crops to a circle or squircle.
    """
    def P(x, y):
        return ((256 + (x - 256) * scale) * K, (256 + (y - 256) * scale) * K)

    def L(v):
        return v * K * scale

    # background: dark blue gradient
    img = Image.new("RGBA", (WORK, WORK))
    d = ImageDraw.Draw(img)
    for y in range(WORK):
        t = y / WORK
        d.line([(0, y), (WORK, y)], fill=(int(14 + 16 * t), int(26 + 20 * t), int(56 + 40 * t), 255))

    # time card with soft shadow
    x0, y0, x1, y1 = 26, 150, 486, 446
    img = _blur_layer(img, lambda g: g.rounded_rectangle(
        [*P(x0 + 6, y0 + 12), *P(x1 + 6, y1 + 12)], radius=L(34), fill=(0, 0, 0, 150)), L(16))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([*P(x0, y0), *P(x1, y1)], radius=L(34), fill=CARD)
    d.rounded_rectangle([*P(x0, y0), *P(x1, y0 + 58)], radius=L(34), fill=BLUE)
    d.rectangle([*P(x0, y0 + 30), *P(x1, y0 + 58)], fill=BLUE)
    hx, hy = P(256, y0 + 29)
    d.ellipse([hx - L(11), hy - L(11), hx + L(11), hy + L(11)], fill=(14, 26, 56, 255))
    d.line([P(x0 + 34, y1 - 36), P(x1 - 34, y1 - 36)], fill=(205, 200, 190, 255), width=int(L(6)))

    # burned time "8:00": red glow + dark burned core
    font = ImageFont.truetype(FONT, int(L(150)))
    text = "8:00"
    cx, cy = P(256, 318)
    img = _blur_layer(img, lambda g: g.text((cx, cy), text, font=font, fill=(255, 40, 30, 255), anchor="mm"), L(10))
    d = ImageDraw.Draw(img)
    d.text((cx, cy), text, font=font, fill=INK, anchor="mm")

    # contact point: on the stroke of the second "0"
    full = d.textbbox((cx, cy), text, font=font, anchor="mm")
    zero_left = full[0] + d.textlength("8:0", font=font)
    zero_w = full[2] - zero_left
    zero_h = full[3] - full[1]
    ex, ey = full[2] - zero_w * 0.11, full[1] + zero_h * 0.62

    # laser head (top right, close to the card) and beam
    sx, sy = P(436, 74)
    img = _blur_layer(img, lambda g: g.line([(sx, sy), (ex, ey)], fill=(255, 30, 20, 255), width=int(L(28))), L(14))
    d = ImageDraw.Draw(img)
    d.line([(sx, sy), (ex, ey)], fill=(255, 70, 50, 255), width=int(L(10)))
    d.line([(sx, sy), (ex, ey)], fill=(255, 235, 225, 255), width=int(L(4)))
    d.rounded_rectangle([sx - L(36), sy - L(36), sx + L(36), sy + L(36)], radius=L(12), fill=(60, 66, 80, 255))
    d.ellipse([sx - L(14), sy - L(14), sx + L(14), sy + L(14)], fill=(255, 80, 60, 255))

    # spark where the beam burns the card
    img = _blur_layer(img, lambda g: g.ellipse([ex - L(38), ey - L(38), ex + L(38), ey + L(38)],
                                               fill=(255, 120, 60, 230)), L(16))
    d = ImageDraw.Draw(img)
    for a in range(0, 360, 45):
        length = L(30 if a % 90 else 46)
        rad = math.radians(a + 20)
        d.line([(ex, ey), (ex + length * math.cos(rad), ey + length * math.sin(rad))],
               fill=(255, 220, 160, 255), width=int(L(5)))
    d.ellipse([ex - L(10), ey - L(10), ex + L(10), ey + L(10)], fill=(255, 255, 255, 255))

    return img.convert("RGB").resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    draw_logo(512).save("icon-512.png")
    draw_logo(192).save("icon-192.png")
    draw_logo(512, scale=0.80).save("icon-maskable-512.png")  # fits Android icon masks
    print("Icons written: icon-192.png, icon-512.png, icon-maskable-512.png")
