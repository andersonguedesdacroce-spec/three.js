# Rota GM Campinas

Painel de estudos para o concurso de Guarda Municipal de Campinas (Vunesp, prova em 21/03/2027).
Site estático de um único `index.html`, montado a partir de arquivos pequenos.

## Estrutura

| Pasta | O que tem |
| --- | --- |
| `src/base.html` | `<head>`, CSS e esqueleto da página |
| `src/edital.js` | constantes do edital e `TRILHAS` (matérias e postos) |
| `src/app.js` | toda a lógica do painel |
| `aulas/<posto>.html` | HTML da aula de cada posto |
| `bancos/<posto>.js` | as 60 questões de cada posto |
| `textos/*.json` | textos de apoio das questões (chave → HTML) |
| `gerador/aulas.py` | funções que geram aula, banco, mapa e documento de revisão |
| `conteudo/<posto>/` | script de conteúdo de cada posto (escrito em Markdown) |
| `revisao/<posto>.md` | aula, fontes, cobertura e pontos para revisão |
| `destaques/destaques.py` | caixas Cai muito, Cuidado e Macete inseridas pelo build nas aulas que não as têm (`python3 destaques/destaques.py` gera o JSON) |
| `MARKETING.md` | briefing de marketing: fatos verificáveis, público, mensagens, riscos e pendências antes de vender |
| `public/index.html` | **saída do build**, é o que o Vercel publica |
| `ferramentas/` | teste no navegador e comparador de builds |

## Fluxo de trabalho

```bash
pip install markdown                 # só para gerar conteúdo novo
python3 conteudo/<posto>/<posto>.py  # grava aulas/, bancos/, textos/ e revisao/
python3 build.py                     # valida os bancos e monta public/index.html
node ferramentas/testar.cjs public/index.html capturas pt-1,mt-1   # teste no Chromium (390 px e 1280 px, claro e escuro)
```

O `build.py` falha se um banco não tiver 60 questões (20/20/20), 5 alternativas distintas,
comentário, `id` com o prefixo certo e `id` único no painel, ou se um texto de apoio não existir.
Rode o build e **faça commit de `public/index.html`** junto com a mudança.

## Publicar no Vercel

O `vercel.json` já aponta `outputDirectory` para `public/`, sem etapa de build no servidor.
Se o repositório contiver outras pastas, em *Project Settings → General → Root Directory* escolha `rota-gm-campinas`.

## Recursos do painel

- **Página de vendas** com dados do edital, peso das matérias, amostra de aula e oferta (checkout ainda é demonstração).
- **Painel** com indicadores, sugestão do próximo posto, busca, revisões do dia, caderno de erros e peso da prova.
- **Mapa do edital**: cada item do Anexo I ligado ao posto que o cobre, com a situação do aluno.
- **Posto** com abas Aula, Resumo (mapa, destaques, armadilhas e quadro-resumo) e Questões.
- **Caixas com função**: azul conceito, verde regra, vermelho cuidado, amarelo cai muito, roxo macete.
- **Revisão espaçada** (1, 7 e 30 dias) e **caderno de erros** (erradas e marcadas; sai ao acertar).
- **Avise a equipe**: aviso de correção ao fim de cada aula, gravado no banco do painel (coleção `correcoes`).
- Progresso salvo no navegador e, no Claude, sincronizado pela conta (`data/users/<id>/progresso`).
- **Navegação**: menu no topo (computador) ou barra inferior (celular) com Painel, Edital, Simulado, Desempenho, Erros e Ranking; cada tela tem endereço próprio (`#posto-cp-14-video`), então o botão voltar do navegador funciona.
- **Vídeo**: postos listados em `videos/videos.json` ganham a aba Vídeo (ver `videos/LEIA-ME.md`). O build copia os arquivos para `public/videos/`.
- **Questões**: correção no final ou a cada questão (com comentário na hora); atalhos de teclado A a E e Enter.
- **Simulado**: 50 questões em 3 horas na proporção do edital (12, 6, 2 e 30), com mapa de respostas, relógio e resultado por matéria.
- **Desempenho**: percentual de acerto por matéria, indicação de onde focar e histórico dos simulados.
- **Meta diária** de questões e sequência de dias de estudo no painel; ajuste do tamanho do texto da aula.
