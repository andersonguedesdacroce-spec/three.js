import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
import math
from functools import reduce
mdc=lambda *a: reduce(math.gcd,a); mmc=lambda *a: reduce(lambda x,y:x*y//math.gcd(x,y),a)
LEAD="MMC e MDC são as duas ferramentas para problemas de repetição e de divisão em partes iguais. O MMC responde quando duas coisas que se repetem em ritmos diferentes voltam a coincidir; o MDC responde qual é o maior pedaço, ou o maior grupo, que reparte tudo sem sobra. A Vunesp quase nunca pede o cálculo seco: pede a situação (rondas que se cruzam, material a repartir em kits, número que deixa resto) e espera que você reconheça qual das duas ferramentas usar. Esta aula ensina o cálculo e, principalmente, o reconhecimento."
S={}
S[1]="""## 1. Múltiplos, divisores e números primos

Múltiplos de um número são os resultados da sua tabuada: os múltiplos de 6 são 0, 6, 12, 18, 24 e assim sem fim. Divisores de um número são os que o dividem sem deixar resto: os divisores de 12 são 1, 2, 3, 4, 6 e 12. Múltiplo e divisor são dois lados da mesma relação: se 12 é múltiplo de 4, então 4 é divisor de 12.

Número primo é o que tem exatamente dois divisores, o 1 e ele mesmo: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. O 2 é o único primo par, e o 1 não é primo, porque tem um só divisor. Os demais números, de dois divisores para cima, são os compostos, e todo composto pode ser escrito, de uma única maneira, como produto de primos. Esse é o teorema da fatoração, e é a chave de tudo nesta aula.

Para fatorar, divida o número pelo menor primo possível, de novo e de novo, até chegar a 1. Fatorando 60: 60 ÷ 2 = 30, 30 ÷ 2 = 15, 15 ÷ 3 = 5, 5 ÷ 5 = 1. Logo 60 = 2<sup>2</sup> × 3 × 5. Os critérios de divisibilidade aceleram o trabalho. Um número é divisível por 2 se termina em algarismo par; por 3 se a soma dos algarismos é múltipla de 3; por 4 se os dois últimos algarismos formam número divisível por 4; por 5 se termina em 0 ou 5; por 6 se é divisível por 2 e por 3; por 9 se a soma dos algarismos é múltipla de 9; por 10 se termina em 0. O número 4.527 tem soma 4 + 5 + 2 + 7 = 18, então é divisível por 9.

A fatoração também conta divisores. Some 1 a cada expoente e multiplique os resultados. Em 60 = 2<sup>2</sup> × 3<sup>1</sup> × 5<sup>1</sup>, o número de divisores é (2 + 1)(1 + 1)(1 + 1) = 12. A razão é que cada divisor escolhe, para cada primo, um expoente de zero até o expoente máximo.
"""
S[2]="""## 2. MDC: o maior pedaço que cabe exato

O máximo divisor comum de dois ou mais números é o maior número que divide todos eles. Imagine duas cordas, de 84 m e de 126 m, que devem ser cortadas em pedaços iguais, sem sobrar nada, e com pedaços os maiores possíveis. O tamanho do pedaço precisa dividir 84 e dividir 126; o maior que faz isso é o MDC, que aqui vale 42 m. Sai 2 pedaços da primeira corda e 3 da segunda.

Há dois métodos. No primeiro, decompõem-se os números em fatores primos e multiplicam-se apenas os fatores comuns, cada um com o menor expoente. Com 84 = 2<sup>2</sup> × 3 × 7 e 126 = 2 × 3<sup>2</sup> × 7, os comuns são 2 (menor expoente 1), 3 (menor expoente 1) e 7 (expoente 1). O MDC é 2 × 3 × 7 = 42.

O segundo método é o algoritmo de Euclides, útil com números grandes. Divide-se o maior pelo menor; depois, o divisor pelo resto, e assim por diante, até o resto zero. O último divisor é o MDC. Para 252 e 420: 420 = 1 × 252 + 168; 252 = 1 × 168 + 84; 168 = 2 × 84 + 0. O MDC é 84.

Dois números cujo MDC é 1 são chamados primos entre si, mesmo que cada um não seja primo: 8 e 15 não têm fator comum. O MDC também simplifica frações até a forma irredutível: 252/420 tem MDC 84, e dividindo em cima e embaixo por 84, vem 3/5.

[[NOTA: Para o MDC, pegue só os fatores comuns e o menor expoente. Para o MMC, pegue todos os fatores e o maior expoente. Se confundir, o MDC nunca ultrapassa o menor dos números, e o MMC nunca é menor que o maior deles.]]
"""
S[3]="""## 3. MMC: quando os ritmos voltam a coincidir

O mínimo múltiplo comum de dois ou mais números é o menor número, diferente de zero, que é múltiplo de todos eles. A imagem útil é a de dois sinais que repetem em ritmos diferentes. Um apita a cada 4 minutos e o outro a cada 6. Apitaram juntos agora; quando apitarão juntos de novo? O primeiro apita nos minutos 4, 8, 12, 16...; o segundo, nos minutos 6, 12, 18... O primeiro minuto comum é o 12, que é o MMC de 4 e 6.

Pela fatoração, o MMC é o produto de todos os fatores primos, comuns e não comuns, cada um com o maior expoente. Para 12, 18 e 30, tem-se 12 = 2<sup>2</sup> × 3, 18 = 2 × 3<sup>2</sup> e 30 = 2 × 3 × 5. O maior expoente do 2 é 2, o do 3 é 2 e o do 5 é 1. O MMC é 2<sup>2</sup> × 3<sup>2</sup> × 5 = 180.

Há um jeito prático, a decomposição simultânea. Escrevem-se os números lado a lado e divide-se por primos, dividindo apenas os que forem divisíveis e repetindo os demais; o MMC é o produto dos divisores usados. Em 12, 18, 30: por 2, vira 6, 9, 15; por 2, vira 3, 9, 15; por 3, vira 1, 3, 5; por 3, vira 1, 1, 5; por 5, vira 1, 1, 1. O produto 2 × 2 × 3 × 3 × 5 é 180.

Quando os números são primos entre si, o MMC é o produto deles: MMC(3, 5) = 15. Quando um é múltiplo do outro, o MMC é o maior: MMC(5, 10) = 10.
"""
S[4]="""## 4. A relação entre MMC e MDC

Para dois números a e b, vale que MDC(a, b) × MMC(a, b) = a × b. A razão está na fatoração: de cada primo, o MDC leva o menor expoente e o MMC leva o maior, e juntos usam os dois expoentes, que é exatamente o que o produto a × b faz. Com 12 e 18: MDC = 6, MMC = 36, e 6 × 36 = 216 = 12 × 18.

A relação resolve um tipo clássico de questão: dados o MDC, o MMC e um dos números, achar o outro. Se o MDC de dois números é 6, o MMC é 60 e um deles é 12, o outro é 6 × 60 ÷ 12 = 30. Também mostra que o MDC divide o MMC e que o MMC é múltiplo de ambos. A relação vale para dois números; com três ou mais, não vale.
"""
S[5]="""## 5. Como reconhecer o problema

A dificuldade da prova está em saber qual ferramenta usar. O texto da questão costuma dar o sinal.

Use o MDC quando o enunciado fala em dividir, repartir, cortar ou agrupar em partes iguais, sem sobra, e pede o maior tamanho ou o maior número de grupos. As palavras são “o maior possível”, “o maior número de equipes”, “pedaços iguais”, “sem sobrar”.

Use o MMC quando o enunciado fala em eventos que se repetem e voltam a coincidir, ou em achar o menor número que seja múltiplo de vários. As palavras são “de quanto em quanto tempo”, “novamente juntos”, “o menor número”, “pela primeira vez”.

Exemplo resolvido 1, com MDC. Uma equipe tem 72 coletes e 108 lanternas, que serão distribuídos em kits iguais, sem sobras. Qual o maior número de kits? Como a repartição é em partes iguais e se quer o maior número de kits, é MDC(72, 108). Fatorando, 72 = 2<sup>3</sup> × 3<sup>2</sup> e 108 = 2<sup>2</sup> × 3<sup>3</sup>. O MDC é 2<sup>2</sup> × 3<sup>2</sup> = 36 kits, cada um com 2 coletes e 3 lanternas.

Exemplo resolvido 2, com MMC. Duas viaturas passam por um cruzamento, uma a cada 10 minutos e outra a cada 15. Passaram juntas às 8h. Quando passam juntas de novo? Como os ritmos voltam a coincidir, é MMC(10, 15) = 30. Passam juntas de novo às 8h30.

Exemplo resolvido 3, com resto. Qual o menor número natural maior que 1 que, dividido por 4, por 6 e por 9, deixa sempre resto 1? Se sobra 1 em cada divisão, então o número menos 1 é múltiplo de 4, de 6 e de 9. O menor múltiplo comum é MMC(4, 6, 9) = 36. O número procurado é 36 + 1 = 37. Conferindo: 37 = 4 × 9 + 1 = 6 × 6 + 1 = 9 × 4 + 1.

Exemplo resolvido 4, com MMC em contagem. Três ônibus saem às 6h de um terminal, com intervalos de 15, 20 e 24 minutos. Quantas vezes saem juntos entre 6h e 18h, contando a saída das 6h? O MMC(15, 20, 24) = 120 minutos, ou 2 horas. Em 12 horas cabem 6 intervalos de 2 horas, e as saídas coincidentes acontecem às 6h, 8h, 10h, 12h, 14h, 16h e 18h. São 7 vezes.
"""
S[7]="""## 7. Na rotina do guarda

- **Cruzamento de rondas:** duas equipes com voltas de 20 e 30 minutos se reencontram a cada MMC(20, 30) = 60 minutos. Saber disso ajuda a marcar o momento da troca de informações.
- **Montagem de kits:** 48 cones e 60 coletes viram, no máximo, MDC(48, 60) = 12 kits iguais.
- **Escala de folgas:** quem folga a cada 4 dias e quem folga a cada 6 só têm folga juntos a cada MMC(4, 6) = 12 dias.
- **Fiscalizações periódicas:** inspeções a cada 15 e a cada 21 dias coincidem a cada 105 dias, que é o MMC.
- **Fila de identificação:** 36 homens e 48 mulheres podem formar, no máximo, MDC(36, 48) = 12 grupos com a mesma composição.
"""
S[8]="""## 8. Onde a Vunesp pega

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
"""
S[9]="""## 9. Quadro-resumo

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
"""
assert mdc(84,126)==42 and mmc(4,6)==12 and mmc(12,18,30)==180 and mdc(252,420)==84 and 252//84==3 and 420//84==5
assert mdc(72,108)==36 and mmc(10,15)==30 and mmc(4,6,9)+1==37 and mmc(15,20,24)==120
assert 6*60//12==30 and 12*18==math.gcd(12,18)*mmc(12,18)
assert (2+1)*(1+1)*(1+1)==12 and sum(map(int,'4527'))==18 and mdc(48,60)==12 and mmc(20,30)==60 and mmc(15,21)==105
# ---------- questões resolvidas ----------
QR=[("Questão 1","Duas luzes de sinalização piscam, uma a cada 8 segundos e outra a cada 12 segundos. Piscaram juntas num instante inicial. Piscarão juntas novamente depois de",["24 segundos.","4 segundos.","20 segundos.","48 segundos.","96 segundos."],0,"Coincidência de ritmos pede MMC. 8 = 2<sup>3</sup> e 12 = 2<sup>2</sup> × 3, então MMC = 2<sup>3</sup> × 3 = 24 segundos."),
("Questão 2","Um posto tem 90 coletes e 150 lanternas, que serão distribuídos em kits idênticos, sem sobras, com o maior número possível de kits. Cada kit terá",["3 coletes e 5 lanternas.","9 coletes e 15 lanternas.","1 colete e 5 lanternas.","30 coletes e 50 lanternas.","6 coletes e 10 lanternas."],0,"Partes iguais e o maior número de kits: MDC(90, 150) = 30 (90 = 2 × 3<sup>2</sup> × 5; 150 = 2 × 3 × 5<sup>2</sup>; comuns 2 × 3 × 5). Com 30 kits, cada um recebe 90 ÷ 30 = 3 coletes e 150 ÷ 30 = 5 lanternas."),
("Questão 3","O menor número natural que, dividido por 6, por 8 e por 10, deixa sempre resto 4 é",["124","120","244","64","84"],0,"O número menos 4 é múltiplo de 6, 8 e 10. MMC(6, 8, 10) = 120. O número é 120 + 4 = 124. Confira: 124 = 6 × 20 + 4 = 8 × 15 + 4 = 10 × 12 + 4."),
("Questão 4","O produto de dois números naturais é 1.296 e o MDC deles é 6. O MMC desses números é",["216","1.290","7.776","162","432"],0,"MDC × MMC = produto. MMC = 1.296 ÷ 6 = 216.")]
# posições da resposta correta: 3, 1, 4, 2
def reposicao(it,pos):
    t,e,a,_,c=it; return (t,e,a,pos,c)
QR=[reposicao(QR[0],3),reposicao(QR[1],1),reposicao(QR[2],4),reposicao(QR[3],2)]
assert mmc(8,12)==24 and mdc(90,150)==30 and 90//30==3 and 150//30==5 and mmc(6,8,10)+4==124 and 1296//6==216
QRF=qr_md(QR,6)
# ---------- textos de apoio ----------
t1="<strong>Escala de rondas do Parque Linear</strong><br><br>Três equipes da Guarda Municipal fazem rondas circulares no Parque Linear, partindo juntas do portão principal às 22h. A equipe A completa uma volta a cada 12 minutos; a equipe B, a cada 18 minutos; e a equipe C, a cada 30 minutos. Sempre que duas ou mais equipes passam juntas pelo portão, aproveitam para trocar informações."
t2="<strong>Distribuição de material</strong><br><br>A Secretaria de Segurança recebeu 72 coletes, 108 lanternas e 144 apitos. O material será distribuído em kits idênticos, sem sobra de nenhum item, com o maior número possível de kits."
tx={"mt2a":t1,"mt2b":t2}
assert mmc(12,18)==36 and mmc(12,18,30)==180 and 180//36==5 and (180//12,180//18,180//30)==(15,10,6)
assert mdc(72,108,144)==36 and (72//36,108//36,144//36)==(2,3,4) and mdc(72,108,180)==36 and 180//36==5
# ---------- banco ----------
# n=1
q(1,"O máximo divisor comum de 12 e 18 é",[str(mdc(12,18)),"3","2","36","1"],"12 = 2<sup>2</sup> × 3 e 18 = 2 × 3<sup>2</sup>. Comuns: 2 e 3, com menor expoente. MDC = 6.")
q(1,"O mínimo múltiplo comum de 4 e 6 é",[str(mmc(4,6)),"2","24","10","6"],"Múltiplos de 4: 4, 8, 12. Múltiplos de 6: 6, 12. O menor comum é 12.")
q(1,"Entre os números abaixo, o único que é primo é",["29","27","33","39","51"],"27 = 3<sup>3</sup>; 33 = 3 × 11; 39 = 3 × 13; 51 = 3 × 17. Só o 29 tem exatamente dois divisores.")
q(1,"A decomposição de 60 em fatores primos é",["2<sup>2</sup> × 3 × 5","2 × 3 × 10","4 × 15","2 × 30","2<sup>3</sup> × 3 × 5"],"60 ÷ 2 = 30; 30 ÷ 2 = 15; 15 ÷ 3 = 5; 5 ÷ 5 = 1. Logo 60 = 2<sup>2</sup> × 3 × 5.")
q(1,"O número de divisores positivos de 12 é",["6","4","5","12","3"],"Divisores: 1, 2, 3, 4, 6 e 12. Pela fatoração 2<sup>2</sup> × 3: (2 + 1)(1 + 1) = 6.")
q(1,"O mínimo múltiplo comum de 5 e 10 é",["10","5","15","50","2"],"10 já é múltiplo de 5. O MMC de um número e do seu múltiplo é o maior deles.")
q(1,"Os números 8 e 15 são primos entre si porque",["o MDC entre eles é 1.","ambos são primos.","o MMC entre eles é 1.","ambos são ímpares.","ambos são múltiplos de 1 e de 3."],"Primos entre si são os que não têm fator comum além do 1. 8 = 2<sup>3</sup> e 15 = 3 × 5, e o MDC é 1. O 8 e o 15 não são primos.")
q(1,"Entre os números abaixo, o divisível por 9 é",["4.527","4.526","4.525","4.528","4.529"],"Soma dos algarismos de 4.527: 4 + 5 + 2 + 7 = 18, múltiplo de 9.")
q(1,"Entre 20 e 40, a quantidade de múltiplos de 7 é",["3","2","4","5","6"],"21, 28 e 35.")
q(1,"O mínimo múltiplo comum de 3 e 5 é",["15","8","2","1","30"],"Primos entre si: o MMC é o produto, 3 × 5 = 15.")
q(1,"O máximo divisor comum de 24 e 36 é",["12","6","24","72","4"],"24 = 2<sup>3</sup> × 3 e 36 = 2<sup>2</sup> × 3<sup>2</sup>. Comuns, menor expoente: 2<sup>2</sup> × 3 = 12.")
q(1,"O mínimo múltiplo comum de 6 e 8 é",["24","48","2","14","12"],"6 = 2 × 3 e 8 = 2<sup>3</sup>. Maiores expoentes: 2<sup>3</sup> × 3 = 24.")
q(1,"O máximo divisor comum de 18 e 27 é",["9","3","54","6","18"],"18 = 2 × 3<sup>2</sup> e 27 = 3<sup>3</sup>. Comum: 3<sup>2</sup> = 9.")
q(1,"A decomposição de 84 em fatores primos é",["2<sup>2</sup> × 3 × 7","2 × 3 × 14","2<sup>3</sup> × 3 × 7","4 × 21","2 × 42"],"84 ÷ 2 = 42; 42 ÷ 2 = 21; 21 ÷ 3 = 7. Logo 84 = 2<sup>2</sup> × 3 × 7.")
q(1,"O mínimo múltiplo comum de 2, 3 e 4 é",["12","24","9","6","4"],"2 = 2; 3 = 3; 4 = 2<sup>2</sup>. Maiores expoentes: 2<sup>2</sup> × 3 = 12.")
q(1,"Um guarda passa por um ponto a cada 10 minutos e outro a cada 15 minutos. Passaram juntos às 8h. Passarão juntos novamente às",["8h30","8h25","8h10","9h","8h50"],"MMC(10, 15) = 30 minutos. 8h + 30 min = 8h30.")
q(1,"Uma equipe tem 20 cones e 30 coletes para montar kits iguais, sem sobra, com o maior número possível de kits. O número de kits é",["10","5","2","60","15"],"Partes iguais, o maior possível: MDC(20, 30) = 10 kits.")
q(1,"O número de divisores positivos de 7 é",["2","1","3","7","0"],"7 é primo: tem só o 1 e o 7.")
q(1,"De acordo com o texto, as equipes A e B passam juntas pelo portão pela primeira vez, depois da saída, após",[str(mmc(12,18))+" minutos.","6 minutos.","30 minutos.","18 minutos.","216 minutos."],"MMC(12, 18) = 36 minutos.","mt2a")
q(1,"De acordo com o texto, o maior número possível de kits idênticos, sem sobras, é",[str(mdc(72,108,144)),"12","18","24","72"],"MDC(72, 108, 144): 72 = 2<sup>3</sup> × 3<sup>2</sup>, 108 = 2<sup>2</sup> × 3<sup>3</sup>, 144 = 2<sup>4</sup> × 3<sup>2</sup>. Comuns, menor expoente: 2<sup>2</sup> × 3<sup>2</sup> = 36.","mt2b")
# n=2
q(2,"O mínimo múltiplo comum de 12, 15 e 20 é",[str(mmc(12,15,20)),"30","120","180","20"],"12 = 2<sup>2</sup> × 3; 15 = 3 × 5; 20 = 2<sup>2</sup> × 5. Maiores expoentes: 2<sup>2</sup> × 3 × 5 = 60.")
q(2,"O máximo divisor comum de 48, 72 e 120 é",[str(mdc(48,72,120)),"12","8","6","48"],"48 = 2<sup>4</sup> × 3; 72 = 2<sup>3</sup> × 3<sup>2</sup>; 120 = 2<sup>3</sup> × 3 × 5. Comuns, menor expoente: 2<sup>3</sup> × 3 = 24.")
q(2,"O MDC de dois números é 6 e o MMC é 60. Se um deles é 12, o outro é",["30","20","10","36","5"],"MDC × MMC = produto. 6 × 60 = 360, e 360 ÷ 12 = 30.")
q(2,"O menor número natural, maior que 1, que dividido por 4, por 6 e por 9 deixa sempre resto 1 é",[str(mmc(4,6,9)+1),"36","35","73","13"],"O número menos 1 é múltiplo de 4, 6 e 9: MMC = 36. O número é 37.")
q(2,"O maior número que divide 90 e 126 sem deixar resto é",[str(mdc(90,126)),"9","6","3","36"],"90 = 2 × 3<sup>2</sup> × 5 e 126 = 2 × 3<sup>2</sup> × 7. MDC = 2 × 3<sup>2</sup> = 18.")
q(2,"O número de divisores positivos de 72 é",["12","9","8","6","24"],"72 = 2<sup>3</sup> × 3<sup>2</sup>. (3 + 1)(2 + 1) = 12.")
q(2,"O menor número natural, diferente de zero, divisível por 2, 3, 4, 5 e 6 é",["60","30","120","12","360"],"Maiores expoentes: 2<sup>2</sup> (do 4), 3, 5. 4 × 3 × 5 = 60.")
q(2,"O menor número natural diferente de zero que é, ao mesmo tempo, múltiplo de 12 e de 18 e um quadrado perfeito é",["36","216","72","144","18"],"MMC(12, 18) = 36 = 6<sup>2</sup>, já é quadrado perfeito.")
q(2,"Um piso retangular de 3,6 m por 4,8 m será coberto com ladrilhos quadrados, todos iguais e inteiros, sem cortes e com o maior lado possível. O lado do ladrilho, em centímetros, é",[str(mdc(360,480)),"60","30","240","12"],"MDC(360, 480): 360 = 2<sup>3</sup> × 3<sup>2</sup> × 5 e 480 = 2<sup>5</sup> × 3 × 5. Comuns: 2<sup>3</sup> × 3 × 5 = 120.")
q(2,"Dois relógios tocam, um a cada 45 minutos e outro a cada 60 minutos. Tocaram juntos às 6h. Tocarão juntos novamente às",["9h","7h","8h","10h","12h"],"MMC(45, 60) = 180 minutos = 3 horas. 6h + 3h = 9h.")
q(2,"Três lâmpadas piscam, a primeira a cada 4 s, a segunda a cada 6 s e a terceira a cada 10 s. Se piscaram juntas num instante, voltarão a piscar juntas depois de",["60 s.","20 s.","30 s.","120 s.","24 s."],"MMC(4, 6, 10): 4 = 2<sup>2</sup>, 6 = 2 × 3, 10 = 2 × 5. Resultado 2<sup>2</sup> × 3 × 5 = 60 s.")
q(2,"O valor de 2<sup>3</sup> × 3 × 5<sup>2</sup> é",["600","120","360","300","150"],"8 × 3 = 24 e 24 × 25 = 600.")
q(2,"O número de divisores positivos de 100 é",["9","4","6","10","25"],"100 = 2<sup>2</sup> × 5<sup>2</sup>. (2 + 1)(2 + 1) = 9.")
q(2,"O máximo divisor comum de 150 e 225 é",["75","25","15","50","45"],"150 = 2 × 3 × 5<sup>2</sup> e 225 = 3<sup>2</sup> × 5<sup>2</sup>. Comuns: 3 × 5<sup>2</sup> = 75.")
q(2,"O menor número de pessoas com o qual se podem formar grupos de 6, de 8 ou de 10 pessoas, sem sobra em qualquer caso, é",[str(mmc(6,8,10)),"24","60","240","30"],"MMC(6, 8, 10): 2<sup>3</sup> × 3 × 5 = 120.")
q(2,"O MDC entre 2<sup>3</sup> × 3<sup>2</sup> × 5 e 2<sup>2</sup> × 3<sup>3</sup> × 7 é",["2<sup>2</sup> × 3<sup>2</sup>","2<sup>3</sup> × 3<sup>3</sup>","2<sup>2</sup> × 3<sup>3</sup> × 5 × 7","2 × 3","2<sup>3</sup> × 3<sup>2</sup> × 5 × 7"],"No MDC, só fatores comuns, com menor expoente: 2<sup>2</sup> × 3<sup>2</sup> = 36.")
q(2,"O MMC entre 2<sup>3</sup> × 3<sup>2</sup> × 5 e 2<sup>2</sup> × 3<sup>3</sup> × 7 é",["7.560","36","2.520","3.780","15.120"],"No MMC, todos os fatores com maior expoente: 2<sup>3</sup> × 3<sup>3</sup> × 5 × 7 = 8 × 27 × 35 = 7.560.")
q(2,"Depois da saída às 22h, as equipes A, B e C do texto passam juntas pelo portão pela primeira vez às",["1h.","22h36.","23h.","23h30.","0h."],"MMC(12, 18, 30) = 180 minutos = 3 horas. 22h + 3h = 1h.","mt2a")
q(2,"Considerando o texto, entre a saída das 22h e as 1h, incluindo as 1h, o número de vezes em que as equipes A e B passam juntas pelo portão é",["5","4","6","3","15"],"A e B coincidem a cada 36 minutos: aos 36, 72, 108, 144 e 180 minutos. São 5 passagens conjuntas.","mt2a")
q(2,"Segundo o texto, cada kit idêntico terá",["2 coletes, 3 lanternas e 4 apitos.","3 coletes, 2 lanternas e 4 apitos.","4 coletes, 6 lanternas e 8 apitos.","1 colete, 3 lanternas e 4 apitos.","36 coletes, 36 lanternas e 36 apitos."],"São 36 kits: 72 ÷ 36 = 2; 108 ÷ 36 = 3; 144 ÷ 36 = 4.","mt2b")
# n=3
q(3,"O MDC de dois números é 12 e o MMC é 180. Se um deles é 36, o outro é",["60","45","90","30","15"],"MDC × MMC = produto: 12 × 180 = 2.160. 2.160 ÷ 36 = 60.")
q(3,"O menor número natural que, dividido por 6, por 8 e por 12, deixa sempre resto 5 é",[str(mmc(6,8,12)+5),"24","19","53","47"],"O número menos 5 é múltiplo comum: MMC(6, 8, 12) = 24. O número é 24 + 5 = 29.")
q(3,"O menor número natural que, dividido por 5, por 6 e por 7, deixa sempre resto 3 é",[str(mmc(5,6,7)+3),"210","207","423","63"],"5, 6 e 7 não têm fatores em comum dois a dois, então MMC(5, 6, 7) = 5 × 6 × 7 = 210. O número é 210 + 3 = 213.")
q(3,"O maior número que, dividindo 200 e 250, deixa resto 8 e 10, respectivamente, é",[str(mdc(192,240)),"24","16","12","50"],"Se sobra 8 em 200, o divisor divide 192. Se sobra 10 em 250, divide 240. MDC(192, 240) = 48. Como 48 é maior que os restos 8 e 10, serve.")
q(3,"O menor número natural pelo qual se deve multiplicar 12 para obter um quadrado perfeito é",["3","2","4","6","12"],"12 = 2<sup>2</sup> × 3. Falta um fator 3 para o expoente do 3 ficar par. 12 × 3 = 36 = 6<sup>2</sup>.")
q(3,"O menor número natural pelo qual se deve multiplicar 90 para obter um cubo perfeito é",["300","30","900","10","60"],"90 = 2 × 3<sup>2</sup> × 5. Para ser cubo, todos os expoentes devem ser múltiplos de 3. Faltam 2<sup>2</sup>, 3 e 5<sup>2</sup>: 4 × 3 × 25 = 300, e 90 × 300 = 27.000 = 30<sup>3</sup>.")
q(3,"Entre os divisores positivos de 360, o número dos que são ímpares é",["6","12","24","3","9"],"360 = 2<sup>3</sup> × 3<sup>2</sup> × 5. Divisores ímpares não levam o fator 2: (2 + 1)(1 + 1) = 6.")
q(3,"O produto de dois números naturais é 1.296 e o MDC deles é 6. Então o MMC é",["216","1.290","7.776","162","432"],"MMC = produto ÷ MDC = 1.296 ÷ 6 = 216.")
q(3,"Três ônibus saem às 6h de um terminal, com intervalos de 15, 20 e 24 minutos. Contando a saída das 6h, o número de vezes em que saem juntos até as 18h, inclusive, é",["7","6","8","12","5"],"MMC(15, 20, 24) = 120 minutos. Em 12 horas (720 minutos) há 6 intervalos, e com a saída inicial são 7 vezes.")
q(3,"Duas engrenagens têm 18 e 30 dentes e giram acopladas. Partindo da posição em que dois dentes marcados estão em contato, elas voltam a essa posição quando a primeira tiver dado",["5 voltas e a segunda, 3.","3 voltas e a segunda, 5.","15 voltas e a segunda, 9.","9 voltas e a segunda, 15.","30 voltas e a segunda, 18."],"MMC(18, 30) = 90 dentes passados. Primeira: 90 ÷ 18 = 5 voltas. Segunda: 90 ÷ 30 = 3 voltas.")
q(3,"Três cordas de 84 m, 126 m e 210 m serão cortadas em pedaços iguais, os maiores possíveis, sem sobra. O número total de pedaços é",["10","7","21","5","42"],"MDC(84, 126, 210) = 42 m. Pedaços: 84 ÷ 42 = 2, 126 ÷ 42 = 3, 210 ÷ 42 = 5. Total 10.")
q(3,"A forma irredutível da fração 252/420 é",["3/5","126/210","6/10","9/15","21/35"],"MDC(252, 420) = 84. 252 ÷ 84 = 3 e 420 ÷ 84 = 5. As demais são equivalentes, porém não irredutíveis.")
q(3,"O menor número natural que, dividido por 12, por 15 e por 20, deixa resto 7 em todos os casos é",[str(mmc(12,15,20)+7),"60","53","127","47"],"MMC(12, 15, 20) = 60. O número é 60 + 7 = 67.")
q(3,"Entre 1 e 100, inclusive, o número de múltiplos comuns de 6 e de 8 é",["4","3","8","12","16"],"São os múltiplos de MMC(6, 8) = 24: 24, 48, 72 e 96.")
q(3,"O valor de 1/12 + 1/18 + 1/30 é",["31/180","3/60","1/20","1/10","3/180"],"MMC(12, 18, 30) = 180. 15/180 + 10/180 + 6/180 = 31/180.")
q(3,"O número de divisores positivos de 2<sup>4</sup> × 3<sup>2</sup> × 5 é",["30","11","15","24","45"],"(4 + 1)(2 + 1)(1 + 1) = 5 × 3 × 2 = 30.")
q(3,"O MDC de dois números naturais é 15 e o MMC é 210. Se um deles é 30, o outro é",["105","70","90","210","45"],"MDC × MMC = produto: 15 × 210 = 3.150. 3.150 ÷ 30 = 105.")
q(3,"Assinale a afirmação INCORRETA.",["O MDC de dois números naturais pode ser maior que o MMC deles.","O MMC de dois números é divisível por cada um deles.","O MDC de dois números primos entre si é 1.","O MMC de um número e do seu dobro é o dobro desse número.","O produto do MDC pelo MMC de dois números é igual ao produto dos dois números."],"O MDC nunca é maior que o MMC: o MDC divide o MMC. Todas as demais afirmações são verdadeiras.")
q(3,"No texto, quando as três equipes passam juntas pelo portão pela primeira vez, as equipes A, B e C terão completado, respectivamente,",["15, 10 e 6 voltas.","6, 10 e 15 voltas.","12, 18 e 30 voltas.","15, 9 e 6 voltas.","30, 20 e 12 voltas."],"Passam juntas aos 180 minutos. A: 180 ÷ 12 = 15. B: 180 ÷ 18 = 10. C: 180 ÷ 30 = 6.","mt2a")
q(3,"Se a Secretaria do texto recebesse 180 apitos, em vez de 144, e mantivesse os 72 coletes e as 108 lanternas, montando de novo o maior número possível de kits idênticos, sem sobras, cada kit teria",["5 apitos.","4 apitos.","3 apitos.","6 apitos.","2 apitos."],"MDC(72, 108, 180) = 36, pois 180 = 2<sup>2</sup> × 3<sup>2</sup> × 5 mantém os fatores comuns 2<sup>2</sup> × 3<sup>2</sup>. São 36 kits, com 180 ÷ 36 = 5 apitos cada.","mt2b")
# conferências
assert mdc(18,27)==9 and mmc(2,3,4)==12 and mdc(20,30)==10 and mmc(12,15,20)==60 and mdc(48,72,120)==24
assert mdc(90,126)==18 and mmc(2,3,4,5,6)==60 and mdc(360,480)==120 and mmc(45,60)==180 and mmc(4,6,10)==60
assert 2**3*3*5**2==600 and mdc(150,225)==75 and mdc(2**3*3**2*5,2**2*3**3*7)==36 and mmc(2**3*3**2*5,2**2*3**3*7)==7560
assert 2160//36==60 and mmc(6,8,12)+5==29 and mmc(5,6,7)+3==213 and mdc(192,240)==48 and 12*3==36 and 90*300==30**3
assert sum(1 for d in range(1,361) if 360%d==0 and d%2==1)==6 and mdc(84,126,210)==42 and 84//42+126//42+210//42==10
assert sum(1 for k in range(1,101) if k%6==0 and k%8==0)==4 and Fr(1,12)+Fr(1,18)+Fr(1,30)==Fr(31,180)
assert sum(1 for d in range(1,73) if 72%d==0)==12 and sum(1 for d in range(1,101) if 100%d==0)==9 and sum(1 for d in range(1,2**4*9*5+1) if 720%d==0)==30
assert 15*210//30==105
assert 720//120==6 and mmc(18,30)//18==5 and mmc(18,30)//30==3 and mmc(15,20,24)==120
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("MMC e MDC: duas perguntas diferentes",[
 ("primos","Primos e fatoração",["2, 3, 5, 7, 11, 13...","divide pelo menor primo","divisores: expoente + 1"],"seção 1"),
 ("mdc","MDC",["fatores comuns","menor expoente","partes iguais, maior possível"],"seção 2"),
 ("mmc","MMC",["todos os fatores","maior expoente","ritmos que coincidem"],"seção 3"),
 ("rel","Relação",["MDC × MMC = a × b","só para dois números","dado um, acha o outro"],"seção 4"),
 ("quando","Qual usar",["dividir, repartir, cortar: MDC","novamente juntos: MMC","resto r: MMC + r"],"seção 5"),
 ("euclides","Euclides",["divide maior pelo menor","repete com o resto","último divisor = MDC"],"seção 2")],
 "Na prova: ache a palavra-chave (“maior possível” é MDC; “novamente juntos” é MMC)")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"A caixa “Qual usar” é o centro da aula: as demais ensinam o cálculo que ela manda fazer.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.")
revisao("mt-2","Mínimo múltiplo comum e máximo divisor comum",QQ,list(tx),
 cobertura=["Recorte do edital: “situações-problema” com MMC e MDC. Cobertos: múltiplos, divisores, primos, fatoração, critérios de divisibilidade, contagem de divisores, MDC (fatoração e Euclides), MMC (fatoração e decomposição simultânea), relação MDC × MMC, problemas de partes iguais, coincidência, resto constante e frações irredutíveis."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","Gabaritos e exemplos conferidos por código (math.gcd e contagens por força bruta); a redação dos enunciados continua para revisão humana."],
 fontes_conferidas=["Cálculos: assert no script conteudo/mt2/mt2.py."])
gravar("mt-2",aula_html,banco("mt-2",QQ),tx)
print(len(aula_html))
