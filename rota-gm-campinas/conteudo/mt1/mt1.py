import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
import math
LEAD="Operações com números racionais é a base de todo o resto da prova de Matemática: porcentagem, regra de três, equação e média dependem de somar, multiplicar e dividir frações e decimais sem errar. A Vunesp cobra quatro coisas: operar com frações, operar com decimais, passar de um formato ao outro (inclusive a dízima periódica) e resolver expressões que misturam tudo isso, com potência e raiz, na ordem certa. Esta aula parte da ideia de cada operação e só depois chega à regra."
S={}
S[1]="""## 1. O que é um número racional

Número racional é todo número que pode ser escrito como fração a/b, com a e b inteiros e b diferente de zero. Cabem aí os inteiros (5 = 5/1), os decimais finitos (0,75 = 3/4) e as dízimas periódicas (0,333... = 1/3). Fora dos racionais ficam, por exemplo, a raiz de 2 e o pi, que não têm representação como fração.

A melhor maneira de pensar numa fração é como uma divisão que ainda não foi feita. A fração 3/4 é “3 dividido por 4”: três barras de chocolate repartidas entre quatro pessoas dão 0,75 de barra para cada uma. O denominador diz em quantas partes iguais o inteiro foi cortado; o numerador diz quantas dessas partes entram na conta. Por isso o denominador não pode ser zero: ninguém corta uma barra em zero pedaços.

Duas frações podem ter escrita diferente e valer o mesmo. Multiplicar ou dividir numerador e denominador pelo mesmo número não muda o valor, porque é o mesmo que multiplicar por 1 (2/2 = 1). Assim, 1/2 = 2/4 = 50/100. Simplificar uma fração é fazer esse caminho de volta, dividindo em cima e embaixo pelo maior divisor comum, até a fração ficar irredutível: 18/24 = 3/4. Quando o numerador é maior que o denominador, a fração é imprópria e pode virar número misto: 7/3 = 2 inteiros e 1/3, escrito 2 1/3. Para voltar, multiplica-se o inteiro pelo denominador e soma-se o numerador: 2 1/3 = (2 × 3 + 1)/3 = 7/3.

Para comparar duas frações, leve-as ao mesmo denominador e compare os numeradores. Qual é maior, 5/8 ou 7/12? O menor múltiplo comum de 8 e 12 é 24. Então 5/8 = 15/24 e 7/12 = 14/24. Como 15 é maior que 14, 5/8 é maior. Conferindo em decimal: 5/8 = 0,625 e 7/12 = 0,583.
"""
S[2]="""## 2. Somar e subtrair frações

Somar frações é como somar pedaços: só faz sentido juntar pedaços do mesmo tamanho. Três quartos de pizza mais dois terços de pizza não dão “cinco quartos-e-terços” de nada. Antes de somar, é preciso cortar tudo em pedaços do mesmo tamanho, e isso é achar o denominador comum. O mais enxuto é o menor múltiplo comum (MMC) dos denominadores.

O caminho tem quatro passos: achar o MMC; transformar cada fração em outra equivalente com esse denominador; somar ou subtrair só os numeradores, mantendo o denominador; simplificar o resultado. Quando não se quer calcular o MMC, vale o atalho geral a/b + c/d = (a × d + b × c) / (b × d), que funciona sempre, mas pode exigir simplificação no fim.

Exemplo resolvido. Quanto vale 2/3 + 3/4 − 1/6? O MMC de 3, 4 e 6 é 12. Então 2/3 = 8/12, 3/4 = 9/12 e 1/6 = 2/12. A conta fica (8 + 9 − 2)/12 = 15/12. Dividindo em cima e embaixo por 3, vem 5/4, que é o mesmo que 1 1/4.

Com números mistos há dois caminhos. O primeiro transforma tudo em fração imprópria: 2 1/2 + 1 2/3 = 5/2 + 5/3 = 15/6 + 10/6 = 25/6 = 4 1/6. O segundo soma separadamente a parte inteira e a fracionária: 2 + 1 = 3 e 1/2 + 2/3 = 3/6 + 4/6 = 7/6 = 1 1/6; no total, 3 + 1 1/6 = 4 1/6. Na subtração com misto, o primeiro caminho costuma ser mais seguro. Para calcular 5 − 1 3/4, escreva 5 = 20/4 e 1 3/4 = 7/4; a diferença é 13/4 = 3 1/4.

[[NOTA: Nunca some denominadores. 1/2 + 1/3 não é 2/5. O denominador diz o tamanho do pedaço e não muda quando os pedaços já são iguais: 1/5 + 2/5 = 3/5, porque um quinto e mais dois quintos são três quintos.]]
"""
S[3]="""## 3. Multiplicar e dividir frações

Multiplicar frações é pegar uma parte de uma parte. A metade de um terço de barra é um sexto de barra: 1/2 × 1/3 = 1/6. Por isso a palavra “de” na matemática quer dizer multiplicação. A regra sai daí: multiplica-se numerador por numerador e denominador por denominador. Antes de multiplicar vale simplificar em cruz, cortando um fator do numerador de uma fração com um fator do denominador da outra: 3/4 × 8/9 = (3 × 8)/(4 × 9), e como 3 cabe em 9 três vezes e 4 cabe em 8 duas vezes, sobra 1 × 2 sobre 1 × 3, ou seja, 2/3.

Dividir é perguntar quantas vezes um valor cabe em outro. Quantas meias-barras cabem em 3 barras? Cabem 6, porque cada barra tem duas metades: 3 ÷ 1/2 = 6. A regra é conservar a primeira fração, inverter a segunda e multiplicar: a/b ÷ c/d = a/b × d/c. A inversão faz sentido porque dividir por 1/2 é multiplicar por 2, e dividir por 3/4 é multiplicar por 4/3, que é quanto precisa para completar um inteiro.

Exemplo resolvido 1. Quantas garrafas de 3/4 de litro se enchem com 9 litros de água? A pergunta é “quantas vezes 3/4 cabe em 9”, então 9 ÷ 3/4 = 9 × 4/3 = 36/3 = 12 garrafas. Confira: 12 garrafas de 0,75 litro dão 9 litros.

Exemplo resolvido 2. Do efetivo de 120 guardas, 2/3 estão de serviço e, destes, 3/8 patrulham a pé. Quantos patrulham a pé? Primeiro, 2/3 de 120 são 120 × 2/3 = 80 guardas de serviço. Depois, 3/8 de 80 são 80 × 3/8 = 30 guardas a pé. De uma vez só: 2/3 × 3/8 = 6/24 = 1/4, e 1/4 de 120 é 30.

Quando a fração aparece sobre outra fração, a barra grande também é uma divisão. Em (1/2)/(3/4), faz-se 1/2 ÷ 3/4 = 1/2 × 4/3 = 4/6 = 2/3.
"""
S[4]="""## 4. Decimais e dízimas periódicas

Um número decimal é uma fração cujo denominador é 10, 100, 1000 e assim por diante: 0,7 = 7/10; 0,07 = 7/100; 2,35 = 235/100. A vírgula separa os inteiros dos décimos, centésimos e milésimos, e é essa organização que dita as regras das operações.

Na soma e na subtração, alinhe a vírgula. É a mesma ideia do denominador comum: décimos só se somam com décimos, centésimos com centésimos. Para calcular 2,4 + 0,75, escreva 2,40 + 0,75 = 3,15. Para 5 − 1,35, escreva 5,00 − 1,35 = 3,65.

Na multiplicação, ignore as vírgulas, multiplique como se fossem inteiros e depois dê ao resultado tantas casas decimais quantas têm os dois fatores juntos. Em 0,12 × 0,3, faz-se 12 × 3 = 36, e como há duas casas num fator e uma no outro, o resultado tem três: 0,036. A razão é que 0,12 é 12/100 e 0,3 é 3/10; o produto é 36/1000.

Na divisão, multiplique dividendo e divisor pela mesma potência de 10 até o divisor virar inteiro. Isso não muda o resultado, porque é multiplicar a fração por 1. Em 7,5 ÷ 0,25, multiplicando os dois por 100 vem 750 ÷ 25 = 30. Multiplicar um decimal por 10, 100 ou 1000 é andar com a vírgula para a direita; dividir é andar para a esquerda.

Para passar de fração a decimal, divida o numerador pelo denominador: 3/4 = 3 ÷ 4 = 0,75. Para passar de decimal a fração, escreva sobre 10, 100 ou 1000 e simplifique: 0,375 = 375/1000 = 3/8.

Há frações cuja divisão nunca termina: 1/3 = 0,333... e 4/33 = 0,1212... São as dízimas periódicas, e o trecho que se repete é o período. Elas também são números racionais, e a fração que as origina é a geratriz. O método da geratriz usa a ideia de que multiplicar por 10 desloca a vírgula e permite subtrair a parte infinita. Para x = 0,333..., tem-se 10x = 3,333..., e subtraindo, 9x = 3, logo x = 1/3.

Na prática, há uma regra pronta. Na dízima periódica simples, o numerador é o período e o denominador tem tantos noves quanto os algarismos do período: 0,1212... = 12/99 = 4/33. Na dízima composta (há uma parte que não se repete, o antiperíodo), o numerador é o número formado pelo antiperíodo seguido do período, menos o antiperíodo, e o denominador tem tantos noves quanto os algarismos do período, seguidos de tantos zeros quanto os do antiperíodo. Para 0,2333..., o antiperíodo é 2 e o período é 3: numerador 23 − 2 = 21 e denominador 90, ou seja, 21/90 = 7/30. Se há parte inteira, ela entra à parte: 1,2333... = 1 + 7/30 = 37/30.
"""
S[5]="""## 5. Potenciação

Potência é multiplicação repetida: 2<sup>5</sup> = 2 × 2 × 2 × 2 × 2 = 32. A base é o número que se repete e o expoente diz quantas vezes. Em 2<sup>5</sup>, a base é 2 e o expoente é 5.

As propriedades decorrem dessa contagem de fatores. Ao multiplicar potências de mesma base, somam-se os expoentes: 2<sup>3</sup> × 2<sup>2</sup> = 2<sup>5</sup>, pois são três fatores mais dois fatores. Ao dividir, subtraem-se: 2<sup>5</sup> ÷ 2<sup>2</sup> = 2<sup>3</sup>. Potência de potência multiplica os expoentes: (2<sup>3</sup>)<sup>2</sup> = 2<sup>6</sup>. O expoente também se distribui sobre produto e quociente: (2 × 3)<sup>2</sup> = 2<sup>2</sup> × 3<sup>2</sup> = 36. Mas não se distribui sobre soma: (2 + 3)<sup>2</sup> = 25, e não 2<sup>2</sup> + 3<sup>2</sup> = 13.

O expoente zero e o expoente negativo parecem regras decoradas, mas saem de uma escadinha. Cada vez que o expoente diminui uma unidade, o resultado é dividido pela base: 2<sup>3</sup> = 8, 2<sup>2</sup> = 4, 2<sup>1</sup> = 2, 2<sup>0</sup> = 1, 2<sup>−1</sup> = 1/2, 2<sup>−2</sup> = 1/4. Daí vêm as duas regras: todo número diferente de zero elevado a zero vale 1, e expoente negativo inverte a base, a<sup>−n</sup> = 1/a<sup>n</sup>. Em fração, inverte-se a fração: (1/2)<sup>−3</sup> = 2<sup>3</sup> = 8.

O sinal pede atenção. Base negativa com expoente par dá resultado positivo, porque os sinais negativos se anulam aos pares: (−3)<sup>2</sup> = 9. Com expoente ímpar, o resultado é negativo: (−2)<sup>3</sup> = −8. Sem parênteses, o expoente pega só o número: −3<sup>2</sup> = −(3<sup>2</sup>) = −9. Potência de fração eleva numerador e denominador: (2/3)<sup>2</sup> = 4/9.

Exemplo resolvido. Quanto vale 2<sup>5</sup> × 2<sup>−2</sup> ÷ 2<sup>2</sup>? Todos têm base 2, então basta operar os expoentes: 5 − 2 − 2 = 1. O resultado é 2<sup>1</sup> = 2.
"""
S[6]="""## 6. Radiciação

A raiz é a operação inversa da potência. Perguntar “quanto é a raiz quadrada de 49?” é perguntar “que número elevado ao quadrado dá 49?”. A resposta é 7, porque 7<sup>2</sup> = 49. Do mesmo modo, a raiz cúbica de 27 é 3, porque 3<sup>3</sup> = 27. O número do índice diz que potência se desfaz; quando o índice é 2, ele costuma ficar oculto.

Algumas regras bastam para a prova. A raiz de um produto é o produto das raízes, e o mesmo vale para o quociente: √(a × b) = √a × √b e √(a/b) = √a / √b. Então √(9/16) = 3/4, e √0,25 = 0,5, porque 0,5 × 0,5 = 0,25. Raiz quadrada de número negativo não existe entre os números reais, pois nenhum número real ao quadrado dá negativo.

Simplificar um radical é tirar de dentro da raiz os fatores que formam quadrados perfeitos. Para √72, procure o maior quadrado que divide 72, que é 36: √72 = √(36 × 2) = 6√2. Radicais só se somam quando são semelhantes, isto é, têm o mesmo índice e o mesmo número dentro. Por isso 3√2 + 5√2 = 8√2, como “3 sacos mais 5 sacos”, enquanto √2 + √3 não se junta. Quando os radicais não parecem semelhantes, simplifique antes: √8 = 2√2, e então √8 + √2 = 3√2.

Há uma armadilha clássica: a raiz de uma soma não é a soma das raízes. √(9 + 16) = √25 = 5, e não 3 + 4 = 7. A regra de distribuição vale para produto e quociente, nunca para soma e subtração.

A raiz também pode ser escrita como expoente fracionário: a<sup>1/2</sup> = √a e a<sup>m/n</sup> é a raiz de índice n de a<sup>m</sup>. Assim, 8<sup>2/3</sup> = (∛8)<sup>2</sup> = 2<sup>2</sup> = 4. Por fim, quando a raiz aparece no denominador, é costume tirá-la de lá, multiplicando em cima e embaixo por ela: 1/√2 = √2/2.

Exemplo resolvido. Quanto vale √(1/4) + √0,09? A raiz de 1/4 é 1/2 = 0,5, e a raiz de 0,09 é 0,3, porque 0,3 × 0,3 = 0,09. A soma é 0,5 + 0,3 = 0,8, ou 4/5.
"""
S[7]="""## 7. Expressões numéricas e a ordem das operações

Quando uma expressão mistura operações, a ordem decide o resultado, e a convenção é a mesma em todo o mundo. Primeiro, potenciação e radiciação. Depois, multiplicação e divisão, na ordem em que aparecem, da esquerda para a direita. Por último, adição e subtração, também da esquerda para a direita. Os sinais de agrupamento mandam em tudo: resolve-se primeiro o que está entre parênteses ( ), depois colchetes [ ], depois chaves { }, sempre de dentro para fora.

O erro mais comum é achar que multiplicação vem sempre antes da divisão, ou soma antes de subtração. Na verdade, são operações de mesmo nível e valem na ordem de leitura. Em 8 ÷ 2 × 4, divide-se primeiro e multiplica-se depois: 4 × 4 = 16, e não 8 ÷ 8 = 1.

Exemplo resolvido 1. Calcule 2 + 3 × (4 − 1)<sup>2</sup> ÷ 9. O parêntese vale 3; elevado ao quadrado, 9. A expressão fica 2 + 3 × 9 ÷ 9. Multiplicando e dividindo da esquerda para a direita, 3 × 9 = 27 e 27 ÷ 9 = 3. Resta 2 + 3 = 5.

Exemplo resolvido 2. Calcule 1/2 + 2/3 ÷ 4/9. A divisão vem antes da soma: 2/3 ÷ 4/9 = 2/3 × 9/4 = 18/12 = 3/2. Agora, 1/2 + 3/2 = 4/2 = 2.

Exemplo resolvido 3, com decimais e potência. Calcule 0,5 × (1,2 + 0,8)<sup>2</sup> − 0,25. O parêntese vale 2,0 e, ao quadrado, 4. Então 0,5 × 4 = 2, e 2 − 0,25 = 1,75.
"""
S[9]="""## 9. Na rotina do guarda

- **Combustível da viatura:** o painel mostra o tanque em frações. Se a ronda gastou 3/8 do tanque e o tanque tem 48 litros, foram 3/8 × 48 = 18 litros.
- **Distâncias no relatório:** o hodômetro marca decimais. Ao registrar que a viatura saiu com 45.230,4 km e voltou com 45.261,9 km, o trecho percorrido é 31,5 km.
- **Escala e horas:** 2 h 45 min é 2 3/4 h, ou 2,75 h. Converter bem evita erro na soma de horas de patrulhamento.
- **Rateio de material:** dividir 7,5 litros de água entre 5 guardas é 7,5 ÷ 5 = 1,5 litro cada.
- **Efetivo por turno:** “2/3 do efetivo em serviço” só vira número de guardas depois de multiplicar a fração pelo efetivo.
"""
S[10]="""## 10. Onde a Vunesp pega

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
"""
S[11]="""## 11. Quadro-resumo

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
"""
# conferências do texto
assert Fr(2,3)+Fr(3,4)-Fr(1,6)==Fr(5,4); assert Fr(5,2)+Fr(5,3)==Fr(25,6); assert 5-Fr(7,4)==Fr(13,4)
assert 9/Fr(3,4)==12; assert Fr(2,3)*Fr(3,8)*120==30; assert Fr(1,2)/Fr(3,4)==Fr(2,3)
assert Fr('7.5')/Fr('0.25')==30; assert Fr('0.375')==Fr(3,8); assert Fr(12,99)==Fr(4,33); assert 1+Fr(21,90)==Fr(37,30)
assert Fr(2)**5*Fr(2)**-2/Fr(2)**2==2; assert Fr(1,2)**-3==8; assert 8**Fr(2,3)==4 if False else round(8**(2/3))==4
assert math.isclose(math.sqrt(72),6*math.sqrt(2)); assert Fr(1,2)+Fr('0.3')==Fr(4,5)
assert 2+3*(4-1)**2/9==5; assert Fr(1,2)+Fr(2,3)/Fr(4,9)==2; assert Fr('0.5')*(Fr('1.2')+Fr('0.8'))**2-Fr('0.25')==Fr('1.75')
assert Fr(3,8)*48==18 and Fr('45261.9')-Fr('45230.4')==Fr('31.5') and Fr('7.5')/5==Fr('1.5')

