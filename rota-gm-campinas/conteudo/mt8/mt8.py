import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
LEAD="Grandezas e medidas é o assunto das conversões: metros e quilômetros, minutos e horas, litros e metros cúbicos, gramas e toneladas. A Vunesp cobra três habilidades: converter unidades de comprimento, superfície, volume, capacidade, massa e tempo; operar com horas e minutos, que não seguem o sistema decimal; e usar as conversões dentro de problemas de área, volume e velocidade. A conta é sempre simples, e o erro típico é o de mover a vírgula o número errado de casas."
S={}
S[1]="""## 1. O sistema métrico e o comprimento

As unidades do sistema métrico seguem a escada dos prefixos: quilo (mil), hecto (cem), deca (dez), a unidade, deci (um décimo), centi (um centésimo) e mili (um milésimo). No comprimento, a unidade é o metro. Cada degrau da escada vale 10: para ir de uma unidade maior para uma menor, multiplica-se por 10 a cada degrau, ou seja, a vírgula anda para a direita; para ir de uma menor para uma maior, divide-se, e a vírgula anda para a esquerda.

Assim, 3,5 km são 3,5 × 1.000 = 3.500 m, porque se descem três degraus (km, hm, dam, m). E 250 cm são 250 ÷ 100 = 2,5 m, porque se sobem dois degraus. Um jeito de não errar é perguntar se o número deve crescer ou diminuir: o mesmo comprimento, medido numa unidade menor, dá um número maior.
"""
S[2]="""## 2. Superfície: o degrau vale 100

Na área, a escada anda de 100 em 100, porque a área é comprimento vezes comprimento: 1 m = 100 cm, então 1 m² = 100 × 100 = 10.000 cm². Por isso, 4 m² são 40.000 cm². Também, 1 km² = 1.000 × 1.000 = 1.000.000 m².

Para terrenos há unidades agrárias. O are vale 100 m² (um quadrado de 10 m por 10 m) e o hectare (ha) vale 10.000 m² (um quadrado de 100 m por 100 m). Um km² tem 100 ha. Um terreno de 60.000 m² tem 6 ha.

Exemplo resolvido. Uma sala retangular de 5 m por 4 m tem área de 20 m². Em centímetros quadrados, a área é 20 × 10.000 = 200.000 cm². Se o piso for coberto por ladrilhos de 20 cm por 20 cm, cada um cobre 400 cm², e são necessários 200.000 ÷ 400 = 500 ladrilhos.
"""
S[3]="""## 3. Volume e capacidade: o degrau vale 1.000

No volume, a escada anda de 1.000 em 1.000, porque é comprimento vezes comprimento vezes comprimento: 1 m³ = 100 × 100 × 100 = 1.000.000 cm³. A capacidade, medida em litros, se liga ao volume por uma relação que vale decorar: 1 litro é o volume de um cubo de 10 cm de aresta, ou seja, 1 dm³. Daí vêm 1 m³ = 1.000 dm³ = 1.000 litros, e 1 cm³ = 1 mL.

Uma caixa de 40 cm por 30 cm por 20 cm tem volume de 24.000 cm³, ou 24 litros. Uma piscina de 8 m por 4 m e 1,5 m de profundidade tem 48 m³, ou 48.000 litros. Um reservatório de 12 m³ guarda 12.000 litros e, se o consumo é de 400 litros por dia, dura 30 dias.

Para a capacidade, os prefixos seguem a escada de 10 em 10: 1 litro tem 1.000 mL, e 1 hectolitro (hL) tem 100 litros.
"""
S[4]="""## 4. Massa

A unidade de massa é o grama, e o quilograma vale 1.000 g. A tonelada vale 1.000 kg. Então 1,5 kg são 1.500 g, 800 g são 0,8 kg e 1,2 t são 1.200 kg. Um litro de água pesa, aproximadamente, 1 kg; por isso, um tanque de 3 m³ cheio de água tem massa de 3.000 kg, ou 3 t.
"""
S[5]="""## 5. Tempo: o sistema que não é decimal

O tempo não segue a escada de 10: 1 hora tem 60 minutos, 1 minuto tem 60 segundos e 1 dia tem 24 horas. Por isso, 2 h 30 min valem 150 minutos, e não 2,3 hora. Para passar de minutos a horas decimais, divide-se por 60: 90 min = 1,5 h, e 45 min = 0,75 h. Para passar de horas decimais a horas e minutos, multiplica-se a parte decimal por 60: 5,25 h = 5 h + 0,25 × 60 min = 5 h 15 min.

Na soma, quando os minutos passam de 59, “vai um” para as horas. Em 2 h 40 min + 1 h 35 min, os minutos são 40 + 35 = 75, que dão 1 h 15 min; as horas são 2 + 1 + 1 = 4. O total é 4 h 15 min. Na subtração, quando faltam minutos, empresta-se 1 hora. Em 5 h 10 min − 2 h 45 min, não dá para tirar 45 de 10; empresta-se 1 hora, e a conta vira 4 h 70 min − 2 h 45 min = 2 h 25 min.

Para a duração entre dois horários que cruzam a meia-noite, calcule até 24h e some o resto. De 22h45 a 6h15 do dia seguinte: até 24h são 1 h 15 min, e mais 6 h 15 min dão 7 h 30 min.

A velocidade liga distância e tempo e exige cuidado com a unidade. Para passar de km/h para m/s, divide-se por 3,6: 72 km/h = 20 m/s e 36 km/h = 10 m/s. Uma viatura a 18 km/h faz 3,6 km em 3,6 ÷ 18 = 0,2 h, ou 12 minutos.
"""
S[7]="""## 7. Na rotina do guarda

- **Relatório de distância:** o hodômetro e o mapa usam quilômetros e metros; converter antes de comparar.
- **Cobertura de terreno:** a área de um parque em hectares vira m² para dividir o patrulhamento por guarda.
- **Escala de plantão:** de 22h45 a 6h15 são 7 h 30 min, não 8 horas nem 7,3 horas.
- **Reservatórios e viaturas-pipa:** a capacidade vem em m³ ou em litros e precisa ser uniformizada.
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Usar o degrau de 10 na área ou no volume | Área anda de 100 em 100; volume, de 1.000 em 1.000 |
| Tratar 2 h 30 min como 2,3 h | Converta: 30 min = 0,5 h, logo 2,5 h |
| Confundir hectare e are | 1 ha = 10.000 m²; 1 are = 100 m² |
| Esquecer 1 m³ = 1.000 L | 1 dm³ = 1 L |
| Converter km/h em m/s multiplicando por 3,6 | Divide por 3,6 |
| Esquecer de emprestar 1 hora na subtração | 60 min vêm da hora emprestada |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Comprimento | Degrau de 10: km, hm, dam, m, dm, cm, mm |
| Área | Degrau de 100: 1 m² = 10.000 cm² |
| Hectare e are | 1 ha = 10.000 m²; 1 are = 100 m² |
| Volume | Degrau de 1.000: 1 m³ = 1.000.000 cm³ |
| Capacidade | 1 L = 1 dm³; 1 m³ = 1.000 L; 1 cm³ = 1 mL |
| Massa | 1 kg = 1.000 g; 1 t = 1.000 kg |
| Tempo | 60 min = 1 h; 60 s = 1 min |
| Velocidade | km/h ÷ 3,6 = m/s |
"""
assert Fr('3.5')*1000==3500 and 250/100==2.5 and 4*10000==40000 and 20*10000==200000 and 200000//400==500
assert 40*30*20==24000 and 8*4*Fr('1.5')==48 and 12000//400==30 and 2*60+30==150 and Fr(90,60)==Fr('1.5')
assert 40+35==75 and 2+1+1==4 and Fr('0.25')*60==15 and 72/3.6==20 and 36/3.6==10 and abs(3.6/18-0.2)<1e-9
QR=[("Questão 1","Uma sala retangular mede 5 m por 4 m. O piso será coberto com ladrilhos quadrados de 20 cm de lado. O número de ladrilhos necessário é",["500","50","5.000","250","400"],1,"Área: 20 m² = 200.000 cm². Cada ladrilho: 20 × 20 = 400 cm². 200.000 ÷ 400 = 500."),
("Questão 2","Um reservatório com 12 m³ de água abastece uma base que consome 400 litros por dia. A água dura",["30 dias.","3 dias.","48 dias.","300 dias.","12 dias."],3,"12 m³ = 12.000 litros. 12.000 ÷ 400 = 30 dias."),
("Questão 3","Um plantão começa às 22h45 e termina às 6h15 do dia seguinte. Sua duração é de",["7 h 30 min.","7 h 70 min.","8 h 30 min.","7 h 15 min.","8 h."],0,"Até 24h: 1 h 15 min. Mais 6 h 15 min: 7 h 30 min."),
("Questão 4","A velocidade de 72 km/h equivale, em metros por segundo, a",["20","72","259,2","7,2","200"],4,"Divide-se por 3,6: 72 ÷ 3,6 = 20 m/s.")]
QR=[(a,b,c,[0,3,4,2][k] if False else [2,0,4,1][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
QR[3]=("Questão 4",QR[3][1],["20","72","259,2","7,2","200"],1,QR[3][4]) if False else QR[3]
QRF=qr_md(QR,6)
t1="<strong>Parque da Guarda</strong><br><br>O parque que a Guarda Municipal de Vila Nova, cidade fictícia, patrulha é retangular, com 400 m por 150 m. Em volta há uma pista de caminhada de 1,8 km por volta. Um reservatório de 12 m³ abastece o parque e tem consumo de 400 litros por dia."
t2="<strong>Escala de plantão</strong><br><br>O plantão noturno da Guarda Municipal começa às 22h45 e termina às 6h15 do dia seguinte. Cada guarda faz 5 plantões por semana."
tx={"mt8a":t1,"mt8b":t2}
assert 400*150==60000 and 60000//10000==6 and 4*Fr('1.8')==Fr('7.2') and 12*1000==12000 and Fr(75,10)*5==Fr('37.5')
# n=1
qv(1,"Em metros, 3,5 km correspondem a","{} m",3500,[350,35,35000,0.35],"3,5 × 1.000.")
qv(1,"Em metros, 250 cm correspondem a","{} m",2.5,[25,250000,0.25,2500],"250 ÷ 100.")
qv(1,"Em minutos, 2 horas correspondem a","{} min",120,[200,100,60,180],"2 × 60.")
qv(1,"Em gramas, 1,5 kg correspondem a","{} g",1500,[150,15,15000,1.5],"1,5 × 1.000.")
qv(1,"Em mililitros, 3 litros correspondem a","{} mL",3000,[300,30,30000,0.3],"3 × 1.000.")
qv(1,"Em litros, 1 m³ corresponde a","{} L",1000,[100,10,10000,1],"1 m³ = 1.000 dm³ = 1.000 L.")
qv(1,"Em centímetros quadrados, 4 m² correspondem a","{} cm²",40000,[400,4000,4.0*0+4000000,8000],"4 × 10.000.")
qv(1,"Em minutos, 2 h 30 min correspondem a","{} min",150,[230,250,120,200],"120 + 30.")
qv(1,"Em quilogramas, 800 g correspondem a","{} kg",0.8,[8,80,0.08,800],"800 ÷ 1.000.")
qv(1,"Em metros quadrados, 1 hectare corresponde a","{} m²",10000,[100,1000,100000,1000000],"Um quadrado de 100 m por 100 m.")
qv(1,"Em horas, 90 minutos correspondem a","{} h",1.5,[0.9,9,1.3,1.9],"90 ÷ 60 = 1,5.")
qv(1,"Em quilômetros, 5.000 m correspondem a","{} km",5,[50,0.5,500,0.05],"5.000 ÷ 1.000.")
qv(1,"Um cubo de 10 cm de aresta tem capacidade de","{} litro(s)",1,[10,100,0.1,1000],"1.000 cm³ = 1 dm³ = 1 L.")
qv(1,"Em litros, 2 dm³ correspondem a","{} L",2,[20,200,0.2,2000],"1 dm³ = 1 L.")
qv(1,"A soma de 45 min com 35 min é, em minutos,","{} min",80,[70,75,85,90],"45 + 35 = 80, ou 1 h 20 min.")
qv(1,"Em horas, 3 dias correspondem a","{} h",72,[36,48,60,24],"3 × 24.")
qv(1,"Em quilogramas, 1,2 t correspondem a","{} kg",1200,[120,12,12000,1.2],"1,2 × 1.000.")
qv(1,"Em litros, 250 mL correspondem a","{} L",0.25,[2.5,25,0.025,250],"250 ÷ 1.000.")
q(1,"Pelo texto, a área do parque, em hectares, é",["6","60","0,6","600","3"],"400 × 150 = 60.000 m², ou 6 ha.","mt8a")
q(1,"Pelo texto, a duração de um plantão é de",["7 h 30 min","7 h 70 min","8 h 30 min","7 h 15 min","8 h"],"1 h 15 min até a meia-noite mais 6 h 15 min.","mt8b")
# n=2
qv(2,"Em centímetros, 0,0045 km correspondem a","{} cm",450,[45,4.5,4500,0.45],"0,0045 × 100.000.")
qv(2,"A diferença entre 3 h 45 min e 1 h 50 min é, em minutos,","{} min",115,[155,125,105,95],"3 h 45 min − 1 h 50 min = 1 h 55 min = 115 min.")
qv(2,"Em litros, 2,5 m³ correspondem a","{} L",2500,[250,25,25000,2.5],"2,5 × 1.000.")
qv(2,"Uma sala de 5 m por 4 m tem área, em cm², de","{} cm²",200000,[2000,20000,2000000,20],"20 m² × 10.000.")
qv(2,"Em hectares, 20 m² correspondem a","{} ha",0.002,[0.02,0.2,2,0.0002],"20 ÷ 10.000.")
q(2,"A soma 2 h 40 min + 1 h 35 min é igual a",["4 h 15 min","3 h 75 min","3 h 15 min","4 h 5 min","3 h 5 min"],"40 + 35 = 75 min = 1 h 15 min; 2 + 1 + 1 = 4 h.")
qv(2,"Uma cisterna de 2 m por 1,5 m por 1 m tem capacidade de","{} L",3000,[300,30000,3,2000],"3 m³ = 3.000 L.")
qv(2,"Três sacos de 2,5 kg e quatro de 1,2 kg pesam, juntos,","{} kg",12.3,[9.7,12,13.5,11.3],"7,5 + 4,8 = 12,3.")
qv(2,"A velocidade de 72 km/h equivale a","{} m/s",20,[72,259.2,7.2,200],"72 ÷ 3,6 = 20.")
qv(2,"Em metros quadrados, 1,5 km² correspondem a","{} m²",1500000,[150000,15000,1500,15000000],"1,5 × 1.000.000.")
qv(2,"Com 8 litros de água, o número de garrafas de 250 mL que se enchem é","{}",32,[8,16,40,20],"8.000 ÷ 250 = 32.")
q(2,"Quem sai às 14h25 e viaja 2 h 50 min chega às",["17h15","16h75","17h25","16h15","17h05"],"14h25 + 2 h 50 min = 16h75 = 17h15.")
qv(2,"Uma viatura percorre 1 km a cada 2 min 30 s. Em 10 minutos percorre","{} km",4,[5,3,2.5,6],"10 ÷ 2,5 = 4.")
qv(2,"Em minutos, 1,25 h correspondem a","{} min",75,[125,85,65,90],"1,25 × 60.")
q(2,"A diferença 5 h 10 min − 2 h 45 min é igual a",["2 h 25 min","3 h 35 min","2 h 35 min","3 h 25 min","2 h 65 min"],"Empresta-se 1 h: 4 h 70 min − 2 h 45 min = 2 h 25 min.")
qv(2,"A velocidade de 3,6 km/h equivale a","{} m/s",1,[3.6,12.96,0.36,10],"3,6 ÷ 3,6 = 1.")
qv(2,"Um terreno de 30 m por 50 m tem, em ares,","{} ares",15,[1.5,150,0.15,30],"1.500 m² ÷ 100 = 15.")
qv(2,"Pelo texto, uma pessoa que dá 4 voltas na pista percorre","{} km",7.2,[6,7,9,0.72],"4 × 1,8.","mt8a")
qv(2,"Pelo texto, a capacidade do reservatório, em litros, é","{} L",12000,[1200,120,120000,12],"12 × 1.000.","mt8a")
qv(2,"Pelo texto, o total de horas de plantão de um guarda em uma semana é","{} h",37.5,[35,40,36.5,32.5],"5 × 7,5 = 37,5.","mt8b")
# n=3
qv(3,"Uma piscina de 8 m por 4 m e 1,5 m de profundidade, cheia, comporta","{} L",48000,[4800,480,32000,480000],"48 m³ = 48.000 L.")
qv(3,"Uma torneira despeja 20 litros por minuto. Para encher um reservatório de 12 m³, são necessárias","{} h",10,[6,8,12,20],"12.000 ÷ 20 = 600 min = 10 h.")
qv(3,"Um tanque de 3 m³ cheio de água tem massa aproximada, em toneladas, de","{} t",3,[0.3,30,300,1.5],"3.000 L pesam cerca de 3.000 kg = 3 t.")
q(3,"Quem sai às 23h50 e chega às 2h20 do dia seguinte viaja",["2 h 30 min","3 h 30 min","2 h 70 min","3 h","2 h"],"10 min até a meia-noite mais 2 h 20 min = 2 h 30 min.")
qv(3,"A velocidade de 36 km/h equivale a","{} m/s",10,[36,129.6,3.6,100],"36 ÷ 3,6 = 10.")
qv(3,"Um terreno retangular de 45 m por 30 m será cercado com postes a cada 2,5 m. O número de postes é","{}",60,[30,120,62,64],"Perímetro: 150 m. 150 ÷ 2,5 = 60.")
qv(3,"Uma viatura a 18 km/h percorre 3,6 km em","{} min",12,[20,10,15,18],"3,6 ÷ 18 = 0,2 h = 12 min.")
qv(3,"Uma caixa de 40 cm por 30 cm por 20 cm tem capacidade de","{} L",24,[240,2.4,12,6],"24.000 cm³ = 24 L.")
qv(3,"Em um volume de 1,44 m³, o número de caixas de 24 litros que cabem é","{}",60,[6,600,48,72],"1.440 L ÷ 24 = 60.")
q(3,"O tempo de 5,25 horas corresponde a",["5 h 15 min","5 h 25 min","5 h 45 min","5 h 2 min","5 h 30 min"],"0,25 × 60 = 15 min.")
qv(3,"Um piso de 6 m por 4 m será coberto com ladrilhos de 20 cm por 20 cm. O número de ladrilhos é","{}",600,[60,6000,480,300],"240.000 cm² ÷ 400 = 600.")
qv(3,"Uma área de 2,5 ha é patrulhada por 5 guardas, cada um cobrindo 500 m² por hora. O tempo necessário é","{} h",10,[5,12.5,20,50],"25.000 m² ÷ 2.500 m²/h = 10 h.")
q(3,"A soma 3 dias 4 h + 2 dias 20 h é igual a",["6 dias","5 dias 24 h","5 dias 14 h","6 dias 4 h","5 dias 4 h"],"4 + 20 = 24 h = 1 dia; 3 + 2 + 1 = 6 dias.")
qv(3,"Em segundos, 10 min 30 s correspondem a","{} s",630,[1030,330,600,1830],"10 × 60 + 30.")
qv(3,"A soma 0,75 h + 45 min é, em minutos,","{} min",90,[120,75,100,80],"0,75 h = 45 min; 45 + 45 = 90.")
qv(3,"Um vazamento perde 5 mL por minuto. Em um dia perde","{} L",7.2,[72,0.72,3.6,12],"5 × 1.440 = 7.200 mL = 7,2 L.")
qv(3,"Em hectares, 1 km² corresponde a","{} ha",100,[10,1000,1,10000],"1.000.000 ÷ 10.000.")
qv(3,"Em hectolitros, 15 m³ correspondem a","{} hL",150,[15,1500,1.5,15000],"15.000 L ÷ 100.")
qv(3,"Pelo texto, o reservatório abastece o parque por","{} dias",30,[3,48,300,12],"12.000 ÷ 400.","mt8a")
qv(3,"Pelo texto, um guarda que ganha R$ 12,00 por hora de plantão recebe, por semana,","R$ {},00",450,[420,480,360,500],"37,5 × 12 = 450.","mt8b")
assert 24000//1000==24 and 1440//24==60 and 240000//400==600 and 10*60+30==630 and 5*1440==7200
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("Grandezas e medidas: o degrau de cada escada",[
 ("comp","Comprimento",["degrau de 10","km, hm, dam, m, dm, cm, mm","3,5 km = 3.500 m"],"seção 1"),
 ("area","Superfície",["degrau de 100","1 m² = 10.000 cm²","1 ha = 10.000 m²"],"seção 2"),
 ("vol","Volume e capacidade",["degrau de 1.000","1 dm³ = 1 L","1 m³ = 1.000 L"],"seção 3"),
 ("massa","Massa",["1 kg = 1.000 g","1 t = 1.000 kg","1 L de água ≈ 1 kg"],"seção 4"),
 ("tempo","Tempo",["60 min = 1 h","2 h 30 min = 2,5 h","empresta 1 h"],"seção 5"),
 ("veloc","Velocidade",["km/h ÷ 3,6 = m/s","distância ÷ tempo","72 km/h = 20 m/s"],"seção 5")],
 "Na prova: confira se o número deve crescer ou diminuir ao trocar de unidade")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"Cada caixa tem a sua escada: de 10 em 10 no comprimento, de 100 na área, de 1.000 no volume e de 60 no tempo.","Fontes: Edital 02/2026, Anexo I. Referências de base: Sistema Internacional de Unidades (INMETRO); Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 10 e 11. Exemplos criados para a aula.")
revisao("mt-8","Grandezas e medidas",QQ,list(tx),
 cobertura=["Recorte do edital: quantidade, tempo, comprimento, superfície, capacidade e massa. Cobertos: prefixos do SI, conversões, hectare e are, relação volume-capacidade, operações com horas e minutos, velocidade em m/s e km/h."],
 pendencias=["Referências citadas como base (INMETRO, Iezzi et al.) não foram consultadas página a página.","Os resultados foram conferidos em parte por código; as conversões menos usuais devem ser rechecadas."],
 fontes_conferidas=[])
gravar("mt-8",aula_html,banco("mt-8",QQ),tx)
