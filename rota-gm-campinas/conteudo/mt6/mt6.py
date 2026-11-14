import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
import math
LEAD="Equação é uma igualdade com um valor desconhecido, e resolvê-la é descobrir esse valor. A Vunesp cobra duas coisas: resolver equações do 1º e do 2º graus e, principalmente, montar a equação a partir de um problema escrito. A conta costuma ser curta; o trabalho difícil é traduzir o texto. Esta aula começa pela imagem da balança, passa à resolução passo a passo e dedica uma seção inteira à tradução do enunciado."
S={}
S[1]="""## 1. A equação como uma balança

Pense numa balança de dois pratos em equilíbrio. Num prato há uma caixa de peso desconhecido x mais 3 pesos de 1 kg; no outro, 10 pesos de 1 kg. A balança só continua equilibrada se, para qualquer coisa que se faça num prato, se faça a mesma coisa no outro. Tirando 3 kg de cada lado, resta x = 7. Essa é toda a técnica: aplicar a mesma operação nos dois lados para isolar a incógnita.

Na prática, a operação inversa isola o x. Se algo foi somado, subtrai-se; se foi multiplicado, divide-se. Em x + 3 = 10, subtrai-se 3: x = 7. Em 3x = 21, divide-se por 3: x = 7. Em x/4 = 6, multiplica-se por 4: x = 24. É o que se resume na frase “muda de lado, muda de sinal”: ela é só um atalho para somar ou subtrair o mesmo valor dos dois lados.
"""
S[2]="""## 2. Equação do 1º grau, passo a passo

A equação do 1º grau tem a forma ax + b = 0, com a diferente de zero, e uma única solução, x = −b/a. Quando a equação vem desarrumada, a ordem é sempre a mesma: eliminar parênteses, eliminar denominadores multiplicando tudo pelo MMC, juntar os termos com x de um lado e os números do outro, e dividir pelo coeficiente de x.

Exemplo resolvido 1. Resolva 3(x − 2) = 2x + 5. Eliminando os parênteses, 3x − 6 = 2x + 5. Passando 2x para a esquerda e −6 para a direita, 3x − 2x = 5 + 6, ou seja, x = 11. Conferindo: 3 × 9 = 27 e 2 × 11 + 5 = 27.

Exemplo resolvido 2, com frações. Resolva x/3 + x/2 = 10. O MMC de 3 e 2 é 6. Multiplicando tudo por 6, 2x + 3x = 60, então 5x = 60 e x = 12. Conferindo: 12/3 + 12/2 = 4 + 6 = 10.

Sempre vale substituir a resposta na equação original: é a conferência que a prova permite.
"""
S[3]="""## 3. Do texto à equação

Quase toda questão cobra a tradução. O método é escolher a incógnita, escrever o que o texto diz sobre ela e montar a igualdade. Algumas traduções aparecem o tempo todo: “o dobro de um número” é 2x; “o triplo” é 3x; “a metade” é x/2; “um número aumentado de 5” é x + 5; “a soma de dois números consecutivos” é x + (x + 1); “três números consecutivos” são x, x + 1 e x + 2; “a idade de Ana daqui a 5 anos” é x + 5; “há 3 anos” é x − 3; “é igual a” ou “resulta em” é o sinal de igual.

Exemplo resolvido 1. A soma de três números inteiros consecutivos é 72. Quais são eles? Sendo x o menor, o texto diz x + (x + 1) + (x + 2) = 72. Então 3x + 3 = 72, 3x = 69, x = 23. Os números são 23, 24 e 25.

Exemplo resolvido 2. Cinco coletes e um frete de R$ 30,00 custaram R$ 280,00. Qual o preço de cada colete? Com x o preço do colete, 5x + 30 = 280, então 5x = 250 e x = 50.

Exemplo resolvido 3. Em 50 moedas de 5 e de 10 centavos, que somam R$ 3,50, quantas são de 10 centavos? Seja a o número de moedas de 5 centavos. As de 10 centavos são 50 − a, e o valor em centavos fica 5a + 10(50 − a) = 350. Então 500 − 5a = 350, 5a = 150 e a = 30. As de 10 centavos são 50 − 30 = 20.
"""
S[4]="""## 4. Equação do 2º grau

A equação do 2º grau tem a forma ax<sup>2</sup> + bx + c = 0, com a diferente de zero, e pode ter duas soluções, uma ou nenhuma entre os reais. Os casos incompletos resolvem-se sem fórmula. Se falta o termo em x (b = 0), isola-se o quadrado: x<sup>2</sup> = 49 dá x = 7 ou x = −7, porque ambos ao quadrado dão 49. Se falta o termo independente (c = 0), coloca-se x em evidência: x<sup>2</sup> − 5x = 0 vira x(x − 5) = 0, e um produto é zero quando um dos fatores é zero, então x = 0 ou x = 5.

Para a equação completa, usa-se a fórmula de Bhaskara. Calcula-se o discriminante Δ = b<sup>2</sup> − 4ac, que diz quantas soluções existem: Δ positivo dá duas soluções reais diferentes; Δ igual a zero dá uma solução dupla; Δ negativo não dá solução real. As soluções são x = (−b ± √Δ) / (2a).

Exemplo resolvido. Resolva 2x<sup>2</sup> − 3x − 2 = 0. Aqui a = 2, b = −3 e c = −2. Δ = (−3)<sup>2</sup> − 4 × 2 × (−2) = 9 + 16 = 25 e √Δ = 5. Então x = (3 ± 5) / 4, ou seja, x = 8/4 = 2 e x = −2/4 = −1/2.

Há um caminho mais rápido em muitas questões, o da soma e produto das raízes. Se x<sub>1</sub> e x<sub>2</sub> são as raízes, então x<sub>1</sub> + x<sub>2</sub> = −b/a e x<sub>1</sub> × x<sub>2</sub> = c/a. Em x<sup>2</sup> − 7x + 12 = 0, a soma é 7 e o produto é 12, o que leva a 3 e 4, porque 3 + 4 = 7 e 3 × 4 = 12. Essas relações permitem dizer a soma ou o produto das raízes sem resolver a equação.

[[NOTA: Em problemas, nem toda raiz serve. Se a incógnita é uma idade, um comprimento ou um número de pessoas, a raiz negativa é descartada.]]
"""
S[6]="""## 6. Na rotina do guarda

- **Compras e orçamento:** valor unitário desconhecido, frete fixo e total conhecido formam uma equação do 1º grau, como a dos coletes.
- **Rateios:** dividir uma verba entre um número de guardas que muda leva a equações com fração, resolvidas ao multiplicar tudo pelo MMC.
- **Áreas de terrenos e salas:** lados que se relacionam por “3 m a mais” levam a equações do 2º grau.
- **Escalas e tempos:** distâncias e velocidades entre duas viaturas também levam a equações.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Errar o sinal ao mudar de lado | Subtraia ou some o mesmo valor dos dois lados |
| Esquecer de multiplicar todos os termos pelo MMC | Multiplique também os termos sem denominador |
| Aplicar Bhaskara com o sinal de b errado | Calcule −b com cuidado: se b = −3, −b = 3 |
| Dividir os dois lados por x e perder a raiz x = 0 | Coloque x em evidência em vez de dividir |
| Aceitar raiz negativa para comprimento ou idade | Descarte a raiz que não faz sentido |
| Traduzir mal “a mais que” e “vezes mais” | Escreva a relação em símbolos antes de calcular |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| 1º grau | Operação inversa dos dois lados; x = −b/a |
| Frações | Multiplicar tudo pelo MMC |
| Tradução | Defina a incógnita; “é” vira igual |
| 2º grau incompleto | b = 0: raiz quadrada; c = 0: x em evidência |
| Bhaskara | Δ = b² − 4ac; x = (−b ± √Δ) / 2a |
| Soma e produto | x₁ + x₂ = −b/a; x₁ × x₂ = c/a |
| Conferência | Substitua na equação original |
"""
assert 3*(11-2)==2*11+5 and Fr(12,3)+Fr(12,2)==10 and 23+24+25==72 and 5*50+30==280 and 5*30+10*20==350
assert (-3)**2-4*2*(-2)==25 and Fr(3+5,4)==2 and Fr(3-5,4)==Fr(-1,2) and 3+4==7 and 3*4==12
QR=[("Questão 1","A solução da equação 3(x − 2) = 2x + 5 é",["11","−1","7","3","1"],0,"3x − 6 = 2x + 5, então 3x − 2x = 5 + 6, x = 11."),
("Questão 2","As raízes da equação x<sup>2</sup> − 7x + 12 = 0 são",["3 e 4","−3 e −4","2 e 6","1 e 12","−3 e 4"],0,"Soma 7 e produto 12: 3 e 4."),
("Questão 3","A soma de três números inteiros consecutivos é 72. O menor deles é",["23","24","22","21","25"],0,"x + (x + 1) + (x + 2) = 72, 3x + 3 = 72, x = 23."),
("Questão 4","As raízes da equação 2x<sup>2</sup> − 3x − 2 = 0 são",["2 e −1/2","−2 e 1/2","3 e −2","1 e −2","2 e 1/2"],0,"Δ = 9 + 16 = 25; x = (3 ± 5)/4: 2 e −1/2.")]
QR=[(a,b,c,[2,4,1,3][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
QRF=qr_md(QR,5)
t1="<strong>Compra de coletes</strong><br><br>A Guarda Municipal de Vila Nova, cidade fictícia, comprou 5 coletes de mesmo preço. O fornecedor cobrou um frete fixo de R$ 30,00, e o valor total da compra foi de R$ 280,00."
t2="<strong>Cerca de um terreno</strong><br><br>Um terreno retangular, ao lado do quartel, tem comprimento 3 metros maior que a largura e área de 40 metros quadrados. A Prefeitura pretende cercá-lo."
tx={"mt6a":t1,"mt6b":t2}
assert 5*50+30==280 and 5*8==40 and 8-5==3
# n=1
q(1,"A solução da equação x + 7 = 15 é",["8","22","7","−8","2"],"x = 15 − 7 = 8.")
q(1,"A solução da equação 3x = 21 é",["7","18","24","63","3"],"x = 21 ÷ 3 = 7.")
q(1,"A solução da equação 2x − 5 = 9 é",["7","2","14","−2","4"],"2x = 14, x = 7.")
q(1,"A solução da equação x/4 = 6 é",["24","1,5","10","2","6"],"x = 6 × 4 = 24.")
q(1,"A solução da equação 5x + 3 = 28 é",["5","6,2","31","4","25"],"5x = 25, x = 5.")
q(1,"A solução da equação 4x = 3x + 9 é",["9","1","−9","3","12"],"4x − 3x = 9, x = 9.")
q(1,"A solução da equação x − 12 = 30 é",["42","18","−18","2,5","360"],"x = 30 + 12 = 42.")
q(1,"O triplo de um número é 45. Esse número é",["15","135","42","14","48"],"3x = 45, x = 15.")
q(1,"A soma de um número com o seu dobro é 36. O número é",["12","18","9","24","6"],"x + 2x = 36, 3x = 36, x = 12.")
q(1,"As soluções da equação x<sup>2</sup> = 49 são",["7 e −7","7","−7","49","24,5"],"Os dois números, 7 e −7, elevados ao quadrado dão 49.")
q(1,"As soluções da equação x<sup>2</sup> − 9 = 0 são",["3 e −3","3","9 e −9","0 e 3","−3"],"x<sup>2</sup> = 9, logo x = 3 ou x = −3.")
q(1,"As soluções da equação x<sup>2</sup> − 5x = 0 são",["0 e 5","5","−5 e 0","0 e −5","5 e −5"],"x(x − 5) = 0: x = 0 ou x = 5.")
q(1,"O dobro de um número, aumentado de 4, é igual a 20. O número é",["8","12","6","10","16"],"2x + 4 = 20, 2x = 16, x = 8.")
q(1,"A solução da equação 2x + x = 27 é",["9","13,5","27","3","18"],"3x = 27, x = 9.")
q(1,"A solução da equação 10 − x = 3 é",["7","13","−7","3","30"],"x = 10 − 3 = 7.")
q(1,"As raízes de x<sup>2</sup> − 5x + 6 = 0 são",["2 e 3","−2 e −3","1 e 6","−2 e 3","5 e 6"],"Soma 5 e produto 6: 2 e 3.")
q(1,"Em x<sup>2</sup> − 4x + 3 = 0, os coeficientes a, b e c são, respectivamente,",["1, −4 e 3","1, 4 e 3","−4, 1 e 3","1, 3 e −4","0, −4 e 3"],"a é o número que multiplica x<sup>2</sup>, b o de x e c o termo livre.")
q(1,"O discriminante Δ da equação x<sup>2</sup> − 6x + 5 = 0 é",["16","56","−16","6","4"],"Δ = 36 − 4 × 1 × 5 = 16.")
q(1,"Pelo texto, o preço de cada colete é",["R$ 50,00","R$ 56,00","R$ 46,00","R$ 62,00","R$ 280,00"],"5x + 30 = 280, 5x = 250, x = 50.","mt6a")
q(1,"Segundo o texto, o valor total dos coletes, sem o frete, foi de",["R$ 250,00","R$ 30,00","R$ 280,00","R$ 310,00","R$ 56,00"],"280 − 30 = 250.","mt6a")
# n=2
q(2,"A solução de 3(x − 2) = 2x + 5 é",["11","−1","7","3","1"],"3x − 6 = 2x + 5; x = 11.")
q(2,"A solução de (x + 1)/2 = 7 é",["13","6","15","14","7"],"x + 1 = 14, x = 13.")
q(2,"A solução de x/3 + x/2 = 10 é",["12","4","6","5","10"],"Multiplica por 6: 2x + 3x = 60, x = 12.")
q(2,"A solução de 5x − 8 = 2x + 7 é",["5","1","3","15","−5"],"3x = 15, x = 5.")
q(2,"A soma das idades de um pai e de um filho é 50 anos, e o pai tem o quádruplo da idade do filho. A idade do pai é",["40","10","30","45","20"],"x + 4x = 50, x = 10; pai 40.")
q(2,"As raízes de x<sup>2</sup> − 7x + 12 = 0 são",["3 e 4","−3 e −4","2 e 6","1 e 12","−3 e 4"],"Soma 7, produto 12: 3 e 4.")
q(2,"As raízes de x<sup>2</sup> + 2x − 15 = 0 são",["3 e −5","−3 e 5","3 e 5","−3 e −5","15 e −1"],"Soma −2 e produto −15: 3 e −5.")
q(2,"A soma das raízes de x<sup>2</sup> − 8x + 15 = 0 é",["8","15","−8","7","3"],"Soma = −b/a = 8.")
q(2,"As soluções de x<sup>2</sup> − 16 = 0 são",["4 e −4","4","16","8 e −8","0 e 4"],"x<sup>2</sup> = 16.")
q(2,"As soluções de 2x<sup>2</sup> − 8x = 0 são",["0 e 4","4","0 e −4","2 e 4","8"],"2x(x − 4) = 0.")
q(2,"Três números inteiros consecutivos somam 72. O menor é",["23","24","22","21","25"],"3x + 3 = 72, x = 23.")
q(2,"O discriminante de 2x<sup>2</sup> − 3x − 2 = 0 é",["25","1","−7","17","9"],"Δ = 9 − 4 × 2 × (−2) = 25.")
q(2,"As raízes de 2x<sup>2</sup> − 3x − 2 = 0 são",["2 e −1/2","−2 e 1/2","3 e −2","1 e −2","2 e 1/2"],"(3 ± 5)/4.")
q(2,"Daqui a 5 anos, a idade de Ana será o dobro da que ela tinha há 3 anos. A idade atual de Ana é",["11","8","13","16","10"],"x + 5 = 2(x − 3), x + 5 = 2x − 6, x = 11.")
q(2,"Em 50 moedas, de 5 e de 10 centavos, que somam R$ 3,50, o número de moedas de 10 centavos é",["20","30","25","15","35"],"5a + 10(50 − a) = 350 → a = 30; as de 10 centavos são 20.")
q(2,"A solução de (2x − 1)/3 = 5 é",["8","7","3","16","2"],"2x − 1 = 15, x = 8.")
q(2,"A raiz positiva de x<sup>2</sup> + 2x − 24 = 0 é",["4","6","3","8","2"],"Soma −2 e produto −24: 4 e −6.")
q(2,"Pelo texto, o valor da compra de 8 coletes iguais, com o mesmo frete de R$ 30,00, seria de",["R$ 430,00","R$ 400,00","R$ 460,00","R$ 280,00","R$ 380,00"],"8 × 50 + 30 = 430.","mt6a")
q(2,"Pelo texto, a largura do terreno é, em metros,",["5","8","3","4","10"],"x(x + 3) = 40 → x<sup>2</sup> + 3x − 40 = 0 → x = 5 (a outra raiz, −8, é descartada).","mt6b")
q(2,"Pelo texto, o comprimento do terreno é, em metros,",["8","5","13","3","40"],"A largura é 5 e o comprimento é 5 + 3 = 8.","mt6b")
# n=3
q(3,"A raiz positiva de x<sup>2</sup> − x − 56 = 0 é",["8","7","14","56","9"],"Soma 1 e produto −56: 8 e −7.")
q(3,"A soma dos quadrados de dois números inteiros consecutivos é 61. O menor é",["5","6","4","3","7"],"x<sup>2</sup> + (x + 1)<sup>2</sup> = 61 → x<sup>2</sup> + x − 30 = 0 → x = 5. Confira: 25 + 36 = 61.")
q(3,"Um retângulo tem perímetro 30 m e área 56 m². Seu maior lado mede, em metros,",["8","7","14","15","6"],"Semiperímetro 15: lados x e 15 − x. x(15 − x) = 56 → x<sup>2</sup> − 15x + 56 = 0 → 7 e 8.")
q(3,"O valor de k para que x<sup>2</sup> − 6x + k = 0 tenha uma única solução real é",["9","6","36","3","−9"],"Δ = 36 − 4k = 0 → k = 9.")
q(3,"Os valores de b para que x<sup>2</sup> + bx + 36 = 0 tenha raiz dupla são",["12 e −12","6 e −6","36 e −36","12","−6"],"Δ = b<sup>2</sup> − 144 = 0, b = 12 ou b = −12.")
q(3,"O produto das raízes de 2x<sup>2</sup> − 10x + 8 = 0 é",["4","5","−4","8","10"],"Produto = c/a = 8/2 = 4.")
q(3,"A soma dos quadrados das raízes de x<sup>2</sup> − 5x + 6 = 0 é",["13","25","11","30","5"],"As raízes são 2 e 3: 4 + 9 = 13.")
q(3,"Um guarda caminha 24 km. Se andasse 2 km/h mais depressa, chegaria 1 hora mais cedo. Sua velocidade é, em km/h,",["6","8","4","12","3"],"24/x − 24/(x + 2) = 1 → x<sup>2</sup> + 2x − 48 = 0 → x = 6. Conferindo: 4 h contra 3 h.")
q(3,"Um objeto lançado tem altura h = −t<sup>2</sup> + 6t, em metros, com t em segundos. Ele volta ao solo depois de",["6 s","3 s","9 s","12 s","36 s"],"h = 0: t(6 − t) = 0, t = 0 (lançamento) ou t = 6.")
q(3,"A solução de x/(x − 1) = 3/2 é",["3","1","2","−3","6"],"2x = 3x − 3, x = 3.")
q(3,"A solução positiva de 1/x + 1/(x + 1) = 5/6 é",["2","3","1","6","5"],"6(2x + 1) = 5x(x + 1) → 5x<sup>2</sup> − 7x − 6 = 0 → x = 2. Confira: 1/2 + 1/3 = 5/6.")
q(3,"A soma das soluções de (x − 3)<sup>2</sup> = 25 é",["6","8","−2","16","0"],"x − 3 = ±5: x = 8 ou x = −2; soma 6.")
q(3,"Aumentando 3 m o lado de um quadrado, a área aumenta 51 m². O lado original mede, em metros,",["7","6","8","5","9"],"(x + 3)<sup>2</sup> − x<sup>2</sup> = 51 → 6x + 9 = 51 → x = 7.")
q(3,"A solução de 3x − 2(x − 4) = 15 é",["7","23","11","−7","3"],"3x − 2x + 8 = 15, x = 7.")
q(3,"R$ 180,00 seriam divididos igualmente entre alguns guardas. Como 3 faltaram, cada presente recebeu R$ 2,00 a mais. O número de guardas previsto era",["18","15","12","20","21"],"180/(n − 3) = 180/n + 2 → n<sup>2</sup> − 3n − 270 = 0 → n = 18. 180 ÷ 15 = 12 e 180 ÷ 18 = 10.")
q(3,"Se a soma de um número com seu quadrado é 42, o número positivo é",["6","7","−7","21","5"],"x<sup>2</sup> + x − 42 = 0: soma −1, produto −42: 6 e −7.")
q(3,"A equação x<sup>2</sup> + 4x + 5 = 0",["não tem raízes reais.","tem duas raízes reais iguais.","tem raízes 1 e 5.","tem raízes −1 e −5.","tem uma raiz real."],"Δ = 16 − 20 = −4, negativo: sem raízes reais.")
q(3,"Pelo texto, com um orçamento de R$ 600,00 para coletes de mesmo preço e o mesmo frete, o número máximo de coletes é",["11","12","10","13","9"],"50x + 30 ≤ 600 → x ≤ 11,4. Máximo 11.","mt6a")
q(3,"Pelo texto, o perímetro do terreno, em metros, é",["26","13","16","40","21"],"2 × (5 + 8) = 26.","mt6b")
q(3,"Pelo texto, se a largura e o comprimento aumentassem 1 metro cada, a área passaria a ser, em m²,",["54","50","48","56","45"],"6 × 9 = 54.","mt6b")
assert 50*11+30<=600<50*12+30 and 2*(5+8)==26 and 6*9==54 and 36-4*9==0 and 5**2+7*0==25
for r in (8,-7): assert r*r-r-56==0
for r in (5,): assert r**2+(r+1)**2==61
assert 24/6-24/8==1 and 180/15+0==12 and 180/18==10 and 18*18-3*18-270==0 and 6+36==42
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("Equações: traduzir, resolver, conferir",[
 ("balanca","Balança",["mesma operação nos dois lados","operação inversa","muda de lado, muda de sinal"],"seção 1"),
 ("g1","1º grau",["x = −b/a","tira parênteses e denominadores","confere substituindo"],"seção 2"),
 ("traducao","Tradução",["defina a incógnita","dobro = 2x; consecutivos","“é” vira igual"],"seção 3"),
 ("incompleta","2º grau incompleto",["b = 0: raiz quadrada","c = 0: x em evidência","raízes: ±; 0 e outro"],"seção 4"),
 ("bhaskara","Bhaskara",["Δ = b² − 4ac","x = (−b ± √Δ)/2a","Δ < 0: sem raiz real"],"seção 4"),
 ("somaprod","Soma e produto",["x₁ + x₂ = −b/a","x₁ · x₂ = c/a","sem resolver a equação"],"seção 4")],
 "Na prova: monte a equação em símbolos e descarte a raiz que não faz sentido")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"A tradução do texto é a etapa mais cobrada; as demais caixas são as ferramentas para resolver a equação montada.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula.")
revisao("mt-6","Equações do 1º e do 2º graus",QQ,list(tx),
 cobertura=["Recorte do edital: montagem e resolução de equações. Cobertos: 1º grau com parênteses e frações, tradução de enunciados (consecutivos, idades, moedas), 2º grau incompleto e completo, discriminante, soma e produto das raízes, equações fracionárias e problemas de geometria e velocidade."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","Parte dos gabaritos foi conferida por substituição na equação (exemplos e QR) e por asserts no script; as demais por conferência manual. Recomendo uma segunda checagem das questões do banco."],
 fontes_conferidas=[])
gravar("mt-6",aula_html,banco("mt-6",QQ),tx)
