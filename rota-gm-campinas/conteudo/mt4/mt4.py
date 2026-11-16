import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
LEAD="Razão e proporção é o assunto que explica por que a regra de três funciona. A Vunesp cobra três coisas: calcular e comparar razões (inclusive com unidades diferentes e escalas), resolver proporções e reconhecer se duas grandezas variam na mesma direção ou em direções opostas, para então dividir um valor proporcionalmente. A ideia central cabe em uma frase: duas grandezas são proporcionais quando mudam juntas, mantendo uma relação fixa."
S={}
S[1]="""## 1. Razão: comparar por divisão

Razão entre dois números é o quociente entre eles. Dizer que há 12 guardas para cada 20 viaturas é dizer que a razão entre guardas e viaturas é 12/20, ou 3/5. Lê-se “3 para 5”, e significa que, a cada 3 guardas, há 5 viaturas. A ordem importa: a razão entre viaturas e guardas é 5/3, outro número.

Para comparar, as unidades precisam ser iguais. A razão entre 40 minutos e 2 horas não é 40/2. Primeiro converta: 2 horas são 120 minutos, e a razão é 40/120 = 1/3. Quando as unidades são diferentes de propósito, a razão ganha nome e unidade própria: velocidade é a razão entre distância e tempo (120 km em 2 h dão 60 km/h); densidade é a razão entre massa e volume; escala é a razão entre o desenho e a realidade.

Escala 1:50.000 significa que 1 cm no mapa representa 50.000 cm no terreno. Como 50.000 cm são 500 m, cada centímetro do mapa vale meio quilômetro. Uma distância de 3 cm no mapa equivale a 3 × 500 = 1.500 m, ou 1,5 km. Na escala 1:100, 5 cm no desenho são 500 cm, ou 5 m, no real.
"""
S[2]="""## 2. Proporção: duas razões iguais

Proporção é a igualdade entre duas razões: a/b = c/d. Em 3/4 = 15/20, os dois lados valem 0,75. Os termos de fora, a e d, são os extremos; os de dentro, b e c, são os meios. A propriedade fundamental diz que o produto dos meios é igual ao produto dos extremos: a × d = b × c. No exemplo, 3 × 20 = 4 × 15 = 60. É a conhecida “multiplicação em cruz”, e ela existe porque multiplicar os dois lados da igualdade por b e por d elimina os denominadores.

Para achar o termo que falta, aplique a propriedade. Em 5/x = 10/4, tem-se 10x = 5 × 4 = 20, logo x = 2. Em x/6 = 10/15, tem-se 15x = 60, logo x = 4.

Há uma segunda propriedade, muito usada em divisões: em uma proporção, a soma dos antecedentes está para a soma dos consequentes como cada antecedente para o seu consequente. Em a/b = c/d, vale (a + c)/(b + d) = a/b. Com 3/4 = 15/20, (3 + 15)/(4 + 20) = 18/24 = 3/4.
"""
S[3]="""## 3. Grandezas diretamente e inversamente proporcionais

Duas grandezas são diretamente proporcionais quando, dobrando uma, a outra também dobra; triplicando uma, a outra triplica. A razão entre elas é constante. Oito canetas a R$ 3,00 custam R$ 24,00, e 16 canetas custam R$ 48,00: a razão preço por caneta é sempre 3. O distanciamento acompanha o tempo, a velocidade se mantendo.

Duas grandezas são inversamente proporcionais quando, dobrando uma, a outra cai pela metade; triplicando uma, a outra cai à terça parte. Neste caso, o que se mantém constante é o produto. Se 4 guardas fazem uma vistoria em 6 horas, então 8 guardas, o dobro, fazem em 3 horas, a metade: 4 × 6 = 8 × 3 = 24 “guarda-horas” de trabalho. Velocidade e tempo, para uma mesma distância, são inversamente proporcionais.

A pergunta que decide o caso é: “se uma aumentar, a outra aumenta ou diminui?”. Se as duas crescem juntas, é direta; se uma cresce e a outra decresce, é inversa. Cuidado com o falso proporcional: a idade de uma pessoa e a sua altura crescem juntas, mas não de forma proporcional, porque a razão entre elas não é constante.

[[NOTA: Na direta, as razões são iguais (a/b = c/d). Na inversa, uma razão é igual ao inverso da outra (a/b = d/c), ou seja, o produto é constante.]]
"""
S[4]="""## 4. Divisão proporcional

Dividir um valor em partes proporcionais é repartir de modo que cada parte siga a razão dada. A ideia é achar a constante k que multiplica cada número do grupo. Dividir R$ 12.000,00 entre três guardas, proporcionalmente ao número de ocorrências que atenderam (5, 7 e 8), funciona assim: some os números, 5 + 7 + 8 = 20; divida o total pela soma, 12.000 ÷ 20 = 600, que é o valor de cada “unidade”; e multiplique: 5 × 600 = 3.000, 7 × 600 = 4.200 e 8 × 600 = 4.800. A soma volta a ser 12.000.

Na divisão inversamente proporcional, usam-se os inversos. Dividir 130 em partes inversamente proporcionais a 2 e 3 é dividir proporcionalmente a 1/2 e 1/3. Com denominador comum, 3/6 e 2/6, as razões são 3 e 2. Soma 5, constante 130 ÷ 5 = 26, partes 78 e 52. Note que a parte maior foi para o menor número, como pede a inversão.

Exemplo resolvido. Dividir 90 em partes proporcionais a 2 e 3. Soma 5; 90 ÷ 5 = 18; partes 36 e 54.
"""
S[6]="""## 6. Na rotina do guarda

- **Mapa e escala:** ao medir 8 cm entre dois pontos num mapa 1:25.000, a distância real é 8 × 250 = 2.000 m, ou 2 km.
- **Rateio de gratificação:** valor proporcional às ocorrências atendidas, como na divisão proporcional da seção 4.
- **Efetivo e tempo:** inversamente proporcionais; dobrar as equipes em uma vistoria reduz o tempo à metade, mantidas as condições.
- **Consumo e distância:** a viatura que faz 10 km por litro gasta 5 litros em 50 km, e o gasto é diretamente proporcional.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Montar a razão sem converter as unidades | Converta antes: 40 min e 2 h viram 40 e 120 |
| Inverter a ordem da razão | A razão “de A para B” é A/B |
| Tratar como direta uma grandeza inversa | Pergunte: aumentando uma, a outra aumenta ou diminui? |
| Dividir inversamente usando os próprios números | Use os inversos e leve a maior parte ao menor número |
| Errar a escala trocando cm por km | 1:50.000 é 1 cm para 500 m |
| Esquecer de conferir a soma das partes | As partes devem somar o total |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Razão | Quociente a/b; mesmas unidades |
| Escala | Desenho para real; 1:50.000 é 1 cm para 500 m |
| Proporção | a/b = c/d; a × d = b × c |
| Grandezas diretas | Razão constante; crescem juntas |
| Grandezas inversas | Produto constante; uma cresce, a outra decresce |
| Divisão proporcional | Soma das razões; k = total ÷ soma; parte = razão × k |
| Divisão inversa | Usa os inversos dos números |
"""
assert Fr(12,20)==Fr(3,5) and Fr(40,120)==Fr(1,3) and 3*500==1500 and 3*20==4*15 and 5*4==10*2 and 15*4==6*10
assert 4*6==8*3 and 12000//20==600 and (5*600,7*600,8*600)==(3000,4200,4800) and Fr(1,2)+Fr(1,3)==Fr(5,6) and (78+52,)==(130,) and 130//5*3==78 and 130//5*2==52
QR=[("Questão 1","Em um mapa de escala 1:25.000, a distância entre dois postos é de 8 cm. A distância real é de",["2 km.","200 m.","20 km.","3,2 km.","2,5 km."],0,"1 cm no mapa são 25.000 cm, ou 250 m. Então 8 cm são 8 × 250 = 2.000 m = 2 km."),
("Questão 2","Quatro guardas fazem uma vistoria em 6 horas. Mantido o ritmo, 6 guardas fariam a mesma vistoria em",["4 horas.","9 horas.","3 horas.","5 horas.","8 horas."],0,"Guardas e tempo são inversamente proporcionais: o produto é constante. 4 × 6 = 24 e 24 ÷ 6 = 4 horas."),
("Questão 3","Um prêmio de R$ 1.800,00 será dividido, de forma diretamente proporcional ao tempo de serviço, entre dois guardas de 4 e 5 anos de casa. O guarda de 5 anos receberá",["R$ 1.000,00","R$ 800,00","R$ 900,00","R$ 1.080,00","R$ 720,00"],0,"Soma 4 + 5 = 9; 1.800 ÷ 9 = 200 por unidade. O de 5 anos recebe 5 × 200 = 1.000; o de 4 anos, 800."),
("Questão 4","Dividir 130 em partes inversamente proporcionais a 2 e a 3 resulta em",["78 e 52.","52 e 78.","65 e 65.","80 e 50.","60 e 70."],0,"Usam-se os inversos 1/2 e 1/3, que valem 3/6 e 2/6, razões 3 e 2. Constante 130 ÷ 5 = 26: 3 × 26 = 78 e 2 × 26 = 52. A maior parte vai ao menor número.")]
QR=[(a,b,c,[2,4,0,3][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
assert 1800//9*5==1000 and 24//6==4
QRF=qr_md(QR,5)
t1="<strong>Gratificação por produtividade</strong><br><br>A Guarda Municipal de Vila Nova, cidade fictícia, destinou R$ 12.000,00 a uma gratificação por produtividade, a ser dividida entre três guardas, de forma diretamente proporcional ao número de ocorrências atendidas no mês: Ana atendeu 5, Bruno atendeu 7 e Carla atendeu 8."
t2="<strong>Planejamento de ronda</strong><br><br>Em um mapa de escala 1:50.000, o trajeto da ronda noturna mede 6 cm. Uma viatura percorre esse trajeto em 30 minutos, em velocidade constante. Para a ronda de reforço, o comando quer que o mesmo trajeto seja feito em 20 minutos."
tx={"mt4a":t1,"mt4b":t2}
assert Fr(6*500)==3000 and 3000/1000==3 and Fr(3)/Fr(1,2)==6 and Fr(3)/Fr(20,60)==9 and Fr(9)/Fr(3,2)==6
# n=1
q(1,"A razão entre 15 e 25, na forma irredutível, é",["3/5","5/3","15/10","3/25","1/10"],"15/25 = 3/5 (divisão por 5).")
q(1,"O valor de x na proporção 3/4 = x/20 é",["15","12","16","5","80/3"],"Meios e extremos: 4x = 3 × 20 = 60, logo x = 15.")
q(1,"Em um desenho de escala 1:100, um comprimento de 5 cm representa, na realidade,",["5 m","50 cm","500 m","0,5 m","50 m"],"5 × 100 = 500 cm = 5 m.")
q(1,"Uma viatura percorre 120 km em 2 horas. A velocidade média é",["60 km/h","240 km/h","120 km/h","30 km/h","6 km/h"],"Razão distância/tempo: 120 ÷ 2 = 60 km/h.")
q(1,"Oito canetas custam R$ 24,00. Dezesseis canetas, mesmo preço unitário, custam",["R$ 48,00","R$ 12,00","R$ 32,00","R$ 36,00","R$ 40,00"],"Grandezas diretas: dobra a quantidade, dobra o preço.")
q(1,"Quatro guardas fazem um trabalho em 6 horas. Oito guardas, no mesmo ritmo, fazem em",["3 horas","12 horas","24 horas","2 horas","4 horas"],"Inversa: o dobro de guardas leva à metade do tempo.")
q(1,"Dividir 100 em partes diretamente proporcionais a 1 e 4 resulta em",["20 e 80","25 e 75","10 e 40","50 e 50","40 e 60"],"Soma 5; 100 ÷ 5 = 20. Partes 20 e 80.")
q(1,"A razão entre 40 minutos e 2 horas é",["1/3","1/20","20","3","2/3"],"2 h = 120 min. 40/120 = 1/3.")
q(1,"O valor de x na proporção 5/x = 10/4 é",["2","8","5","12,5","0,5"],"10x = 20, x = 2.")
q(1,"A razão entre 3 km e 500 m é",["6","3/500","1/6","0,6","600"],"3 km = 3.000 m. 3.000 ÷ 500 = 6.")
q(1,"O valor de x na proporção x/6 = 10/15 é",["4","9","25","15","2,5"],"15x = 60, x = 4.")
q(1,"Em um grupo há 12 homens e 18 mulheres. A razão entre o número de homens e o total é",["2/5","2/3","3/5","4/9","3/2"],"Total 30. 12/30 = 2/5.")
q(1,"Duas grandezas são inversamente proporcionais quando",["o produto entre elas é constante.","a razão entre elas é constante.","a soma entre elas é constante.","a diferença entre elas é constante.","ambas crescem na mesma proporção."],"Dobrando uma, a outra cai pela metade: o produto se mantém.")
q(1,"A razão entre 20 e 80, escrita como porcentagem, é",["25%","20%","4%","40%","16%"],"20/80 = 1/4 = 25%.")
q(1,"Uma receita usa 2 copos de A para 3 copos de B. Com 12 copos de A, serão necessários de B",["18 copos","8 copos","12 copos","24 copos","15 copos"],"2/3 = 12/x, 2x = 36, x = 18.")
q(1,"Em um mapa de escala 1:50.000, 3 cm representam",["1,5 km","15 km","150 m","3 km","0,5 km"],"1 cm = 500 m; 3 cm = 1.500 m.")
q(1,"Dividir 90 em partes diretamente proporcionais a 2 e 3 resulta em",["36 e 54","30 e 60","45 e 45","40 e 50","18 e 72"],"Soma 5; 90 ÷ 5 = 18. Partes 36 e 54.")
q(1,"A razão entre 7 e 21 é",["1/3","3","7/3","1/7","2/3"],"7/21 = 1/3.")
q(1,"No texto da gratificação, a soma das ocorrências atendidas pelos três guardas é",["20","12","15","18","25"],"5 + 7 + 8 = 20.","mt4a")
q(1,"Segundo o texto, o trajeto de 6 cm no mapa 1:50.000 mede, na realidade,",["3 km","30 km","300 m","6 km","0,3 km"],"6 × 500 m = 3.000 m = 3 km.","mt4b")
# n=2
q(2,"Dividir R$ 12.000,00 em partes proporcionais a 5, 7 e 8 dá ao terceiro",["R$ 4.800,00","R$ 4.000,00","R$ 3.000,00","R$ 4.200,00","R$ 5.600,00"],"Soma 20; 12.000 ÷ 20 = 600. Terceiro: 8 × 600 = 4.800.")
q(2,"Quatro guardas vistoriam um prédio em 6 horas. Seis guardas, no mesmo ritmo, fariam em",["4 horas","9 horas","3 horas","5 horas","8 horas"],"4 × 6 = 24 e 24 ÷ 6 = 4.")
q(2,"Em um mapa 1:25.000, 8 cm correspondem a",["2 km","200 m","20 km","3,2 km","2,5 km"],"8 × 250 m = 2.000 m.")
q(2,"Dividir 130 em partes inversamente proporcionais a 2 e 3 dá",["78 e 52","52 e 78","65 e 65","80 e 50","60 e 70"],"Inversos 1/2 e 1/3: razões 3 e 2. 130 ÷ 5 = 26. Partes 78 e 52.")
q(2,"Um carro faz 12 km por litro. Para percorrer 150 km, são necessários",["12,5 litros","15 litros","10 litros","18 litros","8 litros"],"Direta: 150 ÷ 12 = 12,5 litros.")
q(2,"Uma viatura a 60 km/h faz um trajeto em 40 minutos. A 80 km/h, fará o mesmo trajeto em",["30 minutos","53 minutos","45 minutos","20 minutos","35 minutos"],"Velocidade e tempo são inversos: 60 × 40 = 80 × t, t = 30.")
q(2,"Se a razão entre dois números é 3/5 e sua soma é 40, o maior deles é",["25","15","24","30","20"],"Soma das razões 3 + 5 = 8; 40 ÷ 8 = 5. Maior: 5 × 5 = 25.")
q(2,"Uma planta tem escala 1:200. Um muro de 12 m aparece na planta com",["6 cm","60 cm","1,2 cm","24 cm","12 cm"],"12 m = 1.200 cm. 1.200 ÷ 200 = 6 cm.")
q(2,"Se x/y = 3/4 e x + y = 56, então x vale",["24","32","21","28","18"],"3 + 4 = 7; 56 ÷ 7 = 8. x = 3 × 8 = 24.")
q(2,"Dez operários constroem um muro em 12 dias. Em quantos dias 15 operários, no mesmo ritmo, constroem o mesmo muro?",["8","18","6","10","9"],"Inversa: 10 × 12 = 120; 120 ÷ 15 = 8.")
q(2,"Três quilos de tinta cobrem 45 m². Cinco quilos, mantido o rendimento, cobrem",["75 m²","27 m²","60 m²","90 m²","15 m²"],"Direta: 45 ÷ 3 = 15 m² por quilo; 5 × 15 = 75.")
q(2,"Assinale as grandezas diretamente proporcionais.",["Quantidade de combustível e distância percorrida, com consumo constante.","Número de guardas e tempo para concluir uma tarefa.","Velocidade e tempo para uma mesma distância.","Idade e altura de uma pessoa.","Número de torneiras e tempo para encher um tanque."],"Distância cresce na proporção do combustível. As demais são inversas ou não proporcionais.")
q(2,"Um prêmio de R$ 1.800,00 é dividido proporcionalmente a 4 e 5 anos de serviço. Quem tem 5 anos recebe",["R$ 1.000,00","R$ 800,00","R$ 900,00","R$ 1.080,00","R$ 720,00"],"9 partes, R$ 200,00 cada. 5 × 200 = 1.000.")
q(2,"A razão entre a idade de um pai e a do filho é 5/2. Se o pai tem 40 anos, o filho tem",["16","20","8","100","25"],"40/x = 5/2, x = 16.")
q(2,"Em uma maquete de escala 1:500, um prédio tem 8 cm de altura. A altura real é",["40 m","4 m","400 m","5 m","16 m"],"8 × 500 = 4.000 cm = 40 m.")
q(2,"Dividir 220 em partes proporcionais a 3, 4 e 4 dá à menor parte",["60","80","55","40","44"],"Soma 11; 220 ÷ 11 = 20. Menor: 3 × 20 = 60.")
q(2,"Uma torneira enche um tanque em 6 horas. Duas torneiras idênticas, juntas, enchem em",["3 horas","12 horas","4 horas","2 horas","8 horas"],"Inversa: dobro de torneiras, metade do tempo.")
q(2,"No texto da gratificação, Ana receberá",["R$ 3.000,00","R$ 2.400,00","R$ 4.200,00","R$ 3.600,00","R$ 2.000,00"],"12.000 ÷ 20 = 600; 5 × 600 = 3.000.","mt4a")
q(2,"Pelo texto, a velocidade da viatura na ronda de reforço, em relação à da ronda original, deve ser",["1,5 vez maior.","2 vezes maior.","igual.","0,5 vez maior.","3 vezes maior."],"Tempo inverso da velocidade: 30 ÷ 20 = 1,5.","mt4b")
q(2,"Considerando o texto, a velocidade da ronda original é de",["6 km/h","3 km/h","12 km/h","1,5 km/h","18 km/h"],"3 km em 30 min = 3 km em 0,5 h: 6 km/h.","mt4b")
# n=3
q(3,"Dividir 120 em partes inversamente proporcionais a 2, 3 e 6 dá à maior parte",["60","20","40","30","36"],"Inversos 1/2, 1/3 e 1/6 = 3/6, 2/6 e 1/6: razões 3, 2 e 1. Soma 6; 120 ÷ 6 = 20. Maior parte: 3 × 20 = 60.")
q(3,"Se 5 máquinas produzem 200 peças em 8 horas, 8 máquinas, no mesmo ritmo, produzem em 5 horas",["200 peças","125 peças","320 peças","160 peças","250 peças"],"Produção por máquina-hora: 200 ÷ 40 = 5. 8 × 5 × 5 = 200.")
q(3,"A razão entre dois números é 3/7 e a diferença entre eles é 24. O maior número é",["42","18","56","63","30"],"7 − 3 = 4; 24 ÷ 4 = 6. Maior: 7 × 6 = 42.")
q(3,"Um mapa tem escala 1:40.000. Uma praça quadrada, de 1,6 km de lado, aparece no mapa com lado de",["4 cm","2,5 cm","40 cm","16 cm","0,4 cm"],"1,6 km = 160.000 cm. 160.000 ÷ 40.000 = 4 cm.")
q(3,"Três sócios investiram R$ 2.000,00, R$ 3.000,00 e R$ 5.000,00 e dividiram o lucro proporcionalmente. Se o primeiro recebeu R$ 600,00, o lucro total foi de",["R$ 3.000,00","R$ 2.400,00","R$ 6.000,00","R$ 1.800,00","R$ 5.000,00"],"Razão 2:3:5, soma 10. O primeiro tem 2/10 do lucro. 600 ÷ (2/10) = 3.000.")
q(3,"Se A é diretamente proporcional a B e A = 12 quando B = 8, então A, quando B = 20, vale",["30","25","32","24","15"],"A/B = 12/8 = 1,5. A = 1,5 × 20 = 30.")
q(3,"Se A é inversamente proporcional a B e A = 12 quando B = 8, então A, quando B = 16, vale",["6","24","12","3","4"],"Produto constante: 12 × 8 = 96. A = 96 ÷ 16 = 6.")
q(3,"A razão entre o número de homens e o de mulheres de um grupo é 3/5. Se há 12 pessoas a mais de mulheres, o total de pessoas é",["48","30","60","36","72"],"5 − 3 = 2 partes valem 12; cada parte 6. Total 8 partes = 48.")
q(3,"Uma tinta é feita misturando A e B na razão 2 para 5. Para fazer 28 litros, são necessários de A",["8 litros","10 litros","12 litros","14 litros","20 litros"],"Soma 7 partes; 28 ÷ 7 = 4. A: 2 × 4 = 8.")
q(3,"Se x/3 = y/5 = z/7 e x + y + z = 90, então z vale",["42","18","30","35","27"],"Soma das razões 15; 90 ÷ 15 = 6. z = 7 × 6 = 42.")
q(3,"Em uma proporção, os extremos são 6 e 20 e um dos meios é 8. O outro meio é",["15","16","12","10","24"],"Meios × meios = extremos: 8 × m = 6 × 20 = 120, m = 15.")
q(3,"Quatro guardas, trabalhando 6 horas por dia, concluem uma vistoria em 5 dias. Seis guardas, 4 horas por dia, concluem em",["5 dias","4 dias","6 dias","3 dias","10 dias"],"Trabalho total: 4 × 6 × 5 = 120 guarda-horas. 6 × 4 = 24 por dia; 120 ÷ 24 = 5.")
q(3,"A idade de A está para a de B como 3 está para 4. Daqui a 10 anos, a soma das idades será 90. A idade atual de A é",["30","24","40","45","20"],"Soma atual 70, razões 3 e 4, constante 10. A tem 30.")
q(3,"Dois números estão na razão 4/9. Se o menor aumenta em 10 unidades, ficam iguais. O maior é",["18","8","20","36","12"],"9k − 4k = 10 → 5k = 10, k = 2. Maior 18.")
q(3,"Um prêmio é dividido em partes inversamente proporcionais ao número de faltas de dois guardas, que tiveram 2 e 6 faltas. Quem faltou 2 vezes recebe, do total,",["3/4","1/4","2/3","1/3","1/2"],"Inversos 1/2 e 1/6 = 3/6 e 1/6. O primeiro fica com 3/4.")
q(3,"Segundo o texto, o trajeto de 6 cm será feito na ronda de reforço a uma velocidade de",["9 km/h","6 km/h","3 km/h","12 km/h","4,5 km/h"],"3 km em 20 min = 3 km em 1/3 h: 9 km/h.","mt4b")
q(3,"Segundo o texto, se Bruno atendesse 3 ocorrências a mais, com a mesma gratificação dividida entre os três, Ana passaria a receber",["R$ 2.608,70, aproximadamente.","R$ 3.000,00","R$ 2.400,00","R$ 2.857,14, aproximadamente.","R$ 3.200,00"],"Ocorrências: 5, 10, 8; soma 23. 12.000 ÷ 23 × 5 ≈ 2.608,70.","mt4a")
q(3,"Dividir 310 em partes proporcionais a 1/2, 1/3 e 1/5 dá à maior parte",["150","100","60","120","130"],"Com denominador 30: 15/30, 10/30, 6/30, razões 15, 10 e 6. Soma 31; 310 ÷ 31 = 10. Maior: 15 × 10 = 150.")
q(3,"A velocidade da viatura A é 3/4 da velocidade da B. Se B faz um percurso em 6 horas, A fará o mesmo percurso em",["8 horas","4,5 horas","9 horas","7 horas","10 horas"],"Velocidade e tempo são inversos. Tempo de A = 6 ÷ (3/4) = 8 horas.")
q(3,"A razão entre as velocidades de dois ciclistas é 5/3. No mesmo tempo, o mais rápido percorre 40 km. O outro percorre",["24 km","66,7 km","30 km","20 km","25 km"],"5/3 = 40/x, 5x = 120, x = 24.")
assert 120//6*3==60 and Fr(15,31)*310==150 and Fr(6)/Fr(3,4)==8 and 3*40==5*24
QQ=fechar(); assert len(QQ)==60, len(QQ)
code,svg=mapa("Razão e proporção: da comparação à divisão",[
 ("razao","Razão",["quociente a/b","mesmas unidades","escala, velocidade, densidade"],"seção 1"),
 ("prop","Proporção",["a/b = c/d","meios × meios = extremos","soma dos termos"],"seção 2"),
 ("diretas","Grandezas diretas",["crescem juntas","razão constante","preço × quantidade"],"seção 3"),
 ("inversas","Grandezas inversas",["uma cresce, outra decresce","produto constante","velocidade × tempo"],"seção 3"),
 ("divisao","Divisão proporcional",["soma das razões","k = total ÷ soma","inversa: usa os inversos"],"seção 4"),
 ("escala","Escala",["1:50.000 = 1 cm para 500 m","converter antes","mapa e planta"],"seção 1")],
 "Na prova: pergunte se as grandezas crescem juntas ou em sentidos opostos")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"A razão é a peça básica; a proporção iguala duas razões; as grandezas e a divisão proporcional usam as duas.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 11; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.")
revisao("mt-4","Razão e proporção",QQ,list(tx),
 cobertura=["Recorte do edital: “grandezas diretamente e inversamente proporcionais”. Cobertos: razão, escala, proporção e suas propriedades, grandezas direta e inversamente proporcionais, divisão proporcional direta e inversa."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","Cálculos conferidos por código; redação para revisão humana. Uma questão (rateio entre 23 ocorrências) usa valor aproximado em reais: conferir."],
 fontes_conferidas=["Cálculos: assert no script conteudo/mt4/mt4.py."])
gravar("mt-4",aula_html,banco("mt-4",QQ),tx)
