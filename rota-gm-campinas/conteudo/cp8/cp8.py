import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O roubo e a extorsão são os crimes patrimoniais com violência ou grave ameaça, e é nessa fronteira que a Guarda Municipal mais atua em flagrante. A Vunesp cobra os arts. 157 a 160 pela diferença entre roubo e furto, pelo roubo impróprio, pelas causas de aumento (que são muitas), pelo roubo com resultado (lesão grave e morte, o latrocínio) e pela extorsão, inclusive mediante sequestro. A aula organiza o texto consolidado em quatro blocos."
S={}
S[1]="## 1. Roubo e roubo impróprio\n\n"+L("art. 157, caput e § 1º","Art. 157. Subtrair coisa móvel alheia","§ 1º-A.")+"""

Roubar é subtrair coisa móvel alheia, para si ou para outrem, mediante grave ameaça ou violência a pessoa, ou depois de reduzi-la, por qualquer meio, à impossibilidade de resistência. A pena é de reclusão de seis a dez anos e multa. A diferença para o furto é o meio: o furto não tem violência nem ameaça. Já o § 1º é o roubo impróprio: o agente primeiro subtrai a coisa, sem violência, e só depois, logo em seguida, emprega violência ou grave ameaça para assegurar a impunidade do crime ou a detenção da coisa. A pena é a do roubo, porque o desvalor da conduta é o mesmo.

"""+L("art. 157, § 1º-A","§ 1º-A. A pena é de reclusão, de 6","§ 2º A pena aumenta-se")+"""

O § 1º-A é a figura do roubo contra bens que comprometam o funcionamento de órgãos públicos ou de estabelecimentos que prestem serviços públicos essenciais, com reclusão de seis a doze anos e multa.
"""
S[2]="## 2. Causas de aumento do roubo\n\n"+L("art. 157, § 2º","§ 2º A pena aumenta-se de 1/3 (um terço) até metade:","§ 2º-A.")+"\n\n"+L("art. 157, §§ 2º-A e 2º-B","§ 2º-A. A pena aumenta-se de 2/3","III - se do crime previsto")+" "+L("art. 157, § 2º-B","§ 2º-B. Se a violência ou grave ameaça","§ 3º Se da violência resulta")+"""

O § 2º traz as causas de aumento de um terço até a metade. As mais cobradas são o concurso de duas ou mais pessoas, a vítima em serviço de transporte de valores, conhecendo o agente essa circunstância, a subtração de veículo automotor transportado para outro Estado ou para o exterior, a restrição da liberdade da vítima (manter a vítima em seu poder), a violência ou ameaça com arma branca e a subtração de celular, de computador, de arma de fogo, de explosivos, de fios e cabos e de combustíveis. O inciso I, que previa o aumento pela arma de fogo, foi revogado: o tema passou aos §§ 2º-A e 2º-B.

O § 2º-A aumenta a pena de dois terços se a violência ou ameaça é exercida com arma de fogo, ou se há destruição ou rompimento de obstáculo com explosivo. E o § 2º-B, para arma de fogo de uso restrito ou proibido, manda aplicar em dobro a pena do caput. Repare na gradação: arma branca (um terço até a metade), arma de fogo (dois terços) e arma de fogo de uso restrito ou proibido (pena em dobro).
"""
S[3]="## 3. Roubo com lesão grave ou morte\n\n"+L("art. 157, § 3º","§ 3º Se da violência resulta:","§ 4º Se a violência")+"""

Se da violência resulta lesão corporal grave, a pena é de reclusão de sete a dezoito anos e multa. Se resulta morte, a pena é de reclusão de vinte e quatro a trinta anos e multa: é o latrocínio, crime hediondo. O mais cobrado é o limite da pena: o latrocínio tem a pena mínima de vinte e quatro anos, uma das maiores do Código.

"""+L("art. 157, §§ 4º e 5º","§ 4º Se a violência ou grave ameaça é cometida","Extorsão")+"""

Quando a violência ou a grave ameaça é cometida por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, no contexto da atuação, aplica-se em triplo a pena do caput, desprezadas as demais causas de aumento. E, se disso resulta morte, a reclusão é de vinte a quarenta anos e multa.
"""
S[4]="## 4. Extorsão e extorsão mediante sequestro\n\n"+L("art. 158, caput e §§ 1º e 2º","Art. 158. Constranger alguém","§ 3º Se o crime é cometido mediante a restrição")+"\n\n"+L("art. 158, § 3º","§ 3º Se o crime é cometido mediante a restrição","Extorsão mediante seqüestro")+"""

Na extorsão, o agente constrange a vítima, mediante violência ou grave ameaça, com o intuito de obter indevida vantagem econômica, a fazer, tolerar que se faça ou deixar de fazer alguma coisa. A pena é de reclusão de quatro a dez anos e multa, aumentada de um terço até a metade se há duas ou mais pessoas ou emprego de arma. A diferença para o roubo está em que, na extorsão, a vítima colabora (entrega a coisa, assina, faz a transferência), e o crime depende dessa conduta. Se o crime é cometido mediante restrição da liberdade da vítima, e essa condição é necessária para a obtenção da vantagem, é o que se chama de sequestro relâmpago: reclusão de seis a doze anos, além da multa, e, se resulta lesão grave ou morte, aplicam-se as penas do art. 159, §§ 2º e 3º.

"""+L("art. 159","Art. 159. Seqüestrar pessoa","Extorsão indireta")+"\n\n"+L("art. 160","Art. 160. Exigir ou receber","CAPÍTULO III")+"""

Na extorsão mediante sequestro, o agente sequestra pessoa para obter, como condição ou preço do resgate, qualquer vantagem. A pena é de reclusão de oito a quinze anos; se o sequestro dura mais de 24 horas, ou se a vítima é menor de 18 ou maior de 60 anos, ou se o crime é cometido por bando ou quadrilha, a pena é de doze a vinte anos; com lesão grave, de dezesseis a vinte e quatro; e, com morte, de vinte e quatro a trinta. O concorrente que denunciar o crime à autoridade, facilitando a libertação da vítima, tem a pena reduzida de um a dois terços (§ 4º), a chamada delação premiada. A extorsão indireta, do art. 160, é exigir ou receber, como garantia de dívida, abusando da situação de alguém, documento que possa dar causa a procedimento criminal, com reclusão de um a três anos e multa.
"""
S[6]="""## 6. Na rotina do guarda

- **Roubo em andamento:** é flagrante, e o guarda intervém, protege a vítima e conduz o autor; o uso progressivo da força vale também diante de arma.
- **Roubo de celular e de veículo:** são as ocorrências mais comuns; o aumento do § 2º reflete essa realidade.
- **Latrocínio:** a morte da vítima em roubo é crime de pena altíssima; o local deve ser preservado como cena de homicídio.
- **Sequestro relâmpago:** a restrição da liberdade da vítima para obter vantagem é crime grave, e a rápida comunicação à polícia é essencial.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do roubo simples | Reclusão de seis a dez anos, e multa |
| Roubo impróprio | Violência ou ameaça depois da subtração, para assegurar a impunidade ou a posse |
| Aumento por arma branca e arma de fogo | Branca: 1/3 até a metade (§ 2º, VII); fogo: 2/3 (§ 2º-A); fogo de uso restrito: pena em dobro (§ 2º-B) |
| Pena do latrocínio | Reclusão de 24 a 30 anos, e multa |
| Pena do roubo com lesão grave | Reclusão de 7 a 18 anos, e multa |
| Pena da extorsão | Reclusão de quatro a dez anos, e multa |
| Pena da extorsão mediante sequestro | Reclusão de oito a quinze anos |
| Confundir roubo e extorsão | No roubo, o agente toma; na extorsão, a vítima colabora |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Roubo | Reclusão, 6 a 10 anos, e multa; violência ou grave ameaça |
| Roubo impróprio | Violência depois da subtração, para impunidade ou posse |
| Aumento do § 2º | 1/3 até a metade: concurso, valores, restrição de liberdade, arma branca, celular |
| Arma de fogo | Aumento de 2/3 (§ 2º-A); uso restrito ou proibido: pena do caput em dobro |
| Lesão grave | Reclusão, 7 a 18 anos, e multa |
| Latrocínio | Reclusão, 24 a 30 anos, e multa |
| Extorsão | Reclusão, 4 a 10 anos, e multa |
| Sequestro relâmpago | Reclusão, 6 a 12 anos, e multa |
| Extorsão mediante sequestro | Reclusão, 8 a 15 anos; qualificadas: 12 a 20, 16 a 24, 24 a 30 |
"""
QR=[("Questão 1","A pena do roubo simples (art. 157, caput) é de",["reclusão, de seis a dez anos, e multa.","reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos, e multa.","reclusão, de oito a quinze anos.","reclusão, de dois a oito anos."],0,"Art. 157, caput."),
("Questão 2","Se da violência no roubo resulta morte, a pena é de",["reclusão, de vinte e quatro a trinta anos, e multa.","reclusão, de sete a dezoito anos, e multa.","reclusão, de doze a vinte anos.","reclusão, de vinte a quarenta anos.","reclusão, de dezesseis a vinte e quatro anos."],2,"Art. 157, § 3º, II."),
("Questão 3","No roubo impróprio, o agente emprega violência ou grave ameaça",["logo depois de subtraída a coisa, para assegurar a impunidade do crime ou a detenção da coisa.","antes da subtração.","durante a subtração, apenas.","depois de uma semana.","para obter vantagem econômica."],1,"Art. 157, § 1º."),
("Questão 4","A extorsão mediante sequestro (art. 159, caput) tem pena de",["reclusão, de oito a quinze anos.","reclusão, de quatro a dez anos, e multa.","reclusão, de seis a doze anos.","reclusão, de doze a vinte anos.","reclusão, de dois a oito anos."],4,"Art. 159, caput.")]
t1="<strong>Roubo de celular no ponto de ônibus</strong><br><br>Dois homens, um deles armado com faca, abordaram uma mulher no ponto de ônibus de Vila Nova, cidade fictícia, e levaram seu celular, ameaçando-a. Uma equipe da Guarda Municipal, acionada pelos passantes, perseguiu os dois e os deteve com o aparelho."
t2="<strong>Sequestro relâmpago</strong><br><br>Um homem foi abordado por um criminoso, que entrou em seu carro, o manteve em seu poder por duas horas e o obrigou, sob ameaça, a fazer transferências bancárias, para obter a vantagem econômica. A vítima foi libertada sem ferimentos."
tx={"cp8a":t1,"cp8b":t2}
# n=1
q(1,"A pena do roubo simples é de",["reclusão, de seis a dez anos, e multa.","reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos, e multa.","reclusão, de oito a quinze anos.","reclusão, de dois a oito anos."],"Art. 157, caput.")
q(1,"O roubo se distingue do furto porque no roubo há",["grave ameaça ou violência a pessoa.","coisa comum.","coisa imóvel.","vítima idosa.","dois agentes."],"Art. 157, caput.")
q(1,"No roubo impróprio, o agente emprega violência ou grave ameaça",["logo depois de subtraída a coisa.","antes da subtração.","dias depois.","durante o planejamento.","após a prisão."],"Art. 157, § 1º.")
q(1,"A pena do roubo impróprio é",["a mesma do roubo.","a do furto.","a da extorsão.","a da lesão corporal.","a de contravenção."],"Art. 157, § 1º: “na mesma pena incorre”.")
q(1,"A pena do roubo aumenta-se de um terço até a metade se há",["concurso de duas ou mais pessoas.","um só agente.","coisa de valor baixo.","autor primário.","idoso como autor."],"Art. 157, § 2º, II.")
q(1,"A pena do roubo aumenta-se de um terço até a metade se a vítima está em serviço de transporte de valores e o agente conhece tal circunstância. Esse aumento está no",["§ 2º, III.","§ 3º.","§ 4º.","§ 2º-A.","§ 2º-B."],"Art. 157, § 2º, III.")
q(1,"A pena do roubo aumenta-se de um terço até a metade se a violência ou grave ameaça é exercida com emprego de",["arma branca.","mão livre.","gritos.","documento falso.","veículo."],"Art. 157, § 2º, VII.")
q(1,"A pena do roubo aumenta-se de um terço até a metade se a subtração é de",["aparelho de telefonia celular, computador ou dispositivo semelhante.","dinheiro, apenas.","joia, apenas.","documento, apenas.","calçado, apenas."],"Art. 157, § 2º, IX.")
q(1,"A pena do roubo aumenta-se de dois terços se a violência ou ameaça é exercida com emprego de",["arma de fogo.","arma branca.","mão livre.","gritos.","pedra."],"Art. 157, § 2º-A, I.")
q(1,"Se a violência ou grave ameaça é exercida com emprego de arma de fogo de uso restrito ou proibido, aplica-se",["em dobro a pena do caput.","a pena do caput, sem aumento.","em triplo a pena do caput.","reclusão de dez a vinte anos.","detenção."],"Art. 157, § 2º-B.")
q(1,"Se da violência no roubo resulta lesão corporal grave, a pena é de",["reclusão, de sete a dezoito anos, e multa.","reclusão, de seis a dez anos.","reclusão, de vinte e quatro a trinta anos.","reclusão, de quatro a dez anos.","reclusão, de oito a quinze anos."],"Art. 157, § 3º, I.")
q(1,"Se da violência no roubo resulta morte, a pena é de",["reclusão, de vinte e quatro a trinta anos, e multa.","reclusão, de sete a dezoito anos.","reclusão, de doze a vinte anos.","reclusão, de vinte a quarenta anos.","reclusão, de oito a quinze anos."],"Art. 157, § 3º, II.")
q(1,"Na extorsão, o agente constrange a vítima, mediante violência ou grave ameaça, com o intuito de obter",["indevida vantagem econômica.","qualquer vantagem moral.","vingança.","prestígio.","reconhecimento."],"Art. 158, caput.")
q(1,"A pena da extorsão é de",["reclusão, de quatro a dez anos, e multa.","reclusão, de seis a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de oito a quinze anos.","reclusão, de dois a oito anos."],"Art. 158, caput.")
q(1,"A pena da extorsão aumenta-se de um terço até metade se o crime é cometido por duas ou mais pessoas, ou",["com emprego de arma.","com vítima idosa.","de dia.","em local fechado.","com testemunha."],"Art. 158, § 1º.")
q(1,"A pena da extorsão mediante sequestro (art. 159, caput) é de",["reclusão, de oito a quinze anos.","reclusão, de quatro a dez anos, e multa.","reclusão, de seis a doze anos.","reclusão, de doze a vinte anos.","reclusão, de dois a oito anos."],"Art. 159, caput.")
q(1,"A extorsão mediante sequestro tem pena de doze a vinte anos se o sequestro dura mais de",["24 horas.","12 horas.","48 horas.","72 horas.","7 dias."],"Art. 159, § 1º.")
q(1,"A extorsão indireta consiste em exigir ou receber, como garantia de dívida, documento que pode dar causa a",["procedimento criminal contra a vítima ou contra terceiro.","procedimento civil.","cobrança de juros.","penhora.","protesto."],"Art. 160.")
q(1,"No texto do celular, a subtração do aparelho, com ameaça de faca, é crime de",["roubo.","furto.","extorsão.","estelionato.","apropriação indébita."],"Art. 157, caput.","cp8a")
q(1,"No texto do sequestro relâmpago, a restrição da liberdade da vítima, necessária para a vantagem econômica, caracteriza",["extorsão com restrição da liberdade, prevista no art. 158, § 3º.","furto.","roubo simples.","estelionato.","apropriação indébita."],"Art. 158, § 3º.","cp8b")
# n=2
q(2,"O art. 157, § 1º-A, pune com reclusão de seis a doze anos o roubo contra bens que comprometam o funcionamento de",["órgãos públicos ou estabelecimentos que prestem serviços públicos essenciais.","residências.","lojas.","veículos particulares.","joalherias."],"Art. 157, § 1º-A.")
q(2,"A pena do roubo aumenta-se de um terço até a metade se a subtração é de veículo automotor que venha a ser",["transportado para outro Estado ou para o exterior.","estacionado.","guardado.","lavado.","emplacado."],"Art. 157, § 2º, IV.")
q(2,"A pena do roubo aumenta-se de um terço até a metade se o agente",["mantém a vítima em seu poder, restringindo sua liberdade.","foge.","empresta o veículo.","pede desculpas.","devolve a coisa."],"Art. 157, § 2º, V.")
q(2,"A pena do roubo aumenta-se de um terço até a metade se a subtração é de",["arma de fogo.","dinheiro.","roupa.","comida.","livro."],"Art. 157, § 2º, X.")
q(2,"O inciso I do § 2º do art. 157, que previa aumento pelo emprego de arma, aparece no texto consolidado como",["revogado.","vigente.","vetado.","declarado inconstitucional.","suspenso."],"Art. 157, § 2º, I: [revogado].")
q(2,"A pena do roubo aumenta-se de dois terços se há destruição ou rompimento de obstáculo mediante o emprego de",["explosivo ou artefato análogo que cause perigo comum.","ferramenta manual.","alicate.","pé de cabra.","chave falsa."],"Art. 157, § 2º-A, II.")
q(2,"Se a violência ou grave ameaça no roubo é cometida por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, aplica-se a pena do caput",["em triplo, desprezadas as demais causas de aumento.","em dobro.","aumentada de um terço.","aumentada de metade.","inalterada."],"Art. 157, § 4º.")
q(2,"Se o roubo com morte é cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, a pena é de",["reclusão, de vinte a quarenta anos, e multa.","reclusão, de vinte e quatro a trinta anos.","reclusão, de seis a dez anos.","reclusão, de doze a vinte anos.","reclusão, de dezesseis a vinte e quatro anos."],"Art. 157, § 5º.")
q(2,"A diferença entre extorsão e roubo é que, na extorsão,",["a conduta da vítima é necessária para a obtenção da vantagem.","a vítima é sempre idosa.","há dois agentes.","há arma.","a coisa é imóvel."],"Art. 158, caput: a vítima faz, tolera ou deixa de fazer algo.")
q(2,"A extorsão praticada mediante violência a que resulta lesão grave ou morte aplica-se o disposto",["no § 3º do art. 157.","no art. 155.","no art. 150.","no art. 129.","no art. 121."],"Art. 158, § 2º.")
q(2,"Se a extorsão é cometida mediante restrição da liberdade da vítima, e essa condição é necessária para a vantagem, a pena é de",["reclusão, de seis a doze anos, além da multa.","reclusão, de quatro a dez anos.","reclusão, de oito a quinze anos.","reclusão, de dois a oito anos.","detenção, de um a três anos."],"Art. 158, § 3º.")
q(2,"A extorsão mediante sequestro tem pena de reclusão de doze a vinte anos se o sequestrado é",["menor de 18 ou maior de 60 anos.","adulto jovem.","mulher.","estrangeiro.","funcionário."],"Art. 159, § 1º.")
q(2,"Se da extorsão mediante sequestro resulta lesão corporal grave, a pena é de",["reclusão, de dezesseis a vinte e quatro anos.","reclusão, de oito a quinze anos.","reclusão, de doze a vinte anos.","reclusão, de vinte e quatro a trinta anos.","reclusão, de seis a dez anos."],"Art. 159, § 2º.")
q(2,"Se da extorsão mediante sequestro resulta a morte, a pena é de",["reclusão, de vinte e quatro a trinta anos.","reclusão, de dezesseis a vinte e quatro anos.","reclusão, de oito a quinze anos.","reclusão, de doze a vinte anos.","reclusão, de vinte a quarenta anos."],"Art. 159, § 3º.")
q(2,"O concorrente que denunciar à autoridade a extorsão mediante sequestro, facilitando a libertação do sequestrado, terá a pena",["reduzida de um a dois terços.","aumentada.","dobrada.","mantida.","extinta."],"Art. 159, § 4º.")
q(2,"Se a extorsão mediante sequestro é cometida por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, a pena é",["aumentada em dois terços.","reduzida.","dobrada.","triplicada.","mantida."],"Art. 159, § 5º.")
q(2,"No texto do celular, o emprego de faca na ameaça é causa de aumento de",["um terço até a metade, pelo § 2º, VII.","dois terços, pelo § 2º-A.","pena em dobro, pelo § 2º-B.","um sexto.","metade, apenas."],"Art. 157, § 2º, VII.","cp8a")
q(2,"No texto do celular, a participação de dois agentes é causa de aumento de",["um terço até a metade, pelo § 2º, II.","dois terços.","pena em dobro.","um sexto.","um quarto."],"Art. 157, § 2º, II.","cp8a")
q(2,"No texto do sequestro relâmpago, a pena do art. 158, § 3º, é de",["reclusão, de seis a doze anos, além da multa.","reclusão, de quatro a dez anos.","reclusão, de oito a quinze anos.","reclusão, de dois a oito anos.","detenção, de um a três anos."],"Art. 158, § 3º.","cp8b")
q(2,"No roubo, a pena é aumentada de um terço até a metade se a subtração é de substâncias explosivas ou de acessórios que possibilitem sua fabricação, hipótese do",["§ 2º, VI.","§ 2º, II.","§ 3º, I.","§ 4º.","§ 2º-B."],"Art. 157, § 2º, VI.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Roubo: reclusão de seis a dez anos e multa; latrocínio: reclusão de vinte e quatro a trinta anos e multa; extorsão: reclusão de quatro a dez anos e multa.","Roubo: reclusão de quatro a dez anos; latrocínio: reclusão de doze a vinte anos.","Extorsão: reclusão de seis a dez anos; roubo: reclusão de oito a quinze anos.","Roubo: detenção de seis a dez anos; extorsão: detenção.","Latrocínio: reclusão de sete a dezoito anos; roubo com lesão grave: vinte e quatro a trinta."],"Arts. 157, caput e § 3º, II, e 158.")
q(3,"Considere as afirmações. I. O roubo com arma de fogo tem aumento de dois terços. II. O roubo com arma de fogo de uso restrito tem a pena do caput em dobro. III. O roubo com arma branca tem aumento de dois terços. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A arma branca tem aumento de 1/3 até a metade (art. 157, § 2º, VII).")
q(3,"Assinale a INCORRETA.",["O latrocínio tem pena de reclusão de sete a dezoito anos.","O roubo com lesão corporal grave tem pena de reclusão de sete a dezoito anos.","A extorsão mediante sequestro tem pena de reclusão de oito a quinze anos.","O roubo impróprio tem a mesma pena do roubo.","A extorsão tem pena de reclusão de quatro a dez anos."],"O latrocínio tem pena de vinte e quatro a trinta anos.")
q(3,"No roubo, a diferença entre os §§ 2º-A e 2º-B é que o § 2º-A aumenta a pena de dois terços para arma de fogo, e o § 2º-B",["aplica em dobro a pena do caput se a arma de fogo é de uso restrito ou proibido.","aumenta a pena de metade.","aumenta a pena de um sexto.","reduz a pena.","aplica a pena de reclusão de 4 a 10 anos."],"Arts. 157, §§ 2º-A e 2º-B.")
q(3,"A extorsão difere da extorsão mediante sequestro porque, nesta última, o agente",["sequestra pessoa com o fim de obter, como condição ou preço do resgate, qualquer vantagem.","apenas ameaça.","cobra uma dívida.","exige documento.","usa fraude."],"Art. 159, caput.")
q(3,"Na extorsão mediante sequestro, a vantagem exigida como condição ou preço do resgate é",["qualquer vantagem, não necessariamente econômica.","apenas econômica.","apenas moral.","apenas política.","apenas patrimonial."],"Art. 159, caput: “qualquer vantagem”.")
q(3,"Na extorsão do art. 158, a vantagem é",["indevida e econômica.","qualquer vantagem moral.","apenas devida.","apenas pública.","apenas de natureza política."],"Art. 158, caput.")
q(3,"A extorsão indireta (art. 160) tem pena de",["reclusão, de um a três anos, e multa.","reclusão, de quatro a dez anos.","detenção, de um a três anos.","reclusão, de dois a oito anos.","multa."],"Art. 160.")
q(3,"No roubo, a pena é aumentada de um terço até a metade, entre outras hipóteses, se a subtração é de",["fios, cabos ou equipamentos de energia, telefonia ou transferência de dados.","pasta de documentos.","roupas.","alimentos.","bijuterias."],"Art. 157, § 2º, VIII.")
q(3,"A pena do roubo, nos termos do § 2º, é aumentada de",["um terço até a metade.","dois terços.","metade a dois terços.","um sexto.","o dobro."],"Art. 157, § 2º, caput.")
q(3,"A extorsão pode ser praticada mediante",["violência ou grave ameaça.","fraude, apenas.","omissão.","contrato.","convenção."],"Art. 158, caput.")
q(3,"O § 3º do art. 158 manda aplicar, se da extorsão com restrição da liberdade resulta lesão grave ou morte,",["as penas do art. 159, §§ 2º e 3º.","as penas do art. 157, § 3º.","as penas do art. 121.","as penas do art. 129.","as penas do art. 148."],"Art. 158, § 3º.")
q(3,"Se, no roubo impróprio, o agente emprega a violência para assegurar a impunidade, a pena aplicada é",["a do roubo.","a do furto.","a da lesão corporal.","a da ameaça.","a do constrangimento ilegal."],"Art. 157, § 1º.")
q(3,"A subtração de explosivos, no roubo, é causa de aumento de",["um terço até a metade, pelo § 2º, VI.","dois terços.","pena em dobro.","um sexto.","metade a dois terços."],"Art. 157, § 2º, VI.")
q(3,"O aumento de dois terços do § 2º-A aplica-se se a violência ou ameaça é exercida com emprego de",["arma de fogo.","arma branca.","pedra.","faca de cozinha.","cassetete."],"Art. 157, § 2º-A, I.")
q(3,"Assinale a alternativa correta sobre a extorsão mediante sequestro.",["A pena básica é de reclusão de oito a quinze anos, e passa a doze a vinte anos se o sequestro dura mais de 24 horas.","A pena básica é de reclusão de quatro a dez anos.","A pena é de detenção.","Só existe se a vantagem é econômica.","O concorrente que denuncia tem a pena aumentada."],"Art. 159, caput e § 1º.")
q(3,"Se a extorsão mediante sequestro resulta lesão grave e o crime foi cometido em concurso, o concorrente que o denunciar à autoridade, facilitando a libertação, tem a pena",["reduzida de um a dois terços.","aumentada de um a dois terços.","dobrada.","mantida.","extinta."],"Art. 159, § 4º.")
q(3,"No texto do celular, se um dos agentes tivesse usado arma de fogo de uso restrito, a pena do caput seria",["aplicada em dobro, nos termos do § 2º-B.","aumentada de um terço.","aumentada de metade.","reduzida.","mantida."],"Art. 157, § 2º-B.","cp8a")
q(3,"No texto do celular, a subtração do celular é, ainda, causa de aumento do",["§ 2º, IX, de um terço até a metade.","§ 2º-A, de dois terços.","§ 2º-B.","§ 3º.","§ 4º."],"Art. 157, § 2º, IX.","cp8a")
q(3,"No texto do sequestro relâmpago, a duração da privação (duas horas) e a ausência de lesão resultam em pena de",["reclusão, de seis a doze anos, além da multa.","reclusão, de dezesseis a vinte e quatro anos.","reclusão, de vinte e quatro a trinta anos.","reclusão, de oito a quinze anos.","reclusão, de doze a vinte anos."],"Art. 158, § 3º.","cp8b")
assert len(Q)==60,len(Q)
code,svg=mapa("Roubo e extorsão",[
 ("roubo","Roubo",["reclusão, 6 a 10 anos, e multa","violência ou grave ameaça","impróprio: violência depois"],"seção 1"),
 ("aum","Aumentos",["§ 2º: 1/3 até a metade","arma de fogo: 2/3","uso restrito: pena em dobro"],"seção 2"),
 ("latro","Roubo com resultado",["lesão grave: 7 a 18 anos","morte: 24 a 30 anos","organização: triplo"],"seção 3"),
 ("ext","Extorsão",["reclusão, 4 a 10 anos","vítima colabora","relâmpago: 6 a 12"],"seção 4"),
 ("seq","Extorsão mediante sequestro",["reclusão, 8 a 15 anos","qualificada: 12 a 20","lesão grave: 16 a 24; morte: 24 a 30"],"seção 4"),
 ("ind","Extorsão indireta",["art. 160","documento como garantia","reclusão, 1 a 3 anos"],"seção 4")],
 "Na prova: arma branca, arma de fogo e arma de uso restrito têm aumentos diferentes")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As duas primeiras caixas tratam do roubo e dos aumentos; as demais, do resultado mais grave e da extorsão.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 157 a 160, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-8","Roubo e extorsão (CP, arts. 157 a 160)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 157 a 160. Cobertos todos, incluindo os §§ 1º-A, 2º-A, 2º-B, 4º e 5º do art. 157."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; os arts. 157 e 158 têm alterações muito recentes (2026) e devem ser reconferidos no Planalto.","A consolidação traz, no art. 157, § 2º-A, III, uma alínea e vetada por lei de 2026; o inciso foi omitido da aula.","O art. 157, § 3º, II, é chamado de latrocínio pela doutrina; o nome não consta do texto.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp8a e cp8b fictícios."],
 fontes_conferidas=["CP, arts. 157 a 160: texto da Câmara, copiado por programa."])
gravar("cp-8",aula_html,banco("cp-8",Q),tx)