QR=[("Questão 1","O valor de 5/6 − 1/4 + 1/3 é",["11/12","7/13","1/12","3/4","5/12"],2,"MMC de 6, 4 e 3 é 12. 5/6 = 10/12, 1/4 = 3/12 e 1/3 = 4/12. A conta é (10 − 3 + 4)/12 = 11/12."),
("Questão 2","Uma garrafa térmica de 2,5 litros enche copos de 0,25 litro. O número de copos que ela enche é",["10","1","8","25","12,5"],4,"Divisão: 2,5 ÷ 0,25. Multiplicando os dois por 100, fica 250 ÷ 25 = 10 copos."),
("Questão 3","A fração geratriz da dízima 0,8333... é",["11/15","5/6","83/100","8/9","4/5"],1,"Antiperíodo 8, período 3. Numerador: 83 − 8 = 75. Denominador: 90. A fração é 75/90, que simplificada por 15 dá 5/6."),
("Questão 4","O valor da expressão 2<sup>−1</sup> + (−3)<sup>2</sup> ÷ 6 é",["2","9/2","1/2","3","1"],0,"Potências primeiro: 2<sup>−1</sup> = 1/2 e (−3)<sup>2</sup> = 9. Depois a divisão: 9 ÷ 6 = 3/2. Por fim, a soma: 1/2 + 3/2 = 2.")]
assert Fr(5,6)-Fr(1,4)+Fr(1,3)==Fr(11,12); assert Fr('2.5')/Fr('0.25')==10; assert Fr(75,90)==Fr(5,6)
assert Fr(1,2)+Fr(9,6)==2 and Fr(1,2)==Fr(2)**-1
QRF=qr_md(QR,8)

