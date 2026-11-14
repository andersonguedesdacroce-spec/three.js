import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='amb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O último bloco de crimes da Lei 9.605/1998 (arts. 54 a 69-A) reúne a poluição, a mineração sem autorização, os produtos tóxicos, as atividades poluidoras sem licença, a pichação, o patrimônio cultural e os crimes contra a administração ambiental. A Vunesp cobra a pena de cada um, os aumentos do art. 58 e a exceção do grafite no art. 65, § 2º. Para o guarda municipal, a pichação e a construção em solo não edificável são ocorrências comuns."
S={}
S[1]="## 1. Poluição, mineração e substâncias tóxicas\n\n"+L("art. 54, caput","Art. 54. Causar poluição","§ 1º Se o crime é culposo")+"\n\n"+L("art. 54, §§ 1º a 3º","§ 1º Se o crime é culposo","Art. 55.")+"\n\n"+L("art. 55","Art. 55. Executar pesquisa","Art. 56.")+"\n\n"+L("art. 56","Art. 56. Produzir, processar","Art. 57.")+"\n\n"+L("art. 58","Art. 58. Nos crimes dolosos","Art. 59.")+"""

Causar poluição de qualquer natureza em níveis que resultem ou possam resultar em danos à saúde humana, ou que provoquem a mortandade de animais ou a destruição significativa da flora, tem reclusão de um a quatro anos e multa; se culposo, detenção de seis meses a um ano e multa. A pena é de reclusão de um a cinco anos se a poluição torna uma área imprópria para a ocupação humana, provoca retirada de habitantes, interrompe o abastecimento público de água, impede o uso público das praias ou decorre de lançamento de resíduos em desacordo com a lei.

Executar pesquisa, lavra ou extração de recursos minerais sem autorização tem detenção de seis meses a um ano e multa. Produzir, processar, embalar, importar, comercializar, transportar ou guardar produto ou substância tóxica, perigosa ou nociva em desacordo com a lei tem reclusão de um a quatro anos e multa, aumentada de um sexto a um terço se for nuclear ou radioativa. Nos crimes dolosos desta seção, as penas aumentam de um sexto a um terço se resulta dano irreversível, de um terço até a metade se resulta lesão grave e até o dobro se resulta morte.
"""
S[2]="## 2. Atividade poluidora sem licença e disseminação de pragas\n\n"+L("arts. 60 e 61","Art. 60. Construir, reformar","Seção IV")+"""

Construir, reformar, ampliar, instalar ou fazer funcionar estabelecimentos, obras ou serviços potencialmente poluidores sem licença ou autorização dos órgãos ambientais tem detenção de seis meses a dois anos, ou multa, ou ambas; a pena aumenta até o dobro se o licenciamento exige Estudo Prévio de Impacto Ambiental. Disseminar doença, praga ou espécies que possam causar dano à agricultura, à pecuária, à fauna, à flora ou aos ecossistemas tem reclusão de um a quatro anos e multa.
"""
S[3]="## 3. Patrimônio cultural, pichação e administração ambiental\n\n"+L("art. 62","Art. 62. Destruir, inutilizar","Art. 63.")+"\n\n"+L("arts. 63 e 64","Art. 63. Alterar o aspecto","Art. 65.")+"\n\n"+L("art. 65, caput","Art. 65. Pichar ou por outro meio","§ 1º Se o ato for realizado")+"\n\n"+L("art. 65, § 1º","§ 1º Se o ato for realizado em monumento","§ 1º pela Lei nº 12.408")+"\n\n"+L("art. 65, § 2º","§ 2º Não constitui crime a prática de grafite","Seção V")+"\n\n"+L("arts. 66 e 67","Art. 66. Fazer o funcionário público","Parágrafo único. [revogado]")+"\n\n"+L("arts. 68 e 69","Art. 68. Deixar, aquele que tiver o dever","Art. 69-A.")+"\n\n"+L("art. 69-A","Art. 69-A. Elaborar ou apresentar","CAPÍTULO VI")+"""

Destruir, inutilizar ou deteriorar bem protegido por lei, ato administrativo ou decisão judicial, ou arquivo, museu, biblioteca ou instalação científica protegida, tem reclusão de um a três anos e multa; se culposo, detenção de seis meses a um ano. Alterar o aspecto ou a estrutura de edificação ou local especialmente protegido tem reclusão de um a três anos e multa. Promover construção em solo não edificável, ou no seu entorno, sem autorização, tem detenção de seis meses a um ano e multa.

Pichar ou conspurcar edificação ou monumento urbano tem detenção de três meses a um ano e multa; em monumento ou coisa tombada, a pena é de seis meses a um ano de detenção e multa. Não constitui crime o grafite realizado para valorizar o patrimônio público ou privado mediante manifestação artística, desde que consentido pelo proprietário e, no bem público, autorizado pelo órgão competente.

Contra a administração ambiental: o funcionário que faz afirmação falsa ou omite a verdade em licenciamento tem reclusão de um a três anos; quem concede dolosamente licença em desacordo com as normas ambientais, detenção de um a três anos e multa; quem deixa de cumprir obrigação de relevante interesse ambiental, detenção de um a três anos e multa; quem obsta a fiscalização, detenção de um a três anos e multa; e quem elabora estudo ambiental falso ou enganoso, reclusão de três a seis anos e multa.
"""
S[5]="""## 5. Na rotina do guarda

- **Pichação:** é crime (detenção de três meses a um ano e multa); em monumento ou bem tombado, seis meses a um ano. O guarda registra e conduz.
- **Grafite:** não é crime se autorizado pelo proprietário e, em bem público, pelo órgão competente.
- **Construção em área protegida:** promover construção em solo não edificável sem autorização é crime e deve ser comunicada ao órgão ambiental.
- **Lançamento de resíduos:** o lançamento em desacordo com a lei, que provoque poluição, pode configurar crime.
- **Obstar a fiscalização:** obstar ou dificultar a ação fiscalizadora do Poder Público em questões ambientais é crime.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Art. 54 (poluição) | Reclusão de 1 a 4 anos e multa; culposo: detenção de 6 meses a 1 ano |
| Art. 54, § 2º | Reclusão de 1 a 5 anos |
| Art. 55 (mineração sem licença) | Detenção de 6 meses a 1 ano e multa |
| Art. 56 (substâncias tóxicas) | Reclusão de 1 a 4 anos e multa; nuclear: +1/6 a 1/3 |
| Art. 58 | 1/6 a 1/3 (dano irreversível), 1/3 até a metade (lesão grave), até o dobro (morte) |
| Art. 60 (sem licença) | Detenção de 6 meses a 2 anos, ou multa, ou ambas; até o dobro com EIA |
| Art. 62 | Reclusão de 1 a 3 anos e multa |
| Art. 65 (pichação) | Detenção de 3 meses a 1 ano e multa; monumento tombado: 6 meses a 1 ano |
| Grafite | Não é crime se autorizado |
| Art. 69-A | Reclusão de 3 a 6 anos e multa |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 54 | Poluição: reclusão de 1 a 4 anos |
| Art. 55 | Mineração: detenção de 6 meses a 1 ano |
| Art. 56 | Tóxicos: reclusão de 1 a 4 anos |
| Art. 58 | Aumentos |
| Art. 60 | Atividade poluidora sem licença |
| Art. 61 | Disseminar pragas: reclusão de 1 a 4 anos |
| Art. 62 | Bem protegido: reclusão de 1 a 3 anos |
| Art. 64 | Solo não edificável: detenção de 6 meses a 1 ano |
| Art. 65 | Pichação: detenção de 3 meses a 1 ano |
| Art. 66 | Funcionário falso: reclusão de 1 a 3 anos |
| Art. 69 | Obstar fiscalização: detenção de 1 a 3 anos |
| Art. 69-A | Estudo falso: reclusão de 3 a 6 anos |
"""
QR=[("Questão 1","Pichar ou por outro meio conspurcar edificação ou monumento urbano tem pena de detenção de três meses a",["um ano e multa.","dois anos.","três anos.","seis meses.","cinco anos."],0,"Art. 65."),
("Questão 2","Não constitui crime a prática de grafite realizada com o objetivo de valorizar o patrimônio público ou privado mediante manifestação artística, desde que consentida pelo",["proprietário e, no bem público, autorizada pelo órgão competente.","vizinho.","guarda.","delegado.","juiz."],1,"Art. 65, § 2º."),
("Questão 3","Causar poluição que resulte ou possa resultar em danos à saúde humana tem pena de reclusão, de",["um a quatro anos, e multa.","seis meses a um ano.","um a três anos.","dois a cinco anos.","três a seis anos."],2,"Art. 54."),
("Questão 4","Obstar ou dificultar a ação fiscalizadora do Poder Público no trato de questões ambientais tem pena de detenção de um a três anos e",["multa.","reclusão.","advertência.","nada.","perdão."],3,"Art. 69.")]
t1="<strong>Muro pichado</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, flagrou jovens pichando o muro de um prédio tombado pelo patrimônio histórico do Município."
t2="<strong>Grafite autorizado</strong><br><br>Em Vila Nova, um artista pintou um grafite em uma parede de escola pública, com autorização do órgão competente e consentimento da direção."
t3="<strong>Fábrica sem licença</strong><br><br>Uma fábrica de Vila Nova passou a funcionar, sem licença ambiental, e lançou resíduos líquidos num córrego em desacordo com a lei."
tx={"amb3a":t1,"amb3b":t2,"amb3c":t3}
# n=1
q(1,"Se o crime de poluição do art. 54 é culposo, a pena é de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 54, § 1º.")
q(1,"A poluição por lançamento de resíduos sólidos, líquidos ou gasosos em desacordo com a lei tem pena de reclusão de um a",["cinco anos.","dois anos.","três anos.","quatro anos.","seis anos."],"Art. 54, § 2º, V.")
q(1,"Executar pesquisa, lavra ou extração de recursos minerais sem autorização tem pena de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 55.")
q(1,"Produzir, processar, comercializar ou transportar substância tóxica em desacordo com a lei tem pena de reclusão de um a quatro anos e",["multa.","advertência.","nada.","perdão.","detenção."],"Art. 56.")
q(1,"Se o produto ou substância for nuclear ou radioativa, a pena é aumentada de",["um sexto a um terço.","metade.","dobro.","triplo.","um quarto."],"Art. 56, § 2º.")
q(1,"Nos crimes dolosos da Seção III, a pena é aumentada até o dobro se resultar a",["morte de outrem.","lesão leve.","fuga.","multa.","apreensão."],"Art. 58, III.")
q(1,"Construir ou fazer funcionar estabelecimentos potencialmente poluidores, sem licença, tem pena de detenção de seis meses a",["dois anos, ou multa, ou ambas.","um ano.","três anos.","cinco anos.","dez anos."],"Art. 60.")
q(1,"Disseminar doença ou praga que possam causar dano à agricultura, à pecuária ou à fauna tem pena de reclusão de um a",["quatro anos, e multa.","dois anos.","três anos.","cinco anos.","seis meses."],"Art. 61.")
q(1,"Destruir, inutilizar ou deteriorar bem especialmente protegido por lei tem pena de reclusão de um a",["três anos, e multa.","dois anos.","quatro anos.","cinco anos.","seis meses."],"Art. 62.")
q(1,"Alterar o aspecto ou estrutura de edificação especialmente protegida tem pena de reclusão de um a",["três anos, e multa.","dois anos.","quatro anos.","cinco anos.","seis meses."],"Art. 63.")
q(1,"Promover construção em solo não edificável sem autorização tem pena de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 64.")
q(1,"Pichar monumento ou coisa tombada em virtude de valor artístico, arqueológico ou histórico tem pena de detenção de seis meses a",["um ano e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 65, § 1º.")
q(1,"O funcionário público que faz afirmação falsa ou omite a verdade em procedimento de licenciamento ambiental tem pena de reclusão de um a",["três anos, e multa.","dois anos.","quatro anos.","cinco anos.","seis meses."],"Art. 66.")
q(1,"Conceder dolosamente licença em desacordo com as normas ambientais tem pena de detenção de um a",["três anos, e multa.","dois anos.","quatro anos.","cinco anos.","seis meses."],"Art. 67.")
q(1,"Deixar de cumprir obrigação de relevante interesse ambiental tem pena de detenção de um a três anos e",["multa.","reclusão.","advertência.","nada.","perdão."],"Art. 68.")
q(1,"Elaborar ou apresentar estudo, laudo ou relatório ambiental falso ou enganoso tem pena de reclusão de três a",["seis anos, e multa.","dois anos.","quatro anos.","cinco anos.","dez anos."],"Art. 69-A.")
q(1,"A pena do art. 60 é aumentada até o dobro se o licenciamento for sujeito ao Estudo Prévio de Impacto",["Ambiental.","Urbano.","Social.","Econômico.","Cultural."],"Art. 60, parágrafo único.")
q(1,"No texto do muro pichado, pichar o prédio tombado tem pena de detenção de seis meses a um ano e multa, conforme o art. 65,",["§ 1º.","caput.","§ 2º.","art. 64.","art. 62."],"Art. 65, § 1º.","amb3a")
q(1,"No texto do grafite autorizado, o grafite com autorização do órgão e consentimento do proprietário",["não constitui crime.","constitui crime de pichação.","depende de multa.","é sempre crime.","é contravenção."],"Art. 65, § 2º.","amb3b")
q(1,"No texto da fábrica sem licença, o funcionamento sem licença corresponde ao art.",["60.","54.","55.","62.","65."],"Art. 60.","amb3c")
# n=2
q(2,"A poluição do art. 54 também é crime quando provoca a mortandade de animais ou a destruição significativa da",["flora.","fauna apenas.","cultura.","urbanização.","economia."],"Art. 54.")
q(2,"A poluição que dificulte ou impeça o uso público das praias tem pena de reclusão de um a",["cinco anos.","dois anos.","três anos.","quatro anos.","seis anos."],"Art. 54, § 2º, IV.")
q(2,"Incorre nas penas do art. 54, § 2º, quem deixar de adotar, quando assim o exigir a autoridade competente, medidas de precaução em caso de risco de dano ambiental grave ou",["irreversível.","leve.","eventual.","moderado.","reversível."],"Art. 54, § 3º.")
q(2,"Nas penas do art. 55 incorre quem deixa de recuperar a área pesquisada ou explorada, nos termos da autorização, permissão, licença ou determinação do órgão",["competente.","vizinho.","privado.","local.","religioso."],"Art. 55, parágrafo único.")
q(2,"Incorre nas penas do art. 56 quem abandona os produtos ou substâncias tóxicas ou os utiliza em desacordo com as normas ambientais ou de",["segurança.","moda.","preço.","embalagem.","venda."],"Art. 56, § 1º, I.")
q(2,"Se o crime do art. 56 é culposo, a pena é de detenção de seis meses a",["um ano, e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 56, § 3º.")
q(2,"Nos crimes dolosos da Seção III, a pena é aumentada de um sexto a um terço se resulta dano irreversível à flora ou ao meio",["ambiente em geral.","urbano.","cultural.","econômico.","social."],"Art. 58, I.")
q(2,"A pena é aumentada de um terço até a metade nos crimes dolosos da Seção III se resulta lesão corporal de natureza",["grave em outrem.","leve.","média.","qualquer.","nenhuma."],"Art. 58, II.")
q(2,"As penalidades do art. 58 somente serão aplicadas se do fato não resultar crime",["mais grave.","menos grave.","culposo.","doloso.","tentado."],"Art. 58, parágrafo único.")
q(2,"Se o crime do art. 62 for culposo, a pena é de detenção de seis meses a um ano, sem prejuízo da",["multa.","reclusão.","advertência.","prisão.","perda do cargo."],"Art. 62, parágrafo único.")
q(2,"A alteração do aspecto de local protegido, no art. 63, ocorre em razão de seu valor paisagístico, ecológico, turístico, artístico, histórico, cultural, religioso, arqueológico, etnográfico ou",["monumental.","comercial.","econômico.","político.","social."],"Art. 63.")
q(2,"A construção em solo não edificável do art. 64 também alcança o seu",["entorno.","interior.","subsolo.","espaço aéreo.","horizonte."],"Art. 64.")
q(2,"Na pichação em monumento ou coisa tombada, a pena é de seis meses a um ano de detenção e",["multa.","reclusão.","advertência.","perdão.","prisão perpétua."],"Art. 65, § 1º.")
q(2,"Se o crime do art. 68 é culposo, a pena é de três meses a um ano, sem prejuízo da",["multa.","reclusão.","advertência.","prisão.","perda do cargo."],"Art. 68, parágrafo único.")
q(2,"Obstar a ação fiscalizadora do Poder Público no trato de questões ambientais tem pena de detenção de um a",["três anos, e multa.","dois anos.","quatro anos.","cinco anos.","seis meses."],"Art. 69.")
q(2,"O crime do art. 69-A, se culposo, tem pena de detenção de um a",["três anos.","dois anos.","quatro anos.","seis meses.","cinco anos."],"Art. 69-A, § 1º.")
q(2,"A pena do art. 69-A é aumentada de um terço a dois terços se há dano significativo ao meio ambiente em decorrência do uso da informação",["falsa, incompleta ou enganosa.","verdadeira.","pública.","oficial.","antiga."],"Art. 69-A, § 2º.")
q(2,"No texto do muro pichado, os jovens poderiam ser enquadrados no art. 65, que trata de",["conspurcar edificação ou monumento urbano.","poluição.","mineração.","incêndio.","caça."],"Art. 65.","amb3a")
q(2,"No texto do grafite autorizado, a autorização é do órgão competente porque se trata de",["bem público.","bem particular, apenas.","bem estrangeiro.","bem móvel.","imóvel rural."],"Art. 65, § 2º.","amb3b")
q(2,"No texto da fábrica sem licença, o lançamento de resíduos líquidos em desacordo com a lei também pode configurar o art.",["54, § 2º, V.","55.","62.","64.","65."],"Art. 54, § 2º, V.","amb3c")
# n=3
q(3,"Assinale a alternativa correta sobre pichação e grafite.",["Pichar edificação é crime; o grafite artístico, consentido pelo proprietário e autorizado pelo órgão competente, quando público, não é crime.","O grafite é sempre crime.","A pichação não é crime.","A pichação em monumento tombado tem pena menor.","O grafite em bem público dispensa autorização."],"Art. 65.")
q(3,"Considere. I. A poluição do art. 54 tem reclusão de 1 a 4 anos. II. Soltar balão é crime do art. 65. III. O art. 69-A tem reclusão de 3 a 6 anos. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Soltar balão é do art. 42; o art. 65 trata da pichação.")
q(3,"Assinale a INCORRETA.",["O art. 58 aumenta a pena nos crimes culposos desta seção.","O art. 58 aumenta a pena nos crimes dolosos desta seção.","As penalidades do art. 58 só se aplicam se não resultar crime mais grave.","A morte de outrem aumenta até o dobro.","O dano irreversível aumenta de 1/6 a 1/3."],"O art. 58 trata dos crimes dolosos (art. 58, caput).")
q(3,"A pena do art. 54, § 2º, é de reclusão de um a cinco anos, e o dispositivo se aplica a quem tornar área urbana ou rural imprópria para a",["ocupação humana.","agricultura.","indústria.","pesca.","caça."],"Art. 54, § 2º, I.")
q(3,"No art. 54, § 2º, a poluição atmosférica que provoque a retirada, ainda que momentânea, dos habitantes das áreas afetadas, está no inciso",["II.","I.","III.","IV.","V."],"Art. 54, § 2º, II.")
q(3,"A poluição hídrica que torne necessária a interrupção do abastecimento público de água de uma comunidade está no inciso III do",["§ 2º do art. 54.","art. 55.","art. 56.","art. 60.","art. 62."],"Art. 54, § 2º, III.")
q(3,"Nas mesmas penas do art. 56 incorre quem manipula, acondiciona, armazena, coleta, transporta, reutiliza, recicla ou dá destinação final a resíduos perigosos de forma diversa da estabelecida em lei ou",["regulamento.","contrato.","costume.","tradição.","sentença."],"Art. 56, § 1º, II.")
q(3,"A pena do art. 56 é aumentada de um sexto a um terço se o produto for nuclear ou",["radioativo.","explosivo.","inflamável.","comum.","orgânico."],"Art. 56, § 2º.")
q(3,"O art. 62 trata de bem protegido, arquivo, registro, museu, biblioteca, pinacoteca ou instalação científica protegida por lei, ato administrativo ou decisão",["judicial.","fiscal.","comercial.","familiar.","religiosa."],"Art. 62, II.")
q(3,"Entre os crimes contra a administração ambiental está o do funcionário que concede licença que sabe estar em desacordo com as normas ambientais, que exige conduta",["dolosa.","culposa.","omissiva apenas.","imprudente.","negligente."],"Art. 67.")
q(3,"A pena do art. 66, para o funcionário público que sonega informações ou dados técnico-científicos, é de reclusão de",["um a três anos, e multa.","seis meses a um ano.","dois a cinco anos.","três a seis anos.","um mês."],"Art. 66.")
q(3,"O art. 69-A abrange o estudo, laudo ou relatório ambiental total ou parcialmente falso ou enganoso, inclusive por",["omissão.","ação, apenas.","contrato.","tradição.","costume."],"Art. 69-A.")
q(3,"No texto do muro pichado, a pichação em monumento tombado tem pena maior que a do caput, pois o § 1º prevê detenção de seis meses a um ano, enquanto o caput prevê",["três meses a um ano.","um ano a dois anos.","dois a quatro anos.","seis meses a dois anos.","um a três anos."],"Art. 65.","amb3a")
q(3,"No texto do muro pichado, além do art. 65, a conduta de alterar a estrutura do prédio tombado poderia configurar o art.",["63.","54.","55.","60.","69."],"Art. 63.","amb3a")
q(3,"No texto do grafite autorizado, o grafite só deixa de ser crime se observadas as posturas municipais e as normas dos órgãos de preservação do patrimônio",["histórico e artístico nacional.","privado.","econômico.","fiscal.","militar."],"Art. 65, § 2º.","amb3b")
q(3,"No texto do grafite autorizado, a autorização expressa do órgão competente é exigida porque o bem é",["público.","privado.","estrangeiro.","móvel.","inexistente."],"Art. 65, § 2º.","amb3b")
q(3,"No texto da fábrica sem licença, a pena do art. 60 é de detenção de seis meses a dois anos, ou multa, ou",["ambas as penas cumulativamente.","reclusão.","advertência.","nada.","perdão."],"Art. 60.","amb3c")
q(3,"No texto da fábrica sem licença, a pena do art. 60 aumenta até o dobro se o licenciamento exigir",["Estudo Prévio de Impacto Ambiental.","aprovação do vizinho.","parecer do guarda.","ordem judicial.","vistoria policial."],"Art. 60, parágrafo único.","amb3c")
q(3,"A pena do art. 67, para o funcionário público que concede licença em desacordo com as normas ambientais, é de detenção de um a",["três anos, e multa.","seis meses.","cinco anos.","dois anos.","dez anos."],"Art. 67.")
q(3,"No art. 54, § 2º, constitui hipótese de reclusão de um a cinco anos dificultar ou impedir o uso público das",["praias.","praças.","estradas.","escolas.","ruas."],"Art. 54, § 2º, IV.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes ambientais: poluição, patrimônio e administração (arts. 54 a 69-A)",[
 ("pol","Poluição",["reclusão 1 a 4 anos","§ 2º: 1 a 5 anos","culposo: detenção"],"seção 1"),
 ("min","Mineração e tóxicos",["detenção 6m a 1a","tóxicos: reclusão 1 a 4","aumentos do art. 58"],"seção 1"),
 ("lic","Atividade sem licença",["art. 60","detenção 6m a 2a","EIA: até o dobro"],"seção 2"),
 ("pat","Patrimônio",["art. 62: reclusão 1 a 3","solo não edificável","art. 63"],"seção 3"),
 ("pic","Pichação e grafite",["art. 65","tombado: 6m a 1a","grafite autorizado"],"seção 3"),
 ("adm","Administração ambiental",["falsidade: 1 a 3 anos","obstar: 1 a 3 anos","69-A: 3 a 6 anos"],"seção 3")],
 "Na prova: penas e a exceção do grafite")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a poluição e as substâncias tóxicas; as demais, as atividades sem licença, o patrimônio, a pichação e a administração ambiental.","Fontes: Edital 02/2026, Anexo I; Lei 9.605/1998 (Lei de Crimes Ambientais), arts. 54 a 69-A, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("amb-3","Crimes ambientais: poluição, patrimônio e administração ambiental (arts. 54 a 69-A)",Q,list(tx),
 cobertura=["Cobertos: arts. 54 a 56, 58, 60 a 69-A. Os arts. 57 e 59 foram vetados e omitidos."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Trechos de lei copiados de fontes/amb.txt por programa.","Casos amb3a, amb3b e amb3c fictícios."],
 fontes_conferidas=["Lei 9.605/1998, arts. 54 a 69-A: texto da Câmara, copiado por programa."])
gravar("amb-3",aula_html,banco("amb-3",Q),tx)
