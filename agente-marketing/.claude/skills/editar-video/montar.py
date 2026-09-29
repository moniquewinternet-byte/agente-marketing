# -*- coding: utf-8 -*-
"""Corta o video nos trechos escolhidos, deixa vertical e queima a legenda.
Uso: python montar.py video.mp4 cortes.json saida.mp4
cortes.json: [{"start": 1.2, "end": 5.8, "text": "legenda deste trecho"}, ...]
"""
import sys, os, json, subprocess, tempfile

video, cortes_path, saida = sys.argv[1], sys.argv[2], sys.argv[3]
cortes = json.load(open(cortes_path, encoding="utf-8"))
tmp = tempfile.mkdtemp()

def srt_t(s):
    ms = int(round(s * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sec, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"

# 1) cortar cada trecho, ja em 1080x1920 (vertical, preenche e centraliza)
vf = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
partes, t, srt = [], 0.0, []
for n, c in enumerate(cortes):
    p = os.path.join(tmp, f"p{n:03d}.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(c["start"]), "-to", str(c["end"]),
                    "-i", video, "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "aac", "-ar", "48000", "-ac", "2", p], check=True)
    dur = c["end"] - c["start"]
    # quebra a legenda em blocos curtos (ate 5 palavras), divididos no tempo do trecho
    palavras = c["text"].split()
    blocos = [palavras[i:i + 5] for i in range(0, len(palavras), 5)] or [[]]
    passo = dur / len(blocos)
    for k, b in enumerate(blocos):
        if b:
            srt.append((t + k * passo, t + (k + 1) * passo, " ".join(b)))
    partes.append(p); t += dur

# 2) juntar
lista = os.path.join(tmp, "lista.txt")
with open(lista, "w", encoding="utf-8") as f:
    for p in partes:
        f.write(f"file '{p.replace(os.sep, '/')}'\n")
junto = os.path.join(tmp, "junto.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", junto], check=True)

# 3) legenda: arquivo .srt ao lado do video final + queimada na imagem
srt_path = os.path.splitext(saida)[0] + ".srt"
with open(srt_path, "w", encoding="utf-8") as f:
    for i, (a, b, txt) in enumerate(srt, 1):
        f.write(f"{i}\n{srt_t(a)} --> {srt_t(b)}\n{txt}\n\n")

estilo = ("FontName=Arial,FontSize=15,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
          "BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV=90")
srt_ff = srt_path.replace("\\", "/").replace(":", "\\:")
r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", junto,
                    "-vf", f"subtitles='{srt_ff}':force_style='{estilo}'",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "copy", saida])
if r.returncode != 0:
    # plano B: se a legenda queimada falhar, entrega o video cortado + o .srt separado
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", junto, "-c", "copy", saida], check=True)
    print("AVISO: legenda nao foi queimada; o .srt esta ao lado do video")
print(f"PRONTO {saida} ({t:.1f}s)")
