import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A usurpação e o dano são os crimes patrimoniais sem subtração: o primeiro atinge o imóvel, a água e as marcas de propriedade, e o segundo, a coisa que é destruída, inutilizada ou deteriorada. A Vunesp cobra os arts. 161 a 167 pelo conceito de cada crime, pelo esbulho possessório e pela invasão de terrenos, pelo dano qualificado (patrimônio público, explosivo, violência) e pela ação penal, que no dano simples é privada. Para o guarda, o assunto toca invasões de terreno, pichações e danos ao patrimônio público."
S={}
S[1]="## 1. Usurpação\n\n"+L("art. 161, caput e § 1º","Art. 161. Suprimir ou deslocar tapume","§ 2º Se o agente usa")+"""

A usurpação de limites é suprimir ou deslocar tapume, marco ou outro sinal indicativo de linha divisória, para se apropriar, no todo ou em parte, de coisa imóvel alheia. A pena é de detenção de um a seis meses e multa. Nas mesmas penas incorre quem desvia ou represa, em proveito próprio ou de outrem, águas alheias (usurpação de águas), e quem invade, com violência a pessoa ou grave ameaça, ou mediante concurso de mais de duas pessoas, terreno ou edifício alheio, para o fim de esbulho possessório. Esse último é o crime que mais aparece nas invasões: não basta entrar, é preciso o fim de esbulho, isto é, de tomar a posse do imóvel, e a violência ou o grupo de mais de duas pessoas.

"""+L("art. 161, §§ 2º e 3º","§ 2º Se o agente usa de violência","Supressão ou alteração de marca em animais")+"\n\n"+L("art. 162","Art. 162. Suprimir ou alterar","CAPÍTULO IV")+"""

Se há violência, o agente responde também pela pena dela. Se a propriedade é particular e não há violência, procede-se mediante queixa. O art. 162 pune quem suprime ou altera, indevidamente, marca ou sinal de propriedade em gado ou rebanho alheio, com detenção de seis meses a três anos e multa.
"""
S[2]="## 2. Dano\n\n"+L("art. 163, caput","Art. 163. Destruir, inutilizar","Dano qualificado")+"\n\n"+L("art. 163, parágrafo único","Parágrafo único. Se o crime é cometido:","Introdução ou abandono")+"""

O dano é destruir, inutilizar ou deteriorar coisa alheia, com detenção de um a seis meses ou multa. Os três verbos têm sentidos diferentes: destruir é acabar com a coisa, inutilizar é torná-la imprestável para o fim a que serve, e deteriorar é estragá-la em parte. A pichação de um muro, por exemplo, deteriora. O dano qualificado, de pena de detenção de seis meses a três anos e multa, além da pena da violência, ocorre se o crime é cometido com violência a pessoa ou grave ameaça, com emprego de substância inflamável ou explosiva (se não constitui crime mais grave), contra o patrimônio da União, Estado, DF, Município ou de autarquia, fundação pública, empresa pública, sociedade de economia mista ou empresa concessionária de serviços públicos, ou por motivo egoístico ou com prejuízo considerável para a vítima.

Para a Guarda Municipal, o inciso III é o mais próximo do trabalho: o dano ao patrimônio do Município, como a depredação de praça, de ponto de ônibus e de prédio público, é dano qualificado.
"""
S[3]="## 3. Outras figuras e ação penal\n\n"+L("art. 164","Art. 164. Introduzir ou deixar animais","Dano em coisa de valor artístico")+"\n\n"+L("arts. 165 e 166","Art. 165. Destruir, inutilizar","Ação penal")+"\n\n"+L("art. 167","Art. 167. Nos casos do art. 163","CAPÍTULO V")+"""

Introduzir ou deixar animais em propriedade alheia, sem consentimento de quem de direito, é crime se do fato resulta prejuízo, com detenção de quinze dias a seis meses ou multa. Destruir, inutilizar ou deteriorar coisa tombada pela autoridade competente em razão de valor artístico, arqueológico ou histórico é crime, com detenção de seis meses a dois anos e multa. E alterar, sem licença, o aspecto de local especialmente protegido por lei tem detenção de um mês a um ano, ou multa.

A ação penal é, no dano simples (art. 163, caput), no dano por motivo egoístico ou com prejuízo considerável (inciso IV) e na introdução de animais (art. 164), de queixa. No dano qualificado dos incisos I a III, a ação é pública. Essa é a pegadinha: quem lê só o art. 167 acha que todo dano é de ação privada.
"""
S[5]="""## 5. Na rotina do guarda

- **Pichação e depredação:** o guarda registra, e a pena do dano qualificado vale quando o bem é público ou concessionário, como ponto de ônibus.
- **Invasão de terreno:** a invasão por mais de duas pessoas, para tomar posse, é esbulho possessório (art. 161, § 1º, II); o guarda deve acionar a autoridade e preservar a situação.
- **Patrimônio tombado:** danos a bens tombados têm pena de detenção de seis meses a dois anos e multa.
- **Animais soltos em propriedade alheia:** o art. 164 só pune se houver prejuízo, e a ação é de queixa.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do dano simples | Detenção de um a seis meses, ou multa |
| Pena do dano qualificado | Detenção de seis meses a três anos, e multa |
| Dano ao patrimônio municipal | Qualificado (parágrafo único, III) |
| Ação penal do dano | Simples: queixa; qualificado I a III: pública |
| Esbulho possessório | Exige violência, grave ameaça ou mais de duas pessoas |
| Usurpação de limites | Suprimir ou deslocar marco para apropriar-se de imóvel |
| Introdução de animais | Só é crime se houver prejuízo |
| Dano em coisa tombada | Detenção de seis meses a dois anos, e multa |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Usurpação de limites | Detenção, 1 a 6 meses, e multa |
| Esbulho possessório | Invadir terreno ou edifício com violência, grave ameaça ou mais de duas pessoas |
| Marca em animais | Detenção, 6 meses a 3 anos, e multa |
| Dano | Detenção, 1 a 6 meses, ou multa; queixa |
| Dano qualificado | Detenção, 6 meses a 3 anos, e multa |
| Animais em propriedade alheia | Detenção, 15 dias a 6 meses, ou multa |
| Coisa tombada | Detenção, 6 meses a 2 anos, e multa |
| Local protegido | Detenção, 1 mês a 1 ano, ou multa |
"""
QR=[("Questão 1","A pena do crime de dano simples (art. 163, caput) é de",["detenção, de um a seis meses, ou multa.","detenção, de seis meses a três anos, e multa.","reclusão, de um a quatro anos.","detenção, de um a três anos.","multa, apenas."],0,"Art. 163, caput."),
("Questão 2","O dano cometido contra o patrimônio de Município é",["dano qualificado, com detenção de seis meses a três anos, e multa.","dano simples.","furto.","atípico.","contravenção."],2,"Art. 163, parágrafo único, III."),
("Questão 3","O esbulho possessório de terreno alheio exige, entre outras hipóteses,",["violência a pessoa, grave ameaça ou concurso de mais de duas pessoas.","simples entrada.","autorização do dono.","passagem rápida.","nenhuma circunstância."],1,"Art. 161, § 1º, II."),
("Questão 4","No dano simples, procede-se mediante",["queixa.","denúncia incondicionada.","representação.","requisição do Ministro.","requisição do juiz."],4,"Art. 167.")]
t1="<strong>Pichação em ponto de ônibus</strong><br><br>Um grupo de jovens pichou o abrigo de um ponto de ônibus de Vila Nova, cidade fictícia, que é de propriedade da concessionária do transporte coletivo. A Guarda Municipal flagrou um deles."
t2="<strong>Invasão de terreno</strong><br><br>Cerca de quarenta pessoas invadiram um terreno particular, cercaram uma área e começaram a erguer barracos, com o fim de se estabelecer ali. Não houve violência nem ameaça. A Guarda Municipal foi acionada pelo proprietário."
tx={"cp9a":t1,"cp9b":t2}
# n=1
q(1,"A pena do dano simples é de",["detenção, de um a seis meses, ou multa.","detenção, de seis meses a três anos, e multa.","reclusão, de um a quatro anos.","detenção, de um a três anos.","multa, apenas."],"Art. 163, caput.")
q(1,"O dano consiste em destruir, inutilizar ou deteriorar coisa",["alheia.","própria.","comum.","sem dono.","abandonada."],"Art. 163, caput.")
q(1,"A pena do dano qualificado é de",["detenção, de seis meses a três anos, e multa, além da pena correspondente à violência.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de um a três anos.","multa, apenas."],"Art. 163, parágrafo único.")
q(1,"Qualifica o dano o crime cometido",["com violência a pessoa ou grave ameaça.","com a coisa abandonada.","contra coisa própria.","sem prejuízo.","com consentimento do dono."],"Art. 163, parágrafo único, I.")
q(1,"Qualifica o dano o crime cometido",["contra o patrimônio da União, de Estado, do DF ou de Município.","contra patrimônio particular, apenas.","contra coisa comum.","sem violência.","contra vizinho."],"Art. 163, parágrafo único, III.")
q(1,"Qualifica o dano o crime cometido com emprego de substância",["inflamável ou explosiva, se o fato não constitui crime mais grave.","comum.","inerte.","medicinal.","alimentícia."],"Art. 163, parágrafo único, II.")
q(1,"Qualifica o dano o crime cometido",["por motivo egoístico ou com prejuízo considerável para a vítima.","por esquecimento.","por brincadeira.","sem dolo.","por consentimento."],"Art. 163, parágrafo único, IV.")
q(1,"A usurpação de limites é a conduta de suprimir ou deslocar tapume, marco ou sinal indicativo de linha divisória para",["apropriar-se, no todo ou em parte, de coisa imóvel alheia.","vender o terreno.","construir.","plantar.","alugar o imóvel."],"Art. 161, caput.")
q(1,"A pena da usurpação de limites é de",["detenção, de um a seis meses, e multa.","reclusão, de um a quatro anos.","detenção, de seis meses a três anos.","multa.","reclusão, de dois a oito anos."],"Art. 161, caput.")
q(1,"Na mesma pena da usurpação de limites incorre quem",["desvia ou represa, em proveito próprio ou de outrem, águas alheias.","paga o aluguel.","cerca o próprio terreno.","faz a divisa.","compra o terreno."],"Art. 161, § 1º, I.")
q(1,"O esbulho possessório consiste em invadir terreno ou edifício alheio",["com o fim de esbulho possessório, com violência, grave ameaça ou concurso de mais de duas pessoas.","por curiosidade.","para passeio.","para visita.","com consentimento."],"Art. 161, § 1º, II.")
q(1,"A pena da supressão ou alteração de marca em animais (art. 162) é de",["detenção, de seis meses a três anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa.","reclusão, de dois a oito anos."],"Art. 162.")
q(1,"A introdução ou o abandono de animais em propriedade alheia só é crime se do fato resulta",["prejuízo.","lucro.","alegria.","dívida.","nenhum efeito."],"Art. 164.")
q(1,"A pena do crime do art. 164 (introdução de animais) é de",["detenção, de quinze dias a seis meses, ou multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","multa, apenas."],"Art. 164.")
q(1,"Destruir, inutilizar ou deteriorar coisa tombada pela autoridade competente em virtude de valor artístico, arqueológico ou histórico tem pena de",["detenção, de seis meses a dois anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa.","reclusão, de dois a oito anos."],"Art. 165.")
q(1,"Alterar, sem licença, o aspecto de local especialmente protegido por lei tem pena de",["detenção, de um mês a um ano, ou multa.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos, e multa.","multa, apenas.","detenção, de dois a oito anos."],"Art. 166.")
q(1,"No dano, ressalvados os casos do parágrafo único, I a III, a ação penal é, em regra,",["de queixa.","pública incondicionada.","pública condicionada à representação.","por requisição do Ministro.","por requisição do juiz."],"Art. 167.")
q(1,"No texto da pichação, a concessionária de serviço público é a titular do bem. O dano, em tese, é",["qualificado, pelo art. 163, parágrafo único, III.","simples.","furto.","atípico.","contravenção penal."],"Art. 163, parágrafo único, III: “empresa concessionária de serviços públicos”.","cp9a")
q(1,"No texto da invasão, a conduta de invadir terreno alheio com o fim de estabelecer-se ali caracteriza, em tese,",["esbulho possessório.","furto.","roubo.","dano.","estelionato."],"Art. 161, § 1º, II.","cp9b")
q(1,"A introdução de animais em propriedade alheia (art. 164) exige que ela se dê",["sem consentimento de quem de direito.","com consentimento do dono.","com fim de lucro.","por menor.","com violência."],"Art. 164.")
# n=2
q(2,"A diferença entre destruir, inutilizar e deteriorar é que deteriorar é",["estragar a coisa em parte.","acabar com a coisa.","tornar a coisa imprestável.","vender a coisa.","guardar a coisa."],"Art. 163, caput (sentido doutrinário).")
q(2,"A supressão ou o deslocamento de marco para apropriar-se de imóvel alheio configura",["usurpação de limites.","furto.","roubo.","dano.","esbulho."],"Art. 161, caput.")
q(2,"Se o agente usa de violência na usurpação, incorre",["também na pena correspondente à violência.","apenas na pena da usurpação.","em pena em dobro.","em pena em triplo.","em pena de multa."],"Art. 161, § 2º.")
q(2,"Se a propriedade é particular e não há emprego de violência, a usurpação é de ação",["mediante queixa.","pública incondicionada.","por representação.","por requisição do Ministro.","por requisição do juiz."],"Art. 161, § 3º.")
q(2,"O dano qualificado pelo emprego de substância inflamável ou explosiva só se aplica",["se o fato não constitui crime mais grave.","em qualquer caso.","se houver violência.","se houver ameaça.","se houver dano ao patrimônio público."],"Art. 163, parágrafo único, II.")
q(2,"O dano é qualificado se o crime é cometido contra o patrimônio de",["autarquia, fundação pública, empresa pública, sociedade de economia mista ou empresa concessionária de serviços públicos.","pessoa física apenas.","empresa privada comum.","associação privada.","condomínio."],"Art. 163, parágrafo único, III.")
q(2,"Nos casos do art. 163, caput, do inciso IV do parágrafo único e do art. 164, procede-se mediante",["queixa.","denúncia incondicionada.","representação.","requisição do Ministro da Justiça.","requisição do juiz."],"Art. 167.")
q(2,"No dano qualificado pelo inciso I do parágrafo único (violência ou grave ameaça), a ação penal é",["pública.","de queixa.","condicionada à requisição.","privada subsidiária.","inexistente."],"Art. 167 não abrange os incisos I a III.")
q(2,"A pena do dano qualificado inclui, além da detenção e da multa,",["a pena correspondente à violência.","a pena de reclusão.","a perda do cargo.","a prisão perpétua.","nenhuma pena adicional."],"Art. 163, parágrafo único.")
q(2,"A destruição de coisa tombada é punida com detenção de seis meses a dois anos e multa porque a coisa é protegida em razão de valor",["artístico, arqueológico ou histórico.","comercial.","econômico apenas.","sentimental.","pessoal."],"Art. 165.")
q(2,"A alteração do aspecto de local especialmente protegido por lei, sem licença da autoridade competente, é crime do art.",["166.","161.","163.","164.","167."],"Art. 166.")
q(2,"Suprimir ou alterar, indevidamente, marca ou sinal indicativo de propriedade em gado ou rebanho alheio é crime com pena de",["detenção, de seis meses a três anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa.","reclusão, de dois a oito anos."],"Art. 162.")
q(2,"O art. 164 exige o consentimento de quem de direito para",["introduzir ou deixar animais em propriedade alheia.","criar animais em propriedade própria.","vender animais.","transportar animais.","tratar animais."],"Art. 164.")
q(2,"Na usurpação de águas, o agente",["desvia ou represa, em proveito próprio ou de outrem, águas alheias.","paga a conta de água.","limpa o rio.","coleta água da chuva.","usa a própria água."],"Art. 161, § 1º, I.")
q(2,"O esbulho possessório do art. 161, § 1º, II, tem a mesma pena da",["usurpação de limites (detenção de um a seis meses e multa).","do roubo.","da extorsão.","do furto.","do dano."],"Art. 161, § 1º: “na mesma pena incorre”.")
q(2,"No texto da pichação, a ação penal, por ser dano qualificado contra bem de concessionária, é",["pública.","de queixa.","condicionada à representação.","condicionada à requisição do Ministro.","subsidiária."],"Art. 163, parágrafo único, III, e art. 167.","cp9a")
q(2,"No texto da pichação, o ato de pintar o abrigo do ponto de ônibus é, quanto ao verbo do tipo,",["deteriorar.","destruir.","inutilizar.","subtrair.","apropriar-se."],"Art. 163, caput.","cp9a")
q(2,"No texto da invasão, a participação de quarenta pessoas atende, entre as hipóteses do § 1º, II, do art. 161, ao",["concurso de mais de duas pessoas.","uso de arma.","uso de explosivo.","uso de fraude.","uso de violência."],"Art. 161, § 1º, II.","cp9b")
q(2,"No texto da invasão, a ação penal é de queixa porque a propriedade é particular e não houve",["violência.","testemunha.","prejuízo.","denúncia.","consentimento."],"Art. 161, § 3º.","cp9b")
q(2,"A diferença entre dano e usurpação é que o dano atinge",["a integridade da coisa, enquanto a usurpação atinge a posse ou a propriedade do imóvel.","apenas imóveis.","apenas semoventes.","apenas águas.","apenas marcas."],"Arts. 161 e 163.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Dano simples: detenção de um a seis meses ou multa; dano qualificado: detenção de seis meses a três anos e multa; coisa tombada: detenção de seis meses a dois anos e multa.","Dano simples: reclusão; qualificado: detenção.","Dano simples: multa; qualificado: reclusão.","Dano simples: detenção de seis meses a três anos; coisa tombada: reclusão.","Dano simples: reclusão de um a quatro anos."],"Arts. 163 e 165.")
q(3,"Considere as afirmações. I. O dano ao patrimônio do Município é qualificado. II. O dano simples é de ação privada. III. O dano qualificado por violência é de ação privada. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"O art. 167 só se aplica ao caput e ao inciso IV.")
q(3,"Assinale a INCORRETA.",["A usurpação de limites tem pena de reclusão de um a seis anos.","O esbulho possessório exige violência, grave ameaça ou concurso de mais de duas pessoas.","A introdução de animais em propriedade alheia só é crime se resulta prejuízo.","O dano à coisa tombada tem pena de detenção de seis meses a dois anos e multa.","A alteração de local especialmente protegido tem pena de detenção de um mês a um ano, ou multa."],"A usurpação de limites tem detenção de um a seis meses, e multa.")
q(3,"A diferença entre o dano e o furto é que, no dano, o agente",["destrói, inutiliza ou deteriora, sem subtrair.","subtrai a coisa.","toma a coisa com violência.","engana a vítima.","retém a coisa."],"Arts. 155 e 163.")
q(3,"O dano qualificado do inciso IV exige motivo egoístico ou prejuízo considerável. Nesse caso, a ação penal é",["de queixa.","pública incondicionada.","por representação.","por requisição.","inexistente."],"Art. 167: “n. IV do seu parágrafo”.")
q(3,"A pena de seis meses a dois anos e multa corresponde ao crime de",["dano em coisa de valor artístico, arqueológico ou histórico.","dano simples.","introdução de animais.","usurpação de limites.","dano qualificado."],"Art. 165.")
q(3,"No esbulho possessório, o crime exige o fim de",["esbulho possessório.","passear.","visitar.","fotografar.","vender."],"Art. 161, § 1º, II.")
q(3,"A usurpação de águas é a conduta de",["desviar ou represar águas alheias.","pescar.","pagar água.","captar água de chuva.","limpar nascente."],"Art. 161, § 1º, I.")
q(3,"A introdução de animais em propriedade alheia é punida com detenção de",["quinze dias a seis meses, ou multa.","seis meses a dois anos.","um a seis meses.","um mês a um ano.","três meses a um ano."],"Art. 164.")
q(3,"No dano, a conduta de “inutilizar” significa",["tornar a coisa imprestável para o fim a que se destina.","acabar com a coisa.","estragar em parte.","subtrair.","vender."],"Art. 163, caput (sentido doutrinário).")
q(3,"O dano qualificado pelo prejuízo considerável para a vítima tem a pena de",["detenção, de seis meses a três anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa.","detenção, de um a dois anos."],"Art. 163, parágrafo único, IV.")
q(3,"A ação penal na usurpação de limites, se a propriedade é particular e sem violência, é de queixa. Se há violência, o agente responde",["também pela pena da violência.","somente pela usurpação.","por furto.","por roubo.","por estelionato."],"Art. 161, §§ 2º e 3º.")
q(3,"O art. 166 pune a alteração do aspecto de local especialmente protegido por lei, sem",["licença da autoridade competente.","dolo.","violência.","fraude.","testemunha."],"Art. 166.")
q(3,"A pena do art. 162 (marca em animais) é, em comparação com a do dano simples,",["maior, pois chega a três anos de detenção.","igual.","menor.","apenas multa.","reclusão."],"Art. 162: detenção de seis meses a três anos e multa.")
q(3,"Se o dano é cometido com emprego de substância inflamável e do fato resulta crime mais grave, como o de incêndio,",["não se aplica o inciso II, que é subsidiário.","aplica-se o inciso II.","aplica-se o inciso IV.","aplica-se a pena do furto.","aplica-se a pena do roubo."],"Art. 163, parágrafo único, II: “se o fato não constitui crime mais grave”.")
q(3,"Assinale a alternativa que associa corretamente o crime ao artigo.",["Dano em coisa tombada: art. 165; local protegido: art. 166; marca em gado: art. 162.","Dano em coisa tombada: art. 162; local protegido: art. 165.","Marca em gado: art. 164; animais: art. 166.","Local protegido: art. 163; dano: art. 167.","Dano: art. 161; usurpação: art. 163."],"Arts. 162, 165 e 166.")
q(3,"O art. 167 submete à ação de queixa os casos do art. 163, do inciso IV do seu parágrafo e do art. 164. Isso significa que o dano contra patrimônio da União é de ação",["pública.","de queixa.","condicionada.","por requisição do Ministro.","por requisição do juiz."],"Art. 167 não menciona os incisos I a III.")
q(3,"Se, na usurpação de limites, a propriedade é pública, a ação é",["pública, pois a queixa só se exige em propriedade particular.","de queixa.","por requisição do Ministro.","por representação.","sempre privada."],"Art. 161, § 3º: queixa se a propriedade é particular e sem violência.")
q(3,"No texto da pichação, a pena aplicável ao dano qualificado é de",["detenção, de seis meses a três anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa.","detenção, de um a dois anos."],"Art. 163, parágrafo único.","cp9a")
q(3,"No texto da invasão, a ação penal, por ser terreno particular e sem violência, é, nos termos do § 3º do art. 161,",["de queixa.","pública incondicionada.","de representação.","por requisição do juiz.","por requisição do Ministro."],"Art. 161, § 3º.","cp9b")
assert len(Q)==60,len(Q)
code,svg=mapa("Usurpação e dano",[
 ("usurp","Usurpação de limites",["art. 161","marco, tapume, divisa","detenção, 1 a 6 meses, e multa"],"seção 1"),
 ("esb","Esbulho e águas",["invadir com violência","ou mais de duas pessoas","desviar águas alheias"],"seção 1"),
 ("dano","Dano",["destruir, inutilizar, deteriorar","detenção, 1 a 6 meses, ou multa","queixa"],"seção 2"),
 ("qual","Dano qualificado",["6 meses a 3 anos, e multa","patrimônio público","explosivo ou violência"],"seção 2"),
 ("out","Outras figuras",["marca em gado: 6 meses a 3 anos","animais: 15 dias a 6 meses","coisa tombada: 6 meses a 2 anos"],"seção 3"),
 ("acao","Ação penal",["dano simples: queixa","inciso IV: queixa","incisos I a III: pública"],"seção 3")],
 "Na prova: leia o parágrafo único do art. 163 para saber se o dano é qualificado e qual é a ação penal")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira caixa trata do imóvel; a segunda e a terceira, da coisa destruída; a última, de quem propõe a ação.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 161 a 167, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-9","Usurpação e dano (CP, arts. 161 a 167)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 161 a 167. Cobertos todos os artigos."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","Os sentidos de destruir, inutilizar e deteriorar são doutrinários; não constam do texto da lei.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp9a e cp9b fictícios."],
 fontes_conferidas=["CP, arts. 161 a 167: texto da Câmara, copiado por programa."])
gravar("cp-9",aula_html,banco("cp-9",Q),tx)
