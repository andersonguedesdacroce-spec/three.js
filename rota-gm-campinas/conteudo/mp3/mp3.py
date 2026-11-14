import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='mp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="As medidas protetivas de urgência (arts. 18 a 24-A) são o coração da Lei Maria da Penha na prática: o juiz decide em 48 horas, as medidas valem enquanto houver risco, e descumpri-las é crime (art. 24-A). O guarda municipal é quem muitas vezes fiscaliza o cumprimento e prende em flagrante quem descumpre. A Vunesp cobra o prazo de 48 horas, as medidas que obrigam o agressor (art. 22), as medidas à ofendida (art. 23), a pena do art. 24-A (reclusão de dois a cinco anos) e a regra de que só o juiz concede fiança no descumprimento."
S={}
S[1]="## 1. Disposições gerais do processo\n\n"+L("art. 14","Art. 14. Os Juizados de Violência","Art. 14-A.")+"\n\n"+L("art. 15","Art. 15. É competente, por opção da ofendida","Art. 16.")+"\n\n"+L("art. 16","Art. 16. Nas ações penais públicas condicionadas","Parágrafo único. A audiência")+"\n\n"+L("arts. 16-A e 17","Art. 16-A. Nos crimes praticados","Art. 17-A.")+"\n\n"+L("art. 17-A","Art. 17-A. O nome da ofendida","CAPÍTULO II")+"""

Os Juizados de Violência Doméstica e Familiar contra a Mulher têm competência cível e criminal, e os atos processuais podem ser realizados à noite. Nos processos cíveis, a ofendida escolhe o Juizado do seu domicílio, do lugar do fato ou do domicílio do agressor. Nas ações penais públicas condicionadas à representação, a renúncia só é admitida perante o juiz, em audiência especial, antes do recebimento da denúncia e ouvido o Ministério Público. A ofendida decai do direito de queixa ou de representação se não o exerce em 12 meses.

É vedada a aplicação de penas de cesta básica ou outras de prestação pecuniária e a substituição de pena que implique o pagamento isolado de multa. O nome da ofendida fica sob sigilo nos processos, mas o sigilo não abrange o nome do autor do fato.
"""
S[2]="## 2. Medidas protetivas de urgência: regras gerais\n\n"+L("art. 18","Art. 18. Recebido o expediente","Art. 19.")+"\n\n"+L("art. 19, caput a § 3º","Art. 19. As medidas protetivas","§ 4º As medidas protetivas")+"\n\n"+L("art. 19, §§ 4º a 6º","§ 4º As medidas protetivas de urgência serão concedidas","Art. 20.")+"\n\n"+L("arts. 20 e 21","Art. 20. Em qualquer fase","Seção II")+"""

Recebido o expediente, o juiz tem 48 horas para decidir sobre as medidas protetivas, encaminhar a ofendida à assistência judiciária, comunicar o Ministério Público e determinar a apreensão imediata de arma de fogo do agressor. As medidas podem ser concedidas a requerimento do Ministério Público ou a pedido da ofendida, de imediato, sem audiência das partes, isolada ou cumulativamente, e substituídas por outras mais eficazes. Valem independentemente da tipificação penal, do ajuizamento de ação ou do boletim de ocorrência, e vigoram enquanto persistir o risco.

Cabe prisão preventiva do agressor em qualquer fase do inquérito ou da instrução, decretada pelo juiz de ofício, a requerimento do Ministério Público ou por representação da autoridade policial. A ofendida deve ser notificada dos atos processuais relativos ao agressor, especialmente ao ingresso e à saída da prisão, e não pode entregar intimação ou notificação ao agressor.
"""
S[3]="## 3. Medidas que obrigam o agressor e medidas à ofendida\n\n"+L("art. 22, caput e incisos","Art. 22. Constatada a prática","§ 1º As medidas referidas")+"\n\n"+L("art. 22, § 3º","§ 3º Para garantir a efetividade","§ 4º Na aplicação")+"\n\n"+L("art. 22, §§ 6º a 8º","§ 6º A aplicação da medida prevista no inciso VIII","§ 9º Nos casos")+"\n\n"+L("art. 23","Art. 23. Poderá o juiz, quando necessário","Art. 24.")+"\n\n"+L("art. 24","Art. 24. Para a proteção patrimonial","Seção IV")+"""

O juiz pode aplicar de imediato ao agressor, em conjunto ou separadamente, entre outras: suspensão da posse ou restrição do porte de armas; afastamento do lar; proibição de aproximação da ofendida, de familiares e testemunhas, de contato por qualquer meio e de frequentação de determinados lugares; restrição ou suspensão de visitas aos dependentes menores; prestação de alimentos provisionais; comparecimento a programas de recuperação e reeducação; acompanhamento psicossocial; e monitoração eletrônica com dispositivo de alerta à vítima. Para garantir a efetividade, o juiz pode requisitar, a qualquer momento, auxílio da força policial. O sistema de monitoração emite alerta automático à vítima e à unidade policial mais próxima quando o agressor rompe o perímetro de exclusão.

À ofendida, o juiz pode encaminhar a programa de proteção, determinar a recondução ao domicílio após o afastamento do agressor, afastar a ofendida do lar sem prejuízo de seus direitos, determinar a separação de corpos, determinar a matrícula dos dependentes em instituição mais próxima, independentemente de vaga, e conceder auxílio-aluguel por período não superior a seis meses. Na proteção patrimonial, pode determinar a restituição de bens subtraídos, a proibição temporária de atos e contratos sobre propriedade comum, a suspensão de procurações e a caução provisória.
"""
S[4]="## 4. Crime de descumprimento de medidas protetivas\n\n"+L("art. 24-A","Art. 24-A. Descumprir decisão judicial","CAPÍTULO III")+"""

Descumprir decisão judicial que defere medidas protetivas de urgência é crime, com reclusão de dois a cinco anos e multa. O crime independe da competência civil ou criminal do juiz que deferiu as medidas. Na prisão em flagrante, apenas a autoridade judicial pode conceder fiança. A pena aumenta de um terço até a metade se o descumprimento decorrer da violação das áreas de exclusão monitoradas eletronicamente ou da remoção, violação ou alteração do dispositivo de monitoração sem autorização judicial.
"""
S[5]="""## 6. Na rotina do guarda

- **Descumprimento de medida protetiva:** é crime (reclusão de dois a cinco anos e multa), e o guarda pode prender em flagrante; apenas o juiz concede fiança.
- **Proibição de aproximação:** a distância mínima fixada pelo juiz vale; o agressor que se aproxima descumpre a medida.
- **Auxílio da força policial:** o juiz pode requisitar, a qualquer momento, o auxílio da guarda e da polícia para garantir a medida.
- **Alerta do monitoramento:** o sistema alerta a vítima e a unidade policial mais próxima quando o agressor rompe o perímetro.
- **Arma de fogo:** o juiz pode determinar a apreensão imediata da arma sob a posse do agressor.
"""
S[6]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Prazo do juiz | 48 horas para decidir |
| Medidas protetivas | Vigoram enquanto persistir o risco; independem de tipificação penal e de boletim |
| Representação | Renúncia só perante o juiz, em audiência, antes do recebimento da denúncia |
| Decadência | 12 meses |
| Penas vedadas | Cesta básica e prestação pecuniária; multa isolada |
| Medidas ao agressor | Armas, afastamento, proibição de aproximação e contato, visitas, alimentos, programas, monitoração |
| Auxílio-aluguel | Até 6 meses |
| Descumprimento (art. 24-A) | Reclusão de 2 a 5 anos e multa; fiança só pelo juiz |
| Aumento da pena | 1/3 até a metade se viola monitoração |
| Sigilo | Nome da ofendida sigiloso; nome do autor não |
"""
S[7]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 15 | Juizado do domicílio, do fato ou do agressor, à opção da ofendida |
| Art. 16 | Renúncia perante o juiz |
| Art. 16-A | Decadência em 12 meses |
| Art. 17 | Vedadas cesta básica e multa isolada |
| Art. 18 | Juiz decide em 48 horas |
| Art. 19 | Medidas isoladas ou cumuladas; vigoram enquanto houver risco |
| Art. 20 | Prisão preventiva |
| Art. 22 | Medidas ao agressor |
| Art. 23 | Medidas à ofendida; auxílio-aluguel até 6 meses |
| Art. 24 | Proteção patrimonial |
| Art. 24-A | Crime de descumprimento: reclusão de 2 a 5 anos |
"""
QR=[("Questão 1","Recebido o expediente com o pedido da ofendida, caberá ao juiz, no prazo de",["quarenta e oito horas, conhecer do pedido e decidir sobre as medidas protetivas.","vinte e quatro horas.","dez dias.","cinco dias.","trinta dias."],0,"Art. 18."),
("Questão 2","Descumprir decisão judicial que defere medidas protetivas de urgência tem pena de",["reclusão, de dois a cinco anos, e multa.","detenção de seis meses a um ano.","reclusão de um a três anos.","multa apenas.","detenção de dois a quatro anos."],1,"Art. 24-A."),
("Questão 3","Na hipótese de prisão em flagrante pelo descumprimento de medida protetiva, apenas a autoridade judicial poderá conceder",["fiança.","liberdade provisória.","habeas corpus.","indulto.","anistia."],2,"Art. 24-A, § 2º."),
("Questão 4","As medidas protetivas de urgência vigorarão enquanto persistir risco à integridade física, psicológica, sexual, patrimonial ou moral da ofendida ou de seus",["dependentes.","vizinhos.","amigos.","empregados.","colegas."],3,"Art. 19, § 6º.")]
t1="<strong>Agressor que se aproxima</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, foi chamada por mulher que tem medida protetiva proibindo o ex-companheiro de se aproximar a menos de 300 metros. Ele estava parado diante da casa dela."
t2="<strong>Pedido ao juiz</strong><br><br>A ofendida de Vila Nova pediu medidas protetivas. O juiz recebeu o expediente e deferiu as medidas, determinando a apreensão da arma de fogo do agressor."
t3="<strong>Tornozeleira violada</strong><br><br>Um agressor de Vila Nova, monitorado eletronicamente, removeu o dispositivo sem autorização judicial e foi até a casa da ofendida."
tx={"mp3a":t1,"mp3b":t2,"mp3c":t3}
# n=1
q(1,"Os Juizados de Violência Doméstica e Familiar contra a Mulher são órgãos da Justiça Ordinária com competência cível e",["criminal.","trabalhista.","eleitoral.","militar.","tributária."],"Art. 14.")
q(1,"Os atos processuais nos Juizados poderão realizar-se em horário",["noturno.","apenas diurno.","apenas matutino.","apenas dominical.","apenas de feriado."],"Art. 14, parágrafo único.")
q(1,"Nos processos cíveis, é competente, por opção da ofendida, o Juizado do seu domicílio ou de sua",["residência.","empresa.","escola.","igreja.","clube."],"Art. 15, I.")
q(1,"A renúncia à representação só é admitida perante o",["juiz, em audiência especialmente designada.","delegado.","promotor.","guarda.","advogado."],"Art. 16.")
q(1,"A ofendida decai do direito de queixa ou de representação se não o exerce no prazo de",["doze meses.","seis meses.","um mês.","dois anos.","cinco anos."],"Art. 16-A.")
q(1,"É vedada a aplicação, nos casos de violência doméstica, de penas de cesta básica ou outras de prestação",["pecuniária.","de serviço.","de liberdade.","de advertência.","de reparação."],"Art. 17.")
q(1,"O nome da ofendida ficará sob",["sigilo nos processos.","publicidade obrigatória.","divulgação.","edital.","registro público."],"Art. 17-A.")
q(1,"O sigilo do art. 17-A não abrange o nome do",["autor do fato.","juiz.","promotor.","delegado.","advogado da vítima."],"Art. 17-A, parágrafo único.")
q(1,"As medidas protetivas de urgência poderão ser concedidas pelo juiz a requerimento do Ministério Público ou a pedido da",["ofendida.","vizinha.","testemunha.","guarda.","empresa."],"Art. 19.")
q(1,"As medidas protetivas poderão ser concedidas de imediato, independentemente de audiência das partes e de manifestação do",["Ministério Público.","juiz.","delegado.","advogado.","guarda."],"Art. 19, § 1º.")
q(1,"As medidas protetivas serão aplicadas isolada ou",["cumulativamente.","alternadamente.","eventualmente.","anualmente.","retroativamente."],"Art. 19, § 2º.")
q(1,"Em qualquer fase do inquérito ou da instrução criminal, caberá a prisão",["preventiva do agressor.","temporária da ofendida.","domiciliar do juiz.","administrativa.","civil."],"Art. 20.")
q(1,"A ofendida não poderá entregar intimação ou notificação ao",["agressor.","juiz.","promotor.","delegado.","escrivão."],"Art. 21, parágrafo único.")
q(1,"Entre as medidas ao agressor está a suspensão da posse ou restrição do porte de",["armas.","veículos.","celulares.","documentos.","cartões."],"Art. 22, I.")
q(1,"Entre as medidas ao agressor está o afastamento do lar, domicílio ou local de convivência com a",["ofendida.","testemunha.","vizinha.","empresa.","escola."],"Art. 22, II.")
q(1,"Entre as medidas ao agressor está a prestação de alimentos provisionais ou",["provisórios.","definitivos.","eventuais.","facultativos.","simbólicos."],"Art. 22, V.")
q(1,"A monitoração eletrônica do agressor disponibiliza à vítima aplicação ou dispositivo de segurança que alerte sobre eventual",["aproximação do agressor.","fuga do agressor.","pagamento.","visita.","audiência."],"Art. 22, VIII.")
q(1,"No texto do agressor que se aproxima, a proibição de aproximação é medida do art. 22, inciso",["III.","I.","II.","V.","VI."],"Art. 22, III, a.","mp3a")
q(1,"No texto do pedido ao juiz, o juiz determinou a apreensão imediata da arma de fogo, prevista no art. 18, inciso",["IV.","I.","II.","III.","V."],"Art. 18, IV.","mp3b")
q(1,"No texto da tornozeleira violada, a remoção do dispositivo sem autorização judicial aumenta a pena do art.",["24-A.","22.","23.","24.","21."],"Art. 24-A, § 4º.","mp3c")
# n=2
q(2,"Os Juizados podem ser criados pela União, no Distrito Federal e nos Territórios, e pelos",["Estados.","Municípios.","empresas.","condomínios.","clubes."],"Art. 14.")
q(2,"A ofendida pode escolher o Juizado do lugar do fato em que se baseou a",["demanda.","empresa.","escola.","família.","vizinhança."],"Art. 15, II.")
q(2,"A audiência do art. 16 tem por objetivo confirmar a retratação da vítima, não a",["representação.","denúncia.","sentença.","prova.","pena."],"Art. 16, parágrafo único.")
q(2,"Vedada a substituição de pena que implique o pagamento isolado de",["multa.","serviço.","advertência.","prisão.","reparação."],"Art. 17.")
q(2,"O juiz, em 48 horas, determina a apreensão imediata de arma de fogo sob a posse do",["agressor.","vizinho.","ofendido.","delegado.","advogado."],"Art. 18, IV.")
q(2,"As medidas protetivas poderão ser substituídas a qualquer tempo por outras de maior",["eficácia.","custo.","duração.","gravidade.","burocracia."],"Art. 19, § 2º.")
q(2,"As medidas protetivas são concedidas em juízo de cognição sumária a partir do depoimento da ofendida perante a",["autoridade policial.","escola.","empresa.","imprensa.","família."],"Art. 19, § 4º.")
q(2,"As medidas protetivas serão concedidas independentemente da tipificação penal da violência, do ajuizamento de ação, da existência de inquérito ou do registro de",["boletim de ocorrência.","passaporte.","contrato.","título.","fiança."],"Art. 19, § 5º.")
q(2,"A prisão preventiva pode ser decretada pelo juiz de ofício, a requerimento do Ministério Público ou mediante representação da autoridade",["policial.","tributária.","educacional.","sanitária.","eleitoral."],"Art. 20.")
q(2,"A ofendida deverá ser notificada dos atos processuais relativos ao agressor, especialmente os pertinentes ao ingresso e à saída da",["prisão.","escola.","empresa.","cidade.","igreja."],"Art. 21.")
q(2,"Entre as proibições de conduta está a aproximação da ofendida, de seus familiares e das testemunhas, fixando o limite mínimo de",["distância.","horário.","valor.","tempo.","idade."],"Art. 22, III, a.")
q(2,"As medidas do art. 22 não impedem a aplicação de outras previstas na legislação, devendo a providência ser comunicada ao",["Ministério Público.","prefeito.","vereador.","síndico.","conselho."],"Art. 22, § 1º.")
q(2,"Para garantir a efetividade das medidas, o juiz poderá requisitar, a qualquer momento, auxílio da",["força policial.","imprensa.","vizinhança.","empresa.","escola."],"Art. 22, § 3º.")
q(2,"O sistema de monitoração emite alerta automático e simultâneo à vítima e à unidade policial mais próxima sempre que o agressor romper o",["perímetro de exclusão.","contrato.","prazo.","horário.","cadastro."],"Art. 22, § 8º.")
q(2,"As medidas protetivas de natureza cível constituem título executivo",["judicial de pleno direito.","extrajudicial.","provisório.","facultativo.","eventual."],"Art. 22, § 10.")
q(2,"O auxílio-aluguel é concedido por período não superior a",["seis meses.","um mês.","três meses.","um ano.","dois anos."],"Art. 23, VI.")
q(2,"No texto do agressor que se aproxima, a conduta caracteriza, em tese, o crime do art.",["24-A.","22.","23.","24.","21."],"Art. 24-A.","mp3a")
q(2,"No texto do pedido ao juiz, a medida do art. 22, I, refere-se à suspensão da posse ou restrição do porte de",["armas.","veículos.","documentos.","celulares.","cartões."],"Art. 22, I.","mp3b")
q(2,"No texto da tornozeleira violada, o aumento de pena do art. 24-A, § 4º, é de",["um terço até a metade.","metade até o dobro.","um sexto.","dois terços.","triplo."],"Art. 24-A, § 4º.","mp3c")
q(2,"No texto da tornozeleira violada, ao romper o perímetro de exclusão, o sistema emite alerta automático e simultâneo à vítima e à unidade policial",["mais próxima.","mais antiga.","federal.","regional.","militar."],"Art. 22, § 8º.","mp3c")
# n=3
q(3,"Assinale a alternativa correta sobre o art. 24-A.",["Pena de reclusão de 2 a 5 anos e multa; fiança só pelo juiz; independe da competência civil ou criminal do juiz que deferiu.","Pena de detenção de 6 meses.","Fiança concedida pelo delegado.","Exige competência criminal do juiz.","Pena de multa apenas."],"Art. 24-A.")
q(3,"Considere. I. O juiz decide sobre as medidas em 48 horas. II. As medidas dependem do boletim de ocorrência. III. As medidas vigoram enquanto persistir o risco. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"As medidas independem de boletim (art. 19, § 5º).")
q(3,"Assinale a INCORRETA.",["A fiança no descumprimento pode ser concedida pelo delegado.","O descumprimento é crime.","A pena aumenta em 1/3 até a metade se viola a monitoração.","O crime independe da competência civil ou criminal do juiz.","Cabe multa além da reclusão."],"Apenas a autoridade judicial concede fiança (art. 24-A, § 2º).")
q(3,"A aplicação da monitoração eletrônica terá prioridade nos casos de descumprimento de medidas protetivas anteriores ou quando for verificado risco iminente à integridade",["física ou psicológica da vítima.","financeira.","patrimonial apenas.","social.","moral apenas."],"Art. 22, § 6º.")
q(3,"Para a instalação do equipamento de monitoração, a autoridade competente instruirá o agressor sobre o seu funcionamento e as áreas de exclusão, constando a ciência de",["termo nos autos.","contrato.","edital.","alvará.","carta."],"Art. 22, § 7º.")
q(3,"Se o juiz deixar de aplicar a monitoração nos casos do § 6º, a decisão deverá apresentar fundamentação expressa quanto às razões da",["não aplicação.","aplicação.","urgência.","vítima.","prisão."],"Art. 22, § 9º.")
q(3,"A matrícula dos dependentes da ofendida em instituição mais próxima do domicílio independe da existência de",["vaga.","documento.","renda.","laudo.","certidão."],"Art. 23, V.")
q(3,"Na proteção patrimonial, o juiz pode determinar a suspensão das procurações conferidas pela ofendida ao",["agressor.","juiz.","delegado.","advogado.","vizinho."],"Art. 24, III.")
q(3,"Para os atos de proibição de atos e contratos sobre propriedade comum e de suspensão de procurações, o juiz oficiará ao cartório",["competente.","eleitoral.","trabalhista.","militar.","rural."],"Art. 24, parágrafo único.")
q(3,"Se o agressor for pessoa com arma por razão do cargo, o superior imediato é responsável pelo cumprimento da restrição, sob pena de prevaricação ou de",["desobediência.","furto.","estelionato.","roubo.","peculato."],"Art. 22, § 2º.")
q(3,"A restrição do porte de armas é comunicada ao órgão competente nos termos da Lei do",["Desarmamento.","Idoso.","Torcedor.","Juizado Especial.","Execução Penal."],"Art. 22, I.")
q(3,"O juiz concederá a tutela específica ou determinará providências que assegurem a obtenção de tutela pelo resultado prático",["equivalente.","oposto.","mínimo.","máximo.","irrelevante."],"Art. 22, § 4º.")
q(3,"A configuração do crime do art. 24-A independe da competência civil ou criminal do",["juiz que deferiu as medidas.","delegado.","promotor.","advogado.","guarda."],"Art. 24-A, § 1º.")
q(3,"O art. 24-A, § 3º, estabelece que o crime não exclui a aplicação de outras",["sanções cabíveis.","fianças.","anistias.","isenções.","prescrições."],"Art. 24-A, § 3º.")
q(3,"No texto do agressor que se aproxima, a fiança, na hipótese de prisão em flagrante, será concedida somente pela",["autoridade judicial.","guarda.","delegado.","promotor.","vizinha."],"Art. 24-A, § 2º.","mp3a")
q(3,"No texto do agressor que se aproxima, a distância de 300 metros fixada judicialmente é medida do art. 22, III,",["a, de aproximação.","b, de contato.","c, de frequentação.","d, de visitas.","e, de armas."],"Art. 22, III, a.","mp3a")
q(3,"No texto do pedido ao juiz, o prazo para o juiz decidir sobre as medidas é de",["quarenta e oito horas.","vinte e quatro horas.","cinco dias.","dez dias.","trinta dias."],"Art. 18.","mp3b")
q(3,"No texto do pedido ao juiz, o juiz deve comunicar o fato ao",["Ministério Público, para as providências cabíveis.","Detran.","Conselho Tutelar.","Prefeitura.","Corpo de Bombeiros."],"Art. 18, III.","mp3b")
q(3,"No texto da tornozeleira violada, a remoção do dispositivo sem autorização configura o aumento de pena do",["§ 4º do art. 24-A.","§ 1º do art. 24-A.","§ 2º do art. 24-A.","§ 3º do art. 24-A.","art. 23."],"Art. 24-A, § 4º.","mp3c")
q(3,"No texto da tornozeleira violada, ao ir até a casa da ofendida, o agressor também descumpriu a área de",["exclusão monitorada eletronicamente.","livre trânsito.","trabalho.","lazer.","estudo."],"Art. 24-A, § 4º.","mp3c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Lei Maria da Penha: medidas protetivas (arts. 13 a 24-A)",[
 ("pro","Procedimento",["Juizados","renúncia perante o juiz","decadência em 12 meses"],"seção 1"),
 ("pra","Prazo do juiz",["48 horas","arma de fogo","comunicação ao MP"],"seção 2"),
 ("vig","Vigência",["enquanto houver risco","sem boletim","isolada ou cumulativa"],"seção 2"),
 ("agr","Medidas ao agressor",["armas e afastamento","proibição de aproximação e contato","monitoração eletrônica"],"seção 3"),
 ("ofe","Medidas à ofendida",["programa de proteção","auxílio-aluguel: 6 meses","matrícula sem vaga"],"seção 3"),
 ("des","Descumprimento",["reclusão de 2 a 5 anos","fiança só pelo juiz","aumento de 1/3 à metade"],"seção 4")],
 "Na prova: 48 horas, 24-A e fiança só pelo juiz")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',5,6,7],QR,5,svg,"A primeira linha traz o procedimento; as demais, as medidas protetivas, suas modalidades e o crime de descumprimento.","Fontes: Edital 02/2026, Anexo I; Lei 11.340/2006 (Lei Maria da Penha), arts. 13 a 24-A, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("mp-3","Lei Maria da Penha: procedimentos e medidas protetivas de urgência (arts. 13 a 24-A)",Q,list(tx),
 cobertura=["Cobertos: arts. 14 a 24-A. Não detalhados: art. 13, art. 14-A (vetado), art. 22, §§ 1º, 2º, 4º, 9º e 10 (apenas citados em questões)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","A aula traz o art. 22, inciso VIII, com a monitoração eletrônica; conferir a redação atual no Planalto.","Trechos de lei copiados de fontes/mp.txt por programa.","Casos mp3a, mp3b e mp3c fictícios."],
 fontes_conferidas=["Lei 11.340/2006, arts. 13 a 24-A: texto da Câmara, copiado por programa."])
gravar("mp-3",aula_html,banco("mp-3",Q),tx)
