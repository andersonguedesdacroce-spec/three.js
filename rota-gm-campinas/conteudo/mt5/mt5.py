import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
LEAD="Regra de três é o método para resolver, com uma conta só, problemas em que três valores são conhecidos e um quarto precisa ser descoberto. A Vunesp cobra a regra simples direta, a simples inversa e a composta, com três ou mais grandezas. O ponto decisivo não é a conta, que é uma multiplicação em cruz, e sim classificar cada grandeza como direta ou inversa em relação à que se procura. Esta aula ensina a classificar primeiro e calcular depois."
S={}
S[1]="""## 1. Regra de três simples direta

A ideia vem da proporção. Se 3 viaturas gastam 24 litros de combustível em uma ronda, quantos litros gastam 5 viaturas na mesma ronda? Organize os dados em duas linhas, com cada grandeza na sua coluna, e a incógnita x no lugar do que se quer:

viaturas: 3 e 5; litros: 24 e x.

Mais viaturas gastam mais combustível, então as grandezas crescem juntas: são diretamente proporcionais. Nesse caso as razões são iguais: 3/5 = 24/x. Multiplicando em cruz, 3x = 5 × 24 = 120, e x = 40 litros.

Uma segunda forma de pensar dispensa o esquema: primeiro ache o valor de uma unidade. Se 3 viaturas gastam 24 litros, 1 viatura gasta 8 litros, e 5 viaturas gastam 5 × 8 = 40 litros. É a chamada redução à unidade, e vale a pena porque funciona também quando o esquema embaralha.
"""
S[2]="""## 2. Regra de três simples inversa

Se 4 guardas fazem uma vistoria em 6 horas, em quanto tempo 8 guardas fazem a mesma vistoria? Mais guardas, menos tempo: as grandezas variam em sentidos opostos, e são inversamente proporcionais. Aqui a razão de uma é igual ao inverso da razão da outra: 4/8 = x/6. Resolvendo, 8x = 24, e x = 3 horas.

A segunda forma é mais intuitiva: o trabalho total vale 4 × 6 = 24 guarda-horas, uma quantidade que se mantém. Com 8 guardas, o tempo é 24 ÷ 8 = 3 horas.

O erro mais comum é aplicar a multiplicação em cruz da direta a um problema inverso. Por isso, o primeiro passo é sempre o mesmo: pergunte “aumentando uma, a outra aumenta ou diminui?” e só então monte a proporção.
"""
S[3]="""## 3. Regra de três composta

Na regra composta há mais de duas grandezas. O método é comparar cada uma, separadamente, com a grandeza que contém a incógnita, mantendo as demais fixas, e dizer se é direta ou inversa em relação a ela. Depois, multiplicam-se as razões, invertendo as das grandezas inversas.

Exemplo resolvido. Seis guardas, trabalhando 8 horas por dia, patrulham um parque em 5 dias. Em quantos dias 10 guardas, trabalhando 6 horas por dia, patrulham o mesmo parque? A incógnita são os dias. Comparando com os dias: guardas, quanto mais, menos dias, então é inversa; horas por dia, quanto mais, menos dias, também inversa. Escreve-se a razão dos dias como o produto dos inversos: 5/x = (10/6) × (6/8). Calculando, 5/x = 60/48 = 5/4, e x = 4 dias. Pelo caminho do trabalho total: 6 × 8 × 5 = 240 guarda-horas, e 10 × 6 = 60 por dia, logo 240 ÷ 60 = 4 dias.

Exemplo resolvido com direta e inversa juntas. Três máquinas produzem 120 peças em 4 horas. Quantas peças 5 máquinas produzem em 6 horas? A incógnita são as peças. Com mais máquinas, mais peças (direta), e com mais horas, mais peças (direta). Então x/120 = (5/3) × (6/4) = 30/12 = 5/2, e x = 300 peças.
"""
S[5]="""## 5. Na rotina do guarda

- **Combustível:** se 3 viaturas gastam 24 litros em uma ronda, 5 viaturas gastam 40 litros, supondo mesmo trajeto.
- **Escala de serviço:** com mais guardas por turno, a mesma vistoria termina antes; a relação é inversa.
- **Material de escritório:** 1.200 folhas para 20 dias; para 30 dias, mantido o consumo diário, são 1.800 folhas.
- **Plantões:** o número de horas extras pagas cresce de modo direto com o número de plantões feitos.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Usar multiplicação em cruz direta num problema inverso | Classifique antes: aumenta uma, a outra aumenta ou diminui? |
| Comparar as grandezas entre si, e não com a incógnita | Compare cada uma com a que tem o x |
| Misturar unidades (min e h, m e km) | Converta tudo antes de montar |
| Esquecer de inverter a razão da grandeza inversa | Na dúvida, use o trabalho total constante |
| Dar o resultado sem conferir se faz sentido | Mais gente e menos tempo; menos gente e mais tempo |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Simples direta | As duas crescem juntas; razões iguais |
| Simples inversa | Uma cresce, a outra decresce; produto constante |
| Composta | Compare cada grandeza com a incógnita; multiplique as razões |
| Redução à unidade | Ache o valor de 1 e depois multiplique |
| Conferência | Unidades iguais; resposta coerente com o sentido |
"""
assert Fr(5*24,3)==40 and 4*6//8==3 and Fr(5)/(Fr(10,6)*Fr(6,8))==4 and 6*8*5//(10*6)==4 and 120*Fr(5,3)*Fr(6,4)==300
QR=[("Questão 1","Três viaturas gastam 24 litros de combustível em uma ronda. Para a mesma ronda, cinco viaturas gastarão",["40 litros.","14,4 litros.","30 litros.","45 litros.","120 litros."],2,"Mais viaturas, mais combustível: direta. 3/5 = 24/x → x = 40."),
("Questão 2","Quatro guardas fazem uma vistoria em 6 horas. Oito guardas, no mesmo ritmo, fariam em",["3 horas.","12 horas.","4 horas.","2 horas.","24 horas."],0,"Mais guardas, menos tempo: inversa. 4 × 6 = 8 × x → x = 3."),
("Questão 3","Seis guardas, trabalhando 8 horas por dia, patrulham um parque em 5 dias. Dez guardas, trabalhando 6 horas por dia, patrulham o mesmo parque em",["4 dias.","6 dias.","5 dias.","7,5 dias.","3 dias."],4,"Trabalho total: 6 × 8 × 5 = 240 guarda-horas. Por dia, 10 × 6 = 60. Logo 240 ÷ 60 = 4 dias."),
("Questão 4","Três máquinas produzem 120 peças em 4 horas. Cinco máquinas, em 6 horas, produzem",["300 peças.","200 peças.","240 peças.","180 peças.","150 peças."],1,"Cada máquina produz 120 ÷ (3 × 4) = 10 peças por hora. 5 máquinas × 6 horas × 10 = 300.")]
QRF=qr_md(QR,4)
t1="<strong>Consumo de material na Guarda</strong><br><br>O almoxarifado da Guarda Municipal de Vila Nova, cidade fictícia, registrou que 12 guardas consomem 480 litros de água potável em 8 dias de plantão. A direção quer prever o consumo para um evento que durará 10 dias, com 18 guardas escalados, mantido o consumo diário por pessoa."
t2="<strong>Mutirão de vistorias</strong><br><br>Uma equipe de 5 fiscais vistoria 60 estabelecimentos em 4 dias, trabalhando 6 horas por dia. Para um mutirão, a Prefeitura reunirá 10 fiscais, que trabalharão 8 horas por dia, e precisa vistoriar 160 estabelecimentos."
tx={"mt5a":t1,"mt5b":t2}
assert Fr(480,12*8)==5 and 5*18*10==900 and Fr(60,5*4*6)==Fr(1,2) and Fr(160)/(Fr(1,2)*10*8)==4
# n=1 (18 + 2)
qv(1,"Três viaturas gastam 24 litros em uma ronda. Cinco viaturas gastam","{} litros",40,[14.4,30,45,120],"Direta: 24 ÷ 3 = 8 por viatura; 5 × 8 = 40.")
qv(1,"Quatro guardas fazem um trabalho em 6 horas. Oito guardas fazem o mesmo trabalho em","{} horas",3,[12,4,2,24],"Inversa: 4 × 6 = 24; 24 ÷ 8 = 3.")
qv(1,"Se 2 cadernos custam R$ 10,00, 6 cadernos custam","R$ {},00",30,[20,12,60,15],"Direta: R$ 5,00 cada; 6 × 5 = 30.")
qv(1,"Uma viatura percorre 90 km com 9 litros. Com 20 litros, percorre","{} km",200,[180,100,10,81],"90 ÷ 9 = 10 km por litro; 20 × 10 = 200.")
qv(1,"Seis torneiras iguais enchem um tanque em 4 horas. Doze torneiras enchem o mesmo tanque em","{} horas",2,[8,1,6,24],"Inversa: o dobro de torneiras, metade do tempo.")
qv(1,"Um guarda caminha 3 km em 30 minutos. No mesmo ritmo, em 2 horas caminha","{} km",12,[6,9,18,10],"2 horas são 120 minutos; 120 ÷ 30 = 4; 4 × 3 = 12.")
qv(1,"Se 10 operários fazem um muro em 12 dias, 20 operários fazem em","{} dias",6,[24,10,12,3],"Inversa: o dobro de operários, metade do tempo.")
qv(1,"Um carro gasta 8 litros em 100 km. Em 250 km gasta","{} litros",20,[16,25,12,32],"Direta: 250 ÷ 100 = 2,5; 2,5 × 8 = 20.")
qv(1,"Uma bomba enche 300 litros em 10 minutos. Em 25 minutos enche","{} litros",750,[600,500,120,1200],"30 litros por minuto; 25 × 30 = 750.")
qv(1,"Dez cadeiras custam R$ 400,00. Quinze cadeiras, mesmo preço unitário, custam","R$ {},00",600,[500,800,450,560],"R$ 40,00 cada; 15 × 40 = 600.")
qv(1,"Em 3 horas, um guarda faz 4 rondas. Em 9 horas, faz","{} rondas",12,[6,16,36,8],"Direta: 9 ÷ 3 = 3; 3 × 4 = 12.")
qv(1,"Uma impressora imprime 120 folhas em 4 minutos. Em 10 minutos imprime","{} folhas",300,[200,480,40,150],"30 folhas por minuto; 10 × 30 = 300.")
qv(1,"Dois pedreiros constroem 6 m de muro por dia. Quatro pedreiros, mesmo ritmo, constroem por dia","{} m",12,[3,8,24,10],"Direta: dobro de pedreiros, dobro de muro.")
qv(1,"Uma equipe de 4 guardas atende 20 ocorrências por semana. Uma equipe de 6, no mesmo ritmo, atende","{} ocorrências",30,[24,10,80,26],"Direta: 5 por guarda; 6 × 5 = 30.")
qv(1,"Com velocidade de 40 km/h, uma viatura faz um trajeto em 3 horas. A 60 km/h, faz em","{} horas",2,[4,4.5,1,1.5],"Inversa: 40 × 3 = 120; 120 ÷ 60 = 2.")
qv(1,"Um pacote com 500 folhas dura 25 dias. Um pacote com 750 folhas, mesmo consumo diário, dura","{} dias",37.5,[50,30,35,75],"Direta: 20 folhas por dia; 750 ÷ 20 = 37,5.")
qv(1,"Dois ralos esvaziam uma caixa em 6 horas. Três ralos iguais esvaziam em","{} horas",4,[9,3,12,5],"Inversa: 2 × 6 = 12; 12 ÷ 3 = 4.")
qv(1,"Uma fotocópia custa R$ 0,25. Cem fotocópias custam","R$ {}",25,[2.5,250,12.5,4],"100 × 0,25 = 25.")
qv(1,"No texto, o consumo de água por guarda por dia é de","{} litros",5,[4,6,40,8],"480 ÷ (12 × 8) = 5.","mt5a")
qv(1,"No texto, a equipe original de 5 fiscais vistoria, por dia,","{} estabelecimentos",15,[12,10,60,20],"60 ÷ 4 = 15 por dia.","mt5b")
# n=2 (17 + 3)
qv(2,"Seis guardas, 8 horas por dia, patrulham um parque em 5 dias. Dez guardas, 6 horas por dia, patrulham em","{} dias",4,[6,5,7.5,3],"Trabalho: 6 × 8 × 5 = 240 guarda-horas; 10 × 6 = 60 por dia; 4 dias.")
qv(2,"Três máquinas produzem 120 peças em 4 horas. Cinco máquinas, em 6 horas, produzem","{} peças",300,[200,240,180,150],"10 peças por máquina-hora; 5 × 6 × 10 = 300.")
qv(2,"Oito pedreiros constroem 20 m de muro em 5 dias. Doze pedreiros, no mesmo ritmo, constroem 60 m em","{} dias",10,[7.5,6,15,12],"Por pedreiro-dia: 20 ÷ 40 = 0,5 m. 60 ÷ (12 × 0,5) = 10 dias.")
qv(2,"Um ônibus a 60 km/h leva 3 h 20 min para uma viagem. A 80 km/h levará","{} min",150,[200,160,170,140],"Tempo de 200 min; inversa: 200 × 60 ÷ 80 = 150 minutos, ou 2 h 30.")
qv(2,"Cinco guardas consomem 40 refeições em 4 dias. Oito guardas, em 10 dias, consomem","{} refeições",160,[100,80,128,200],"2 refeições por guarda-dia; 8 × 10 × 2 = 160.")
qv(2,"Uma equipe de 3 pessoas pinta 90 m² de parede em 6 horas. Para pintar 150 m² em 5 horas, são necessárias","{} pessoas",6,[5,4,3,10],"Rendimento: 5 m² por pessoa-hora. 150 ÷ (5 × 5) = 6.")
qv(2,"Uma torneira despeja 12 litros por minuto e enche um tanque em 50 minutos. Com 15 litros por minuto, enche em","{} minutos",40,[62.5,30,45,60],"Volume 600 litros; 600 ÷ 15 = 40.")
qv(2,"Se 8 máquinas fazem um serviço em 15 dias, 10 máquinas, no mesmo ritmo, fazem em","{} dias",12,[18.75,10,13,9],"Inversa: 8 × 15 = 120; 120 ÷ 10 = 12.")
qv(2,"Um fiscal vistoria 12 estabelecimentos em 3 dias. Para vistoriar 40 estabelecimentos no mesmo ritmo são necessários","{} dias",10,[12,9,13.3,8],"4 por dia; 40 ÷ 4 = 10.")
qv(2,"Quatro operários fazem uma obra em 15 dias. Depois de 5 dias, chegam mais 4 operários. A obra termina em mais","{} dias",5,[7.5,10,6,4],"Trabalho total 60 operário-dias; feitos 20; restam 40. Com 8 operários: 5 dias.")
qv(2,"Se 3 gatos pegam 3 ratos em 3 minutos, 9 gatos pegam 9 ratos, no mesmo ritmo, em","{} minutos",3,[9,1,27,6],"Cada gato pega 1 rato em 3 minutos; 9 gatos pegam 9 ratos em 3 minutos.")
qv(2,"Uma viatura percorre 300 km com 25 litros. Com 40 litros, percorre","{} km",480,[375,420,520,320],"12 km por litro; 40 × 12 = 480.")
qv(2,"Em 2 dias, 6 guardas fazem 24 rondas. Em 5 dias, 10 guardas fazem","{} rondas",100,[60,80,120,50],"2 rondas por guarda-dia; 10 × 5 × 2 = 100.")
qv(2,"Um tanque tem uma torneira que o enche em 6 horas e um ralo que o esvazia em 12 horas. Com ambos abertos, o tanque enche em","{} horas",12,[9,18,8,6],"Por hora: 1/6 − 1/12 = 1/12. Enche em 12 horas.")
qv(2,"Em um acampamento, há comida para 30 pessoas por 12 dias. Se chegarem mais 10 pessoas, a comida dura","{} dias",9,[16,10,8,6],"Total 360 pessoa-dias; 360 ÷ 40 = 9.")
qv(2,"Uma bomba enche 4.800 litros em 2 horas. Duas bombas iguais enchem 14.400 litros em","{} horas",3,[6,2,4,1.5],"Cada bomba: 2.400 L/h; duas: 4.800 L/h; 14.400 ÷ 4.800 = 3.")
qv(2,"Um texto de 12 páginas é digitado em 90 minutos. Em 4 horas, digitam-se","{} páginas",32,[24,30,36,48],"7,5 min por página; 240 ÷ 7,5 = 32.")
qv(2,"Segundo o texto, a previsão de consumo de água para o evento é de","{} litros",900,[600,720,750,1000],"5 litros × 18 guardas × 10 dias = 900.","mt5a")
qv(2,"Segundo o texto, o mutirão de 10 fiscais, em 1 dia de 8 horas, vistoria","{} estabelecimentos",40,[30,60,80,20],"0,5 estab. por fiscal-hora; 10 × 8 × 0,5 = 40.","mt5b")
qv(2,"Pelo texto, a quantidade de dias de mutirão necessária é de","{} dias",4,[3,5,6,2],"160 ÷ 40 por dia = 4 dias.","mt5b")
# n=3 (18 + 2)
qv(3,"Um grupo de 12 guardas faz um serviço em 10 dias, 8 horas por dia. Trabalhando 6 horas por dia, 16 guardas fazem o mesmo serviço em","{} dias",10,[8,12,7.5,9],"Total 12 × 10 × 8 = 960 guarda-horas. 16 × 6 = 96 por dia; 10 dias.")
qv(3,"Uma torneira enche um tanque em 3 horas, outra em 6 horas. Abertas juntas, enchem em","{} horas",2,[4.5,3,1.5,9],"Por hora: 1/3 + 1/6 = 1/2. Enchem em 2 horas.")
qv(3,"Um serviço seria feito por 10 operários em 24 dias. Depois de 8 dias, saíram 5 operários. Os que ficaram concluem o restante em","{} dias",32,[16,24,20,40],"Total 240 operário-dias; feitos 80; restam 160. Com 5 operários: 160 ÷ 5 = 32 dias.")
qv(3,"Uma equipe de 8 pessoas planejava terminar um relatório em 15 dias, 6 horas por dia. Se a equipe passar para 10 pessoas, com 4 horas por dia, o relatório sai em","{} dias",18,[12,20,16,24],"Total 8 × 15 × 6 = 720 pessoa-horas. 10 × 4 = 40 por dia; 18 dias.")
qv(3,"Para pintar 4 salas, 3 pintores gastam 6 dias. Para pintar 10 salas, com 5 pintores, gastam","{} dias",9,[8,10,12,7.5],"3 × 6 = 18 pintor-dias por 4 salas, 4,5 por sala. 10 salas: 45; ÷ 5 = 9.")
qv(3,"Quatro guardas fazem 3 rondas em 6 horas. Seis guardas fazem 9 rondas em","{} horas",12,[8,9,6,16],"Cada guarda faz 3/24 = 1/8 de ronda por hora. 6 guardas: 6/8 = 0,75 ronda por hora; 9 ÷ 0,75 = 12.")
qv(3,"Um relógio atrasa 3 minutos a cada 12 horas. Em 5 dias, atrasa","{} minutos",30,[15,36,45,18],"5 dias = 10 períodos de 12 h; 10 × 3 = 30.")
qv(3,"Uma obra, com 20 operários, ficaria pronta em 30 dias. Depois de 10 dias, 10 operários foram dispensados. A obra termina em mais","{} dias",40,[20,30,35,45],"Total 600; feitos 200; restam 400; com 10 operários: 40 dias.")
qv(3,"Se 5 homens ou 8 mulheres fazem um serviço em 12 dias, 10 homens e 8 mulheres, juntos, fazem o mesmo serviço em","{} dias",4,[6,3,5,8],"5 homens equivalem a 8 mulheres, então 10 homens equivalem a 16. Juntos com 8 mulheres, são 24 mulheres-equivalentes. 8 mulheres levam 12 dias; 24 levam 12 ÷ 3 = 4 dias.")
qv(3,"Uma fábrica produz 1.200 peças com 5 máquinas em 8 dias. Para produzir 2.700 peças em 9 dias, são necessárias","{} máquinas",10,[8,12,15,9],"Por máquina-dia: 30 peças. 2.700 ÷ (30 × 9) = 10.")
qv(3,"Um motorista a 90 km/h leva 4 horas. Para chegar 1 hora mais cedo, a velocidade média deve ser de","{} km/h",120,[100,110,135,105],"Distância 360 km; em 3 horas: 120 km/h.")
qv(3,"Para encher uma piscina, 4 bombas levam 12 horas. Se 2 bombas pararem após 4 horas, as outras 2 terminam em mais","{} horas",16,[8,12,24,10],"Total 48 bomba-horas; feitas 16; restam 32; 2 bombas: 16 horas.")
qv(3,"Uma torneira enche um tanque em 4 horas e outra, em 12 horas. Abertas juntas, enchem o tanque em","{} horas",3,[8,6,4.5,2],"Por hora: 1/4 + 1/12 = 4/12 = 1/3. Enchem em 3 horas.")
qv(3,"Uma tinta de 18 litros pinta 270 m². Para pintar 450 m², com a mesma tinta, são necessários","{} litros",30,[27,24,36,45],"15 m² por litro; 450 ÷ 15 = 30.")
qv(3,"Doze operários fazem 3/5 de uma obra em 9 dias. Para terminar o restante em 4 dias, o número total de operários deve ser","{} operários",18,[12,15,24,20],"Total da obra = 9 ÷ (3/5) = 15 dias com 12 operários = 180 operário-dias. Restam 72; em 4 dias: 18 operários.")
qv(3,"Em um quartel, 30 soldados têm comida para 20 dias. Depois de 5 dias, chegam 15 soldados. A comida restante dura mais","{} dias",10,[15,12,9,8],"Total 600 soldado-dias; consumidos 150; restam 450; com 45: 10 dias.")
qv(3,"Seis máquinas iguais fazem um serviço em 20 dias. Para fazer em 8 dias, o número de máquinas deve ser","{} máquinas",15,[9,12,18,10],"Total 120 máquina-dias; 120 ÷ 8 = 15.")
qv(3,"Um relatório de 30 páginas é digitado por 3 pessoas em 5 horas. Para digitar 80 páginas em 8 horas, são necessárias","{} pessoas",5,[4,6,8,7.5],"2 páginas por pessoa-hora. 80 ÷ (2 × 8) = 5.")
qv(3,"No texto, se o evento durasse 15 dias com 12 guardas, o consumo previsto seria de","{} litros",900,[720,600,1000,1200],"5 × 12 × 15 = 900.","mt5a")
qv(3,"No texto, para fazer o mutirão em 2 dias com 8 horas por dia, seriam necessários, no mínimo,","{} fiscais",20,[16,10,15,30],"160 ÷ 2 = 80 por dia; 0,5 × 8 = 4 por fiscal; 80 ÷ 4 = 20.","mt5b")

