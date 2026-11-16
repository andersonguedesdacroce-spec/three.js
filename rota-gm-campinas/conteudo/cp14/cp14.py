import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Concussão, corrupção passiva, prevaricação e condescendência criminosa são os crimes funcionais mais cobrados e tocam diretamente o dia a dia do guarda: o agente que exige, solicita ou recebe vantagem, que deixa de agir para satisfazer interesse pessoal ou que tolera a falta de um subordinado. A Vunesp cobra os arts. 316 a 320 pela diferença entre exigir (concussão), solicitar ou receber (corrupção passiva) e retardar ou deixar de agir por interesse pessoal (prevaricação), pelas penas e pelo aumento da corrupção passiva. A aula segue o texto consolidado."
S={}
S[1]="## 1. Concussão e excesso de exação\n\n"+L("art. 316, caput","Art. 316. Exigir, para si ou para outrem","Excesso de exação")+"""

A concussão é exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida. A pena é de reclusão de dois a doze anos e multa. O verbo é exigir: o funcionário impõe, e a vítima cede por medo da função. É a diferença para a corrupção passiva, em que o verbo é solicitar ou receber. Note que o crime pode ser praticado fora da função ou antes de assumi-la, desde que em razão dela.

"""+L("art. 316, §§ 1º e 2º","Excesso de exação","Corrupção passiva")+"""

O excesso de exação é exigir tributo ou contribuição social que sabe ou deveria saber indevido, ou, quando devido, empregar na cobrança meio vexatório ou gravoso que a lei não autoriza, com reclusão de três a oito anos e multa. E, se o funcionário desvia, em proveito próprio ou de outrem, o que recebeu indevidamente para recolher aos cofres públicos, a pena é de dois a doze anos e multa.
"""
S[2]="## 2. Corrupção passiva\n\n"+L("art. 317, caput","Art. 317. Solicitar ou receber","§ 1º A pena é aumentada")+"\n\n"+L("art. 317, §§ 1º e 2º","§ 1º A pena é aumentada de um terço, se, em conseqüência da vantagem","Facilitação de contrabando")+"""

A corrupção passiva é solicitar ou receber, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida, ou aceitar promessa de tal vantagem. A pena é de reclusão de dois a doze anos e multa, a mesma da concussão. Os verbos são três: solicitar (pedir), receber e aceitar promessa. É um crime que se consuma com a solicitação, com o recebimento ou com a aceitação, e não depende de o ato ser praticado depois.

O § 1º aumenta a pena de um terço se, em consequência da vantagem ou promessa, o funcionário retarda ou deixa de praticar ato de ofício ou o pratica infringindo dever funcional. O § 2º é a corrupção passiva privilegiada: o funcionário pratica, deixa de praticar ou retarda ato de ofício, com infração de dever funcional, cedendo a pedido ou influência de outrem, e a pena é de detenção de três meses a um ano, ou multa. Aqui não há vantagem: há influência, o que reduz muito a pena.
"""
S[3]="## 3. Contrabando, prevaricação e condescendência\n\n"+L("art. 318","Art. 318. Facilitar, com infração","Prevaricação")+"\n\n"+L("art. 319","Art. 319. Retardar ou deixar","Art. 319-A.")+"\n\n"+L("art. 319-A","Art. 319-A. Deixar o Diretor","Condescendência criminosa")+"\n\n"+L("art. 320","Art. 320. Deixar o funcionário","Advocacia administrativa")+"""

A facilitação de contrabando ou descaminho (art. 318) é facilitar, com infração de dever funcional, a prática desses crimes, com reclusão de três a oito anos e multa. A prevaricação (art. 319) é retardar ou deixar de praticar, indevidamente, ato de ofício, ou praticá-lo contra disposição expressa de lei, para satisfazer interesse ou sentimento pessoal, com detenção de três meses a um ano e multa. A palavra decisiva é o móvel: o interesse ou sentimento pessoal, como a amizade, o ódio ou a vingança, e não uma vantagem, o que a distingue da corrupção. O art. 319-A pune o diretor de penitenciária ou o agente público que deixa de cumprir o dever de vedar ao preso o acesso a aparelho telefônico, de rádio ou similar, com detenção de três meses a um ano.

A condescendência criminosa (art. 320) é deixar o funcionário, por indulgência, de responsabilizar subordinado que cometeu infração no exercício do cargo ou, quando lhe falte competência, não levar o fato ao conhecimento da autoridade competente. A pena é de detenção de quinze dias a um mês, ou multa. O móvel é a indulgência, a bondade do chefe, que o faz tolerar a falta do subordinado.
"""
S[5]="""## 5. Na rotina do guarda

- **Pedido de dinheiro para liberar:** o guarda que exige dinheiro para não lavrar uma multa comete concussão; se apenas pede ou aceita, corrupção passiva.
- **Aceitar “um agrado”:** receber vantagem por ato do cargo é corrupção passiva, ainda que o ato seja legal.
- **Deixar de atuar por amizade:** não lavrar auto contra o amigo, por interesse ou sentimento pessoal, é prevaricação.
- **Chefia tolerante:** o inspetor que deixa de responsabilizar o guarda que errou, por pena, comete condescendência criminosa.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Verbo da concussão | Exigir |
| Verbos da corrupção passiva | Solicitar, receber ou aceitar promessa |
| Pena da concussão | Reclusão de dois a doze anos, e multa |
| Pena da corrupção passiva | Reclusão de dois a doze anos, e multa |
| Aumento da corrupção passiva | Um terço, se o funcionário retarda, deixa de praticar ou infringe dever (§ 1º) |
| Corrupção passiva privilegiada | Cede a pedido ou influência, sem vantagem: detenção de três meses a um ano, ou multa |
| Prevaricação | Retardar ou deixar de praticar ato, por interesse ou sentimento pessoal: detenção de três meses a um ano, e multa |
| Condescendência criminosa | Indulgência do chefe: detenção de quinze dias a um mês, ou multa |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Concussão | Exigir vantagem indevida: reclusão, 2 a 12 anos, e multa |
| Excesso de exação | Exigir tributo indevido ou cobrar com meio vexatório: reclusão, 3 a 8 anos |
| Corrupção passiva | Solicitar, receber ou aceitar promessa: reclusão, 2 a 12 anos, e multa |
| Aumento | 1/3, se retarda, deixa de praticar ou infringe dever |
| Privilegiada | Cede a pedido ou influência: detenção, 3 meses a 1 ano, ou multa |
| Facilitação de contrabando | Reclusão, 3 a 8 anos, e multa |
| Prevaricação | Detenção, 3 meses a 1 ano, e multa; interesse ou sentimento pessoal |
| Condescendência criminosa | Detenção, 15 dias a 1 mês, ou multa |
"""
QR=[("Questão 1","O funcionário público que exige, para si, vantagem indevida, em razão da função, comete",["concussão.","corrupção passiva.","prevaricação.","peculato.","extorsão."],0,"Art. 316."),
("Questão 2","O funcionário que solicita ou recebe vantagem indevida, em razão da função, comete",["corrupção passiva.","concussão.","prevaricação.","peculato.","condescendência."],2,"Art. 317."),
("Questão 3","O funcionário que deixa de praticar ato de ofício para satisfazer interesse ou sentimento pessoal comete",["prevaricação.","corrupção passiva.","concussão.","peculato.","abuso de poder."],1,"Art. 319."),
("Questão 4","O funcionário que, por indulgência, deixa de responsabilizar subordinado que cometeu infração comete",["condescendência criminosa.","prevaricação.","corrupção passiva.","concussão.","advocacia administrativa."],4,"Art. 320.")]
t1="<strong>Multa em troca de dinheiro</strong><br><br>Um guarda municipal de Vila Nova, cidade fictícia, parou um motorista que estacionou em local proibido e disse que, para não lavrar a multa, o motorista deveria lhe entregar R$ 100,00. O motorista, com medo de ser prejudicado, entregou o dinheiro."
t2="<strong>Agrado por um favor</strong><br><br>Um servidor da Prefeitura pediu a um comerciante R$ 500,00 para agilizar a liberação de um alvará que o comerciante tinha direito de receber. O comerciante pagou, e o alvará foi liberado em dois dias, mais rápido que o normal. Em outro caso, o mesmo servidor deixou de fiscalizar o estabelecimento de um amigo, por amizade."
tx={"cp14a":t1,"cp14b":t2}
# n=1
q(1,"A pena da concussão é de",["reclusão, de dois a doze anos, e multa.","reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","reclusão, de quatro a oito anos.","detenção, de um a três meses."],"Art. 316, caput.")
q(1,"O verbo da concussão é",["exigir.","solicitar.","receber.","aceitar.","oferecer."],"Art. 316, caput.")
q(1,"Na concussão, a vantagem exigida é",["indevida, em razão da função.","devida.","legal.","gratuita.","irrelevante."],"Art. 316, caput.")
q(1,"A concussão pode ser praticada",["ainda que fora da função ou antes de assumi-la, mas em razão dela.","apenas no exercício da função.","apenas depois de deixar a função.","apenas por quem está de serviço.","apenas em horário de expediente."],"Art. 316, caput.")
q(1,"O excesso de exação é exigir tributo ou contribuição social que o funcionário sabe ou deveria saber",["indevido.","devido.","pago.","prescrito.","pequeno."],"Art. 316, § 1º.")
q(1,"A pena do excesso de exação é de",["reclusão, de três a oito anos, e multa.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],"Art. 316, § 1º.")
q(1,"A pena da corrupção passiva é de",["reclusão, de dois a doze anos, e multa.","reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","reclusão, de quatro a oito anos.","detenção, de um a três meses."],"Art. 317, caput.")
q(1,"Os verbos da corrupção passiva são solicitar, receber ou",["aceitar promessa de vantagem indevida.","exigir.","oferecer.","pagar.","entregar."],"Art. 317, caput.")
q(1,"A pena da corrupção passiva é aumentada de um terço se, em consequência da vantagem ou promessa, o funcionário",["retarda ou deixa de praticar ato de ofício, ou o pratica infringindo dever funcional.","pratica o ato legal.","devolve a vantagem.","comunica a autoridade.","pede demissão."],"Art. 317, § 1º.")
q(1,"A corrupção passiva privilegiada (§ 2º) tem pena de",["detenção, de três meses a um ano, ou multa.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de um a três meses.","multa, apenas."],"Art. 317, § 2º.")
q(1,"Na corrupção passiva privilegiada, o funcionário cede a",["pedido ou influência de outrem.","vantagem.","dinheiro.","presente.","promessa."],"Art. 317, § 2º.")
q(1,"A facilitação de contrabando ou descaminho tem pena de",["reclusão, de três a oito anos, e multa.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],"Art. 318.")
q(1,"A pena da prevaricação é de",["detenção, de três meses a um ano, e multa.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de um a três meses.","multa, apenas."],"Art. 319.")
q(1,"Na prevaricação, o funcionário retarda ou deixa de praticar ato de ofício para satisfazer",["interesse ou sentimento pessoal.","vantagem econômica.","ordem do chefe.","necessidade do serviço.","erro."],"Art. 319.")
q(1,"A pena da condescendência criminosa é de",["detenção, de quinze dias a um mês, ou multa.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa, apenas."],"Art. 320.")
q(1,"A condescendência criminosa é deixar o funcionário, por indulgência, de responsabilizar",["subordinado que cometeu infração no exercício do cargo.","chefe que errou.","colega de outro órgão.","cidadão.","testemunha."],"Art. 320.")
q(1,"O art. 319-A pune o agente público que deixa de vedar ao preso o acesso a",["aparelho telefônico, de rádio ou similar.","livro.","televisão.","jornal.","visita."],"Art. 319-A.")
q(1,"A pena do art. 319-A é de",["detenção, de três meses a um ano.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de um a três meses.","multa."],"Art. 319-A.")
q(1,"No texto da multa em troca de dinheiro, o guarda que impõe o pagamento, sob pena de lavrar a multa, comete, em tese,",["concussão.","corrupção passiva.","prevaricação.","peculato.","condescendência criminosa."],"Art. 316: exigiu vantagem.","cp14a")
q(1,"No texto do agrado, o servidor que pediu R$ 500,00 para agilizar o alvará comete, em tese,",["corrupção passiva, pois solicitou vantagem.","concussão, pois exigiu.","prevaricação.","peculato.","condescendência."],"Art. 317, caput.","cp14b")
# n=2
q(2,"A diferença entre concussão e corrupção passiva está no verbo: na concussão, o funcionário",["exige; na corrupção passiva, solicita ou recebe.","solicita; na corrupção, exige.","recebe; na corrupção, exige.","aceita; na corrupção, exige.","oferece; na corrupção, exige."],"Arts. 316 e 317.")
q(2,"Na concussão, a vítima entrega a vantagem por",["medo de represália do funcionário.","vontade própria apenas.","erro.","engano.","gratidão."],"Art. 316 (sentido doutrinário).")
q(2,"Ainda quanto à concussão, o § 2º do art. 316 trata do funcionário que desvia o que recebeu indevidamente para recolher",["aos cofres públicos.","ao banco.","ao comerciante.","ao amigo.","à família."],"Art. 316, § 2º.")
q(2,"A pena do § 2º do art. 316 é de",["reclusão, de dois a doze anos, e multa.","reclusão, de três a oito anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],"Art. 316, § 2º.")
q(2,"O excesso de exação também se configura quando, sendo o tributo devido, o funcionário emprega na cobrança meio",["vexatório ou gravoso que a lei não autoriza.","legal.","autorizado.","educado.","gratuito."],"Art. 316, § 1º.")
q(2,"A corrupção passiva pode ser praticada, nos termos do art. 317, direta ou",["indiretamente.","apenas diretamente.","apenas por escrito.","apenas por intermediário.","apenas em dinheiro."],"Art. 317, caput.")
q(2,"A corrupção passiva exige que a vantagem seja",["indevida.","devida.","legal.","irrelevante.","pequena."],"Art. 317, caput.")
q(2,"O crime de corrupção passiva se consuma com a solicitação, o recebimento ou a aceitação de promessa",["independentemente da prática do ato.","apenas com a prática do ato.","apenas com o recebimento.","apenas com o pagamento.","apenas com a denúncia."],"Art. 317, caput.")
q(2,"A corrupção passiva privilegiada difere da do caput porque, no § 2º,",["o funcionário cede a pedido ou influência, e não por vantagem.","o funcionário exige.","o funcionário recebe.","há violência.","há ameaça."],"Art. 317, § 2º.")
q(2,"A facilitação de contrabando ou descaminho (art. 318) é praticada com infração de",["dever funcional.","regra de trânsito.","regra de etiqueta.","norma de vizinhança.","contrato."],"Art. 318.")
q(2,"Na prevaricação, o funcionário pode também praticar o ato",["contra disposição expressa de lei.","conforme a lei.","por ordem do juiz.","por ordem do chefe.","por obrigação."],"Art. 319.")
q(2,"A prevaricação difere da corrupção passiva porque, na prevaricação, o móvel é",["interesse ou sentimento pessoal, e não vantagem indevida.","vantagem indevida.","ordem superior.","medo.","erro."],"Arts. 317 e 319.")
q(2,"A condescendência criminosa também ocorre quando, faltando competência para responsabilizar o subordinado, o funcionário",["não leva o fato ao conhecimento da autoridade competente.","pede demissão.","comunica a imprensa.","aplica sanção.","arquiva o fato."],"Art. 320.")
q(2,"O móvel da condescendência criminosa é a",["indulgência.","vantagem.","vingança.","ordem.","necessidade."],"Art. 320.")
q(2,"A pena da condescendência criminosa é bem menor que a da prevaricação porque, na condescendência,",["o móvel é a indulgência, de menor reprovação.","há vantagem.","há violência.","há dano.","há fraude."],"Arts. 319 e 320.")
q(2,"No texto da multa em troca de dinheiro, o guarda exigiu a vantagem porque, na hipótese, o motorista",["cedeu por medo de ser prejudicado.","cedeu por vontade livre.","cedeu por erro.","cedeu por troca.","cedeu por consentimento."],"Art. 316.","cp14a")
q(2,"No texto do agrado, o fato de o alvará ser devido e liberado mais rápido",["não exclui a corrupção passiva, pois a vantagem é indevida.","exclui o crime.","transforma em prevaricação.","transforma em concussão.","reduz a pena."],"Art. 317, caput.","cp14b")
q(2,"No texto do agrado, o fato de o servidor ter deixado de fiscalizar o estabelecimento do amigo por amizade configura, em tese,",["prevaricação.","corrupção passiva.","concussão.","peculato.","condescendência."],"Art. 319.","cp14b")
q(2,"A pena mínima da concussão e da corrupção passiva é de",["dois anos de reclusão.","um ano de reclusão.","três meses de detenção.","seis meses de reclusão.","quatro anos de reclusão."],"Arts. 316 e 317.")
q(2,"A pena mínima da prevaricação é de",["três meses de detenção.","um ano de reclusão.","quinze dias de detenção.","dois anos de reclusão.","um mês de reclusão."],"Art. 319.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Concussão: reclusão de dois a doze anos e multa; corrupção passiva: reclusão de dois a doze anos e multa; prevaricação: detenção de três meses a um ano e multa.","Concussão: detenção; prevaricação: reclusão.","Corrupção passiva: detenção de três meses a um ano; concussão: multa.","Prevaricação: reclusão de dois a doze anos.","Condescendência: reclusão de um a quatro anos."],"Arts. 316, 317 e 319.")
q(3,"Considere as afirmações. I. Na concussão, o verbo é exigir. II. Na corrupção passiva, os verbos são solicitar, receber e aceitar promessa. III. A prevaricação exige vantagem econômica. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A prevaricação exige interesse ou sentimento pessoal, e não vantagem (art. 319).")
q(3,"Assinale a INCORRETA.",["A concussão tem pena de detenção de três meses a um ano.","A corrupção passiva tem pena de reclusão de dois a doze anos e multa.","A prevaricação tem pena de detenção de três meses a um ano e multa.","A condescendência criminosa tem pena de detenção de quinze dias a um mês, ou multa.","A facilitação de contrabando tem pena de reclusão de três a oito anos e multa."],"A concussão tem reclusão de dois a doze anos e multa.")
q(3,"A diferença entre a corrupção passiva do caput e a privilegiada do § 2º é que, nesta última,",["o funcionário cede a pedido ou influência de outrem, sem vantagem.","o funcionário exige.","há violência.","há ameaça.","há arma."],"Art. 317, § 2º.")
q(3,"O aumento do § 1º do art. 317 incide quando, em consequência da vantagem ou promessa, o funcionário",["retarda ou deixa de praticar ato de ofício, ou o pratica infringindo dever funcional.","paga o ato.","recebe e devolve.","pratica ato legal.","comunica a autoridade."],"Art. 317, § 1º.")
q(3,"A corrupção passiva pode ser praticada por quem ainda não assumiu a função, desde que a vantagem seja pedida",["em razão dela.","por parente.","por terceiro estranho.","depois da posse.","sem relação com a função."],"Art. 317, caput.")
q(3,"A concussão e a corrupção passiva têm a mesma pena, mas diferem, principalmente, quanto ao",["verbo do tipo e à intimidação da vítima.","valor.","local.","horário.","sujeito passivo."],"Arts. 316 e 317.")
q(3,"Na prevaricação, o “interesse ou sentimento pessoal” pode ser, por exemplo,",["amizade, ódio ou vingança.","ordem do chefe.","necessidade.","erro.","vantagem econômica."],"Art. 319.")
q(3,"A facilitação de contrabando ou descaminho exige que o funcionário infrinja",["dever funcional.","regra de convivência.","norma de etiqueta.","regra de trânsito.","contrato civil."],"Art. 318.")
q(3,"A diferença entre prevaricação e condescendência criminosa é que, na condescendência, o funcionário",["deixa de responsabilizar subordinado por indulgência.","pratica ato por interesse pessoal.","exige vantagem.","solicita vantagem.","recebe vantagem."],"Arts. 319 e 320.")
q(3,"O art. 319-A é crime praticado por",["diretor de penitenciária ou agente público.","qualquer particular.","apenas preso.","apenas visitante.","apenas advogado."],"Art. 319-A.")
q(3,"A pena de reclusão de três a oito anos e multa corresponde a",["facilitação de contrabando ou descaminho.","prevaricação.","condescendência criminosa.","corrupção passiva privilegiada.","art. 319-A."],"Art. 318.")
q(3,"No excesso de exação, o funcionário exige tributo que “sabe ou deveria saber indevido”, o que significa que o crime admite",["dolo direto e dolo eventual.","apenas culpa.","apenas dolo direto.","apenas ato comissivo.","apenas ato omissivo."],"Art. 316, § 1º.")
q(3,"Assinale a alternativa correta sobre as figuras de omissão funcional.",["Prevaricação: interesse ou sentimento pessoal; condescendência criminosa: indulgência com o subordinado.","Prevaricação: indulgência; condescendência: interesse pessoal.","Ambas exigem vantagem econômica.","Ambas são de reclusão.","Ambas são de ação privada."],"Arts. 319 e 320.")
q(3,"Assinale a alternativa que associa corretamente o artigo ao crime.",["316: concussão; 317: corrupção passiva; 318: facilitação de contrabando; 319: prevaricação; 320: condescendência criminosa.","316: corrupção passiva; 317: concussão.","318: prevaricação; 319: contrabando.","320: concussão; 316: condescendência.","317: prevaricação; 319: corrupção passiva."],"Arts. 316 a 320.")
q(3,"A concussão difere do crime de extorsão do art. 158 porque, na concussão, o agente é",["funcionário público que exige a vantagem em razão da função.","qualquer pessoa, com violência.","qualquer pessoa, com ameaça.","particular, com fraude.","particular, com arma."],"Art. 316, caput.")
q(3,"O § 1º do art. 317 aumenta a pena em um terço. Considerada a pena do caput, o aumento incide sobre a pena de",["reclusão, de dois a doze anos, e multa.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","detenção, de quinze dias a um mês.","multa."],"Art. 317, caput e § 1º.")
q(3,"No texto da multa em troca de dinheiro, a pena do crime é de",["reclusão, de dois a doze anos, e multa.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","detenção, de quinze dias a um mês.","multa."],"Art. 316, caput.","cp14a")
q(3,"No texto do agrado, a pena do crime de corrupção passiva do alvará é de",["reclusão, de dois a doze anos, e multa.","detenção, de três meses a um ano, e multa.","detenção, de quinze dias a um mês.","reclusão, de um a quatro anos.","multa."],"Art. 317, caput.","cp14b")
q(3,"No texto do agrado, a pena do crime em que o servidor deixou de fiscalizar o amigo é de",["detenção, de três meses a um ano, e multa.","reclusão, de dois a doze anos.","detenção, de quinze dias a um mês.","reclusão, de um a quatro anos.","multa."],"Art. 319.","cp14b")
assert len(Q)==60,len(Q)
code,svg=mapa("Concussão, corrupção, prevaricação e condescendência",[
 ("conc","Concussão",["exigir vantagem indevida","reclusão, 2 a 12 anos","excesso de exação: 3 a 8 anos"],"seção 1"),
 ("corr","Corrupção passiva",["solicitar, receber, aceitar","reclusão, 2 a 12 anos","§ 1º: aumento de 1/3"],"seção 2"),
 ("priv","Corrupção privilegiada",["cede a pedido ou influência","detenção, 3 meses a 1 ano","ou multa"],"seção 2"),
 ("conf","Contrabando",["art. 318","reclusão, 3 a 8 anos","infração de dever funcional"],"seção 3"),
 ("prev","Prevaricação",["art. 319","interesse ou sentimento pessoal","detenção, 3 meses a 1 ano"],"seção 3"),
 ("cond","Condescendência",["art. 320","indulgência com o subordinado","detenção, 15 dias a 1 mês"],"seção 3")],
 "Na prova: exigir é concussão; solicitar ou receber é corrupção; interesse pessoal é prevaricação")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As três primeiras caixas distinguem os crimes pelo verbo e pelo móvel; as demais fecham o quadro dos crimes funcionais de omissão.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 316 a 320, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-14","Concussão, corrupção passiva, prevaricação e condescendência (CP, arts. 316 a 320)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 316 a 320. Cobertos: 316, 317, 318, 319, 319-A e 320."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","As expressões corrupção passiva privilegiada e concussão (sentido de intimidação) são doutrinárias.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp14a e cp14b fictícios."],
 fontes_conferidas=["CP, arts. 316 a 320: texto da Câmara, copiado por programa."])
gravar("cp-14",aula_html,banco("cp-14",Q),tx)
