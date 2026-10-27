#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).parent
DOWNLOADS = Path.home() / "Downloads"
REPO = "https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main"
FONT_FILE = "shadows-fright.ttf"
TOKEN_FONT_FILE = "saltblack-combat.ttf"


def pumpkin_assets():
    # Keep original alpha/colors. White ghost and pumpkin highlights are part of art.
    src = Image.open(DOWNLOADS / "labukiri.png").convert("RGBA")
    assert src.getchannel("A").getbbox(), "labukiri.png is empty"
    src.save(ROOT / "labukiri.png")


def card_assets():
    src = Image.open(DOWNLOADS / "kiricard.png").convert("RGBA")
    src.save(ROOT / "kiricard.png")
    src.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(ROOT / "kiricard-right.png")


def foreground_asset():
    bg = Image.open(ROOT / "bg.png").convert("RGBA")
    mask = Image.new("L", bg.size, 0)
    draw = ImageDraw.Draw(mask)
    # Rough foreground silhouette: central character hair and torso.
    draw.polygon([
        (730, 220), (760, 145), (815, 85), (900, 35), (1005, 0),
        (1140, 0), (1270, 8), (1415, 0), (1540, 25), (1650, 75),
        (1715, 145), (1735, 230), (1695, 305), (1635, 355),
        (1535, 330), (1480, 285), (1405, 245), (1320, 220),
        (1225, 210), (1135, 230), (1050, 270), (980, 325),
        (895, 355), (820, 340), (760, 290),
    ], fill=255)
    draw.polygon([
        (680, 405), (790, 430), (900, 405), (1010, 420), (1080, 475),
        (1150, 425), (1260, 405), (1380, 445), (1510, 500),
        (1650, 545), (1780, 595), (1885, 665), (1935, 774),
        (175, 774), (205, 690), (300, 600), (430, 535), (555, 490),
    ], fill=255)
    bg.putalpha(mask)
    return bg, mask


def alert_html(platform):
    supporter = "{supporter}" if platform == "sociabuzz" else "{donator}"
    from_html = '<div class="h39-from">{from_text}</div>' if platform == "sociabuzz" else ""
    return (
        '<div class="h39-wrap"><div class="h39-card">'
        f'<img class="h39-bg" src="{REPO}/bg.png">'
        '<div class="h39-shade"></div>'
        '<div class="h39-mist h39-mist-a"></div><div class="h39-mist h39-mist-b"></div>'
        f'<img class="h39-card-decor" src="{REPO}/kiricard-right.png">'
        f'<img class="h39-pumpkin h39-left" src="{REPO}/labukiri.png">'
        f'<img class="h39-foreground" src="{REPO}/foreground.png">'
        f'<img class="h39-pumpkin h39-right" src="{REPO}/labu-right.png">'
        '<div class="h39-bat h39-bat-a">✦</div><div class="h39-bat h39-bat-b">✦</div>'
        '<div class="h39-body">'
        f'<div class="h39-amount">{{amount}}</div>{from_html}'
        f'<div class="h39-supporter">{supporter}</div>'
        '<div class="h39-divider"><span>✦</span></div>'
        '<div class="h39-message">{message}</div>'
        '</div></div></div>'
    )


