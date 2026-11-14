# Vídeos das aulas

Padrão dos vídeos: animação em HTML sincronizada com a narração, gravada quadro a quadro (1920×1080, 30 qps) e unida ao áudio com ffmpeg.

- `videos.json`: lista dos vídeos publicados (posto → título, duração, arquivo, capa). O `build.py` copia os arquivos para `public/videos/` e a aba **Vídeo** aparece no posto.
- `fonte-<posto>/aula.html`: cenas e linha do tempo (`CUES` traz o início e o fim de cada frase da narração).
- `fonte-<posto>/voz.mp3`: narração (ElevenLabs, voz "Henrique", modelo eleven_v4).
- `fonte-<posto>/render.cjs`: `node render.cjs` gera `aula-fable.mp4` na pasta.

## Como fazer um vídeo novo
1. Escreva o roteiro (cerca de 90 segundos, 7 cenas: gancho, o que é comum, a diferença, teste com casos, detalhe de prova, resumo, marca).
2. Gere a narração e meça as pausas: `ffmpeg -i voz.mp3 -af silencedetect=noise=-35dB:d=0.25 -f null -`.
3. Copie uma pasta `fonte-*`, troque as cenas e ajuste os tempos de `CUES` e das animações às pausas medidas.
4. `node render.cjs`, copie o MP4 para `videos/<posto>.mp4`, gere a capa e registre em `videos.json`.
