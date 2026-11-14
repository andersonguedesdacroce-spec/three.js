import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes contra a liberdade pessoal punem quem tira de outra pessoa a liberdade de decidir ou de ir e vir: o constrangimento ilegal, a ameaça, a perseguição, o sequestro, o trabalho escravo e o tráfico de pessoas. A Vunesp cobra os arts. 146 a 149-A pela pena, pelas causas de aumento e pelas figuras novas (intimidação sistemática, perseguição, violência psicológica). Para o guarda, são crimes que aparecem em ocorrências de ameaça, violência doméstica, trabalho degradante e tráfico de pessoas. A aula segue o texto consolidado."
S={}
S[1]="## 1. Constrangimento ilegal e intimidação sistemática\n\n"+L("art. 146","Art. 146. Constranger alguém","Intimidação sistemática (bullying)")+"""

Constranger é obrigar: o agente, por violência ou grave ameaça, ou depois de reduzir por outro meio a capacidade de resistência da vítima, a obriga a não fazer o que a lei permite ou a fazer o que a lei não manda. A pena é de detenção de três meses a um ano, ou multa. As penas se aplicam cumulativamente e em dobro quando se reúnem mais de três pessoas ou há emprego de armas, e se somam às penas da violência. O § 3º tira do tipo a intervenção médica ou cirúrgica sem consentimento, se justificada por iminente perigo de vida, e a coação exercida para impedir suicídio.

"""+L("art. 146-A","Art. 146-A. Intimidar sistematicamente","Ameaça")+"""

O bullying é a intimidação sistemática: intimidar de modo intencional e repetitivo, sem motivação evidente, por atos de intimidação, humilhação ou discriminação, ou por ações verbais, morais, sexuais, sociais, psicológicas, físicas, materiais ou virtuais. A pena é de multa, se a conduta não constitui crime mais grave. No cyberbullying, praticado por rede de computadores, redes sociais, aplicativos, jogos on-line ou outro ambiente digital, a pena é de reclusão de dois a quatro anos e multa.
"""
S[2]="## 2. Ameaça, perseguição e violência psicológica\n\n"+L("art. 147","Art. 147. Ameaçar alguém","Perseguição")+"\n\n"+L("art. 147-A","Art. 147-A. Perseguir alguém","Violência psicológica contra a mulher")+"""

A ameaça é prometer mal injusto e grave, por palavra, escrito, gesto ou outro meio simbólico, com pena de detenção de um a seis meses ou multa. Se é cometida contra a mulher por razões da condição do sexo feminino, a pena é dobrada. Procede-se mediante representação, exceto nessa hipótese contra a mulher. A perseguição, o stalking, é perseguir alguém, reiteradamente e por qualquer meio, ameaçando-lhe a integridade física ou psicológica, restringindo-lhe a locomoção ou invadindo ou perturbando sua esfera de liberdade ou privacidade, com reclusão de seis meses a dois anos e multa. A pena aumenta de metade se contra criança, adolescente ou idoso, contra a mulher por razões do sexo feminino ou com concurso de duas ou mais pessoas ou arma, e a ação depende de representação.

"""+L("art. 147-B","Art. 147-B. Causar dano emocional","Art. 147-C.")+"\n\n"+L("art. 147-C","Art. 147-C. Ameaçar alguém","Seqüestro e cárcere privado")+"""

A violência psicológica contra a mulher é causar dano emocional que a prejudique e perturbe seu pleno desenvolvimento, ou vise degradar ou controlar suas ações, por meios como ameaça, humilhação, manipulação, isolamento e chantagem, com reclusão de seis meses a dois anos e multa, e aumento de metade se feito com inteligência artificial ou outro recurso que altere imagem ou som da vítima. O art. 147-C pune a ameaça no contexto de atuação de organização criminosa, com reclusão de um a três anos.
"""
S[3]="## 3. Sequestro e cárcere privado\n\n"+L("art. 148","Art. 148. Privar alguém de sua liberdade","Redução a condição análoga à de escravo")+"""

Sequestro e cárcere privado é privar alguém da liberdade: no sequestro a vítima é levada e mantida em outro lugar, e no cárcere privado é mantida no mesmo lugar. A pena básica é de reclusão de um a três anos, que passa a dois a cinco anos se a vítima é ascendente, descendente, cônjuge ou companheiro do agente ou maior de sessenta anos, se há internação em casa de saúde ou hospital, se a privação dura mais de quinze dias, se a vítima é menor de dezoito anos ou se o crime é praticado com fins libidinosos. Se a vítima sofre grave sofrimento físico ou moral por maus-tratos ou pela natureza da detenção, a reclusão é de dois a oito anos. E, se cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, a reclusão é de doze a vinte anos.
"""
S[4]="## 4. Trabalho escravo e tráfico de pessoas\n\n"+L("art. 149","Art. 149. Reduzir alguém a condição análoga","Tráfico de pessoas")+"\n\n"+L("art. 149-A","Art. 149-A. Agenciar, aliciar","Seção II")+"""

Reduzir alguém a condição análoga à de escravo é submetê-lo a trabalhos forçados ou jornada exaustiva, sujeitá-lo a condições degradantes de trabalho, ou restringir sua locomoção por dívida com o empregador. A pena é de reclusão de dois a oito anos e multa, além da pena da violência. Incorre nas mesmas penas quem cerceia o uso de meio de transporte para reter o trabalhador, mantém vigilância ostensiva ou se apodera de seus documentos ou objetos pessoais com esse fim. A pena aumenta de metade contra criança ou adolescente ou por preconceito de raça, cor, etnia, religião ou origem.

O tráfico de pessoas é agenciar, aliciar, recrutar, transportar, transferir, comprar, alojar ou acolher pessoa, mediante grave ameaça, violência, coação, fraude ou abuso, para remover órgãos, submetê-la a trabalho escravo ou servidão, adoção ilegal ou exploração sexual. A pena é de reclusão de quatro a oito anos e multa. Aumenta-se de um terço até a metade, por exemplo, se o crime é cometido por funcionário público, contra criança, adolescente, idoso ou pessoa com deficiência, ou se a vítima é retirada do território nacional, e a pena é reduzida de um a dois terços se o agente é primário e não integra organização criminosa.
"""
S[6]="""## 6. Na rotina do guarda

- **Ameaça e violência doméstica:** a ameaça contra a mulher por razões do sexo feminino tem pena em dobro e ação pública sem representação; o atendimento deve acionar a rede de proteção.
- **Perseguição:** o relato reiterado de seguimento, mensagens e vigilância configura crime e deve ser registrado.
- **Trabalho degradante:** o guarda que encontra trabalhadores sem documentos, retidos ou em alojamentos degradantes deve acionar a autoridade, porque o tráfico de pessoas e o trabalho escravo são crimes graves.
- **Sequestro:** a privação da liberdade é crime permanente: o flagrante dura enquanto a vítima estiver privada da liberdade.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do constrangimento ilegal | Detenção de três meses a um ano, ou multa |
| Pena da ameaça | Detenção de um a seis meses, ou multa |
| Ameaça contra a mulher | Pena em dobro e sem necessidade de representação |
| Pena da perseguição | Reclusão de seis meses a dois anos, e multa |
| Pena do sequestro simples | Reclusão de um a três anos; qualificado: dois a cinco |
| Pena do trabalho escravo | Reclusão de dois a oito anos, e multa |
| Pena do tráfico de pessoas | Reclusão de quatro a oito anos, e multa |
| Bullying | Multa; no ambiente digital, reclusão de dois a quatro anos |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Constrangimento ilegal | Detenção, 3 meses a 1 ano, ou multa; dobro com mais de 3 pessoas ou armas |
| Intimidação sistemática | Multa; cyberbullying: reclusão, 2 a 4 anos |
| Ameaça | Detenção, 1 a 6 meses, ou multa; representação; dobro contra a mulher |
| Perseguição | Reclusão, 6 meses a 2 anos, e multa; aumento de metade |
| Violência psicológica contra a mulher | Reclusão, 6 meses a 2 anos, e multa |
| Sequestro | Reclusão, 1 a 3 anos; qualificado 2 a 5; sofrimento 2 a 8; milícia 12 a 20 |
| Trabalho escravo | Reclusão, 2 a 8 anos, e multa |
| Tráfico de pessoas | Reclusão, 4 a 8 anos, e multa |
"""
QR=[("Questão 1","A pena do crime de constrangimento ilegal (art. 146) é de",["detenção, de três meses a um ano, ou multa.","reclusão, de um a três anos.","detenção, de um a seis meses.","reclusão, de dois a oito anos.","detenção, de seis meses a dois anos."],0,"Art. 146, caput."),
("Questão 2","A ameaça (art. 147), praticada contra a mulher por razões da condição do sexo feminino, tem a pena",["aplicada em dobro, sem necessidade de representação.","reduzida pela metade.","aumentada em um terço, com representação.","mantida, com representação.","aumentada de metade, com representação."],2,"Art. 147, §§ 1º e 2º."),
("Questão 3","A pena do crime de redução a condição análoga à de escravo é de",["reclusão, de dois a oito anos, e multa, além da pena correspondente à violência.","reclusão, de um a três anos.","detenção, de dois a oito anos.","reclusão, de quatro a oito anos.","reclusão, de seis meses a dois anos."],4,"Art. 149, caput."),
("Questão 4","O tráfico de pessoas (art. 149-A) tem pena de",["reclusão, de quatro a oito anos, e multa.","reclusão, de um a três anos.","reclusão, de dois a oito anos.","detenção, de quatro a oito anos.","reclusão, de seis a vinte anos."],1,"Art. 149-A.")]
t1="<strong>Mensagens e vigilância</strong><br><br>Uma mulher procurou a Guarda Municipal de Vila Nova, cidade fictícia, para relatar que o ex-companheiro a seguia todos os dias na saída do trabalho, enviava dezenas de mensagens e ficava parado na frente de sua casa. Ele já a havia ameaçado de morte. Ela temia por sua integridade."
t2="<strong>Fazenda com trabalhadores retidos</strong><br><br>Em uma fiscalização, uma equipe encontrou 12 trabalhadores em alojamento degradante, sem água potável, com jornadas exaustivas, e o dono da fazenda mantinha seguranças armados na porta e guardava os documentos dos trabalhadores. Três dos trabalhadores tinham 16 anos."
tx={"cp5a":t1,"cp5b":t2}
# n=1
q(1,"A pena do constrangimento ilegal é de",["detenção, de três meses a um ano, ou multa.","reclusão, de um a três anos.","detenção, de um a seis meses.","reclusão, de dois a oito anos.","detenção, de seis meses a dois anos."],"Art. 146, caput.")
q(1,"As penas do constrangimento ilegal aplicam-se cumulativamente e em dobro quando, para a execução do crime,",["se reúnem mais de três pessoas, ou há emprego de armas.","há mais de duas pessoas.","há violência.","há uma vítima idosa.","há dano patrimonial."],"Art. 146, § 1º.")
q(1,"Não se compreende no crime de constrangimento ilegal",["a coação exercida para impedir suicídio.","qualquer ameaça.","a violência física.","a coação para pagamento.","a prisão ilegal."],"Art. 146, § 3º, II.")
q(1,"A pena da ameaça é de",["detenção, de um a seis meses, ou multa.","detenção, de três meses a um ano.","reclusão, de um a três anos.","reclusão, de seis meses a dois anos.","multa, apenas."],"Art. 147, caput.")
q(1,"A ameaça consiste em ameaçar alguém, por palavra, escrito, gesto ou outro meio simbólico, de causar-lhe mal",["injusto e grave.","qualquer.","justo e grave.","leve.","lícito."],"Art. 147, caput.")
q(1,"A pena da ameaça contra a mulher por razões da condição do sexo feminino é",["aplicada em dobro.","reduzida.","mantida.","aumentada de um terço.","aumentada de metade."],"Art. 147, § 1º.")
q(1,"Em regra, o crime de ameaça somente se procede mediante",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 147, § 2º.")
q(1,"A pena do crime de perseguição (art. 147-A) é de",["reclusão, de seis meses a dois anos, e multa.","detenção, de um a seis meses.","reclusão, de um a três anos.","detenção, de três meses a um ano.","reclusão, de dois a cinco anos."],"Art. 147-A, caput.")
q(1,"A pena da perseguição é aumentada de metade se o crime é cometido contra",["criança, adolescente ou idoso.","qualquer adulto.","qualquer mulher, em qualquer caso.","estrangeiro.","funcionário."],"Art. 147-A, § 1º, I.")
q(1,"O crime de perseguição exige que o agente persiga a vítima",["reiteradamente.","uma única vez.","em local público.","à noite.","com arma."],"Art. 147-A, caput.")
q(1,"O crime de violência psicológica contra a mulher (art. 147-B) tem pena de",["reclusão, de seis meses a dois anos, e multa.","detenção, de um a seis meses.","reclusão, de um a três anos.","multa.","detenção, de três meses a um ano."],"Art. 147-B.")
q(1,"A pena do sequestro e cárcere privado simples é de",["reclusão, de um a três anos.","reclusão, de dois a cinco anos.","detenção, de um a três anos.","reclusão, de dois a oito anos.","reclusão, de doze a vinte anos."],"Art. 148, caput.")
q(1,"A pena do sequestro é de reclusão de dois a cinco anos se a privação da liberdade dura mais de",["quinze dias.","dez dias.","vinte dias.","trinta dias.","cinco dias."],"Art. 148, § 1º, III.")
q(1,"A pena do sequestro é de reclusão de dois a cinco anos se o crime é praticado contra menor de",["dezoito anos.","catorze anos.","dezesseis anos.","doze anos.","vinte e um anos."],"Art. 148, § 1º, IV.")
q(1,"Reduzir alguém a condição análoga à de escravo tem pena de",["reclusão, de dois a oito anos, e multa, além da pena correspondente à violência.","reclusão, de um a três anos.","detenção, de dois a oito anos.","reclusão, de quatro a oito anos.","detenção, de seis meses a dois anos."],"Art. 149, caput.")
q(1,"É forma de reduzir alguém a condição análoga à de escravo submetê-lo a",["trabalhos forçados ou jornada exaustiva.","trabalho remunerado.","trabalho voluntário.","estágio.","jornada normal."],"Art. 149, caput.")
q(1,"O tráfico de pessoas tem pena de",["reclusão, de quatro a oito anos, e multa.","reclusão, de um a três anos.","reclusão, de dois a oito anos.","detenção, de quatro a oito anos.","reclusão, de seis a vinte anos."],"Art. 149-A.")
q(1,"A pena do tráfico de pessoas é reduzida de um a dois terços se o agente é",["primário e não integra organização criminosa.","reincidente.","menor.","funcionário público.","estrangeiro."],"Art. 149-A, § 2º.")
q(1,"No texto da perseguição, o comportamento do ex-companheiro configura, em tese,",["perseguição.","omissão de socorro.","rixa.","maus-tratos.","calúnia."],"Art. 147-A.","cp5a")
q(1,"No texto da fazenda, a retenção dos documentos dos trabalhadores faz incidir",["as mesmas penas do trabalho escravo, nos termos do art. 149, § 1º.","a pena de ameaça.","a pena do constrangimento.","a pena de rixa.","a pena do sequestro."],"Art. 149, § 1º, II.","cp5b")
# n=2
q(2,"Não se compreende na disposição do art. 146 a intervenção médica ou cirúrgica sem consentimento, se justificada por",["iminente perigo de vida.","interesse financeiro.","pedido de parente.","decisão do hospital.","simples conveniência."],"Art. 146, § 3º, I.")
q(2,"O art. 146-A (intimidação sistemática) pune a conduta com pena de multa",["se a conduta não constitui crime mais grave.","em qualquer caso, em dobro.","com detenção de um a seis meses.","com reclusão.","somente se houver violência."],"Art. 146-A.")
q(2,"A intimidação sistemática virtual (cyberbullying) tem pena de reclusão de",["dois anos a quatro anos, e multa.","um a três anos.","seis meses a dois anos.","três a sete anos.","quatro a oito anos."],"Art. 146-A, parágrafo único.")
q(2,"A intimidação sistemática exige, entre outros elementos, que a conduta seja",["intencional e repetitiva, sem motivação evidente.","eventual.","acidental.","motivada por vingança.","praticada à noite."],"Art. 146-A, caput.")
q(2,"A pena da perseguição é aumentada de metade se o crime é cometido",["mediante concurso de duas ou mais pessoas ou com emprego de arma.","de dia.","na internet.","por reincidente.","em local público."],"Art. 147-A, § 1º, III.")
q(2,"No crime de perseguição, procede-se",["mediante representação.","mediante queixa.","de ofício, sempre.","por requisição do Ministro da Justiça.","por requisição do juiz."],"Art. 147-A, § 3º.")
q(2,"As penas da perseguição são aplicadas",["sem prejuízo das correspondentes à violência.","em lugar das da violência.","apenas se não houver violência.","apenas com lesão grave.","apenas se a vítima for mulher."],"Art. 147-A, § 2º.")
q(2,"A pena da violência psicológica contra a mulher é aumentada de metade se o crime é cometido mediante uso de",["inteligência artificial ou outro recurso tecnológico que altere imagem ou som da vítima.","arma de fogo.","veículo.","dois ou mais agentes.","documento falso."],"Art. 147-B, parágrafo único.")
q(2,"O art. 147-C pune a ameaça no contexto de atuação de",["organização criminosa, com reclusão de um a três anos.","qualquer crime, com multa.","violência doméstica, com detenção.","rixa, com detenção.","contravenção, com multa."],"Art. 147-C.")
q(2,"A pena do sequestro é de reclusão de dois a cinco anos se a vítima é",["ascendente, descendente, cônjuge ou companheiro do agente ou maior de 60 anos.","qualquer pessoa.","estrangeira.","funcionária pública.","menor de 12 anos."],"Art. 148, § 1º, I.")
q(2,"A pena do sequestro é de reclusão de dois a cinco anos se o crime é praticado",["com fins libidinosos.","de dia.","em via pública.","por funcionário público.","com um comparsa."],"Art. 148, § 1º, V.")
q(2,"Se do sequestro resulta à vítima grave sofrimento físico ou moral, em razão de maus-tratos ou da natureza da detenção, a pena é de",["reclusão, de dois a oito anos.","reclusão, de um a três anos.","reclusão, de doze a vinte anos.","reclusão, de dois a cinco anos.","reclusão, de quatro a oito anos."],"Art. 148, § 2º.")
q(2,"O sequestro cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada tem pena de",["reclusão, de doze a vinte anos.","reclusão, de dois a oito anos.","reclusão, de um a três anos.","reclusão, de dois a cinco anos.","reclusão, de vinte a quarenta anos."],"Art. 148, § 3º.")
q(2,"Incorre nas mesmas penas do trabalho escravo quem",["cerceia o uso de qualquer meio de transporte do trabalhador, com o fim de retê-lo no local de trabalho.","paga o salário.","fornece alojamento adequado.","exige jornada legal.","contrata por prazo determinado."],"Art. 149, § 1º, I.")
q(2,"A pena do trabalho escravo é aumentada de metade se o crime é cometido",["contra criança ou adolescente, ou por preconceito de raça, cor, etnia, religião ou origem.","de dia.","por funcionário.","por estrangeiro.","em área urbana."],"Art. 149, § 2º.")
q(2,"É finalidade do tráfico de pessoas (art. 149-A)",["remoção de órgãos, tecidos ou partes do corpo.","comércio lícito.","doação voluntária.","estágio.","aprendizagem."],"Art. 149-A, I.")
q(2,"A pena do tráfico de pessoas é aumentada de um terço até a metade se o crime for cometido por",["funcionário público no exercício de suas funções ou a pretexto de exercê-las.","qualquer pessoa.","reincidente.","menor.","estrangeiro."],"Art. 149-A, § 1º, I.")
q(2,"No texto da perseguição, a ameaça de morte feita à ex-companheira, se por razões do sexo feminino, leva à pena",["em dobro, nos termos do art. 147, § 1º.","reduzida.","mantida.","em triplo.","aumentada de um terço."],"Art. 147, § 1º.","cp5a")
q(2,"No texto da fazenda, o fato de três trabalhadores terem 16 anos",["aumenta a pena de metade, nos termos do art. 149, § 2º, I.","reduz a pena.","é irrelevante.","exclui o crime.","transforma o crime em tráfico."],"Art. 149, § 2º, I.","cp5b")
q(2,"No texto da fazenda, a manutenção de seguranças armados na porta, para reter os trabalhadores, configura",["vigilância ostensiva com o fim de retê-los, nos termos do art. 149, § 1º, II.","legítima defesa.","exercício regular de direito.","estado de necessidade.","omissão de socorro."],"Art. 149, § 1º, II.","cp5b")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Constrangimento ilegal: detenção de três meses a um ano, ou multa; ameaça: detenção de um a seis meses, ou multa; sequestro: reclusão de um a três anos.","Constrangimento: reclusão; ameaça: reclusão; sequestro: detenção.","Ameaça: reclusão de um a três anos; sequestro: detenção de um a três anos.","Constrangimento: multa; ameaça: multa; sequestro: multa.","Perseguição: detenção; trabalho escravo: detenção."],"Arts. 146, 147 e 148.")
q(3,"Considere as afirmações. I. A perseguição tem pena de reclusão de seis meses a dois anos e multa. II. A ameaça se procede mediante representação, exceto contra a mulher por razões do sexo feminino. III. A violência psicológica contra a mulher tem pena de detenção. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A violência psicológica tem reclusão (art. 147-B).")
q(3,"Quanto ao art. 147-B, assinale a alternativa correta.",["Causar dano emocional à mulher, mediante ameaça, humilhação, manipulação, isolamento ou chantagem, é crime com pena de reclusão de seis meses a dois anos, e multa, se a conduta não constitui crime mais grave.","A pena é de detenção de um a seis meses.","A conduta só é punida se houver lesão física.","A pena é de multa.","É crime contra o patrimônio."],"Art. 147-B.")
q(3,"No sequestro, a pena é de reclusão de dois a cinco anos nas hipóteses do § 1º. Assinale a hipótese que NÃO consta do § 1º.",["Se o crime é praticado com emprego de arma.","Se a privação dura mais de quinze dias.","Se a vítima é menor de dezoito anos.","Se o crime é praticado com fins libidinosos.","Se há internação da vítima em casa de saúde ou hospital."],"O emprego de arma não está nas hipóteses do § 1º do art. 148.")
q(3,"O sequestro e o cárcere privado diferem porque, no sequestro,",["a vítima é levada e mantida em outro lugar; no cárcere privado, é mantida no mesmo lugar.","a vítima é sempre criança.","há violência física.","há dinheiro envolvido.","a vítima é sempre idosa."],"Art. 148 (distinção doutrinária).")
q(3,"No art. 149, a expressão “condições degradantes de trabalho” se refere a",["condições de trabalho que aviltam a dignidade do trabalhador.","salário baixo, apenas.","jornada de oito horas.","trabalho noturno.","trabalho em local fechado."],"Art. 149, caput.")
q(3,"A restrição da locomoção do trabalhador por dívida contraída com o empregador ou preposto é, nos termos do art. 149, forma de",["redução a condição análoga à de escravo.","exercício regular de direito.","contrato lícito.","cobrança legítima.","retenção salarial."],"Art. 149, caput.")
q(3,"O art. 149-A prevê, entre as finalidades do tráfico de pessoas, além da remoção de órgãos, a de",["submeter a vítima a trabalho em condições análogas à de escravo, a qualquer tipo de servidão, à adoção ilegal ou à exploração sexual.","comprar bens.","vender imóveis.","fazer turismo.","fazer pesquisa."],"Art. 149-A, II a V.")
q(3,"No tráfico de pessoas, a pena é aumentada de um terço até a metade se a vítima do tráfico for",["retirada do território nacional.","encontrada em outro bairro.","conhecida do agente.","maior de idade.","do sexo feminino, apenas."],"Art. 149-A, § 1º, IV.")
q(3,"No tráfico de pessoas, o agente se prevalecendo de relações de parentesco, domésticas, de coabitação, de hospitalidade, de dependência econômica, de autoridade ou de superioridade hierárquica",["tem a pena aumentada de um terço até a metade.","tem a pena reduzida.","é isento de pena.","tem a pena em dobro.","é punido por contravenção."],"Art. 149-A, § 1º, III.")
q(3,"Considere o crime de perseguição. O § 1º, II, aumenta a pena de metade se o crime é cometido contra",["mulher por razões da condição de sexo feminino.","qualquer homem.","qualquer adulto.","estrangeiro.","funcionário público."],"Art. 147-A, § 1º, II.")
q(3,"Assinale a INCORRETA sobre o crime de ameaça.",["A pena da ameaça é de reclusão de um a três anos.","A ameaça pode ser feita por palavra, escrito, gesto ou meio simbólico.","O mal prometido deve ser injusto e grave.","Contra a mulher por razões do sexo feminino, a pena é em dobro.","Em regra, procede-se mediante representação."],"A pena da ameaça simples é de detenção de um a seis meses, ou multa.")
q(3,"A pena do constrangimento ilegal é aplicada",["cumulativamente com a da violência.","em lugar da da violência.","apenas se a violência for leve.","apenas se não houver violência.","reduzida à metade."],"Art. 146, § 2º.")
q(3,"Em relação ao bullying, o art. 146-A prevê que a conduta, em ambiente digital, é punida com",["reclusão, de dois a quatro anos, e multa, se não constituir crime mais grave.","multa, apenas.","detenção, de um a seis meses.","reclusão, de um a três anos.","detenção, de três meses a um ano."],"Art. 146-A, parágrafo único.")
q(3,"No art. 148, a diferença entre as penas do caput e do § 1º é que, no § 1º, a pena de reclusão é de",["dois a cinco anos.","um a três anos.","dois a oito anos.","doze a vinte anos.","quatro a oito anos."],"Art. 148, § 1º.")
q(3,"A pena do trabalho escravo é de reclusão, e multa,",["além da pena correspondente à violência.","em lugar da pena da violência.","sem prejuízo, apenas, de multa.","apenas se houver lesão.","apenas se houver tortura."],"Art. 149, caput.")
q(3,"A pena do tráfico de pessoas é reduzida de um a dois terços se o agente for primário e",["não integrar organização criminosa.","integrar organização criminosa.","for funcionário público.","tiver mais de 60 anos.","for estrangeiro."],"Art. 149-A, § 2º.")
q(3,"No texto da perseguição, a situação da mulher que é seguida, recebe dezenas de mensagens e vê o ex-companheiro parado na frente de casa configura reiteração que",["invade ou perturba sua esfera de liberdade ou privacidade.","é lícita.","é mera contravenção.","é rixa.","depende de lesão."],"Art. 147-A, caput.","cp5a")
q(3,"No texto da perseguição, a ação penal, em regra, depende de",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 147-A, § 3º.","cp5a")
q(3,"No texto da fazenda, a sujeição dos trabalhadores a jornadas exaustivas e a alojamento sem água potável configura",["trabalho em condições análogas à de escravo.","trabalho regular.","estágio.","trabalho voluntário.","trabalho informal lícito."],"Art. 149, caput.","cp5b")
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes contra a liberdade pessoal",[
 ("constr","Constrangimento",["146: detenção, 3 meses a 1 ano","dobro com mais de 3 pessoas","bullying: multa"],"seção 1"),
 ("ameaca","Ameaça e perseguição",["147: 1 a 6 meses, ou multa","147-A: reclusão, 6 meses a 2 anos","violência psicológica"],"seção 2"),
 ("seq","Sequestro",["148: reclusão, 1 a 3 anos","§ 1º: 2 a 5 anos","milícia: 12 a 20"],"seção 3"),
 ("esc","Trabalho escravo",["149: reclusão, 2 a 8 anos","jornada exaustiva","condições degradantes"],"seção 4"),
 ("trafico","Tráfico de pessoas",["149-A: reclusão, 4 a 8 anos","remoção de órgãos, servidão","aumento: funcionário"],"seção 4"),
 ("rep","Ação penal",["ameaça: representação","perseguição: representação","contra a mulher: sem condição"],"seção 2")],
 "Na prova: leia a pena e se é reclusão ou detenção em cada artigo")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As primeiras caixas vão do constrangimento à perseguição; as demais tratam das privações de liberdade mais graves.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 146 a 149-A, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-5","Crimes contra a liberdade pessoal (CP, arts. 146 a 149-A)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 146 a 149-A. Cobertos: 146, 146-A, 147, 147-A, 147-B, 147-C, 148, 149 e 149-A."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto, em especial os arts. 146-A, 147-A, 147-B e 147-C, de redação recente.","O art. 147-A, § 1º, II, remete ao § 2º-A do art. 121, que está revogado; a remissão é da própria consolidação e deve ser conferida.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp5a e cp5b fictícios."],
 fontes_conferidas=["CP, arts. 146 a 149-A: texto da Câmara, copiado por programa."])
gravar("cp-5",aula_html,banco("cp-5",Q),tx)