# ---------- textos de apoio ----------
t1="<strong>Guarda renova frota e reduz gasto com combustível</strong><br><br>A Guarda Municipal de Vila Nova, cidade fictícia, recebeu 12 viaturas novas. O tanque de cada uma comporta 50 litros. Em abril, uma delas gastou 3/5 do tanque na primeira semana e 1/4 do tanque na segunda. O litro do combustível custou R$ 6,40 no período. A Guarda informou ainda que, com a nova frota, a economia mensal estimada é de 0,15 do gasto anterior, que era de R$ 20.000,00."
t2="<strong>Relatório de ronda</strong><br><br>Na manhã de terça-feira, a equipe 3 da Guarda Municipal percorreu 18,6 km em ronda preventiva pelos parques da região norte. À tarde, percorreu 2/3 da distância feita pela manhã, em trajeto pelas escolas do bairro. A viatura saiu da base às 7h e retornou às 12h, na ronda da manhã."
tx={"mt1a":t1,"mt1b":t2}
# gabaritos conferidos
g1=Fr(3,5)+Fr(1,4); assert g1==Fr(17,20); assert Fr(3,5)*50==30; assert g1*50==Fr('42.5'); assert Fr('42.5')*Fr('6.4')==272
assert 20000-Fr('0.15')*20000==17000; assert (1-g1)*50==Fr('7.5')
assert Fr(2,3)*Fr('18.6')==Fr('12.4'); assert Fr('18.6')+Fr('12.4')==31; assert Fr(31,5)==Fr('6.2')

