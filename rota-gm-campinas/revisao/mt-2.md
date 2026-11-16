# Revisão do posto mt-2: Mínimo múltiplo comum e máximo divisor comum

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 7 com texto de apoio (mt2a, mt2b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 5, 7, 8, 9 (questões resolvidas na seção 6).

## Fontes

Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.

Conferidas nesta produção:

- Cálculos: assert no script conteudo/mt2/mt2.py.

## Verificação de cobertura

- Recorte do edital: “situações-problema” com MMC e MDC. Cobertos: múltiplos, divisores, primos, fatoração, critérios de divisibilidade, contagem de divisores, MDC (fatoração e Euclides), MMC (fatoração e decomposição simultânea), relação MDC × MMC, problemas de partes iguais, coincidência, resto constante e frações irredutíveis.

## Pontos para revisão (não conferidos na fonte)

- Referências bibliográficas citadas como base; não foram consultadas página a página.
- Gabaritos e exemplos conferidos por código (math.gcd e contagens por força bruta); a redação dos enunciados continua para revisão humana.

## Aula

**MMC e MDC são as duas ferramentas para problemas de repetição e de divisão em partes iguais. O MMC responde quando duas coisas que se repetem em ritmos diferentes voltam a coincidir; o MDC responde qual é o maior pedaço, ou o maior grupo, que reparte tudo sem sobra. A Vunesp quase nunca pede o cálculo seco: pede a situação (rondas que se cruzam, material a repartir em kits, número que deixa resto) e espera que você reconheça qual das duas ferramentas usar. Esta aula ensina o cálculo e, principalmente, o reconhecimento.**

## 1. Múltiplos, divisores e números primos

Múltiplos de um número são os resultados da sua tabuada: os múltiplos de 6 são 0, 6, 12, 18, 24 e assim sem fim. Divisores de um número são os que o dividem sem deixar resto: os divisores de 12 são 1, 2, 3, 4, 6 e 12. Múltiplo e divisor são dois lados da mesma relação: se 12 é múltiplo de 4, então 4 é divisor de 12.

Número primo é o que tem exatamente dois divisores, o 1 e ele mesmo: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. O 2 é o único primo par, e o 1 não é primo, porque tem um só divisor. Os demais números, de dois divisores para cima, são os compostos, e todo composto pode ser escrito, de uma única maneira, como produto de primos. Esse é o teorema da fatoração, e é a chave de tudo nesta aula.

Para fatorar, divida o número pelo menor primo possível, de novo e de novo, até chegar a 1. Fatorando 60: 60 ÷ 2 = 30, 30 ÷ 2 = 15, 15 ÷ 3 = 5, 5 ÷ 5 = 1. Logo 60 = 2<sup>2</sup> × 3 × 5. Os critérios de divisibilidade aceleram o trabalho. Um número é divisível por 2 se termina em algarismo par; por 3 se a soma dos algarismos é múltipla de 3; por 4 se os dois últimos algarismos formam número divisível por 4; por 5 se termina em 0 ou 5; por 6 se é divisível por 2 e por 3; por 9 se a soma dos algarismos é múltipla de 9; por 10 se termina em 0. O número 4.527 tem soma 4 + 5 + 2 + 7 = 18, então é divisível por 9.

A fatoração também conta divisores. Some 1 a cada expoente e multiplique os resultados. Em 60 = 2<sup>2</sup> × 3<sup>1</sup> × 5<sup>1</sup>, o número de divisores é (2 + 1)(1 + 1)(1 + 1) = 12. A razão é que cada divisor escolhe, para cada primo, um expoente de zero até o expoente máximo.

## 2. MDC: o maior pedaço que cabe exato

O máximo divisor comum de dois ou mais números é o maior número que divide todos eles. Imagine duas cordas, de 84 m e de 126 m, que devem ser cortadas em pedaços iguais, sem sobrar nada, e com pedaços os maiores possíveis. O tamanho do pedaço precisa dividir 84 e dividir 126; o maior que faz isso é o MDC, que aqui vale 42 m. Sai 2 pedaços da primeira corda e 3 da segunda.

Há dois métodos. No primeiro, decompõem-se os números em fatores primos e multiplicam-se apenas os fatores comuns, cada um com o menor expoente. Com 84 = 2<sup>2</sup> × 3 × 7 e 126 = 2 × 3<sup>2</sup> × 7, os comuns são 2 (menor expoente 1), 3 (menor expoente 1) e 7 (expoente 1). O MDC é 2 × 3 × 7 = 42.

O segundo método é o algoritmo de Euclides, útil com números grandes. Divide-se o maior pelo menor; depois, o divisor pelo resto, e assim por diante, até o resto zero. O último divisor é o MDC. Para 252 e 420: 420 = 1 × 252 + 168; 252 = 1 × 168 + 84; 168 = 2 × 84 + 0. O MDC é 84.

Dois números cujo MDC é 1 são chamados primos entre si, mesmo que cada um não seja primo: 8 e 15 não têm fator comum. O MDC também simplifica frações até a forma irredutível: 252/420 tem MDC 84, e dividindo em cima e embaixo por 84, vem 3/5.

> **Nota:** Para o MDC, pegue só os fatores comuns e o menor expoente. Para o MMC, pegue todos os fatores e o maior expoente. Se confundir, o MDC nunca ultrapassa o menor dos números, e o MMC nunca é menor que o maior deles.

## 3. MMC: quando os ritmos voltam a coincidir

O mínimo múltiplo comum de dois ou mais números é o menor número, diferente de zero, que é múltiplo de todos eles. A imagem útil é a de dois sinais que repetem em ritmos diferentes. Um apita a cada 4 minutos e o outro a cada 6. Apitaram juntos agora; quando apitarão juntos de novo? O primeiro apita nos minutos 4, 8, 12, 16...; o segundo, nos minutos 6, 12, 18... O primeiro minuto comum é o 12, que é o MMC de 4 e 6.

Pela fatoração, o MMC é o produto de todos os fatores primos, comuns e não comuns, cada um com o maior expoente. Para 12, 18 e 30, tem-se 12 = 2<sup>2</sup> × 3, 18 = 2 × 3<sup>2</sup> e 30 = 2 × 3 × 5. O maior expoente do 2 é 2, o do 3 é 2 e o do 5 é 1. O MMC é 2<sup>2</sup> × 3<sup>2</sup> × 5 = 180.

Há um jeito prático, a decomposição simultânea. Escrevem-se os números lado a lado e divide-se por primos, dividindo apenas os que forem divisíveis e repetindo os demais; o MMC é o produto dos divisores usados. Em 12, 18, 30: por 2, vira 6, 9, 15; por 2, vira 3, 9, 15; por 3, vira 1, 3, 5; por 3, vira 1, 1, 5; por 5, vira 1, 1, 1. O produto 2 × 2 × 3 × 3 × 5 é 180.

Quando os números são primos entre si, o MMC é o produto deles: MMC(3, 5) = 15. Quando um é múltiplo do outro, o MMC é o maior: MMC(5, 10) = 10.

## 4. A relação entre MMC e MDC

Para dois números a e b, vale que MDC(a, b) × MMC(a, b) = a × b. A razão está na fatoração: de cada primo, o MDC leva o menor expoente e o MMC leva o maior, e juntos usam os dois expoentes, que é exatamente o que o produto a × b faz. Com 12 e 18: MDC = 6, MMC = 36, e 6 × 36 = 216 = 12 × 18.

A relação resolve um tipo clássico de questão: dados o MDC, o MMC e um dos números, achar o outro. Se o MDC de dois números é 6, o MMC é 60 e um deles é 12, o outro é 6 × 60 ÷ 12 = 30. Também mostra que o MDC divide o MMC e que o MMC é múltiplo de ambos. A relação vale para dois números; com três ou mais, não vale.

## 5. Como reconhecer o problema

A dificuldade da prova está em saber qual ferramenta usar. O texto da questão costuma dar o sinal.

Use o MDC quando o enunciado fala em dividir, repartir, cortar ou agrupar em partes iguais, sem sobra, e pede o maior tamanho ou o maior número de grupos. As palavras são “o maior possível”, “o maior número de equipes”, “pedaços iguais”, “sem sobrar”.

Use o MMC quando o enunciado fala em eventos que se repetem e voltam a coincidir, ou em achar o menor número que seja múltiplo de vários. As palavras são “de quanto em quanto tempo”, “novamente juntos”, “o menor número”, “pela primeira vez”.

Exemplo resolvido 1, com MDC. Uma equipe tem 72 coletes e 108 lanternas, que serão distribuídos em kits iguais, sem sobras. Qual o maior número de kits? Como a repartição é em partes iguais e se quer o maior número de kits, é MDC(72, 108). Fatorando, 72 = 2<sup>3</sup> × 3<sup>2</sup> e 108 = 2<sup>2</sup> × 3<sup>3</sup>. O MDC é 2<sup>2</sup> × 3<sup>2</sup> = 36 kits, cada um com 2 coletes e 3 lanternas.

Exemplo resolvido 2, com MMC. Duas viaturas passam por um cruzamento, uma a cada 10 minutos e outra a cada 15. Passaram juntas às 8h. Quando passam juntas de novo? Como os ritmos voltam a coincidir, é MMC(10, 15) = 30. Passam juntas de novo às 8h30.

Exemplo resolvido 3, com resto. Qual o menor número natural maior que 1 que, dividido por 4, por 6 e por 9, deixa sempre resto 1? Se sobra 1 em cada divisão, então o número menos 1 é múltiplo de 4, de 6 e de 9. O menor múltiplo comum é MMC(4, 6, 9) = 36. O número procurado é 36 + 1 = 37. Conferindo: 37 = 4 × 9 + 1 = 6 × 6 + 1 = 9 × 4 + 1.

Exemplo resolvido 4, com MMC em contagem. Três ônibus saem às 6h de um terminal, com intervalos de 15, 20 e 24 minutos. Quantas vezes saem juntos entre 6h e 18h, contando a saída das 6h? O MMC(15, 20, 24) = 120 minutos, ou 2 horas. Em 12 horas cabem 6 intervalos de 2 horas, e as saídas coincidentes acontecem às 6h, 8h, 10h, 12h, 14h, 16h e 18h. São 7 vezes.

## 6. Questões resolvidas

### Questão 1

Duas luzes de sinalização piscam, uma a cada 8 segundos e outra a cada 12 segundos. Piscaram juntas num instante inicial. Piscarão juntas novamente depois de

- (A) 4 segundos.
- (B) 20 segundos.
- (C) 48 segundos.
- (D) 24 segundos.
- (E) 96 segundos.

**Resposta: D.** Coincidência de ritmos pede MMC. 8 = 2<sup>3</sup> e 12 = 2<sup>2</sup> × 3, então MMC = 2<sup>3</sup> × 3 = 24 segundos.

### Questão 2

Um posto tem 90 coletes e 150 lanternas, que serão distribuídos em kits idênticos, sem sobras, com o maior número possível de kits. Cada kit terá

- (A) 9 coletes e 15 lanternas.
- (B) 3 coletes e 5 lanternas.
- (C) 1 colete e 5 lanternas.
- (D) 30 coletes e 50 lanternas.
- (E) 6 coletes e 10 lanternas.

**Resposta: B.** Partes iguais e o maior número de kits: MDC(90, 150) = 30 (90 = 2 × 3<sup>2</sup> × 5; 150 = 2 × 3 × 5<sup>2</sup>; comuns 2 × 3 × 5). Com 30 kits, cada um recebe 90 ÷ 30 = 3 coletes e 150 ÷ 30 = 5 lanternas.

### Questão 3

O menor número natural que, dividido por 6, por 8 e por 10, deixa sempre resto 4 é

- (A) 120
- (B) 244
- (C) 64
- (D) 84
- (E) 124

**Resposta: E.** O número menos 4 é múltiplo de 6, 8 e 10. MMC(6, 8, 10) = 120. O número é 120 + 4 = 124. Confira: 124 = 6 × 20 + 4 = 8 × 15 + 4 = 10 × 12 + 4.

### Questão 4

O produto de dois números naturais é 1.296 e o MDC deles é 6. O MMC desses números é

- (A) 1.290
- (B) 7.776
- (C) 216
- (D) 162
- (E) 432

**Resposta: C.** MDC × MMC = produto. MMC = 1.296 ÷ 6 = 216.

## 7. Na rotina do guarda

- **Cruzamento de rondas:** duas equipes com voltas de 20 e 30 minutos se reencontram a cada MMC(20, 30) = 60 minutos. Saber disso ajuda a marcar o momento da troca de informações.
- **Montagem de kits:** 48 cones e 60 coletes viram, no máximo, MDC(48, 60) = 12 kits iguais.
- **Escala de folgas:** quem folga a cada 4 dias e quem folga a cada 6 só têm folga juntos a cada MMC(4, 6) = 12 dias.
- **Fiscalizações periódicas:** inspeções a cada 15 e a cada 21 dias coincidem a cada 105 dias, que é o MMC.
- **Fila de identificação:** 36 homens e 48 mulheres podem formar, no máximo, MDC(36, 48) = 12 grupos com a mesma composição.

## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Usar MMC em questão de dividir em partes iguais | “O maior possível” e “sem sobra” pedem MDC |
| Usar MDC em questão de coincidência | “Novamente juntos” e “o menor” pedem MMC |
| Esquecer de somar o resto no “menor número que deixa resto r” | Número = MMC + r |
| Dar como MMC um valor menor que algum dos números | O MMC nunca é menor que o maior número |
| Contar a saída inicial ou não, em “quantas vezes coincidem” | Releia se o início “conta”; some 1 aos intervalos quando contar |
| Pegar fatores comuns de maior expoente no MDC | No MDC é o menor expoente; no MMC, o maior |
| Aplicar MDC × MMC = produto com três números | A relação só vale para dois números |
| Tratar 1 como número primo | Primo tem exatamente dois divisores |

## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Primo | Exatamente dois divisores; o 2 é o único par |
| Fatoração | Divide pelo menor primo até chegar a 1 |
| Quantidade de divisores | Soma 1 a cada expoente e multiplica |
| MDC | Fatores comuns, menor expoente; partes iguais, o maior possível |
| MMC | Todos os fatores, maior expoente; ritmos que coincidem |
| Relação | MDC × MMC = a × b, só para dois números |
| Resto igual r | Número = MMC + r |
| Euclides | Divide o maior pelo menor, repete com o resto; o último divisor é o MDC |
