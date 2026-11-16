import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
import math
LEAD="Noções de geometria reúne o que a prova cobra de forma, ângulo, perímetro, área, volume, o teorema de Pitágoras e o teorema de Tales. O padrão das questões é sempre o mesmo: uma figura simples, um dado de medida e a pergunta por outra medida. O caminho é identificar a figura, escolher a fórmula certa e cuidar das unidades. Esta aula explica de onde vem cada fórmula, porque quem entende a origem esquece menos."
S={}
S[1]="""## 1. Ângulos

Ângulo é a abertura entre duas semirretas que partem do mesmo ponto. Mede-se em graus: uma volta completa tem 360°, meia volta tem 180° (ângulo raso) e um quarto de volta tem 90° (ângulo reto). Ângulo menor que 90° é agudo; maior que 90° e menor que 180° é obtuso. Dois ângulos são complementares quando somam 90° e suplementares quando somam 180°.

Duas retas que se cruzam formam ângulos opostos pelo vértice, que são iguais. Quando uma reta corta duas paralelas, formam-se pares de ângulos iguais (correspondentes e alternos) e pares que somam 180° (colaterais). A soma dos ângulos internos de um triângulo é sempre 180°, e a de um quadrilátero é 360°. Em um triângulo com ângulos de 50° e 60°, o terceiro é 180° − 110° = 70°.
"""
S[2]="""## 2. Perímetro e área das figuras planas

Perímetro é o comprimento do contorno de uma figura: a soma dos lados. Área é a medida da superfície, em unidades quadradas. A ideia que sustenta as fórmulas é a de ladrilhar: a área do retângulo é o número de quadradinhos que cabem nele, base vezes altura. Um retângulo de 8 m por 5 m tem perímetro 2 × (8 + 5) = 26 m e área 8 × 5 = 40 m².

O paralelogramo tem a mesma área de um retângulo de mesma base e altura: base × altura. O triângulo é metade de um paralelogramo, por isso a área é base × altura ÷ 2. O trapézio tem área (base maior + base menor) × altura ÷ 2. O losango tem área diagonal maior × diagonal menor ÷ 2. O quadrado de lado L tem perímetro 4L e área L<sup>2</sup>.

O círculo de raio r tem comprimento C = 2πr e área A = πr<sup>2</sup>. Com π ≈ 3,14, um círculo de raio 5 m tem comprimento 2 × 3,14 × 5 = 31,4 m e área 3,14 × 25 = 78,5 m². Quando a prova pede o resultado “em função de π”, deixe o π na resposta: a área é 25π m².

Exemplo resolvido. Um terreno trapezoidal tem bases de 20 m e 12 m e altura de 10 m. Sua área é (20 + 12) × 10 ÷ 2 = 160 m².
"""
S[3]="""## 3. Teorema de Pitágoras

Em todo triângulo retângulo, o quadrado da hipotenusa (o lado oposto ao ângulo reto, o maior) é igual à soma dos quadrados dos catetos: a<sup>2</sup> = b<sup>2</sup> + c<sup>2</sup>. A ideia visual é que, se se desenham quadrados sobre os três lados, a área do quadrado maior é igual à soma das áreas dos dois menores.

Um triângulo com catetos 3 e 4 tem hipotenusa √(9 + 16) = √25 = 5. Os trios de números inteiros que satisfazem a relação, como 3, 4, 5; 5, 12, 13; 8, 15, 17 e seus múltiplos (6, 8, 10), valem decorar, porque aparecem sempre. A diagonal de um quadrado de lado L é L√2, porque é a hipotenusa de um triângulo de catetos L e L. A diagonal de um retângulo de 6 m por 8 m é √(36 + 64) = 10 m.

Exemplo resolvido. Uma escada de 5 m apoia-se numa parede, com a base a 3 m dela. Que altura ela alcança? A escada é a hipotenusa; a base e a altura são catetos: altura = √(25 − 9) = √16 = 4 m.
"""
S[4]="""## 4. Teorema de Tales e semelhança

O teorema de Tales diz que, quando retas paralelas cortam duas retas transversais, os segmentos que elas determinam são proporcionais. Se três paralelas cortam uma transversal em segmentos de 4 e 6, e cortam outra em segmentos de 8 e x, então 4/6 = 8/x, e x = 12.

A ideia vem da semelhança: figuras semelhantes têm o mesmo formato e lados proporcionais. Um triângulo cortado por uma reta paralela a um dos lados forma outro triângulo, semelhante ao primeiro, e vale a proporção entre os lados correspondentes. Isso explica a sombra: se uma estaca de 2 m projeta sombra de 3 m, no mesmo instante um poste projetando sombra de 12 m tem altura x, com x/2 = 12/3, e x = 8 m.

Na semelhança, a razão entre as áreas é o quadrado da razão entre os lados. Se um triângulo tem lados com o dobro do outro, tem área quatro vezes maior.
"""
S[5]="""## 5. Volume dos sólidos

Volume é a medida do espaço ocupado, e a ideia é a de empilhar: o volume de um prisma é a área da base vezes a altura. O paralelepípedo (a caixa) de 6 m por 4 m por 3 m tem volume 6 × 4 × 3 = 72 m³. O cubo de aresta a tem volume a<sup>3</sup>. O cilindro de raio r e altura h é um prisma de base circular, com volume πr<sup>2</sup>h. A pirâmide e o cone ocupam um terço do prisma e do cilindro de mesma base e altura: V = (área da base × altura) ÷ 3.

Lembre a relação com a capacidade: 1 m³ = 1.000 litros. Um reservatório cilíndrico de raio 1 m e altura 2 m tem volume 3,14 × 1 × 2 = 6,28 m³, ou 6.280 litros.

Os poliedros têm uma regra de contagem, a relação de Euler: V − A + F = 2, em que V é o número de vértices, A o de arestas e F o de faces. No cubo, 8 − 12 + 6 = 2.
"""
S[7]="""## 7. Na rotina do guarda

- **Cercamento:** o perímetro dá a quantidade de cerca; a área, a quantidade de piso ou de grama.
- **Alcance de escada ou câmera:** a distância é a hipotenusa de um triângulo retângulo.
- **Sombras e alturas:** a semelhança de triângulos mede a altura de postes e prédios sem subir neles.
- **Reservatórios:** o volume do cilindro dá a capacidade, em m³ e em litros.
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Esquecer o ÷ 2 na área do triângulo | Triângulo é metade do retângulo de mesma base e altura |
| Confundir perímetro com área | Perímetro é contorno (m); área é superfície (m²) |
| Usar o diâmetro no lugar do raio | A fórmula usa o raio, a metade do diâmetro |
| Somar em vez de subtrair em Pitágoras, quando falta um cateto | Cateto<sup>2</sup> = hipotenusa<sup>2</sup> − outro cateto<sup>2</sup> |
| Aplicar Tales sem paralelas | A proporção só vale se as retas cortadas forem paralelas |
| Esquecer o ÷ 3 no volume de pirâmide e cone | Pirâmide e cone são um terço do prisma e do cilindro |
| Misturar unidades (cm e m) | Converta antes |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Soma dos ângulos | Triângulo 180°; quadrilátero 360° |
| Retângulo | Perímetro 2(b + h); área b × h |
| Triângulo | Área b × h ÷ 2 |
| Trapézio | (B + b) × h ÷ 2 |
| Círculo | C = 2πr; A = πr² |
| Pitágoras | a² = b² + c² (hipotenusa a) |
| Tales | Paralelas cortando transversais: segmentos proporcionais |
| Volume | Prisma e cilindro: base × altura; pirâmide e cone: ÷ 3 |
"""
assert 180-110==70 and 2*(8+5)==26 and 8*5==40 and Fr(32*10,2)==160 and math.isclose(math.hypot(3,4),5) and math.isclose(math.hypot(6,8),10)
assert math.isclose(math.sqrt(25-9),4) and Fr(4,6)==Fr(8,12) and Fr(12*2,3)==8 and 6*4*3==72 and 8-12+6==2 and math.isclose(3.14*1*2,6.28)
QR=[("Questão 1","Um terreno em forma de trapézio tem bases de 20 m e 12 m e altura de 10 m. Sua área é",["160 m²","320 m²","240 m²","120 m²","200 m²"],0,"(20 + 12) × 10 ÷ 2 = 160 m²."),
("Questão 2","Uma escada de 5 m está apoiada em uma parede, com a base a 3 m da parede. A altura que a escada atinge é",["4 m","2 m","8 m","5,8 m","3 m"],0,"A escada é a hipotenusa: altura<sup>2</sup> = 25 − 9 = 16, altura = 4."),
("Questão 3","Uma estaca de 2 m projeta uma sombra de 3 m. No mesmo instante, um poste projeta uma sombra de 12 m. A altura do poste é",["8 m","18 m","6 m","10 m","12 m"],0,"Triângulos semelhantes: x/2 = 12/3, x = 8."),
("Questão 4","Um reservatório cilíndrico tem raio de 1 m e altura de 2 m (use π = 3,14). Sua capacidade é de aproximadamente",["6.280 litros","3.140 litros","628 litros","12.560 litros","6,28 litros"],0,"V = π r² h = 3,14 × 1 × 2 = 6,28 m³ = 6.280 litros.")]
QR=[(a,b,c,[1,3,0,4][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
QRF=qr_md(QR,6)
t1="<strong>Reforma da base da Guarda</strong><br><br>O pátio da base da Guarda Municipal de Vila Nova, cidade fictícia, é retangular, com 30 m por 20 m. Será coberto por uma cobertura em forma de telhado, cuja estrutura apoia-se em dois pontos, a 4 m de distância um do outro, em uma parede de 3 m de altura. Os projetistas querem saber o comprimento de uma viga inclinada que liga o topo da parede ao chão, a 4 m dela."
t2="<strong>Caixa-d'água do quartel</strong><br><br>A caixa-d'água do quartel é um cilindro com 2 m de diâmetro e 3 m de altura. Considere π = 3,14."
tx={"mt10a":t1,"mt10b":t2}
assert 30*20==600 and math.isclose(math.hypot(3,4),5) and 3.14*1*1*3==9.42
# n=1
qv(1,"Em um triângulo, dois ângulos medem 50° e 60°. O terceiro mede","{}°",70,[110,60,80,90],"180 − 110 = 70.")
qv(1,"O perímetro de um retângulo de 8 m por 5 m é","{} m",26,[40,13,18,35],"2 × (8 + 5) = 26.")
qv(1,"A área de um retângulo de 8 m por 5 m é","{} m²",40,[26,13,45,80],"8 × 5 = 40.")
qv(1,"A área de um triângulo de base 10 m e altura 6 m é","{} m²",30,[60,16,32,15],"10 × 6 ÷ 2 = 30.")
qv(1,"A área de um quadrado de lado 7 m é","{} m²",49,[28,14,35,56],"7 × 7.")
qv(1,"O perímetro de um quadrado de lado 7 m é","{} m",28,[49,14,21,35],"4 × 7.")
qv(1,"A hipotenusa de um triângulo retângulo de catetos 3 e 4 mede","{}",5,[7,6,12,25],"√(9 + 16) = 5.")
qv(1,"Dois ângulos complementares somam","{}°",90,[180,360,45,100],"Complementares somam 90°.")
qv(1,"Dois ângulos suplementares somam","{}°",180,[90,360,270,100],"Suplementares somam 180°.")
qv(1,"A soma dos ângulos internos de um triângulo é","{}°",180,[90,360,270,120],"Sempre 180°.")
qv(1,"O volume de uma caixa de 6 m por 4 m por 3 m é","{} m³",72,[13,24,36,144],"6 × 4 × 3.")
qv(1,"O volume de um cubo de aresta 3 m é","{} m³",27,[9,18,12,81],"3 × 3 × 3.")
qv(1,"O raio de um círculo de diâmetro 10 m é","{} m",5,[20,10,2,25],"O raio é a metade do diâmetro.")
qv(1,"A soma dos ângulos internos de um quadrilátero é","{}°",360,[180,270,540,90],"Sempre 360°.")
qv(1,"Um ângulo reto mede","{}°",90,[45,180,60,360],"Ângulo reto = 90°.")
q(1,"Um ângulo de 120° é classificado como",["obtuso.","agudo.","reto.","raso.","complementar de um ângulo de 60°."],"Entre 90° e 180°, é obtuso.")
q(1,"A relação de Euler para poliedros convexos é",["V − A + F = 2","V + A + F = 2","V − A − F = 2","V + A − F = 2","V × A = F"],"Vértices menos arestas mais faces é 2: no cubo, 8 − 12 + 6 = 2.")
qv(1,"A área de um retângulo de base 12 m e altura 3 m é","{} m²",36,[15,30,24,72],"12 × 3.")
q(1,"Pelo texto, a viga inclinada é a hipotenusa de um triângulo retângulo de catetos",["3 m e 4 m.","3 m e 30 m.","4 m e 20 m.","30 m e 20 m.","4 m e 5 m."],"A parede tem 3 m de altura e a base da viga fica a 4 m dela.","mt10a")
qv(1,"Pelo texto, o raio da caixa-d'água é","{} m",1,[2,3,4,0.5],"Diâmetro 2 m, raio 1 m.","mt10b")
# n=2
qv(2,"A área de um trapézio de bases 20 m e 12 m e altura 10 m é","{} m²",160,[320,240,120,200],"(20 + 12) × 10 ÷ 2.")
qv(2,"Uma escada de 5 m, com a base a 3 m da parede, alcança a altura de","{} m",4,[2,8,5.8,3],"25 − 9 = 16; √16 = 4.")
qv(2,"A diagonal de um retângulo de 6 m por 8 m mede","{} m",10,[14,7,48,100],"√(36 + 64) = 10.")
qv(2,"Uma estaca de 2 m projeta sombra de 3 m. No mesmo instante, um poste projeta sombra de 12 m. O poste tem","{} m",8,[18,6,10,12],"x/2 = 12/3.")
qv(2,"Se 4/6 = 8/x, então x vale","{}",12,[16,10,6,9],"4x = 48.")
q(2,"A área de um círculo de raio 5 m, com π = 3,14, é",["78,5 m²","31,4 m²","157 m²","15,7 m²","25 m²"],"3,14 × 25 = 78,5.")
q(2,"O comprimento de uma circunferência de raio 5 m, com π = 3,14, é",["31,4 m","78,5 m","15,7 m","157 m","10 m"],"2 × 3,14 × 5 = 31,4.")
qv(2,"Um reservatório cilíndrico de raio 1 m e altura 2 m, com π = 3,14, comporta","{} litros",6280,[3140,628,12560,62800],"3,14 × 1 × 2 = 6,28 m³ = 6.280 L.")
qv(2,"O volume de uma pirâmide de base quadrada de 6 m de lado e altura 5 m é","{} m³",60,[180,30,90,120],"(36 × 5) ÷ 3 = 60.")
qv(2,"A diagonal de um quadrado de lado 4 m, com √2 ≈ 1,4, mede aproximadamente","{} m",5.6,[8,4.4,2.8,16],"4√2 ≈ 5,6.")
q(2,"Dois triângulos semelhantes têm razão de semelhança 2. A razão entre suas áreas é",["4","2","8","1/2","6"],"A razão entre áreas é o quadrado da razão entre lados.")
qv(2,"A área de um losango de diagonais 10 m e 6 m é","{} m²",30,[60,16,32,15],"10 × 6 ÷ 2 = 30.")
qv(2,"Um triângulo isósceles tem ângulos da base de 50° cada. O ângulo do vértice mede","{}°",80,[50,130,100,40],"180 − 100 = 80.")
qv(2,"Um terreno retangular de 30 m por 20 m será cercado por três voltas de arame. O comprimento total de arame é","{} m",300,[100,150,200,600],"Perímetro 100 m; três voltas: 300 m.")
qv(2,"Um poste de 5 m apoia-se, com cabo de aço, em um ponto a 12 m de sua base. O cabo mede","{} m",13,[17,7,11,15],"√(25 + 144) = 13.")
qv(2,"Uma caixa-d'água em forma de cubo de 1,5 m de aresta tem capacidade de","{} litros",3375,[2250,3750,3000,4500],"1,5³ = 3,375 m³ = 3.375 L.")
qv(2,"Dois ângulos são suplementares e um deles é o dobro do outro. O maior mede","{}°",120,[60,90,100,135],"x + 2x = 180; x = 60; maior 120.")
qv(2,"Pelo texto, a viga inclinada, em metros, mede","{} m",5,[7,4,3,25],"√(9 + 16) = 5.","mt10a")
qv(2,"Pelo texto, a área do pátio é","{} m²",600,[100,50,300,1200],"30 × 20.","mt10a")
qv(2,"Pelo texto, a área da base circular da caixa-d'água é","{} m²",3.14,[6.28,9.42,12.56,1],"π × r² = 3,14 × 1.","mt10b")
# n=3
qv(3,"Um quadrado tem diagonal de 10 m. Sua área é","{} m²",50,[100,25,75,20],"Área = diagonal² ÷ 2 = 50.")
qv(3,"Um triângulo retângulo tem hipotenusa 13 m e um cateto 5 m. Seu outro cateto e sua área são, respectivamente,","{} m e 30 m²",12,[8,10,18,6],"√(169 − 25) = 12; área 5 × 12 ÷ 2 = 30.")
qv(3,"Dobrando-se o raio de um círculo, sua área","fica multiplicada por {}",4,[2,8,3,6],"A área depende de r².")
qv(3,"Dobrando-se a aresta de um cubo, seu volume","fica multiplicado por {}",8,[2,4,6,16],"O volume depende de a³.")
qv(3,"Em um trapézio retângulo, as bases medem 12 m e 8 m e o lado inclinado mede 5 m. A altura é","{} m",3,[4,5,1,2],"Diferença das bases 4; altura = √(25 − 16) = 3.")
qv(3,"Um cone de raio 3 m e altura 4 m, com π = 3,14, tem volume de aproximadamente","{} m³",37.68,[113.04,12.56,75.36,18.84],"V = π r² h ÷ 3 = 3,14 × 9 × 4 ÷ 3 = 37,68.")
qv(3,"Um prédio projeta sombra de 30 m no mesmo instante em que uma pessoa de 1,8 m projeta sombra de 2,4 m. A altura do prédio é","{} m",22.5,[24,18,32,20],"x/1,8 = 30/2,4; x = 22,5.")
qv(3,"A diagonal de um paralelepípedo de arestas 2, 3 e 6 mede","{}",7,[11,5,9,6],"√(4 + 9 + 36) = 7.")
qv(3,"Um poliedro convexo tem 6 vértices e 9 arestas. O número de faces é","{}",5,[3,4,6,7],"6 − 9 + F = 2, F = 5.")
qv(3,"Um quadrado e um triângulo equilátero têm o mesmo perímetro, 24 m. O lado do triângulo supera o do quadrado em","{} m",2,[1,3,4,0],"Quadrado: 6; triângulo: 8; diferença 2.")
qv(3,"A área do anel entre dois círculos concêntricos de raios 5 m e 3 m, com π = 3,14, é","{} m²",50.24,[25.12,78.5,100.48,12.56],"3,14 × (25 − 9) = 50,24.")
qv(3,"Em uma proporção de Tales, três paralelas determinam em uma transversal segmentos de 3 e 5 e, em outra, de x e 15. O valor de x é","{}",9,[6,25,12,10],"3/5 = x/15, x = 9.")
qv(3,"Uma folha retangular de 20 cm por 30 cm é dobrada ao meio no sentido do maior lado. A área da folha dobrada é","{} cm²",300,[600,150,200,450],"Metade de 600.")
qv(3,"Um tanque tem forma de paralelepípedo com base de 2 m por 3 m. Para encher 9.000 litros, a altura da água deve ser","{} m",1.5,[1,2,3,0.5],"9 m³ ÷ 6 m² = 1,5.")
qv(3,"Em um triângulo, o maior ângulo é o triplo do menor e o terceiro mede 40°. O menor mede","{}°",35,[20,40,28,45],"x + 3x + 40 = 180; x = 35.")
qv(3,"Um retângulo tem perímetro de 36 m e comprimento igual ao dobro da largura. A área é","{} m²",72,[36,48,64,81],"l = 6, c = 12.")
qv(3,"Um círculo tem comprimento de 31,4 m (π = 3,14). Sua área é","{} m²",78.5,[157,31.4,25,314],"r = 5; área 3,14 × 25 = 78,5.")
qv(3,"O volume de um cilindro de raio 2 m e altura 5 m, com π = 3,14, é","{} m³",62.8,[31.4,125.6,20.9,15.7],"3,14 × 4 × 5 = 62,8.")
qv(3,"Pelo texto, se a viga fosse ligada ao chão a 12 m da parede de 5 m, mediria","{} m",13,[17,7,11,15],"√(25 + 144) = 13.","mt10a")
qv(3,"Pelo texto, o volume da caixa-d'água, em litros, é de aproximadamente","{} litros",9420,[3140,6280,4710,18840],"3,14 × 1² × 3 = 9,42 m³ = 9.420 L.","mt10b")
assert math.isclose(math.sqrt(169-25),12) and math.isclose(3.14*9*4/3,37.68) and math.isclose(math.sqrt(4+9+36),7)
assert math.isclose(3.14*(25-9),50.24) and 9/6==1.5 and 6-9+5==2 and 1.8*30/2.4==22.5
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("Geometria: da figura à fórmula",[
 ("ang","Ângulos",["reto 90°, raso 180°","triângulo 180°","quadrilátero 360°"],"seção 1"),
 ("area","Perímetro e área",["retângulo b × h","triângulo b × h ÷ 2","círculo πr²"],"seção 2"),
 ("pit","Pitágoras",["a² = b² + c²","3, 4, 5","diagonal do quadrado L√2"],"seção 3"),
 ("tales","Tales e semelhança",["paralelas: segmentos proporcionais","sombra e altura","área: razão ao quadrado"],"seção 4"),
 ("vol","Volume",["prisma: base × altura","pirâmide e cone: ÷ 3","1 m³ = 1.000 L"],"seção 5"),
 ("euler","Poliedros",["V − A + F = 2","cubo: 8, 12, 6","contagem de faces"],"seção 5")],
 "Na prova: identifique a figura, converta as unidades e confira o ÷ 2 e o ÷ 3")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"Ângulos, áreas e volumes dão as medidas; Pitágoras e Tales ligam medidas entre si.","Fontes: Edital 02/2026, Anexo I. Referências de base: Dolce e Pompeo, <em>Fundamentos de Matemática Elementar</em>, v. 9 (Geometria plana) e v. 10 (Geometria espacial); Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula.")
revisao("mt-10","Noções de geometria",QQ,list(tx),
 cobertura=["Recorte do edital: forma, ângulos, área, perímetro, volume, Pitágoras e Tales. Cobertos: ângulos, perímetro e área de polígonos e círculo, Pitágoras, Tales e semelhança, volumes de prisma, cilindro, pirâmide e cone, relação de Euler."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","A aula não traz desenhos das figuras (o painel só tem o mapa do assunto). Para esta matéria, vale incluir figuras em SVG numa revisão posterior.","Gabaritos conferidos em parte por código (math)."],
 fontes_conferidas=[])
gravar("mt-10",aula_html,banco("mt-10",QQ),tx)
