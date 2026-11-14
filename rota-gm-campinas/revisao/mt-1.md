# Revisão do posto mt-1: Operações com números racionais

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 8 com texto de apoio (mt1a, mt1b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11 (questões resolvidas na seção 8).

## Fontes

Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1 e 2; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; todos os resultados foram recalculados em código.

Conferidas nesta produção:

- Gabaritos e exemplos: recalculados com Fraction/Decimal (assert no script conteudo/mt1/mt1.py).

## Verificação de cobertura

- Recorte do edital: “adição a radiciação, em forma fracionária ou decimal”. Cobertos: adição, subtração, multiplicação, divisão, potenciação (inclui expoente zero e negativo), radiciação, decimais, dízimas periódicas e geratriz, números mistos e ordem das operações.
- Não coberto de propósito: racionalização com binômios e raízes de índice maior que 3, por estarem acima do nível esperado para o cargo.

## Pontos para revisão (não conferidos na fonte)

- Referências bibliográficas (Iezzi et al.; Dante) citadas como base; não foram consultadas página a página nesta produção.
- Todos os cálculos da aula e os gabaritos foram verificados por código (módulo fractions do Python). A conferência humana do enunciado e da redação das alternativas continua valendo.
- A regra da geratriz da dízima composta foi explicada em prosa; vale ler com olho de aluno.

## Aula

**Operações com números racionais é a base de todo o resto da prova de Matemática: porcentagem, regra de três, equação e média dependem de somar, multiplicar e dividir frações e decimais sem errar. A Vunesp cobra quatro coisas: operar com frações, operar com decimais, passar de um formato ao outro (inclusive a dízima periódica) e resolver expressões que misturam tudo isso, com potência e raiz, na ordem certa. Esta aula parte da ideia de cada operação e só depois chega à regra.**

## 1. O que é um número racional

Número racional é todo número que pode ser escrito como fração a/b, com a e b inteiros e b diferente de zero. Cabem aí os inteiros (5 = 5/1), os decimais finitos (0,75 = 3/4) e as dízimas periódicas (0,333... = 1/3). Fora dos racionais ficam, por exemplo, a raiz de 2 e o pi, que não têm representação como fração.

A melhor maneira de pensar numa fração é como uma divisão que ainda não foi feita. A fração 3/4 é “3 dividido por 4”: três barras de chocolate repartidas entre quatro pessoas dão 0,75 de barra para cada uma. O denominador diz em quantas partes iguais o inteiro foi cortado; o numerador diz quantas dessas partes entram na conta. Por isso o denominador não pode ser zero: ninguém corta uma barra em zero pedaços.

Duas frações podem ter escrita diferente e valer o mesmo. Multiplicar ou dividir numerador e denominador pelo mesmo número não muda o valor, porque é o mesmo que multiplicar por 1 (2/2 = 1). Assim, 1/2 = 2/4 = 50/100. Simplificar uma fração é fazer esse caminho de volta, dividindo em cima e embaixo pelo maior divisor comum, até a fração ficar irredutível: 18/24 = 3/4. Quando o numerador é maior que o denominador, a fração é imprópria e pode virar número misto: 7/3 = 2 inteiros e 1/3, escrito 2 1/3. Para voltar, multiplica-se o inteiro pelo denominador e soma-se o numerador: 2 1/3 = (2 × 3 + 1)/3 = 7/3.

Para comparar duas frações, leve-as ao mesmo denominador e compare os numeradores. Qual é maior, 5/8 ou 7/12? O menor múltiplo comum de 8 e 12 é 24. Então 5/8 = 15/24 e 7/12 = 14/24. Como 15 é maior que 14, 5/8 é maior. Conferindo em decimal: 5/8 = 0,625 e 7/12 = 0,583.

## 2. Somar e subtrair frações

Somar frações é como somar pedaços: só faz sentido juntar pedaços do mesmo tamanho. Três quartos de pizza mais dois terços de pizza não dão “cinco quartos-e-terços” de nada. Antes de somar, é preciso cortar tudo em pedaços do mesmo tamanho, e isso é achar o denominador comum. O mais enxuto é o menor múltiplo comum (MMC) dos denominadores.

O caminho tem quatro passos: achar o MMC; transformar cada fração em outra equivalente com esse denominador; somar ou subtrair só os numeradores, mantendo o denominador; simplificar o resultado. Quando não se quer calcular o MMC, vale o atalho geral a/b + c/d = (a × d + b × c) / (b × d), que funciona sempre, mas pode exigir simplificação no fim.

Exemplo resolvido. Quanto vale 2/3 + 3/4 − 1/6? O MMC de 3, 4 e 6 é 12. Então 2/3 = 8/12, 3/4 = 9/12 e 1/6 = 2/12. A conta fica (8 + 9 − 2)/12 = 15/12. Dividindo em cima e embaixo por 3, vem 5/4, que é o mesmo que 1 1/4.

Com números mistos há dois caminhos. O primeiro transforma tudo em fração imprópria: 2 1/2 + 1 2/3 = 5/2 + 5/3 = 15/6 + 10/6 = 25/6 = 4 1/6. O segundo soma separadamente a parte inteira e a fracionária: 2 + 1 = 3 e 1/2 + 2/3 = 3/6 + 4/6 = 7/6 = 1 1/6; no total, 3 + 1 1/6 = 4 1/6. Na subtração com misto, o primeiro caminho costuma ser mais seguro. Para calcular 5 − 1 3/4, escreva 5 = 20/4 e 1 3/4 = 7/4; a diferença é 13/4 = 3 1/4.

> **Nota:** Nunca some denominadores. 1/2 + 1/3 não é 2/5. O denominador diz o tamanho do pedaço e não muda quando os pedaços já são iguais: 1/5 + 2/5 = 3/5, porque um quinto e mais dois quintos são três quintos.

## 3. Multiplicar e dividir frações

Multiplicar frações é pegar uma parte de uma parte. A metade de um terço de barra é um sexto de barra: 1/2 × 1/3 = 1/6. Por isso a palavra “de” na matemática quer dizer multiplicação. A regra sai daí: multiplica-se numerador por numerador e denominador por denominador. Antes de multiplicar vale simplificar em cruz, cortando um fator do numerador de uma fração com um fator do denominador da outra: 3/4 × 8/9 = (3 × 8)/(4 × 9), e como 3 cabe em 9 três vezes e 4 cabe em 8 duas vezes, sobra 1 × 2 sobre 1 × 3, ou seja, 2/3.

Dividir é perguntar quantas vezes um valor cabe em outro. Quantas meias-barras cabem em 3 barras? Cabem 6, porque cada barra tem duas metades: 3 ÷ 1/2 = 6. A regra é conservar a primeira fração, inverter a segunda e multiplicar: a/b ÷ c/d = a/b × d/c. A inversão faz sentido porque dividir por 1/2 é multiplicar por 2, e dividir por 3/4 é multiplicar por 4/3, que é quanto precisa para completar um inteiro.

Exemplo resolvido 1. Quantas garrafas de 3/4 de litro se enchem com 9 litros de água? A pergunta é “quantas vezes 3/4 cabe em 9”, então 9 ÷ 3/4 = 9 × 4/3 = 36/3 = 12 garrafas. Confira: 12 garrafas de 0,75 litro dão 9 litros.

Exemplo resolvido 2. Do efetivo de 120 guardas, 2/3 estão de serviço e, destes, 3/8 patrulham a pé. Quantos patrulham a pé? Primeiro, 2/3 de 120 são 120 × 2/3 = 80 guardas de serviço. Depois, 3/8 de 80 são 80 × 3/8 = 30 guardas a pé. De uma vez só: 2/3 × 3/8 = 6/24 = 1/4, e 1/4 de 120 é 30.

Quando a fração aparece sobre outra fração, a barra grande também é uma divisão. Em (1/2)/(3/4), faz-se 1/2 ÷ 3/4 = 1/2 × 4/3 = 4/6 = 2/3.

## 4. Decimais e dízimas periódicas

Um número decimal é uma fração cujo denominador é 10, 100, 1000 e assim por diante: 0,7 = 7/10; 0,07 = 7/100; 2,35 = 235/100. A vírgula separa os inteiros dos décimos, centésimos e milésimos, e é essa organização que dita as regras das operações.

Na soma e na subtração, alinhe a vírgula. É a mesma ideia do denominador comum: décimos só se somam com décimos, centésimos com centésimos. Para calcular 2,4 + 0,75, escreva 2,40 + 0,75 = 3,15. Para 5 − 1,35, escreva 5,00 − 1,35 = 3,65.

Na multiplicação, ignore as vírgulas, multiplique como se fossem inteiros e depois dê ao resultado tantas casas decimais quantas têm os dois fatores juntos. Em 0,12 × 0,3, faz-se 12 × 3 = 36, e como há duas casas num fator e uma no outro, o resultado tem três: 0,036. A razão é que 0,12 é 12/100 e 0,3 é 3/10; o produto é 36/1000.

Na divisão, multiplique dividendo e divisor pela mesma potência de 10 até o divisor virar inteiro. Isso não muda o resultado, porque é multiplicar a fração por 1. Em 7,5 ÷ 0,25, multiplicando os dois por 100 vem 750 ÷ 25 = 30. Multiplicar um decimal por 10, 100 ou 1000 é andar com a vírgula para a direita; dividir é andar para a esquerda.

Para passar de fração a decimal, divida o numerador pelo denominador: 3/4 = 3 ÷ 4 = 0,75. Para passar de decimal a fração, escreva sobre 10, 100 ou 1000 e simplifique: 0,375 = 375/1000 = 3/8.

Há frações cuja divisão nunca termina: 1/3 = 0,333... e 4/33 = 0,1212... São as dízimas periódicas, e o trecho que se repete é o período. Elas também são números racionais, e a fração que as origina é a geratriz. O método da geratriz usa a ideia de que multiplicar por 10 desloca a vírgula e permite subtrair a parte infinita. Para x = 0,333..., tem-se 10x = 3,333..., e subtraindo, 9x = 3, logo x = 1/3.

Na prática, há uma regra pronta. Na dízima periódica simples, o numerador é o período e o denominador tem tantos noves quanto os algarismos do período: 0,1212... = 12/99 = 4/33. Na dízima composta (há uma parte que não se repete, o antiperíodo), o numerador é o número formado pelo antiperíodo seguido do período, menos o antiperíodo, e o denominador tem tantos noves quanto os algarismos do período, seguidos de tantos zeros quanto os do antiperíodo. Para 0,2333..., o antiperíodo é 2 e o período é 3: numerador 23 − 2 = 21 e denominador 90, ou seja, 21/90 = 7/30. Se há parte inteira, ela entra à parte: 1,2333... = 1 + 7/30 = 37/30.

## 5. Potenciação

Potência é multiplicação repetida: 2<sup>5</sup> = 2 × 2 × 2 × 2 × 2 = 32. A base é o número que se repete e o expoente diz quantas vezes. Em 2<sup>5</sup>, a base é 2 e o expoente é 5.

As propriedades decorrem dessa contagem de fatores. Ao multiplicar potências de mesma base, somam-se os expoentes: 2<sup>3</sup> × 2<sup>2</sup> = 2<sup>5</sup>, pois são três fatores mais dois fatores. Ao dividir, subtraem-se: 2<sup>5</sup> ÷ 2<sup>2</sup> = 2<sup>3</sup>. Potência de potência multiplica os expoentes: (2<sup>3</sup>)<sup>2</sup> = 2<sup>6</sup>. O expoente também se distribui sobre produto e quociente: (2 × 3)<sup>2</sup> = 2<sup>2</sup> × 3<sup>2</sup> = 36. Mas não se distribui sobre soma: (2 + 3)<sup>2</sup> = 25, e não 2<sup>2</sup> + 3<sup>2</sup> = 13.

O expoente zero e o expoente negativo parecem regras decoradas, mas saem de uma escadinha. Cada vez que o expoente diminui uma unidade, o resultado é dividido pela base: 2<sup>3</sup> = 8, 2<sup>2</sup> = 4, 2<sup>1</sup> = 2, 2<sup>0</sup> = 1, 2<sup>−1</sup> = 1/2, 2<sup>−2</sup> = 1/4. Daí vêm as duas regras: todo número diferente de zero elevado a zero vale 1, e expoente negativo inverte a base, a<sup>−n</sup> = 1/a<sup>n</sup>. Em fração, inverte-se a fração: (1/2)<sup>−3</sup> = 2<sup>3</sup> = 8.

O sinal pede atenção. Base negativa com expoente par dá resultado positivo, porque os sinais negativos se anulam aos pares: (−3)<sup>2</sup> = 9. Com expoente ímpar, o resultado é negativo: (−2)<sup>3</sup> = −8. Sem parênteses, o expoente pega só o número: −3<sup>2</sup> = −(3<sup>2</sup>) = −9. Potência de fração eleva numerador e denominador: (2/3)<sup>2</sup> = 4/9.

Exemplo resolvido. Quanto vale 2<sup>5</sup> × 2<sup>−2</sup> ÷ 2<sup>2</sup>? Todos têm base 2, então basta operar os expoentes: 5 − 2 − 2 = 1. O resultado é 2<sup>1</sup> = 2.

## 6. Radiciação

A raiz é a operação inversa da potência. Perguntar “quanto é a raiz quadrada de 49?” é perguntar “que número elevado ao quadrado dá 49?”. A resposta é 7, porque 7<sup>2</sup> = 49. Do mesmo modo, a raiz cúbica de 27 é 3, porque 3<sup>3</sup> = 27. O número do índice diz que potência se desfaz; quando o índice é 2, ele costuma ficar oculto.

Algumas regras bastam para a prova. A raiz de um produto é o produto das raízes, e o mesmo vale para o quociente: √(a × b) = √a × √b e √(a/b) = √a / √b. Então √(9/16) = 3/4, e √0,25 = 0,5, porque 0,5 × 0,5 = 0,25. Raiz quadrada de número negativo não existe entre os números reais, pois nenhum número real ao quadrado dá negativo.

Simplificar um radical é tirar de dentro da raiz os fatores que formam quadrados perfeitos. Para √72, procure o maior quadrado que divide 72, que é 36: √72 = √(36 × 2) = 6√2. Radicais só se somam quando são semelhantes, isto é, têm o mesmo índice e o mesmo número dentro. Por isso 3√2 + 5√2 = 8√2, como “3 sacos mais 5 sacos”, enquanto √2 + √3 não se junta. Quando os radicais não parecem semelhantes, simplifique antes: √8 = 2√2, e então √8 + √2 = 3√2.

Há uma armadilha clássica: a raiz de uma soma não é a soma das raízes. √(9 + 16) = √25 = 5, e não 3 + 4 = 7. A regra de distribuição vale para produto e quociente, nunca para soma e subtração.

A raiz também pode ser escrita como expoente fracionário: a<sup>1/2</sup> = √a e a<sup>m/n</sup> é a raiz de índice n de a<sup>m</sup>. Assim, 8<sup>2/3</sup> = (∛8)<sup>2</sup> = 2<sup>2</sup> = 4. Por fim, quando a raiz aparece no denominador, é costume tirá-la de lá, multiplicando em cima e embaixo por ela: 1/√2 = √2/2.

Exemplo resolvido. Quanto vale √(1/4) + √0,09? A raiz de 1/4 é 1/2 = 0,5, e a raiz de 0,09 é 0,3, porque 0,3 × 0,3 = 0,09. A soma é 0,5 + 0,3 = 0,8, ou 4/5.

## 7. Expressões numéricas e a ordem das operações

Quando uma expressão mistura operações, a ordem decide o resultado, e a convenção é a mesma em todo o mundo. Primeiro, potenciação e radiciação. Depois, multiplicação e divisão, na ordem em que aparecem, da esquerda para a direita. Por último, adição e subtração, também da esquerda para a direita. Os sinais de agrupamento mandam em tudo: resolve-se primeiro o que está entre parênteses ( ), depois colchetes [ ], depois chaves { }, sempre de dentro para fora.

O erro mais comum é achar que multiplicação vem sempre antes da divisão, ou soma antes de subtração. Na verdade, são operações de mesmo nível e valem na ordem de leitura. Em 8 ÷ 2 × 4, divide-se primeiro e multiplica-se depois: 4 × 4 = 16, e não 8 ÷ 8 = 1.

Exemplo resolvido 1. Calcule 2 + 3 × (4 − 1)<sup>2</sup> ÷ 9. O parêntese vale 3; elevado ao quadrado, 9. A expressão fica 2 + 3 × 9 ÷ 9. Multiplicando e dividindo da esquerda para a direita, 3 × 9 = 27 e 27 ÷ 9 = 3. Resta 2 + 3 = 5.

Exemplo resolvido 2. Calcule 1/2 + 2/3 ÷ 4/9. A divisão vem antes da soma: 2/3 ÷ 4/9 = 2/3 × 9/4 = 18/12 = 3/2. Agora, 1/2 + 3/2 = 4/2 = 2.

Exemplo resolvido 3, com decimais e potência. Calcule 0,5 × (1,2 + 0,8)<sup>2</sup> − 0,25. O parêntese vale 2,0 e, ao quadrado, 4. Então 0,5 × 4 = 2, e 2 − 0,25 = 1,75.

## 8. Questões resolvidas

### Questão 1

O valor de 5/6 − 1/4 + 1/3 é

- (A) 7/13
- (B) 1/12
- (C) 11/12
- (D) 3/4
- (E) 5/12

**Resposta: C.** MMC de 6, 4 e 3 é 12. 5/6 = 10/12, 1/4 = 3/12 e 1/3 = 4/12. A conta é (10 − 3 + 4)/12 = 11/12.

### Questão 2

Uma garrafa térmica de 2,5 litros enche copos de 0,25 litro. O número de copos que ela enche é

- (A) 1
- (B) 8
- (C) 25
- (D) 12,5
- (E) 10

**Resposta: E.** Divisão: 2,5 ÷ 0,25. Multiplicando os dois por 100, fica 250 ÷ 25 = 10 copos.

### Questão 3

A fração geratriz da dízima 0,8333... é

- (A) 5/6
- (B) 11/15
- (C) 83/100
- (D) 8/9
- (E) 4/5

**Resposta: B.** Antiperíodo 8, período 3. Numerador: 83 − 8 = 75. Denominador: 90. A fração é 75/90, que simplificada por 15 dá 5/6.

### Questão 4

O valor da expressão 2<sup>−1</sup> + (−3)<sup>2</sup> ÷ 6 é

- (A) 2
- (B) 9/2
- (C) 1/2
- (D) 3
- (E) 1

**Resposta: A.** Potências primeiro: 2<sup>−1</sup> = 1/2 e (−3)<sup>2</sup> = 9. Depois a divisão: 9 ÷ 6 = 3/2. Por fim, a soma: 1/2 + 3/2 = 2.

## 9. Na rotina do guarda

- **Combustível da viatura:** o painel mostra o tanque em frações. Se a ronda gastou 3/8 do tanque e o tanque tem 48 litros, foram 3/8 × 48 = 18 litros.
- **Distâncias no relatório:** o hodômetro marca decimais. Ao registrar que a viatura saiu com 45.230,4 km e voltou com 45.261,9 km, o trecho percorrido é 31,5 km.
- **Escala e horas:** 2 h 45 min é 2 3/4 h, ou 2,75 h. Converter bem evita erro na soma de horas de patrulhamento.
- **Rateio de material:** dividir 7,5 litros de água entre 5 guardas é 7,5 ÷ 5 = 1,5 litro cada.
- **Efetivo por turno:** “2/3 do efetivo em serviço” só vira número de guardas depois de multiplicar a fração pelo efetivo.

## 10. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Somar 1/2 + 1/3 e achar 2/5 | Denominador comum primeiro: 3/6 + 2/6 = 5/6 |
| Dividir fração sem inverter | Conserva a primeira, inverta a segunda, multiplique |
| Trocar 0,1212... por 0,12 | Dízima periódica não é decimal finito: 0,1212... = 4/33 |
| Achar que −3<sup>2</sup> vale 9 | Sem parênteses o sinal fica de fora: −3<sup>2</sup> = −9 |
| √(9 + 16) = 3 + 4 | Raiz de soma não se distribui: √25 = 5 |
| 8 ÷ 2 × 4 = 1 | Mesmo nível, da esquerda para a direita: 16 |
| Esquecer a vírgula no produto de decimais | Conte as casas dos dois fatores juntas |
| Resposta numa forma diferente das alternativas | Converta tudo para fração ou tudo para decimal antes de comparar |

## 11. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Somar e subtrair frações | MMC, depois numeradores; o denominador não se soma |
| Multiplicar frações | Numerador com numerador, denominador com denominador; “de” é vezes |
| Dividir frações | Conserva a primeira, inverte a segunda, multiplica |
| Decimais: soma e subtração | Alinhar a vírgula |
| Decimais: multiplicação | Multiplica como inteiros; soma as casas |
| Decimais: divisão | Multiplicar os dois por 10, 100... até o divisor ficar inteiro |
| Geratriz | Período sobre 9s; antiperíodo acrescenta 0s e subtrai |
| Potência | a<sup>0</sup> = 1; a<sup>−n</sup> = 1/a<sup>n</sup>; expoente par torna positivo |
| Raiz | Distribui no produto e no quociente, não na soma |
| Ordem | Potência e raiz, depois × ÷, depois + −; parênteses mandam |