assert 240-80==160 and Fr(160,5)==32 and Fr(12,3)==4
QQ=fechar()
assert Fr(1,4)+Fr(1,12)==Fr(1,3)
assert len(QQ)==60, len(QQ)
code,svg=mapa("Regra de três: classifique primeiro, calcule depois",[
 ("direta","Simples direta",["as duas crescem juntas","razões iguais","3/5 = 24/x"],"seção 1"),
 ("inversa","Simples inversa",["uma cresce, a outra decresce","produto constante","trabalho total fixo"],"seção 2"),
 ("composta","Composta",["compare com a incógnita","inverta as inversas","multiplique as razões"],"seção 3"),
 ("unidade","Redução à unidade",["ache o valor de 1","multiplique depois","funciona sempre"],"seção 1"),
 ("total","Trabalho total",["homens × horas × dias","guarda-hora, máquina-dia","divida pelo ritmo novo"],"seção 3"),
 ("conf","Conferência",["unidades iguais","sentido coerente","mais gente, menos tempo"],"seção 6")],
 "Na prova: pergunte se uma cresce quando a outra cresce e confira o sentido da resposta")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A classificação em direta ou inversa decide a conta; a redução à unidade e o trabalho total servem de rede de segurança.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 11; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.")
revisao("mt-5","Regra de três simples e composta",QQ,list(tx),
 cobertura=["Recorte do edital: situações-problema com regra de três simples e composta. Cobertos: simples direta e inversa, composta com duas e três grandezas, redução à unidade, trabalho total constante, torneiras e ralos, obras com saída de operários."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","Conferi cada resposta de cabeça e por raciocínio de trabalho total; ao contrário dos postos mt-1 a mt-3, nem todas as respostas foram recalculadas por código. Recomendo conferir os gabaritos do banco, em especial as questões difíceis."],
 fontes_conferidas=[])
gravar("mt-5",aula_html,banco("mt-5",QQ),tx)
