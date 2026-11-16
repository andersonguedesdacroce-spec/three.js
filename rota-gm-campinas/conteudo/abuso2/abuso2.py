import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='abuso.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes em espécie da Lei de Abuso de Autoridade (arts. 9º em diante) são o conteúdo mais tocante ao guarda: prisão sem as hipóteses legais, algemas e constrangimento do preso, identificação do agente, invasão de domicílio, prova ilícita, divulgação de gravação. A maioria tem pena de detenção de um a quatro anos e multa; alguns têm pena menor, de seis meses a dois anos. A Vunesp cobra a pena de cada artigo, o prazo de 24 horas para a nota de culpa, o horário do mandado domiciliar (das 5h às 21h) e a regra do interrogatório noturno."
S={}
S[1]="## 1. Prisão, condução, comunicação e constrangimento\n\n"+L("art. 9º","Art. 9º Decretar medida de privação","Parágrafo único. Incorre na mesma pena a autoridade judiciária")+"\n\n"+L("art. 10","Art. 10. Decretar a condução coercitiva","Art. 11.")+"\n\n"+L("art. 12","Art. 12. Deixar injustificadamente","Art. 13.")+"\n\n"+L("art. 13","Art. 13. Constranger o preso","III - produzir prova")+"\n\n"+L("art. 15","Art. 15. Constranger a depor","Parágrafo único. Incorre na mesma pena quem prossegue")+"\n\n"+L("art. 15-A","Art. 15-A. Submeter a vítima","Art. 16.")+"\n\n"+L("art. 16, caput","Art. 16. Deixar de identificar-se","Parágrafo único. Incorre na mesma pena quem, como responsável")+"""

Decretar medida de privação da liberdade em manifesta desconformidade com as hipóteses legais tem detenção de um a quatro anos e multa, assim como decretar condução coercitiva de testemunha ou investigado manifestamente descabida ou sem prévia intimação. Deixar injustificadamente de comunicar prisão em flagrante à autoridade judiciária no prazo legal tem detenção de seis meses a dois anos e multa; na mesma pena incorre quem deixa de comunicar imediatamente a prisão e o local à família ou à pessoa indicada, quem deixa de entregar ao preso, em 24 horas, a nota de culpa, com o motivo da prisão e os nomes do condutor e das testemunhas, e quem prolonga a execução de pena ou prisão sem executar de imediato o alvará de soltura.

Constranger o preso, mediante violência, grave ameaça ou redução de sua capacidade de resistência, a exibir-se à curiosidade pública ou a submeter-se a situação vexatória ou constrangimento não autorizado em lei tem detenção de um a quatro anos e multa, sem prejuízo da pena da violência. Constranger a depor, sob ameaça de prisão, quem deva guardar segredo ou sigilo tem a mesma pena. Submeter a vítima de infração penal ou a testemunha de crimes violentos a procedimentos desnecessários, repetitivos ou invasivos tem detenção de três meses a um ano e multa. Deixar de identificar-se ou identificar-se falsamente ao preso, por ocasião da captura ou durante a detenção, tem detenção de seis meses a dois anos e multa.
"""
S[2]="## 2. Interrogatório, advogado, cela, invasão de domicílio e prova\n\n"+L("art. 18","Art. 18. Submeter o preso a interrogatório","Art. 19.")+"\n\n"+L("art. 19","Art. 19. Impedir ou retardar","Art. 20.")+"\n\n"+L("art. 20","Art. 20. Impedir, sem justa causa","Parágrafo único. Incorre na mesma pena quem impede o preso")+"\n\n"+L("art. 21","Art. 21. Manter presos","Art. 22.")+"\n\n"+L("art. 22","Art. 22. Invadir ou adentrar","Art. 23.")+"\n\n"+L("art. 23","Art. 23. Inovar artificiosamente","Art. 24.")+"\n\n"+L("art. 25","Art. 25. Proceder à obtenção de prova","Art. 26.")+"""

Submeter o preso a interrogatório policial durante o repouso noturno, salvo se capturado em flagrante ou se ele, assistido, consentir, tem detenção de seis meses a dois anos e multa. Impedir ou retardar o envio de pleito do preso à autoridade judiciária tem detenção de um a quatro anos e multa. Impedir, sem justa causa, a entrevista pessoal e reservada do preso com o advogado tem detenção de seis meses a dois anos e multa. Manter presos de ambos os sexos na mesma cela tem detenção de um a quatro anos e multa, e a mesma pena vale para manter criança ou adolescente na companhia de maior de idade.

Invadir ou adentrar, clandestina ou astuciosamente, ou à revelia da vontade do ocupante, imóvel alheio, sem determinação judicial ou fora das condições legais, tem detenção de um a quatro anos e multa; incorre na mesma pena quem coage alguém a franquear o acesso ao imóvel e quem cumpre mandado de busca e apreensão domiciliar após as 21h ou antes das 5h. Não há crime se o ingresso for para prestar socorro, ou havendo fundados indícios de flagrante delito ou de desastre. Inovar artificiosamente o estado de lugar, de coisa ou de pessoa, no curso de diligência, para eximir-se de responsabilidade ou responsabilizar alguém, tem detenção de um a quatro anos e multa. Obter prova por meio manifestamente ilícito, ou usá-la com prévio conhecimento da ilicitude, tem a mesma pena.
"""
S[3]="## 3. Investigação, divulgação e procedimento\n\n"+L("art. 27","Art. 27. Requisitar instauração","Art. 28.")+"\n\n"+L("art. 28","Art. 28. Divulgar gravação","Art. 29.")+"\n\n"+L("art. 29, caput","Art. 29. Prestar informação falsa","Parágrafo único. (VETADO)")+"\n\n"+L("art. 31","Art. 31. Estender injustificadamente","Art. 32.")+"\n\n"+L("art. 33","Art. 33. Exigir informação","Art. 34.")+"\n\n"+L("art. 39","Art. 39. Aplicam-se ao processo","CAPÍTULO VIII")+"""

Requisitar ou instaurar procedimento investigatório sem qualquer indício da prática de crime, de ilícito funcional ou de infração administrativa tem detenção de seis meses a dois anos e multa, mas não há crime na sindicância ou investigação preliminar sumária devidamente justificada. Divulgar gravação sem relação com a prova que se pretenda produzir, expondo a intimidade, a honra ou a imagem do investigado, tem detenção de um a quatro anos e multa. Prestar informação falsa sobre procedimento para prejudicar o investigado, estender injustificadamente a investigação e exigir informação ou cumprimento de obrigação sem expresso amparo legal têm detenção de seis meses a dois anos e multa. Aplicam-se ao processo e ao julgamento, no que couber, o Código de Processo Penal e a Lei 9.099/1995.
"""
S[5]="""## 5. Na rotina do guarda

- **Nota de culpa:** o preso recebe, em 24 horas, a nota de culpa com o motivo da prisão e os nomes do condutor e das testemunhas.
- **Identificação:** o guarda se identifica ao preso por ocasião da captura; deixar de identificar-se ou identificar-se falsamente é crime.
- **Domicílio:** só entra em imóvel sem ordem judicial para prestar socorro ou em caso de flagrante delito ou desastre; o mandado cumpre-se entre 5h e 21h.
- **Constrangimento:** expor o preso à curiosidade pública ou a situação vexatória é crime.
- **Prova:** obter prova por meio manifestamente ilícito, ou usá-la sabendo da ilicitude, é crime.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Penas | Maioria: detenção de 1 a 4 anos e multa; arts. 12, 16, 18, 20, 27, 29, 31 e 33: 6 meses a 2 anos |
| Art. 15-A | Detenção de 3 meses a 1 ano |
| Nota de culpa | 24 horas |
| Mandado domiciliar | Vedado após 21h ou antes de 5h |
| Invasão de domicílio | Não há crime para socorro, flagrante ou desastre |
| Interrogatório noturno | Salvo flagrante ou consentimento assistido |
| Presos de sexos diferentes | Mesma cela: crime |
| Sindicância sumária justificada | Não é crime (art. 27, parágrafo único) |
| Gravação sem relação com a prova | Crime do art. 28 |
| Procedimento | CPP e Lei 9.099/1995 |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 9º | Prisão ilegal: 1 a 4 anos |
| Art. 10 | Condução coercitiva descabida: 1 a 4 anos |
| Art. 12 | Falta de comunicação de prisão: 6 meses a 2 anos |
| Art. 13 | Constranger o preso: 1 a 4 anos |
| Art. 15-A | Violência institucional: 3 meses a 1 ano |
| Art. 16 | Falta de identificação: 6 meses a 2 anos |
| Art. 18 | Interrogatório noturno: 6 meses a 2 anos |
| Art. 22 | Invasão de domicílio: 1 a 4 anos |
| Art. 25 | Prova ilícita: 1 a 4 anos |
| Art. 28 | Divulgar gravação: 1 a 4 anos |
| Art. 39 | CPP e Lei 9.099/1995 |
"""
QR=[("Questão 1","Invadir ou adentrar, clandestina ou astuciosamente, ou à revelia da vontade do ocupante, imóvel alheio, sem determinação judicial ou fora das condições legais, tem pena de detenção de um a quatro anos e",["multa.","reclusão.","advertência.","perda do cargo apenas.","prisão civil."],0,"Art. 22."),
("Questão 2","Incorre na mesma pena do art. 22 quem cumpre mandado de busca e apreensão domiciliar após as vinte e uma horas ou antes das",["cinco horas.","seis horas.","quatro horas.","sete horas.","oito horas."],1,"Art. 22, § 1º, III."),
("Questão 3","Deixar de entregar ao preso, no prazo de vinte e quatro horas, a nota de culpa, com o motivo da prisão e os nomes do condutor e das testemunhas, tem pena de detenção de",["seis meses a dois anos e multa.","um a quatro anos.","três meses a um ano.","dois a cinco anos.","um ano apenas."],2,"Art. 12, parágrafo único, III."),
("Questão 4","Não há crime de invasão de domicílio se o ingresso for para prestar socorro, ou quando houver fundados indícios de flagrante delito ou de",["desastre.","reunião.","festa.","fuga de cães.","trânsito."],3,"Art. 22, § 2º.")]
t1="<strong>Entrada sem ordem</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, entrou numa casa sem ordem judicial, sem consentimento do morador e sem flagrante, apenas para procurar um suspeito."
t2="<strong>Preso exposto</strong><br><br>Um guarda de Vila Nova convidou a imprensa e expôs o preso, algemado, à curiosidade pública, forçando-o a posar para fotos."
t3="<strong>Mandado de madrugada</strong><br><br>Um agente de Vila Nova cumpriu mandado de busca e apreensão domiciliar às 4h30 da manhã, sem situação de flagrante ou socorro."
tx={"abuso2a":t1,"abuso2b":t2,"abuso2c":t3}
# n=1
q(1,"Decretar medida de privação da liberdade em manifesta desconformidade com as hipóteses legais tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 9º.")
q(1,"Decretar condução coercitiva de testemunha manifestamente descabida ou sem prévia intimação tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 10.")
q(1,"Deixar injustificadamente de comunicar prisão em flagrante à autoridade judiciária no prazo legal tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 12.")
q(1,"Deixar de entregar ao preso a nota de culpa, no prazo de",["vinte e quatro horas.","dez horas.","quarenta e oito horas.","sete dias.","trinta dias."],"Art. 12, parágrafo único, III.")
q(1,"Constranger o preso a exibir-se à curiosidade pública tem pena de detenção de um a quatro anos, multa e a pena cominada à",["violência.","fuga.","omissão.","comunicação.","lesão leve."],"Art. 13.")
q(1,"Constranger a depor, sob ameaça de prisão, quem deva guardar segredo tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 15.")
q(1,"Submeter a vítima a procedimentos desnecessários, repetitivos ou invasivos tem pena de detenção de três meses a",["um ano, e multa.","dois anos.","três anos.","seis meses.","quatro anos."],"Art. 15-A.")
q(1,"Deixar de identificar-se ao preso por ocasião de sua captura tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 16.")
q(1,"Submeter o preso a interrogatório policial durante o período de repouso noturno é crime, salvo se capturado em",["flagrante delito.","fuga.","festa.","rodovia.","feriado."],"Art. 18.")
q(1,"Impedir ou retardar o envio de pleito de preso à autoridade judiciária tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 19.")
q(1,"Impedir, sem justa causa, a entrevista pessoal e reservada do preso com seu advogado tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 20.")
q(1,"Manter presos de ambos os sexos na mesma cela tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 21.")
q(1,"Cumprir mandado de busca e apreensão domiciliar após as vinte e uma horas ou antes das cinco horas é conduta equiparada à de invasão de",["domicílio.","carro.","empresa.","escola.","rua."],"Art. 22, § 1º, III.")
q(1,"Inovar artificiosamente o estado de lugar, de coisa ou de pessoa, no curso de diligência, tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 23.")
q(1,"Proceder à obtenção de prova, em procedimento de investigação ou fiscalização, por meio manifestamente ilícito tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 25.")
q(1,"Requisitar instauração de procedimento investigatório sem qualquer indício da prática de crime tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 27.")
q(1,"Divulgar gravação sem relação com a prova que se pretenda produzir tem pena de detenção de um a",["quatro anos, e multa.","dois anos.","três anos.","seis meses.","cinco anos."],"Art. 28.")
q(1,"No texto da entrada sem ordem, entrar em casa sem ordem judicial e sem flagrante configura o crime do art.",["22.","9º.","13.","16.","25."],"Art. 22.","abuso2a")
q(1,"No texto do preso exposto, expor o preso à curiosidade pública configura o crime do art.",["13.","9º.","22.","25.","28."],"Art. 13, I.","abuso2b")
q(1,"No texto do mandado de madrugada, cumprir mandado às 4h30 está proibido porque o horário vedado é antes das",["cinco horas.","quatro horas.","seis horas.","sete horas.","oito horas."],"Art. 22, § 1º, III.","abuso2c")
# n=2
q(2,"Incorre na mesma pena do art. 12 quem deixa de comunicar imediatamente a prisão de qualquer pessoa e o local onde se encontra à sua família ou à pessoa por ela",["indicada.","contratada.","nomeada pelo juiz.","escolhida pelo guarda.","vizinha."],"Art. 12, parágrafo único, II.")
q(2,"Também incorre nas penas do art. 12 quem prolonga a execução de pena, deixando de executar o alvará de soltura",["imediatamente após recebido.","depois de 24 horas.","em dez dias.","a critério do diretor.","em sete dias."],"Art. 12, parágrafo único, IV.")
q(2,"Constranger o preso a submeter-se a situação vexatória ou a constrangimento não autorizado em lei é conduta do art.",["13.","9º.","22.","25.","28."],"Art. 13, II.")
q(2,"No art. 15-A, se o agente público permitir que terceiro intimide a vítima, gerando revitimização, a pena é aumentada de",["dois terços.","metade.","um terço.","dobro.","triplo."],"Art. 15-A, § 1º.")
q(2,"No art. 15-A, se o agente público intimidar a vítima, gerando revitimização, aplica-se a pena",["em dobro.","pela metade.","em triplo.","simples.","reduzida."],"Art. 15-A, § 2º.")
q(2,"Incorre na pena do art. 21 quem mantém, na mesma cela, criança ou adolescente na companhia de",["maior de idade.","outro adolescente.","educador.","médico.","advogado."],"Art. 21, parágrafo único.")
q(2,"Incorre nas penas do art. 22 quem coage alguém, mediante violência ou grave ameaça, a franquear-lhe o acesso a",["imóvel ou suas dependências.","veículo.","documentos.","dados.","contas."],"Art. 22, § 1º, I.")
q(2,"Não haverá crime de invasão se o ingresso for para prestar",["socorro.","visita.","serviço.","entrega.","orientação."],"Art. 22, § 2º.")
q(2,"Incorre na pena do art. 23 quem pratica a conduta com o intuito de eximir-se de responsabilidade civil ou administrativa por excesso praticado no curso de",["diligência.","viagem.","licença.","férias.","plantão."],"Art. 23, parágrafo único, I.")
q(2,"Incorre na pena do art. 25 quem faz uso de prova, em desfavor do investigado, com prévio conhecimento de sua",["ilicitude.","validade.","origem.","data.","extensão."],"Art. 25, parágrafo único.")
q(2,"Não há crime, no art. 27, quando se tratar de sindicância ou investigação preliminar sumária, devidamente",["justificada.","omitida.","sigilosa.","ignorada.","atrasada."],"Art. 27, parágrafo único.")
q(2,"Prestar informação falsa sobre procedimento judicial, policial, fiscal ou administrativo com o fim de prejudicar interesse de investigado tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 29.")
q(2,"Estender injustificadamente a investigação, procrastinando-a em prejuízo do investigado, tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 31.")
q(2,"Exigir informação ou cumprimento de obrigação sem expresso amparo legal tem pena de detenção de seis meses a",["dois anos, e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 33.")
q(2,"Incorre na pena do art. 33 quem se utiliza de cargo ou função pública para se eximir de obrigação legal ou obter vantagem ou privilégio",["indevido.","legal.","comum.","profissional.","obrigatório."],"Art. 33, parágrafo único.")
q(2,"Aplicam-se ao processo e julgamento dos delitos da lei, no que couber, o Código de Processo Penal e a Lei dos Juizados",["Especiais (9.099/1995).","Trabalhistas.","Eleitorais.","Militares.","Agrários."],"Art. 39.")
q(2,"No texto da entrada sem ordem, a exceção do art. 22, § 2º, que afastaria o crime seria o ingresso para prestar socorro ou diante de fundados indícios de flagrante ou",["desastre.","denúncia anônima.","pedido do vizinho.","suspeita.","rumor."],"Art. 22, § 2º.","abuso2a")
q(2,"No texto do preso exposto, a pena do art. 13 é de detenção de um a quatro anos, multa e a pena da",["violência.","omissão.","fuga.","lesão leve.","injúria."],"Art. 13.","abuso2b")
q(2,"No texto do mandado de madrugada, o cumprimento fora do horário é equiparado ao crime de",["invasão de domicílio.","furto.","roubo.","constrangimento ilegal.","desobediência."],"Art. 22, § 1º, III.","abuso2c")
q(2,"Impedir o preso de entrevistar-se pessoal e reservadamente com seu advogado, sem justa causa, é crime previsto no art.",["20.","18.","19.","21.","22."],"Art. 20.")
# n=3
q(3,"Assinale a alternativa correta sobre as penas dos crimes de abuso de autoridade.",["Art. 9º: detenção de 1 a 4 anos; art. 12: detenção de 6 meses a 2 anos; art. 15-A: detenção de 3 meses a 1 ano.","Art. 9º: reclusão de 1 a 4 anos.","Art. 12: detenção de 1 a 4 anos.","Art. 15-A: detenção de 1 a 4 anos.","Art. 22: detenção de 6 meses."],"Arts. 9º, 12 e 15-A.")
q(3,"Considere. I. Há crime em invadir imóvel sem ordem judicial fora das hipóteses legais. II. O mandado domiciliar pode ser cumprido às 23h. III. A nota de culpa é entregue em 24 horas. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O mandado após as 21h ou antes das 5h é crime (art. 22, § 1º, III).")
q(3,"Assinale a INCORRETA.",["O interrogatório noturno do preso é sempre permitido.","A prova ilícita é crime se obtida por meio manifestamente ilícito.","A divulgação de gravação sem relação com a prova é crime.","A violência institucional é crime.","A falta de identificação é crime."],"Salvo flagrante ou consentimento assistido, é crime (art. 18).")
q(3,"A sindicância ou investigação preliminar sumária, devidamente justificada, não configura o crime do art.",["27.","25.","28.","29.","31."],"Art. 27, parágrafo único.")
q(3,"A pena de detenção de um a quatro anos e multa é a do crime de",["manter presos de ambos os sexos na mesma cela.","falta de identificação.","interrogatório noturno.","entrevista com advogado.","prestar informação falsa."],"Art. 21 (1 a 4 anos).")
q(3,"A pena de detenção de seis meses a dois anos e multa é a do crime de",["deixar de identificar-se ao preso.","decretar prisão ilegal.","constranger o preso.","violar o domicílio.","usar prova ilícita."],"Art. 16 (6 meses a 2 anos).")
q(3,"A violência institucional do art. 15-A tem pena de detenção de três meses a um ano e multa, e a vítima é a de infração penal ou a testemunha de crimes",["violentos.","patrimoniais.","contra a honra.","ambientais.","tributários."],"Art. 15-A.")
q(3,"O interrogatório policial do preso não pode ocorrer no período de repouso noturno, salvo flagrante ou se o preso, devidamente assistido, consentir em prestar",["declarações.","depoimentos escritos.","documentos.","contratos.","laudos."],"Art. 18.")
q(3,"O art. 19, parágrafo único, estende a pena ao magistrado que, ciente do impedimento, deixa de tomar as providências tendentes a",["saná-lo.","agravá-lo.","ignorá-lo.","omiti-lo.","promovê-lo."],"Art. 19, parágrafo único.")
q(3,"A inovação artificiosa do art. 23 visa eximir-se de responsabilidade ou responsabilizar criminalmente alguém ou",["agravar-lhe a responsabilidade.","absolvê-lo.","extinguir o processo.","adiar a audiência.","beneficiar a vítima."],"Art. 23.")
q(3,"O art. 24 pune constranger, sob violência ou grave ameaça, funcionário de instituição hospitalar a admitir para tratamento pessoa cujo óbito já tenha",["ocorrido.","sido atestado.","sido registrado.","sido noticiado.","sido investigado."],"Art. 24.")
q(3,"O art. 28 pune a divulgação de gravação que exponha a intimidade, a vida privada, a honra ou a imagem do investigado ou",["acusado.","vítima.","testemunha.","juiz.","promotor."],"Art. 28.")
q(3,"A procrastinação de investigação sem prazo, de forma imotivada, em prejuízo do investigado, está no parágrafo único do art.",["31.","27.","29.","33.","25."],"Art. 31, parágrafo único.")
q(3,"No texto da entrada sem ordem, a conduta sujeita o guarda à pena de detenção de um a quatro anos e multa, prevista no art.",["22.","16.","20.","27.","31."],"Art. 22.","abuso2a")
q(3,"No texto da entrada sem ordem, o agente comete o crime porque o ingresso foi sem determinação judicial, sem consentimento e fora das condições",["estabelecidas em lei.","do bairro.","da guarda.","do comandante.","do vizinho."],"Art. 22.","abuso2a")
q(3,"No texto do preso exposto, a pena do art. 13 não prejudica a pena da violência eventualmente",["empregada.","omitida.","relatada.","legal.","consentida."],"Art. 13.","abuso2b")
q(3,"No texto do preso exposto, o constrangimento do preso à curiosidade pública ocorre mediante violência, grave ameaça ou redução de sua capacidade de",["resistência.","comunicação.","memória.","locomoção.","audição."],"Art. 13.","abuso2b")
q(3,"No texto do mandado de madrugada, o cumprimento às 4h30 enquadra-se no art. 22, § 1º, inciso",["III.","I.","II.","IV.","V."],"Art. 22, § 1º, III.","abuso2c")
q(3,"No texto do mandado de madrugada, o horário permitido para o mandado domiciliar é entre cinco e",["vinte e uma horas.","dezoito horas.","vinte horas.","vinte e duas horas.","vinte e três horas."],"Art. 22, § 1º, III.","abuso2c")
q(3,"No texto do mandado de madrugada, ausente socorro ou flagrante, o ingresso é, nos termos do art. 22, § 2º,",["crime, pois não incide a excludente.","lícito.","dispensado de ordem.","autorizado pela guarda.","autorizado por qualquer vizinho."],"Art. 22, § 2º.","abuso2c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Abuso de autoridade: crimes em espécie (arts. 9º em diante)",[
 ("pri","Prisão e condução",["art. 9º","art. 10","comunicação e nota de culpa em 24 horas"],"seção 1"),
 ("con","Constrangimento",["art. 13","art. 15-A","identificação do agente"],"seção 1"),
 ("int","Interrogatório e advogado",["repouso noturno","entrevista reservada","cela mista"],"seção 2"),
 ("inv","Domicílio",["art. 22","mandado entre 5h e 21h","exceções: socorro, flagrante, desastre"],"seção 2"),
 ("pro","Prova e inovação",["inovação artificiosa","prova ilícita"],"seção 2"),
 ("inf","Investigação",["sem indício","gravação divulgada","informação falsa"],"seção 3")],
 "Na prova: penas, 24 horas e horário do mandado")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a prisão e o constrangimento; as demais, o domicílio, a prova e a investigação.","Fontes: Edital 02/2026, Anexo I; Lei 13.869/2019 (Abuso de Autoridade), arts. 9º a 39, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("abuso-2","Abuso de autoridade: crimes em espécie e procedimento (arts. 9º em diante)",Q,list(tx),
 cobertura=["Cobertos: arts. 9º, 10, 12, 13, 15, 15-A, 16, 18 a 23, 25, 27 a 29, 31, 33 e 39. Os arts. 11, 14, 17, 26, 34 e 35 (vetados) e os arts. 24, 30, 32, 36 a 38 não foram detalhados."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Vários artigos do capítulo (arts. 30, 32 e 38) aparecem vetados na consolidação.","Trechos de lei copiados de fontes/abuso.txt por programa.","Casos abuso2a, abuso2b e abuso2c fictícios."],
 fontes_conferidas=["Lei 13.869/2019, arts. 9º a 39: texto da Câmara, copiado por programa."])
gravar("abuso-2",aula_html,banco("abuso-2",Q),tx)
