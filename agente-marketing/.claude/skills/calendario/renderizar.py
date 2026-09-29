# -*- coding: utf-8 -*-
"""Transforma os posts do calendario em imagens prontas (1080x1350).
Uso: python renderizar.py posts.json pasta_saida
posts.json:
{
 "marca": {"nome": "@perfil", "cor1": "#0057B8", "cor2": "#FF6B2B", "cor3": "#FF3E8A",
           "fundo": "#F4F6F9", "texto": "#1d2433",
           "fonte_titulo": "Chakra Petch", "fonte_texto": "Inter"},
 "posts": [ {"id": "01", "slides": [ {"titulo": "...", "texto": "..."}, ... ]} ]
}
"""
import sys, os, json, subprocess, shutil, html, tempfile

def achar_navegador():
    for c in [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"]:
        if os.path.exists(c):
            return c
    for n in ["google-chrome", "chromium", "chrome", "msedge"]:
        p = shutil.which(n)
        if p:
            return p
    sys.exit("Nao achei Chrome nem Edge instalado.")

cfg = json.load(open(sys.argv[1], encoding="utf-8"))
saida = sys.argv[2]
os.makedirs(saida, exist_ok=True)
m = cfg["marca"]
nav = achar_navegador()
fonts = "family=" + m.get("fonte_titulo", "Inter").replace(" ", "+") + ":wght@700&family=" + m.get("fonte_texto", "Inter").replace(" ", "+") + ":wght@400;600"

def pagina(slide, n, total, capa):
    t = html.escape(slide.get("titulo", "")).replace("\n", "<br>")
    x = html.escape(slide.get("texto", "")).replace("\n", "<br>")
    tam = 92 if capa else 64
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>
*{{margin:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{m['fundo']};font-family:'{m.get('fonte_texto','Inter')}',sans-serif;color:{m['texto']};
display:flex;flex-direction:column;justify-content:center;padding:110px 96px;position:relative;overflow:hidden}}
.pontos{{position:absolute;top:70px;left:96px;display:flex;gap:14px}}
.pontos i{{width:26px;height:26px;border-radius:50%;display:block}}
h1{{font-family:'{m.get('fonte_titulo','Inter')}',sans-serif;font-size:{tam}px;line-height:1.08;margin-bottom:40px}}
.traco{{height:12px;width:220px;border-radius:6px;margin-bottom:44px;
background:linear-gradient(90deg,{m['cor1']} 33%,{m['cor2']} 33% 66%,{m['cor3']} 66%)}}
p{{font-size:44px;line-height:1.35}}
.rod{{position:absolute;bottom:70px;left:96px;right:96px;display:flex;justify-content:space-between;font-size:30px;opacity:.7}}
</style></head><body>
<div class="pontos"><i style="background:{m['cor1']}"></i><i style="background:{m['cor2']}"></i><i style="background:{m['cor3']}"></i></div>
<h1>{t}</h1><div class="traco"></div><p>{x}</p>
<div class="rod"><span>{html.escape(m['nome'])}</span><span>{n}/{total}</span></div>
</body></html>"""

tmp = tempfile.mkdtemp()
feitos = []
for post in cfg["posts"]:
    slides = post["slides"]
    for i, s in enumerate(slides, 1):
        h = os.path.join(tmp, f"{post['id']}-{i}.html")
        open(h, "w", encoding="utf-8").write(pagina(s, i, len(slides), i == 1))
        png = os.path.abspath(os.path.join(saida, f"post{post['id']}-slide{i}.png"))
        subprocess.run([nav, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--window-size=1080,1350", "--virtual-time-budget=4000",
                        f"--screenshot={png}", "file:///" + h.replace("\\", "/")],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        feitos.append(png)
print("PRONTO", len(feitos), "imagens em", saida)