# ---------- banco ----------
# n=1 (fáceis)
q(1,"Uma viatura gastou 1/2 do tanque pela manhã e 1/3 do tanque à tarde. Ao todo, gastou",[s(Fr(1,2)+Fr(1,3)),"2/5","1/6","2/3","3/5"],"MMC de 2 e 3 é 6: 3/6 + 2/6 = 5/6. Não se somam os denominadores.")
q(1,"O resultado de 3/4 − 1/6 é",[s(Fr(3,4)-Fr(1,6)),"2/2","1/2","5/12","1/5"],"MMC 12: 9/12 − 2/12 = 7/12.")
q(1,"O produto 2/5 × 3/4 é igual a",[s(Fr(2,5)*Fr(3,4)),"5/9","6/9","1/2","8/15"],"Numerador com numerador, denominador com denominador: 6/20 = 3/10.")
q(1,"O resultado de 3 ÷ 1/2 é",["6","3/2","1/6","2/3","1,5"],"Dividir por 1/2 é multiplicar por 2: 3 × 2 = 6.")
q(1,"O valor de 3/5 de 40 é",["24","8","16","25","120"],"40 ÷ 5 = 8, e 8 × 3 = 24.")
q(1,"A soma 2,4 + 0,75 é igual a",[dc(Fr('2.4')+Fr('0.75')),"2,79","3,0","3,05","2,115"],"Alinhando a vírgula: 2,40 + 0,75 = 3,15.")
q(1,"O resultado de 5 − 1,35 é",[dc(5-Fr('1.35')),"4,35","3,75","4,65","3,35"],"5,00 − 1,35 = 3,65.")
q(1,"O produto 0,3 × 0,2 é igual a",["0,06","0,6","0,5","0,006","0,05"],"3 × 2 = 6, e há duas casas decimais no total: 0,06.")
q(1,"O quociente de 7,2 ÷ 0,6 é",["12","1,2","0,12","120","1,12"],"Multiplicando os dois por 10: 72 ÷ 6 = 12.")
q(1,"A fração 3/4, escrita na forma decimal, é",["0,75","0,34","0,25","3,4","0,43"],"3 ÷ 4 = 0,75.")
q(1,"O número decimal 0,6, escrito como fração irredutível, é",["3/5","6/100","1/6","2/3","6/5"],"0,6 = 6/10 = 3/5.")
q(1,"O valor de 2<sup>5</sup> é",["32","10","25","64","16"],"2 × 2 × 2 × 2 × 2 = 32.")
q(1,"O valor de √81 é",["9","8","40,5","18","27"],"9 × 9 = 81.")
q(1,"O valor de (−3)<sup>2</sup> é",["9","−9","6","−6","1/9"],"Expoente par: os sinais negativos se anulam. (−3) × (−3) = 9.")
q(1,"O valor de 12 + 3 × 4 é",["24","60","15","48","144"],"A multiplicação vem antes: 3 × 4 = 12, e 12 + 12 = 24.")
q(1,"O número misto 4 1/2, escrito como fração imprópria, é",["9/2","5/2","4/2","8/2","41/2"],"(4 × 2 + 1)/2 = 9/2.")
q(1,"A fração 18/24, na forma irredutível, é",["3/4","9/12","6/8","2/3","1/2"],"Dividindo por 6 (maior divisor comum): 3/4. As frações 9/12 e 6/8 são equivalentes, mas não irredutíveis.")
q(1,"A fração de maior valor entre as listadas é",["3/4","2/3","5/8","1/2","3/5"],"Em decimais: 0,75; 0,667; 0,625; 0,5; 0,6. A maior é 3/4.")
# n=1 com texto de apoio t1
q(1,"De acordo com o texto, a fração do tanque que a viatura gastou nas duas semanas, somadas, foi",[s(g1),"4/9","3/10","1/2","4/5"],"3/5 + 1/4 = 12/20 + 5/20 = 17/20.","mt1a")
q(1,"Segundo o texto, na primeira semana a viatura gastou, em litros,",["30","25","20","15","12,5"],"3/5 de 50 = 50 ÷ 5 × 3 = 30 litros.","mt1a")
# n=2 (médias)
q(2,"O valor de 5/6 − 3/8 + 1/4 é",[s(Fr(5,6)-Fr(3,8)+Fr(1,4)),"3/18","1/2","7/12","3/4"],"MMC 24: 20/24 − 9/24 + 6/24 = 17/24.")
q(2,"A soma 2 1/3 + 1 3/4 é igual a",[misto(Fr(7,3)+Fr(7,4)),"3 4/7","3 1/12","4 1/7","4"],"7/3 + 7/4 = 28/12 + 21/12 = 49/12 = 4 1/12.")
q(2,"O valor da fração (2/3) / (4/9) é",["3/2","8/27","2/3","1/3","6"],"2/3 ÷ 4/9 = 2/3 × 9/4 = 18/12 = 3/2.")
q(2,"O valor de 3/4 de 2/5 de 200 é",["60","80","120","150","30"],"2/5 de 200 = 80; 3/4 de 80 = 60.")
q(2,"O valor de 0,25 × 1,2 ÷ 0,05 é",["6","0,6","60","0,06","1,5"],"0,25 × 1,2 = 0,3, e 0,3 ÷ 0,05 = 30 ÷ 5 = 6.")
q(2,"O valor de 0,333... + 1/6 é",["1/2","1/3","5/9","2/9","1/18"],"0,333... = 1/3. Então 1/3 + 1/6 = 2/6 + 1/6 = 1/2.")
q(2,"A fração geratriz da dízima 0,4545... é",["5/11","45/100","9/20","4/9","4/11"],"Período 45 sobre 99: 45/99 = 5/11 (dividindo por 9).")
q(2,"O valor de 2<sup>−3</sup> + 2<sup>−2</sup> é",["3/8","1/32","−5","1/5","1/2"],"2<sup>−3</sup> = 1/8 e 2<sup>−2</sup> = 1/4. Então 1/8 + 2/8 = 3/8.")
q(2,"O valor de (3<sup>4</sup> × 3<sup>−2</sup>) ÷ 3 é",["3","27","1/3","9","81"],"Somam-se e subtraem-se os expoentes: 4 − 2 − 1 = 1. Resultado 3<sup>1</sup> = 3.")
q(2,"O valor de √(49/64) é",["7/8","49/8","7/64","1/8","7/16"],"A raiz do quociente é o quociente das raízes: √49 / √64 = 7/8.")
q(2,"O radical √50, simplificado, é igual a",["5√2","25√2","2√5","10√5","5√10"],"50 = 25 × 2, e √25 = 5. Logo √50 = 5√2.")
q(2,"O valor de 10 − 2 × (3 + 1)<sup>2</sup> ÷ 8 é",["6","−2","16","1","−6"],"Parêntese: 4; ao quadrado, 16. Depois 2 × 16 ÷ 8 = 4. Por fim, 10 − 4 = 6.")
q(2,"O valor de 1/2 + 1/3 ÷ 1/6 é",["5/2","1","1/9","2/9","3"],"A divisão vem antes: 1/3 ÷ 1/6 = 1/3 × 6 = 2. Depois 1/2 + 2 = 5/2.")
q(2,"Do efetivo de 120 guardas, 2/3 estão de serviço e, destes, 3/8 patrulham a pé. O número de guardas que patrulham a pé é",["30","45","80","60","40"],"2/3 de 120 = 80; 3/8 de 80 = 30.")
q(2,"Com 9 litros de água, o número de garrafas de 3/4 de litro que se enchem é",["12","6","8","10","27/4"],"9 ÷ 3/4 = 9 × 4/3 = 12.")
q(2,"O valor de (0,1)<sup>2</sup> + 0,9 é",["0,91","1,0","0,19","0,29","1,9"],"(0,1)<sup>2</sup> = 0,01. Então 0,01 + 0,9 = 0,91.")
# n=2 com texto
q(2,"Considerando que o tanque estava cheio, o número de litros gastos nas duas semanas foi",[dc(g1*50),"40","45","42","35"],"17/20 de 50 = 50 × 17 ÷ 20 = 42,5 litros.","mt1a")
q(2,"Com o litro a R$ 6,40, o custo do combustível gasto nas duas semanas foi",[rs(Fr('42.5')*Fr('6.4')),"R$ 256,00","R$ 192,00","R$ 280,00","R$ 217,60"],"42,5 × 6,40 = 272,00.","mt1a")
q(2,"Após a economia estimada pela Guarda, o gasto mensal passa a ser de",[rs(17000),"R$ 3.000,00","R$ 19.985,00","R$ 15.000,00","R$ 18.500,00"],"Economia: 0,15 × 20.000 = 3.000. Novo gasto: 20.000 − 3.000 = 17.000.","mt1a")
q(2,"De acordo com o texto, a distância percorrida pela equipe à tarde foi, em km,",[dc(Fr(2,3)*Fr('18.6')),"9,3","12,6","13,2","28"],"2/3 de 18,6 = 18,6 ÷ 3 × 2 = 6,2 × 2 = 12,4.","mt1b")
# n=3 (difíceis)
q(3,"O valor do produto (1 − 1/2)(1 − 1/3)(1 − 1/4)(1 − 1/5) é",["1/5","1/120","1/2","24/120","4/5"],"Cada parêntese é 1/2, 2/3, 3/4 e 4/5. O produto cancela em sequência: 1/2 × 2/3 × 3/4 × 4/5 = 1/5.")
q(3,"O valor de 1 / (1/2 + 1/3) é",["6/5","5/6","2/5","1/5","5"],"1/2 + 1/3 = 5/6. O inverso de 5/6 é 6/5.")
q(3,"O valor de (3/4 + 1/2) ÷ (5/8 − 1/4) é",[s((Fr(3,4)+Fr(1,2))/(Fr(5,8)-Fr(1,4))),"15/32","3/10","2","5/3"],"3/4 + 1/2 = 5/4 e 5/8 − 1/4 = 3/8. Então 5/4 ÷ 3/8 = 5/4 × 8/3 = 40/12 = 10/3.")
q(3,"O valor de 0,1212... + 0,333... é",["5/11","15/45","1/2","0,4545","4/11"],"0,1212... = 12/99 = 4/33 e 0,333... = 1/3 = 11/33. A soma é 15/33 = 5/11.")
q(3,"A fração geratriz de 1,2333... é",["37/30","123/100","12/9","11/9","111/90"],"A parte inteira entra à parte. Em 0,2333..., antiperíodo 2 e período 3: (23 − 2)/90 = 21/90 = 7/30. Somando 1: 37/30.")
q(3,"O valor de (2<sup>−1</sup> + 3<sup>−1</sup>)<sup>−1</sup> é",["6/5","5/6","1/5","5","−5"],"2<sup>−1</sup> + 3<sup>−1</sup> = 1/2 + 1/3 = 5/6. O expoente −1 inverte: 6/5.")
q(3,"O valor de 5√2 + 3√8 − √18 é",["8√2","7√2","5√8","13√2","8√28"],"√8 = 2√2 e √18 = 3√2. Então 5√2 + 6√2 − 3√2 = 8√2.")
q(3,"O valor de √0,0144 é",["0,12","0,012","1,2","0,0012","0,144"],"0,12 × 0,12 = 0,0144.")
q(3,"O valor de 8<sup>2/3</sup> é",["4","16/3","2","64","8/3"],"8<sup>2/3</sup> = (raiz cúbica de 8)<sup>2</sup> = 2<sup>2</sup> = 4.")
q(3,"O valor de −2<sup>2</sup> + (−2)<sup>3</sup> − (−1)<sup>5</sup> é",["−11","−13","−9","5","−7"],"−2<sup>2</sup> = −4; (−2)<sup>3</sup> = −8; −(−1)<sup>5</sup> = −(−1) = +1. A soma é −4 − 8 + 1 = −11.")
q(3,"Assinale a igualdade que é verdadeira.",["√(9 × 16) = √9 × √16","√(9 + 16) = √9 + √16","(−2)<sup>2</sup> = −4","2<sup>−1</sup> = −2","(2 + 3)<sup>2</sup> = 2<sup>2</sup> + 3<sup>2</sup>"],"A raiz distribui no produto: 12 = 3 × 4. Nas outras: √25 = 5, não 7; (−2)<sup>2</sup> = 4; 2<sup>−1</sup> = 1/2; (2 + 3)<sup>2</sup> = 25, não 13.")
q(3,"O valor de (2<sup>7</sup> × 4<sup>2</sup>) ÷ 8<sup>3</sup> é",["4","1","2","8","16"],"Tudo na base 2: 2<sup>7</sup> × 2<sup>4</sup> ÷ 2<sup>9</sup> = 2<sup>7+4−9</sup> = 2<sup>2</sup> = 4.")
q(3,"O valor de (1/2 + 1/3) ÷ (1/2 − 1/3) é",["5","5/36","1","1/5","6"],"1/2 + 1/3 = 5/6 e 1/2 − 1/3 = 1/6. Então 5/6 ÷ 1/6 = 5.")
q(3,"Um tanque perdeu 1/3 do combustível na ida e, na volta, gastou 1/4 do que restava. A fração do tanque que sobrou foi",["1/2","5/12","7/12","1/6","2/3"],"Restou 2/3. Na volta gastou 1/4 de 2/3 = 1/6. Sobrou 2/3 − 1/6 = 4/6 − 1/6 = 3/6 = 1/2.")
q(3,"Uma fita de 7,2 m é cortada em pedaços de 0,45 m. O número de pedaços obtidos é",["16","15","14","18","1,6"],"7,2 ÷ 0,45 = 720 ÷ 45 = 16.")
q(3,"O valor da expressão 8 ÷ 2 × 4 − 3 é",["13","−2","1","−1","5"],"Divisão e multiplicação, da esquerda para a direita: 8 ÷ 2 = 4; 4 × 4 = 16. Depois 16 − 3 = 13.")
q(3,"Os números 0,65; 2/3; 5/8 e 0,6, em ordem crescente, ficam",["0,6; 5/8; 0,65; 2/3","5/8; 0,6; 0,65; 2/3","0,6; 0,65; 5/8; 2/3","2/3; 0,65; 5/8; 0,6","5/8; 0,6; 2/3; 0,65"],"Em decimais: 0,6; 0,625; 0,65; 0,667.")
q(3,"O valor de (√2)<sup>6</sup> é",["8","12","6","2√2","64"],"(√2)<sup>6</sup> = (2<sup>1/2</sup>)<sup>6</sup> = 2<sup>3</sup> = 8.")
# n=3 com texto
q(3,"Se o tanque estava cheio no início da primeira semana, ao final da segunda semana restavam no tanque, em litros,",[dc((1-g1)*50),"15","12,5","8","10"],"Sobrou 1 − 17/20 = 3/20 do tanque. 3/20 de 50 = 7,5 litros.","mt1a")
q(3,"Se o total percorrido pela equipe no dia, manhã e tarde, tivesse sido feito em 5 horas de deslocamento, a velocidade média seria, em km/h, de",[dc(Fr(31,5)),"3,72","7,44","6,0","18,6"],"Total: 18,6 + 12,4 = 31 km. Em 5 horas, 31 ÷ 5 = 6,2 km/h.","mt1b")