def alert_css():
    return """@font-face{font-family:'Shadows Fright';src:url('https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main/shadows-fright.ttf') format('truetype');font-display:swap}
@font-face{font-family:'Saltblack Combat';src:url('https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main/saltblack-combat.ttf') format('truetype');font-display:swap}
.h39-wrap{position:fixed;top:0;left:0;width:100%;height:100%;display:flex;justify-content:center;align-items:center;overflow:hidden}
.h39-card{position:relative;width:760px;max-width:96vw;height:290px;margin:0 auto;overflow:hidden;border:2px solid #f47b20;border-radius:18px;background:#160b20;box-shadow:0 0 18px #f47b2088,0 0 55px #7e27a866;color:#fff2d2;font-family:'Shadows Fright',sans-serif}
.h39-bg{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:center;z-index:0;filter:brightness(.82) saturate(1.2) contrast(1.08);animation:h39-bg-zoom 18s ease-in-out infinite alternate}
.h39-shade{position:absolute;top:0;left:0;width:100%;height:100%;z-index:1;background:linear-gradient(90deg,#12091b99 0%,#1c0b2280 22%,#160b2060 50%,#1c0b2280 78%,#12091b99 100%);pointer-events:none}
.h39-mist{position:absolute;z-index:2;width:38%;height:44%;border-radius:50%;background:#8e36b820;filter:blur(22px);pointer-events:none;animation:h39-mist 9s ease-in-out infinite alternate}
.h39-mist-a{left:5%;top:4%}.h39-mist-b{right:5%;bottom:0;animation-delay:-4s;background:#f47b2018}
.h39-card-decor{position:absolute;left:-5%;top:-8%;width:54%;height:116%;object-fit:contain;object-position:left center;z-index:3;pointer-events:none;opacity:1;filter:invert(1) sepia(1) saturate(2.8) hue-rotate(330deg) brightness(1.15) drop-shadow(0 0 5px #ffd27a);animation:h39-card-float 5.5s ease-in-out infinite}
.h39-pumpkin{position:absolute;top:9%;width:24%;height:82%;object-fit:contain;z-index:4;filter:drop-shadow(0 0 8px #ff7a2199);animation:h39-pumpkin-float 4.5s ease-in-out infinite alternate}
.h39-left{left:26%;top:6%;width:27%;height:88%;object-position:center;z-index:4;transform:rotate(-14deg);transform-origin:50% 85%;animation:h39-left-emerge 4.5s ease-in-out infinite alternate}.h39-right{right:1%;object-position:right center;z-index:5;animation-delay:-2.2s}
.h39-foreground{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:center;z-index:5;pointer-events:none;filter:brightness(.82) saturate(1.2) contrast(1.08)}
.h39-bat{position:absolute;z-index:5;color:#ffb342;font:700 23px/1 'Shadows Fright',sans-serif;text-shadow:0 0 10px #f47b20;animation:h39-bat 4s ease-in-out infinite alternate;pointer-events:none}
.h39-bat-a{left:29%;top:13%}.h39-bat-b{right:29%;bottom:13%;animation-delay:-2s}
.h39-body{position:relative;z-index:6;width:50%;height:100%;margin:0 auto;padding:28px 10px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.h39-amount{padding:7px 18px 8px;border:1px solid #ffd27a;border-radius:10px;background:#160b20f2;box-shadow:0 2px 7px #000b;color:#fff0b0;font:800 42px/1.1 'Saltblack Combat','Shadows Fright',sans-serif;letter-spacing:2.4px;text-shadow:0 2px 3px #000;animation:none}
.h39-from{margin-top:5px;color:#ffd27a;font:700 13px/1.2 'Shadows Fright',sans-serif;letter-spacing:1px;text-shadow:0 2px 3px #000}
.h39-supporter{max-width:100%;margin-top:7px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#fff8e6;font:700 30px/1.2 'Saltblack Combat','Shadows Fright',sans-serif;letter-spacing:2px;text-shadow:0 2px 3px #000}
.h39-divider{display:flex;align-items:center;width:82%;height:12px;margin:6px auto 3px;color:#ffb342;font-size:13px}
.h39-divider:before,.h39-divider:after{content:'';height:1px;flex:1;background:linear-gradient(90deg,transparent,#ffb342)}
.h39-divider:after{background:linear-gradient(90deg,#ffb342,transparent)}
.h39-divider span{padding:0 8px;text-shadow:0 0 8px #f47b20}
.h39-message{max-width:100%;color:#f7dfba;font:400 16px/1.35 'Shadows Fright',sans-serif;word-wrap:break-word;text-shadow:0 2px 5px #000}
@keyframes h39-bg-zoom{0%{transform:scale(1)}100%{transform:scale(1.18)}}
@keyframes h39-pumpkin-float{0%{transform:translateY(0)}100%{transform:translateY(-7px)}}
@keyframes h39-left-emerge{0%{transform:translateY(8px) rotate(-14deg)}100%{transform:translateY(-5px) rotate(-18deg)}}
@keyframes h39-card-float{0%,100%{transform:translateY(0) rotate(-1deg)}50%{transform:translateY(-10px) rotate(1deg)}}
@keyframes h39-mist{0%{transform:translateX(-8px) scale(1)}100%{transform:translateX(10px) scale(1.18)}}
@keyframes h39-bat{0%{transform:translateY(0) rotate(-8deg);opacity:.45}100%{transform:translateY(-13px) rotate(8deg);opacity:1}}
@keyframes h39-pulse{0%{box-shadow:0 0 12px #f47b204c,0 0 5px #ffb34244 inset}100%{box-shadow:0 0 25px #f47b20aa,0 0 12px #ffb34288 inset}}
@media(max-width:600px){.h39-card{height:220px;border-radius:14px}.h39-body{width:64%;padding:18px 4px}.h39-card-decor{left:-8%;top:-7%;width:66%;height:114%}.h39-pumpkin{width:22%;height:78%;top:11%}.h39-left{left:24%;top:8%;width:28%;height:82%;transform:rotate(-14deg);animation:h39-left-emerge 4.5s ease-in-out infinite alternate}.h39-amount{font-size:30px;letter-spacing:1.4px;padding:6px 10px}.h39-supporter{font-size:22px;letter-spacing:1.4px}.h39-message{font-size:12px}.h39-from{font-size:11px}.h39-bat{font-size:16px}}
"""


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    font_source = ROOT / "Shadows Fright.ttf"
    if font_source.is_file():
        font_source.rename(ROOT / FONT_FILE)
    pumpkin_assets()
    card_assets()
    assert (ROOT / FONT_FILE).is_file(), f"missing {FONT_FILE}"
    assert (ROOT / TOKEN_FONT_FILE).is_file(), f"missing {TOKEN_FONT_FILE}"
    bg_source = DOWNLOADS / "bg.png"
    if bg_source.is_file():
        (ROOT / "bg.png").write_bytes(bg_source.read_bytes())
    assert (ROOT / "bg.png").is_file(), "missing bg.png"
    foreground, _ = foreground_asset()
    foreground.save(ROOT / "foreground.png")
    css = alert_css()
    for platform in ("sociabuzz", "saweria"):
        html = alert_html(platform)
        assert '\n' not in html and 'style="' not in html and '<style' not in html
        assert all(token in html for token in ("{amount}", "{message}"))
        if platform == "sociabuzz":
            assert "{from_text}" in html and "{supporter}" in html
        else:
            assert "{donator}" in html and "{from_text}" not in html
        (ROOT / f"{platform}-alert.html").write_text(html, encoding="utf-8")
        (ROOT / f"{platform}-alert.css").write_text(css, encoding="utf-8")
    assert css.count("url('") == 2 and "inset:" not in css
    print("Built Halloween alert assets and Sociabuzz/Saweria alert files")


if __name__ == "__main__":
    main()
