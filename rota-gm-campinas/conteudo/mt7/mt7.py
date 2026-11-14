import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
LEAD="Sistema de equações do 1º grau é o recurso para problemas com duas incógnitas e duas pistas: preços de dois produtos, moedas de dois valores, idades de duas pessoas. A Vunesp cobra a montagem do sistema a partir do texto e sua resolução por substituição ou por adição, além de reconhecer quando o sistema não tem solução ou tem infinitas. Como em toda equação, a parte difícil é traduzir; a conta é curta."
S={}
S[1]="""## 1. Por que duas equações

Uma equação com duas incógnitas, como x + y = 10, tem infinitas soluções: (1, 9), (2, 8), (5, 5) e tantas outras. Para fixar um par só, é preciso uma segunda informação, e a ela corresponde uma segunda equação. O conjunto das duas é um sistema, e a solução é o par (x, y) que satisfaz as duas ao mesmo tempo. Com x + y = 10 e x − y = 2, só o par (6, 4) serve: 6 + 4 = 10 e 6 − 4 = 2.

A imagem geométrica ajuda: cada equação é uma reta, e a solução é o ponto em que as retas se cruzam. Isso explica os dois casos especiais, tratados na seção 4.
"""
S[2]="""## 2. Método da substituição

A ideia é isolar uma incógnita em uma equação e colocar o resultado na outra, que passa a ter só uma incógnita. Considere x + y = 11 e x = y + 3. A segunda já traz x isolado. Trocando na primeira, (y + 3) + y = 11, então 2y + 3 = 11, 2y = 8 e y = 4. De volta a x = y + 3, x = 7. Confira nas duas: 7 + 4 = 11 e 7 = 4 + 3.

Escolha para isolar a incógnita que tem coeficiente 1, porque evita frações. Em 2x + y = 9 e x − y = 0, isole y = 2x − ... ou melhor, perceba que x = y na segunda e troque: 2y + y = 9, y = 3, x = 3.
"""
S[3]="""## 3. Método da adição

A ideia é somar (ou subtrair) as duas equações de modo que uma incógnita desapareça. Em x + y = 10 e x − y = 2, somando termo a termo, 2x = 12 e x = 6; depois, y = 4. Quando os coeficientes não se anulam, multiplica-se uma ou as duas equações por números que os igualem.

Exemplo resolvido. Duas canetas e um lápis custam R$ 7,00, e uma caneta e um lápis custam R$ 5,00. Quanto custa a caneta? Com c a caneta e l o lápis, 2c + l = 7 e c + l = 5. Subtraindo a segunda da primeira, o lápis some: c = 2. Então l = 3.

Outro exemplo. Resolva 3x + 2y = 16 e x + y = 6. Multiplicando a segunda por 2, 2x + 2y = 12. Subtraindo da primeira, x = 4, e então y = 2. Conferindo: 3 × 4 + 2 × 2 = 16.
"""
S[4]="""## 4. Problemas e casos especiais

Para montar o sistema, dê um nome a cada incógnita e escreva uma equação para cada informação do texto. Em problemas de moedas e ingressos, uma equação conta quantos objetos há, e a outra soma os valores.

Exemplo resolvido 1. Em 25 notas de R$ 5,00 e de R$ 10,00, que somam R$ 190,00, quantas notas são de R$ 10,00? Sendo a o número de notas de 5 e b o de 10, a + b = 25 e 5a + 10b = 190. Multiplicando a primeira por 5, 5a + 5b = 125. Subtraindo, 5b = 65 e b = 13. Então a = 12.

Exemplo resolvido 2, com rodas. Em um pátio há 20 veículos, entre carros e motos, e 64 rodas. Quantos carros? Com c carros e m motos, c + m = 20 e 4c + 2m = 64. Multiplicando a primeira por 2, 2c + 2m = 40. Subtraindo, 2c = 24 e c = 12. Então m = 8.

Exemplo resolvido 3, com correnteza. Um barco faz um trecho a favor da correnteza com velocidade 18 km/h e, contra, com 12 km/h. A soma da velocidade do barco b com a da correnteza c é 18, e a diferença é 12. Somando, 2b = 30 e b = 15. Então c = 3.

Os casos especiais aparecem quando as retas não se cruzam num único ponto. Se as retas são paralelas, o sistema é impossível, sem solução: x + y = 3 e 2x + 2y = 8, porque a segunda dá x + y = 4, que contradiz a primeira. Se as retas coincidem, o sistema é possível e indeterminado, com infinitas soluções: x + y = 3 e 2x + 2y = 6, porque a segunda é só a primeira multiplicada por 2. O sistema com um único par é possível e determinado.
"""
S[6]="""## 6. Na rotina do guarda

- **Compras:** dois produtos e dois pedidos com quantidades diferentes formam um sistema, como as canetas e os lápis.
- **Pátio e frota:** número de veículos e número de rodas dão o sistema de carros e motos.
- **Rateios desiguais:** duas condições sobre dois valores, como “soma de R$ 1.000,00 e diferença de R$ 300,00”.
- **Idades:** quando a prova dá a relação entre as idades hoje e daqui a alguns anos, monta-se um sistema.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Montar duas equações iguais com palavras diferentes | Cada equação deve trazer uma informação nova |
| Esquecer de multiplicar todos os termos ao ajustar coeficientes | Multiplique os dois lados e todos os termos |
| Responder só x quando pedem x + y ou o maior valor | Releia a pergunta antes de responder |
| Trocar o sinal ao subtrair equações | Subtraia termo a termo, com atenção aos negativos |
| Dar por solução um par que só satisfaz uma equação | Teste nas duas equações |
| Achar que todo sistema tem solução única | Se os coeficientes são proporcionais, é impossível ou indeterminado |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Sistema | Duas equações; o par que satisfaz as duas |
| Substituição | Isola uma incógnita e troca na outra equação |
| Adição | Soma ou subtrai as equações para eliminar uma incógnita |
| Moedas e ingressos | Uma equação conta objetos; outra soma valores |
| Impossível | Retas paralelas: sem solução |
| Indeterminado | Retas coincidentes: infinitas soluções |
| Conferência | Teste o par nas duas equações |
"""
assert sis(1,1,10,1,-1,2)==(6,4) and sis(2,1,7,1,1,5)==(2,3) and sis(3,2,16,1,1,6)==(4,2)
assert sis(1,1,25,5,10,190)==(12,13) and sis(1,1,20,4,2,64)==(12,8) and sis(1,1,18,1,-1,12)==(15,3)
QR=[("Questão 1","Duas canetas e um lápis custam R$ 7,00, e uma caneta e um lápis custam R$ 5,00. O preço de uma caneta é",["R$ 2,00","R$ 3,00","R$ 1,50","R$ 2,50","R$ 4,00"],1,"2c + l = 7 e c + l = 5. Subtraindo, c = 2 (e l = 3)."),
("Questão 2","Em um pátio há 20 veículos, entre carros e motos, e 64 rodas. O número de motos é",["8","12","6","10","14"],0,"c + m = 20 e 4c + 2m = 64. Multiplicando a primeira por 2 e subtraindo, 2c = 24: c = 12 e m = 8."),
("Questão 3","A soma de dois números é 40 e a diferença entre eles é 12. O maior deles é",["26","28","14","24","32"],0,"x + y = 40 e x − y = 12. Somando, 2x = 52 e x = 26."),
("Questão 4","O sistema x + y = 3 e 2x + 2y = 8 é",["impossível.","possível e determinado.","possível e indeterminado.","satisfeito por (1, 2).","satisfeito por (2, 1)."],0,"A segunda equação, dividida por 2, dá x + y = 4, que contradiz x + y = 3. Não há solução.")]
QR=[(a,b,c,[2,4,0,3][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
assert sis(1,1,40,1,-1,12)[0]==26
QRF=qr_md(QR,5)
t1="<strong>Compra de caixas de material</strong><br><br>A Guarda Municipal de Vila Nova, cidade fictícia, comprou caixas de dois tipos de material: A e B. Duas caixas do tipo A e três do tipo B custaram R$ 190,00. Uma caixa do tipo A e duas do tipo B custaram R$ 110,00."
t2="<strong>Pátio da Guarda</strong><br><br>No pátio da Guarda Municipal de Vila Nova há 20 veículos, entre carros e motocicletas, que somam 64 rodas."
tx={"mt7a":t1,"mt7b":t2}
assert sis(2,3,190,1,2,110)==(50,30) and 5*50+4*30==370 and 50-30==20
# n=1
qv(1,"Se x + y = 10 e x − y = 2, o valor de x é","{}",6,[4,8,12,2],"Somando: 2x = 12, x = 6.")
qv(1,"Se x + y = 12 e x = y + 4, o valor de y é","{}",4,[8,6,16,2],"y + 4 + y = 12, y = 4.")
qv(1,"Duas canetas e um lápis custam R$ 7,00, e uma caneta e um lápis custam R$ 5,00. A caneta custa","R$ {},00",2,[3,1,4,5],"Subtraindo as equações: c = 2.")
qv(1,"A soma de dois números é 20 e a diferença é 6. O maior é","{}",13,[7,14,10,26],"2x = 26, x = 13.")
qv(1,"Se x + y = 15 e 2x + y = 22, o valor de x é","{}",7,[8,15,22,37],"Subtraindo a primeira da segunda: x = 7.")
qv(1,"Duas camisas e uma calça custam R$ 100,00, e uma camisa e uma calça custam R$ 70,00. A camisa custa","R$ {},00",30,[40,70,50,35],"Subtraindo: camisa = 30.")
qv(1,"Se x + y = 11 e x = y + 3, o valor de x é","{}",7,[4,8,3,11],"2y + 3 = 11, y = 4, x = 7.")
q(1,"O par ordenado que é solução do sistema x + y = 5 e x − y = 1 é",["(3, 2)","(2, 3)","(4, 1)","(1, 4)","(5, 0)"],"2x = 6, x = 3, y = 2.")
qv(1,"A soma das idades de um pai e de seu filho é 45 anos, e a diferença é 25 anos. O filho tem","{} anos",10,[35,15,20,25],"Soma menos diferença: 2f = 20, f = 10.")
qv(1,"Em 10 moedas, de R$ 1,00 e de R$ 0,50, que somam R$ 7,00, o número de moedas de R$ 0,50 é","{}",6,[4,5,7,3],"a + b = 10 e a + 0,5b = 7. Subtraindo, 0,5b = 3, b = 6.")
qv(1,"Três ingressos de adulto e dois de criança custam R$ 80,00; um de adulto e dois de criança, R$ 40,00. O ingresso de adulto custa","R$ {},00",20,[10,25,30,15],"Subtraindo: 2a = 40, a = 20.")
qv(1,"Se x + 2y = 11 e x = 3, o valor de y é","{}",4,[3,8,5,2],"3 + 2y = 11, y = 4.")
qv(1,"Se 2x + y = 9 e x − y = 0, o valor de x é","{}",3,[9,4.5,2,6],"x = y: 3x = 9, x = 3.")
qv(1,"A soma de dois números é 30 e um é o dobro do outro. O maior é","{}",20,[10,15,25,30],"x + 2x = 30, x = 10; o maior é 20.")
qv(1,"Um retângulo tem perímetro 20 cm e comprimento 2 cm maior que a largura. O comprimento é","{} cm",6,[4,8,5,10],"2(l + l + 2) = 20 → l = 4, comprimento 6.")
qv(1,"Se 3x + y = 10 e x + y = 6, o valor de y é","{}",4,[2,6,10,3],"Subtraindo: 2x = 4, x = 2, y = 4.")
qv(1,"Dois cadernos e três canetas custam R$ 21,00; um caderno e três canetas, R$ 15,00. O caderno custa","R$ {},00",6,[3,9,5,7],"Subtraindo: caderno = 6.")
qv(1,"Em um grupo de 40 pessoas, o número de homens é o triplo do de mulheres. As mulheres são","{}",10,[30,13,20,8],"m + 3m = 40, m = 10.")
qv(1,"Pelo texto, o preço de cada caixa do tipo A é","R$ {},00",50,[40,60,30,45],"2a + 3b = 190 e a + 2b = 110. Multiplicando a segunda por 2 e subtraindo: b = 30, a = 50.","mt7a")
qv(1,"Pelo texto, o preço de cada caixa do tipo B é","R$ {},00",30,[20,35,25,40],"b = 30 (ver sistema).","mt7a")
# n=2
qv(2,"Se 2x + 3y = 12 e x − y = 1, o valor de y é","{}",2,[3,1,4,6],"x = y + 1: 2y + 2 + 3y = 12, y = 2.")
qv(2,"Se 3x + 2y = 16 e x + y = 6, o valor de x é","{}",4,[2,6,3,8],"Multiplicando a segunda por 2 e subtraindo: x = 4.")
qv(2,"A é 4 anos mais velho que B, e a soma das idades é 36. A idade de A é","{} anos",20,[16,18,22,24],"a = b + 4: 2b + 4 = 36, b = 16, a = 20.")
qv(2,"Uma loja vende camisas a R$ 40,00 e calças a R$ 60,00. Foram vendidas 5 peças por R$ 260,00. O número de calças foi","{}",3,[2,4,1,5],"c + p = 5 e 40c + 60p = 260. 200 + 20p = 260, p = 3.")
qv(2,"Se x/2 + y/3 = 4 e x − y = 3, o valor de x é","{}",6,[3,4,9,5],"3x + 2y = 24; x = y + 3: 5y + 9 = 24, y = 3, x = 6.")
qv(2,"Em 25 notas de R$ 5,00 e de R$ 10,00, que somam R$ 190,00, o número de notas de R$ 10,00 é","{}",13,[12,15,10,8],"a + b = 25 e 5a + 10b = 190: 5b = 65, b = 13.")
qv(2,"Um barco, a favor da correnteza, anda 18 km/h e, contra, 12 km/h. A velocidade da correnteza é","{} km/h",3,[6,15,2,1.5],"b + c = 18 e b − c = 12. Subtraindo: 2c = 6, c = 3.")
qv(2,"Um terreno retangular tem perímetro 36 m e comprimento igual ao dobro da largura. A área é","{} m²",72,[48,36,64,81],"2(l + 2l) = 36, l = 6, comprimento 12; área 72.")
qv(2,"Se 4x − y = 7 e 2x + y = 5, o valor de x + y é","{}",3,[2,5,4,6],"Somando: 6x = 12, x = 2, y = 1.")
qv(2,"A soma de dois números é 48 e a razão entre eles é 3/5. O maior é","{}",30,[18,24,20,35],"3k + 5k = 48, k = 6; maior 30.")
qv(2,"A soma de dois números é 40 e a diferença é 12. O menor é","{}",14,[26,12,20,16],"x = 26, y = 14.")
qv(2,"Em um pátio de bicicletas e triciclos há 10 veículos e 24 rodas. O número de triciclos é","{}",4,[6,3,5,2],"b + t = 10 e 2b + 3t = 24: t = 4.")
qv(2,"Duas entradas inteiras e três meias custam R$ 70,00; uma inteira e uma meia, R$ 30,00. A meia custa","R$ {},00",10,[20,15,5,25],"Multiplicando a segunda por 2: 2i + 2m = 60. Subtraindo: m = 10.")
qv(2,"O pai tem o triplo da idade do filho; daqui a 10 anos terá o dobro. O filho tem hoje","{} anos",10,[12,15,8,5],"3f + 10 = 2(f + 10), f = 10.")
q(2,"O sistema x + y = 3 e 2x + 2y = 8 é",["impossível.","possível e determinado.","possível e indeterminado.","satisfeito por (1, 2).","satisfeito por (0, 4)."],"A segunda equação equivale a x + y = 4, que contradiz x + y = 3.")
q(2,"O sistema x + y = 3 e 2x + 2y = 6 é",["possível e indeterminado.","impossível.","possível e determinado, com solução (1, 2).","possível e determinado, com solução (3, 0).","possível, com solução única (2, 1)."],"A segunda equação é a primeira multiplicada por 2: infinitas soluções.")
q(2,"O par (2, 3) é solução do sistema",["2x + y = 7 e x + y = 5","x + y = 6 e x − y = 1","2x + y = 8 e x + y = 5","x + 2y = 7 e x − y = 1","2x − y = 7 e x + y = 5"],"2 × 2 + 3 = 7 e 2 + 3 = 5. Os demais falham em ao menos uma equação.")
qv(2,"Pelo texto, o custo de 5 caixas do tipo A e 4 do tipo B é","R$ {},00",370,[340,380,350,400],"5 × 50 + 4 × 30 = 370.","mt7a")
qv(2,"Pelo texto, o número de carros no pátio é","{}",12,[8,10,14,16],"c + m = 20 e 4c + 2m = 64: c = 12.","mt7b")
qv(2,"Pelo texto, o número de motocicletas no pátio é","{}",8,[12,6,10,4],"20 − 12 = 8.","mt7b")
# n=3
qv(3,"Há 6 anos a soma das idades de Maria e de Ana era 24, e hoje Maria tem o dobro da idade de Ana. Ana tem hoje","{} anos",12,[10,14,16,8],"Hoje a soma é 36. m = 2a: 3a = 36, a = 12.")
qv(3,"Um barco faz 24 km a favor da correnteza em 2 horas e 24 km contra em 3 horas. A velocidade do barco em água parada é","{} km/h",10,[12,8,2,9],"b + c = 12 e b − c = 8: b = 10, c = 2.")
qv(3,"Misturam-se 20 litros de dois combustíveis, a R$ 5,00 e a R$ 3,00 o litro. O total pago foi R$ 84,00. O volume do combustível de R$ 5,00 é","{} litros",12,[8,10,14,15],"a + b = 20 e 5a + 3b = 84. 5a + 60 − 3a = 84, a = 12.")
qv(3,"Um número de dois algarismos tem soma dos algarismos 9. Trocando a ordem, o número aumenta 27. O número é","{}",36,[63,27,45,18],"x + y = 9 e (10y + x) − (10x + y) = 27, ou y − x = 3: y = 6, x = 3.")
qv(3,"R$ 100,00 serão repartidos entre A, B e C. A recebe R$ 20,00 a mais que B, e C recebe R$ 10,00 a menos que B. C recebe","R$ {},00",20,[30,50,10,40],"b + 20 + b + b − 10 = 100, 3b = 90, b = 30; C = 20.")
qv(3,"Em um sítio há galinhas e coelhos, num total de 35 cabeças e 94 pés. O número de coelhos é","{}",12,[23,10,15,17],"g + c = 35 e 2g + 4c = 94. 70 + 2c = 94, c = 12.")
qv(3,"Dois prêmios somam R$ 1.000,00 e a diferença entre eles é R$ 300,00. O maior é","R$ {},00",650,[700,350,600,500],"x = (1.000 + 300)/2 = 650.")
qv(3,"O pai tem o triplo da idade do filho; daqui a 12 anos terá o dobro. A idade do pai hoje é","{} anos",36,[12,48,30,42],"3f + 12 = 2(f + 12), f = 12, p = 36.")
qv(3,"Dois sócios têm lucro total de R$ 5.000,00, e A recebe 1,5 vez o que B recebe. A recebe","R$ {},00",3000,[2000,2500,3500,3750],"a = 1,5b: 2,5b = 5.000, b = 2.000, a = 3.000.")
qv(3,"Se x/2 + y/3 = 4 e x/4 − y/6 = 0, o valor de x + y é","{}",10,[8,12,14,6],"Multiplicando: 3x + 2y = 24 e 3x − 2y = 0. Somando: x = 4; y = 6.")
qv(3,"Se 2x − 3y = −4 e 3x + 2y = 7, o valor de 5x + y é","{}",7,[5,9,11,3],"Resolvendo, x = 1 e y = 2. Então 5 + 2 = 7.")
qv(3,"O valor de k para o qual o sistema x + 2y = 5 e 3x + ky = 7 é impossível é","{}",6,[2,3,7,5],"As retas são paralelas quando 3/1 = k/2 e 7 ≠ 15: k = 6.")
qv(3,"Três canetas e dois cadernos custam R$ 23,00; duas canetas e três cadernos, R$ 27,00. Uma caneta e um caderno custam juntos","R$ {},00",10,[8,12,9,14],"Somando as equações: 5c + 5k = 50, logo c + k = 10.")
qv(3,"As retas y = 2x + 1 e y = −x + 7 se cruzam em um ponto cuja soma das coordenadas é","{}",7,[5,3,9,6],"2x + 1 = −x + 7, x = 2, y = 5. Soma 7.")
qv(3,"Dois números somam 44 e 2/5 de um deles é igual a 1/3 do outro. O maior é","{}",24,[20,22,26,30],"y = 6x/5 e x + y = 44: x = 20, y = 24.")
qv(3,"Se 3x − y = 5 e x + y = 11, o valor de y é","{}",7,[4,5,3,8],"Somando: 4x = 16, x = 4, y = 7.")
qv(3,"O triplo de um número mais outro é 19, e o primeiro mais o dobro do segundo é 13. O produto dos dois números é","{}",20,[15,24,35,12],"3x + y = 19 e x + 2y = 13. Multiplicando a primeira por 2 e subtraindo a segunda: 5x = 25, x = 5, y = 4. Produto 20.")
qv(3,"Para que o par (2, 1) seja solução da equação x + ky = 5, o valor de k deve ser","{}",3,[2,1,4,5],"2 + k × 1 = 5, k = 3.")
qv(3,"Se, para o texto, a Guarda comprasse 4 caixas do tipo A e 6 do tipo B, gastaria","R$ {},00",380,[340,360,400,420],"4 × 50 + 6 × 30 = 380.","mt7a")
qv(3,"Pelo texto, retiradas as motocicletas do pátio, as rodas restantes seriam","{}",48,[44,64,56,40],"12 carros × 4 rodas = 48.","mt7b")
assert sis(1,1,20,5,3,84)[0]==12 and sis(1,1,35,2,4,94)[1]==12
assert sis(2,-3,-4,3,2,7)==(1,2) and sis(3,-1,5,1,1,11)==(4,7)
assert sis(3,2,23,2,3,27)==(3,7)
QQ=fechar()
assert sis(3,1,19,1,2,13)==(5,4)
assert len(QQ)==60, len(QQ)
code,svg=mapa("Sistemas: duas pistas, duas incógnitas",[
 ("porque","Por que duas equações",["uma equação tem infinitas soluções","duas fixam um par","as retas se cruzam"],"seção 1"),
 ("subst","Substituição",["isola uma incógnita","troca na outra equação","bom se o coeficiente é 1"],"seção 2"),
 ("adicao","Adição",["soma ou subtrai","elimina uma incógnita","ajusta coeficientes"],"seção 3"),
 ("probl","Problemas",["moedas e ingressos","rodas e correnteza","idades"],"seção 4"),
 ("imposs","Impossível",["retas paralelas","sem solução","x + y = 3 e 2x + 2y = 8"],"seção 4"),
 ("indet","Indeterminado",["retas coincidentes","infinitas soluções","uma é múltipla da outra"],"seção 4")],
 "Na prova: monte uma equação para cada informação e teste o par nas duas")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"Os dois métodos resolvem o mesmo sistema; os dois últimos quadros dizem quando ele não tem uma solução única.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula.")
revisao("mt-7","Sistemas de equações do 1º grau",QQ,list(tx),
 cobertura=["Recorte do edital: situações-problema com duas incógnitas. Cobertos: substituição, adição, problemas de moedas, ingressos, rodas, idades, correnteza, mistura, sistema impossível e indeterminado."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","Os sistemas do banco foram conferidos com um solucionador (regra de Cramer) em código para boa parte das questões; as demais, por conferência manual."],
 fontes_conferidas=[])
gravar("mt-7",aula_html,banco("mt-7",QQ),tx)
