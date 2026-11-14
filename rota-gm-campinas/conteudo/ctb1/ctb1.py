import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Código de Trânsito Brasileiro começa dizendo o que é trânsito, quais vias o Código alcança e quem integra o Sistema Nacional de Trânsito. A Vunesp cobra os arts. 1º a 25 pela definição de trânsito e de via, pelos órgãos que compõem o sistema, pelas competências do Contran, dos Cetran e das JARI e, principalmente, pelas competências dos órgãos municipais de trânsito, que são os mais próximos do trabalho da Guarda Municipal. A aula segue o texto consolidado, com a lei citada e a explicação logo abaixo."
S={}
S[1]="## 1. O trânsito, as vias e o Sistema Nacional de Trânsito\n\n"+L("art. 1º, caput e § 1º","Art. 1º O trânsito de qualquer natureza","§ 2º O trânsito, em condições seguras")+"\n\n"+L("art. 1º, §§ 2º e 3º","§ 2º O trânsito, em condições seguras","§ 4º (VETADO)")+"\n\n"+L("art. 1º, § 5º","§ 5º Os órgãos e entidades de trânsito","Art. 2º")+"""

Trânsito é a utilização das vias por pessoas, veículos e animais, isolados ou em grupos, conduzidos ou não, para fins de circulação, parada, estacionamento e operação de carga ou descarga. Note que o conceito inclui o pedestre e o animal, e inclui a parada e o estacionamento, e não só o movimento. O trânsito em condições seguras é direito de todos e dever dos órgãos do Sistema Nacional de Trânsito, que respondem objetivamente, no âmbito de suas competências, por danos causados por ação, omissão ou erro na execução de programas, projetos e serviços. E a prioridade do sistema é a defesa da vida, nela incluída a preservação da saúde e do meio ambiente.

"""+L("art. 2º","Art. 2º São vias terrestres","Art. 3º")+"""

As vias são as ruas, avenidas, logradouros, caminhos, passagens, estradas e rodovias. O parágrafo único amplia o alcance do Código: são consideradas vias terrestres as praias abertas à circulação pública, as vias internas dos condomínios constituídos por unidades autônomas e as vias e áreas de estacionamento de estabelecimentos privados de uso coletivo. É a pegadinha do shopping: o estacionamento privado de uso coletivo está sujeito ao Código.

"""+L("art. 5º","Art. 5º O Sistema Nacional de Trânsito é o conjunto","Art. 6º")+"""

O Sistema Nacional de Trânsito é o conjunto de órgãos e entidades da União, dos Estados, do Distrito Federal e dos Municípios que exercem as atividades de planejamento, administração, normatização, pesquisa, registro e licenciamento de veículos, formação e habilitação de condutores, educação, engenharia, operação do sistema viário, policiamento, fiscalização, julgamento de infrações e de recursos e aplicação de penalidades.
"""
S[2]="## 2. Quem compõe o sistema e o que fazem o Contran, os Cetran e as JARI\n\n"+L("art. 7º","Art. 7º Compõem o Sistema Nacional de Trânsito","Art. 7º-A")+"\n\n"+L("art. 12, I e II","Art. 12. Compete ao CONTRAN: I - estabelecer","III - (VETADO)")+"\n\n"+L("art. 14, caput e I a V","Art. 14. Compete aos Conselhos Estaduais","VI - indicar um representante")+"\n\n"+L("arts. 16 e 17","Art. 16. Junto a cada órgão","Art. 18.")+"""

O Contran é o coordenador do sistema e o órgão máximo normativo e consultivo. Os Cetran (estaduais) e o Contrandife (do Distrito Federal) são órgãos normativos, consultivos e coordenadores. Em seguida vêm os órgãos executivos de trânsito (que fiscalizam o trânsito e autuam) e os executivos rodoviários (que cuidam das rodovias), a Polícia Rodoviária Federal, as Polícias Militares dos Estados e do Distrito Federal e as JARI. Ao Contran cabe estabelecer as normas regulamentares do Código e as diretrizes da Política Nacional de Trânsito, e coordenar os órgãos do sistema.

Aos Cetran cabe cumprir e fazer cumprir a legislação, elaborar normas, responder a consultas, estimular campanhas educativas e julgar recursos interpostos contra decisões das JARI e de órgãos estaduais nos casos de inaptidão permanente. Junto a cada órgão executivo de trânsito ou rodoviário funciona uma JARI, colegiado que julga os recursos dos infratores contra as penalidades, solicita informações complementares e encaminha ao órgão as falhas que se repetem nas autuações.
"""
S[3]="## 3. As competências de cada órgão e o papel do Município\n\n"+L("art. 23, III","III - executar a fiscalização de trânsito, quando e conforme convênio","IV - (VETADO)")+"\n\n"+L("art. 24, caput e I a VI","Art. 24. Compete aos órgãos e entidades executivos de trânsito dos Municípios","VII - [revogado]")+"\n\n"+L("art. 24, § 4º","§ 4º Compete privativamente aos órgãos e entidades executivos de trânsito dos Municípios","Art. 24-A.")+"\n\n"+L("art. 24-A","Art. 24-A. Compete concorrentemente","Art. 25.")+"\n\n"+L("art. 25, caput","Art. 25. Os órgãos e entidades executivos","§ 1º Os órgãos e entidades de trânsito poderão prestar")+"""

A Polícia Militar só executa a fiscalização de trânsito quando e conforme convênio firmado, como agente do órgão executivo de trânsito. Os órgãos municipais de trânsito, de outro lado, planejam, projetam, regulamentam e operam o trânsito, implantam e mantêm a sinalização, estabelecem com a polícia as diretrizes de policiamento ostensivo, executam a fiscalização de trânsito, autuam e aplicam penalidades de advertência por escrito, multa e medidas administrativas. A fiscalização municipal alcança as vias terrestres, as edificações de uso público e as edificações privadas de uso coletivo, e, nestas últimas, somente para infrações de uso de vagas reservadas em estacionamentos (§ 3º).

O § 4º traz as competências privativas dos Municípios, ou seja, aquelas que só eles exercem: as infrações dos arts. 95, 181, 182, 183, 218 e 219, dos incisos V e X do caput do art. 231 e dos arts. 245, 246 e 279-A. São, em geral, as de estacionamento, parada, velocidade e obras na via. As demais infrações cabem concorrentemente aos Estados, ao Distrito Federal e aos Municípios (art. 24-A), e as privativas podem ser delegadas por convênio (art. 25). A prova costuma explorar essa distinção entre privativa e concorrente, e a possibilidade de convênio.
"""
S[5]="""## 5. Na rotina do guarda

- **Município no sistema:** para exercer as competências do art. 24, o Município deve integrar-se ao Sistema Nacional de Trânsito, por órgão ou entidade executivos de trânsito ou diretamente pela prefeitura (§ 2º).
- **Agente de trânsito:** o guarda que atua na fiscalização de trânsito o faz como agente do órgão executivo de trânsito municipal, por meio de lei ou convênio.
- **Estacionamento:** infrações de estacionamento e parada estão entre as competências privativas dos Municípios.
- **Estacionamento de shopping:** a vaga reservada em edificação privada de uso coletivo pode ser fiscalizada pelo Município.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Trânsito é só circulação | Inclui parada, estacionamento e operação de carga ou descarga |
| Via é só rua e estrada | Inclui praias abertas, vias internas de condomínios e estacionamentos de uso coletivo |
| Contran é executivo | É o órgão máximo normativo e consultivo e coordenador |
| Quem julga os recursos dos infratores | As JARI, junto a cada órgão de trânsito ou rodoviário |
| Recursos contra decisões das JARI | Vão ao Cetran (e ao Contrandife) |
| Polícia Militar fiscaliza o trânsito | Só quando e conforme convênio, como agente do órgão executivo |
| Competência privativa municipal | Arts. 95, 181, 182, 183, 218, 219, 231 (V e X), 245, 246 e 279-A |
| Competência concorrente | Estados, DF e Municípios, observadas as privativas (art. 24-A) |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Trânsito | Uso da via por pessoas, veículos e animais, para circular, parar, estacionar, carregar |
| Vias | Ruas, avenidas, estradas; mais praias abertas, vias de condomínio e estacionamentos de uso coletivo |
| Prioridade do sistema | Defesa da vida, saúde e meio ambiente |
| Contran | Coordenador; órgão máximo normativo e consultivo |
| Cetran e Contrandife | Normativos, consultivos e coordenadores; julgam recursos das JARI |
| JARI | Julgam os recursos dos infratores |
| PM | Fiscaliza trânsito mediante convênio |
| Município | Fiscaliza, autua e aplica penalidades; privativas do § 4º do art. 24 |
| Convênio | Art. 25: delegação de atividades |
"""
QR=[("Questão 1","Segundo o Código de Trânsito Brasileiro, o trânsito é a utilização das vias por pessoas, veículos e animais, isolados ou em grupos, conduzidos ou não, para fins de",["circulação, parada, estacionamento e operação de carga ou descarga.","circulação, apenas.","circulação e parada, apenas.","circulação e estacionamento, apenas.","transporte de cargas, apenas."],0,"Art. 1º, § 1º."),
("Questão 2","O órgão máximo normativo e consultivo do Sistema Nacional de Trânsito, coordenador do sistema, é o",["Conselho Nacional de Trânsito (Contran).","Conselho Estadual de Trânsito (Cetran).","Departamento Nacional de Trânsito.","Polícia Rodoviária Federal.","Departamento Estadual de Trânsito."],2,"Art. 7º, I."),
("Questão 3","Junto a cada órgão ou entidade executivos de trânsito ou rodoviário funcionam as",["Juntas Administrativas de Recursos de Infrações (JARI), que julgam os recursos dos infratores.","Câmaras Temáticas.","Corregedorias.","Delegacias.","Ouvidorias."],1,"Art. 16."),
("Questão 4","A Polícia Militar executa a fiscalização de trânsito",["quando e conforme convênio firmado, como agente do órgão ou entidade executivos de trânsito ou rodoviários.","sempre, por competência própria.","nunca.","apenas em rodovias federais.","apenas nas capitais."],4,"Art. 23, III.")]
t1="<strong>Estacionamento do shopping</strong><br><br>Em Vila Nova, cidade fictícia, uma equipe de agentes de trânsito do Município encontrou um carro estacionado em vaga reservada a pessoas com deficiência, sem credencial, no estacionamento de um shopping center, área privada de uso coletivo. O Município tem órgão executivo de trânsito integrado ao Sistema Nacional de Trânsito."
t2="<strong>Recurso contra uma multa</strong><br><br>Um motorista, autuado pelo órgão executivo de trânsito do Município por infração de estacionamento, apresentou recurso, que foi julgado e negado. Ele quer recorrer da decisão e pergunta a quem."
tx={"ctb1a":t1,"ctb1b":t2}
# n=1
q(1,"Segundo o art. 1º do CTB, o trânsito de qualquer natureza nas vias terrestres do território nacional, abertas à circulação, rege-se",["pelo Código de Trânsito Brasileiro.","pelas leis municipais.","pelos costumes.","pelo Código Civil.","pela Constituição Estadual."],"Art. 1º, caput.")
q(1,"Considera-se trânsito a utilização das vias por pessoas, veículos e animais para fins de circulação, parada, estacionamento e",["operação de carga ou descarga.","lazer.","comércio ambulante.","manifestação.","competição."],"Art. 1º, § 1º.")
q(1,"O trânsito, em condições seguras, é direito de todos e dever dos",["órgãos e entidades componentes do Sistema Nacional de Trânsito.","motoristas apenas.","pedestres apenas.","comerciantes.","vizinhos."],"Art. 1º, § 2º.")
q(1,"A prioridade do Sistema Nacional de Trânsito é a defesa da",["vida, nela incluída a preservação da saúde e do meio ambiente.","fluidez do trânsito.","arrecadação.","propriedade.","velocidade."],"Art. 1º, § 5º.")
q(1,"São vias terrestres urbanas e rurais as ruas, as avenidas, os logradouros, os caminhos, as passagens, as estradas e",["as rodovias.","as ferrovias.","os rios.","os aeroportos.","os portos."],"Art. 2º.")
q(1,"Para os efeitos do CTB, são consideradas vias terrestres as praias abertas à circulação pública, as vias internas dos condomínios constituídos por unidades autônomas e",["as vias e áreas de estacionamento de estabelecimentos privados de uso coletivo.","os parques particulares.","as garagens residenciais.","os quintais.","os pátios de escolas."],"Art. 2º, parágrafo único.")
q(1,"O Sistema Nacional de Trânsito é o conjunto de órgãos e entidades da União, dos Estados, do Distrito Federal e",["dos Municípios.","das empresas privadas.","das autoescolas.","das seguradoras.","das fábricas de veículos."],"Art. 5º.")
q(1,"O Conselho Nacional de Trânsito (Contran) é o",["coordenador do sistema e órgão máximo normativo e consultivo.","órgão executivo de trânsito da União.","órgão de fiscalização.","órgão que julga recursos.","órgão de policiamento."],"Art. 7º, I.")
q(1,"Compõem o Sistema Nacional de Trânsito os Conselhos Estaduais de Trânsito (Cetran) e o",["Conselho de Trânsito do Distrito Federal (Contrandife).","Conselho Municipal de Trânsito.","Conselho da OAB.","Conselho Regional de Medicina.","Conselho de Segurança."],"Art. 7º, II.")
q(1,"Compõem o Sistema Nacional de Trânsito as Polícias Militares dos Estados e do Distrito Federal e a",["Polícia Rodoviária Federal.","Polícia Federal.","Polícia Civil.","Polícia Legislativa.","Guarda portuária."],"Art. 7º, V e VI.")
q(1,"Compõem o Sistema Nacional de Trânsito as Juntas Administrativas de Recursos de",["Infrações (JARI).","Impostos.","Indenizações.","Inquéritos.","Investigações."],"Art. 7º, VII.")
q(1,"Compete ao Contran estabelecer as normas regulamentares do Código e as diretrizes da",["Política Nacional de Trânsito.","Política Criminal.","Política Monetária.","Política Fiscal.","Política Externa."],"Art. 12, I.")
q(1,"Compete ao Contran coordenar os órgãos do Sistema Nacional de Trânsito, objetivando a",["integração de suas atividades.","competição entre eles.","extinção de competências.","redução de quadros.","privatização."],"Art. 12, II.")
q(1,"Compete aos Cetran e ao Contrandife julgar os recursos interpostos contra decisões das",["JARI.","autoescolas.","seguradoras.","delegacias.","corregedorias."],"Art. 14, V, a.")
q(1,"As JARI são órgãos colegiados responsáveis pelo julgamento dos",["recursos interpostos contra penalidades impostas pelo órgão ou entidade junto ao qual funcionam.","processos criminais.","processos trabalhistas.","processos de habilitação.","processos de licenciamento."],"Art. 16.")
q(1,"Compete às JARI julgar os recursos interpostos pelos",["infratores.","juízes.","promotores.","policiais.","fiscais."],"Art. 17, I.")
q(1,"A Polícia Militar executa a fiscalização de trânsito quando e conforme",["convênio firmado.","sua conveniência.","ordem do juiz.","pedido do motorista.","determinação do prefeito."],"Art. 23, III.")
q(1,"Compete aos órgãos e entidades executivos de trânsito dos Municípios implantar, manter e operar o sistema de sinalização, os dispositivos e os",["equipamentos de controle viário.","sistemas de ensino.","sistemas bancários.","sistemas de saúde.","sistemas de segurança privada."],"Art. 24, III.")
q(1,"No texto do estacionamento do shopping, a vaga reservada ocupada indevidamente pode ser fiscalizada pelo Município porque, nas edificações privadas de uso coletivo, a fiscalização municipal alcança as infrações de",["uso de vagas reservadas em estacionamentos.","excesso de velocidade.","embriaguez.","documentação do veículo.","emissão de poluentes."],"Art. 24, § 3º.","ctb1a")
q(1,"No texto do recurso contra a multa, o recurso do motorista, em primeira instância, é julgado pela",["JARI.","Polícia Militar.","Guarda Municipal.","autoescola.","seguradora."],"Art. 16 e art. 17, I.","ctb1b")
# n=2
q(2,"O trânsito de pedestres, veículos e animais, para fins de circulação, parada, estacionamento e carga e descarga, abrange",["não só a circulação, mas também a parada e o estacionamento.","apenas a circulação.","apenas os veículos.","apenas os motoristas.","apenas as vias urbanas."],"Art. 1º, § 1º.")
q(2,"Os órgãos e entidades do Sistema Nacional de Trânsito respondem, no âmbito das respectivas competências, objetivamente, por danos causados por",["ação, omissão ou erro na execução e manutenção de programas, projetos e serviços que garantam o direito do trânsito seguro.","apenas ação dos agentes.","apenas omissão dos agentes.","culpa do motorista.","caso fortuito."],"Art. 1º, § 3º.")
q(2,"Os conceitos e definições estabelecidos para os efeitos do Código são os constantes do",["Anexo I.","Anexo II.","art. 1º.","art. 2º.","art. 10."],"Art. 4º.")
q(2,"São objetivos básicos do Sistema Nacional de Trânsito estabelecer diretrizes da Política Nacional de Trânsito, com vistas à segurança, à fluidez, ao conforto, à defesa ambiental e à",["educação para o trânsito.","arrecadação de multas.","redução da frota.","reforma das vias.","venda de veículos."],"Art. 6º, I.")
q(2,"Os Estados, o Distrito Federal e os Municípios organizam os respectivos órgãos e entidades executivos de trânsito e executivos rodoviários, estabelecendo os limites",["circunscricionais de suas atuações.","de pontos da carteira.","de velocidade.","de multas.","de impostos."],"Art. 8º.")
q(2,"O Contran é composto pelos",["Ministros de Estado responsáveis por diversas áreas, como saúde, justiça, transportes terrestres, segurança pública e mobilidade urbana.","governadores de Estado.","prefeitos.","juízes.","delegados."],"Art. 10.")
q(2,"A Polícia Rodoviária Federal exerce, no âmbito das rodovias e estradas federais, entre outras competências, o",["patrulhamento ostensivo e a fiscalização de trânsito.","julgamento de recursos.","registro de veículos.","licenciamento de veículos.","habilitação de condutores."],"Art. 20, II e III.")
q(2,"Os Cetran julgam recursos contra decisões das JARI e dos órgãos executivos estaduais nos casos de",["inaptidão permanente constatados nos exames de aptidão física, mental ou psicológica.","excesso de velocidade.","estacionamento irregular.","falta de documento.","embriaguez."],"Art. 14, V, b.")
q(2,"Dos casos previstos no art. 14, V, julgados pelo Cetran, no âmbito administrativo",["não cabe recurso.","cabe recurso ao Contran.","cabe recurso às JARI.","cabe recurso à JARI estadual.","cabe recurso ao prefeito."],"Art. 14, parágrafo único.")
q(2,"Os presidentes dos Cetran são nomeados pelos",["Governadores dos Estados.","Prefeitos.","Presidente da República.","juízes de direito.","comandantes da PM."],"Art. 15, caput.")
q(2,"O mandato dos membros dos Cetran e do Contrandife é de",["dois anos, admitida a recondução.","quatro anos, sem recondução.","um ano.","cinco anos.","seis anos."],"Art. 15, § 3º.")
q(2,"As JARI têm regimento próprio, observado o inciso VI do art. 12, e apoio administrativo e financeiro do",["órgão ou entidade junto ao qual funcionem.","Contran.","Cetran.","Ministério Público.","Poder Judiciário."],"Art. 16, parágrafo único.")
q(2,"Compete aos órgãos e entidades executivos de trânsito dos Municípios executar a fiscalização de trânsito em vias terrestres, edificações de uso público e",["edificações privadas de uso coletivo.","residências.","fábricas.","quintais.","estacionamentos de casas."],"Art. 24, VI.")
q(2,"O exercício da fiscalização municipal em edificações privadas de uso coletivo somente se aplica a infrações de",["uso de vagas reservadas em estacionamentos.","excesso de velocidade.","embriaguez.","documentação.","emissão de ruído."],"Art. 24, § 3º.")
q(2,"Para exercer as competências do art. 24, os Municípios devem",["integrar-se ao Sistema Nacional de Trânsito.","aguardar autorização do Contran.","contratar a PM.","criar uma guarda.","pagar taxa ao Estado."],"Art. 24, § 2º.")
q(2,"Compete concorrentemente aos órgãos executivos de trânsito dos Estados, do DF e dos Municípios executar a fiscalização, autuar e aplicar as medidas administrativas, observado o disposto",["no § 2º do art. 22 e no § 4º do art. 24.","no art. 1º.","no art. 5º.","no art. 10.","no art. 12."],"Art. 24-A.")
q(2,"As competências privativas previstas no § 2º do art. 22 e no § 4º do art. 24 podem ser delegadas por meio do convênio de que trata o",["art. 25.","art. 1º.","art. 7º.","art. 12.","art. 16."],"Art. 24-A, parágrafo único.")
q(2,"No texto do estacionamento do shopping, o fato de o Município ter órgão executivo de trânsito integrado ao Sistema Nacional de Trânsito atende ao exigido no",["§ 2º do art. 24.","art. 1º.","art. 5º.","art. 12.","art. 16."],"Art. 24, § 2º.","ctb1a")
q(2,"No texto do recurso, a decisão da JARI pode ser objeto de recurso ao",["Cetran.","Contran.","Prefeito.","Delegado.","Juiz de paz."],"Art. 14, V, a.","ctb1b")
q(2,"No texto do recurso, a multa foi aplicada por órgão executivo de trânsito municipal. A JARI que o julgou funciona",["junto ao órgão ou entidade que aplicou a penalidade.","junto ao Contran.","junto ao Cetran.","junto à PM.","junto à Guarda estadual."],"Art. 16.","ctb1b")
# n=3
q(3,"Assinale a alternativa que traz apenas órgãos componentes do Sistema Nacional de Trânsito, nos termos do art. 7º.",["Contran, Cetran, órgãos executivos de trânsito, Polícia Rodoviária Federal, Polícias Militares e JARI.","Contran, Polícia Civil e Polícia Federal.","Cetran, Ministério Público e Defensoria.","JARI, Tribunais de Justiça e Contran.","Contran, DNIT e INSS."],"Art. 7º.")
q(3,"Considere as afirmações. I. As vias terrestres incluem os estacionamentos privados de uso coletivo. II. O Contran é o órgão máximo normativo e consultivo. III. As JARI julgam os recursos contra decisões do Contran. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"As JARI julgam recursos dos infratores contra penalidades (art. 16).")
q(3,"Assinale a INCORRETA.",["A Polícia Militar executa a fiscalização de trânsito sempre, independentemente de convênio.","Os órgãos municipais executam a fiscalização de trânsito nas vias, nas edificações de uso público e, em parte, nas privadas de uso coletivo.","As JARI funcionam junto a cada órgão de trânsito ou rodoviário.","O trânsito inclui a parada e o estacionamento.","Os Cetran julgam recursos contra decisões das JARI."],"A PM só fiscaliza o trânsito quando e conforme convênio (art. 23, III).")
q(3,"O § 4º do art. 24 traz competências privativas dos Municípios, incluindo as infrações dos",["arts. 95, 181, 182, 183, 218 e 219, entre outros.","arts. 165 a 170.","arts. 252 a 255.","arts. 302 a 312.","arts. 140 a 160."],"Art. 24, § 4º.")
q(3,"A diferença entre competência privativa e concorrente, no art. 24-A, é que a concorrente é exercida",["por Estados, DF e Municípios, observadas as competências privativas.","somente pelos Municípios.","somente pelos Estados.","somente pela União.","somente pela PRF."],"Art. 24-A.")
q(3,"Os convênios do art. 25 permitem delegar as atividades do Código com vistas a",["maior eficiência e segurança para os usuários da via.","economia de recursos.","redução de multas.","extinção de órgãos.","privatização das vias."],"Art. 25, caput.")
q(3,"Se não há órgão executivo de trânsito no Município, o convênio do art. 25 poderá ser celebrado",["diretamente pela prefeitura municipal com órgão ou entidade que integre o Sistema, permitido o consórcio.","apenas pela União.","apenas pelo Estado.","apenas pelo Contran.","apenas pela PRF."],"Art. 25, § 2º.")
q(3,"O Contran pode, em caso de urgência e de relevante interesse público, editar deliberação",["ad referendum do Plenário.","sem prazo.","sem necessidade de aprovação.","só com o prefeito.","só com o governador."],"Art. 12, § 3º.")
q(3,"As propostas de normas regulamentares do Contran são submetidas a prévia consulta pública, pelo prazo mínimo de",["30 dias.","10 dias.","15 dias.","60 dias.","90 dias."],"Art. 12, § 1º.")
q(3,"As contribuições recebidas na consulta pública do Contran ficam à disposição do público pelo prazo de",["2 anos.","6 meses.","1 ano.","5 anos.","10 anos."],"Art. 12, § 2º.")
q(3,"A Polícia Rodoviária Federal pode aplicar as penalidades de",["advertência por escrito e multa, e as medidas administrativas cabíveis.","apenas advertência.","apenas multa.","cassação de habilitação.","prisão."],"Art. 20, III.")
q(3,"O quórum de votação e de aprovação no Contran é o de",["maioria absoluta.","maioria simples.","dois terços.","unanimidade.","um terço."],"Art. 10, § 6º.")
q(3,"O Contran será presidido pelo Ministro de Estado ao qual estiver subordinado o",["órgão máximo executivo de trânsito da União.","Presidente do STF.","Presidente da República.","Governador do DF.","Prefeito da capital."],"Art. 10, § 3º-A.")
q(3,"Os órgãos e entidades executivos de trânsito dos Municípios devem estabelecer, em conjunto com os órgãos de polícia ostensiva de trânsito,",["as diretrizes para o policiamento ostensivo de trânsito.","as tarifas de ônibus.","os horários de lojas.","as regras de habilitação.","os limites de pontos."],"Art. 24, V.")
q(3,"Compete aos órgãos municipais de trânsito executar a fiscalização, autuar e aplicar penalidades de",["advertência por escrito e multa, e as medidas administrativas cabíveis.","apenas multa.","apenas advertência.","apenas suspensão.","apenas cassação."],"Art. 24, VI.")
q(3,"Considere o art. 24, § 4º. A fiscalização de trânsito, a autuação e a aplicação das penalidades previstas nos arts. 95, 181, 182, 183, 218 e 219, entre outros, competem",["privativamente aos órgãos executivos de trânsito dos Municípios, no âmbito de sua circunscrição.","privativamente à PRF.","privativamente aos Estados.","privativamente à PM.","privativamente ao Contran."],"Art. 24, § 4º.")
q(3,"O art. 24, VI, que dá ao Município a competência de fiscalização, atribui-lhe também a de notificar os infratores e arrecadar",["as multas que aplicar.","os impostos federais.","as multas estaduais.","as taxas de cartório.","os tributos do Estado."],"Art. 24, VI.")
q(3,"No texto do estacionamento do shopping, a competência para autuar a infração da vaga reservada, no estacionamento privado de uso coletivo, cabe, nos termos do art. 24,",["ao órgão executivo de trânsito do Município.","à Polícia Federal.","ao Contran.","ao proprietário do shopping.","à JARI."],"Art. 24, VI e § 3º.","ctb1a")
q(3,"No texto do estacionamento do shopping, a possibilidade de o Município fiscalizar a vaga reservada em área privada limita-se ao",["uso de vagas reservadas em estacionamentos.","excesso de velocidade no estacionamento.","excesso de peso.","embriaguez.","documentação."],"Art. 24, § 3º.","ctb1a")
q(3,"No texto do recurso, o recurso ao Cetran, contra decisão da JARI, é a última instância administrativa porque",["dos casos julgados pelo Cetran não cabe recurso na esfera administrativa.","a lei veda recursos.","o prazo prescreve.","o Cetran não existe.","o Contran decide de ofício."],"Art. 14, parágrafo único.","ctb1b")
assert len(Q)==60,len(Q)
code,svg=mapa("Sistema Nacional de Trânsito",[
 ("def","Trânsito e vias",["uso da via por pessoas, veículos e animais","circular, parar, estacionar, carregar","vias incluem praias e estacionamentos de uso coletivo"],"seção 1"),
 ("comp","Composição",["Contran, Cetran, executivos","PRF, Polícias Militares","JARI"],"seção 2"),
 ("contr","Contran e Cetran",["Contran: normas e coordenação","Cetran: normas e recursos","consulta pública de 30 dias"],"seção 2"),
 ("jari","JARI",["junto a cada órgão","julgam recursos dos infratores","recurso da JARI vai ao Cetran"],"seção 2"),
 ("mun","Município",["fiscaliza e autua","multa e advertência","§ 4º: competências privativas"],"seção 3"),
 ("conv","Convênio e concorrência",["art. 24-A: concorrente","art. 25: delegação","PM só por convênio"],"seção 3")],
 "Na prova: separe órgão normativo (Contran e Cetran), julgador (JARI) e executivo (fiscaliza e autua)")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira caixa define o objeto do Código; as demais mostram quem faz o quê, até chegar ao Município.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 1º a 25, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-1","Disposições preliminares e Sistema Nacional de Trânsito (CTB, arts. 1º a 25)",Q,list(tx),
 cobertura=["Recorte do edital: composição e competências dos órgãos. Cobertos: arts. 1º a 6º, 7º, 8º, 10, 12, 14 a 17, 20 a 25. Os arts. 9º, 11, 13, 18, 19 e 25-A foram citados apenas em parte ou omitidos."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","A consolidação traz erros de digitação do próprio texto da fonte (ex.: “Policia Rodovia Federal”, no art. 20); as citações os reproduzem.","As competências dos arts. 19 (órgão máximo executivo da União) e 21 (órgãos rodoviários) foram tratadas apenas de passagem.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb1a e ctb1b fictícios."],
 fontes_conferidas=["CTB, arts. 1º a 25: texto da Câmara, copiado por programa."])
gravar("ctb-1",aula_html,banco("ctb-1",Q),tx)