# conferências adicionais de gabarito
assert Fr(5,6)-Fr(3,8)+Fr(1,4)==Fr(17,24); assert Fr(7,3)+Fr(7,4)==Fr(49,12); assert Fr('0.25')*Fr('1.2')/Fr('0.05')==6
assert Fr(1,3)+Fr(1,6)==Fr(1,2); assert Fr(45,99)==Fr(5,11); assert Fr(1,8)+Fr(1,4)==Fr(3,8)
assert 10-Fr(2*16,8)==6; assert Fr(1,2)+Fr(1,3)/Fr(1,6)==Fr(5,2); assert Fr('0.01')+Fr('0.9')==Fr('0.91')
p=1
for k in (2,3,4,5): p*=1-Fr(1,k)
assert p==Fr(1,5); assert 1/(Fr(1,2)+Fr(1,3))==Fr(6,5); assert (Fr(3,4)+Fr(1,2))/(Fr(5,8)-Fr(1,4))==Fr(10,3)
assert Fr(4,33)+Fr(1,3)==Fr(5,11); assert (Fr(1,2)+Fr(1,3))/(Fr(1,2)-Fr(1,3))==5
assert -4-8+1==-11; assert (2**7*4**2)/8**3==4; assert Fr(2,3)-Fr(2,3)*Fr(1,4)==Fr(1,2); assert Fr('7.2')/Fr('0.45')==16
assert Fr('0.12')**2==Fr('0.0144'); assert 8//2*4-3==13
vals=[Fr('0.65'),Fr(2,3),Fr(5,8),Fr('0.6')]; assert sorted(vals)==[Fr('0.6'),Fr(5,8),Fr('0.65'),Fr(2,3)]
assert max([Fr(3,4),Fr(2,3),Fr(5,8),Fr(1,2),Fr(3,5)])==Fr(3,4)
# o gabarito 'misto' e dízimas escritas à mão acima
QQ=fechar()
assert len(QQ)==60, len(QQ)

