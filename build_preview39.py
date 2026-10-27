from pathlib import Path

ROOT = Path(__file__).parent

def alert(platform, **values):
    html = (ROOT / f'{platform}-alert.html').read_text(encoding='utf-8')
    css = (ROOT / f'{platform}-alert.css').read_text(encoding='utf-8')
    for key, value in values.items():
        html = html.replace('{' + key + '}', value)
    html = html.replace('https://raw.githubusercontent.com/MasAjie12/halloween-alert-assets/main/', '')
    return f'<style>{css}</style>{html}'


def main():
    soc = alert('sociabuzz', amount='Rp 100.000', from_text='via Sociabuzz', supporter='PumpkinKing', message='Malam Halloween seru!')
    saw = alert('saweria', amount='Rp 75.000', donator='NightWatcher', message='Salam dari kastil!')
    css = (ROOT / 'widgets' / 'sociabuzz-top-donator.css').read_text(encoding='utf-8')
    html = f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Halloween 39 Preview</title><style>body{{margin:0;padding:24px;background:#09050e;color:#ffe9c4;font:14px 'Shadows Fright',sans-serif}}h1{{text-align:center;color:#ff8a24;font:800 28px 'Shadows Fright',sans-serif;text-shadow:0 0 14px #ff8a24}}h2{{color:#ffb342;font-family:'Shadows Fright',sans-serif}}.alert-wrap{{width:760px;max-width:100%;margin:0 auto 24px;overflow:hidden}}.alert-wrap .h39-wrap{{position:relative;width:100%;height:290px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:14px}}.w{{padding:16px;border:1px solid #ff8a2480;border-radius:14px;background:linear-gradient(135deg,#170b20,#28102f);position:relative;overflow:hidden}}.sub_timer{{display:flex;justify-content:center;gap:10px;flex-wrap:nowrap}}.sub_timer span{{font:700 40px 'Shadows Fright';color:#ff8a24}}table{{width:100%;color:#ffd27a}}td{{padding:6px}}.progress{{height:12px;background:#24122c;border-radius:6px;overflow:hidden}}.progress-bar{{height:100%;width:65%;background:linear-gradient(90deg,#9b4dca,#ff8a24,#ffd27a);}}@media(max-width:600px){{body{{padding:12px}}.alert-wrap .h39-wrap{{height:220px}}}}</style><style>{css}</style></head><body><h1>✦ Halloween Night ✦</h1><h2>Alert Sociabuzz</h2><div class="alert-wrap">{soc}</div><h2>Alert Saweria</h2><div class="alert-wrap">{saw}</div><h2>Widgets</h2><div class="grid"><div class="w"><div class="sub_judul"><strong>Subathon Timer</strong></div><div class="sub_timer"><span>12</span><span>:</span><span>34</span><span>:</span><span>56</span></div></div><div class="w"><div class="card-header">Top Donator</div><table class="show_donate"><tr><td>1</td><td class="text-limit">PumpkinKing</td><td>Rp 500.000</td></tr><tr><td>2</td><td class="text-limit">NightWatcher</td><td>Rp 250.000</td></tr></table></div><div class="w"><div class="card-header">Milestone</div><p>Rp 650.000 / Rp 1.000.000</p><div class="progress"><div class="progress-bar"></div></div></div><div class="w"><div class="card-header">Queue</div><table class="show_donate"><tr><td>1</td><td class="text-limit">CastleVisitor</td><td>Rp 50.000</td></tr></table></div></div></body></html>'''
    assert all(x not in html for x in ('{amount}', '{supporter}', '{donator}', '{message}', '{from_text}'))
    (ROOT / 'preview-halloween.html').write_text(html, encoding='utf-8')
    print('Built preview-halloween.html')

if __name__ == '__main__':
    main()
