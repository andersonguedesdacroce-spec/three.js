import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O estelionato é o crime da fraude: o agente engana a vítima, que entrega o bem por vontade própria, viciada pelo erro. Na prova, os arts. 171 a 179 aparecem pelo conceito de estelionato, pelas modalidades do § 2º (como o cheque sem fundos), pela fraude eletrônica, hoje de pena autônoma, pelo aumento contra idoso ou vulnerável e por outras fraudes, como a duplicata simulada, o abuso de incapazes e o calote de refeição. A aula segue o texto consolidado."
S={}
S[1]="## 1. Estelionato\n\n"+L("art. 171, caput e § 1º","Art. 171. Obter, para si ou para outrem","§ 2º Nas mesmas penas incorre quem:")+"""

O estelionato é obter, para si ou para outrem, vantagem ilícita em prejuízo alheio, induzindo ou mantendo alguém em erro, mediante artifício, ardil ou qualquer outro meio fraudulento. A pena é de reclusão de um a cinco anos e multa. Três elementos formam o crime: a fraude, o erro da vítima e a vantagem ilícita. A diferença para o furto e o roubo é que, no estelionato, a vítima entrega a coisa voluntariamente, enganada. Se o criminoso é primário e o prejuízo é de pequeno valor, aplica-se o privilégio do art. 155, § 2º.

"""+L("art. 171, § 2º","§ 2º Nas mesmas penas incorre quem:","§ 2º-A.")+"""

O § 2º lista as modalidades equiparadas, com a mesma pena: vender coisa alheia como própria; vender coisa própria inalienável, gravada de ônus ou litigiosa, silenciando sobre a circunstância; defraudar penhor; defraudar a substância, qualidade ou quantidade da coisa que deve entregar; destruir ou ocultar coisa própria ou lesar o próprio corpo para receber seguro; emitir cheque sem suficiente provisão de fundos ou frustrar-lhe o pagamento; e ceder conta bancária para que nela transitem recursos de atividade criminosa. A mais cobrada é a emissão de cheque sem fundos.
"""
S[2]="## 2. Fraude eletrônica e aumentos\n\n"+L("art. 171, §§ 2º-A e 2º-B","§ 2º-A. A pena é de reclusão, de 4","§ 3º A pena aumenta-se")+"\n\n"+L("art. 171, §§ 3º e 4º","§ 3º A pena aumenta-se de um terço","§ 5º [revogado]")+"\n\n"+L("art. 171-A","Art. 171-A. Organizar, gerir","Duplicata simulada")+"""

A fraude eletrônica é cometida com informações fornecidas pela vítima ou por terceiro induzido a erro por redes sociais, contatos telefônicos, e-mail fraudulento, duplicação de dispositivo ou aplicação de internet. A pena é de reclusão de quatro a oito anos e multa, aumentada de um terço a dois terços se o crime usa servidor mantido fora do território nacional. O § 3º aumenta a pena de um terço se o crime é em detrimento de entidade de direito público ou de instituto de economia popular, assistência social ou beneficência. O § 4º aumenta a pena de um terço ao dobro se é contra idoso ou vulnerável. E o art. 171-A pune com reclusão de quatro a oito anos e multa a fraude com ativos virtuais, valores mobiliários ou ativos financeiros.
"""
S[3]="## 3. Outras fraudes\n\n"+L("arts. 172 a 174","Art. 172. Emitir fatura","Fraude no comércio")+"\n\n"+L("art. 175","Art. 175. Enganar, no exercício","Outras fraudes")+"\n\n"+L("art. 176","Art. 176. Tomar refeição","Fraudes e abusos na fundação")+"""

A duplicata simulada é emitir fatura, duplicata ou nota de venda que não corresponda à mercadoria vendida ou ao serviço prestado: detenção de dois a quatro anos e multa. O abuso de incapazes é abusar, em proveito próprio ou alheio, de necessidade, paixão ou inexperiência de menor, ou da alienação ou debilidade mental, induzindo-os à prática de ato com efeito jurídico em prejuízo próprio ou de terceiro: reclusão de dois a seis anos e multa. O induzimento à especulação (jogo, aposta ou especulação ruinosa) tem reclusão de um a três anos e multa.

A fraude no comércio é enganar o adquirente ou consumidor, no exercício de atividade comercial, vendendo mercadoria falsificada ou deteriorada como verdadeira ou perfeita, ou entregando uma mercadoria por outra: detenção de seis meses a dois anos, ou multa. Trabalhos com metal e pedras preciosas têm reclusão de um a cinco anos e multa.

O art. 176 é o calote de refeição: tomar refeição em restaurante, alojar-se em hotel ou utilizar-se de meio de transporte sem dispor de recursos para pagar. A pena é de detenção de quinze dias a dois meses, ou multa. Só se procede mediante representação, e o juiz pode deixar de aplicar a pena conforme as circunstâncias.

"""+L("art. 179","Art. 179. Fraudar execução","CAPÍTULO VII")+"""

Os arts. 177 e 178 tratam de fraudes e abusos em sociedades por ações e na emissão irregular de warrant, com reclusão de um a quatro anos e multa. O art. 179 é a fraude à execução, de alienar, desviar, destruir ou danificar bens ou simular dívidas, com detenção de seis meses a dois anos, ou multa, e ação por queixa.
"""
S[5]="""## 5. Na rotina do guarda

- **Golpes a idosos:** o golpe do falso parente, do falso funcionário e dos falsos prêmios é estelionato com aumento de um terço ao dobro (art. 171, § 4º).
- **Fraude eletrônica:** o golpe por redes sociais e mensagens tem pena autônoma de quatro a oito anos; o registro da ocorrência deve preservar capturas de tela.
- **Cheque sem fundos:** emitir cheque sem provisão de fundos é estelionato, não mera dívida civil.
- **Calote de refeição:** a pessoa que come sem dinheiro responde por fraude, mas a ação depende de representação.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do estelionato | Reclusão de um a cinco anos, e multa |
| Pena da fraude eletrônica | Reclusão de quatro a oito anos, e multa |
| Aumento contra idoso | De um terço ao dobro |
| Cheque sem fundos | Modalidade do § 2º, VI, do art. 171 |
| Calote de refeição | Detenção de quinze dias a dois meses, ou multa; representação |
| Duplicata simulada | Detenção de dois a quatro anos, e multa |
| Fraude no comércio | Detenção de seis meses a dois anos, ou multa |
| Privilégio do estelionato | Primário e pequeno valor: art. 155, § 2º |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Estelionato | Reclusão, 1 a 5 anos, e multa; fraude, erro, vantagem |
| Fraude eletrônica | Reclusão, 4 a 8 anos, e multa |
| Aumento contra idoso ou vulnerável | De 1/3 ao dobro |
| Duplicata simulada | Detenção, 2 a 4 anos, e multa |
| Abuso de incapazes | Reclusão, 2 a 6 anos, e multa |
| Fraude no comércio | Detenção, 6 meses a 2 anos, ou multa |
| Calote de refeição | Detenção, 15 dias a 2 meses, ou multa; representação |
| Fraude à execução | Detenção, 6 meses a 2 anos, ou multa; queixa |
"""
QR=[("Questão 1","A pena do estelionato (art. 171, caput) é de",["reclusão, de um a cinco anos, e multa.","reclusão, de quatro a oito anos, e multa.","detenção, de um a cinco anos.","reclusão, de dois a seis anos.","detenção, de seis meses a dois anos."],0,"Art. 171, caput."),
("Questão 2","A emissão de cheque sem suficiente provisão de fundos, ou a frustração de seu pagamento, é",["modalidade de estelionato.","crime contra a honra.","furto.","apropriação indébita.","contravenção penal."],2,"Art. 171, § 2º, VI."),
("Questão 3","A fraude eletrônica (art. 171, § 2º-A) tem pena de",["reclusão, de quatro a oito anos, e multa.","reclusão, de um a cinco anos, e multa.","detenção, de quatro a oito anos.","reclusão, de dois a seis anos.","multa."],1,"Art. 171, § 2º-A."),
("Questão 4","A pena do estelionato é aumentada de um terço ao dobro se o crime é cometido contra",["idoso ou vulnerável.","qualquer pessoa.","empresa privada.","servidor público.","estudante."],4,"Art. 171, § 4º.")]
t1="<strong>Golpe do falso parente</strong><br><br>Um homem ligou para uma idosa de Vila Nova, cidade fictícia, dizendo ser seu neto, em apuros financeiros, e conseguiu que ela transferisse dinheiro por aplicativo bancário. A idosa foi enganada e o prejuízo foi grande."
t2="<strong>Refeição sem pagamento</strong><br><br>Um cliente almoçou em um restaurante e, na hora de pagar, disse que não tinha dinheiro nem cartão. O dono chamou a Guarda Municipal. O cliente alegou que havia perdido a carteira."
tx={"cp11a":t1,"cp11b":t2}
# n=1
q(1,"A pena do estelionato é de",["reclusão, de um a cinco anos, e multa.","reclusão, de quatro a oito anos, e multa.","detenção, de um a cinco anos.","reclusão, de dois a seis anos.","detenção, de seis meses a dois anos."],"Art. 171, caput.")
q(1,"O estelionato consiste em obter vantagem ilícita, em prejuízo alheio, induzindo ou mantendo alguém em erro, mediante",["artifício, ardil ou qualquer outro meio fraudulento.","violência.","ameaça.","subtração.","omissão."],"Art. 171, caput.")
q(1,"No estelionato, se o criminoso é primário e de pequeno valor o prejuízo, o juiz pode aplicar a pena conforme o art.",["155, § 2º.","157.","158.","163.","168."],"Art. 171, § 1º.")
q(1,"Incorre nas mesmas penas do estelionato quem vende, permuta, dá em pagamento, em locação ou em garantia",["coisa alheia como própria.","coisa própria como própria.","coisa própria com ônus declarado.","coisa abandonada.","coisa achada."],"Art. 171, § 2º, I.")
q(1,"Incorre nas mesmas penas do estelionato quem emite cheque",["sem suficiente provisão de fundos em poder do sacado, ou lhe frustra o pagamento.","com fundos suficientes.","pré-datado com fundos.","em favor de si mesmo.","a favor de parente."],"Art. 171, § 2º, VI.")
q(1,"Incorre nas mesmas penas do estelionato quem cede, gratuita ou onerosamente, conta bancária para que nela transitem recursos",["destinados ao financiamento de atividade criminosa ou que dela sejam fruto.","de salário.","de aposentadoria.","de pensão.","de aluguel."],"Art. 171, § 2º, VII.")
q(1,"A fraude eletrônica tem pena de",["reclusão, de quatro a oito anos, e multa.","reclusão, de um a cinco anos.","detenção, de quatro a oito anos.","reclusão, de dois a seis anos.","multa."],"Art. 171, § 2º-A.")
q(1,"A pena da fraude eletrônica é aumentada de um terço a dois terços se o crime é praticado mediante utilização de",["servidor mantido fora do território nacional.","celular.","computador pessoal.","rede local.","servidor municipal."],"Art. 171, § 2º-B.")
q(1,"A pena do estelionato aumenta-se de um terço se o crime é cometido em detrimento de",["entidade de direito público ou de instituto de economia popular, assistência social ou beneficência.","pessoa física.","empresa privada.","condomínio.","associação esportiva."],"Art. 171, § 3º.")
q(1,"A pena do estelionato aumenta-se de um terço ao dobro se o crime é cometido contra",["idoso ou vulnerável.","qualquer pessoa.","empresário.","servidor.","estudante."],"Art. 171, § 4º.")
q(1,"A pena da fraude com a utilização de ativos virtuais, valores mobiliários ou ativos financeiros (art. 171-A) é de",["reclusão, de quatro a oito anos, e multa.","reclusão, de um a cinco anos.","detenção, de dois a quatro anos.","reclusão, de dois a seis anos.","multa."],"Art. 171-A.")
q(1,"A duplicata simulada (art. 172) tem pena de",["detenção, de dois a quatro anos, e multa.","reclusão, de um a cinco anos.","reclusão, de quatro a oito anos.","detenção, de seis meses a dois anos.","multa."],"Art. 172.")
q(1,"O abuso de incapazes (art. 173) tem pena de",["reclusão, de dois a seis anos, e multa.","reclusão, de um a cinco anos.","detenção, de dois a quatro anos.","detenção, de seis meses a dois anos.","multa."],"Art. 173.")
q(1,"A fraude no comércio (art. 175, caput) tem pena de",["detenção, de seis meses a dois anos, ou multa.","reclusão, de um a cinco anos.","reclusão, de dois a seis anos.","detenção, de dois a quatro anos.","multa."],"Art. 175.")
q(1,"Tomar refeição em restaurante sem dispor de recursos para pagar (art. 176) tem pena de",["detenção, de quinze dias a dois meses, ou multa.","reclusão, de um a cinco anos.","detenção, de seis meses a dois anos.","detenção, de dois a quatro anos.","multa, apenas."],"Art. 176.")
q(1,"No art. 176 (outras fraudes), a ação penal é",["pública condicionada à representação.","de queixa.","pública incondicionada.","por requisição do Ministro.","por requisição do juiz."],"Art. 176, parágrafo único.")
q(1,"A fraude à execução (art. 179) tem pena de",["detenção, de seis meses a dois anos, ou multa.","reclusão, de um a cinco anos.","reclusão, de quatro a oito anos.","detenção, de dois a quatro anos.","multa, apenas."],"Art. 179.")
q(1,"No texto do falso parente, a conduta é, em tese,",["estelionato, com aumento por ser a vítima idosa.","furto.","roubo.","extorsão.","apropriação indébita."],"Art. 171, § 4º.","cp11a")
q(1,"No texto da refeição sem pagamento, a conduta é, em tese,",["fraude do art. 176, que depende de representação.","furto.","roubo.","extorsão.","dano."],"Art. 176.","cp11b")
q(1,"O estelionato exige, além da vantagem ilícita, que a vítima seja induzida ou mantida em",["erro.","medo.","violência.","coação.","omissão."],"Art. 171, caput.")
# n=2
q(2,"O estelionato difere do furto porque, no estelionato,",["a vítima entrega a coisa voluntariamente, induzida em erro.","há violência.","há ameaça.","o agente subtrai.","a coisa é imóvel."],"Art. 171, caput.")
q(2,"Incorre nas mesmas penas do estelionato quem defrauda, mediante alienação não consentida pelo credor, a garantia",["pignoratícia, quando tem a posse do objeto empenhado.","hipotecária, quando não tem a posse.","pessoal.","fiduciária.","bancária."],"Art. 171, § 2º, III.")
q(2,"Incorre nas mesmas penas do estelionato quem defrauda substância, qualidade ou quantidade de",["coisa que deve entregar a alguém.","coisa que já entregou.","coisa que recebeu.","coisa própria.","coisa achada."],"Art. 171, § 2º, IV.")
q(2,"Incorre nas mesmas penas do estelionato quem destrói, oculta coisa própria ou lesa o próprio corpo, com o intuito de",["haver indenização ou valor de seguro.","vingar-se.","livrar-se de dívidas.","esconder-se.","economizar."],"Art. 171, § 2º, V.")
q(2,"Incorre nas mesmas penas do estelionato quem vende coisa própria inalienável, gravada de ônus ou litigiosa, silenciando sobre",["qualquer dessas circunstâncias.","o preço.","a forma de pagamento.","a data.","o nome do comprador."],"Art. 171, § 2º, II.")
q(2,"A fraude eletrônica se caracteriza por fraude cometida com informações fornecidas pela vítima ou por terceiro induzido a erro por meio de",["redes sociais, contatos telefônicos, e-mail fraudulento, duplicação de dispositivo eletrônico ou aplicação de internet.","apenas cartas.","apenas telegramas.","apenas telefone fixo.","apenas fax."],"Art. 171, § 2º-A.")
q(2,"A pena do § 3º do art. 171 aumenta-se de um terço se o crime é em detrimento de",["instituto de economia popular, assistência social ou beneficência.","empresa privada.","pessoa idosa.","menor.","vizinho."],"Art. 171, § 3º.")
q(2,"A duplicata simulada se caracteriza por emitir fatura, duplicata ou nota de venda que não corresponda",["à mercadoria vendida, em quantidade ou qualidade, ou ao serviço prestado.","ao preço.","ao prazo.","ao endereço.","à cor."],"Art. 172.")
q(2,"Nas mesmas penas da duplicata simulada incorre quem",["falsificar ou adulterar a escrituração do Livro de Registro de Duplicatas.","guardar duplicatas.","pagar duplicatas.","protestar duplicatas.","vender duplicatas."],"Art. 172, parágrafo único.")
q(2,"O abuso de incapazes exige que o agente induza a vítima à prática de ato",["suscetível de produzir efeito jurídico, em prejuízo próprio ou de terceiro.","sem efeito.","irrelevante.","gratuito.","de caridade."],"Art. 173.")
q(2,"O induzimento a especulação (art. 174) é abusar da inexperiência ou simplicidade ou inferioridade mental de outrem, induzindo-o a",["jogo ou aposta, ou à especulação com títulos ou mercadorias, sabendo ou devendo saber que a operação é ruinosa.","poupar.","investir em imóveis.","contrair empréstimo.","pagar dívida."],"Art. 174.")
q(2,"Na fraude no comércio, o agente engana o adquirente ou consumidor, vendendo como verdadeira ou perfeita mercadoria",["falsificada ou deteriorada, ou entregando uma mercadoria por outra.","nova.","de qualidade.","em promoção.","importada."],"Art. 175.")
q(2,"No art. 176, o juiz pode, conforme as circunstâncias,",["deixar de aplicar a pena.","aplicar reclusão.","aumentar a pena.","dobrar a pena.","converter em estelionato."],"Art. 176, parágrafo único.")
q(2,"Alienar, desviar, destruir ou danificar bens, ou simular dívidas, para fraudar execução é crime de ação",["de queixa.","pública incondicionada.","por representação.","por requisição do Ministro.","por requisição do juiz."],"Art. 179, parágrafo único.")
q(2,"A emissão irregular de conhecimento de depósito ou warrant tem pena de",["reclusão, de um a quatro anos, e multa.","detenção, de seis meses a dois anos.","reclusão, de dois a seis anos.","multa.","detenção, de dois a quatro anos."],"Art. 178.")
q(2,"As fraudes e abusos na fundação ou administração de sociedade por ações (art. 177) têm pena de reclusão de um a quatro anos e multa",["se o fato não constitui crime contra a economia popular.","em qualquer caso.","apenas se houver prejuízo.","apenas se houver lucro.","apenas se houver violência."],"Art. 177.")
q(2,"No texto do falso parente, a pena-base da fraude, se cometida por meio de aplicativo e com informações da vítima, pode ser a do",["art. 171, § 2º-A.","art. 155.","art. 157.","art. 158.","art. 168."],"Art. 171, § 2º-A.","cp11a")
q(2,"No texto do falso parente, por ser a vítima idosa, a pena é aumentada de",["um terço ao dobro, considerada a relevância do resultado gravoso.","um sexto.","metade.","dois terços.","apenas multa."],"Art. 171, § 4º.","cp11a")
q(2,"No texto da refeição sem pagamento, o juiz pode, nas circunstâncias, nos termos do art. 176,",["deixar de aplicar a pena.","aplicar reclusão.","aumentar a pena.","dobrar a pena.","converter em furto."],"Art. 176, parágrafo único.","cp11b")
q(2,"No estelionato, a vantagem ilícita é obtida em prejuízo",["alheio.","próprio.","do agente.","de ninguém.","do Estado, apenas."],"Art. 171, caput.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Estelionato: reclusão de um a cinco anos e multa; fraude eletrônica: reclusão de quatro a oito anos e multa; duplicata simulada: detenção de dois a quatro anos e multa.","Estelionato: detenção; fraude eletrônica: multa.","Estelionato: reclusão de dois a seis anos; fraude eletrônica: detenção.","Duplicata simulada: reclusão de um a cinco anos.","Fraude eletrônica: reclusão de um a quatro anos."],"Arts. 171, § 2º-A, e 172.")
q(3,"Considere as afirmações. I. O estelionato tem pena de reclusão de um a cinco anos e multa. II. O estelionato contra idoso tem aumento de um terço ao dobro. III. O calote de refeição é de ação pública incondicionada. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"O art. 176 exige representação.")
q(3,"Assinale a INCORRETA.",["A emissão de cheque sem fundos não é modalidade de estelionato.","A fraude eletrônica tem pena de reclusão de quatro a oito anos e multa.","O estelionato contra idoso tem aumento de um terço ao dobro.","A fraude no comércio tem pena de detenção de seis meses a dois anos, ou multa.","A duplicata simulada tem pena de detenção de dois a quatro anos, e multa."],"Art. 171, § 2º, VI: é modalidade de estelionato.")
q(3,"A diferença entre estelionato e apropriação indébita é que, no estelionato,",["há fraude para obter a coisa.","a coisa chega por confiança.","há violência.","há ameaça.","há subtração."],"Arts. 168 e 171.")
q(3,"No estelionato, o “erro” é elemento porque a vítima",["entrega a vantagem enganada pela fraude.","é ameaçada.","é agredida.","é surpreendida.","é coagida."],"Art. 171, caput.")
q(3,"O art. 171, § 5º, que previa ação penal condicionada à representação, aparece no texto consolidado como",["revogado.","vigente.","vetado.","suspenso.","inconstitucional."],"Art. 171, § 5º: [revogado].")
q(3,"No § 2º, II, do art. 171, o agente vende coisa própria que é",["inalienável, gravada de ônus ou litigiosa, silenciando sobre isso.","livre e desembaraçada.","sem ônus.","alugada.","emprestada."],"Art. 171, § 2º, II.")
q(3,"O art. 171, § 2º, VI, pune quem emite cheque sem fundos ou lhe frustra o pagamento. Frustrar o pagamento é, por exemplo,",["sustar o cheque indevidamente, com fraude.","pagar o cheque.","depositar o cheque.","descontar o cheque.","guardar o cheque."],"Art. 171, § 2º, VI.")
q(3,"O aumento do § 4º do art. 171 considera a relevância do",["resultado gravoso.","valor do bem.","local do crime.","horário do crime.","número de agentes."],"Art. 171, § 4º.")
q(3,"A fraude eletrônica do § 2º-A pode ser cometida por",["redes sociais, telefone, e-mail ou duplicação de dispositivo, ou outro meio fraudulento análogo.","apenas presencialmente.","apenas por carta.","apenas por violência.","apenas por ameaça."],"Art. 171, § 2º-A.")
q(3,"Na fraude no comércio, o § 1º do art. 175, que trata de metais e pedras preciosas, tem pena de",["reclusão, de um a cinco anos, e multa.","detenção, de seis meses a dois anos.","reclusão, de dois a seis anos.","multa.","detenção, de dois a quatro anos."],"Art. 175, § 1º.")
q(3,"O abuso de incapazes protege, entre outros,",["o menor e quem tem alienação ou debilidade mental.","qualquer adulto.","qualquer empresário.","o idoso, apenas.","o servidor."],"Art. 173.")
q(3,"A pena de detenção de quinze dias a dois meses, ou multa, é prevista para",["tomar refeição em restaurante, alojar-se em hotel ou utilizar-se de meio de transporte sem dispor de recursos para pagar.","o estelionato.","a duplicata simulada.","a fraude eletrônica.","a fraude à execução."],"Art. 176.")
q(3,"A fraude à execução (art. 179) pode ocorrer mediante",["alienação, desvio, destruição ou dano de bens, ou simulação de dívidas.","apenas venda.","apenas doação.","apenas hipoteca.","apenas penhor."],"Art. 179.")
q(3,"Nas hipóteses do art. 171, § 1º, o juiz aplica a pena conforme o art. 155, § 2º, se o criminoso é primário e",["o prejuízo é de pequeno valor.","o prejuízo é alto.","a vítima é idosa.","há fraude eletrônica.","há concurso de agentes."],"Art. 171, § 1º.")
q(3,"A emissão de cheque sem fundos, no § 2º, VI, do art. 171, tem a pena",["do estelionato, reclusão de um a cinco anos e multa.","de detenção de um a seis meses.","de multa.","do furto.","do dano."],"Art. 171, § 2º, caput e VI.")
q(3,"A fraude eletrônica do § 2º-A tem pena maior que a do estelionato simples porque o legislador considerou",["a maior gravidade das fraudes por meios eletrônicos e redes sociais.","a menor lesividade.","a ausência de dolo.","a existência de violência.","a presença de arma."],"Art. 171, § 2º-A (reclusão de quatro a oito anos).")
q(3,"No art. 172, o parágrafo único pune quem falsificar ou adulterar a escrituração do",["Livro de Registro de Duplicatas.","Livro-caixa.","Livro de ponto.","Livro de atas.","Livro de matrícula."],"Art. 172, parágrafo único.")
q(3,"No texto do falso parente, o fato de a transferência ser feita por aplicativo bancário, por indução de uma voz ao telefone, aponta para a hipótese do",["§ 2º-A do art. 171.","art. 155, § 6º.","art. 157.","art. 158.","art. 163."],"Art. 171, § 2º-A: informações fornecidas pela vítima induzida por contatos telefônicos.","cp11a")
q(3,"No texto da refeição, se o cliente tinha recursos e mesmo assim se recusou a pagar, o fato",["pode configurar estelionato, e não o art. 176, que exige não dispor de recursos.","configura sempre o art. 176.","não é crime.","configura roubo.","configura furto."],"Art. 176: “sem dispor de recursos”.","cp11b")
assert len(Q)==60,len(Q)
code,svg=mapa("Estelionato e outras fraudes",[
 ("est","Estelionato",["art. 171: reclusão, 1 a 5 anos","fraude, erro, vantagem","privilégio: art. 155, § 2º"],"seção 1"),
 ("mod","Modalidades do § 2º",["coisa alheia como própria","cheque sem fundos","conta laranja"],"seção 1"),
 ("eletr","Fraude eletrônica",["reclusão, 4 a 8 anos","servidor no exterior: aumento","171-A: ativos virtuais"],"seção 2"),
 ("aum","Aumentos",["§ 3º: entidade pública (+1/3)","§ 4º: idoso (1/3 ao dobro)","relevância do resultado"],"seção 2"),
 ("fraudes","Outras fraudes",["duplicata simulada: 2 a 4 anos","abuso de incapazes: 2 a 6","comércio: 6 meses a 2 anos"],"seção 3"),
 ("calote","Calote e fraude à execução",["176: 15 dias a 2 meses","representação","179: queixa"],"seção 3")],
 "Na prova: lembre que o estelionato tem fraude, erro e vantagem, e que a vítima entrega por vontade própria")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As duas primeiras caixas tratam do estelionato e de seus aumentos; as demais, de fraudes específicas.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 171 a 179, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-11","Estelionato e outras fraudes (CP, arts. 171 a 179)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 171 a 179. Cobertos: 171 (caput e §§ 1º a 4º), 171-A, 172, 173, 174, 175, 176, 177 (resumido), 178 e 179."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O art. 171, § 5º, aparece revogado na consolidação; a regra de ação penal do estelionato não foi conferida em outra fonte e a aula não a aborda.","O art. 177 foi resumido; os incisos do § 1º não foram detalhados.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp11a e cp11b fictícios."],
 fontes_conferidas=["CP, arts. 171 a 179: texto da Câmara, copiado por programa."])
gravar("cp-11",aula_html,banco("cp-11",Q),tx)
