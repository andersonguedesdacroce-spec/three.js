# Pendências para a próxima sessão

Registradas em 14/11/2026, a pedido do Anderson. Nada aqui foi feito ainda, salvo o que está marcado como corrigido.

## 1. Vídeos precisam cobrir a aula inteira

- O vídeo do posto **cp-14** trata só de concussão e corrupção passiva. O posto também tem excesso de exação,
  facilitação de contrabando, **prevaricação** e **condescendência criminosa** (arts. 316 a 320).
- **Regra para todos os vídeos daqui em diante:** o vídeo pode ser resumido, mas tem de passar por todos os tópicos
  da aula do posto (todas as seções numeradas). Roteiro = uma cena por seção da aula, mais abertura, teste e resumo.
- **Feito em 15/11:** o vídeo do cp-14 foi refeito e agora cobre os seis crimes do posto (3min32). Também foram publicados gm-1 e ctn-1.
- **Bloqueio:** a cota de 10.000 créditos do ElevenLabs acabou. Há quatro roteiros prontos à espera de narração (ver `videos/FILA.md`).
  Para cobrir os 91 postos é preciso um plano maior do ElevenLabs (cerca de 280 mil créditos) ou outra voz.
- Padrão visual e de narração aprovado: o do vídeo atual (modelo Fable 5.2; voz "Henrique" do ElevenLabs). Ver `videos/LEIA-ME.md`.

## 2. Texto de lei nas aulas está ruim de ler

- As citações de lei aparecem como um bloco corrido, com caput, parágrafos, incisos e a pena na mesma linha.
- A fazer, em todas as aulas (826 citações; 90 delas com mais de 900 caracteres, em 37 postos):
  - quebrar a citação em linhas: caput, cada parágrafo (§), cada inciso (I, II, III) e cada alínea em linha própria;
  - destacar a **pena** em linha separada;
  - recolher citações longas ("ver o artigo completo") e mostrar só o trecho que a aula explica;
  - rever tipografia e espaçamento do bloco de lei (hoje serifado, corpo grande, sem respiro).
- O melhor lugar para fazer isso é a função `LEI`/`LEIS` de `conteudo/_fontes.py` e o CSS `blockquote.lei` em `src/base.html`,
  para valer em todos os postos de uma vez.

### Erro de conteúdo encontrado ao investigar (corrigido)

- **cp-14**, citação "art. 317, §§ 1º e 2º": o trecho copiado começava no § 1º de outro artigo (art. 147) e trazia
  mais de 100 mil caracteres de artigos que não são do posto. **Corrigido.**
- **ctb-9**, citação "art. 282, § 7º": mesmo problema, com 13,8 mil caracteres a mais. **Corrigido.**
- O `build.py` agora recusa qualquer citação de lei com mais de 6.000 caracteres, para isso não voltar.
- Ainda vale conferir as 10 citações longas que juntam vários artigos num bloco só (ctb-7, ctb-8 e ctb-10):
  o texto é do posto, mas deveria estar separado por artigo.
- **ctn-1**, citação do art. 79: o trecho avançava sobre o art. 80. **Corrigido.**
