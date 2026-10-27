#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).parent / "widgets"
RAW = "https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main"
ORANGE = "#ff8a24"
GOLD = "#ffd27a"
PURPLE = "#9b4dca"
DARK = "#170b20"
DARK2 = "#28102f"
BORDER = "#ff8a2480"

BASE = f"""@font-face{{font-family:'Shadows Fright';src:url('https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main/shadows-fright.ttf') format('truetype');font-display:swap}}
@font-face{{font-family:'Saltblack Combat';src:url('https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main/saltblack-combat.ttf') format('truetype');font-display:swap}}
html,body{{overflow:hidden!important;margin:0;padding:0;background:transparent}}
.card,.subathon-container,#ms_container,#__next>div,.w,.w-sub,.w-mile,.w-top,.w-queue{{background:linear-gradient(135deg,#26102fcc,#3a1842cc 55%,#26102fcc),url('{RAW}/bgbaru.png') center no-repeat!important;background-size:cover!important;border:1px solid {BORDER}!important;border-radius:14px!important;box-shadow:0 0 24px #ff8a2438!important;color:{GOLD}!important;font-family:'Shadows Fright',sans-serif!important;overflow:hidden!important;position:relative!important}}
.card:before,.subathon-container:before,#ms_container:before,#__next>div:before{{content:''!important;position:absolute!important;top:0!important;left:0!important;right:0!important;height:3px!important;background:linear-gradient(90deg,{PURPLE},{ORANGE},{GOLD},{ORANGE},{PURPLE})!important;background-size:240% 100%!important;animation:h39-witch-bar 5s linear infinite!important;pointer-events:none!important}}
.sub_judul,.card-header,#__next>div>.chakra-heading{{font-family:'Shadows Fright',sans-serif!important;color:{ORANGE}!important;font-size:22px!important;letter-spacing:1.8px!important;text-shadow:0 0 10px #ff8a2488!important;border-bottom:1px solid {BORDER}!important;padding-bottom:8px!important;margin-bottom:12px!important;display:block!important}}.sub_judul strong,.sub_judul strong:before,.sub_judul strong:after{{font:inherit!important;color:inherit!important;border:0!important;box-shadow:none!important;background:none!important;padding:0!important;margin:0!important;display:inline!important;content:none!important}}
@keyframes h39-witch-bar{{0%{{background-position:0 0}}100%{{background-position:240% 0}}}}
"""

DECOR = """.card>*,.subathon-container>*,#ms_container>*,#__next>div>*{position:relative!important;z-index:1!important}
"""

MEDIA_COMMON = f"""#ms_container .text-container{{position:relative!important;z-index:3!important;width:min(880px,96%,calc((100vh - 215px)*16/9))!important;max-width:100%!important;box-sizing:border-box!important;margin:10px auto!important;padding:12px 68px 14px!important;background:#170b20dd!important;border:1px solid {BORDER}!important;border-radius:12px!important;color:{GOLD}!important;font-family:'Shadows Fright',sans-serif!important;text-align:center!important;overflow:visible!important}}
#ms_container .title{{display:flex!important;flex-wrap:wrap!important;align-items:center!important;justify-content:center!important;gap:4px 10px!important;margin:0 auto!important;line-height:1.2!important;max-width:100%!important}}
#ms_container #sender{{order:1!important;min-width:0!important;max-width:100%!important;overflow-wrap:anywhere!important;color:#fff8e6!important;font:700 40px 'Saltblack Combat','Shadows Fright',sans-serif!important;letter-spacing:2px!important;text-shadow:0 2px 3px #000!important}}
#ms_container .dari,#ms_container #from_text,#ms_container .from-text,#ms_container .from{{order:2!important;color:{ORANGE}!important;font:700 18px 'Shadows Fright',sans-serif!important}}
#ms_container #nominal{{order:3!important;min-width:0!important;max-width:100%!important;overflow-wrap:anywhere!important;color:#fff0b0!important;font:900 44px 'Saltblack Combat','Shadows Fright',sans-serif!important;letter-spacing:2.4px!important;text-shadow:0 2px 3px #000!important;white-space:nowrap!important}}
#ms_container #message,#ms_container .message{{display:block!important;max-width:92%!important;margin:7px auto 0!important;color:#f7dfba!important;font:italic 18px/1.35 'Shadows Fright',sans-serif!important;text-shadow:0 2px 5px #000!important}}
#ms_container .media-container{{display:flex!important;flex-direction:column!important;align-items:center!important;gap:12px!important;margin:0!important;padding:0!important;width:100%!important;text-align:center!important}}
#ms_container .media-container iframe.media,#ms_container .video-preview,#ms_container .thumbnail{{width:min(880px,96%,calc((100vh - 215px)*16/9))!important;height:auto!important;aspect-ratio:16/9!important;max-width:100%!important;min-height:0!important;margin:14px auto 0!important;border:1px solid {BORDER}!important;border-radius:12px!important;background:#050208!important;box-shadow:0 0 18px #ff8a2455!important;display:block!important}}
#ms_container .loadingbar{{display:block!important;position:relative!important;z-index:6!important;width:min(880px,96%,calc((100vh - 215px)*16/9))!important;max-width:100%!important;height:5px!important;margin:12px auto 14px!important;background:#050208cc!important;border:1px solid {BORDER}!important;border-radius:999px!important;opacity:1!important;visibility:visible!important;overflow:hidden!important}}
#ms_container .loadingbar svg path:first-child{{stroke:#0000!important}}#ms_container .loadingbar svg path:last-child{{stroke:{ORANGE}!important;filter:drop-shadow(0 0 5px {ORANGE})!important}}
#ms_container .wrapper.hide,#ms_container.hide,#ms_container .hide{{opacity:0!important;visibility:hidden!important}}
"""

