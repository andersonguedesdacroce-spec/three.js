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
