# Prompt para produzir o vídeo de um posto

Copie o bloco abaixo, troque `<POSTO>` (ex.: `cp-7`) e cole numa sessão nova do Claude Code aberta neste repositório.
Serve para Sonnet 5.5, Fable 5.2 ou Opus 5.5: a qualidade visual e a sincronia vêm do motor em `videos/motor/`; o modelo só escreve o roteiro e opera os comandos.

---

## PROMPT (copiar daqui)

Você vai produzir o vídeo-aula do posto **<POSTO>** do projeto Rota GM Campinas (pasta `rota-gm-campinas/`). Responda sempre em português do Brasil.
Não publique nada e não faça commit antes de eu pedir. Antes de começar, leia `videos/LEIA-ME.md`, `videos/FILA.md` e um roteiro de exemplo: `videos/fonte/cp-14/roteiro.json` (aula longa) e `videos/fonte/ctn-1/roteiro.json` (aula curta).

### 1. Ler a aula inteira
Leia `aulas/<POSTO>.html` e `revisao/<POSTO>.md`. Liste as seções numeradas da aula (os `<h3>`), excluindo "Questões resolvidas", "Na rotina do guarda", "Onde a Vunesp pega" e "Quadro-resumo" (estas viram o teste e o resumo do vídeo).
**Regra de ouro: o vídeo pode ser resumido, mas tem de passar por todas as seções de conteúdo da aula.** Faça uma tabela "seção da aula → cena do vídeo" e confira que nenhuma ficou de fora.
Use somente fatos que estão na aula (artigos, prazos, penas, números). Não acrescente nada de memória. Se a aula citar um valor, copie igual.

### 2. Escrever `videos/fonte/<POSTO>/roteiro.json`
Estrutura: `{"posto","titulo","chamada":"Agora faça as questões deste posto","cenas":[...]}`. A tela final com a marca é automática.
Ordem das cenas: capa → uma ou mais cenas por seção da aula → 1 a 3 casos para testar (`caso`) → resumo. Entre 8 e 14 cenas, 2 a 4 minutos no total.

Tipos de cena e campos (`cor` é uma de: red, blue, amber, green, violet, navy):
| Tipo | Campos | Use para |
| --- | --- | --- |
| `capa` | sobre, titulo, gancho | primeira cena |
| `lei` | cor, rotulo, selo, def, pena, itens | um artigo ou crime: palavra-chave em carimbo (`selo`), pena em faixa (`pena`), até 3 itens |
| `lista` | cor, sobre, titulo, itens | enumerações (de 3 a 5 itens) |
| `versus` | titulo, a{cor,rotulo,titulo,itens}, b{...} | duas coisas que a banca confunde |
| `alerta` | cor, rotulo, titulo, grande, sub, itens | pegadinha ou "cai muito" (`grande` é uma palavra ou número, curto) |
| `caso` | cor, sobre, titulo, texto, selo, resposta, porque | exercício rápido com resposta |
| `resumo` | sobre, linhas [[pergunta, resposta, cor]], final | última cena de conteúdo, 3 a 4 linhas |

Itens têm a forma `"Destaque|resto da frase"`. O destaque aparece em negrito colorido (até 4 palavras). No texto de `caso`, `**assim**` vira negrito. No `final` do resumo, `*palavra*` vira destaque amarelo.

### 3. Escrever a fala de cada cena (`fala`)
- Fala natural, em frases curtas, como um professor: "Primeiro, ...", "Cuidado com...", "Resumindo...". Sem listas de siglas e sem juridiquês desnecessário.
- Cada cena tem de 40 a 110 palavras. A fala **de cada cena** fala tudo o que está escrito na tela daquela cena, e a tela não traz nada que a fala não diga.
- Marcadores de entrada dos elementos, colocados **imediatamente antes** da palavra em que o elemento deve aparecer: `{1}`, `{2}`, `{3}`... para os itens, na ordem; `{s}` selo; `{d}` definição; `{p}` pena/faixa; `{g}` palavra grande do alerta; `{r}` resposta do caso; `{q}` o porquê; `{f}` frase final do resumo. Em `versus`, a numeração continua do lado A para o B.
- Números e siglas pela voz: `[[316|trezentos e dezesseis]]` mostra "316" na legenda e a voz lê por extenso. Use para artigos, anos, números de decisões ("Tema [[656|seiscentos e cinquenta e seis]]"), percentuais ("zero vírgula quatro por cento") e siglas lidas letra a letra ("[[ADPF 995|A D P F novecentos e noventa e cinco]]"). Não escreva dígitos soltos fora desse formato.
- Evite parênteses, travessões, abreviações e símbolos na fala (a voz os lê mal). Escreva "por cento", "artigo", "parágrafo primeiro".
- Cada cena deve poder ser entendida sozinha e terminar numa frase pontuada com ponto.

