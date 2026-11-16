import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='susp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Este posto trata de quem integra o Susp e como ele funciona (arts. 9º a 37): os integrantes estratégicos e operacionais, as formas de integração, os Conselhos de Segurança Pública, o Plano Nacional, o Sinaped e o Sinesp. Para a Guarda Municipal, o ponto central é o art. 9º, § 2º, VII: as guardas municipais são integrantes operacionais do Susp. A Vunesp cobra a lista de integrantes, a duração do Plano (dez anos), o prazo para os planos locais (dois anos), a composição dos Conselhos e o mandato de dois anos."
S={}
S[1]="## 1. Composição do Susp\n\n"+L("art. 9º, caput","Art. 9º É instituído o Sistema Único","§ 1º São integrantes estratégicos")+"\n\n"+L("art. 9º, § 1º","§ 1º São integrantes estratégicos","§ 2º São integrantes operacionais")+"\n\n"+L("art. 9º, § 2º, I e II","§ 2º São integrantes operacionais","III - (VETADO)")+"\n\n"+L("art. 9º, § 2º, IV a VIII","IV - polícias civis","IX - (VETADO)")+"\n\n"+L("art. 9º, § 2º, X a XVI","X - institutos oficiais","XVII - polícia legislativa")+"\n\n"+L("art. 9º, § 4º","§ 4º Os sistemas estaduais","Seção II")+"""

O Susp é integrado pelos órgãos do art. 144 da Constituição, pelos agentes penitenciários, pelas guardas municipais e pelos demais integrantes estratégicos e operacionais, que atuam nos limites de suas competências, de forma cooperativa, sistêmica e harmônica. São integrantes estratégicos a União, os Estados, o Distrito Federal e os Municípios, por intermédio dos Executivos, e os Conselhos de Segurança Pública e Defesa Social. São integrantes operacionais, entre outros: a polícia federal; a polícia rodoviária federal; as polícias civis; as polícias militares; os corpos de bombeiros militares; as guardas municipais; os órgãos do sistema penitenciário; os institutos oficiais de criminalística, medicina legal e identificação; a Senasp; as secretarias estaduais de segurança; a Sedec; a Senad; os agentes de trânsito; e a guarda portuária. Os sistemas estaduais, distrital e municipais implementam seus programas, com liberdade de organização e funcionamento.
"""
S[2]="## 2. Funcionamento e integração\n\n"+L("art. 10, caput e incisos","Art. 10. A integração e a coordenação","§ 1º O Susp será coordenado")+"\n\n"+L("arts. 15 e 16","Art. 15. A União poderá apoiar","Art. 17.")+"""

A integração e a coordenação dos órgãos do Susp, nos limites de suas competências, dão-se por operações com planejamento e execução integrados; estratégias comuns de prevenção e controle de infrações penais; aceitação mútua de registro de ocorrência policial; compartilhamento de informações, inclusive com o Sisbin; intercâmbio de conhecimentos técnicos e científicos; e integração das informações e dos dados por meio do Sinesp. As operações combinadas podem ser ostensivas, investigativas, de inteligência ou mistas. A União pode apoiar Estados, Distrito Federal e Municípios que não tenham condições de implementar o Susp. Os órgãos do Susp podem atuar em vias urbanas, rodovias, terminais, ferrovias, hidrovias, portos e aeroportos, no âmbito de suas competências, em integração com o órgão cuja circunscrição esteja o local de atuação.
"""
S[3]="## 3. Conselhos de Segurança Pública e Defesa Social\n\n"+L("arts. 19 e 20, caput","Art. 19. A estrutura formal","§ 1º O Conselho Nacional")+"\n\n"+L("art. 20, § 2º","§ 2º Os Conselhos de Segurança Pública e Defesa Social congregarão","§ 3º Os Conselhos")+"\n\n"+L("art. 21, caput e incisos","Art. 21. Os Conselhos serão compostos por","§ 1º Os representantes")+"\n\n"+L("art. 21, §§ 2º e 3º","§ 2º Cada conselheiro terá","§ 4º Na ausência")+"""

A estrutura formal do Susp se dá pela formação de Conselhos permanentes. Os Conselhos de Segurança Pública e Defesa Social são criados no âmbito da União, dos Estados, do Distrito Federal e dos Municípios, mediante proposta dos chefes dos Poderes Executivos, encaminhada aos Legislativos. Têm natureza de colegiado, com competência consultiva, sugestiva e de acompanhamento social das atividades de segurança pública e defesa social. São compostos por representantes de cada órgão integrante do Susp, do Poder Judiciário, do Ministério Público, da OAB, da Defensoria Pública, de entidades da sociedade ligadas às políticas de segurança e de entidades de profissionais de segurança pública. Cada conselheiro tem um suplente, e os mandatos e designações duram dois anos, permitida apenas uma recondução ou reeleição.
"""
S[4]="## 4. Plano Nacional, controle e Sinesp\n\n"+L("art. 22, caput e incisos","Art. 22. A União instituirá","§ 1º As políticas públicas de segurança não se restringem")+"\n\n"+L("art. 22, § 2º","§ 2º O Plano de que trata","§ 3º As ações de prevenção")+"\n\n"+L("art. 22, § 5º","§ 5º Os Estados, o Distrito Federal e os Municípios deverão","§ 6º O poder público")+"\n\n"+L("art. 34","Art. 34. A União, os Estados","Art. 35.")+"\n\n"+L("art. 35, caput e incisos I a V","Art. 35. É instituído o Sistema Nacional de Informações","VI - enfrentamento da violência doméstica")+"""

A União institui o Plano Nacional de Segurança Pública e Defesa Social, com duração de dez anos a contar de sua publicação, para articular as ações do poder público, melhorar a gestão das políticas, contribuir para a organização dos Conselhos, assegurar a produção de conhecimento e priorizar ações preventivas e fiscalizatórias nas divisas, fronteiras, portos e aeroportos. Estados, Distrito Federal e Municípios devem, com base no Plano Nacional, elaborar seus planos em até dois anos, sob pena de não receberem recursos da União. As ações de prevenção à criminalidade são prioritárias.

A União, os Estados, o DF e os Municípios devem instituir órgãos de ouvidoria dotados de autonomia e independência, com competência para receber e tratar representações, elogios e sugestões sobre as ações dos profissionais do Susp. O Sinesp armazena, trata e integra dados para auxiliar as políticas de segurança pública, sistema prisional e execução penal, rastreabilidade de armas e munições, banco de perfil genético e digitais e enfrentamento do tráfico de drogas.
"""
S[5]="""## 5. Na rotina do guarda

- **Integrante operacional:** a Guarda Municipal integra o Susp como integrante operacional, atuando nos limites de suas competências, de forma cooperativa.
- **Registro de ocorrência:** o registro lavrado é aceito por todos os integrantes do sistema, em aceitação mútua.
- **Operações integradas:** as operações podem ser ostensivas, investigativas, de inteligência ou mistas, planejadas conjuntamente.
- **Conselhos:** o Conselho Municipal de Segurança Pública e Defesa Social acompanha as instituições e pode recomendar providências.
- **Ouvidoria:** o cidadão pode registrar representações, elogios e sugestões sobre a atuação do guarda na ouvidoria, que deve ter autonomia e independência.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Guardas municipais | Integrantes operacionais (art. 9º, § 2º, VII) |
| Conselhos de Segurança | Integrantes estratégicos |
| Integrantes estratégicos | Entes por intermédio dos Executivos e os Conselhos |
| Formas de integração | Operações integradas, estratégias comuns, aceitação mútua de registro, compartilhamento, intercâmbio, Sinesp |
| Atuação em vias, portos e aeroportos | Dentro das competências, em integração com o órgão da circunscrição |
| Natureza dos Conselhos | Colegiado de competência consultiva, sugestiva e de acompanhamento social |
| Mandato dos conselheiros | Dois anos, uma recondução |
| Duração do Plano Nacional | Dez anos |
| Planos locais | Em até dois anos, sob pena de perder recursos da União |
| Ouvidoria | Autonomia e independência |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 9º | Composição: estratégicos e operacionais; guardas municipais |
| Art. 10 | Seis formas de integração |
| Art. 15 | A União pode apoiar entes sem condições |
| Art. 16 | Atuação em vias, portos e aeroportos |
| Art. 20 | Conselhos: colegiado consultivo |
| Art. 21 | Composição; mandato de 2 anos |
| Art. 22 | Plano Nacional: 10 anos; planos locais em 2 anos |
| Art. 34 | Ouvidorias autônomas |
| Art. 35 | Sinesp |
"""
QR=[("Questão 1","São integrantes operacionais do Susp, entre outros, as polícias civis, as polícias militares, os corpos de bombeiros militares e as",["guardas municipais.","empresas de segurança privada.","associações de moradores.","agências de turismo.","escolas."],0,"Art. 9º, § 2º, VII."),
("Questão 2","O Plano Nacional de Segurança Pública e Defesa Social terá duração de",["dez anos a contar de sua publicação.","cinco anos.","dois anos.","quinze anos.","vinte anos."],1,"Art. 22, § 2º."),
("Questão 3","Os mandatos dos membros dos Conselhos terão duração de dois anos, permitida apenas uma",["recondução ou reeleição.","prorrogação automática.","substituição por sorteio.","renúncia imediata.","delegação."],2,"Art. 21, § 3º."),
("Questão 4","A União, os Estados, o Distrito Federal e os Municípios deverão instituir órgãos de ouvidoria dotados de autonomia e",["independência no exercício de suas atribuições.","subordinação total.","sigilo absoluto.","poder de polícia.","poder de julgar."],3,"Art. 34.")]
t1="<strong>Operação integrada</strong><br><br>Uma operação de Vila Nova, cidade fictícia, reuniu a polícia militar, a guarda municipal e os agentes de trânsito, com planejamento conjunto, para combater furtos no centro."
t2="<strong>Plano municipal</strong><br><br>O Plano Nacional de Segurança Pública foi publicado, e o Município de Vila Nova ainda não elaborou seu plano, passados três anos."
t3="<strong>Reclamação contra um guarda</strong><br><br>Um morador de Vila Nova quis registrar uma reclamação sobre a abordagem de um guarda e procurou a ouvidoria do Município."
tx={"susp2a":t1,"susp2b":t2,"susp2c":t3}
# n=1
q(1,"O Susp tem como integrantes os órgãos do art. 144 da Constituição, os agentes penitenciários e as",["guardas municipais.","empresas privadas.","associações.","universidades.","igrejas."],"Art. 9º.")
q(1,"Os integrantes do Susp atuam nos limites de suas competências, de forma cooperativa, sistêmica e",["harmônica.","isolada.","eventual.","facultativa.","competitiva."],"Art. 9º.")
q(1,"São integrantes estratégicos do Susp a União, os Estados, o Distrito Federal e os Municípios, por intermédio dos respectivos Poderes",["Executivos.","Legislativos.","Judiciários.","Moderadores.","Constituintes."],"Art. 9º, § 1º, I.")
q(1,"São integrantes estratégicos do Susp os Conselhos de Segurança Pública e Defesa Social dos três entes",["federados.","privados.","religiosos.","partidários.","militares."],"Art. 9º, § 1º, II.")
q(1,"É integrante operacional do Susp a polícia",["rodoviária federal.","legislativa municipal apenas.","particular.","penal civil.","científica privada."],"Art. 9º, § 2º, II.")
q(1,"São integrantes operacionais os corpos de bombeiros",["militares.","civis.","privados.","voluntários.","municipais apenas."],"Art. 9º, § 2º, VI.")
q(1,"São integrantes operacionais os agentes de",["trânsito.","imprensa.","turismo.","comércio.","câmbio."],"Art. 9º, § 2º, XV.")
q(1,"É integrante operacional do Susp a guarda",["portuária.","privada.","florestal.","escolar.","comunitária."],"Art. 9º, § 2º, XVI.")
q(1,"Os sistemas estaduais, distrital e municipais têm liberdade de organização e",["funcionamento.","tributação.","legislação penal.","orçamento da União.","jurisdição."],"Art. 9º, § 4º.")
q(1,"A integração dos órgãos do Susp dá-se por meio, entre outros, de operações com planejamento e execução",["integrados.","isolados.","privados.","sigilosos.","eventuais."],"Art. 10, I.")
q(1,"Entre as formas de integração está a aceitação mútua de registro de ocorrência",["policial.","civil.","tributária.","eleitoral.","trabalhista."],"Art. 10, III.")
q(1,"A integração das informações e dos dados de segurança pública dá-se por meio do",["Sinesp.","Sinaped.","Sievap.","Pró-Vida.","Renaesp."],"Art. 10, VI.")
q(1,"A União poderá apoiar os entes que não dispuserem de condições técnicas e operacionais para implementar o",["Susp.","trânsito.","imposto.","tribunal.","consórcio."],"Art. 15.")
q(1,"Os Conselhos de Segurança Pública e Defesa Social serão criados mediante proposta dos chefes dos Poderes",["Executivos.","Judiciários.","Legislativos.","Moderadores.","Constituintes."],"Art. 20.")
q(1,"Os Conselhos têm natureza de",["colegiado.","empresa.","autarquia.","fundação.","sindicato."],"Art. 20, § 2º.")
q(1,"O Plano Nacional de Segurança Pública e Defesa Social é instituído pela",["União.","Prefeitura.","Câmara de Vereadores.","Assembleia.","OAB."],"Art. 22.")
q(1,"As ações de prevenção à criminalidade são",["prioritárias na elaboração do Plano Nacional.","secundárias.","eventuais.","opcionais.","proibidas."],"Art. 22, § 3º.")
q(1,"No texto da operação integrada, a reunião de polícia militar, guarda municipal e agentes de trânsito mostra integrantes",["operacionais do Susp.","apenas estratégicos.","apenas privados.","apenas federais.","apenas judiciais."],"Art. 9º, § 2º.","susp2a")
q(1,"No texto do plano municipal, o Município deveria ter elaborado seu plano em até",["dois anos da publicação do documento nacional.","um ano.","cinco anos.","dez anos.","três meses."],"Art. 22, § 5º.","susp2b")
q(1,"No texto da reclamação contra um guarda, o órgão que recebe representações, elogios e sugestões é a",["ouvidoria.","câmara.","promotoria.","delegacia.","prefeitura, apenas."],"Art. 34, parágrafo único.","susp2c")
# n=2
q(2,"São integrantes operacionais do Susp os institutos oficiais de criminalística, medicina legal e",["identificação.","pesquisa.","educação.","imprensa.","turismo."],"Art. 9º, § 2º, X.")
q(2,"A Senasp é a Secretaria Nacional de Segurança",["Pública.","Privada.","Penal.","Comunitária.","Municipal."],"Art. 9º, § 2º, XI.")
q(2,"A Sedec é a Secretaria Nacional de Proteção e",["Defesa Civil.","Segurança.","Educação.","Saúde.","Política."],"Art. 9º, § 2º, XIII.")
q(2,"A Senad é a Secretaria Nacional de Política sobre",["Drogas.","Armas.","Trânsito.","Segurança.","Crimes."],"Art. 9º, § 2º, XIV.")
q(2,"As operações combinadas podem ser ostensivas, investigativas, de inteligência ou",["mistas.","isoladas.","privadas.","eventuais.","paralelas."],"Art. 10, § 2º.")
q(2,"O compartilhamento de informações será feito preferencialmente por meio",["eletrônico, com acesso recíproco aos bancos de dados.","impresso.","verbal.","por carta.","por jornal."],"Art. 10, § 4º.")
q(2,"Os órgãos do Susp podem atuar em vias urbanas, rodovias, ferrovias, hidrovias, portos e aeroportos, em efetiva integração com o órgão cujo local esteja sob sua",["circunscrição.","vontade.","propriedade.","tutela.","guarda."],"Art. 16.")
q(2,"A estrutura formal do Susp se dá pela formação de Conselhos",["permanentes.","eventuais.","temporários.","privados.","itinerantes."],"Art. 19.")
q(2,"Os Conselhos têm competência consultiva, sugestiva e de acompanhamento social das atividades de segurança pública e defesa",["social.","privada.","militar.","judicial.","penal."],"Art. 20, § 2º.")
q(2,"Os Conselhos Estaduais, Distrital e Municipais contarão com representantes da sociedade civil organizada e de representantes dos",["trabalhadores.","empresários.","partidos.","militares.","juízes."],"Art. 20, § 7º.")
q(2,"A composição do Conselho inclui representante da Ordem dos Advogados do Brasil e da",["Defensoria Pública.","Receita Federal.","Polícia Federal.","Câmara.","imprensa."],"Art. 21, IV e V.")
q(2,"Cada conselheiro terá um",["suplente, que o substituirá em sua ausência.","assessor.","advogado.","vice-presidente.","fiscal."],"Art. 21, § 2º.")
q(2,"O Plano Nacional terá, entre as finalidades, priorizar ações preventivas e fiscalizatórias de segurança interna nas divisas, fronteiras, portos e",["aeroportos.","escolas.","praças.","hospitais.","clubes."],"Art. 22, IV.")
q(2,"Estados, Distrito Federal e Municípios que não elaborarem seus planos em dois anos não poderão receber recursos da",["União.","iniciativa privada.","OAB.","imprensa.","igreja."],"Art. 22, § 5º.")
q(2,"O poder público deverá dar ampla divulgação ao conteúdo das Políticas e dos",["Planos de segurança pública.","processos disciplinares.","inquéritos.","orçamentos secretos.","dados pessoais."],"Art. 22, § 6º.")
q(2,"À ouvidoria competirá receber e tratar representações, elogios e",["sugestões.","multas.","prisões.","recursos.","impostos."],"Art. 34, parágrafo único.")
q(2,"O Sinesp auxilia na formulação de políticas, entre outras, sobre rastreabilidade de armas e",["munições.","veículos.","imóveis.","empresas.","escolas."],"Art. 35, III.")
q(2,"No texto da operação integrada, a participação dos agentes de trânsito decorre do art. 9º, § 2º, inciso",["XV.","VII.","VI.","II.","XVI."],"Art. 9º, § 2º, XV.","susp2a")
q(2,"No texto do plano municipal, a sanção para o Município que não elabora o plano é a perda de",["recursos da União para segurança pública.","autonomia política.","mandato do prefeito.","competência tributária.","território."],"Art. 22, § 5º.","susp2b")
q(2,"No texto da reclamação contra um guarda, a ouvidoria deve encaminhar a representação ao órgão com atribuição para as",["providências legais e a resposta ao requerente.","punições automáticas.","prisões.","arquivamento.","publicação em jornal."],"Art. 34, parágrafo único.","susp2c")
# n=3
q(3,"Assinale a alternativa correta sobre os integrantes do Susp.",["Os Conselhos de Segurança são integrantes estratégicos; as guardas municipais, agentes de trânsito e guardas portuárias são integrantes operacionais.","As guardas municipais são integrantes estratégicos.","Os Conselhos são integrantes operacionais.","As polícias civis são integrantes estratégicos.","Os agentes de trânsito não integram o Susp."],"Art. 9º.")
q(3,"Considere. I. O Plano Nacional tem duração de 10 anos. II. Os planos locais devem ser feitos em até 2 anos. III. Os Conselhos têm mandato de 5 anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O mandato é de 2 anos (art. 21, § 3º).")
q(3,"Assinale a INCORRETA.",["Os Conselhos têm competência deliberativa e punitiva.","Os Conselhos têm natureza de colegiado.","Os Conselhos acompanham as instituições do art. 9º, § 2º.","Os Conselhos podem recomendar providências legais.","Os Conselhos propõem diretrizes para as políticas públicas."],"A competência é consultiva, sugestiva e de acompanhamento social (art. 20, § 2º).")
q(3,"Os Conselhos de Segurança Pública exercem o acompanhamento das instituições do art. 9º, § 2º, e podem recomendar providências legais às autoridades",["competentes.","privadas.","partidárias.","estrangeiras.","militares."],"Art. 20, § 3º.")
q(3,"O acompanhamento dos Conselhos considera as condições de trabalho, a valorização e o respeito pela integridade física e moral dos",["integrantes das instituições.","cidadãos.","presos.","vizinhos.","empresários."],"Art. 20, § 4º, I.")
q(3,"Os representantes das entidades da sociedade e dos profissionais, nos Conselhos, serão eleitos por processo aberto a todas as entidades, conforme convocação",["pública e critérios objetivos previamente definidos.","privada.","sigilosa.","por sorteio.","por indicação do prefeito."],"Art. 21, § 1º.")
q(3,"Os mandatos dos membros dos incisos VI e VII do art. 21 e a designação dos demais membros têm a duração de",["dois anos, com uma recondução ou reeleição.","quatro anos.","um ano, sem recondução.","três anos, com duas reconduções.","cinco anos."],"Art. 21, § 3º.")
q(3,"A avaliação anual do Plano Nacional é feita pela União, em articulação com os Estados, o Distrito Federal e os",["Municípios.","clubes.","sindicatos.","bancos.","partidos."],"Art. 23.")
q(3,"Os agentes públicos devem adotar estratégias de articulação entre órgãos públicos, entidades privadas, corporações policiais e organismos",["internacionais.","partidários.","religiosos.","esportivos.","comerciais."],"Art. 24, I.")
q(3,"As políticas públicas de segurança não se restringem aos integrantes do Susp, pois devem considerar um contexto social amplo, com abrangência de outras áreas, como educação, saúde, lazer e",["cultura.","tributos.","indústria.","pesca.","mineração."],"Art. 22, § 1º.")
q(3,"Os integrantes do Susp fixarão, anualmente, metas de excelência no âmbito de suas competências, visando à prevenção e repressão de infrações penais e administrativas e à prevenção de",["desastres.","impostos.","greves.","eleições.","feriados."],"Art. 25.")
q(3,"O Sinaped é instituído no âmbito do Susp com o objetivo, entre outros, de contribuir para organização e integração dos",["membros do Susp.","tribunais.","partidos.","bancos.","clubes."],"Art. 26, I.")
q(3,"Os órgãos de correição, dotados de autonomia, cabem o gerenciamento dos processos de apuração de responsabilidade funcional, por sindicância e processo administrativo",["disciplinar.","civil.","fiscal.","eleitoral.","tributário."],"Art. 33.")
q(3,"O Sinesp tem a finalidade de armazenar, tratar e integrar dados e informações, entre outras, sobre sistema prisional e execução",["penal.","civil.","fiscal.","trabalhista.","eleitoral."],"Art. 35, II.")
q(3,"No texto da operação integrada, a participação da guarda municipal em operação com a polícia militar é compatível com o art. 10, que prevê",["operações com planejamento e execução integrados.","atuação isolada.","competição entre órgãos.","sigilo entre órgãos.","separação de bancos de dados."],"Art. 10, I.","susp2a")
q(3,"No texto da operação integrada, o planejamento e a coordenação das operações combinadas são exercidos",["conjuntamente pelos participantes.","apenas pela polícia militar.","apenas pelo Município.","apenas pela União.","pelos agentes de trânsito apenas."],"Art. 10, § 3º.","susp2a")
q(3,"No texto do plano municipal, o prazo de dois anos conta-se da publicação do documento",["nacional.","estadual.","municipal.","privado.","judicial."],"Art. 22, § 5º.","susp2b")
q(3,"No texto do plano municipal, a sanção do art. 22, § 5º, é aplicável aos entes que não elaborarem seus planos",["com base no Plano Nacional, em até dois anos.","apenas em cinco anos.","somente se a União pedir.","somente se o Estado pedir.","depois de dez anos."],"Art. 22, § 5º.","susp2b")
q(3,"No texto da reclamação contra um guarda, a ouvidoria deve ter autonomia e",["independência.","subordinação.","sigilo.","poder de punir.","poder de julgar."],"Art. 34.","susp2c")
q(3,"No texto da reclamação contra um guarda, a ouvidoria deve ser instituída pela União, pelos Estados, pelo DF e pelos",["Municípios.","clubes.","sindicatos.","bancos.","partidos."],"Art. 34.","susp2c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Susp: composição e funcionamento (arts. 9º a 37)",[
 ("est","Integrantes estratégicos",["entes federados (Executivos)","Conselhos"],"seção 1"),
 ("ope","Integrantes operacionais",["polícias, bombeiros","guardas municipais","agentes de trânsito, guarda portuária"],"seção 1"),
 ("int","Integração",["operações integradas","registro aceito mutuamente","Sinesp"],"seção 2"),
 ("con","Conselhos",["colegiado consultivo","composição plural","mandato de 2 anos"],"seção 3"),
 ("pla","Plano Nacional",["10 anos","planos locais em 2 anos","prevenção prioritária"],"seção 4"),
 ("ouv","Ouvidoria e Sinesp",["autonomia e independência","dados integrados","armas, genético, drogas"],"seção 4")],
 "Na prova: guardas municipais são integrantes operacionais; prazos de 10 anos, 2 anos")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',5,6,7],QR,5,svg,"A primeira linha traz a composição do Susp; as demais, o funcionamento, os Conselhos, o Plano e o Sinesp.","Fontes: Edital 02/2026, Anexo I; Lei 13.675/2018 (Susp), arts. 9º a 37, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("susp-2","Susp: composição e funcionamento (arts. 9º a 37)",Q,list(tx),
 cobertura=["Cobertos os arts. 9º a 10, 15, 16, 19 a 23, 34 e 35. Não detalhados: arts. 11 a 14, 17, 18, 24 a 33, 36 e 37."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","A consolidação ainda cita o 'Ministério Extraordinário da Segurança Pública' como órgão central; conferir a redação atual e o órgão atual no Planalto.","O art. 9º, § 2º, XVII (polícia legislativa) aparece vetado na consolidação; foi omitido.","Trechos de lei copiados de fontes/susp.txt por programa.","Casos susp2a, susp2b e susp2c fictícios."],
 fontes_conferidas=["Lei 13.675/2018, arts. 9º a 37: texto da Câmara, copiado por programa."])
gravar("susp-2",aula_html,banco("susp-2",Q),tx)
