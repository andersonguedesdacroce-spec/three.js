import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os arts. 321 a 327 fecham os crimes dos funcionários públicos contra a Administração e definem quem é funcionário público para efeitos penais. A Vunesp cobra a advocacia administrativa, a violência arbitrária (a mais próxima do guarda), o abandono de função, o exercício funcional ilegalmente antecipado ou prolongado, a violação de sigilo funcional e de sigilo de proposta, e o conceito de funcionário público, com a equiparação e o aumento de pena para cargos em comissão e de direção. A aula segue o texto consolidado."
S={}
S[1]="## 1. Advocacia administrativa e violência arbitrária\n\n"+L("art. 321","Art. 321. Patrocinar, direta ou indiretamente","Violência arbitrária")+"""

A advocacia administrativa é patrocinar, direta ou indiretamente, interesse privado perante a administração pública, valendo-se da qualidade de funcionário. A pena é de detenção de um a três meses, ou multa, e, se o interesse é ilegítimo, de três meses a um ano, além da multa. É o servidor que “defende”, por meio do cargo, o interesse de um particular perante o próprio órgão.

"""+L("art. 322","Art. 322. Praticar violência","Abandono de função")+"""

A violência arbitrária é praticar violência no exercício de função ou a pretexto de exercê-la. A pena é de detenção de seis meses a três anos, além da pena correspondente à violência. É o crime do agente que, em serviço ou invocando a função, usa de força desnecessária ou ilegal. Para o guarda, a regra é de uso progressivo e proporcional da força, e o excesso pode configurar violência arbitrária, sem prejuízo da pena da lesão corporal que causar.
"""
S[2]="## 2. Abandono de função e exercício ilegal\n\n"+L("art. 323","Art. 323. Abandonar cargo público","Exercício funcional")+"\n\n"+L("art. 324","Art. 324. Entrar no exercício","Violação de sigilo funcional")+"""

O abandono de função é abandonar cargo público, fora dos casos permitidos em lei, com detenção de quinze dias a um mês, ou multa. Se resulta prejuízo público, a pena é de detenção de três meses a um ano e multa, e, se o fato ocorre em faixa de fronteira, de um a três anos e multa. O exercício funcional ilegalmente antecipado ou prolongado (art. 324) é entrar no exercício da função antes de satisfeitas as exigências legais, ou continuar a exercê-la, sem autorização, depois de saber oficialmente que foi exonerado, removido, substituído ou suspenso, com detenção de quinze dias a um mês, ou multa.
"""
S[3]="## 3. Sigilo funcional\n\n"+L("art. 325","Art. 325. Revelar fato","Violação do sigilo de proposta")+"\n\n"+L("art. 326","Art. 326. Devassar o sigilo","Funcionário público")+"""

A violação de sigilo funcional (art. 325) é revelar fato de que tem ciência em razão do cargo e que deva permanecer em segredo, ou facilitar a revelação. A pena é de detenção de seis meses a dois anos, ou multa, se o fato não constitui crime mais grave. Nas mesmas penas incorre quem permite ou facilita, mediante atribuição, fornecimento ou empréstimo de senha, o acesso de pessoas não autorizadas aos sistemas ou bancos de dados da Administração Pública, ou usa indevidamente o acesso restrito. Se da ação ou omissão resulta dano à Administração Pública ou a outrem, a reclusão é de dois a seis anos e multa. O empréstimo de senha, comum no serviço público, é crime.

A violação do sigilo de proposta de concorrência (art. 326) é devassar o sigilo de proposta de concorrência pública, ou proporcionar a terceiro o ensejo de devassá-lo, com detenção de três meses a um ano e multa.
"""
S[4]="## 4. Conceito de funcionário público\n\n"+L("art. 327, caput e § 1º","Art. 327. Considera-se funcionário público","§ 1º pela Lei")+"\n\n"+L("art. 327, § 2º","§ 2º A pena será aumentada","CAPÍTULO II")+"""

Para efeitos penais, funcionário público é quem exerce cargo, emprego ou função pública, ainda que transitoriamente ou sem remuneração. Esse conceito é mais amplo que o do direito administrativo: inclui o estagiário, o mesário, o jurado e o servidor temporário. Equipara-se a funcionário público quem exerce cargo, emprego ou função em entidade paraestatal e quem trabalha para empresa prestadora de serviço contratada ou conveniada para a execução de atividade típica da Administração Pública. O guarda municipal, ocupante de cargo público, é funcionário público para os efeitos penais.

A pena é aumentada de um terço quando os autores dos crimes deste capítulo forem ocupantes de cargos em comissão ou de função de direção ou assessoramento de órgão da administração direta, sociedade de economia mista, empresa pública ou fundação instituída pelo poder público. Quem manda tem mais dever de zelo.
"""
S[6]="""## 6. Na rotina do guarda

- **Uso da força:** a violência no exercício da função ou a pretexto dele é crime, com pena de detenção de seis meses a três anos, além da pena da lesão que causar.
- **Sigilo:** o guarda não revela o conteúdo de ocorrências sigilosas, e não empresta senha de sistema, sob pena de violação de sigilo funcional.
- **Abandono do posto:** deixar o cargo sem autorização, fora dos casos permitidos em lei, é abandono de função.
- **Quem é funcionário público:** o guarda, o estagiário e o prestador de serviço contratado para atividade típica da Administração respondem por esses crimes.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena da violência arbitrária | Detenção de seis meses a três anos, além da pena da violência |
| Pena do abandono de função | Detenção de quinze dias a um mês, ou multa |
| Abandono com prejuízo público | Detenção de três meses a um ano, e multa |
| Abandono em faixa de fronteira | Detenção de um a três anos, e multa |
| Violação de sigilo funcional | Detenção de seis meses a dois anos, ou multa |
| Empréstimo de senha | Mesmas penas da violação de sigilo funcional |
| Funcionário público para a lei penal | Quem exerce cargo, emprego ou função, ainda que transitoriamente ou sem remuneração |
| Aumento por cargo em comissão | Um terço |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Advocacia administrativa | Detenção, 1 a 3 meses, ou multa; ilegítimo: 3 meses a 1 ano |
| Violência arbitrária | Detenção, 6 meses a 3 anos, além da pena da violência |
| Abandono de função | Detenção, 15 dias a 1 mês, ou multa; prejuízo: 3 meses a 1 ano |
| Exercício funcional ilegal | Detenção, 15 dias a 1 mês, ou multa |
| Violação de sigilo funcional | Detenção, 6 meses a 2 anos, ou multa; dano: reclusão, 2 a 6 anos |
| Sigilo de proposta | Detenção, 3 meses a 1 ano, e multa |
| Funcionário público | Cargo, emprego ou função, mesmo transitório ou sem remuneração |
| Aumento | 1/3 para cargo em comissão, direção ou assessoramento |
"""
QR=[("Questão 1","A pena da violência arbitrária (art. 322) é de",["detenção, de seis meses a três anos, além da pena correspondente à violência.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],0,"Art. 322."),
("Questão 2","Para efeitos penais, considera-se funcionário público quem exerce cargo, emprego ou função pública",["embora transitoriamente ou sem remuneração.","apenas se remunerado.","apenas se concursado.","apenas se efetivo.","apenas se federal."],2,"Art. 327, caput."),
("Questão 3","A violação de sigilo funcional tem pena de",["detenção, de seis meses a dois anos, ou multa, se o fato não constitui crime mais grave.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],1,"Art. 325."),
("Questão 4","A pena dos crimes do capítulo é aumentada da terça parte quando os autores forem",["ocupantes de cargos em comissão ou de função de direção ou assessoramento.","servidores efetivos.","estagiários.","terceirizados.","aposentados."],4,"Art. 327, § 2º.")]
t1="<strong>Abordagem com excesso</strong><br><br>Durante uma abordagem em Vila Nova, cidade fictícia, um guarda municipal, irritado com um rapaz que o desafiou, o agrediu com socos, sem necessidade, e o rapaz sofreu lesão leve. Outro guarda registrou a cena."
t2="<strong>Senha emprestada</strong><br><br>Um servidor municipal emprestou sua senha de acesso ao sistema de dados da Prefeitura a um amigo que não tinha autorização, que consultou informações restritas. Dias depois, os dados vazaram, e houve prejuízo para a Administração."
tx={"cp15a":t1,"cp15b":t2}
# n=1
q(1,"A pena da violência arbitrária é de",["detenção, de seis meses a três anos, além da pena correspondente à violência.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],"Art. 322.")
q(1,"A violência arbitrária consiste em praticar violência no exercício de função ou",["a pretexto de exercê-la.","em casa.","na rua, sem relação com a função.","em férias.","em ambiente privado."],"Art. 322.")
q(1,"A advocacia administrativa consiste em patrocinar, direta ou indiretamente, interesse privado perante a administração pública, valendo-se da",["qualidade de funcionário.","amizade.","riqueza.","idade.","vizinhança."],"Art. 321.")
q(1,"A pena da advocacia administrativa é de",["detenção, de um a três meses, ou multa.","reclusão, de dois a doze anos.","detenção, de seis meses a três anos.","reclusão, de um a quatro anos.","multa."],"Art. 321.")
q(1,"Se o interesse patrocinado na advocacia administrativa é ilegítimo, a pena é de",["detenção, de três meses a um ano, além da multa.","reclusão, de dois a doze anos.","detenção, de um a três meses.","reclusão, de um a quatro anos.","multa."],"Art. 321, parágrafo único.")
q(1,"A pena do abandono de função é de",["detenção, de quinze dias a um mês, ou multa.","reclusão, de dois a doze anos.","detenção, de seis meses a três anos.","reclusão, de um a quatro anos.","multa, apenas."],"Art. 323, caput.")
q(1,"No abandono de função, se resulta prejuízo público, a pena é de",["detenção, de três meses a um ano, e multa.","detenção, de quinze dias a um mês.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","multa."],"Art. 323, § 1º.")
q(1,"No abandono de função, se o fato ocorre em lugar compreendido na faixa de fronteira, a pena é de",["detenção, de um a três anos, e multa.","detenção, de quinze dias a um mês.","detenção, de três meses a um ano.","reclusão, de dois a doze anos.","multa."],"Art. 323, § 2º.")
q(1,"Entrar no exercício de função pública antes de satisfeitas as exigências legais é crime com pena de",["detenção, de quinze dias a um mês, ou multa.","reclusão, de dois a doze anos.","detenção, de seis meses a três anos.","reclusão, de um a quatro anos.","multa, apenas."],"Art. 324.")
q(1,"Continuar a exercer a função, sem autorização, depois de saber oficialmente que foi exonerado, é crime do art.",["324.","321.","322.","323.","325."],"Art. 324.")
q(1,"A violação de sigilo funcional (art. 325) tem pena de",["detenção, de seis meses a dois anos, ou multa, se o fato não constitui crime mais grave.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa, apenas."],"Art. 325, caput.")
q(1,"Incorre nas mesmas penas da violação de sigilo funcional quem permite ou facilita, mediante empréstimo de senha, o acesso de pessoas não autorizadas a",["sistemas de informações ou banco de dados da Administração Pública.","sistemas privados.","redes sociais.","cadernos escolares.","bibliotecas."],"Art. 325, § 1º, I.")
q(1,"Se da violação de sigilo funcional resulta dano à Administração Pública ou a outrem, a pena é de",["reclusão, de dois a seis anos, e multa.","detenção, de seis meses a dois anos.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","multa."],"Art. 325, § 2º.")
q(1,"A violação do sigilo de proposta de concorrência tem pena de",["detenção, de três meses a um ano, e multa.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de quinze dias a um mês.","multa."],"Art. 326.")
q(1,"Para efeitos penais, considera-se funcionário público quem exerce cargo, emprego ou função pública, embora",["transitoriamente ou sem remuneração.","apenas se remunerado.","apenas se concursado.","apenas se efetivo.","apenas se federal."],"Art. 327, caput.")
q(1,"Equipara-se a funcionário público quem exerce cargo, emprego ou função em",["entidade paraestatal.","empresa privada comum.","associação de bairro.","condomínio.","clube."],"Art. 327, § 1º.")
q(1,"Equipara-se a funcionário público quem trabalha para empresa prestadora de serviço contratada ou conveniada para a execução de",["atividade típica da Administração Pública.","qualquer atividade.","atividade privada.","atividade doméstica.","atividade agrícola."],"Art. 327, § 1º.")
q(1,"A pena é aumentada da terça parte quando os autores dos crimes do capítulo forem",["ocupantes de cargos em comissão ou de função de direção ou assessoramento.","servidores efetivos.","estagiários.","terceirizados.","aposentados."],"Art. 327, § 2º.")
q(1,"No texto da abordagem, o guarda que agrediu o rapaz sem necessidade, no exercício da função, comete, em tese,",["violência arbitrária, além da pena da lesão.","prevaricação.","peculato.","concussão.","corrupção passiva."],"Art. 322.","cp15a")
q(1,"No texto da senha emprestada, o servidor que emprestou a senha comete, em tese,",["violação de sigilo funcional.","peculato.","corrupção passiva.","concussão.","prevaricação."],"Art. 325, § 1º, I.","cp15b")
# n=2
q(2,"A advocacia administrativa exige que o funcionário se valha de sua qualidade para patrocinar interesse privado perante",["a administração pública.","a Justiça.","a imprensa.","o cliente.","o vizinho."],"Art. 321.")
q(2,"Na violência arbitrária, a pena da violência",["é somada à pena do art. 322.","substitui a pena do art. 322.","é reduzida.","não se aplica.","é de multa."],"Art. 322: “além da pena correspondente à violência”.")
q(2,"O abandono de função se configura quando o funcionário abandona o cargo",["fora dos casos permitidos em lei.","para férias.","para licença.","para tratamento de saúde.","por ordem superior."],"Art. 323, caput.")
q(2,"O exercício funcional ilegalmente antecipado se dá quando o agente entra em exercício antes de",["satisfeitas as exigências legais.","tomar posse apenas.","obter aprovação.","ser nomeado.","assinar contrato."],"Art. 324.")
q(2,"O exercício funcional ilegalmente prolongado se dá quando o agente continua a exercer a função, sem autorização, depois de saber oficialmente que foi",["exonerado, removido, substituído ou suspenso.","promovido.","transferido a pedido.","elogiado.","aposentado."],"Art. 324.")
q(2,"Na violação de sigilo funcional, o agente revela fato de que tem ciência em razão do cargo e que deva permanecer",["em segredo.","público.","em evidência.","em debate.","em consulta."],"Art. 325, caput.")
q(2,"A violação de sigilo funcional tem pena de detenção de seis meses a dois anos, ou multa, se o fato",["não constitui crime mais grave.","for de pouca importância.","for sigiloso.","for público.","for notório."],"Art. 325, caput.")
q(2,"Incorre nas mesmas penas do art. 325 quem",["se utiliza, indevidamente, do acesso restrito.","guarda senha.","lê documento público.","faz cópia de documento público.","consulta processo aberto."],"Art. 325, § 1º, II.")
q(2,"O art. 326 pune quem devassa o sigilo de proposta de",["concorrência pública.","venda particular.","contrato de locação.","testamento.","carta."],"Art. 326.")
q(2,"Para efeitos penais, o estagiário, que exerce função pública, é",["funcionário público, pois o conceito alcança quem exerce função, ainda que transitoriamente.","não funcionário público.","funcionário público somente se concursado.","funcionário público somente se remunerado.","terceiro."],"Art. 327, caput.")
q(2,"O funcionário público, para a lei penal, pode exercer o cargo",["sem remuneração.","apenas com remuneração.","apenas por concurso.","apenas por período indeterminado.","apenas por mandato."],"Art. 327, caput.")
q(2,"O aumento de um terço do § 2º do art. 327 aplica-se aos ocupantes de",["cargos em comissão ou de função de direção ou assessoramento de órgão da administração direta, sociedade de economia mista, empresa pública ou fundação instituída pelo poder público.","qualquer cargo.","cargos de carreira apenas.","cargos efetivos apenas.","cargos de estagiário."],"Art. 327, § 2º.")
q(2,"A pena do exercício funcional ilegalmente antecipado ou prolongado é de",["detenção, de quinze dias a um mês, ou multa.","reclusão, de dois a doze anos.","detenção, de seis meses a três anos.","reclusão, de um a quatro anos.","multa."],"Art. 324.")
q(2,"A violação do sigilo funcional que resulta dano à Administração tem pena de reclusão de",["dois a seis anos, e multa.","um a quatro anos.","seis meses a dois anos.","três meses a um ano.","dois a doze anos."],"Art. 325, § 2º.")
q(2,"A pena do abandono de função pode chegar a detenção de um a três anos se o fato ocorre em",["faixa de fronteira.","cidade grande.","zona rural.","zona urbana.","litoral."],"Art. 323, § 2º.")
q(2,"No texto da abordagem, a pena do crime de violência arbitrária é de",["detenção, de seis meses a três anos, além da pena da violência.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","multa."],"Art. 322.","cp15a")
q(2,"No texto da abordagem, a lesão leve causada ao rapaz, além do art. 322, gera a pena do art.",["129.","121.","155.","157.","158."],"Art. 322: além da pena correspondente à violência (art. 129).","cp15a")
q(2,"No texto da senha emprestada, o dano para a Administração faz incidir, no art. 325, a pena de",["reclusão, de dois a seis anos, e multa.","detenção, de seis meses a dois anos.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","multa."],"Art. 325, § 2º.","cp15b")
q(2,"A pena mínima da violência arbitrária é de",["seis meses de detenção.","um ano de reclusão.","três meses de detenção.","quinze dias de detenção.","dois anos de reclusão."],"Art. 322.")
q(2,"A violação do sigilo de proposta de concorrência pública tem pena mínima de",["três meses de detenção.","seis meses de detenção.","um ano de reclusão.","quinze dias de detenção.","dois anos de reclusão."],"Art. 326.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Violência arbitrária: detenção de seis meses a três anos; abandono de função: detenção de quinze dias a um mês, ou multa; sigilo funcional: detenção de seis meses a dois anos, ou multa.","Violência arbitrária: multa; abandono: reclusão.","Sigilo funcional: reclusão de dois a doze anos.","Abandono de função: reclusão de um a quatro anos.","Advocacia administrativa: reclusão de dois a doze anos."],"Arts. 322, 323 e 325.")
q(3,"Considere as afirmações. I. O guarda municipal é funcionário público para efeitos penais. II. A violência arbitrária tem pena de detenção, além da pena da violência. III. O empréstimo de senha de sistema da Administração é conduta penalmente irrelevante. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"O empréstimo de senha é crime (art. 325, § 1º, I).")
q(3,"Assinale a INCORRETA.",["O conceito de funcionário público, para a lei penal, exige remuneração.","O art. 327, § 1º, equipara a funcionário público quem exerce função em entidade paraestatal.","O art. 327, § 2º, aumenta a pena em um terço para cargos em comissão e de direção.","A violência arbitrária tem pena de detenção de seis meses a três anos.","O abandono de função com prejuízo público tem pena de detenção de três meses a um ano e multa."],"Art. 327, caput: “embora transitoriamente ou sem remuneração”.")
q(3,"No art. 322, o termo “a pretexto de exercê-la” significa que o crime ocorre também quando o agente",["invoca a função para justificar a violência, sem que o ato esteja no exercício regular.","age em férias.","age em casa.","age por ordem do chefe.","age em legítima defesa."],"Art. 322.")
q(3,"A diferença entre a violência arbitrária e o crime de lesão corporal é que a violência arbitrária",["exige que a violência seja praticada no exercício ou a pretexto de função pública.","exige lesão grave.","exige dolo de matar.","exige arma.","exige reincidência."],"Arts. 129 e 322.")
q(3,"A advocacia administrativa ilegítima, do parágrafo único do art. 321, tem pena de detenção de",["três meses a um ano, além da multa.","um a três meses.","seis meses a três anos.","quinze dias a um mês.","dois a seis anos."],"Art. 321, parágrafo único.")
q(3,"A violação de sigilo funcional do art. 325, caput, é crime subsidiário porque se aplica",["se o fato não constitui crime mais grave.","em qualquer caso.","apenas com dano.","apenas com lucro.","apenas com dolo."],"Art. 325, caput.")
q(3,"O conceito de funcionário público do art. 327 é utilizado para efeitos",["penais.","apenas administrativos.","apenas trabalhistas.","apenas tributários.","apenas civis."],"Art. 327, caput.")
q(3,"O terceirizado de empresa contratada para a execução de atividade típica da Administração Pública",["equipara-se a funcionário público.","é funcionário público.","é particular, sem equiparação.","é isento de crimes funcionais.","não responde por crimes funcionais."],"Art. 327, § 1º.")
q(3,"No art. 323, a expressão “fora dos casos permitidos em lei” indica que o abandono de cargo",["é lícito em casos como licença e férias.","é sempre crime.","é sempre lícito.","depende de decisão do chefe.","depende de ordem verbal."],"Art. 323, caput.")
q(3,"A pena do abandono de função com prejuízo público é de detenção de três meses a um ano e multa, mais severa que a do caput porque",["há prejuízo público.","há violência.","há fraude.","há ameaça.","há arma."],"Art. 323, § 1º.")
q(3,"A violação de sigilo de proposta de concorrência exige que o agente devasse o sigilo ou proporcione a terceiro o ensejo de",["devassá-lo.","consultá-lo.","copiá-lo.","fotografá-lo.","guardá-lo."],"Art. 326.")
q(3,"O funcionário que continua a exercer a função depois de saber oficialmente que foi exonerado comete o crime do art.",["324.","323.","322.","321.","325."],"Art. 324.")
q(3,"Em relação ao aumento do art. 327, § 2º, o fundamento é o de que quem ocupa cargo em comissão ou de direção tem",["maior dever de zelo.","menor dever de zelo.","mais tempo.","mais dinheiro.","mais idade."],"Art. 327, § 2º.")
q(3,"Assinale a alternativa correta sobre o art. 327.",["Funcionário público, para os efeitos penais, é quem exerce cargo, emprego ou função pública, embora transitoriamente ou sem remuneração.","Só é funcionário público quem é concursado.","Só é funcionário público quem é efetivo.","Só é funcionário público quem é remunerado.","Só é funcionário público quem é federal."],"Art. 327, caput.")
q(3,"Assinale a alternativa que associa corretamente o artigo ao crime.",["321: advocacia administrativa; 322: violência arbitrária; 323: abandono de função; 324: exercício funcional ilegal; 325: sigilo funcional; 326: sigilo de proposta.","321: violência arbitrária; 322: advocacia administrativa.","323: sigilo; 325: abandono.","324: violência; 326: exercício.","327: sigilo; 325: conceito."],"Arts. 321 a 327.")
q(3,"No art. 325, o empréstimo de senha de acesso a sistemas da Administração Pública, mediante atribuição, fornecimento ou empréstimo, caracteriza conduta",["equiparada, em pena, à violação de sigilo funcional do caput.","atípica.","contravencional.","de menor gravidade, sem pena.","punida apenas administrativamente."],"Art. 325, § 1º, I.")
q(3,"No texto da abordagem, o outro guarda que registrou a cena, nesses termos, atuou como",["testemunha, e seu relato poderá fundamentar a apuração da violência arbitrária.","autor da violência.","vítima.","partícipe.","juiz."],"Art. 322.","cp15a")
q(3,"No texto da senha emprestada, o amigo, que consultou informações restritas sem autorização, utilizou-se, em tese,",["indevidamente do acesso restrito, nos termos do art. 325, § 1º, II.","de acesso lícito.","de acesso público.","de acesso livre.","de acesso concedido por lei."],"Art. 325, § 1º, II.","cp15b")
q(3,"No texto da senha emprestada, o dano à Administração Pública eleva a pena do art. 325 para",["reclusão, de dois a seis anos, e multa.","detenção, de seis meses a dois anos.","detenção, de três meses a um ano.","reclusão, de dois a doze anos.","multa."],"Art. 325, § 2º.","cp15b")
assert len(Q)==60,len(Q)
code,svg=mapa("Demais crimes funcionais e conceito de funcionário público",[
 ("adv","Advocacia administrativa",["art. 321","patrocinar interesse privado","detenção, 1 a 3 meses"],"seção 1"),
 ("viol","Violência arbitrária",["art. 322","detenção, 6 meses a 3 anos","além da pena da violência"],"seção 1"),
 ("aband","Abandono de função",["art. 323","detenção, 15 dias a 1 mês","fronteira: 1 a 3 anos"],"seção 2"),
 ("exerc","Exercício ilegal",["art. 324","antecipado ou prolongado","detenção, 15 dias a 1 mês"],"seção 2"),
 ("sig","Sigilo",["325: detenção, 6 meses a 2 anos","senha emprestada","326: proposta de concorrência"],"seção 3"),
 ("func","Funcionário público",["art. 327","mesmo transitório ou sem remuneração","aumento de 1/3 para comissão e direção"],"seção 4")],
 "Na prova: o conceito penal de funcionário público é amplo e inclui quem não é remunerado")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As três primeiras caixas reúnem os crimes do próprio cargo; a última define quem responde por eles.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 321 a 327, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-15","Demais crimes funcionais e conceito de funcionário público (CP, arts. 321 a 327)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 321 a 327. Cobertos todos."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","No art. 327, a consolidação apresenta resíduo de nota de alteração depois do § 1º; o trecho foi excluído da citação.","A citação do estagiário, do mesário e do jurado como funcionários públicos para efeitos penais é entendimento doutrinário, não consta do texto do art. 327.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp15a e cp15b fictícios."],
 fontes_conferidas=["CP, arts. 321 a 327: texto da Câmara, copiado por programa."])
gravar("cp-15",aula_html,banco("cp-15",Q),tx)
