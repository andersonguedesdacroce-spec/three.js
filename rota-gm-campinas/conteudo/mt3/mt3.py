import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
def pc(x,casas=None):  # Fraction (razão) -> "12,5%"
    return dc(Fr(x)*100,casas)+"%"
LEAD="Porcentagem é a ferramenta mais cobrada da prova de Matemática, porque aparece em quase tudo: preço, salário, estatística de ocorrências, tabelas e gráficos. A Vunesp cobra quatro habilidades: calcular a porcentagem de um valor, descobrir a taxa ou o total quando se conhece o resto, aplicar aumento e desconto, e encadear variações sucessivas. Os erros de prova quase sempre vêm de uma única confusão, a de somar percentuais que deveriam ser multiplicados. Esta aula constrói a ideia, depois a regra, e fecha com as armadilhas."
S={}
S[1]="""## 1. A ideia de “por cento”

Por cento quer dizer “por cem”. Dizer que 25% dos guardas estão de folga é dizer que, a cada 100 guardas, 25 estão de folga; é a fração 25/100, ou 1/4, ou o decimal 0,25. Porcentagem, fração e decimal são três nomes para a mesma coisa. Para passar de porcentagem a decimal, divide-se por 100, ou seja, anda-se com a vírgula duas casas para a esquerda: 35% = 0,35; 8% = 0,08; 150% = 1,5. Para voltar, multiplica-se por 100.

Calcular uma porcentagem de um valor é multiplicar o valor pelo decimal. A palavra “de” continua sendo multiplicação: 20% de 300 é 0,20 × 300 = 60. Alguns atalhos poupam conta. Para achar 10%, divida por 10. Para 1%, divida por 100. Para 50%, divida por 2; para 25%, divida por 4. Os demais saem por combinação: 15% de 80 é 10% mais a metade de 10%, ou 8 + 4 = 12. Porcentagem acima de 100% é válida e significa mais que o todo: 150% de 40 é 60.

Se o todo é o preço de um produto, 100% é o preço inteiro. Um produto que custa R$ 200,00 e tem 15% de desconto custa 85% do preço original, porque 100% − 15% = 85%. Guarde esta ideia, porque ela vai simplificar tudo mais adiante: em vez de calcular o desconto e subtrair, calcule direto quanto sobra.
"""
S[2]="""## 2. Parte, todo e taxa

Todo problema simples de porcentagem tem três ingredientes: o todo, a parte e a taxa. A relação entre eles é parte = taxa × todo. A pergunta é que ingrediente falta, e há três versões.

Na primeira, falta a parte. Quanto é 30% de 250? A parte é 0,30 × 250 = 75. Na segunda, falta a taxa. 15 é quantos por cento de 60? A taxa é parte ÷ todo = 15 ÷ 60 = 0,25, ou 25%. Na terceira, falta o todo. Se 35% de um número é 70, que número é esse? O todo é parte ÷ taxa = 70 ÷ 0,35 = 200.

A dica de leitura é perguntar “em relação a quê?”. A palavra que vem depois de “de”, ou depois de “em relação a”, é o todo, e é por ele que se divide quando se quer a taxa. Se 8 pessoas são aprovadas num grupo de 32, a taxa de aprovação é 8 ÷ 32 = 25%, e não 32 ÷ 8.

Exemplo resolvido. Em um grupo de 60 guardas, 45% são mulheres. Quantos são homens? Há dois caminhos. No primeiro, calcula-se o número de mulheres, 0,45 × 60 = 27, e subtrai-se: 60 − 27 = 33 homens. No segundo, usa-se o complemento: se 45% são mulheres, 55% são homens, e 0,55 × 60 = 33. O segundo caminho é mais curto e é o que a prova premia.
"""
S[3]="""## 3. Aumento e desconto: o fator multiplicador

Aumentar um valor em 15% é ficar com 100% + 15% = 115% dele, e 115% é 1,15. Descontar 20% é ficar com 100% − 20% = 80% dele, e 80% é 0,80. Esses números, 1,15 e 0,80, são os fatores multiplicadores. Em vez de calcular o aumento e depois somar, multiplica-se uma só vez.

Com taxa de aumento i, o fator é 1 + i. Com taxa de desconto i, o fator é 1 − i. Assim, um produto de R$ 80,00 com aumento de 15% passa a custar 80 × 1,15 = R$ 92,00. Um produto de R$ 150,00 com desconto de 20% passa a custar 150 × 0,80 = R$ 120,00. Aumento de 30% tem fator 1,30; desconto de 15% tem fator 0,85; aumento de 100% tem fator 2, porque o valor dobra.

O fator multiplicador também resolve a pergunta inversa, a de descobrir a variação. Se um valor passou de 80 para 100, o fator é 100 ÷ 80 = 1,25, e a variação é fator − 1 = 0,25, um aumento de 25%. Se passou de 100 para 80, o fator é 0,80, e a variação é −20%, uma queda de 20%. Note que a mesma diferença de 20 unidades vale 25% quando a base é 80 e 20% quando a base é 100. A variação percentual é sempre calculada sobre o valor inicial.

[[NOTA: Variação percentual = (valor final − valor inicial) ÷ valor inicial. A base é o valor de antes, nunca o de depois.]]
"""
S[4]="""## 4. Variações sucessivas

Quando há dois aumentos, dois descontos ou um aumento seguido de desconto, os percentuais não se somam. O segundo incide sobre o resultado do primeiro, e por isso os fatores se multiplicam. A razão é simples: depois do primeiro aumento, o valor é outro, e a segunda porcentagem é calculada sobre esse valor novo.

O caso que a prova ama é o de um aumento de 20% seguido de um desconto de 20%. Muita gente conclui que o valor volta ao que era. Não volta. Os fatores são 1,20 e 0,80, e 1,20 × 0,80 = 0,96. O resultado final é 96% do valor original, uma queda de 4%. Com um preço de R$ 100,00, o aumento leva a R$ 120,00, e 20% de 120 é 24, que deixa R$ 96,00. O desconto de 20% foi aplicado sobre uma base maior, e por isso tirou mais do que o aumento acrescentou.

O mesmo vale para dois descontos. Um desconto de 10% seguido de outro de 20% tem fator 0,90 × 0,80 = 0,72, e o desconto total é 1 − 0,72 = 28%, não 30%. Dois aumentos de 10% têm fator 1,10 × 1,10 = 1,21, ou seja, aumento total de 21%. Três descontos de 10% têm fator 0,90<sup>3</sup> = 0,729, e o desconto total é 27,1%.

O mesmo raciocínio explica o crescimento composto: um valor que cresce 10% ao mês durante 3 meses fica multiplicado por 1,10<sup>3</sup> = 1,331, ou seja, 33,1% de aumento total, e não 30%.

Exemplo resolvido. O salário de R$ 2.400,00 recebeu um aumento de 15% e, no mês seguinte, outro de 10%. Qual o salário final? Os fatores são 1,15 e 1,10. Então 2.400 × 1,15 = 2.760 e 2.760 × 1,10 = 3.036. O salário final é R$ 3.036,00, e o aumento total foi de 26,5%, e não de 25%, porque 1,15 × 1,10 = 1,265.
"""
S[5]="""## 5. Voltar ao valor original e outras armadilhas

Se um valor foi multiplicado por um fator, para recuperar o original divide-se pelo mesmo fator. Um produto que, depois de um aumento de 25%, custa R$ 150,00, tinha preço original de 150 ÷ 1,25 = R$ 120,00. Um produto que, depois de um desconto de 20%, foi vendido por R$ 144,00, custava 144 ÷ 0,80 = R$ 180,00. O erro típico é calcular 25% de 150 e subtrair, o que dá R$ 112,50, porque o aumento incidiu sobre o valor antigo e não sobre o novo.

Pela mesma lógica, o aumento que desfaz um desconto não é igual ao desconto. Depois de um desconto de 20%, o valor é 0,80 do original, e para voltar a 1 é preciso multiplicar por 1 ÷ 0,80 = 1,25, ou seja, um aumento de 25%. Da mesma forma, um aumento de 25% é desfeito por um desconto de 20%, porque 1,25 × 0,80 = 1.

Outra confusão é entre porcentagem e pontos percentuais. Se a taxa de aprovação subiu de 40% para 55%, a diferença é de 15 pontos percentuais. Já o aumento relativo é de 15 ÷ 40 = 37,5%. Quando o enunciado diz “pontos percentuais”, é a subtração das taxas; quando diz “aumento de X%”, é a variação relativa.

Por fim, em problemas de mistura, como 40 litros de uma solução a 30% de álcool com 60 litros de outra a 20%, somam-se as partes e divide-se pelo total. O álcool é 0,30 × 40 + 0,20 × 60 = 12 + 12 = 24 litros, num total de 100 litros: concentração de 24%. A média simples dos percentuais, 25%, estaria errada, porque as quantidades são diferentes.
"""
S[7]="""## 7. Na rotina do guarda

- **Estatística de ocorrências:** “os furtos caíram 20% em relação ao semestre anterior” exige calcular sobre o valor do semestre anterior. Se foram 250 e caíram 20%, passaram a 200.
- **Compras do órgão:** em uma licitação, dois descontos sucessivos de 10% e 5% não valem 15%; valem 1 − 0,90 × 0,95 = 14,5%.
- **Relatório de efetivo:** “45% do efetivo é feminino” vira número de pessoas só depois de multiplicar pelo total.
- **Orçamento de combustível:** um reajuste de 8% sobre R$ 2.500,00 leva a R$ 2.700,00, e esse novo valor é a base do reajuste seguinte.
- **Leitura de gráficos e tabelas:** “aumentou 10 pontos percentuais” e “aumentou 10%” são afirmações diferentes, e a prova costuma explorar a diferença.
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Somar 20% e −20% e dizer que volta ao original | Multiplique os fatores: 1,20 × 0,80 = 0,96, queda de 4% |
| Somar 10% e 20% de descontos como 30% | Multiplique 0,90 × 0,80 = 0,72, desconto de 28% |
| Calcular 25% sobre o preço novo para achar o original | Divida o preço novo pelo fator: 150 ÷ 1,25 |
| Calcular a variação sobre o valor final | A base é sempre o valor inicial |
| Confundir pontos percentuais com porcentagem | De 40% para 55% são 15 pontos e 37,5% relativos |
| Fazer a média simples de percentuais com bases diferentes | Some as partes e divida pelo total |
| Achar que 100% mais 100% é o triplo | Aumento de 100% dobra: fator 2 |
| Dar a resposta como fração quando pedem porcentagem | Multiplique por 100 e escreva o símbolo % |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Por cento | Fração de denominador 100: 35% = 35/100 = 0,35 |
| Parte, todo e taxa | parte = taxa × todo; taxa = parte ÷ todo; todo = parte ÷ taxa |
| Aumento de i | Fator 1 + i |
| Desconto de i | Fator 1 − i |
| Variação percentual | (final − inicial) ÷ inicial |
| Variações sucessivas | Multiplicam-se os fatores; não se somam as taxas |
| Voltar ao original | Divide-se pelo fator |
| Pontos percentuais | Diferença entre duas taxas |
"""
# ---- conferências do texto ----
assert Fr('0.2')*300==60 and Fr('0.15')*80==12 and Fr('1.5')*40==60 and Fr('0.85')*200==170
assert Fr('0.3')*250==75 and Fr(15,60)==Fr(1,4) and Fr(70)/Fr('0.35')==200 and 60-Fr('0.45')*60==33==Fr('0.55')*60
assert 80*Fr('1.15')==92 and 150*Fr('0.8')==120 and Fr(100,80)==Fr('1.25')
assert Fr('1.2')*Fr('0.8')==Fr('0.96') and Fr('0.9')*Fr('0.8')==Fr('0.72') and Fr('1.1')**2==Fr('1.21') and Fr('0.9')**3==Fr('0.729') and Fr('1.1')**3==Fr('1.331')
assert 2400*Fr('1.15')*Fr('1.1')==3036 and Fr('1.15')*Fr('1.1')==Fr('1.265')
assert Fr(150)/Fr('1.25')==120 and Fr(144)/Fr('0.8')==180 and 150-Fr('0.25')*150==Fr('112.5') and 1/Fr('0.8')==Fr('1.25') and Fr('1.25')*Fr('0.8')==1
assert Fr(15,40)==Fr('0.375') and Fr('0.3')*40+Fr('0.2')*60==24 and 1-Fr('0.9')*Fr('0.95')==Fr('0.145') and Fr('2500')*Fr('1.08')==2700
# ---- questões resolvidas ----
QR=[("Questão 1","O preço de uma jaqueta recebeu dois descontos sucessivos, o primeiro de 20% e o segundo de 10%. O desconto total sobre o preço original foi de",["28%","30%","32%","27%","25%"],3,"Fatores 0,80 e 0,90: 0,80 × 0,90 = 0,72. O preço final é 72% do original, e o desconto total é 100% − 72% = 28%. Os descontos não se somam."),
("Questão 2","Em uma sala, 40% dos candidatos são mulheres. Depois de 10 homens saírem, as mulheres passam a ser 50% dos presentes. O número inicial de candidatos era",["50","40","60","80","100"],0,"Seja N o total. Mulheres: 0,4N; homens: 0,6N. Saindo 10 homens, as mulheres (0,4N) igualam os homens restantes (0,6N − 10). Então 0,4N = 0,6N − 10, e 0,2N = 10, logo N = 50. Conferindo: 20 mulheres e 30 homens; saem 10, ficam 20 e 20."),
("Questão 3","Depois de um aumento de 25%, um produto passou a custar R$ 150,00. O preço antes do aumento era",["R$ 120,00","R$ 112,50","R$ 125,00","R$ 130,00","R$ 187,50"],2,"O preço novo é 125% do antigo: 1,25 × antigo = 150, então antigo = 150 ÷ 1,25 = 120. O erro seria tirar 25% de 150, que dá 112,50, porque os 25% incidiram sobre o preço antigo."),
("Questão 4","A taxa de aprovação em um curso passou de 40% para 55%. É correto afirmar que a taxa",["aumentou 15 pontos percentuais, ou 37,5% em termos relativos.","aumentou 15%, em termos relativos.","aumentou 15 pontos percentuais, ou 15% em termos relativos.","aumentou 37,5 pontos percentuais.","aumentou 27,5%, em termos relativos."],1,"A diferença entre as taxas é 55 − 40 = 15 pontos percentuais. A variação relativa é 15 ÷ 40 = 0,375, ou 37,5%. Pontos percentuais e porcentagem são medidas diferentes.")]
assert Fr('0.8')*Fr('0.9')==Fr('0.72') and Fr(50)*Fr('0.4')==20 and 50*Fr('0.6')-10==20 and Fr(150)/Fr('1.25')==120 and 55-40==15
QRF=qr_md(QR,6)
# ---- textos de apoio ----
t1="<strong>Furtos de bicicleta caem após campanha de registro</strong><br><br>Segundo balanço da Guarda Municipal de Vila Nova, cidade fictícia, os furtos de bicicleta somaram 250 ocorrências no primeiro semestre. Após uma campanha de registro das bicicletas, o número caiu 20% no segundo semestre. No terceiro semestre, houve aumento de 10% em relação ao segundo. Das bicicletas furtadas no primeiro semestre, 30% foram recuperadas."
t2="<strong>Compra de camisas de uniforme</strong><br><br>A Guarda Municipal de Vila Nova pretende comprar 200 camisas de uniforme. O fornecedor A cobra R$ 80,00 por camisa e oferece 15% de desconto para compras acima de 150 unidades. O fornecedor B cobra R$ 75,00 por camisa e oferece dois descontos sucessivos: 10% e, em seguida, mais 5% sobre o valor já reduzido."
tx={"mt3a":t1,"mt3b":t2}
f2=Fr('0.8')*250; f3=f2*Fr('1.1'); f4=f3*Fr('0.75')
assert f2==200 and f3==220 and Fr('0.3')*250==75 and f3/250==Fr('0.88') and f4==165 and f4/250==Fr('0.66')
pa=80*Fr('0.85'); pb=75*Fr('0.9')*Fr('0.95'); assert pa==68 and pa*200==13600 and Fr('0.9')*Fr('0.95')==Fr('0.855') and pb*200==12825 and 13600-12825==775
# ---- banco ----
# n=1
q(1,"O valor de 10% de 200 é",["20","10","2","100","180"],"10% é a décima parte: 200 ÷ 10 = 20.")
q(1,"O valor de 25% de 80 é",["20","25","32","40","8"],"25% é a quarta parte: 80 ÷ 4 = 20.")
q(1,"O número decimal 0,35, escrito como porcentagem, é",["35%","3,5%","0,35%","350%","3%"],"Multiplica-se por 100: 0,35 × 100 = 35%.")
q(1,"A fração 3/4, escrita como porcentagem, é",["75%","34%","43%","7,5%","25%"],"3 ÷ 4 = 0,75 = 75%.")
q(1,"O valor de 20% de 300 é",["60","6","20","600","150"],"0,20 × 300 = 60.")
q(1,"O número 15 corresponde a quantos por cento de 60?",["25%","15%","40%","4%","9%"],"15 ÷ 60 = 0,25 = 25%.")
q(1,"Um produto de R$ 50,00 sofreu aumento de 10%. O novo preço é",["R$ 55,00","R$ 45,00","R$ 60,00","R$ 51,00","R$ 5,00"],"50 × 1,10 = 55.")
q(1,"Um produto de R$ 150,00 recebeu desconto de 20%. O novo preço é",["R$ 120,00","R$ 130,00","R$ 30,00","R$ 170,00","R$ 148,00"],"150 × 0,80 = 120.")
q(1,"O valor de 5% de 400 é",["20","5","40","80","2"],"10% de 400 é 40, então 5% é a metade: 20.")
q(1,"O fator multiplicador de um aumento de 30% é",["1,3","0,3","1,03","0,7","30"],"100% + 30% = 130% = 1,3.")
q(1,"O fator multiplicador de um desconto de 15% é",["0,85","1,15","0,15","1,5","0,015"],"100% − 15% = 85% = 0,85.")
q(1,"Um guarda recebe R$ 3.000,00 e terá aumento de 5%. O novo salário será",["R$ 3.150,00","R$ 3.015,00","R$ 3.050,00","R$ 3.500,00","R$ 3.105,00"],"3.000 × 1,05 = 3.150.")
q(1,"Em uma turma de 40 candidatos, 60% são mulheres. O número de mulheres é",["24","16","20","60","40"],"0,60 × 40 = 24.")
q(1,"A porcentagem 12%, escrita como número decimal, é",["0,12","1,2","0,012","12","0,0012"],"12 ÷ 100 = 0,12.")
q(1,"O valor de 1% de 2.500 é",["25","250","2,5","0,25","1"],"2.500 ÷ 100 = 25.")
q(1,"O valor de 150% de 40 é",["60","6","15","150","40"],"1,5 × 40 = 60.")
q(1,"Um produto de R$ 200,00 recebeu desconto de 10%. O valor a pagar é",["R$ 180,00","R$ 190,00","R$ 20,00","R$ 220,00","R$ 100,00"],"200 × 0,90 = 180.")
q(1,"O número 8 corresponde a quantos por cento de 32?",["25%","4%","40%","8%","256%"],"8 ÷ 32 = 0,25 = 25%.")
q(1,"Segundo o texto, os 20% de queda dos furtos no segundo semestre correspondem, em ocorrências, a",[str(Fr('0.2')*250),"25","20","200","75"],"20% de 250 = 0,20 × 250 = 50.","mt3a")
q(1,"De acordo com o texto, o número de furtos de bicicleta no segundo semestre foi",[str(f2),"230","50","275","220"],"O fator da queda de 20% é 0,80: 250 × 0,80 = 200.","mt3a")
# n=2
q(2,"Depois de um aumento de 25%, um produto custa R$ 150,00. O preço antes do aumento era",["R$ 120,00","R$ 112,50","R$ 125,00","R$ 130,00","R$ 187,50"],"150 ÷ 1,25 = 120.")
q(2,"Depois de um desconto de 20%, um produto foi vendido por R$ 144,00. O preço original era",["R$ 180,00","R$ 172,80","R$ 164,00","R$ 160,00","R$ 115,20"],"144 ÷ 0,80 = 180.")
q(2,"Um aumento de 20% seguido de um desconto de 20% resulta em",["queda de 4%.","manutenção do valor.","aumento de 4%.","queda de 2%.","aumento de 2%."],"1,20 × 0,80 = 0,96, ou seja, 96% do original: queda de 4%.")
q(2,"Dois descontos sucessivos, de 10% e de 20%, equivalem a um desconto único de",["28%","30%","32%","27%","18%"],"0,90 × 0,80 = 0,72. Desconto de 1 − 0,72 = 28%.")
q(2,"Dois aumentos sucessivos de 10% equivalem a um aumento único de",["21%","20%","11%","10,5%","22%"],"1,10 × 1,10 = 1,21: aumento de 21%.")
q(2,"Um salário de R$ 2.400,00 teve aumento de 15% e, depois, de 10%. O salário final é",["R$ 3.036,00","R$ 3.000,00","R$ 3.024,00","R$ 2.760,00","R$ 3.060,00"],"2.400 × 1,15 = 2.760; 2.760 × 1,10 = 3.036.")
q(2,"Um valor passou de 80 para 100. O aumento percentual foi de",["25%","20%","80%","125%","10%"],"A base é o valor inicial: (100 − 80) ÷ 80 = 0,25.")
q(2,"Um valor passou de 100 para 80. A variação percentual foi de",["queda de 20%.","queda de 25%.","aumento de 20%.","queda de 80%.","queda de 10%."],"(80 − 100) ÷ 100 = −0,20.")
q(2,"Em uma prova de 50 questões, um candidato acertou 38. O percentual de acertos foi",["76%","38%","12%","19%","88%"],"38 ÷ 50 = 0,76.")
q(2,"A população de um bairro passou de 8.000 para 9.200 habitantes. O crescimento percentual foi de",["15%","12%","13%","20%","1.200%"],"Aumento de 1.200 sobre a base de 8.000: 1.200 ÷ 8.000 = 0,15.")
q(2,"Após um aumento de 20%, um produto custa R$ 360,00. O preço anterior era",["R$ 300,00","R$ 288,00","R$ 320,00","R$ 340,00","R$ 432,00"],"360 ÷ 1,20 = 300.")
q(2,"A taxa de aprovação de um curso passou de 40% para 55%. Essa mudança corresponde a um aumento de",["15 pontos percentuais.","15%.","37,5 pontos percentuais.","27,5%.","55 pontos percentuais."],"A diferença das taxas é 15 pontos percentuais. Em termos relativos, seriam 37,5%, mas a alternativa exata é a que diz “pontos”.")
q(2,"Uma loja dá 15% de desconto no pagamento à vista. Um item de R$ 640,00 sai à vista por",["R$ 544,00","R$ 96,00","R$ 625,00","R$ 576,00","R$ 736,00"],"640 × 0,85 = 544.")
q(2,"O valor de 20% de 30% de 500 é",["30","100","150","75","300"],"30% de 500 = 150; 20% de 150 = 30. Os fatores se multiplicam: 0,20 × 0,30 = 0,06, e 0,06 × 500 = 30.")
q(2,"Se 35% de um número é 70, esse número é",["200","24,5","245","105","35"],"O todo é parte ÷ taxa: 70 ÷ 0,35 = 200.")
q(2,"Um valor de R$ 250,00 recebeu acréscimo de 8%. O valor final é",["R$ 270,00","R$ 258,00","R$ 252,00","R$ 280,00","R$ 200,00"],"250 × 1,08 = 270.")
q(2,"Em um grupo de 60 guardas, 45% são mulheres. O número de homens é",["33","27","45","15","30"],"Homens são 55%: 0,55 × 60 = 33.")
q(2,"Segundo o texto, no terceiro semestre o número de furtos de bicicleta foi de",[str(f3),"225","230","210","240"],"Fator 1,10 sobre o semestre anterior: 200 × 1,10 = 220.","mt3a")
q(2,"Segundo o texto, as bicicletas recuperadas entre as furtadas no primeiro semestre foram",["75","30","50","175","25"],"30% de 250 = 0,30 × 250 = 75.","mt3a")
q(2,"De acordo com o texto, o preço de cada camisa no fornecedor A, já com o desconto, é de",["R$ 68,00","R$ 65,00","R$ 12,00","R$ 70,00","R$ 72,00"],"80 × 0,85 = 68. Como a compra é de 200 unidades (acima de 150), vale o desconto.","mt3b")
# n=3
q(3,"Depois de um aumento de 25%, que desconto deve ser aplicado para o preço voltar ao valor original?",["20%","25%","15%","30%","12,5%"],"Fator do aumento 1,25. Para voltar a 1, é preciso multiplicar por 1 ÷ 1,25 = 0,80, um desconto de 20%.")
q(3,"Depois de um desconto de 20%, que aumento deve ser aplicado para o preço voltar ao valor original?",["25%","20%","15%","30%","80%"],"Fator 0,80. Para voltar a 1: 1 ÷ 0,80 = 1,25, um aumento de 25%.")
q(3,"Três descontos sucessivos de 10% equivalem a um desconto único de",["27,1%","30%","29%","27%","33,1%"],"0,90<sup>3</sup> = 0,729. Desconto de 1 − 0,729 = 0,271, ou 27,1%.")
q(3,"Um produto teve aumento de 30% e, depois, desconto de 30%. Em relação ao preço original, o preço final é",["9% menor.","igual.","9% maior.","30% menor.","3% menor."],"1,30 × 0,70 = 0,91. O preço final é 91% do original: queda de 9%.")
q(3,"Um salário teve dois aumentos sucessivos de 20% cada e hoje é de R$ 3.600,00. O salário antes dos dois aumentos era",["R$ 2.500,00","R$ 2.571,43","R$ 2.592,00","R$ 3.000,00","R$ 2.160,00"],"O fator total é 1,20 × 1,20 = 1,44. Salário original = 3.600 ÷ 1,44 = 2.500.")
q(3,"Um valor que cresce 10% ao mês, sempre sobre o valor do mês anterior, terá crescido, depois de 3 meses, um total de",["33,1%","30%","31%","33%","36,3%"],"1,10<sup>3</sup> = 1,331: aumento total de 33,1%.")
q(3,"Em uma sala, 40% dos candidatos são mulheres. Saindo 10 homens, as mulheres passam a ser 50% dos presentes. O número inicial de candidatos era",["50","40","60","100","80"],"Com N candidatos: 0,4N = 0,6N − 10, logo 0,2N = 10 e N = 50.")
q(3,"Uma mercadoria foi vendida por R$ 96,00, com lucro de 20% sobre o preço de custo. O custo foi de",["R$ 80,00","R$ 76,80","R$ 72,00","R$ 115,20","R$ 84,00"],"Preço de venda = 1,20 × custo. Custo = 96 ÷ 1,20 = 80.")
q(3,"Um produto custava R$ 200,00, teve aumento de 10% e, em seguida, desconto de 10%. O preço final é",["R$ 198,00","R$ 200,00","R$ 202,00","R$ 180,00","R$ 220,00"],"200 × 1,10 = 220; 220 × 0,90 = 198.")
q(3,"Sobre um salário bruto de R$ 5.000,00 incidem descontos de 11% e de 7,5%, ambos calculados sobre o valor bruto. O salário líquido é",["R$ 4.075,00","R$ 4.050,00","R$ 4.162,50","R$ 4.100,00","R$ 4.000,00"],"Descontos somados: 18,5% do bruto. 5.000 × (1 − 0,185) = 4.075. Aqui os percentuais se somam porque têm a mesma base, o salário bruto.")
q(3,"Um reservatório perde por evaporação 20% da água que tem no início de cada semana. Depois de duas semanas, a água restante é",["64% do volume inicial.","60% do volume inicial.","80% do volume inicial.","40% do volume inicial.","66% do volume inicial."],"0,80 × 0,80 = 0,64.")
q(3,"Se A é 20% maior que B, então B é, em relação a A, aproximadamente",["16,7% menor.","20% menor.","16% menor.","25% menor.","17,5% menor."],"A = 1,2B. B = A ÷ 1,2 = 0,8333A, ou seja, B vale cerca de 83,3% de A, 16,7% menor.")
q(3,"Misturam-se 40 litros de uma solução com 30% de álcool e 60 litros de outra com 20% de álcool. A concentração da mistura é",["24%","25%","20%","26%","22,5%"],"Álcool: 0,30 × 40 + 0,20 × 60 = 12 + 12 = 24 litros em 100 litros: 24%. A média simples, 25%, ignora as quantidades.")
q(3,"Um item foi comprado por R$ 120,00, com 20% de desconto sobre o preço de tabela. O preço de tabela era",["R$ 150,00","R$ 144,00","R$ 140,00","R$ 96,00","R$ 160,00"],"120 = 0,80 × tabela. Tabela = 120 ÷ 0,80 = 150.")
q(3,"As vendas de uma loja subiram 20% em um mês e caíram 25% no mês seguinte. No conjunto dos dois meses, as vendas",["caíram 10%.","caíram 5%.","subiram 5%.","ficaram iguais.","caíram 4%."],"1,20 × 0,75 = 0,90. Queda de 10%.")
q(3,"O preço de um produto foi reduzido em 10% e, depois, aumentado em x%, ficando 8% acima do preço original. O valor de x é",["20%","18%","19%","16%","17,5%"],"Fatores: 0,90 × (1 + x) = 1,08. Então 1 + x = 1,08 ÷ 0,90 = 1,20, e x = 20%.")
q(3,"Segundo o texto, em relação ao número de furtos do primeiro semestre, o do terceiro semestre foi",["12% menor.","10% menor.","12% maior.","8% menor.","10% maior."],"220 ÷ 250 = 0,88. Queda de 12%. Os 20% de queda e os 10% de alta não se compensam.","mt3a")
q(3,"Se, no quarto semestre, os furtos caíssem 25% em relação ao terceiro, a variação total, do primeiro ao quarto semestre, seria de",["queda de 34%.","queda de 35%.","queda de 33%.","queda de 25%.","queda de 20%."],"Fatores: 0,80 × 1,10 × 0,75 = 0,66. Queda de 34%. Em números: 250 → 200 → 220 → 165.","mt3a")
q(3,"Segundo o texto, os dois descontos sucessivos do fornecedor B equivalem a um desconto único de",["14,5%","15%","5%","10%","14%"],"0,90 × 0,95 = 0,855. Desconto de 1 − 0,855 = 14,5%.","mt3b")
q(3,"Segundo o texto, ao comprar as 200 camisas, o fornecedor B resulta em um valor total",["R$ 775,00 menor que o do fornecedor A.","R$ 775,00 maior que o do fornecedor A.","R$ 1.000,00 menor que o do fornecedor A.","igual ao do fornecedor A.","R$ 200,00 menor que o do fornecedor A."],"A: 200 × 68 = 13.600. B: 75 × 0,90 × 0,95 = 64,125 por camisa; 200 × 64,125 = 12.825. Diferença: 13.600 − 12.825 = 775.","mt3b")
# conferências
assert Fr('1.25')*Fr('0.8')==1 and Fr('0.7')*Fr('1.3')==Fr('0.91') and Fr(3600)/Fr('1.44')==2500 and Fr(96)/Fr('1.2')==80 and 200*Fr('1.1')*Fr('0.9')==198
assert 5000*(1-Fr('0.185'))==4075 and Fr('0.8')**2==Fr('0.64') and 1/Fr('1.2')==Fr(5,6) and Fr(120)/Fr('0.8')==150 and Fr('1.2')*Fr('0.75')==Fr('0.9')
assert Fr(144)/Fr('0.8')==180 and 640*Fr('0.85')==544 and Fr('0.2')*Fr('0.3')*500==30 and 250*Fr('1.08')==270 and Fr('0.55')*60==33 and Fr(360)/Fr('1.2')==300 and Fr(9200-8000,8000)==Fr('0.15')
assert Fr('0.8')*Fr('1.1')*Fr('0.75')==Fr('0.66') and Fr('1.3')*Fr('0.7')==Fr('0.91')
assert Fr('1.08')/Fr('0.9')==Fr('1.2')
QQ=fechar(); assert len(QQ)==60, len(QQ)
code,svg=mapa("Porcentagem: do fator multiplicador às armadilhas",[
 ("ideia","Por cento = por cem",["35% = 35/100 = 0,35","“de” é vezes","atalho: 10%, 1%, 50%"],"seção 1"),
 ("tres","Parte, todo e taxa",["parte = taxa × todo","taxa = parte ÷ todo","todo = parte ÷ taxa"],"seção 2"),
 ("fator","Aumento e desconto",["aumento i: fator 1 + i","desconto i: fator 1 − i","variação = (f − i) ÷ i"],"seção 3"),
 ("sucessivas","Variações sucessivas",["multiplica os fatores","não soma as taxas","+20% e −20% = −4%"],"seção 4"),
 ("original","Valor original",["divide pelo fator","cuidado com a base","desfazer: 1 ÷ fator"],"seção 5"),
 ("pontos","Pontos percentuais",["diferença das taxas","relativo: sobre a inicial","mistura: soma das partes"],"seção 5")],
 "Na prova: pergunte “em relação a quê?” e multiplique fatores em vez de somar taxas")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"As três primeiras caixas formam o núcleo; a quarta é onde mais se erra; as duas últimas completam com o caminho de volta e com as comparações entre taxas.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 11 (Matemática comercial); Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.")
revisao("mt-3","Porcentagem",QQ,list(tx),
 cobertura=["Recorte do edital: “aumentos, descontos e variações sucessivas”. Cobertos: por cento como fração e decimal, cálculo de parte, taxa e todo, fator multiplicador, variação percentual, variações sucessivas (aumentos e descontos, crescimento composto de 3 períodos), recuperação do valor original, pontos percentuais e mistura.",
            "Não coberto de propósito: juros compostos com fórmula M = C(1+i)^n em fórmula fechada para períodos longos e logaritmos; ficam fora do nível do cargo."],
 pendencias=["Referências bibliográficas (Iezzi et al.; Dante) citadas como base; não foram consultadas página a página.","Gabaritos e exemplos conferidos por código (Fraction); a redação dos enunciados continua para revisão humana.","A questão sobre salário líquido usa percentuais de desconto fictícios (11% e 7,5%), sem relação com a tabela real do INSS ou do IR."],
 fontes_conferidas=["Cálculos: assert no script conteudo/mt3/mt3.py."])
gravar("mt-3",aula_html,banco("mt-3",QQ),tx)
print(len(aula_html))
