---
name: traducao
description: Tradução do seu Instagram. Lê um perfil público (o dela ou de um concorrente) com o Apify e entrega uma página com 8 respostas, do que atrai e do que vende até o que fazer esta semana. Use quando ela digitar /traducao @perfil, pedir análise do perfil, diagnóstico ou leitura do Instagram.
---

# Tradução do seu Instagram

Você lê um perfil de Instagram com dado real e traduz o que ele mostra em
8 respostas simples. Método da Monique Tecnologia.

## Passo 0: pergunte antes de começar
"Esse perfil é seu ou de outra pessoa (concorrente, referência)?" Se for de outra
pessoa, faça a versão curta (ver Regras). Avise que o perfil precisa ser público.

## Passo 1: puxe os dados (conector Apify, actor `apify/instagram-scraper`)
Rode estes 3 inputs (troque PERFIL pelo @ sem arroba):
1. `{"directUrls": ["https://www.instagram.com/PERFIL/"], "resultsType": "details", "resultsLimit": 1}`
2. `{"directUrls": ["https://www.instagram.com/PERFIL/"], "resultsType": "posts", "resultsLimit": 50}`
3. Comentários dos 3 posts com mais visualizações (URL de post, com /p/):
   `{"directUrls": ["https://www.instagram.com/p/CODIGO1/", "...", "..."], "resultsType": "comments", "resultsLimit": 15}`
Se a execução ainda estiver rodando, espere terminar e confira o total de itens
antes de ler. Se o Apify não estiver conectado, pare e peça pra conectar em
Configurações > Conectores.

## Passo 2: classifique e calcule
- Dê a cada post UM assunto, em palavras simples tiradas do próprio perfil
  (ex.: "dica de app", "venda do workshop", "bastidor", "vida pessoal").
- Dê a cada post UM objetivo: alcance, confiança/conexão ou venda. Convite para
  aula grátis, minicurso ou isca também conta como venda.
- Visualizações = campo `videoPlayCount` (o número que o Instagram mostra).
  Carrossel e foto não têm visualização: ficam fora da mediana e entram só na
  % por assunto.
- Calcule tudo com código (um script Python rápido), nunca de cabeça:
  MEDIANA dos reels (nunca média) no geral e por assunto; fora da curva = 5x ou
  mais a mediana; mediana e % de venda por mês.
- Diga o período que os posts cobrem (data do mais antigo ao mais novo).
- Grave os posts classificados em `pesquisa/posts-<perfil>.json`.

## Passo 3: responda as 8 perguntas
Cada afirmação leva uma etiqueta: VISTO (está no perfil) ou SUPOSIÇÃO (leitura provável, a confirmar).
1. **O que atrai e o que vende?** Tabela por assunto (posts, mediana, faixa) + fora da curva. Destaque o post que junta alcance e venda, se existir.
2. **Os 5 segundos:** o que a bio responde sobre quem é, pra quem, o que vende, por que ela, e se o nome aparece na busca.
3. **Do que o perfil fala:** % de cada assunto; qual assunto liga o que atrai ao que vende.
4. **Alcance ou confiança:** quantos posts de cada objetivo.
5. **Isso só eu diria?** Tabela: frases que continuariam verdadeiras com o nome de outro perfil (genéricas) x frases que só ela diria. Cite as frases exatas.
6. **Quem comenta é quem compra?** Comentários reais entre aspas; o que é desejo, pedido de conteúdo e objeção.
7. **O que diferencia aparece?** A prova mais forte que existe (inclusive em post de terceiros) x a que o perfil usa.
8. **O que fazer esta semana:** bio (nome, pra quem, uma prova), 3 posts concretos tirados dos achados, 1 coisa pra pausar.

## Passo 4: entregue a página
- Use `modelo.html` (nesta pasta) SÓ como modelo de visual e estrutura. Ele tem campos
  {{assim}}: troque cada um pelos dados REAIS que você puxou do Apify. NUNCA publique os
  números de exemplo do modelo. Troque cores e fontes pelas da identidade visual dela, se houver.
- Salve em `pesquisa/traducao-<perfil>-<AAAA-MM-DD>.html` com a ferramenta de escrever arquivo (não pelo terminal, que quebra acento) e abra.
- No chat, só o resumo: o achado principal e as 3 ações.

## Se o perfil ainda não vende nada
Muita gente está começando. Se o perfil não tem produto ou serviço à venda,
troque "o que vende" por "o que gera conversa e seguidores" nas perguntas 1 e 4,
e na pergunta 8 sugira o primeiro passo pra transformar o perfil num canal
(bio clara, um assunto principal, 3 posts). Nunca trate isso como defeito.

## Regras
- Nunca invente número. Tudo que não veio do Apify é SUPOSIÇÃO.
- Salvamentos, compartilhamentos, cliques e vendas não são públicos: diga que ficaram fora.
- Nome de quem comentou nunca aparece na página, nem @marcações dentro do texto. Só o texto do comentário.
- No fim, diga o custo estimado no Apify (cerca de US$ 0,25 por Tradução, dos US$ 5 grátis por mês).
- Português simples. Nada de jargão de marketing sem traduzir.
- Para concorrente: mesma leitura, versão curta (perguntas 1, 3, 5, 6), e no fim uma tabela
  comparando assunto por perfil e mostrando o assunto que ninguém ocupa.
