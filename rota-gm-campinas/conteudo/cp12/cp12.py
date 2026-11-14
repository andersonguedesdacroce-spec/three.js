import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A receptação é o crime de quem lucra com o crime alheio, adquirindo ou ocultando coisa produto de crime. Na prova, os arts. 180 a 183-A aparecem pelas quatro figuras da receptação (própria, qualificada, culposa e de animal), pelos aumentos (bem público, fios e cabos, organização criminosa) e pelas disposições gerais do título dos crimes contra o patrimônio, sobre quando o crime entre parentes é isento de pena ou depende de representação. A aula segue o texto consolidado, e o ponto de maior cobrança é a diferença entre o dolo (sabe) e o dolo eventual ou culpa (deve saber, deve presumir)."
S={}
S[1]="## 1. Receptação\n\n"+L("art. 180, caput","Art. 180. Adquirir, receber, transportar","Receptação qualificada")+"""

A receptação própria é adquirir, receber, transportar, conduzir ou ocultar, em proveito próprio ou alheio, coisa que sabe ser produto de crime, ou influir para que terceiro de boa-fé a adquira, receba ou oculte. A pena é de reclusão de dois a seis anos e multa. O elemento subjetivo é saber: o agente conhece a origem criminosa. É um crime acessório, porque depende de um crime anterior, mas é autônomo: o receptador responde ainda que o autor do crime anterior seja desconhecido ou isento de pena (§ 4º).

"""+L("art. 180, §§ 1º e 2º","§ 1º Adquirir, receber, transportar, conduzir, ocultar, ter em depósito","§ 3º Adquirir ou receber coisa")+"""

A receptação qualificada (§ 1º) é praticada no exercício de atividade comercial ou industrial, com coisa que o agente deve saber ser produto de crime. A pena é de reclusão de três a oito anos e multa, mais alta que a da receptação simples, porque o comerciante tem maior dever de cuidado. O § 2º equipara à atividade comercial qualquer forma de comércio irregular ou clandestino, inclusive o exercido em residência. Repare que, na qualificada, a lei diz “deve saber”, mais amplo que o “sabe” do caput.
"""
S[2]="## 2. Receptação culposa, aumentos e receptação de animal\n\n"+L("art. 180, §§ 3º e 4º","§ 3º Adquirir ou receber coisa","§ 5º [revogado]")+"\n\n"+L("art. 180, §§ 6º a 8º","§ 6º Tratando-se de bens","Receptação de animal")+"\n\n"+L("art. 180-A","Art. 180-A. Adquirir, receber","CAPÍTULO VIII")+"""

A receptação culposa (§ 3º) é adquirir ou receber coisa que, por sua natureza, pela desproporção entre o valor e o preço, ou pela condição de quem a oferece, deve presumir-se obtida por meio criminoso. A pena é de detenção de um mês a um ano, ou multa, ou ambas as penas. É o caso do celular vendido a metade do preço por um desconhecido na rua. Os sinais de alerta são a natureza da coisa, o preço muito abaixo do mercado e o vendedor suspeito.

Os aumentos: se a coisa é patrimônio da União, de Estado, do DF, de Município, de autarquia, fundação pública, empresa pública, sociedade de economia mista ou empresa concessionária de serviços públicos, a pena do caput é aplicada em dobro (§ 6º); se a receptação é de fios, cabos ou equipamentos de energia, telefonia ou transferência de dados, ou de cargas transportadas em modais ferroviários ou metroviários, a pena do caput ou do § 1º é aplicada em dobro (§ 7º); se é cometida por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, a pena aumenta em dois terços (§ 8º).

A receptação de animal (art. 180-A) é adquirir, receber, transportar, conduzir, ocultar, ter em depósito ou vender, com a finalidade de produção ou comercialização, semovente domesticável de produção ou animal doméstico que sabe ou deve saber ser produto de crime. A pena é de reclusão de três a oito anos e multa.
"""
S[3]="## 3. Disposições gerais sobre o crime entre parentes\n\n"+L("art. 181","Art. 181. É isento de pena","Art. 182.")+"\n\n"+L("art. 182","Art. 182. Somente se procede","Art. 183.")+"\n\n"+L("art. 183","Art. 183. Não se aplica","Art. 183-A.")+"""

Nos crimes contra o patrimônio, a lei trata com leniência o crime cometido em família. É isento de pena (imunidade absoluta) quem comete o crime em prejuízo do cônjuge, na constância da sociedade conjugal, ou de ascendente ou descendente, seja o parentesco legítimo ou ilegítimo, civil ou natural. Somente se procede mediante representação (imunidade relativa) se o crime é cometido em prejuízo do cônjuge desquitado ou judicialmente separado, de irmão, ou de tio ou sobrinho com quem o agente coabita.

Mas as exceções são o que a prova cobra. Não se aplicam os dois artigos anteriores se o crime é de roubo ou de extorsão, ou se há emprego de grave ameaça ou violência a pessoa, ao estranho que participa do crime, e se o crime é praticado contra pessoa com 60 anos ou mais.

"""+L("art. 183-A","Art. 183-A. Nos crimes de que trata este Título","TÍTULO III")+"""

O art. 183-A, mais recente, aumenta de um terço até o dobro as penas dos crimes contra o patrimônio cometidos contra instituições financeiras e prestadores de serviço de segurança privada.
"""
S[5]="""## 5. Na rotina do guarda

- **Compra de produto suspeito:** quem compra celular ou bicicleta muito abaixo do preço de mercado, de um desconhecido, corre o risco de responder por receptação culposa.
- **Desmanche e comércio clandestino:** o ferro-velho e o comércio informal com peças de origem suspeita são receptação qualificada, de pena de três a oito anos.
- **Cargas e fios:** a receptação de fios e cabos tem a pena em dobro, e o guarda frequentemente flagra os receptadores em pontos de revenda de sucata.
- **Veículo furtado:** conduzir veículo sabendo que é produto de crime é receptação; o guarda verifica a procedência na abordagem.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena da receptação própria | Reclusão de dois a seis anos, e multa |
| Pena da receptação qualificada | Reclusão de três a oito anos, e multa |
| Pena da receptação culposa | Detenção de um mês a um ano, ou multa, ou ambas |
| Receptação de animal | Reclusão de três a oito anos, e multa |
| Bem público | Pena do caput em dobro (§ 6º) |
| Fios e cabos | Pena do caput ou do § 1º em dobro (§ 7º) |
| Autor do crime anterior desconhecido | A receptação continua punível (§ 4º) |
| Imunidade entre parentes | Não vale em roubo, extorsão, violência, para estranhos e contra pessoa com 60 anos ou mais |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Receptação própria | Reclusão, 2 a 6 anos, e multa; “sabe” |
| Receptação qualificada | Reclusão, 3 a 8 anos, e multa; atividade comercial; “deve saber” |
| Receptação culposa | Detenção, 1 mês a 1 ano, ou multa; “deve presumir” |
| Receptação de animal | Reclusão, 3 a 8 anos, e multa |
| Aumentos | Bem público: dobro; fios e cabos: dobro; organização criminosa: 2/3 |
| Isenção de pena | Cônjuge na constância; ascendente ou descendente |
| Representação | Cônjuge separado; irmão; tio ou sobrinho que coabita |
| Exceções | Roubo, extorsão, violência; estranho; vítima com 60 anos ou mais |
"""
QR=[("Questão 1","A pena da receptação própria (art. 180, caput) é de",["reclusão, de dois a seis anos, e multa.","reclusão, de três a oito anos, e multa.","detenção, de um mês a um ano.","reclusão, de um a quatro anos.","detenção, de dois a seis anos."],0,"Art. 180, caput."),
("Questão 2","A receptação culposa é a de coisa que, pela desproporção entre o valor e o preço, ou pela condição de quem a oferece, deve",["presumir-se obtida por meio criminoso.","ser vendida.","ser guardada.","ser consumida.","ser devolvida."],2,"Art. 180, § 3º."),
("Questão 3","Em prejuízo de ascendente ou descendente, quem comete crime contra o patrimônio",["é isento de pena, salvo as exceções do art. 183.","responde com pena em dobro.","responde por representação.","responde por queixa.","sempre responde."],1,"Art. 181, II."),
("Questão 4","A imunidade dos arts. 181 e 182 não se aplica ao crime de",["roubo ou extorsão, ou em que haja grave ameaça ou violência a pessoa.","furto.","dano.","apropriação indébita.","estelionato."],4,"Art. 183, I.")]
t1="<strong>Celular vendido na rua</strong><br><br>Um homem comprou, de um desconhecido, na calçada, um celular de último modelo por um terço do preço da loja, sem nota fiscal. Dias depois, descobriu-se que o aparelho era produto de roubo."
t2="<strong>Ferro-velho com fios de cobre</strong><br><br>O dono de um ferro-velho de Vila Nova, cidade fictícia, que exerce a atividade comercial de compra e venda de sucata, comprou fios de cobre de energia elétrica de pessoas desconhecidas, sem exigir documento. A Guarda Municipal, em fiscalização, encontrou vários rolos de fio de uma concessionária."
tx={"cp12a":t1,"cp12b":t2}
# n=1
q(1,"A pena da receptação própria é de",["reclusão, de dois a seis anos, e multa.","reclusão, de três a oito anos, e multa.","detenção, de um mês a um ano.","reclusão, de um a quatro anos.","detenção, de dois a seis anos."],"Art. 180, caput.")
q(1,"Na receptação própria, o agente adquire, recebe, transporta, conduz ou oculta coisa que",["sabe ser produto de crime.","deve presumir ser legítima.","achou.","recebeu de herança.","comprou em loja."],"Art. 180, caput.")
q(1,"A pena da receptação qualificada (§ 1º) é de",["reclusão, de três a oito anos, e multa.","reclusão, de dois a seis anos, e multa.","detenção, de um mês a um ano.","reclusão, de um a quatro anos.","detenção, de três a oito anos."],"Art. 180, § 1º.")
q(1,"A receptação qualificada é praticada no exercício de atividade",["comercial ou industrial.","doméstica.","agrícola.","escolar.","religiosa."],"Art. 180, § 1º.")
q(1,"Equipara-se à atividade comercial, para a receptação qualificada, qualquer forma de comércio",["irregular ou clandestino, inclusive o exercido em residência.","regular.","licenciado.","formal.","público."],"Art. 180, § 2º.")
q(1,"A receptação culposa tem pena de",["detenção, de um mês a um ano, ou multa, ou ambas as penas.","reclusão, de dois a seis anos.","reclusão, de três a oito anos.","detenção, de dois a seis anos.","multa, apenas."],"Art. 180, § 3º.")
q(1,"A receptação é punível, ainda que",["desconhecido ou isento de pena o autor do crime de que proveio a coisa.","o autor seja condenado.","o autor seja conhecido, apenas.","a coisa seja devolvida.","o crime anterior não exista."],"Art. 180, § 4º.")
q(1,"Tratando-se de bens do patrimônio de Município, a pena da receptação do caput",["é aplicada em dobro.","é aumentada de um terço.","é reduzida.","é mantida.","é aumentada de metade."],"Art. 180, § 6º.")
q(1,"Se a receptação é de fios, cabos ou equipamentos de energia elétrica ou telefonia, a pena do caput ou do § 1º",["é aplicada em dobro.","é aumentada de um terço.","é reduzida.","é mantida.","é aumentada de metade."],"Art. 180, § 7º.")
q(1,"Se a receptação é cometida por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, a pena aumenta em",["dois terços.","um terço.","metade.","dobro.","um sexto."],"Art. 180, § 8º.")
q(1,"A pena da receptação de animal (art. 180-A) é de",["reclusão, de três a oito anos, e multa.","reclusão, de dois a seis anos, e multa.","detenção, de um mês a um ano.","reclusão, de um a quatro anos.","multa."],"Art. 180-A.")
q(1,"É isento de pena quem comete crime contra o patrimônio em prejuízo do",["cônjuge, na constância da sociedade conjugal.","vizinho.","amigo.","empregador.","sócio."],"Art. 181, I.")
q(1,"É isento de pena quem comete crime contra o patrimônio em prejuízo de",["ascendente ou descendente.","tio.","sobrinho.","irmão.","primo."],"Art. 181, II.")
q(1,"Somente se procede mediante representação, nos crimes patrimoniais, se o crime é cometido em prejuízo do",["cônjuge desquitado ou judicialmente separado.","cônjuge na constância do casamento.","pai.","filho.","avô."],"Art. 182, I.")
q(1,"Somente se procede mediante representação, nos crimes patrimoniais, se o crime é cometido em prejuízo de",["irmão, legítimo ou ilegítimo.","pai.","filho.","cônjuge.","avô."],"Art. 182, II.")
q(1,"Não se aplicam os arts. 181 e 182 se o crime é de",["roubo ou de extorsão, ou em geral quando há grave ameaça ou violência a pessoa.","furto.","dano.","estelionato.","apropriação indébita."],"Art. 183, I.")
q(1,"Não se aplicam os arts. 181 e 182",["ao estranho que participa do crime.","ao parente que participa.","a qualquer partícipe.","ao filho.","ao cônjuge."],"Art. 183, II.")
q(1,"No texto do celular vendido na rua, o comprador, ao adquirir o aparelho de um desconhecido, por um terço do preço, sem nota fiscal, pode responder, em tese, por",["receptação culposa.","receptação qualificada.","furto.","roubo.","estelionato."],"Art. 180, § 3º: desproporção entre valor e preço e condição de quem oferece.","cp12a")
q(1,"No texto do ferro-velho, o dono, que exerce atividade comercial e compra fios sem exigir documento, pode responder por",["receptação qualificada.","receptação culposa.","furto.","roubo.","dano."],"Art. 180, § 1º: no exercício de atividade comercial.","cp12b")
q(1,"A receptação, no art. 180, pode ser praticada também por quem",["transporta ou conduz coisa que sabe ser produto de crime.","apenas por quem compra.","apenas por quem vende.","apenas por quem guarda.","apenas por quem doa."],"Art. 180, caput.")
# n=2
q(2,"Na receptação própria, o elemento subjetivo é saber que a coisa é produto de crime. Na receptação qualificada, a lei diz que o agente",["deve saber.","sabe.","pode saber.","desconhece.","ignora."],"Art. 180, § 1º.")
q(2,"A receptação tem como pressuposto a existência de",["um crime anterior de que proveio a coisa.","um acordo prévio com o autor.","uma venda.","um contrato.","um depósito."],"Art. 180, caput.")
q(2,"Na receptação própria, a ação de influir para que terceiro, de boa-fé, adquira, receba ou oculte a coisa também é típica, e a pena é",["a do caput.","a do § 3º.","a do § 1º.","de multa.","a da contravenção."],"Art. 180, caput.")
q(2,"Na receptação qualificada, a conduta inclui, entre outras, ter em depósito, desmontar, montar, remontar, vender, expor à venda ou utilizar a coisa",["em proveito próprio ou alheio, no exercício de atividade comercial ou industrial.","em ambiente doméstico.","por empréstimo.","por doação.","por herança."],"Art. 180, § 1º.")
q(2,"A receptação culposa se caracteriza quando a coisa, por sua natureza, pela desproporção entre o valor e o preço, ou pela condição de quem a oferece, deve presumir-se",["obtida por meio criminoso.","doada.","herdada.","legítima.","paga."],"Art. 180, § 3º.")
q(2,"O art. 180-A trata da receptação de",["semovente domesticável de produção ou animal doméstico.","veículo.","joia.","documento.","fio de cobre."],"Art. 180-A.")
q(2,"Na receptação de animal, a finalidade da conduta é de",["produção ou comercialização.","lazer.","estimação, apenas.","doação.","pesquisa."],"Art. 180-A.")
q(2,"Na receptação, a pena aplicada em dobro aos bens do patrimônio de empresa concessionária de serviços públicos é a",["do caput.","do § 3º.","do art. 180-A.","do art. 155.","do art. 157."],"Art. 180, § 6º.")
q(2,"A receptação de cargas transportadas em modais ferroviários ou metroviários tem a pena do caput ou do § 1º",["aplicada em dobro.","reduzida.","mantida.","aumentada de um terço.","extinta."],"Art. 180, § 7º.")
q(2,"A isenção de pena do art. 181 aplica-se ao crime cometido em prejuízo do cônjuge",["na constância da sociedade conjugal.","separado judicialmente.","divorciado.","ex-companheiro.","sogro."],"Art. 181, I.")
q(2,"O art. 182 exige representação se o crime é cometido em prejuízo de tio ou sobrinho",["com quem o agente coabita.","em qualquer circunstância.","que mora longe.","que é idoso.","que é incapaz."],"Art. 182, III.")
q(2,"A imunidade dos arts. 181 e 182 não se aplica se o crime é praticado contra pessoa com idade",["igual ou superior a 60 anos.","inferior a 18 anos.","igual a 50 anos.","inferior a 60 anos.","igual a 65 anos, apenas."],"Art. 183, III.")
q(2,"O art. 183-A aumenta as penas dos crimes patrimoniais cometidos contra instituições financeiras e prestadores de serviço de segurança privada em",["um terço até o dobro.","metade.","dois terços.","um sexto.","em dobro, apenas."],"Art. 183-A.")
q(2,"A receptação é crime",["acessório, que depende de um crime anterior, mas é autônomo.","principal, que independe de outro crime.","contra a pessoa.","contra a honra.","de menor potencial ofensivo."],"Art. 180, § 4º.")
q(2,"No texto do celular, a venda por um terço do preço da loja, por desconhecido, sem nota fiscal, são sinais da",["desproporção entre valor e preço e da condição de quem oferece.","origem lícita.","boa-fé.","doação.","promoção."],"Art. 180, § 3º.","cp12a")
q(2,"No texto do celular, se o comprador soubesse que o aparelho era roubado, a receptação seria",["própria, com pena de reclusão de dois a seis anos e multa.","culposa.","qualificada.","atípica.","contravenção."],"Art. 180, caput.","cp12a")
q(2,"No texto do ferro-velho, os fios eram de uma concessionária de energia. A pena aplicável é",["a da receptação qualificada, em dobro, pelo § 7º.","a da culposa.","a do caput, sem aumento.","a do furto.","a do dano."],"Art. 180, §§ 1º e 7º.","cp12b")
q(2,"No art. 183, a imunidade deixa de se aplicar ao crime praticado com emprego de",["grave ameaça ou violência a pessoa.","fraude.","destreza.","chave falsa.","abuso de confiança."],"Art. 183, I.")
q(2,"A diferença entre isenção de pena (art. 181) e representação (art. 182) está",["no grau de parentesco: mais próximo, isenção; menos próximo, representação.","no valor do bem.","na idade da vítima.","no local do crime.","no horário."],"Arts. 181 e 182.")
q(2,"Na receptação culposa, a pena de detenção de um mês a um ano pode ser acompanhada de",["multa, ou ambas as penas.","reclusão.","perda de bens.","prisão perpétua.","trabalho forçado."],"Art. 180, § 3º.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Receptação própria: reclusão de dois a seis anos e multa; qualificada: reclusão de três a oito anos e multa; culposa: detenção de um mês a um ano, ou multa, ou ambas.","Receptação própria: detenção; qualificada: multa.","Própria: reclusão de três a oito anos; culposa: reclusão.","Qualificada: reclusão de dois a seis anos.","Culposa: reclusão de um a quatro anos."],"Art. 180, caput e §§ 1º e 3º.")
q(3,"Considere as afirmações. I. A receptação própria exige que o agente saiba que a coisa é produto de crime. II. A receptação qualificada é praticada no exercício de atividade comercial ou industrial. III. A receptação culposa exige dolo. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A receptação culposa não exige dolo (art. 180, § 3º).")
q(3,"Assinale a INCORRETA.",["A receptação é punível apenas se o autor do crime anterior for conhecido.","A receptação de animal tem pena de reclusão de três a oito anos e multa.","Os bens públicos têm a pena do caput em dobro.","A imunidade entre parentes não se aplica ao roubo.","A isenção de pena se aplica ao cônjuge na constância da sociedade conjugal."],"Art. 180, § 4º: punível ainda que desconhecido o autor.")
q(3,"No art. 180, o crime do caput e o do § 1º diferem porque, no § 1º,",["o agente atua no exercício de atividade comercial ou industrial e deve saber a origem criminosa.","o agente é primário.","o agente é funcionário.","a pena é menor.","a vítima é idosa."],"Art. 180, §§ 1º e 2º.")
q(3,"O art. 183 do Código Penal afasta a imunidade se o crime é praticado",["contra pessoa com 60 anos ou mais.","contra o cônjuge.","contra o filho.","contra o irmão.","contra o tio."],"Art. 183, III.")
q(3,"Se o filho furta o pai idoso, de 70 anos, o filho",["não é isento de pena, pois a vítima tem 60 anos ou mais.","é isento de pena.","responde por representação.","responde por queixa.","não responde."],"Art. 183, III.")
q(3,"Se o filho furta a mãe de 50 anos, sem violência, o filho",["é isento de pena.","responde por furto qualificado.","responde por roubo.","responde por apropriação.","responde por representação."],"Art. 181, II.")
q(3,"Se o irmão furta o irmão, sem violência, procede-se mediante",["representação.","queixa.","denúncia incondicionada.","requisição do Ministro.","requisição do juiz."],"Art. 182, II.")
q(3,"Se o genro furta o sogro, sem violência, a imunidade do art. 181",["não se aplica, pois o sogro não é ascendente do agente.","aplica-se.","aplica-se só se coabitam.","aplica-se só se há representação.","aplica-se se o sogro é idoso."],"Art. 181 não abrange afins.")
q(3,"A imunidade do art. 181 aplica-se ao estranho que participa do crime?",["Não, nos termos do art. 183, II.","Sim, sempre.","Sim, se o parente concordar.","Sim, se for menor.","Sim, se houver representação."],"Art. 183, II.")
q(3,"A receptação do § 3º do art. 180, punida com detenção, exige que a coisa, pelas circunstâncias, deva",["presumir-se obtida por meio criminoso.","ser guardada.","ser consumida.","ser devolvida.","ser vendida."],"Art. 180, § 3º.")
q(3,"O art. 180, § 7º, aplica em dobro a pena da receptação de fios, cabos ou equipamentos de energia ou telefonia. Essa regra se aplica à pena",["do caput ou do § 1º, conforme o caso.","do § 3º.","do art. 180-A.","do art. 183-A.","do art. 181."],"Art. 180, § 7º.")
q(3,"O aumento do § 8º do art. 180 (organização criminosa ultraviolenta) é de",["dois terços.","um terço.","metade.","dobro.","triplo."],"Art. 180, § 8º.")
q(3,"A receptação de semovente domesticável de produção, no art. 180-A, aplica-se ainda que o animal esteja",["abatido ou dividido em partes.","vivo, apenas.","em estimação, apenas.","registrado.","vacinado."],"Art. 180-A.")
q(3,"Assinale a alternativa correta sobre as hipóteses de imunidade do art. 181.",["Aplica-se ao crime em prejuízo do cônjuge na constância da sociedade conjugal e de ascendente ou descendente, salvo as exceções do art. 183.","Aplica-se ao crime em prejuízo de irmão.","Aplica-se ao roubo.","Aplica-se ao estranho.","Aplica-se a qualquer parente."],"Arts. 181 e 183.")
q(3,"No art. 180, o dolo da receptação do caput é",["direto: o agente sabe que a coisa é produto de crime.","eventual apenas.","culposo.","preterdoloso.","inexistente."],"Art. 180, caput.")
q(3,"A receptação qualificada, do § 1º, pune a conduta de quem “deve saber” a origem criminosa da coisa, o que a diferencia da receptação própria porque",["amplia o dolo, incluindo o dolo eventual no contexto da atividade comercial.","exige dolo direto.","dispensa a prova do crime anterior.","exclui a atividade comercial.","reduz a pena."],"Art. 180, § 1º.")
q(3,"No texto do celular, a pena da receptação culposa é de",["detenção, de um mês a um ano, ou multa, ou ambas as penas.","reclusão, de dois a seis anos.","reclusão, de três a oito anos.","detenção, de dois a seis anos.","multa, apenas."],"Art. 180, § 3º.","cp12a")
q(3,"No texto do ferro-velho, a pena da receptação qualificada é de reclusão de três a oito anos e multa, e, com o § 7º, é aplicada",["em dobro.","aumentada de um terço.","reduzida.","mantida.","aumentada de dois terços."],"Art. 180, §§ 1º e 7º.","cp12b")
q(3,"No texto do ferro-velho, o dever de cuidado do comerciante justifica a pena maior da receptação qualificada porque o comerciante",["tem a atividade comercial e deve saber a origem da coisa.","é mais rico.","é mais velho.","é funcionário.","é estrangeiro."],"Art. 180, § 1º.","cp12b")
assert len(Q)==60,len(Q)
code,svg=mapa("Receptação e disposições gerais",[
 ("rec","Receptação própria",["reclusão, 2 a 6 anos, e multa","sabe ser produto de crime","autor do crime pode ser desconhecido"],"seção 1"),
 ("qual","Qualificada",["reclusão, 3 a 8 anos, e multa","atividade comercial","deve saber"],"seção 1"),
 ("culp","Culposa",["detenção, 1 mês a 1 ano","preço desproporcional","deve presumir"],"seção 2"),
 ("aum","Aumentos",["bem público: dobro","fios e cabos: dobro","organização: 2/3"],"seção 2"),
 ("anim","Receptação de animal",["art. 180-A","reclusão, 3 a 8 anos","produção ou comercialização"],"seção 2"),
 ("imun","Crime entre parentes",["isenção: cônjuge, ascendente, descendente","representação: separado, irmão, tio","exceções: roubo, estranho, 60 anos"],"seção 3")],
 "Na prova: separe o que “sabe” (própria) do que “deve saber” (qualificada) e do que “deve presumir” (culposa)")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As duas primeiras caixas são as figuras da receptação; as demais, os aumentos e as regras de família.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 180 a 183-A, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-12","Receptação e disposições gerais (CP, arts. 180 a 183-A)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 180 a 183-A. Cobertos todos, incluindo os §§ 6º a 8º do art. 180 e o art. 180-A."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","As expressões imunidade absoluta e relativa são doutrinárias.","As referências a cônjuge desquitado e a parentesco legítimo ou ilegítimo seguem o texto da lei, que usa termos antigos.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp12a e cp12b fictícios."],
 fontes_conferidas=["CP, arts. 180 a 183-A: texto da Câmara, copiado por programa."])
gravar("cp-12",aula_html,banco("cp-12",Q),tx)
