---
name: editar-video
description: Edita um vídeo bruto gravado no celular e entrega um Reels pronto, vertical, com cortes e legenda na tela. Use quando ela digitar /editar-video, mandar um vídeo pra editar, ou pedir pra cortar, legendar ou transformar um vídeo em Reels.
---

# Editar vídeo

Se a pessoa não tiver um vídeo, use `videos/video-exemplo.mp4`, que já vem na pasta.

Você pega um vídeo bruto e entrega um Reels pronto: sem silêncios, sem erros
e repetições, vertical (1080x1920) e com legenda na tela.

## Passo 0: confira as ferramentas (só na primeira vez)
Rode `ffmpeg -version` e `python -c "import whisper"` (no Mac, `python3`).
Se faltar algo, instale, explicando cada passo em uma linha simples:
- **Windows**
  - ffmpeg: `winget install --id Gyan.FFmpeg -e` (depois, abra um terminal novo para o PATH valer).
  - Python, se não houver: `winget install --id Python.Python.3.12 -e`.
  - whisper: `py -m pip install --index-url https://download.pytorch.org/whl/cpu torch` e depois `py -m pip install openai-whisper`.
- **Mac**
  - Homebrew, se não houver (instrução em brew.sh), depois `brew install ffmpeg`.
  - `python3 -m pip install torch openai-whisper`.
Se o Windows bloquear um arquivo com a mensagem "Uma política de Controle de
Aplicativo bloqueou este arquivo", NÃO desligue nada no Windows: o script
`transcrever.py` desta pasta já contorna o bloqueio mais comum.

## Passo 1: transcreva
`python .claude/skills/editar-video/transcrever.py "<video>" videos/<nome>`
(no Windows pode ser `py` no lugar de `python`). Na primeira vez ele baixa o
modelo de fala. Para ir mais rápido, use o modelo menor:
defina a variável `WHISPER_MODELO=base` antes de rodar.

## Passo 2: escolha os cortes (este é o trabalho de editor)
Leia `videos/<nome>/falas.json` e escolha os trechos que contam a história:
- Tire silêncios, hesitações, frases repetidas (fique com a última tentativa),
  conversa paralela e o que não serve ao assunto.
- Comece pela frase mais forte, se ela existir no meio do vídeo.
- Corrija a legenda: escreva o que a pessoa quis dizer, sem mudar o sentido.
  Troque "Cloud" por "Claude".
Mostre a lista de cortes em texto e peça ok antes de montar.
Grave em `videos/<nome>/cortes.json`: `[{"start": 0.0, "end": 5.1, "text": "..."}]`.

## Passo 3: monte
`python .claude/skills/editar-video/montar.py "<video>" videos/<nome>/cortes.json videos/<nome>-reels.mp4`
Sai o vídeo vertical com legenda e um `.srt` ao lado (para usar no CapCut ou no Instagram, se quiser).

## Passo 4: entregue
Abra o vídeo, diga a duração antes e depois, e pergunte se quer ajustar algo
("começa 1 segundo antes", "tira essa frase"). Ajuste mexendo só no cortes.json e remontando.
