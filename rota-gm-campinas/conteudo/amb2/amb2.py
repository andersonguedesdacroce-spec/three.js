import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='amb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes contra a flora (arts. 38 a 53 da Lei 9.605/1998) tratam do corte e destruição de florestas, do incêndio, dos balões, da extração de minerais e da madeira ilegal. É conteúdo cobrado por alternativas de pena e por detalhes como o balão em área urbana, o uso de motosserra sem licença e as causas de aumento do art. 53. Para o guarda municipal, as ocorrências típicas são a poda irregular, a queima de vegetação e a soltura de balões."
S={}
S[1]="## 1. Florestas de preservação permanente e unidades de conservação\n\n"+L("arts. 38 a 39","Art. 38. Destruir ou danificar floresta","Art. 40.")+"\n\n"+L("art. 40","Art. 40. Causar dano direto ou indireto","Art. 40-A.")+"""

Destruir ou danificar floresta de preservação permanente, mesmo em formação, ou utilizá-la com infringência das normas de proteção, tem detenção de um a três anos, ou multa, ou ambas; se culposo, a pena é reduzida à metade. O mesmo vale para a vegetação do bioma Mata Atlântica em estágio avançado ou médio de regeneração. Cortar árvores em floresta de preservação permanente sem permissão tem detenção de um a três anos, ou multa, ou ambas. Causar dano às Unidades de Conservação tem reclusão de um a cinco anos; as Unidades de Proteção Integral são as Estações Ecológicas, as Reservas Biológicas, os Parques Nacionais, os Monumentos Naturais e os Refúgios de Vida Silvestre; o dano a espécies ameaçadas no interior delas agrava a pena, e se culposo a pena é reduzida à metade.
"""
S[2]="## 2. Incêndio, balões, extração e madeira\n\n"+L("arts. 41 e 42","Art. 41. Provocar incêndio","Art. 43.")+"\n\n"+L("arts. 44 a 46","Art. 44. Extrair de florestas","Art. 47.")+"\n\n"+L("art. 48","Art. 48. Impedir ou dificultar a regeneração","Art. 49.")+"""

Provocar incêndio em floresta ou em demais formas de vegetação tem reclusão de dois a quatro anos e multa; se culposo, detenção de seis meses a um ano e multa. Fabricar, vender, transportar ou soltar balões que possam provocar incêndios nas florestas e em áreas urbanas ou qualquer assentamento humano tem detenção de um a três anos ou multa, ou ambas. Extrair de florestas de domínio público ou de preservação permanente, sem autorização, pedra, areia, cal ou minerais tem detenção de seis meses a um ano e multa. Cortar ou transformar em carvão madeira de lei, em desacordo com as determinações legais, tem reclusão de um a dois anos e multa. Receber ou adquirir madeira, lenha ou carvão para fins comerciais sem exigir a licença do vendedor tem detenção de seis meses a um ano e multa. Impedir ou dificultar a regeneração natural de florestas tem detenção de seis meses a um ano e multa.
"""
S[3]="## 3. Plantas ornamentais, florestas públicas, motosserra e agravantes\n\n"+L("art. 49","Art. 49. Destruir, danificar, lesar","Art. 50.")+"\n\n"+L("arts. 50 e 50-A","Art. 50. Destruir ou danificar florestas nativas","Art. 51.")+"\n\n"+L("arts. 51 e 52","Art. 51. Comercializar motosserra","Art. 53.")+"\n\n"+L("art. 53","Art. 53. Nos crimes previstos nesta Seção","Seção III")+"""

Destruir, danificar, lesar ou maltratar plantas de ornamentação de logradouros públicos ou em propriedade privada alheia tem detenção de três meses a um ano, ou multa, ou ambas; no crime culposo, de um a seis meses ou multa. Não incorre em crime quem poda ou corta árvore quando o órgão ambiental não responder, de forma fundamentada, em 45 dias, a requerimento fundado em risco de acidente atestado por profissional habilitado.

Destruir florestas nativas ou plantadas ou vegetação fixadora de dunas e protetora de mangues tem detenção de três meses a um ano e multa. Desmatar ou explorar floresta em terras públicas ou devolutas sem autorização tem reclusão de dois a quatro anos e multa, não sendo crime a conduta necessária à subsistência imediata do agente ou de sua família. Comercializar motosserra ou utilizá-la em florestas sem licença ou registro tem detenção de três meses a um ano e multa. Penetrar em unidades de conservação com instrumentos próprios para caça ou exploração, sem licença, tem detenção de seis meses a um ano e multa. Nos crimes desta seção, a pena é aumentada de um sexto a um terço se resulta diminuição de águas, erosão ou mudança climática, ou se o crime é cometido no período de queda das sementes, na formação de vegetações, contra espécies raras, em época de seca ou inundação, ou à noite, em domingo ou feriado.
"""
S[5]="""## 5. Na rotina do guarda

- **Balão:** fabricar, vender, transportar ou soltar balões que possam causar incêndio em áreas urbanas é crime com detenção de um a três anos ou multa.
- **Poda de árvore:** podar ou cortar sem autorização pode configurar crime; há exceção se o órgão ambiental não responde em 45 dias e há risco de acidente atestado.
- **Motosserra:** utilizá-la em floresta sem licença ou registro é crime.
- **Madeira ilegal:** transportar madeira ou carvão sem licença válida é crime; o guarda apreende e comunica o órgão ambiental.
- **Queimadas:** provocar incêndio em vegetação é crime de reclusão de dois a quatro anos e multa.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Art. 38 (floresta de preservação permanente) | Detenção de 1 a 3 anos, ou multa, ou ambas |
| Culposo | Pena reduzida à metade (arts. 38 e 40) |
| Art. 40 (unidades de conservação) | Reclusão de 1 a 5 anos |
| Art. 41 (incêndio) | Reclusão de 2 a 4 anos e multa; culposo: detenção de 6 meses a 1 ano |
| Art. 42 (balões) | Detenção de 1 a 3 anos ou multa, ou ambas |
| Art. 49 (plantas ornamentais) | Detenção de 3 meses a 1 ano, ou multa, ou ambas |
| Art. 50-A (florestas públicas) | Reclusão de 2 a 4 anos e multa; subsistência não é crime |
| Art. 51 (motosserra) | Detenção de 3 meses a 1 ano e multa |
| Art. 53 | Aumento de 1/6 a 1/3 |
| Poda | 45 dias sem resposta do órgão, com risco atestado |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 38 | Floresta de preservação permanente: detenção de 1 a 3 anos |
| Art. 39 | Cortar árvores sem permissão: 1 a 3 anos |
| Art. 40 | Unidades de conservação: reclusão de 1 a 5 anos |
| Art. 41 | Incêndio: reclusão de 2 a 4 anos |
| Art. 42 | Balões: detenção de 1 a 3 anos |
| Art. 44 | Extração de minerais: 6 meses a 1 ano |
| Art. 45 | Madeira de lei: reclusão de 1 a 2 anos |
| Art. 49 | Plantas ornamentais: 3 meses a 1 ano |
| Art. 50-A | Floresta pública: reclusão de 2 a 4 anos |
| Art. 51 | Motosserra: 3 meses a 1 ano |
| Art. 53 | Aumento de 1/6 a 1/3 |
"""
QR=[("Questão 1","Fabricar, vender, transportar ou soltar balões que possam provocar incêndios nas florestas e demais formas de vegetação, em áreas urbanas ou qualquer tipo de assentamento humano, tem pena de detenção de um a três anos ou",["multa, ou ambas as penas cumulativamente.","reclusão de cinco anos.","advertência.","nada.","prisão perpétua."],0,"Art. 42."),
("Questão 2","Provocar incêndio em floresta ou em demais formas de vegetação tem pena de",["reclusão, de dois a quatro anos, e multa.","detenção de seis meses a um ano.","multa apenas.","detenção de um a três anos.","reclusão de cinco a dez anos."],1,"Art. 41."),
("Questão 3","Comercializar motosserra ou utilizá-la em florestas e demais formas de vegetação, sem licença ou registro da autoridade competente, tem pena de detenção de três meses a",["um ano e multa.","dois anos.","três anos.","cinco anos.","seis meses."],2,"Art. 51."),
("Questão 4","Nos crimes contra a flora, a pena é aumentada de um sexto a um terço se o crime é cometido em época de",["seca ou inundação.","festa.","colheita.","eleição.","verão apenas."],3,"Art. 53, II, d.")]
t1="<strong>Balão sobre o bairro</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, flagrou dois homens soltando balões de papel com fogo numa noite de festa junina, em área urbana."
t2="<strong>Poda sem autorização</strong><br><br>Um morador de Vila Nova cortou uma árvore da calçada que ameaçava cair, sem aguardar o órgão ambiental, que ainda não havia respondido ao pedido feito há 20 dias."
t3="<strong>Carvão sem licença</strong><br><br>Um caminhão parado numa blitz transportava carvão vegetal sem licença válida para toda a viagem."
tx={"amb2a":t1,"amb2b":t2,"amb2c":t3}
# n=1
q(1,"Destruir ou danificar floresta considerada de preservação permanente tem pena de detenção de um a três anos, ou multa, ou",["ambas as penas cumulativamente.","reclusão de cinco anos.","advertência.","nada.","prisão perpétua."],"Art. 38.")
q(1,"Se o crime do art. 38 for culposo, a pena será reduzida",["à metade.","a um terço.","ao dobro.","a um sexto.","a zero."],"Art. 38, parágrafo único.")
q(1,"Cortar árvores em floresta de preservação permanente, sem permissão da autoridade competente, tem pena de detenção de um a",["três anos, ou multa, ou ambas cumulativamente.","dois anos.","cinco anos.","seis meses.","dez anos."],"Art. 39.")
q(1,"Causar dano direto ou indireto às Unidades de Conservação tem pena de",["reclusão de um a cinco anos.","detenção de seis meses.","multa apenas.","detenção de dois anos.","advertência."],"Art. 40.")
q(1,"Entre as Unidades de Conservação de Proteção Integral estão as Estações Ecológicas, as Reservas Biológicas, os Parques Nacionais, os Monumentos Naturais e os Refúgios de Vida",["Silvestre.","Urbana.","Rural.","Marinha.","Pública."],"Art. 40, § 1º.")
q(1,"Provocar incêndio em floresta, se culposo, tem pena de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 41, parágrafo único.")
q(1,"Extrair de florestas de domínio público, sem prévia autorização, pedra, areia, cal ou qualquer espécie de minerais tem pena de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 44.")
q(1,"Cortar ou transformar em carvão madeira de lei, em desacordo com as determinações legais, tem pena de reclusão de um a",["dois anos, e multa.","três anos.","quatro anos.","seis meses.","dez anos."],"Art. 45.")
q(1,"Receber ou adquirir, para fins comerciais, madeira, lenha ou carvão sem exigir a licença do vendedor tem pena de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 46.")
q(1,"Impedir ou dificultar a regeneração natural de florestas tem pena de detenção de seis meses a um ano e",["multa.","reclusão.","advertência.","nada.","prisão."],"Art. 48.")
q(1,"Destruir, danificar, lesar ou maltratar plantas de ornamentação de logradouros públicos tem pena de detenção de três meses a um ano, ou multa, ou",["ambas as penas cumulativamente.","reclusão de cinco anos.","advertência.","nada.","prisão perpétua."],"Art. 49.")
q(1,"No crime culposo do art. 49, a pena é de um a seis meses, ou",["multa.","reclusão.","advertência.","nada.","prisão perpétua."],"Art. 49, § 1º.")
q(1,"Destruir ou danificar florestas nativas ou plantadas ou vegetação fixadora de dunas, protetora de mangues tem pena de detenção de três meses a um ano e",["multa.","reclusão.","advertência.","nada.","perdão."],"Art. 50.")
q(1,"Desmatar ou explorar floresta em terras de domínio público ou devolutas, sem autorização, tem pena de reclusão de dois a quatro anos e",["multa.","advertência.","nada.","perdão.","detenção."],"Art. 50-A.")
q(1,"Não é crime do art. 50-A a conduta necessária à subsistência imediata pessoal do agente ou de sua",["família.","empresa.","vizinhança.","comunidade.","igreja."],"Art. 50-A, § 1º.")
q(1,"Penetrar em Unidades de Conservação conduzindo instrumentos próprios para caça, sem licença, tem pena de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 52.")
q(1,"No texto do balão sobre o bairro, soltar balões com fogo em área urbana corresponde ao art.",["42.","41.","44.","45.","51."],"Art. 42.","amb2a")
q(1,"No texto da poda sem autorização, a exceção do art. 49, § 2º, exige que o órgão ambiental não responda no prazo máximo de",["45 dias.","15 dias.","30 dias.","60 dias.","90 dias."],"Art. 49, § 2º.","amb2b")
q(1,"No texto do carvão sem licença, o transporte de carvão sem licença válida corresponde ao art.",["46, parágrafo único.","41.","42.","49.","51."],"Art. 46, parágrafo único.","amb2c")
q(1,"Fabricar balões que possam provocar incêndios em áreas urbanas é crime previsto no art.",["42.","38.","40.","44.","51."],"Art. 42.")
# n=2
q(2,"O art. 38-A trata da destruição de vegetação do Bioma",["Mata Atlântica.","Cerrado.","Amazônia.","Pantanal.","Caatinga."],"Art. 38-A.")
q(2,"O dano a espécies ameaçadas de extinção no interior das Unidades de Conservação de Proteção Integral é circunstância",["agravante.","atenuante.","irrelevante.","excludente.","descriminante."],"Art. 40, § 2º.")
q(2,"Se o crime do art. 40 for culposo, a pena será reduzida",["à metade.","a um terço.","ao dobro.","a um sexto.","a zero."],"Art. 40, § 3º.")
q(2,"O art. 42 pune quem fabrica, vende, transporta ou solta balões que possam provocar incêndios em áreas",["urbanas ou qualquer tipo de assentamento humano.","apenas rurais.","apenas costeiras.","apenas privadas.","apenas desertas."],"Art. 42.")
q(2,"O art. 44 pune a extração de minerais em florestas de domínio público ou consideradas de",["preservação permanente.","produção.","lazer.","exploração.","cultura."],"Art. 44.")
q(2,"Incorre nas penas do art. 46 quem vende, expõe à venda, tem em depósito, transporta ou guarda madeira sem licença válida para todo o tempo da viagem ou do",["armazenamento.","pagamento.","negócio.","aluguel.","contrato."],"Art. 46, parágrafo único.")
q(2,"A poda ou corte de árvore não é crime se o órgão ambiental não responde de maneira fundamentada no prazo de",["45 dias a requerimento fundado em risco de acidente atestado.","10 dias.","30 dias.","60 dias.","90 dias."],"Art. 49, § 2º.")
q(2,"A realização da poda ou corte, no caso do art. 49, § 2º, considera-se tacitamente",["autorizada quando esgotado o prazo.","negada.","suspensa.","proibida.","adiada."],"Art. 49, § 2º.")
q(2,"Se a área explorada, no art. 50-A, for superior a 1.000 hectares, a pena será aumentada de",["um ano por milhar de hectare.","um mês por hectare.","um terço.","metade.","dobro."],"Art. 50-A, § 2º.")
q(2,"A pena dos crimes da Seção II é aumentada de um sexto a um terço se do fato resulta a diminuição de águas naturais, a erosão do solo ou a modificação do regime",["climático.","político.","fiscal.","militar.","religioso."],"Art. 53, I.")
q(2,"A pena é aumentada de um sexto a um terço se o crime é cometido no período de queda das",["sementes.","folhas.","frutas.","chuvas.","aves."],"Art. 53, II, a.")
q(2,"A pena é aumentada de um sexto a um terço se o crime é cometido durante a noite, em domingo ou",["feriado.","semana.","mês.","ano.","inverno."],"Art. 53, II, e.")
q(2,"A pena é aumentada de um sexto a um terço se o crime é cometido contra espécies raras ou ameaçadas, ainda que a ameaça ocorra somente no local da",["infração.","residência.","venda.","apreensão.","captura."],"Art. 53, II, c.")
q(2,"A comercialização de motosserra sem licença ou registro está prevista no art.",["51.","41.","42.","49.","53."],"Art. 51.")
q(2,"O art. 41 tem, no caso culposo, pena de detenção de seis meses a um ano e",["multa.","reclusão.","advertência.","nada.","perdão."],"Art. 41, parágrafo único.")
q(2,"No texto do balão sobre o bairro, o crime se aplica ao balão que possa provocar incêndios em florestas e demais formas de",["vegetação.","edificação.","navegação.","aviação.","mineração."],"Art. 42.","amb2a")
q(2,"No texto da poda sem autorização, o pedido ao órgão feito há 20 dias, sem resposta, é prazo",["inferior ao de 45 dias, portanto sem a excludente.","superior ao de 45 dias.","igual ao de 45 dias.","irrelevante.","maior que o legal."],"Art. 49, § 2º.","amb2b")
q(2,"No texto do carvão sem licença, o transporte sem licença válida para todo o tempo da viagem tem as mesmas penas do art.",["46.","41.","42.","49.","51."],"Art. 46, parágrafo único.","amb2c")
q(2,"A pena do art. 45, para quem corta ou transforma em carvão madeira de lei em desacordo com as determinações legais, é de reclusão de um a dois anos e",["multa.","perda do veículo.","advertência.","nada.","detenção."],"Art. 45.")
q(2,"O art. 48 pune quem impede ou dificulta a regeneração natural de florestas e demais formas de",["vegetação.","edificação.","rios.","dunas.","cidades."],"Art. 48.")
# n=3
q(3,"Assinale a alternativa correta sobre os crimes contra a flora.",["Provocar incêndio: reclusão de 2 a 4 anos e multa; balões: detenção de 1 a 3 anos ou multa; motosserra sem licença: detenção de 3 meses a 1 ano e multa.","Incêndio: detenção de 6 meses.","Balões: reclusão de 5 anos.","Motosserra: reclusão de 2 anos.","Incêndio culposo: reclusão."],"Arts. 41, 42 e 51.")
q(3,"Considere. I. A pena do art. 38 é reduzida à metade se culposo. II. O art. 53 aumenta a pena de um sexto a um terço. III. O art. 49 exige sempre reclusão. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O art. 49 tem detenção ou multa (art. 49).")
q(3,"Assinale a INCORRETA.",["O corte de madeira de lei tem detenção de 6 meses.","O art. 50-A não é crime se necessário à subsistência.","A poda tem a excludente de 45 dias.","O art. 53 aumenta a pena.","Soltar balão pode ser crime."],"O corte de madeira de lei tem reclusão de um a dois anos (art. 45).")
q(3,"Nas condutas dos arts. 38 e 38-A, a pena é de detenção de um a três anos, ou multa, ou ambas, e, se o crime for culposo, será",["reduzida à metade.","dobrada.","triplicada.","convertida em reclusão.","extinta."],"Arts. 38 e 38-A.")
q(3,"O art. 40 abrange também as áreas de que trata o art. 27 do Decreto 99.274/1990, independentemente de sua",["localização.","extensão.","propriedade.","idade.","origem."],"Art. 40.")
q(3,"A pena do art. 41, no caso doloso, é de reclusão de dois a quatro anos e multa; no culposo, de",["detenção de seis meses a um ano, e multa.","reclusão de dois anos.","multa apenas.","detenção de dois anos.","nada."],"Art. 41.")
q(3,"A conduta de receber ou adquirir madeira, lenha ou carvão sem exigir a licença do vendedor exige também munir-se da via que deverá acompanhar o produto até o final",["beneficiamento.","transporte.","negócio.","aluguel.","contrato."],"Art. 46.")
q(3,"No art. 49, a poda ou o corte pelo particular só afasta o crime se houver possibilidade de acidente atestada por empresa ou profissional",["habilitado.","vizinho.","qualquer.","autônomo.","eventual."],"Art. 49, § 2º.")
q(3,"A pena de reclusão de dois a quatro anos e multa é a do crime do art.",["50-A.","49.","51.","52.","44."],"Art. 50-A.")
q(3,"A pena de detenção de seis meses a um ano e multa, a do art. 52, aplica-se a quem penetra em Unidades de Conservação conduzindo substâncias próprias para caça ou para exploração de produtos ou subprodutos",["florestais.","aquáticos.","urbanos.","industriais.","agrícolas."],"Art. 52.")
q(3,"O aumento de pena do art. 53, II, d, ocorre se o crime é cometido em época de seca ou",["inundação.","chuva.","festa.","colheita.","plantio."],"Art. 53, II, d.")
q(3,"O aumento do art. 53 aplica-se aos crimes previstos na",["seção dos crimes contra a flora.","seção da fauna.","seção da poluição.","lei inteira.","lei de trânsito."],"Art. 53.")
q(3,"No texto do balão sobre o bairro, a noite e a área urbana, além do art. 42, podem levar ao aumento do art. 53, por ser crime cometido",["durante a noite, em domingo ou feriado.","em época de chuva.","em época de colheita.","em período de matrícula.","em horário comercial."],"Art. 53, II, e.","amb2a")
q(3,"No texto do balão sobre o bairro, a pena do crime é de detenção de um a três anos ou",["multa, ou ambas cumulativamente.","reclusão de cinco anos.","advertência.","nada.","prisão perpétua."],"Art. 42.","amb2a")
q(3,"No texto da poda sem autorização, o morador não incorre em crime somente se transcorrido o prazo de 45 dias; antes disso, o corte é",["conduta que pode configurar crime.","sempre lícito.","irrelevante.","incentivado.","dispensa autorização."],"Art. 49, § 2º.","amb2b")
q(3,"No texto da poda sem autorização, o risco de queda deve ser atestado por",["empresa ou profissional habilitado.","vizinho.","qualquer pessoa.","guarda.","delegado."],"Art. 49, § 2º.","amb2b")
q(3,"No texto do carvão sem licença, quem transporta carvão sem licença válida incorre nas mesmas penas de quem",["recebe ou adquire sem exigir a licença do vendedor.","provoca incêndio.","solta balões.","usa motosserra.","destrói mangues."],"Art. 46, parágrafo único.","amb2c")
q(3,"No texto do carvão sem licença, a pena aplicável é de detenção de seis meses a um ano e",["multa.","reclusão.","advertência.","nada.","perdão."],"Art. 46.","amb2c")
q(3,"A pena do art. 44 aplica-se a quem extrai pedra, areia, cal ou minerais de florestas de domínio público ou de preservação permanente sem prévia",["autorização.","licitação.","venda.","ordem judicial.","taxa."],"Art. 44.")
q(3,"No art. 53, a pena é aumentada de um sexto a um terço se o crime é cometido no período de formação de",["vegetações.","cidades.","rios.","dunas.","estradas."],"Art. 53, II, b.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes ambientais: flora (arts. 38 a 53)",[
 ("fpp","Floresta de preservação",["art. 38: detenção 1 a 3 anos","culposo: metade","corte sem permissão"],"seção 1"),
 ("uc","Unidades de conservação",["art. 40: reclusão 1 a 5","proteção integral","dano a ameaçadas agrava"],"seção 1"),
 ("inc","Incêndio e balões",["incêndio: reclusão 2 a 4","balões: detenção 1 a 3","área urbana"],"seção 2"),
 ("mad","Madeira e minerais",["madeira de lei: reclusão 1 a 2","carvão sem licença","extração: 6m a 1a"],"seção 2"),
 ("pla","Plantas e poda",["art. 49","45 dias","risco atestado"],"seção 3"),
 ("mot","Motosserra e aumento",["art. 51","art. 53: 1/6 a 1/3","noite, seca, espécies raras"],"seção 3")],
 "Na prova: balões em área urbana, motosserra e causas do art. 53")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz florestas e unidades de conservação; as demais, incêndio, balões, madeira, poda, motosserra e agravantes.","Fontes: Edital 02/2026, Anexo I; Lei 9.605/1998 (Lei de Crimes Ambientais), arts. 38 a 53, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("amb-2","Crimes ambientais: flora (arts. 38 a 53)",Q,list(tx),
 cobertura=["Cobertos: arts. 38 a 53, exceto os arts. 43 e 47 (vetados) e 40-A (vetado)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","O art. 40-A (vetado) traz, na consolidação, parágrafos sobre Unidades de Uso Sustentável; foram omitidos da aula e das questões.","Trechos de lei copiados de fontes/amb.txt por programa.","Casos amb2a, amb2b e amb2c fictícios."],
 fontes_conferidas=["Lei 9.605/1998, arts. 38 a 53: texto da Câmara, copiado por programa."])
gravar("amb-2",aula_html,banco("amb-2",Q),tx)
