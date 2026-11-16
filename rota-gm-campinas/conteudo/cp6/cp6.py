import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A inviolabilidade do domicílio, da correspondência e dos segredos protege a intimidade. A Vunesp cobra os arts. 150 a 154-B pelo que é crime e pelo que não é: a violação de domicílio e as hipóteses em que a entrada em casa alheia é permitida, o conceito de casa, a violação de correspondência, a divulgação de segredo e a invasão de dispositivo informático. Para o guarda, o ponto mais importante é a entrada em casa alheia, porque a lei diz quando o agente pode entrar sem cometer crime."
S={}
S[1]="## 1. Violação de domicílio\n\n"+L("art. 150, caput e § 1º","Art. 150. Entrar ou permanecer","§ 2º [revogado]")+"""

A violação de domicílio é entrar ou permanecer, clandestina ou astuciosamente, ou contra a vontade expressa ou tácita de quem de direito, em casa alheia ou em suas dependências. A pena é de detenção de um a três meses, ou multa. Observe os dois verbos: o crime existe tanto para quem entra como para quem permanece depois de mandado sair. E o texto fala em “vontade expressa ou tácita”: o morador pode dizer que não quer ou demonstrar com um portão trancado. A forma qualificada tem detenção de seis meses a dois anos, além da pena da violência, se o crime é cometido à noite, em lugar ermo, com violência ou arma, ou por duas ou mais pessoas.

"""+L("art. 150, § 3º","§ 3º Não constitui crime a entrada","§ 4º A expressão")+"""

O § 3º é o dispositivo que mais interessa ao agente de segurança. Não é crime entrar em casa alheia durante o dia, com observância das formalidades legais, para efetuar prisão ou outra diligência. E não é crime entrar a qualquer hora do dia ou da noite quando algum crime está sendo praticado ali, ou está na iminência de ser. Em flagrante delito, portanto, o agente entra a qualquer hora, sem mandado.
"""
S[2]="## 2. O conceito de casa\n\n"+L("art. 150, §§ 4º e 5º","§ 4º A expressão","Seção III")+"""

A palavra “casa” tem sentido amplo: abrange qualquer compartimento habitado, o aposento ocupado de habitação coletiva (o quarto de pensão ou de hotel) e o compartimento não aberto ao público onde alguém exerce profissão ou atividade, como o escritório e o consultório. O § 5º diz o que não é casa: a hospedaria, estalagem ou outra habitação coletiva, enquanto aberta (as áreas comuns), ressalvado o quarto ocupado, a taverna, a casa de jogo e outras do mesmo gênero. Daí que o estabelecimento aberto ao público, enquanto aberto, não é domicílio para esse fim.
"""
S[3]="## 3. Correspondência e comunicações\n\n"+L("art. 151","Art. 151. Devassar indevidamente","Correspondência comercial")+"\n\n"+L("art. 152","Art. 152. Abusar da condição de sócio","Seção IV")+"""

Devassar indevidamente o conteúdo de correspondência fechada dirigida a outrem é violação de correspondência, com detenção de um a seis meses, ou multa. Na mesma pena incorre quem se apossa de correspondência alheia, ainda que aberta, e a sonega ou destrói, quem divulga, transmite ou usa abusivamente comunicação telegráfica ou radioelétrica dirigida a terceiro, ou conversação telefônica entre outras pessoas, quem impede essa comunicação e quem instala ou utiliza estação ou aparelho radioelétrico sem observar a lei. As penas aumentam de metade se há dano a outrem. Se o agente age com abuso de função em serviço postal, telegráfico, radioelétrico ou telefônico, a pena é de detenção de um a três anos. Em regra, procede-se mediante representação, salvo no caso do aparelho radioelétrico e do abuso de função.

O art. 152 pune, com detenção de três meses a dois anos, quem abusa da condição de sócio ou empregado de estabelecimento comercial ou industrial para desviar, sonegar, subtrair ou suprimir correspondência ou revelar o conteúdo a estranho, e só se procede mediante representação.
"""
S[4]="## 4. Segredos e invasão de dispositivo\n\n"+L("art. 153, caput","Art. 153. Divulgar alguém","§ 1º Somente se procede")+"\n\n"+L("art. 153, § 1º-A e § 2º","§ 1º-A. Divulgar, sem justa causa","Violação do segredo profissional")+"\n\n"+L("art. 154","Art. 154. Revelar alguém","Invasão de dispositivo informático")+"""

Divulgar, sem justa causa, o conteúdo de documento particular ou de correspondência confidencial de que se é destinatário ou detentor, se a divulgação pode produzir dano a outrem, é divulgação de segredo, com detenção de um a seis meses, ou multa, e ação penal mediante representação. Quando se divulgam sem justa causa informações sigilosas ou reservadas, assim definidas em lei, contidas nos sistemas ou bancos de dados da Administração Pública, a pena é de detenção de um a quatro anos e multa, e, quando resulta prejuízo para a Administração, a ação é incondicionada. A violação do segredo profissional (art. 154) é revelar, sem justa causa, segredo de que se tem ciência em razão de função, ministério, ofício ou profissão, com dano potencial a outrem, com detenção de três meses a um ano, ou multa, e ação por representação.

"""+L("art. 154-A, caput e § 1º","Art. 154-A. Invadir dispositivo informático","§ 2º Aumenta-se a pena de 1/3")+"\n\n"+L("art. 154-A, §§ 2º a 5º","§ 2º Aumenta-se a pena de 1/3","Ação penal")+"\n\n"+L("art. 154-B","Art. 154-B. Nos crimes definidos","TÍTULO II")+"""

Invadir dispositivo informático de uso alheio, conectado ou não à rede, com o fim de obter, adulterar ou destruir dados sem autorização, ou de instalar vulnerabilidades para obter vantagem ilícita, é crime de reclusão de um a quatro anos e multa. Incorre na mesma pena quem produz, oferece, distribui, vende ou difunde programa com o intuito de permitir a invasão. A pena aumenta de um terço a dois terços se há prejuízo econômico, e passa a reclusão de dois a cinco anos se a invasão resulta na obtenção de conteúdo de comunicações privadas, segredos comerciais ou industriais, informações sigilosas ou controle remoto do dispositivo. Há aumento de um terço à metade se o crime é contra o Presidente da República, governadores, prefeitos e outras autoridades do § 5º. A ação é, em regra, pública condicionada à representação, salvo se contra a administração pública ou empresas concessionárias de serviços públicos (art. 154-B).
"""
S[6]="""## 6. Na rotina do guarda

- **Entrada em casa alheia:** só sem violar o domicílio se há flagrante delito (a qualquer hora), consentimento do morador ou, de dia, ordem judicial e as formalidades legais.
- **Estabelecimento aberto:** enquanto aberto ao público, a entrada para fiscalização não é violação de domicílio, pelo § 5º, II, e pelo § 4º, III, do art. 150.
- **Sigilo funcional:** o guarda que divulga informações sigilosas da Administração pode responder pelo art. 153, § 1º-A, e o que revela segredo de que tem ciência em razão da função, pelo art. 154.
- **Celulares e dispositivos:** acessar o celular de preso ou de vítima sem autorização tem de seguir a lei; a invasão de dispositivo é crime.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena da violação de domicílio | Detenção de um a três meses, ou multa |
| Qualificadora do art. 150, § 1º | Noite, lugar ermo, violência, arma ou duas ou mais pessoas: detenção de seis meses a dois anos |
| Entrada à noite com flagrante | A qualquer hora, se há crime acontecendo ou na iminência de acontecer |
| Entrada sem flagrante | Só durante o dia, com as formalidades legais |
| Estabelecimento aberto ao público | Enquanto aberto, não é casa |
| Pena da violação de correspondência | Detenção de um a seis meses, ou multa |
| Pena do segredo profissional | Detenção de três meses a um ano, ou multa |
| Pena da invasão de dispositivo | Reclusão de um a quatro anos, e multa |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Violação de domicílio | Detenção, 1 a 3 meses, ou multa; qualificada: 6 meses a 2 anos |
| Entrada permitida | Flagrante a qualquer hora; diligência de dia com formalidades |
| Casa | Compartimento habitado; quarto de habitação coletiva; local de profissão não aberto ao público |
| Não é casa | Hospedaria aberta; taverna; casa de jogo |
| Violação de correspondência | Detenção, 1 a 6 meses, ou multa |
| Abuso de função em serviço postal | Detenção, 1 a 3 anos |
| Divulgação de segredo | Detenção, 1 a 6 meses, ou multa |
| Segredo profissional | Detenção, 3 meses a 1 ano, ou multa |
| Invasão de dispositivo | Reclusão, 1 a 4 anos, e multa |
"""
QR=[("Questão 1","A violação de domicílio, no caput do art. 150, é punida com",["detenção, de um a três meses, ou multa.","detenção, de seis meses a dois anos.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","multa, apenas."],0,"Art. 150, caput."),
("Questão 2","Não constitui crime a entrada em casa alheia, a qualquer hora do dia ou da noite, quando",["algum crime está sendo ali praticado ou na iminência de o ser.","o morador está ausente.","há suspeita de crime.","há ordem verbal do delegado.","o morador não atende."],3,"Art. 150, § 3º, II."),
("Questão 3","A expressão “casa”, para fins do art. 150, compreende",["qualquer compartimento habitado e o compartimento não aberto ao público onde alguém exerce profissão ou atividade.","apenas a residência fixa.","apenas imóveis registrados.","apenas imóveis próprios.","qualquer estabelecimento comercial aberto."],1,"Art. 150, § 4º."),
("Questão 4","A invasão de dispositivo informático, no caput do art. 154-A, é punida com",["reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","reclusão, de dois a cinco anos.","detenção, de um a seis meses.","multa, apenas."],4,"Art. 154-A.")]
t1="<strong>Entrada em residência durante uma ocorrência</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, ouviu gritos vindos de uma casa e, pela janela, viu um homem agredindo uma mulher. Os guardas entraram na casa, à noite, sem mandado, e contiveram o agressor. O proprietário depois reclamou da entrada."
t2="<strong>Vazamento de dados</strong><br><br>Um servidor municipal, sem justa causa, divulgou em redes sociais informações sigilosas contidas no banco de dados da Prefeitura, definidas em lei como reservadas. A divulgação causou prejuízo à Administração."
tx={"cp6a":t1,"cp6b":t2}
# n=1
q(1,"A pena da violação de domicílio (art. 150, caput) é de",["detenção, de um a três meses, ou multa.","detenção, de seis meses a dois anos.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","multa, apenas."],"Art. 150, caput.")
q(1,"O art. 150 pune quem entra ou permanece em casa alheia",["clandestina ou astuciosamente, ou contra a vontade expressa ou tácita de quem de direito.","apenas à noite.","apenas com violência.","apenas armado.","apenas com autorização."],"Art. 150, caput.")
q(1,"A forma qualificada da violação de domicílio tem pena de",["detenção, de seis meses a dois anos, além da pena correspondente à violência.","detenção, de um a três meses.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","reclusão, de dois a cinco anos."],"Art. 150, § 1º.")
q(1,"Qualifica a violação de domicílio o crime cometido",["durante a noite, ou em lugar ermo, ou com emprego de violência ou de arma, ou por duas ou mais pessoas.","durante o dia.","por uma só pessoa.","sem violência.","com a anuência do morador."],"Art. 150, § 1º.")
q(1,"Não constitui crime a entrada em casa alheia, durante o dia, com observância das formalidades legais, para",["efetuar prisão ou outra diligência.","fazer vistoria sem ordem.","buscar objetos.","conversar com o morador.","procurar emprego."],"Art. 150, § 3º, I.")
q(1,"Não constitui crime a entrada em casa alheia, a qualquer hora, quando algum crime",["está sendo ali praticado ou na iminência de o ser.","foi praticado há um mês.","é suspeitado, sem indício.","foi denunciado por escrito.","já está prescrito."],"Art. 150, § 3º, II.")
q(1,"Para o art. 150, a expressão “casa” compreende",["qualquer compartimento habitado.","apenas casa de alvenaria.","apenas casas próprias.","apenas casas registradas.","apenas apartamentos."],"Art. 150, § 4º, I.")
q(1,"A expressão “casa” compreende também",["aposento ocupado de habitação coletiva.","taverna.","casa de jogo.","hospedaria aberta.","estalagem aberta."],"Art. 150, § 4º, II.")
q(1,"A expressão “casa” compreende também o compartimento",["não aberto ao público, onde alguém exerce profissão ou atividade.","aberto ao público.","de uso comum.","de repartição pública, em qualquer caso.","de lazer."],"Art. 150, § 4º, III.")
q(1,"Não se compreendem na expressão “casa”",["taverna, casa de jogo e outras do mesmo gênero.","o quarto de hotel ocupado.","o escritório particular.","o consultório fechado.","o apartamento."],"Art. 150, § 5º, II.")
q(1,"A pena da violação de correspondência (art. 151) é de",["detenção, de um a seis meses, ou multa.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","multa, apenas."],"Art. 151, caput.")
q(1,"Devassar indevidamente o conteúdo de correspondência fechada, dirigida a outrem, é crime de",["violação de correspondência.","divulgação de segredo.","invasão de dispositivo informático.","violação de domicílio.","segredo profissional."],"Art. 151, caput.")
q(1,"Se o agente comete a violação de correspondência com abuso de função em serviço postal, a pena é de",["detenção, de um a três anos.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa.","detenção, de seis meses a dois anos."],"Art. 151, § 3º.")
q(1,"A pena da divulgação de segredo (art. 153, caput) é de",["detenção, de um a seis meses, ou multa.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","detenção, de um a quatro anos.","multa, apenas."],"Art. 153, caput.")
q(1,"A pena da violação do segredo profissional (art. 154) é de",["detenção, de três meses a um ano, ou multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","multa, apenas."],"Art. 154, caput.")
q(1,"Invadir dispositivo informático de uso alheio, para obter dados sem autorização, tem pena de",["reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","detenção, de um a seis meses.","reclusão, de dois a cinco anos.","multa."],"Art. 154-A, caput.")
q(1,"A invasão de dispositivo informático pode ocorrer em dispositivo",["conectado ou não à rede de computadores.","apenas conectado.","apenas desconectado.","apenas de empresa.","apenas público."],"Art. 154-A, caput.")
q(1,"No texto da entrada em residência, a entrada dos guardas, à noite, para conter agressor,",["não constitui crime, pois um crime estava sendo ali praticado.","é crime, pois não havia mandado.","só seria lícita de dia.","exigia ordem do juiz.","exigia consentimento por escrito."],"Art. 150, § 3º, II.","cp6a")
q(1,"No texto do vazamento de dados, o servidor, em tese, cometeu",["divulgação de informações sigilosas da Administração Pública.","violação de domicílio.","violação de correspondência.","segredo profissional.","invasão de dispositivo."],"Art. 153, § 1º-A.","cp6b")
q(1,"Na divulgação de segredo (art. 153, caput), procede-se mediante",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 153, § 1º.")
# n=2
q(2,"Em regra, o crime de violação de correspondência se procede mediante",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 151, § 4º.")
q(2,"Na violação de correspondência, as penas aumentam-se de metade se há",["dano para outrem.","reincidência.","violência.","arma.","dois agentes."],"Art. 151, § 2º.")
q(2,"Na mesma pena da violação de correspondência incorre quem",["se apossa indevidamente de correspondência alheia, embora não fechada, e a sonega ou destrói.","entrega a correspondência ao destinatário.","guarda a correspondência para o destinatário.","devolve ao remetente com autorização.","lê o próprio correio."],"Art. 151, § 1º, I.")
q(2,"No art. 152, a correspondência comercial é desviada por quem abusa da condição de",["sócio ou empregado de estabelecimento comercial ou industrial.","cliente.","fornecedor.","vizinho.","entregador."],"Art. 152, caput.")
q(2,"A pena do art. 152 (correspondência comercial) é de",["detenção, de três meses a dois anos.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","multa."],"Art. 152, caput.")
q(2,"Na divulgação de segredo, o crime exige que a divulgação possa produzir",["dano a outrem.","lucro ao agente.","prazer ao agente.","benefício à vítima.","reconhecimento público."],"Art. 153, caput.")
q(2,"Divulgar, sem justa causa, informações sigilosas ou reservadas, assim definidas em lei, contidas nos sistemas da Administração Pública, tem pena de",["detenção, de um a quatro anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","multa."],"Art. 153, § 1º-A.")
q(2,"Quando da divulgação resulta prejuízo para a Administração Pública, a ação penal, no art. 153, é",["incondicionada.","por queixa.","por representação.","por requisição do Ministro da Justiça.","por requisição do juiz."],"Art. 153, § 2º.")
q(2,"No art. 154, a revelação de segredo é punível se o segredo é conhecido em razão de",["função, ministério, ofício ou profissão.","convivência social.","amizade.","vizinhança.","parentesco."],"Art. 154, caput.")
q(2,"A ação penal no crime de violação do segredo profissional depende de",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 154, parágrafo único.")
q(2,"Na invasão de dispositivo informático, a pena aumenta de um terço a dois terços se da invasão resulta",["prejuízo econômico.","prejuízo moral.","nenhum prejuízo.","demora.","apenas inconveniência."],"Art. 154-A, § 2º.")
q(2,"Se da invasão resulta a obtenção de conteúdo de comunicações eletrônicas privadas, a pena é de",["reclusão, de dois a cinco anos, e multa.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","detenção, de um a seis meses.","reclusão, de seis a oito anos."],"Art. 154-A, § 3º.")
q(2,"Nos crimes do art. 154-A, procede-se, em regra, mediante",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 154-B.")
q(2,"A regra de representação do art. 154-B não se aplica se o crime é cometido contra",["a administração pública direta ou indireta de qualquer dos Poderes ou empresas concessionárias de serviços públicos.","pessoa física.","empresa privada, em geral.","associação.","profissional liberal."],"Art. 154-B.")
q(2,"Incorre na mesma pena da invasão de dispositivo quem",["produz, oferece, distribui, vende ou difunde programa com o intuito de permitir a prática da invasão.","usa o próprio dispositivo.","atualiza programa.","faz cópia de segurança.","instala antivírus."],"Art. 154-A, § 1º.")
q(2,"No texto da entrada em residência, a entrada sem mandado foi possível porque",["havia flagrante delito, ou seja, crime sendo praticado.","o proprietário autorizou.","havia ordem do delegado.","era dia.","havia ordem do prefeito."],"Art. 150, § 3º, II.","cp6a")
q(2,"No texto da entrada em residência, o fato de a entrada ter ocorrido à noite",["não afasta a licitude, pois a entrada em flagrante pode ser a qualquer hora.","afasta a licitude.","exige mandado.","agrava a pena do guarda.","é irrelevante."],"Art. 150, § 3º, II: “a qualquer hora do dia ou da noite”.","cp6a")
q(2,"No texto do vazamento de dados, a divulgação causou prejuízo à Administração. Nessa hipótese, a ação penal é",["incondicionada.","por queixa.","por representação.","por requisição do Ministro da Justiça.","por requisição do juiz."],"Art. 153, § 2º.","cp6b")
q(2,"A divulgação de segredo do art. 153, caput, refere-se ao conteúdo de documento particular ou de correspondência confidencial de que o agente é",["destinatário ou detentor.","apenas destinatário.","apenas remetente.","terceiro estranho.","funcionário dos Correios."],"Art. 153, caput.")
q(2,"Na violação de comunicação, incorre na pena do art. 151 quem indevidamente",["divulga, transmite a outrem ou utiliza abusivamente conversação telefônica entre outras pessoas.","atende o telefone.","faz ligação.","grava a própria conversa.","recebe mensagem."],"Art. 151, § 1º, II.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Violação de domicílio: detenção de um a três meses, ou multa; violação de correspondência: detenção de um a seis meses, ou multa; invasão de dispositivo: reclusão de um a quatro anos e multa.","Violação de domicílio: reclusão de um a três anos; correspondência: detenção; invasão: multa.","Domicílio: multa; correspondência: reclusão; invasão: detenção.","Domicílio: reclusão; correspondência: multa; invasão: detenção de um a seis meses.","Domicílio: detenção de um a quatro anos; correspondência: reclusão de um a quatro anos."],"Arts. 150, 151 e 154-A.")
q(3,"Considere as afirmações. I. A entrada em casa alheia, de dia, com observância das formalidades legais, para efetuar prisão não é crime. II. A entrada em casa alheia, à noite, quando um crime está sendo praticado, não é crime. III. A entrada em casa alheia, à noite, sem crime e sem consentimento, é permitida para qualquer diligência. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"Art. 150, § 3º: sem flagrante, a diligência só de dia, com formalidades.")
q(3,"Assinale a INCORRETA.",["A hospedaria aberta é sempre casa, inclusive nas áreas comuns.","O aposento ocupado de habitação coletiva é casa.","O escritório particular, não aberto ao público, é casa.","A taverna não é casa.","A casa de jogo não é casa."],"O § 5º, I, exclui a hospedaria aberta, ressalvado o aposento ocupado.")
q(3,"A violação de domicílio qualificada exige, entre outras hipóteses, que o crime seja cometido",["por duas ou mais pessoas.","por uma pessoa só.","com o consentimento do morador.","de dia, sem violência.","em casa abandonada."],"Art. 150, § 1º.")
q(3,"A pena da violação de domicílio qualificada é aplicada",["além da pena correspondente à violência.","em lugar da pena da violência.","somente se houver arma.","somente se não houver violência.","reduzida pela metade."],"Art. 150, § 1º.")
q(3,"As penas da violação de correspondência aumentam-se de metade se há dano para outrem. Nesse caso, o aumento incide sobre",["a pena do art. 151, caput e § 1º.","a pena do art. 152.","a pena do art. 153.","a pena do art. 154.","a pena do art. 154-A."],"Art. 151, § 2º.")
q(3,"Nos termos do art. 151, § 4º, somente se procede mediante representação, salvo nos casos",["do § 1º, IV, e do § 3º.","do caput.","do § 2º.","de qualquer parágrafo.","do § 1º, I."],"Art. 151, § 4º.")
q(3,"Assinale a alternativa que descreve corretamente o art. 154 do Código Penal.",["Revelar, sem justa causa, segredo de que se tem ciência em razão de função, ministério, ofício ou profissão, e cuja revelação possa produzir dano a outrem.","Revelar qualquer segredo.","Revelar segredo de família.","Revelar segredo de amigo.","Revelar segredo por justa causa."],"Art. 154, caput.")
q(3,"No art. 153, § 1º-A, a divulgação de informações sigilosas ou reservadas tem como elemento",["a ausência de justa causa.","a autorização do chefe.","a necessidade do serviço.","o consentimento do interessado.","a obediência a ordem."],"Art. 153, § 1º-A.")
q(3,"A pena da invasão de dispositivo é aumentada de um terço à metade se o crime é praticado contra",["Presidente da República, governadores e prefeitos, entre outras autoridades do § 5º.","qualquer cidadão.","qualquer servidor.","qualquer empresa.","qualquer estudante."],"Art. 154-A, § 5º.")
q(3,"A pena do art. 154-A, § 4º, é aumentada de um a dois terços se, na hipótese do § 3º, houver",["divulgação, comercialização ou transmissão a terceiro dos dados ou informações obtidos.","apenas acesso.","apenas cópia.","apenas leitura.","apenas armazenamento."],"Art. 154-A, § 4º.")
q(3,"O art. 150, § 3º, I, exige, para a entrada durante o dia, a observância das",["formalidades legais.","conveniências do serviço.","ordens verbais.","preferências do agente.","informações da vizinhança."],"Art. 150, § 3º, I.")
q(3,"No art. 150, a conduta de “permanecer” em casa alheia contra a vontade expressa ou tácita de quem de direito configura",["violação de domicílio.","exercício regular de direito.","legítima defesa.","estado de necessidade.","fato atípico."],"Art. 150, caput.")
q(3,"O consultório particular de um médico, não aberto ao público no momento da consulta, é, para efeitos do art. 150,",["casa, por ser compartimento não aberto ao público onde alguém exerce profissão.","não casa, por ser local de trabalho.","casa apenas à noite.","casa apenas se for dele.","não casa, por ser comercial."],"Art. 150, § 4º, III.")
q(3,"O quarto de hotel ocupado por um hóspede é, para efeitos do art. 150,",["casa, por ser aposento ocupado de habitação coletiva.","não casa, por ser hotel.","casa apenas se for suíte.","não casa, por ser alugado.","casa apenas se estiver a noite."],"Art. 150, § 4º, II, e § 5º, I.")
q(3,"No art. 154-B, a ação penal nos crimes do art. 154-A é pública incondicionada se o crime é cometido contra",["a administração pública direta ou indireta de qualquer dos Poderes da União, Estados, Distrito Federal ou Municípios, ou contra empresas concessionárias de serviços públicos.","pessoa física.","qualquer empresa privada.","qualquer associação.","profissional liberal."],"Art. 154-B.")
q(3,"Se da invasão de dispositivo resulta o controle remoto não autorizado do dispositivo invadido, a pena é de",["reclusão, de dois a cinco anos, e multa.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","detenção, de um a seis meses.","multa."],"Art. 154-A, § 3º.")
q(3,"A diferença entre o art. 153, caput, e o art. 154 está em que, no art. 154, o segredo é conhecido em razão de",["função, ministério, ofício ou profissão.","documento particular.","correspondência confidencial.","conversa casual.","vizinhança."],"Arts. 153 e 154.")
q(3,"No texto da entrada em residência, a licitude da entrada dispensa, por força do art. 150, § 3º, II,",["o mandado e o consentimento do morador, quando um crime está sendo praticado.","a presença de testemunhas.","o registro da ocorrência.","a condução do agressor.","a comunicação ao delegado."],"Art. 150, § 3º, II.","cp6a")
q(3,"No texto do vazamento de dados, a pena do crime em que incorreu o servidor é de",["detenção, de um a quatro anos, e multa.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","multa, apenas."],"Art. 153, § 1º-A.","cp6b")
assert len(Q)==60,len(Q)
code,svg=mapa("Domicílio, correspondência e segredos",[
 ("dom","Violação de domicílio",["150: detenção, 1 a 3 meses","qualificada: 6 meses a 2 anos","entrar ou permanecer"],"seção 1"),
 ("lic","Entrada permitida",["flagrante: a qualquer hora","diligência: de dia","formalidades legais"],"seção 1"),
 ("casa","Conceito de casa",["compartimento habitado","quarto de habitação coletiva","local de profissão fechado"],"seção 2"),
 ("corr","Correspondência",["151: detenção, 1 a 6 meses","abuso de função: 1 a 3 anos","152: correspondência comercial"],"seção 3"),
 ("seg","Segredos",["153: detenção, 1 a 6 meses","1º-A: 1 a 4 anos","154: segredo profissional"],"seção 4"),
 ("inv","Dispositivo informático",["154-A: reclusão, 1 a 4 anos","§ 3º: 2 a 5 anos","154-B: representação"],"seção 4")],
 "Na prova: flagrante autoriza a entrada em casa a qualquer hora; diligência, só de dia")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"A primeira caixa trata de entrar em casa, a segunda diz o que é casa; as demais cuidam da intimidade que não se vê.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 150 a 154-B, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-6","Inviolabilidade do domicílio, da correspondência e dos segredos (CP, arts. 150 a 154-B)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 150 a 154-B. Cobertos: 150, 151, 152, 153, 154, 154-A e 154-B."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","No art. 153, a consolidação apresenta, entre o § 1º e o § 1º-A, resíduos de nota de alteração (de 2000); o texto foi tratado por programa e deve ser reconferido visualmente.","A entrada em domicílio pela Guarda Municipal, na seção 6 (rotina do guarda), resume o art. 150, § 3º; não se tratou da jurisprudência do STF sobre ingresso em domicílio sem mandado (RE 603.616, Tema 280), que não foi conferida na fonte.","Casos cp6a e cp6b fictícios."],
 fontes_conferidas=["CP, arts. 150 a 154-B: texto da Câmara, copiado por programa."])
gravar("cp-6",aula_html,banco("cp-6",Q),tx)
