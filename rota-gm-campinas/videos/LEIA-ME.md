# Vídeos das aulas

Padrão aprovado: animação sincronizada com narração (voz "Henrique", ElevenLabs, modelo eleven_v4), 1920×1080, com legendas.
**Regra:** o vídeo pode ser resumido, mas passa por todas as seções da aula do posto.

## Como funciona o motor (`motor/`)

1. `fonte/<posto>/roteiro.json`: lista de cenas. Tipos: `capa`, `lei`, `lista`, `versus`, `caso`, `alerta`, `resumo` (a tela final da marca entra sozinha).
   No campo `fala` de cada cena, `{1}`, `{s}`, `{p}`, `{g}`, `{r}`, `{f}` marcam o instante em que cada elemento entra;
   `[[316|trezentos e dezesseis]]` mostra "316" na legenda e manda o texto por extenso para a voz.
2. `python3 motor/alinhar.py fonte/<posto> --estimar` grava `narracao.txt` (o texto que vai para a voz) e tempos estimados;
   `node motor/gerar.cjs fonte/<posto> auto` tira uma foto de cada cena para conferir o visual antes de gastar créditos.
3. Gerar a narração com o texto de `narracao.txt` (cada caractere custa 1 crédito) e salvar como `fonte/<posto>/voz.mp3`.
4. `motor/produzir.sh <posto> "<url do mp3>"` (ou `""` se o mp3 já estiver na pasta): alinha a voz ao roteiro pelas pausas da fala,
   renderiza, copia `<posto>.mp4` e a capa e registra em `videos.json`. Depois, `python3 build.py`.

## Situação

Ver `FILA.md`.
