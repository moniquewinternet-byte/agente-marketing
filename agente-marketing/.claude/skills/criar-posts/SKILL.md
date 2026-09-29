---
name: criar-posts
description: Cria os posts do calendário prontos pra publicar, com carrossel em imagem (1080x1350) e legenda. Use quando ela digitar /criar-posts, pedir pra criar os posts do calendário ou gerar carrosséis.
---

# Criar posts

## Passo 1: prepare
- Leia o `pesquisa/calendario-*.json` mais recente.
- Pegue cores, fontes e nome do perfil da skill de identidade visual dela (se não
  houver, pergunte 3 cores e o @).
- Fotos: pergunte se ela quer mandar fotos (arraste para a pasta `fotos/`). Se não
  quiser, os carrosséis saem só com texto no visual dela. Imagem da internet só de
  banco gratuito com licença livre (Unsplash, Pexels), nunca do Google Imagens.

## Passo 2: escreva
Para cada carrossel: 5 a 8 slides. Slide 1 = gancho curto (até 8 palavras).
Uma ideia por slide. Último slide = uma chamada só (salvar, mandar pra alguém, comentar).
Legenda: gancho na primeira linha, texto no tom de voz dela (skill de voz, se houver),
3 a 5 hashtags. Mostre os textos de 2 posts e peça ok antes de gerar tudo.

## Passo 3: gere as imagens
Monte `posts/posts.json` no formato do `renderizar.py` (pasta da skill calendario) e rode:
`python .claude/skills/calendario/renderizar.py posts/posts.json posts/imagens`
(no Windows pode ser `py`). Precisa de Chrome ou Edge instalado.
Salve as legendas em `posts/legendas.md`.

## Passo 3.5: a revisora (antes de gerar as imagens)
Antes de renderizar, passe CADA carrossel por 5 leitoras. Cada uma dá uma nota de 0 a 10:
- **a cética:** acredita no que está escrito? Tem promessa sem prova?
- **a estranha:** entende sem conhecer a marca? Onde ela para de ler?
- **a concorrente:** dava pra colar o nome de outro perfil e continuar igual? (se sim, está genérico)
- **a cliente:** isso responde uma dúvida real dela, ou fala do que só interessa a você?
- **a editora:** tem "cara de IA"? (checa a lista da skill de voz: travessão, "não é X é Y", frase em três, palavra de escritório)
Mostre a nota de cada uma e os 2 ajustes mais importantes. Se a média ficar abaixo de 7,
reescreva só o que a leitora apontou (não o carrossel inteiro) e dê a nota de novo, no
máximo 2 vezes. Só gera as imagens depois que passar. Nunca invente elogio: reprovar é resultado válido.

## Passo 4: entregue
Abra a pasta das imagens, mostre 1 carrossel e diga a nota que ele tirou na revisão.
Reels do calendário: entregue o roteiro (tempo, fala, texto na tela) pra ela gravar; depois
o `/editar-video` edita.
