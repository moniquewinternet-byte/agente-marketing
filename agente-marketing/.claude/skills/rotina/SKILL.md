---
name: rotina
description: A versão automática da Chefe, feita pra rodar sozinha numa tarefa agendada (dia 1º e dia 15). Roda pesquisa, calendário e posts SEM parar pra perguntar, deixa tudo como rascunho na pasta, e escreve um resumo pra dona abrir e aprovar depois. Use quando ela digitar /rotina, ou quando uma tarefa agendada disparar a campanha do mês.
---

# Rotina: a Chefe rodando sozinha

Esta é a mesma equipe do `/campanha`, mas preparada pra rodar SEM ninguém do lado.
Por isso a regra número 1 é diferente: **nunca pare pra perguntar e nunca espere
aprovação.** Faça as etapas, salve tudo como RASCUNHO na pasta, e no fim escreva
um resumo pra dona abrir e aprovar quando quiser. Nada é publicado, nada é enviado.

## Antes de começar (rápido, sem travar)
- Confirme que o conector Apify está ligado. Se não estiver, NÃO pare esperando:
  escreva no resumo do fim "não consegui ler o Instagram porque o Apify não estava
  ligado" e faça o que der com o que já existe na pasta `pesquisa/`.
- Neste computador o Python é `py` (no Mac, `python3`).
- Se um passo der erro, anote no resumo em uma linha e siga pro próximo. O objetivo
  é deixar o máximo pronto pra ela revisar, não parar no meio.

## Passo 0: leia a configuração
Leia o arquivo `rotina-config.md` na raiz da pasta, se existir. Ele diz:
- o @ do perfil dela;
- até 3 perfis do nicho pra comparar;
- 15 ou 30 dias, e quantos posts por semana;
- foco (vender algo ou crescer).
Se o arquivo não existir ou vier incompleto, use estes padrões, sem perguntar:
- perfil: o da Tradução mais recente em `pesquisa/`;
- 15 dias, 3 posts por semana, foco em crescer;
- perfis do nicho: os que já apareceram na última Tradução, se houver.
Anote no resumo qual configuração você usou.

## Passo 1: pesquisa (a Pesquisadora)
Rode a skill `traducao` no perfil dela (e, curto, nos perfis do nicho da config).
Salve a Tradução em `pesquisa/` com a data no nome, como a skill já faz.

## Passo 2: calendário (a Estrategista)
Rode a skill `calendario` usando a Tradução do passo 1 e a config (dias, posts por
semana, foco). Como não há ninguém pra responder as perguntas dela, use a config e os
padrões acima. Salve em `pesquisa/` com a data.

## Passo 3: posts (a Designer)
Rode a skill `criar-posts` para os 3 primeiros posts do calendário (não o mês inteiro).
Passe pela revisora normalmente. Salve os carrosséis e as legendas em `posts/`.

## Passo 4: o resumo pra ela aprovar
Escreva `pesquisa/rotina-<AAAA-MM-DD>.md` com:
- a data e a configuração usada;
- o que foi produzido e ONDE está (a Tradução, o calendário, os 3 posts);
- o achado principal da pesquisa em 3 linhas;
- uma lista curta "o que revisar antes de publicar";
- o aviso: "isto é rascunho. Nada foi publicado. Abra, revise e publique o que gostar."
Se algo falhou, diga o quê e o que ela precisa fazer (ex.: "ligue o Apify e rode
/rotina de novo").

## Regras
- Nunca pergunte nada. Nunca espere aprovação. Nunca publique nem envie.
- Nunca invente número, depoimento ou nome. Faltou dado, escreva `[a confirmar]`.
- Deixe tudo como rascunho na pasta. Quem aprova e publica é a dona, depois.
