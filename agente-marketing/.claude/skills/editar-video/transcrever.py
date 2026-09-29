# -*- coding: utf-8 -*-
"""Transcreve um video e grava as falas com tempo.
Uso: python transcrever.py video.mp4 pasta_saida
Sai: pasta_saida/falas.json  [{"i","start","end","text"}]
"""
import sys, os, types, wave, json, subprocess

# O Windows com Smart App Control bloqueia o numba; o whisper so usa ele
# para tempo por palavra. Este "substituto" deixa o whisper rodar sem ele.
numba = types.ModuleType("numba")
def _id(*a, **k):
    if len(a) == 1 and callable(a[0]) and not k:
        return a[0]
    return lambda f: f
numba.jit = numba.njit = _id
numba.prange = range
numba.__version__ = "0.0.0-shim"
sys.modules["numba"] = numba

import numpy as np
import whisper

video, saida = sys.argv[1], sys.argv[2]
os.makedirs(saida, exist_ok=True)
wav = os.path.join(saida, "audio.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vn", "-ac", "1",
                "-ar", "16000", "-c:a", "pcm_s16le", wav], check=True)

with wave.open(wav, "rb") as w:
    audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

modelo = os.environ.get("WHISPER_MODELO", "small")
print(f"carregando modelo {modelo}...", flush=True)
m = whisper.load_model(modelo)
print("transcrevendo...", flush=True)
r = m.transcribe(audio, language="pt", fp16=False,
                 condition_on_previous_text=False, verbose=False)

falas = []
for i, s in enumerate(r["segments"]):
    t = s["text"].strip().replace("Cloud", "Claude").replace("cloud", "Claude")
    falas.append({"i": i, "start": round(s["start"], 2), "end": round(s["end"], 2), "text": t})

with open(os.path.join(saida, "falas.json"), "w", encoding="utf-8") as f:
    json.dump(falas, f, ensure_ascii=False, indent=1)
for s in falas:
    print(f'[{s["i"]}] {s["start"]:.1f}-{s["end"]:.1f} {s["text"]}')
print("PRONTO", len(falas), "falas", flush=True)