code,svg=mapa("Seis ferramentas para operar com racionais",[
 ("fracao","Fração",["divisão ainda não feita","equivalentes e simplificação","comparar: mesmo denominador"],"seção 1"),
 ("soma","Somar e subtrair",["MMC dos denominadores","soma só os numeradores","mistos: imprópria ou separado"],"seção 2"),
 ("prod","Multiplicar e dividir",["“de” é vezes","dividir: inverte e multiplica","simplifique em cruz"],"seção 3"),
 ("dec","Decimais e dízimas",["alinhar a vírgula","contar casas no produto","geratriz: período sobre noves"],"seção 4"),
 ("pot","Potência e raiz",["a⁰ = 1; a⁻ⁿ = 1/aⁿ","raiz distribui no produto","raiz de soma não distribui"],"seções 5 e 6"),
 ("ordem","Ordem das operações",["potência e raiz primeiro","× e ÷ da esquerda para a direita","parênteses de dentro para fora"],"seção 7")],
 "Na prova: converta tudo para fração ou tudo para decimal antes de operar e confira o sinal")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7,'QR',9,10,11],QR,8,svg,"As quatro primeiras caixas são as operações; a quinta amplia o repertório com potência e raiz; a última diz em que ordem tudo se resolve.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1 e 2; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; todos os resultados foram recalculados em código.")
revisao("mt-1","Operações com números racionais",QQ,list(tx),
 cobertura=["Recorte do edital: “adição a radiciação, em forma fracionária ou decimal”. Cobertos: adição, subtração, multiplicação, divisão, potenciação (inclui expoente zero e negativo), radiciação, decimais, dízimas periódicas e geratriz, números mistos e ordem das operações.",
            "Não coberto de propósito: racionalização com binômios e raízes de índice maior que 3, por estarem acima do nível esperado para o cargo."],
 pendencias=["Referências bibliográficas (Iezzi et al.; Dante) citadas como base; não foram consultadas página a página nesta produção.",
             "Todos os cálculos da aula e os gabaritos foram verificados por código (módulo fractions do Python). A conferência humana do enunciado e da redação das alternativas continua valendo.",
             "A regra da geratriz da dízima composta foi explicada em prosa; vale ler com olho de aluno."],
 fontes_conferidas=["Gabaritos e exemplos: recalculados com Fraction/Decimal (assert no script conteudo/mt1/mt1.py)."])
gravar("mt-1",aula_html,banco("mt-1",QQ),tx)
print(len(aula_html))