MS_TEXT = f""".media-container,.video-preview,video{{display:none!important}}.style-1.text-container,#sender,#nominal,#message{{display:block!important;visibility:visible!important;opacity:1!important}}
#ms_container #sender{{font-family:'Saltblack Combat','Shadows Fright',sans-serif!important;letter-spacing:2px!important;text-shadow:0 2px 3px #000!important}}
#ms_container #nominal{{font-family:'Saltblack Combat','Shadows Fright',sans-serif!important;letter-spacing:2.4px!important;text-shadow:0 2px 3px #000!important}}
#ms_container .loadingbar{{display:block!important;position:relative!important;z-index:6!important;width:min(460px,90%)!important;height:5px!important;margin:16px auto 8px!important;background:#050208cc!important;border:1px solid {BORDER}!important;border-radius:999px!important;opacity:1!important;visibility:visible!important;overflow:hidden!important}}
#ms_container .loadingbar svg path:first-child{{stroke:#0000!important}}#ms_container .loadingbar svg path:last-child{{stroke:{ORANGE}!important;filter:drop-shadow(0 0 6px {ORANGE})!important}}
#ms_container .wrapper.hide,#ms_container.hide,#ms_container .hide{{opacity:0!important;visibility:hidden!important}}
"""

MS_VIDEO = MEDIA_COMMON + """#ms_container{position:relative!important;isolation:isolate!important;overflow:hidden!important}#ms_container>*{position:relative!important;z-index:2!important}
"""
TOP = f""".show_donate{{table-layout:fixed!important;width:100%!important;border-collapse:separate!important;border-spacing:0 5px!important}}.show_donate td{{vertical-align:middle!important;padding:7px 8px!important}}.show_donate td:first-child{{width:32px!important;text-align:center!important;color:{ORANGE}!important;font-weight:bold!important}}.show_donate td:nth-child(2){{width:auto!important}}.show_donate td:last-child{{width:42%!important;max-width:42%!important;text-align:right!important}}.show_donate .text-limit{{overflow:visible!important;text-overflow:clip!important;white-space:normal!important;word-break:break-word!important;line-height:1.25!important;text-align:left!important;color:{GOLD}!important}}.show_donate .text-limit-r{{font-size:12.5px!important;line-height:1.25!important;color:{ORANGE}!important}}
"""
SUBATHON = f""".subathon-container,.w-sub{{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;box-sizing:border-box!important;width:100%!important}}.sub_judul{{width:100%!important;text-align:center!important;box-sizing:border-box!important}}.sub_timer{{display:flex!important;align-items:center!important;justify-content:center!important;flex-direction:row!important;flex-wrap:nowrap!important;width:100%!important;min-height:52px!important;box-sizing:border-box!important;line-height:1!important;gap:6px!important;text-align:center!important;white-space:nowrap!important}}.sub_timer *,.sub_timer span,.sub_timer strong,.sub_timer .hour,.sub_timer .minute,.sub_timer .second,.sub_timer [class*='separator'],.sub_timer [class*='colon']{{display:inline-flex!important;align-items:center!important;justify-content:center!important;position:static!important;float:none!important;flex:0 0 auto!important;min-width:34px!important;height:52px!important;margin:0!important;padding:0!important;white-space:nowrap!important;vertical-align:middle!important;font-family:'Saltblack Combat',sans-serif!important;font-size:44px!important;font-weight:700!important;line-height:1!important;color:{ORANGE}!important;text-shadow:0 0 14px #ff8a2488!important}}.sub_timer [class*='separator'],.sub_timer [class*='colon']{{min-width:12px!important;color:{GOLD}!important}}.sub_timer .minute::before,.sub_timer .second::before{{color:{GOLD}!important;font-family:'Shadows Fright',sans-serif!important;font-size:44px!important;line-height:1!important}}.sub_timer .minute,.sub_timer .second{{color:{ORANGE}!important}}
"""
MILE = f""".progress{{height:12px!important;background:#24122c!important;border:1px solid #ff8a2455!important;border-radius:6px!important;overflow:hidden!important;position:relative!important}}.progress-bar{{background:linear-gradient(90deg,{PURPLE},{ORANGE},{GOLD},{ORANGE},{PURPLE})!important;background-size:220% 100%!important;border-radius:6px!important;animation:h39-witch-bar 2.4s linear infinite!important;box-shadow:0 0 10px #ff8a2488!important}}
"""
VARIANTS = {"mediashare": MS_TEXT, "mediashare-video": MS_VIDEO, "top-donator": TOP, "queue": TOP, "subathon": SUBATHON, "milestone": MILE}


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    count = 0
    for platform in ("sociabuzz", "saweria"):
        for widget, extra in VARIANTS.items():
            css = BASE + DECOR + extra
            for suffix in ("", "-obs"):
                (ROOT / f"{platform}-{widget}{suffix}.css").write_text(css, encoding="utf-8")
                count += 1
    for f in ROOT.glob("*.css"):
        text = f.read_text(encoding="utf-8")
        assert "inset:" not in text
        assert "h39-witch-bar" in text and "labu.png" not in text and "Shadows Fright" in text and "bgbaru.png" in text
    print(f"Built {count} widget CSS files")


if __name__ == "__main__":
    main()
