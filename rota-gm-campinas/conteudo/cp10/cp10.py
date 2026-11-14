import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A apropriação indébita é o crime de quem, tendo a posse ou a detenção de coisa alheia, passa a agir como dono. Na prova, os arts. 168 a 170 aparecem pela diferença para o furto (aqui o agente já tem a coisa), pelas causas de aumento (depósito necessário, cargos de confiança, ofício), pela apropriação previdenciária e pelas figuras da coisa achada e do tesouro. O art. 170, que estende o privilégio do furto a este capítulo, completa o tema."
S={}
S[1]="## 1. Apropriação indébita\n\n"+L("art. 168, caput e § 1º","Art. 168. Apropriar-se de coisa alheia móvel","Apropriação indébita previdenciária")+"""

Na apropriação indébita, o agente se apropria de coisa alheia móvel de que tem a posse ou a detenção. A pena é de reclusão de um a quatro anos e multa. A chave é que a coisa chegou às mãos do agente legitimamente, por confiança: o vizinho que pede emprestada a furadeira e não devolve, ou o depositário que vende o bem guardado. No furto, o agente toma a coisa; aqui, ele a recebeu e inverte o ânimo, passando a agir como dono. A pena aumenta de um terço quando o agente recebeu a coisa em depósito necessário, na qualidade de tutor, curador, síndico, liquidatário, inventariante, testamenteiro ou depositário judicial, ou em razão de ofício, emprego ou profissão.
"""
S[2]="## 2. Apropriação indébita previdenciária\n\n"+L("art. 168-A, caput e § 1º","Art. 168-A. Deixar de repassar","§ 2º É extinta a punibilidade")+"\n\n"+L("art. 168-A, §§ 2º e 3º","§ 2º É extinta a punibilidade","§ 4º A faculdade")+"""

A apropriação indébita previdenciária é deixar de repassar à previdência social as contribuições recolhidas dos contribuintes, no prazo e na forma legal ou convencional. A pena é de reclusão de dois a cinco anos e multa. Incorre nas mesmas penas quem deixa de recolher contribuição descontada de pagamento a segurados, quem deixa de recolher contribuições que integraram custos da venda de produtos ou serviços e quem deixa de pagar benefício a segurado quando a previdência já reembolsou a empresa. A punibilidade é extinta se o agente, espontaneamente, declara, confessa e paga antes do início da ação fiscal. O juiz pode deixar de aplicar a pena ou aplicar só a multa se o agente é primário e de bons antecedentes e promoveu o pagamento antes da denúncia ou o valor devido é igual ou inferior ao mínimo para execução fiscal. A extinção de punibilidade não se aplica ao devedor contumaz declarado em decisão administrativa definitiva.
"""
S[3]="## 3. Coisa havida por erro, coisa achada e tesouro\n\n"+L("art. 169","Art. 169. Apropriar-se alguém de coisa alheia vinda","Art. 170.")+"\n\n"+L("art. 170","Art. 170. Nos crimes previstos neste capítulo","CAPÍTULO VI")+"""

Apropriar-se de coisa alheia que veio ao poder do agente por erro, caso fortuito ou força da natureza tem pena de detenção de um mês a um ano, ou multa. Na mesma pena incorre quem acha tesouro em prédio alheio e se apropria, no todo ou em parte, da quota do proprietário, e quem acha coisa alheia perdida e dela se apropria, deixando de restituí-la ao dono ou de entregá-la à autoridade competente no prazo de quinze dias. O prazo de quinze dias é a pegadinha: quem acha tem esse tempo para devolver ou entregar. O art. 170 manda aplicar a este capítulo o privilégio do art. 155, § 2º (primário e coisa de pequeno valor).
"""
S[5]="""## 5. Na rotina do guarda

- **Objeto achado:** o guarda que recebe objeto perdido deve entregá-lo à autoridade ou ao dono, e registrar, porque a apropriação de coisa achada é crime.
- **Recebimento de bens apreendidos:** o agente que guarda bens apreendidos tem a posse em razão de ofício, o que aumenta a pena da apropriação indébita em um terço.
- **Erro na entrega:** quem recebe coisa por engano e a retém comete o crime do art. 169.
- **Depositário:** quem recebe coisa em depósito, inclusive judicial, responde com aumento se se apropria dela.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Confundir com furto | Na apropriação indébita, o agente já tem a posse ou a detenção da coisa |
| Pena da apropriação indébita | Reclusão de um a quatro anos, e multa |
| Aumento de um terço | Depósito necessário, tutor, curador, etc., ofício, emprego ou profissão |
| Pena da apropriação previdenciária | Reclusão de dois a cinco anos, e multa |
| Coisa achada | Prazo de quinze dias para restituir ou entregar à autoridade |
| Pena do art. 169 | Detenção de um mês a um ano, ou multa |
| Privilégio no capítulo | O art. 170 manda aplicar o art. 155, § 2º |
| Extinção da punibilidade previdenciária | Declarar, confessar e pagar antes do início da ação fiscal |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Apropriação indébita | Reclusão, 1 a 4 anos, e multa; posse ou detenção legítima |
| Aumento de 1/3 | Depósito necessário; tutor, curador etc.; ofício, emprego ou profissão |
| Previdenciária | Reclusão, 2 a 5 anos, e multa; não repassar contribuição |
| Extinção da punibilidade | Declara, confessa e paga antes da ação fiscal |
| Coisa havida por erro | Detenção, 1 mês a 1 ano, ou multa |
| Coisa achada | Restituir ou entregar à autoridade em 15 dias |
| Tesouro | Apropriar-se da quota do proprietário do prédio |
| Privilégio | Art. 170: aplica-se o art. 155, § 2º |
"""
QR=[("Questão 1","A pena da apropriação indébita (art. 168, caput) é de",["reclusão, de um a quatro anos, e multa.","reclusão, de um a seis anos, e multa.","detenção, de um mês a um ano.","reclusão, de dois a cinco anos.","reclusão, de seis a dez anos."],0,"Art. 168, caput."),
("Questão 2","A pena da apropriação indébita é aumentada de um terço quando o agente recebeu a coisa",["em razão de ofício, emprego ou profissão.","por doação.","por herança.","por compra.","por empréstimo de amigo."],2,"Art. 168, § 1º, III."),
("Questão 3","Quem acha coisa alheia perdida e dela se apropria, deixando de restituí-la ou de entregá-la à autoridade competente dentro do prazo de",["quinze dias, comete o crime do art. 169, parágrafo único, II.","cinco dias.","trinta dias.","dez dias.","sessenta dias."],1,"Art. 169, parágrafo único, II."),
("Questão 4","A pena da apropriação indébita previdenciária é de",["reclusão, de dois a cinco anos, e multa.","reclusão, de um a quatro anos.","detenção, de um mês a um ano.","reclusão, de três a oito anos.","multa."],4,"Art. 168-A.")]
t1="<strong>Bens apreendidos desaparecem</strong><br><br>Um servidor municipal, responsável pela guarda de bens apreendidos pela Guarda de Vila Nova, cidade fictícia, vendeu parte desses bens e ficou com o dinheiro. Ele tinha a guarda dos bens em razão do cargo."
t2="<strong>Carteira achada na praça</strong><br><br>Um homem achou uma carteira com documentos e dinheiro em uma praça. Em vez de entregá-la a uma autoridade ou ao dono, guardou o dinheiro e descartou a carteira. Sabia a quem pertencia, pois havia documento de identificação."
tx={"cp10a":t1,"cp10b":t2}
# n=1
q(1,"A pena da apropriação indébita é de",["reclusão, de um a quatro anos, e multa.","reclusão, de um a seis anos, e multa.","detenção, de um mês a um ano.","reclusão, de dois a cinco anos.","reclusão, de seis a dez anos."],"Art. 168, caput.")
q(1,"Na apropriação indébita, o agente se apropria de coisa alheia móvel de que tem",["a posse ou a detenção.","apenas a propriedade.","nenhum contato.","apenas o uso proibido.","nenhuma ciência."],"Art. 168, caput.")
q(1,"A pena da apropriação indébita é aumentada de um terço quando o agente recebeu a coisa em",["depósito necessário.","depósito voluntário.","venda.","doação.","herança."],"Art. 168, § 1º, I.")
q(1,"A pena da apropriação indébita é aumentada de um terço quando o agente recebeu a coisa na qualidade de",["tutor, curador, síndico, liquidatário, inventariante, testamenteiro ou depositário judicial.","comprador.","vizinho.","amigo.","herdeiro."],"Art. 168, § 1º, II.")
q(1,"A pena da apropriação indébita é aumentada de um terço quando o agente recebeu a coisa em razão de",["ofício, emprego ou profissão.","amizade.","parentesco.","vizinhança.","herança."],"Art. 168, § 1º, III.")
q(1,"Deixar de repassar à previdência social as contribuições recolhidas dos contribuintes é crime com pena de",["reclusão, de dois a cinco anos, e multa.","detenção, de um mês a um ano.","reclusão, de um a quatro anos.","multa.","reclusão, de quatro a oito anos."],"Art. 168-A.")
q(1,"A punibilidade é extinta, na apropriação previdenciária, se o agente, espontaneamente, declara, confessa e paga",["antes do início da ação fiscal.","depois da sentença.","depois da denúncia.","a qualquer tempo.","depois do trânsito em julgado."],"Art. 168-A, § 2º.")
q(1,"A pena do crime de apropriação de coisa havida por erro, caso fortuito ou força da natureza é de",["detenção, de um mês a um ano, ou multa.","reclusão, de um a quatro anos.","reclusão, de dois a cinco anos.","detenção, de um a quatro anos.","multa, apenas."],"Art. 169, caput.")
q(1,"Quem acha tesouro em prédio alheio e se apropria, no todo ou em parte, da quota do proprietário do prédio incorre na",["mesma pena do art. 169, caput.","pena do furto.","pena do roubo.","pena da extorsão.","pena do dano."],"Art. 169, parágrafo único, I.")
q(1,"Quem acha coisa alheia perdida deve restituí-la ao dono ou entregá-la à autoridade competente em",["quinze dias.","cinco dias.","trinta dias.","dez dias.","sessenta dias."],"Art. 169, parágrafo único, II.")
q(1,"O art. 170 manda aplicar aos crimes do capítulo da apropriação indébita",["o disposto no art. 155, § 2º.","o disposto no art. 155, § 4º.","o disposto no art. 157.","o disposto no art. 163.","o disposto no art. 171."],"Art. 170.")
q(1,"A principal diferença entre apropriação indébita e furto é que, na apropriação indébita,",["o agente já tem a posse ou a detenção da coisa.","há violência.","há ameaça.","há fraude.","a coisa é imóvel."],"Arts. 155 e 168.")
q(1,"No § 1º do art. 168, o depositário judicial é exemplo de",["causa de aumento de um terço.","causa de diminuição.","excludente de ilicitude.","atenuante.","causa de extinção."],"Art. 168, § 1º, II.")
q(1,"A apropriação indébita previdenciária consiste em deixar de repassar à previdência social as contribuições",["recolhidas dos contribuintes.","devidas pelo agente apenas.","futuras.","de terceiros não recolhidas.","prescritas."],"Art. 168-A, caput.")
q(1,"Incorre nas mesmas penas da apropriação previdenciária quem deixa de recolher, no prazo legal, contribuição",["descontada de pagamento efetuado a segurados, a terceiros ou arrecadada do público.","que não foi descontada.","que não é devida.","já paga.","já prescrita."],"Art. 168-A, § 1º, I.")
q(1,"O juiz pode deixar de aplicar a pena ou aplicar somente a de multa, na apropriação previdenciária, se o agente é",["primário e de bons antecedentes, nas hipóteses do § 3º.","reincidente.","funcionário público.","menor.","estrangeiro."],"Art. 168-A, § 3º.")
q(1,"O art. 169 trata, entre outras figuras, da apropriação de coisa",["achada.","comprada.","herdada.","doada.","emprestada."],"Art. 169, parágrafo único, II.")
q(1,"No texto dos bens apreendidos, o servidor se apropriou de bens de que tinha a guarda. Em tese, o crime é de",["apropriação indébita, com aumento de um terço.","furto.","roubo.","estelionato.","extorsão."],"Art. 168, § 1º, III: em razão do cargo.","cp10a")
q(1,"No texto da carteira, ao guardar o dinheiro de carteira achada, sabendo quem era o dono, o homem pratica, em tese,",["apropriação de coisa achada.","furto.","roubo.","extorsão.","estelionato."],"Art. 169, parágrafo único, II.","cp10b")
q(1,"A pena mínima da apropriação indébita simples é de",["um ano de reclusão.","seis meses de detenção.","dois anos de reclusão.","um mês de detenção.","quatro anos de reclusão."],"Art. 168, caput.")
# n=2
q(2,"A apropriação indébita tem como elemento o fato de a coisa ter chegado ao agente",["legitimamente, por confiança, e depois ele passar a agir como dono.","por violência.","por fraude.","por ameaça.","por subtração."],"Art. 168, caput.")
q(2,"O depósito necessário, no § 1º do art. 168, é aquele em que o agente recebe a coisa",["por obrigação ou circunstância, como nas calamidades ou por força de lei.","por compra.","por empréstimo.","por troca.","por doação."],"Art. 168, § 1º, I.")
q(2,"Na apropriação previdenciária, o prazo e a forma legal ou convencional referem-se ao",["repasse das contribuições recolhidas.","pagamento do salário.","pagamento de impostos municipais.","recebimento de multas.","recolhimento do FGTS."],"Art. 168-A, caput.")
q(2,"Incorre nas mesmas penas da apropriação previdenciária quem deixa de pagar benefício devido a segurado quando",["as cotas ou valores já tiverem sido reembolsados à empresa pela previdência.","o segurado não pediu.","o segurado faleceu.","o benefício é indevido.","o benefício foi pago."],"Art. 168-A, § 1º, III.")
q(2,"O juiz pode deixar de aplicar a pena na apropriação previdenciária se o valor das contribuições devidas é",["igual ou inferior ao estabelecido administrativamente como mínimo para execução fiscal.","muito alto.","desconhecido.","impossível de calcular.","superior ao mínimo."],"Art. 168-A, § 3º, II.")
q(2,"A extinção de punibilidade do § 2º do art. 168-A não se aplica ao",["devedor contumaz declarado em decisão administrativa definitiva.","devedor primário.","devedor de bons antecedentes.","devedor que paga.","devedor menor."],"Art. 168-A, § 5º.")
q(2,"No art. 169, a apropriação de coisa alheia vinda ao poder do agente por",["erro, caso fortuito ou força da natureza.","violência.","ameaça.","fraude.","contrato de depósito."],"Art. 169, caput.")
q(2,"O tesouro de que trata o art. 169 é achado em",["prédio alheio.","prédio próprio.","terreno público, apenas.","rua.","praia."],"Art. 169, parágrafo único, I.")
q(2,"Na apropriação de coisa achada, a conduta típica é apropriar-se da coisa, deixando de restituí-la ao dono ou legítimo possuidor ou de entregá-la",["à autoridade competente, dentro do prazo de quinze dias.","a um vizinho.","a um amigo.","ao Município.","a um parente."],"Art. 169, parágrafo único, II.")
q(2,"Aplica-se o privilégio do art. 155, § 2º, à apropriação indébita se o criminoso é",["primário e a coisa é de pequeno valor.","reincidente.","funcionário público.","menor.","estrangeiro."],"Art. 170.")
q(2,"A apropriação indébita praticada por inventariante tem pena",["aumentada de um terço.","reduzida de um terço.","dobrada.","mantida.","extinta."],"Art. 168, § 1º, II.")
q(2,"O § 4º do art. 168-A afasta a faculdade do § 3º nos casos de parcelamento de contribuições cujo valor seja",["superior ao mínimo para ajuizamento de execuções fiscais.","inferior ao mínimo.","igual ao mínimo.","inexistente.","irrelevante."],"Art. 168-A, § 4º.")
q(2,"No art. 168-A, § 1º, II, também incorre nas mesmas penas quem deixa de recolher contribuições",["que integraram despesas contábeis ou custos relativos à venda de produtos ou à prestação de serviços.","que não foram devidas.","que foram pagas.","que prescreveram.","que foram parceladas."],"Art. 168-A, § 1º, II.")
q(2,"A pena do crime de apropriação indébita pode ser agravada, em razão do cargo, porque",["o agente recebeu a coisa em razão de ofício, emprego ou profissão.","o agente é idoso.","o agente é menor.","o agente é estrangeiro.","o agente é reincidente."],"Art. 168, § 1º, III.")
q(2,"No texto dos bens apreendidos, a pena-base da apropriação indébita é de",["reclusão, de um a quatro anos, e multa.","reclusão, de um a seis anos.","detenção, de um mês a um ano.","reclusão, de dois a cinco anos.","multa."],"Art. 168, caput.","cp10a")
q(2,"No texto dos bens apreendidos, com o aumento de um terço do § 1º, a pena máxima abstrata seria de",["cinco anos e quatro meses.","quatro anos.","cinco anos.","seis anos.","um terço de quatro anos."],"Quatro anos mais um terço: cinco anos e quatro meses.","cp10a")
q(2,"No texto da carteira, o prazo para entregar a carteira à autoridade ou ao dono era de",["quinze dias.","cinco dias.","trinta dias.","dez dias.","sessenta dias."],"Art. 169, parágrafo único, II.","cp10b")
q(2,"A pena mínima da apropriação indébita previdenciária é de",["dois anos de reclusão.","um ano de reclusão.","um mês de detenção.","seis meses de detenção.","quatro anos de reclusão."],"Art. 168-A, caput.")
q(2,"A diferença entre as espécies de pena do art. 168 e do art. 169 é que o art. 168 prevê",["reclusão, e o art. 169, detenção ou multa.","detenção, e o art. 169, reclusão.","multa, e o art. 169, reclusão.","reclusão, e o art. 169, reclusão.","detenção, e o art. 169, detenção."],"Arts. 168 e 169.")
q(2,"Quem entrega a coisa achada à autoridade competente dentro do prazo de quinze dias",["não pratica o crime do art. 169, parágrafo único, II.","pratica o crime.","comete furto.","comete roubo.","comete dano."],"Art. 169, parágrafo único, II.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Apropriação indébita: reclusão de um a quatro anos e multa; previdenciária: reclusão de dois a cinco anos e multa; coisa havida por erro: detenção de um mês a um ano ou multa.","Apropriação indébita: detenção; previdenciária: multa.","Apropriação indébita: reclusão de dois a cinco anos; coisa havida por erro: reclusão de um a quatro.","Apropriação previdenciária: detenção de um a quatro anos.","Coisa achada: reclusão de dois a cinco anos."],"Arts. 168, 168-A e 169.")
q(3,"Considere as afirmações. I. A apropriação indébita exige que o agente tenha a posse ou detenção legítima da coisa. II. A pena da apropriação indébita é aumentada de um terço quando recebida em razão de profissão. III. A apropriação indébita previdenciária tem pena de detenção. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A previdenciária tem pena de reclusão (art. 168-A).")
q(3,"Assinale a INCORRETA.",["A coisa achada deve ser entregue ao dono ou à autoridade em trinta dias.","O art. 170 manda aplicar o privilégio do art. 155, § 2º.","O tesouro achado em prédio alheio gera apropriação da quota do proprietário.","A apropriação de coisa havida por erro tem pena de detenção de um mês a um ano, ou multa.","A apropriação indébita tem pena de reclusão de um a quatro anos, e multa."],"O prazo é de quinze dias.")
q(3,"Na apropriação indébita previdenciária, o juiz pode deixar de aplicar a pena se o agente é primário e de bons antecedentes e",["promoveu o pagamento da contribuição, inclusive acessórios, após o início da ação fiscal e antes de oferecida a denúncia.","pagou após a sentença.","pagou após o trânsito em julgado.","não pagou.","nunca pagou."],"Art. 168-A, § 3º, I.")
q(3,"Na apropriação indébita, a posse que se transforma em crime é aquela que o agente tem",["legitimamente, mas passa a exercer como dono.","por subtração.","por violência.","por fraude.","por ameaça."],"Art. 168, caput.")
q(3,"A diferença entre a apropriação indébita e o estelionato é que, na apropriação indébita,",["a coisa foi recebida legitimamente, sem fraude inicial.","há artifício para obter a coisa.","há violência.","há ameaça.","há mentira para obter a coisa."],"Arts. 168 e 171.")
q(3,"A extinção da punibilidade do art. 168-A, § 2º, exige que o agente, antes do início da ação fiscal,",["declare, confesse e efetue o pagamento das contribuições e preste as informações devidas.","apenas declare.","apenas confesse.","apenas pague.","apenas preste informações."],"Art. 168-A, § 2º.")
q(3,"No art. 168-A, o devedor contumaz, declarado em decisão administrativa definitiva e inscrito no Cadin,",["não se beneficia da extinção de punibilidade do § 2º.","se beneficia sempre.","se beneficia só em dobro.","fica isento de pena.","tem a pena reduzida."],"Art. 168-A, § 5º.")
q(3,"O fato de o agente deixar de ser considerado devedor contumaz",["não afasta o § 5º em relação aos atos praticados no período em que era assim considerado.","afasta o § 5º em relação a todos os atos.","extingue a punibilidade.","reduz a pena.","é irrelevante."],"Art. 168-A, § 6º.")
q(3,"No art. 169, caput, a apropriação de coisa vinda ao poder do agente por força da natureza pode ocorrer, por exemplo, quando",["uma enchente leva um bem alheio para o terreno do agente, que o retém.","o agente compra o bem.","o agente ganha o bem.","o agente furta o bem.","o agente aluga o bem."],"Art. 169, caput (exemplo didático).")
q(3,"A pena máxima da apropriação indébita simples é de",["quatro anos.","seis anos.","cinco anos.","um ano.","oito anos."],"Art. 168, caput.")
q(3,"A apropriação indébita praticada por tutor sobre coisa do tutelado tem a pena",["aumentada de um terço.","reduzida.","dobrada.","extinta.","mantida."],"Art. 168, § 1º, II.")
q(3,"O art. 170 aplica o disposto no art. 155, § 2º, aos crimes do capítulo, o que significa que o juiz pode",["substituir a reclusão pela detenção, diminuir a pena de um a dois terços ou aplicar só a multa, se o criminoso é primário e a coisa de pequeno valor.","aumentar a pena.","extinguir a punibilidade.","aplicar pena de reclusão maior.","absolver o réu."],"Art. 170 e art. 155, § 2º.")
q(3,"Quem acha coisa alheia perdida e não a restitui nem entrega à autoridade no prazo de quinze dias comete crime de",["apropriação de coisa achada.","furto.","roubo.","estelionato.","extorsão."],"Art. 169, parágrafo único, II.")
q(3,"No art. 168-A, § 1º, I, a contribuição é “descontada de pagamento efetuado a segurados, a terceiros ou arrecadada do público”. Isso mostra que o crime exige que a contribuição",["tenha sido efetivamente descontada ou arrecadada.","não tenha sido descontada.","seja futura.","seja de terceiros.","seja prescrita."],"Art. 168-A, § 1º, I.")
q(3,"Assinale a alternativa correta sobre a pena do art. 168 com o aumento do § 1º.",["Um terço sobre a pena de reclusão de um a quatro anos, e multa.","Metade sobre a pena de reclusão.","O dobro da pena.","Dois terços.","Reduz a pena."],"Art. 168, § 1º.")
q(3,"Assinale a alternativa que associa corretamente o crime ao artigo.",["Apropriação previdenciária: art. 168-A; coisa havida por erro: art. 169; privilégio no capítulo: art. 170.","Apropriação previdenciária: art. 169; privilégio: art. 168-A.","Coisa achada: art. 168; erro: art. 170.","Privilégio: art. 168; previdenciária: art. 170.","Previdenciária: art. 170; achada: art. 168-A."],"Arts. 168-A, 169 e 170.")
q(3,"No texto dos bens apreendidos, o agente vendeu parte dos bens. A conduta de vender coisa alheia de que se tem a guarda, como se fosse sua, caracteriza",["apropriação indébita.","furto.","roubo.","extorsão.","dano."],"Art. 168, caput.","cp10a")
q(3,"No texto dos bens apreendidos, o fato de o servidor ter a guarda dos bens em razão do cargo",["é causa de aumento de um terço da pena.","é causa de diminuição.","é irrelevante.","exclui o crime.","extingue a punibilidade."],"Art. 168, § 1º, III.","cp10a")
q(3,"No texto da carteira, o fato de o homem saber quem era o dono, pelos documentos,",["reforça a intenção de apropriar-se, pois podia restituir.","exclui o crime.","extingue a punibilidade.","reduz a pena.","torna o fato atípico."],"Art. 169, parágrafo único, II.","cp10b")
assert len(Q)==60,len(Q)
code,svg=mapa("Apropriação indébita",[
 ("ai","Apropriação indébita",["art. 168","reclusão, 1 a 4 anos, e multa","já tem a posse ou detenção"],"seção 1"),
 ("aum","Aumento de 1/3",["depósito necessário","tutor, curador, inventariante","ofício, emprego, profissão"],"seção 1"),
 ("prev","Previdenciária",["168-A: reclusão, 2 a 5 anos","não repassar contribuição","extinção: antes da ação fiscal"],"seção 2"),
 ("erro","Erro e caso fortuito",["art. 169: detenção, 1 mês a 1 ano","ou multa","força da natureza"],"seção 3"),
 ("achada","Coisa achada e tesouro",["15 dias para devolver","entrega à autoridade","tesouro: quota do proprietário"],"seção 3"),
 ("priv","Privilégio",["art. 170","aplica o art. 155, § 2º","primário e pequeno valor"],"seção 3")],
 "Na prova: lembre que o agente já tem a coisa e que a coisa achada tem prazo de quinze dias")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira caixa é o crime-base; a segunda e a terceira, as figuras especiais; a última, o privilégio.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 168 a 170, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-10","Apropriação indébita (CP, arts. 168 a 170)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 168 a 170. Cobertos: 168, 168-A, 169 e 170."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O conceito de depósito necessário é do Código Civil e não foi conferido na fonte.","O exemplo da enchente na questão do art. 169 é didático.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp10a e cp10b fictícios."],
 fontes_conferidas=["CP, arts. 168 a 170: texto da Câmara, copiado por programa."])
gravar("cp-10",aula_html,banco("cp-10",Q),tx)
