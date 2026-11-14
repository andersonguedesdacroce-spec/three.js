import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='armas.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Decreto 11.615/2023 regulamenta o Estatuto do Desarmamento (Lei 10.826/2003). É longo, mas, para a prova de Guarda Municipal, o ponto central está nos arts. 57 a 60: quem concede o porte funcional ao guarda (a Polícia Federal), por quanto tempo (dez anos), onde vale (nos limites do Estado), quanto de treinamento (cem horas para semiautomática, no mínimo 65% de prática), o estágio anual de oitenta horas e as exigências ao Município (corregedoria e ouvidoria independentes). Esta aula também traz o objeto do decreto, a finalidade do Sinarm e o regime do porte funcional dos arts. 53 a 56."
S={}
S[1]="## 1. Objeto e Sinarm\n\n"+L("art. 1º","Art. 1º Este Decreto regulamenta","Definições Art. 2º")+"\n\n"+L("art. 3º, caput e I","Art. 3º O Sinarm","II - informar às Secretarias")+"\n\n"+L("art. 7º, caput","Art. 7º Serão cadastrados no Sinarm","§ 1º Serão cadastradas")+"\n\n"+L("art. 7º, § 1º, III, i","i) das guardas municipais","j) dos órgãos públicos")+"""

O decreto regulamenta o Estatuto do Desarmamento para estabelecer regras sobre aquisição, registro, posse, porte, cadastro e comercialização de armas de fogo, munições e acessórios; disciplinar a caça excepcional, a caça de subsistência, o tiro desportivo e o colecionamento; disciplinar as entidades de tiro desportivo; e estruturar o Sistema Nacional de Armas (Sinarm). O Sinarm, no âmbito da Polícia Federal e com circunscrição nacional, mantém cadastro geral das armas importadas, produzidas e comercializadas, das autorizações de porte, das transferências, extravios, furtos, roubos, apreensões e dos armeiros em atividade. São cadastrados no Sinarm, entre outros, os armeiros, os produtores, atacadistas e varejistas autorizados, os instrutores de armamento e tiro credenciados, os psicólogos credenciados e os caçadores de subsistência. As armas institucionais das guardas municipais são cadastradas no Sinarm, nos termos das leis municipais que as instituíram.
"""
S[2]="## 2. Porte de arma de fogo funcional\n\n"+L("art. 53, caput","Art. 53. O porte de arma em razão","§ 1º O porte de arma de fogo é deferido")+"\n\n"+L("art. 54, caput","Art. 54. A autorização para o porte","§ 1º O porte de arma de fogo de que tratam")+"\n\n"+L("art. 55, caput","Art. 55. Os órgãos, as instituições","§ 1º As instituições a que se refere o inciso IV")+"\n\n"+L("art. 55, §§ 4º e 5º","§ 4º Não será concedida","§ 6º A vedação")+"\n\n"+L("art. 56","Art. 56. As armas de fogo particulares","Concessão de porte de arma de fogo funcional")+"""

O porte de arma em razão do desempenho de funções institucionais é deferido aos integrantes das instituições a que se referem os incisos I a VII, X e XI do art. 6º da Lei 10.826/2003. A autorização para o porte previsto em legislação própria fica condicionada ao atendimento dos requisitos de idoneidade e de aptidão psicológica e capacidade técnica do art. 4º da Lei. Os órgãos estabelecem, em normas próprias, as condições para a utilização das armas de sua propriedade, ainda que fora de serviço. Não será concedida autorização para porte a integrantes de órgãos não autorizados a portar arma fora de serviço, exceto se comprovarem risco à sua integridade física. O porte de que tratam os incisos V, VI e X do art. 6º é concedido exclusivamente para defesa pessoal, vedado o porte ostensivo. As armas particulares e as institucionais não brasonadas devem ser conduzidas com o respectivo CRAF ou com o termo de cautela decorrente de autorização judicial.
"""
S[3]="## 3. Porte funcional das guardas municipais\n\n"+L("art. 57, caput e incisos","Art. 57. A Polícia Federal, diretamente","Parágrafo único. Os guardas municipais")+"\n\n"+L("art. 57, parágrafo único","Parágrafo único. Os guardas municipais autorizados","Art. 58.")+"\n\n"+L("art. 58","Art. 58. A formação de guardas municipais","Art. 59.")+"\n\n"+L("art. 59","Art. 59. O porte de arma de fogo aos integrantes","Art. 60.")+"\n\n"+L("art. 60","Art. 60. A Polícia Federal somente poderá","Seção V")+"""

A Polícia Federal, diretamente ou por convênio, e sob a supervisão do Ministério da Justiça e Segurança Pública, estabelece o currículo da disciplina de armamento e tiro dos cursos de formação das guardas municipais, concede o porte de arma de fogo funcional aos integrantes, com validade de dez anos, nos limites territoriais do Estado em que exercerem a função, e fiscaliza os cursos. Os guardas autorizados podem portar a arma nos deslocamentos para suas residências, mesmo em Município de Estado limítrofe.

A formação só pode ocorrer em estabelecimento de ensino de atividade policial, em órgão municipal de formação, em órgão criado por Municípios consorciados ou em órgão estadual centralizado e conveniado. O porte exige comprovação de treinamento técnico de, no mínimo, sessenta horas para arma de repetição (se houver na dotação), cem horas para arma semiautomática e sessenta horas para arma automática (se houver na dotação), com no mínimo 65% de carga horária prática. O curso de formação contém técnicas de tiro defensivo e defesa pessoal, e os guardas com porte fazem estágio anual de qualificação de no mínimo oitenta horas.

A Polícia Federal só pode conceder porte às guardas dos Municípios que tenham instituído corregedoria própria e independente para a apuração de infrações disciplinares e ouvidoria, como órgão permanente, autônomo e independente, com competência para fiscalizar, investigar, auditar e propor políticas de qualificação das atividades dos integrantes.
"""
S[5]="""## 5. Na rotina do guarda

- **Porte funcional:** o guarda municipal com porte conduz a arma em serviço e nos deslocamentos para a residência, mesmo em Município de Estado limítrofe.
- **Território:** o porte vale nos limites territoriais do Estado em que o guarda exerce a função.
- **Treinamento:** para a arma semiautomática, o guarda comprova no mínimo cem horas de treinamento técnico, com 65% de prática.
- **Estágio anual:** os guardas com porte fazem estágio de qualificação de no mínimo oitenta horas por ano.
- **Fora de serviço:** só portam fora de serviço se a norma própria da instituição permitir; do contrário, é preciso comprovar risco à integridade física.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Quem concede o porte à guarda municipal | Polícia Federal |
| Validade do porte | Dez anos, da data de emissão |
| Limite territorial | Estado em que exerce a função; deslocamento à residência, inclusive em Estado limítrofe |
| Treinamento para arma semiautomática | Cem horas |
| Arma de repetição ou automática | Sessenta horas, se houver na dotação |
| Carga prática | No mínimo 65% |
| Estágio anual | Mínimo de oitenta horas |
| Exigências ao Município | Corregedoria e ouvidoria independentes |
| Locais de formação | Estabelecimento policial, órgão municipal, consórcio ou órgão estadual conveniado |
| Armas das guardas | Cadastradas no Sinarm |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Aquisição, registro, posse, porte, cadastro, comercialização |
| Art. 3º | Sinarm: cadastro geral na Polícia Federal |
| Art. 53 | Porte funcional |
| Art. 55 | Defesa pessoal; sem porte ostensivo (alguns incisos) |
| Art. 56 | CRAF ou termo de cautela |
| Art. 57 | Porte à guarda municipal: Polícia Federal, dez anos, nos limites do Estado |
| Art. 58 | Locais de formação |
| Art. 59 | Treinamento: 60, 100 e 60 horas; 65% prático; estágio de 80 horas |
| Art. 60 | Corregedoria e ouvidoria como condição |
"""
QR=[("Questão 1","A Polícia Federal concederá porte de arma de fogo funcional aos integrantes das guardas municipais, com prazo de validade de",["dez anos, contado da data de emissão do porte.","cinco anos.","dois anos.","três anos.","um ano."],0,"Art. 57, II."),
("Questão 2","O porte funcional dos integrantes das guardas municipais vale nos limites territoriais do",["Estado em que exercerem a função.","território nacional.","Município.","Distrito Federal.","país e fronteiras."],1,"Art. 57, II."),
("Questão 3","Para a arma de fogo semiautomática, o treinamento técnico mínimo é de",["cem horas.","sessenta horas.","oitenta horas.","quarenta horas.","duzentas horas."],2,"Art. 59, II."),
("Questão 4","Os profissionais das guardas municipais com porte de arma de fogo serão submetidos a estágio de qualificação profissional de, no mínimo,",["oitenta horas anuais.","vinte horas anuais.","quarenta horas anuais.","cento e vinte horas anuais.","sessenta horas anuais."],3,"Art. 59, § 3º.")]
t1="<strong>Guarda e a residência</strong><br><br>Um guarda municipal de Vila Nova, cidade fictícia, mora no Município vizinho, que fica em outro Estado, e foi para casa com sua arma funcional após o plantão."
t2="<strong>Município sem ouvidoria</strong><br><br>Vila Nova pretende armar sua guarda, mas ainda não instituiu a ouvidoria nem a corregedoria própria e independente."
t3="<strong>Curso de formação</strong><br><br>Um curso de formação de guardas de Vila Nova previa sessenta horas de treinamento com a arma semiautomática, sendo 40% de prática."
tx={"armas1a":t1,"armas1b":t2,"armas1c":t3}
# n=1
q(1,"O Decreto 11.615/2023 regulamenta a Lei 10.826/2003, que é o Estatuto do",["Desarmamento.","Idoso.","Torcedor.","Desporto.","Índio."],"Art. 1º.")
q(1,"O decreto estabelece regras sobre aquisição, registro, posse, porte, cadastro e comercialização nacional de armas de fogo, munições e",["acessórios.","veículos.","imóveis.","empresas.","remédios."],"Art. 1º, I.")
q(1,"O Sinarm é instituído no âmbito da Polícia",["Federal.","Civil.","Militar.","Rodoviária.","Penal."],"Art. 3º.")
q(1,"O Sinarm tem circunscrição no território",["nacional.","estadual.","municipal.","urbano.","rural."],"Art. 3º.")
q(1,"Serão cadastrados no Sinarm os armeiros em atividade no País e as suas licenças para o exercício da atividade",["profissional.","comercial.","esportiva.","estrangeira.","rural."],"Art. 7º, I.")
q(1,"Serão cadastrados no Sinarm os psicólogos credenciados para a aplicação do exame de aptidão",["psicológica.","física.","médica.","intelectual.","jurídica."],"Art. 7º, IV.")
q(1,"As armas institucionais das guardas municipais são cadastradas no Sinarm, nos termos das leis municipais que as",["instituíram.","revogaram.","aboliram.","modificaram.","suspenderam."],"Art. 7º, § 1º, III, i.")
q(1,"O porte de arma em razão de funções institucionais é deferido aos integrantes das instituições do art. 6º da Lei",["10.826/2003.","9.503/1997.","11.340/2006.","8.069/1990.","13.675/2018."],"Art. 53.")
q(1,"As armas particulares e as institucionais não brasonadas devem ser conduzidas com o respectivo",["CRAF.","CNH.","CPF.","passaporte.","título."],"Art. 56.")
q(1,"A Polícia Federal concede porte funcional aos integrantes das guardas municipais, nos limites territoriais do",["Estado.","país.","bairro.","Município.","Distrito."],"Art. 57, II.")
q(1,"A Polícia Federal estabelece o currículo da disciplina de armamento e tiro dos cursos de formação das guardas",["municipais.","particulares.","federais.","estaduais.","portuárias."],"Art. 57, I.")
q(1,"Os guardas municipais autorizados a portar arma podem portá-la nos deslocamentos para suas",["residências.","festas.","viagens.","férias.","reuniões."],"Art. 57, parágrafo único.")
q(1,"O porte funcional dos guardas municipais vale por",["dez anos.","um ano.","dois anos.","cinco anos.","vinte anos."],"Art. 57, II.")
q(1,"Para a arma de fogo semiautomática, o treinamento técnico é de, no mínimo, cem",["horas.","dias.","semanas.","meses.","anos."],"Art. 59, II.")
q(1,"O curso de formação das guardas municipais conterá técnicas de tiro defensivo e de defesa",["pessoal.","coletiva.","estratégica.","financeira.","legal."],"Art. 59, § 2º.")
q(1,"A Polícia Federal só concede porte às guardas dos Municípios que tenham instituído corregedoria própria e",["independente.","subordinada.","provisória.","terceirizada.","estadual."],"Art. 60, I.")
q(1,"A Polícia Federal só concede porte às guardas dos Municípios que tenham instituído ouvidoria, como órgão permanente, autônomo e",["independente.","subordinado.","provisório.","terceirizado.","estadual."],"Art. 60, II.")
q(1,"No texto do guarda e a residência, o guarda com porte pode portar a arma na ida para casa, mesmo que seja em Município de Estado",["limítrofe.","distante.","estrangeiro.","da região Norte.","da região Sul."],"Art. 57, parágrafo único.","armas1a")
q(1,"No texto do Município sem ouvidoria, o Município precisa instituir corregedoria própria e independente e",["ouvidoria permanente, autônoma e independente.","apenas ouvidoria.","apenas guarda.","uma delegacia.","um batalhão."],"Art. 60.","armas1b")
q(1,"No texto do curso de formação, o treinamento com a arma semiautomática deveria ser de no mínimo",["cem horas.","sessenta horas.","oitenta horas.","quarenta horas.","trinta horas."],"Art. 59, II.","armas1c")
# n=2
q(2,"O decreto disciplina a caça excepcional, a caça de subsistência, o tiro desportivo e o",["colecionamento de armas de fogo.","comércio varejista.","uso agrícola.","desfile cívico.","transporte aéreo."],"Art. 1º, II.")
q(2,"O Sinarm informa às Secretarias de Segurança Pública dos Estados e do Distrito Federal as concessões, suspensões e cassações de CRAF, CRPF e",["CRPJ.","CNH.","CPF.","CNPJ.","CTPS."],"Art. 3º, II, a.")
q(2,"Serão cadastrados no Sinarm os instrutores de armamento e tiro credenciados para a aplicação de teste de capacidade",["técnica.","física.","psicológica.","moral.","jurídica."],"Art. 7º, III.")
q(2,"Serão cadastrados no Sinarm os caçadores de",["subsistência.","fim de semana.","aventura.","cadastro.","coleção."],"Art. 7º, V.")
q(2,"O porte funcional de que trata o art. 53 é deferido aos integrantes das instituições do art. 6º, incisos I a VII, X e",["XI.","VIII.","IX.","XII.","XIII."],"Art. 53.")
q(2,"A autorização para o porte de arma previsto em legislação própria fica condicionada ao atendimento dos requisitos do caput e do inciso III do art. 4º da Lei, que tratam de idoneidade e de",["aptidão psicológica e capacidade técnica.","renda.","residência.","estado civil.","filiação."],"Art. 54.")
q(2,"Os órgãos estabelecem, em normas próprias, as condições para utilização das armas de sua propriedade, ainda que fora de",["serviço.","alcance.","horário.","limite.","zona."],"Art. 55.")
q(2,"Não será concedida autorização de porte fora de serviço a integrantes de órgãos não autorizados, exceto se comprovarem o risco à sua integridade",["física.","moral.","patrimonial.","profissional.","financeira."],"Art. 55, § 4º.")
q(2,"O porte dos incisos V, VI e X do art. 6º da Lei é concedido exclusivamente para defesa pessoal, vedado o porte",["ostensivo.","discreto.","noturno.","interno.","externo."],"Art. 55, § 5º.")
q(2,"A formação de guardas municipais poderá ocorrer em estabelecimento de ensino de atividade",["policial.","civil.","esportiva.","religiosa.","comercial."],"Art. 58, I.")
q(2,"A formação pode ocorrer em órgão criado e mantido por Municípios",["consorciados.","vizinhos.","estrangeiros.","privados.","federais."],"Art. 58, III.")
q(2,"O porte aos integrantes das instituições dos incisos III e IV do art. 6º da Lei será concedido mediante comprovação de treinamento técnico de, para arma de repetição, no mínimo",["sessenta horas, se a instituição a possuir na dotação.","cem horas.","oitenta horas.","quarenta horas.","trinta horas."],"Art. 59, I.")
q(2,"Para arma de fogo automática, o treinamento técnico mínimo é de",["sessenta horas, se a instituição a possuir na dotação.","cem horas.","oitenta horas.","quarenta horas.","trinta horas."],"Art. 59, III.")
q(2,"O treinamento do art. 59 destinará, no mínimo, sessenta e cinco por cento de sua carga horária ao conteúdo",["prático.","teórico.","jurídico.","administrativo.","burocrático."],"Art. 59, § 1º.")
q(2,"O estágio de qualificação profissional dos guardas com porte é de no mínimo oitenta horas",["anuais.","mensais.","semanais.","diárias.","bianuais."],"Art. 59, § 3º.")
q(2,"A formação de guardas pode ocorrer em órgão estadual centralizado e conveniado, no qual seja assegurada a participação dos Municípios conveniados no conselho",["gestor.","deliberativo.","fiscal.","superior.","consultivo."],"Art. 58, IV.")
q(2,"No texto do guarda e a residência, o porte nos deslocamentos para a residência decorre do",["parágrafo único do art. 57.","art. 53.","art. 55.","art. 56.","art. 60."],"Art. 57, parágrafo único.","armas1a")
q(2,"No texto do Município sem ouvidoria, a Polícia Federal não poderá conceder porte até a instituição de",["corregedoria e ouvidoria.","novo guarda.","novo edifício.","nova viatura.","novo plano."],"Art. 60.","armas1b")
q(2,"No texto do curso de formação, o percentual de prática de 40% é inferior ao mínimo de",["65%.","50%.","30%.","25%.","80%."],"Art. 59, § 1º.","armas1c")
q(2,"O Sinarm mantém cadastro geral, integrado e permanente das autorizações de porte de arma de fogo e das renovações expedidas pela Polícia",["Federal.","Civil.","Militar.","Rodoviária.","Penal."],"Art. 3º, I, b.")
# n=3
q(3,"Assinale a alternativa correta sobre o porte funcional dos guardas municipais.",["Concedido pela Polícia Federal, com validade de dez anos, nos limites do Estado, e vale nos deslocamentos à residência, inclusive em Estado limítrofe.","Concedido pelo Exército, com validade de cinco anos.","Vale em todo o território nacional.","Vale apenas no Município.","Dispensa treinamento."],"Art. 57.")
q(3,"Considere. I. Para arma semiautomática, o treinamento é de 100 horas. II. O estágio anual é de 40 horas. III. O mínimo prático é de 65%. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O estágio anual é de no mínimo oitenta horas (art. 59, § 3º).")
q(3,"Assinale a INCORRETA.",["A Polícia Federal pode conceder porte às guardas de Municípios sem corregedoria.","O Município precisa de ouvidoria independente.","O Município precisa de corregedoria independente.","A Polícia Federal supervisiona o currículo de tiro.","O porte funcional vale dez anos."],"A concessão exige corregedoria e ouvidoria (art. 60).")
q(3,"Entre os requisitos de treinamento do art. 59, para armas de repetição ou automáticas o mínimo é de sessenta horas, na hipótese de a instituição possuir esse armamento em sua",["dotação.","sede.","reserva.","base.","ala."],"Art. 59, I e III.")
q(3,"A Polícia Federal, nos termos do art. 57, fiscaliza os cursos de formação para assegurar o cumprimento do",["currículo da disciplina de armamento e tiro.","regime disciplinar.","regimento da guarda.","edital.","horário de trabalho."],"Art. 57, III.")
q(3,"A Polícia Federal pode conceder o porte diretamente ou por convênio com os órgãos de segurança pública dos Estados, do Distrito Federal e dos",["Municípios.","clubes.","sindicatos.","bancos.","partidos."],"Art. 57.")
q(3,"O art. 57 refere-se ao § 3º do art. 6º da Lei 10.826/2003, que trata do porte pelas guardas",["municipais.","portuárias.","escolares.","florestais.","privadas."],"Art. 57.")
q(3,"A corregedoria exigida do Município deve ser própria e independente para a apuração de infrações disciplinares atribuídas aos servidores integrantes da guarda",["municipal.","estadual.","federal.","militar.","portuária."],"Art. 60, I.")
q(3,"A ouvidoria tem competência para fiscalizar, investigar, auditar e propor políticas de qualificação das atividades dos integrantes das",["guardas municipais.","polícias militares.","polícias civis.","forças armadas.","empresas."],"Art. 60, II.")
q(3,"O porte em razão do art. 53 aplica-se às instituições do art. 6º da Lei do Desarmamento, e atos dos Comandantes-Gerais dispõem sobre o porte dos policiais militares e dos militares dos corpos de",["bombeiros.","florestais.","portos.","escolas.","trânsito."],"Art. 53, § 5º.")
q(3,"O art. 55, § 2º, prevê que os órgãos estabelecerão normas gerais de uso da arma, fora do serviço, em locais onde haja aglomeração de pessoas, como igrejas, escolas, estádios e",["clubes.","bancos.","fazendas.","navios.","aeroportos."],"Art. 55, § 2º.")
q(3,"O art. 55, § 3º, prevê que os órgãos com portes estabelecidos em lei própria encaminharão à Polícia Federal a relação das pessoas autorizadas a portar arma, exceto os integrantes das Forças",["Armadas, das Forças Auxiliares e do GSI.","Policiais Civis.","do Município.","privadas.","portuárias."],"Art. 55, § 3º.")
q(3,"A autorização do porte para praças das Forças Armadas sem estabilidade é regulamentada em ato do",["Comandante da Força correspondente.","Presidente.","Governador.","Prefeito.","Juiz."],"Art. 53, § 3º.")
q(3,"No texto do guarda e a residência, a regra aplicável é a de que os guardas autorizados podem portar a arma nos deslocamentos para suas residências, em Município situado em Estado",["limítrofe.","distante.","estrangeiro.","isolado.","qualquer."],"Art. 57, parágrafo único.","armas1a")
q(3,"No texto do guarda e a residência, o porte do guarda vale, em regra, nos limites territoriais do Estado em que exerce a",["função.","residência.","família.","faculdade.","propriedade."],"Art. 57, II.","armas1a")
q(3,"No texto do Município sem ouvidoria, a condição legal para a concessão pela Polícia Federal é a instituição de",["corregedoria própria e independente e de ouvidoria permanente, autônoma e independente.","apenas ouvidoria.","apenas corregedoria.","um plano de cargos.","um consórcio."],"Art. 60.","armas1b")
q(3,"No texto do Município sem ouvidoria, o art. 60 se destina às guardas dos Municípios que tenham",["instituído os órgãos de controle.","menos de mil habitantes.","mais de um milhão de habitantes.","convênio com o Estado.","vínculo com o Exército."],"Art. 60.","armas1b")
q(3,"No texto do curso de formação, além de a carga de 60 horas ser inferior ao mínimo para a semiautomática, o prático de 40% é menor que 65%, o que contraria o art.",["59 e seu § 1º.","57.","58.","60.","56."],"Art. 59.","armas1c")
q(3,"No texto do curso de formação, o curso de formação dos guardas conterá técnicas de tiro defensivo e de",["defesa pessoal.","tiro esportivo.","caça.","primeiros socorros apenas.","pilotagem."],"Art. 59, § 2º.","armas1c")
q(3,"O art. 3º, I, prevê que o Sinarm cadastra, entre outros dados, as apreensões de armas de fogo, inclusive as vinculadas a procedimentos policiais e",["judiciais.","tributários.","comerciais.","trabalhistas.","eleitorais."],"Art. 3º, I, d.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Decreto 11.615/2023: porte funcional da guarda municipal",[
 ("obj","Objeto",["aquisição, registro, posse, porte","caça, tiro, colecionamento","Sinarm"],"seção 1"),
 ("sin","Sinarm",["cadastro geral na PF","armeiros, psicólogos, instrutores","armas das guardas"],"seção 1"),
 ("fun","Porte funcional",["art. 53","defesa pessoal, sem porte ostensivo","CRAF ou termo de cautela"],"seção 2"),
 ("gm","Guarda municipal",["PF concede","10 anos","nos limites do Estado"],"seção 3"),
 ("tre","Treinamento",["100 h semiautomática","60 h repetição/automática","65% prática; 80 h por ano"],"seção 3"),
 ("mun","Exigência ao Município",["corregedoria independente","ouvidoria independente"],"seção 3")],
 "Na prova: PF, 10 anos, 100 horas, 65% e 80 horas")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o objeto e o Sinarm; as demais, o porte funcional e o regime específico das guardas municipais.","Fontes: Edital 02/2026, Anexo I; Decreto 11.615/2023, texto da publicação original, Câmara dos Deputados. Exemplos criados para a aula.")
revisao("armas-1","Regulamento do Estatuto do Desarmamento (Decreto 11.615/2023)",Q,list(tx),
 cobertura=["Coberto o essencial: arts. 1º, 3º, 7º, 53 a 60. Não cobertos: o restante do decreto (registro, posse, CRAF, aquisição, caça, tiro desportivo, colecionamento etc.), cerca de 90% do texto."],
 pendencias=["Texto-fonte: publicação original da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto, pois o decreto foi alterado posteriormente (o texto original pode não refletir as alterações).","Conferir o recorte exato do edital: o edital diz 'Registro, posse, porte e classificação de armas', o que exige cobrir também os capítulos de registro e posse (arts. 8º a 52), ainda não cobertos.","Trechos de lei copiados de fontes/armas.txt por programa.","Casos armas1a, armas1b e armas1c fictícios."],
 fontes_conferidas=["Decreto 11.615/2023, arts. 1º, 3º, 7º e 53 a 60: texto da Câmara, copiado por programa."])
gravar("armas-1",aula_html,banco("armas-1",Q),tx)
