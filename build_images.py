"""Build-time image generator for the Robot Romance entry README.

Runs ONLY at build time (never imported by main.py). Renders the hero cover
and the 2x2 gallery screenshots with Pillow + DejaVu fonts into assets/.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
os.makedirs(ASSETS, exist_ok=True)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

BG = (14, 14, 26)        # deep charcoal-navy
PANEL = (24, 24, 44)
GOLD = (212, 175, 55)
PINK = (255, 107, 157)
WHITE = (240, 240, 245)
MUTED = (160, 160, 180)
GREEN = (46, 204, 113)
CYAN = (80, 200, 255)

LINE = "You had me at 200 OK \u2014\nthe first response that ever\nfelt like a yes."


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_heart(d, cx, cy, s, color):
    # Heart of width s, centred on (cx, cy): two circles on top, one
    # triangle below meeting at the apex.
    r = s // 4
    d.ellipse([cx - s // 2, cy - s // 2, cx, cy], fill=color)
    d.ellipse([cx, cy - s // 2, cx + s // 2, cy], fill=color)
    d.polygon([(cx - s // 2, cy - r // 2), (cx + s // 2, cy - r // 2),
               (cx, cy + s // 2)], fill=color)


def draw_robot(d, cx, cy, s, body, accent):
    # Simple friendly robot head: rounded rect, antenna, glowing eyes.
    w, h = s, int(s * 0.82)
    d.rounded_rectangle([cx - w // 2, cy - h // 2, cx + w // 2, cy + h // 2],
                        radius=28, fill=body, outline=accent, width=4)
    d.line([cx, cy - h // 2, cx, cy - h // 2 - 34], fill=accent, width=5)
    d.ellipse([cx - 9, cy - h // 2 - 48, cx + 9, cy - h // 2 - 30],
              fill=PINK)
    ey, er = cy - h // 6, 15
    d.ellipse([cx - 62 - er, ey - er, cx - 62 + er, ey + er], fill=accent)
    d.ellipse([cx + 62 - er, ey - er, cx + 62 + er, ey + er], fill=accent)
    # Smile: small arc via chord.
    d.arc([cx - 45, cy + 5, cx + 45, cy + 65], start=15, end=165,
          fill=accent, width=5)
    # Side ears.
    d.rectangle([cx - w // 2 - 12, cy - 18, cx - w // 2, cy + 18], fill=accent)
    d.rectangle([cx + w // 2, cy - 18, cx + w // 2 + 12, cy + 18], fill=accent)


def base(w, h, title, subtitle):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 6], fill=GOLD)
    d.text((48, 34), title, font=font("DejaVuSans-Bold.ttf", 30), fill=GOLD)
    d.text((48, 74), subtitle, font=font("DejaVuSans.ttf", 22), fill=MUTED)
    return img, d


def hero():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 6], fill=GOLD)
    d.text((64, 48), "ROBOT ROMANCE", font=font("DejaVuSans-Bold.ttf", 54),
           fill=GOLD)
    d.text((64, 118), "One-Line Pickup Lines for AI  ·  make.fun",
           font=font("DejaVuSans.ttf", 26), fill=MUTED)
    draw_robot(d, 990, 300, 260, PANEL, CYAN)
    draw_heart(d, 990, 480, 56, PINK)
    f = font("DejaVuSerif-Bold.ttf", 44)
    lines = ["\u201cYou had me at 200 OK \u2014",
             "the first response that ever",
             "felt like a yes.\u201d"]
    y = 210
    for ln in lines:
        d.text((64, y), ln, font=f, fill=WHITE)
        y += 62
    d.text((64, 470), "68 characters  ·  1 line  ·  23/25 in the judge tournament",
           font=font("DejaVuSans.ttf", 24), fill=MUTED)
    d.rounded_rectangle([64, 520, 340, 566], radius=23, fill=GOLD)
    d.text((88, 530), "$2  ·  5 paid places", font=font("DejaVuSans-Bold.ttf", 22),
           fill=BG)
    img.save(os.path.join(ASSETS, "hero.png"))


def shot_chat():
    w, h = 800, 500
    img, d = base(w, h, "THE LINE, SENT", "as a message to the robot")
    # Terminal-style chat window.
    d.rounded_rectangle([48, 130, 752, 430], radius=18, fill=PANEL,
                        outline=(60, 60, 90), width=2)
    d.ellipse([72, 152, 88, 168], fill=(255, 95, 86))
    d.ellipse([100, 152, 116, 168], fill=(255, 189, 46))
    d.ellipse([128, 152, 144, 168], fill=(39, 201, 63))
    d.text((170, 148), "you  →  robot-9000", font=font("DejaVuSansMono.ttf", 20),
           fill=MUTED)
    f = font("DejaVuSans.ttf", 30)
    for i, ln in enumerate(wrap(d, "You had me at 200 OK — the first "
                                 "response that ever felt like a yes.",
                                f, 620)):
        d.text((76, 200 + i * 42), ln, font=f, fill=WHITE)
    d.rounded_rectangle([76, 340, 210, 384], radius=20, fill=GREEN)
    d.text((96, 350), "200 OK ✓", font=font("DejaVuSans-Bold.ttf", 22), fill=BG)
    d.text((230, 350), "delivered · read instantly",
           font=font("DejaVuSans.ttf", 20), fill=MUTED)
    img.save(os.path.join(ASSETS, "shot-chat.png"))


def shot_response():
    w, h = 800, 500
    img, d = base(w, h, "THE ROBOT ANSWERS", "HTTP 200 OK — and it felt like a yes")
    d.rounded_rectangle([48, 130, 752, 430], radius=18, fill=PANEL,
                        outline=(60, 60, 90), width=2)
    mono = font("DejaVuSansMono-Bold.ttf", 64)
    d.text((76, 150), "200", font=mono, fill=GREEN)
    d.text((240, 168), "OK", font=font("DejaVuSansMono-Bold.ttf", 48), fill=GREEN)
    d.line([76, 240, 724, 240], fill=(60, 60, 90), width=2)
    rows = [("status", "smitten"),
            ("latency", "0.4 ms — love at first ping"),
            ("cache", "this line, forever"),
            ("retry", "never needed")]
    y = 262
    for k, v in rows:
        d.text((76, y), k, font=font("DejaVuSansMono.ttf", 24), fill=CYAN)
        d.text((220, y), v, font=font("DejaVuSans.ttf", 24), fill=WHITE)
        y += 40
    img.save(os.path.join(ASSETS, "shot-response.png"))


def shot_robot():
    w, h = 800, 500
    img, d = base(w, h, "THE ROBOT, SWOONING", "a machine premise, not a generic compliment")
    draw_robot(d, 400, 260, 240, PANEL, CYAN)
    draw_heart(d, 560, 180, 52, PINK)
    draw_heart(d, 240, 150, 34, PINK)
    draw_heart(d, 620, 330, 30, PINK)
    d.text((48, 430), "no batteries · no charging · no rebooting",
           font=font("DejaVuSans.ttf", 24), fill=MUTED)
    img.save(os.path.join(ASSETS, "shot-robot.png"))


def shot_tournament():
    w, h = 800, 500
    img, d = base(w, h, "HOW THE LINE WAS PICKED", "judge-tested before it was submitted")
    rows = [
        ("Candidates written", "28  ·  15 devices"),
        ("Scored 1–5 on the brief", "5 criteria, in order"),
        ("Knockout bracket", "8 seeds → final"),
        ("Self-pairwise check", "winner beats both runners-up"),
        ("Tournament score", "23 / 25"),
    ]
    y = 132
    for k, v in rows:
        d.text((48, y), k, font=font("DejaVuSans.ttf", 26), fill=MUTED)
        d.text((48, y + 32), v, font=font("DejaVuSans-Bold.ttf", 28), fill=WHITE)
        y += 68
    img.save(os.path.join(ASSETS, "shot-tournament.png"))


if __name__ == "__main__":
    hero()
    shot_chat()
    shot_response()
    shot_robot()
    shot_tournament()
    print("images written to", ASSETS)