### 4. Conferir o visual ANTES de gastar créditos
```bash
cd videos
python3 motor/alinhar.py fonte/<POSTO> --estimar     # grava narracao.txt e tempos estimados
node motor/gerar.cjs fonte/<POSTO> auto               # uma foto por cena em fonte/<POSTO>/foto-NN.jpg
```
Abra as fotos (junte 4 por imagem com ffmpeg `hstack`/`vstack`) e verifique, cena por cena: texto cortado ou sobreposto, título longo demais (quebrar o título em menos palavras), cena vazia ou tela com texto demais (máximo 5 itens), contraste, e se o `grande` do alerta cabe. Corrija o roteiro e repita. Apague as fotos no fim.

### 5. Narração (gasta créditos do ElevenLabs: perguntar antes)
1. Leia `fonte/<POSTO>/narracao.txt` e informe ao usuário o número de caracteres (1 caractere = 1 crédito) e peça confirmação antes de gerar. Veja o saldo em `videos/FILA.md`.
2. Gere uma única vez com `creative_generate_speech`: `model_id` = `eleven_v4`, `voice_id` = `3ULAAai0IVN00DTWA6vF` (voz "Henrique"), `generations_count` = 1, `prompt` = o texto exato de `narracao.txt`. **Nunca chame de novo para tentar outra vez**: cada chamada cobra de novo.
3. Consulte `creative_get_flow_run_status` até concluir e pegue a URL do mp3. O ambiente precisa permitir o host `elevenlabsusercontent.com`.
4. Se a cota acabar, pare, deixe o roteiro pronto e registre o posto em `videos/FILA.md`, na seção "Roteiro pronto, falta só a narração".

### 6. Produzir
```bash
motor/produzir.sh <POSTO> "<URL do mp3>"
```
O script baixa a voz, alinha cada frase às pausas reais da fala, renderiza (leva de 5 a 15 minutos; rode em segundo plano), copia `<POSTO>.mp4` e a capa e registra em `videos/videos.json`.
Depois rode `python3 build.py`, confira 4 ou 5 quadros do MP4 (`ffmpeg -ss <t> -i <POSTO>.mp4 -frames:v 1`) e rode `node ferramentas/testar.cjs public/index.html /tmp/saida <POSTO>`.

### 7. Entregar
Atualize `videos/FILA.md`. Mostre ao usuário o MP4 e um resumo: duração, seções da aula cobertas, créditos gastos. Só faça commit, push ou publicação se o usuário pedir.

### Lista de verificação final (todas as respostas devem ser "sim")
- Todas as seções de conteúdo da aula aparecem no vídeo?
- Todo número, artigo e pena do vídeo está igual ao da aula?
- Nenhum texto cortado, sobreposto ou ilegível em nenhuma cena?
- A fala não usa dígitos soltos, parênteses nem siglas sem `[[ ]]`?
- A narração foi gerada uma única vez?
- O vídeo termina com o resumo e a chamada para as questões?

## FIM DO PROMPT

---

## Observações para quem for usar

- **Um posto por sessão** rende melhor: ler a aula e escrever o roteiro ocupa pouco contexto, mas a renderização demora.
- **Teste primeiro com um posto já feito** (por exemplo `ctn-1`): peça para gerar o roteiro sem olhar o existente e compare com `fonte/ctn-1/roteiro.json`. Só depois siga para a fila.
- **Custo**: cerca de 3.200 créditos de narração por vídeo; a cota atual está esgotada (ver `FILA.md`).
- **Alinhamento**: se a legenda ficar adiantada ou atrasada em algum trecho, o ajuste está em `motor/alinhar.py` (a função que casa orações com pausas). O vídeo não precisa ser refeito do zero: basta rodar `produzir.sh` de novo com o mesmo mp3.
