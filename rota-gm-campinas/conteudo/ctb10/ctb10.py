import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes de trânsito (arts. 291 a 312-B) são o ponto em que o Código encontra o Direito Penal: homicídio e lesão culposos na direção, omissão de socorro, fuga do local, embriaguez ao volante, racha, direção sem habilitação. Para o guarda municipal, que muitas vezes é o primeiro a chegar ao local, importa saber o que configura crime, qual é a pena, quando há prisão em flagrante e como se prova a embriaguez. A Vunesp cobra principalmente a pena de cada crime, os limites de álcool do art. 306 e a regra de que quem presta socorro não é preso em flagrante."
S={}
S[1]="## 1. Disposições gerais\n\n"+L("art. 291, caput e §§ 1º e 2º","Art. 291. Aos crimes cometidos","§ 3º (VETADO na Lei nº 13.546")+"\n\n"+L("arts. 292 a 293","Art. 292. A suspensão ou a proibição","Art. 294.")+"\n\n"+L("arts. 294 a 296","Art. 294. Em qualquer fase","Art. 297.")+"\n\n"+L("art. 298","Art. 298. São circunstâncias","Parágrafo único. (VETADO na Lei nº 14.304")+"\n\n"+L("art. 301","Art. 301. Ao condutor de veículo","Seção II")+"""

Aos crimes de trânsito aplicam-se as normas gerais do Código Penal e do Código de Processo Penal e a Lei dos Juizados Especiais (Lei 9.099/1995), no que couber. Na lesão corporal culposa valem a composição civil, a transação penal e a representação, salvo se o agente dirigia sob influência de álcool ou outra substância psicoativa, participava de corrida ou exibição não autorizada, ou estava em velocidade superior à máxima da via em 50 km/h; nesses casos, instaura-se inquérito policial.

A suspensão ou a proibição de obter a habilitação dura de dois meses a cinco anos, e o réu condenado tem 48 horas, após o trânsito em julgado, para entregar o documento. A penalidade não começa a correr enquanto o condenado estiver preso. Em qualquer fase da investigação, o juiz pode decretar a suspensão como medida cautelar, para garantir a ordem pública, e dessa decisão cabe recurso em sentido estrito, sem efeito suspensivo. Se o réu for reincidente, o juiz aplica a suspensão. As agravantes incluem o dano potencial a duas ou mais pessoas, o veículo sem placas ou com placas adulteradas, a ausência de habilitação, a categoria diferente e a profissão que exige cuidados especiais.

O condutor que, em sinistro com vítima, presta pronto e integral socorro não sofre prisão em flagrante nem lhe é exigida fiança.
"""
S[2]="## 2. Homicídio e lesão corporal culposos\n\n"+L("art. 302, caput e § 1º","Art. 302. Praticar homicídio culposo","V - [revogado]")+"\n\n"+L("art. 302, § 3º","§ 3º Se o agente conduz veículo","Art. 303.")+"\n\n"+L("art. 303, caput e § 1º","Art. 303. Praticar lesão corporal culposa","§ 1º pela Lei nº 13.546")+"\n\n"+L("art. 303, § 2º","§ 2º A pena privativa de liberdade é de reclusão","Art. 304.")+"""

O homicídio culposo na direção de veículo automotor é punido com detenção de dois a quatro anos e suspensão ou proibição de obter a habilitação. A pena aumenta de um terço à metade se o agente não possui habilitação, pratica o crime em faixa de pedestres ou na calçada, deixa de prestar socorro, ou conduz veículo de transporte de passageiros no exercício da profissão. Se o agente conduz sob a influência de álcool ou outra substância psicoativa, a pena é de reclusão de cinco a oito anos.

A lesão corporal culposa tem detenção de seis meses a dois anos e suspensão ou proibição; as mesmas causas de aumento valem. Se o agente conduz com capacidade psicomotora alterada e a lesão é grave ou gravíssima, a pena é de reclusão de dois a cinco anos.
"""
S[3]="## 3. Omissão de socorro, fuga e embriaguez\n\n"+L("arts. 304 e 305","Art. 304. Deixar o condutor","Art. 306.")+"\n\n"+L("art. 306, caput e § 1º","Art. 306. Conduzir veículo automotor","§ 2º A verificação")+"\n\n"+L("art. 306, § 2º","§ 2º A verificação do disposto","§ 3º O Contran disporá")+"\n\n"+L("art. 306, § 4º","§ 4º Poderá ser empregado","Art. 307.")+"""

Deixar de prestar imediato socorro à vítima, ou, não podendo, de solicitar auxílio da autoridade pública, é crime punido com detenção de seis meses a um ano, ou multa, se o fato não constituir crime mais grave; a omissão incide mesmo que suprida por terceiros ou se a vítima tem morte instantânea ou ferimentos leves. Afastar-se do local do sinistro para fugir à responsabilidade penal ou civil também tem detenção de seis meses a um ano, ou multa.

Conduzir veículo com capacidade psicomotora alterada pela influência de álcool ou outra substância é crime punido com detenção de seis meses a três anos, multa e suspensão ou proibição de obter a habilitação. Configura-se com concentração igual ou superior a 6 decigramas de álcool por litro de sangue ou 0,3 miligrama por litro de ar alveolar, ou por sinais de alteração da capacidade psicomotora. A prova admite teste de alcoolemia ou toxicológico, exame clínico, perícia, vídeo, prova testemunhal e outros meios, observado o direito à contraprova, e pode ser usado qualquer aparelho homologado pelo Inmetro.
"""
S[4]="## 4. Habilitação, racha e outros crimes\n\n"+L("arts. 307 e 308","Art. 307. Violar a suspensão","Art. 309.")+"\n\n"+L("arts. 309 a 312","Art. 309. Dirigir veículo automotor","Art. 312-A.")+"\n\n"+L("art. 312-A","Art. 312-A. Para os crimes","Art. 312-B.")+"""

Violar a suspensão ou proibição de obter a habilitação é crime punido com detenção de seis meses a um ano e multa, com nova imposição de igual prazo; nas mesmas penas incorre quem deixa de entregar o documento no prazo. Participar de corrida, disputa ou exibição de perícia em via pública, sem autorização, gerando situação de risco, tem detenção de seis meses a três anos, multa e suspensão; se resulta lesão grave sem dolo, reclusão de três a seis anos, e se resulta morte, reclusão de cinco a dez anos.

Dirigir sem habilitação, ou com direito cassado, gerando perigo de dano, tem detenção de seis meses a um ano, ou multa. A mesma pena vale para entregar a direção a pessoa não habilitada, cassada, suspensa ou sem condições de saúde ou embriagada, para trafegar em velocidade incompatível com a segurança perto de escolas, hospitais e locais de grande concentração de pessoas, gerando perigo de dano, e para inovar artificiosamente o local, a coisa ou a pessoa em sinistro com vítima, para induzir a erro o policial, o perito ou o juiz. A substituição de pena privativa por restritiva de direitos nos crimes dos arts. 302 a 312 deve ser prestação de serviço à comunidade em atividades ligadas a resgate e atendimento de vítimas de trânsito. O art. 312-B veda a substituição por pena restritiva para o homicídio do art. 302, § 3º, e a lesão do art. 303, § 2º.
"""
S[5]="""## 5. Na rotina do guarda

- **Sinistro com vítima:** o guarda preserva o local e chama o socorro; o condutor que presta pronto e integral socorro não é preso em flagrante.
- **Fuga do local:** o condutor que se afasta para fugir à responsabilidade comete o crime do art. 305.
- **Embriaguez:** a prova pode ser o teste, o exame clínico, o vídeo ou os sinais; a recusa ao teste não impede o crime, se há outras provas.
- **Racha:** corrida em via pública sem autorização e com risco é crime, com suspensão da habilitação.
- **Inquérito:** nos casos de álcool, corrida ou velocidade 50 km/h acima, o crime de lesão culposa segue por inquérito policial.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do homicídio culposo | Detenção de 2 a 4 anos; com álcool, reclusão de 5 a 8 |
| Pena da lesão culposa | Detenção de 6 meses a 2 anos; com álcool e lesão grave, reclusão de 2 a 5 |
| Limites de álcool | 6 dg/L de sangue ou 0,3 mg/L de ar alveolar |
| Pena da embriaguez | Detenção de 6 meses a 3 anos, multa e suspensão |
| Pena de omissão de socorro e fuga | Detenção de 6 meses a 1 ano, ou multa |
| Racha | Detenção de 6 meses a 3 anos; lesão grave 3 a 6; morte 5 a 10 |
| Duração da suspensão | 2 meses a 5 anos |
| Entrega do documento | 48 horas após o trânsito em julgado |
| Prisão em flagrante | Não, se prestar pronto e integral socorro |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 302 | Homicídio culposo: detenção, 2 a 4 anos |
| Art. 302, § 3º | Com álcool: reclusão, 5 a 8 anos |
| Art. 303 | Lesão culposa: detenção, 6 meses a 2 anos |
| Art. 304 | Omissão de socorro: detenção, 6 meses a 1 ano, ou multa |
| Art. 305 | Fuga do local: detenção, 6 meses a 1 ano, ou multa |
| Art. 306 | Embriaguez: detenção, 6 meses a 3 anos |
| Art. 307 | Violar suspensão: detenção, 6 meses a 1 ano e multa |
| Art. 308 | Racha: detenção, 6 meses a 3 anos |
| Art. 309 | Sem habilitação: detenção, 6 meses a 1 ano, ou multa |
| Art. 311 | Velocidade incompatível: detenção, 6 meses a 1 ano, ou multa |
| Art. 301 | Quem socorre não é preso em flagrante |
"""
QR=[("Questão 1","Praticar homicídio culposo na direção de veículo automotor tem como pena detenção de",["dois a quatro anos e suspensão ou proibição de se obter a habilitação.","seis meses a um ano.","um a três anos.","cinco a oito anos.","quatro a dez anos."],0,"Art. 302."),
("Questão 2","A concentração de álcool que configura o crime do art. 306 é de, no mínimo, seis decigramas por litro de sangue ou",["0,3 miligrama de álcool por litro de ar alveolar.","0,1 miligrama por litro de ar alveolar.","0,6 miligrama por litro de ar alveolar.","1 miligrama por litro de ar alveolar.","qualquer concentração."],1,"Art. 306, § 1º, I."),
("Questão 3","Ao condutor de veículo, nos casos de sinistros de trânsito com vítima, não se imporá a prisão em flagrante nem se exigirá fiança se prestar",["pronto e integral socorro à vítima.","o nome.","o documento.","o veículo.","a carteira."],2,"Art. 301."),
("Questão 4","A penalidade de suspensão ou de proibição de se obter a habilitação tem duração de",["dois meses a cinco anos.","um a dois anos.","um mês a um ano.","cinco a dez anos.","seis meses a um ano."],3,"Art. 293.")]
t1="<strong>Sinistro com vítima</strong><br><br>Em Vila Nova, cidade fictícia, um condutor atropelou um pedestre na faixa e, em vez de socorrê-lo, deixou o local. A guarda municipal chegou depois e encontrou a vítima ferida por terceiros socorrida."
t2="<strong>Fiscalização de embriaguez</strong><br><br>Numa blitz, um condutor apresentava fala arrastada e odor de álcool. O teste de etilômetro indicou 0,4 miligrama de álcool por litro de ar alveolar."
t3="<strong>Racha no centro</strong><br><br>Dois jovens disputavam corrida de carros numa avenida da cidade, sem autorização da autoridade, e um deles atropelou um ciclista, que sofreu lesão corporal grave sem dolo."
tx={"ctb10a":t1,"ctb10b":t2,"ctb10c":t3}
# n=1
q(1,"Aos crimes de trânsito aplicam-se as normas gerais do Código Penal, do Código de Processo Penal e a Lei dos Juizados Especiais (Lei 9.099/1995), no que",["couber.","for conveniente ao réu.","for rápido.","for útil.","a imprensa pedir."],"Art. 291.")
q(1,"A suspensão ou a proibição de se obter a habilitação pode ser imposta isolada ou",["cumulativamente com outras penalidades.","apenas isoladamente.","apenas em dobro.","apenas com multa.","apenas com prisão."],"Art. 292.")
q(1,"Transitada em julgado a sentença condenatória, o réu será intimado a entregar o documento à autoridade judiciária em",["quarenta e oito horas.","dez dias.","cinco dias.","trinta dias.","vinte e quatro horas."],"Art. 293, § 1º.")
q(1,"Praticar lesão corporal culposa na direção de veículo automotor tem pena de detenção de seis meses a",["dois anos.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 303.")
q(1,"Deixar o condutor, na ocasião do sinistro, de prestar imediato socorro à vítima é crime punido com detenção de seis meses a um ano ou",["multa.","cinco anos.","reclusão.","sem pena.","perda do veículo."],"Art. 304.")
q(1,"Afastar-se o condutor do local do sinistro, para fugir à responsabilidade penal ou civil, é crime com pena de detenção de seis meses a um ano ou",["multa.","dois anos.","três anos.","prisão perpétua.","nada."],"Art. 305.")
q(1,"Conduzir veículo com capacidade psicomotora alterada por álcool é crime punido com detenção de seis meses a",["três anos, multa e suspensão ou proibição de se obter a habilitação.","um ano.","dois anos.","cinco anos.","dez anos."],"Art. 306.")
q(1,"O crime do art. 306 configura-se com concentração de álcool igual ou superior a 0,3 miligrama por litro de",["ar alveolar.","urina.","saliva.","suor.","cabelo."],"Art. 306, § 1º, I.")
q(1,"Violar a suspensão ou a proibição de se obter a habilitação é crime punido com detenção de seis meses a",["um ano e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 307.")
q(1,"Participar, na direção de veículo, de corrida em via pública, sem autorização, gerando situação de risco, tem pena de detenção de seis meses a",["três anos, multa e suspensão ou proibição.","um ano.","dois anos.","cinco anos.","dez anos."],"Art. 308.")
q(1,"Dirigir veículo automotor, em via pública, sem habilitação, gerando perigo de dano, tem pena de detenção de seis meses a um ano ou",["multa.","dois anos.","três anos.","reclusão.","nada."],"Art. 309.")
q(1,"Permitir, confiar ou entregar a direção de veículo a pessoa não habilitada é crime punido com detenção de seis meses a um ano ou",["multa.","dois anos.","três anos.","reclusão.","nada."],"Art. 310.")
q(1,"Trafegar em velocidade incompatível com a segurança nas proximidades de escolas e hospitais, gerando perigo de dano, é crime com pena de detenção de seis meses a um ano ou",["multa.","dois anos.","três anos.","reclusão.","nada."],"Art. 311.")
q(1,"Inovar artificiosamente, em caso de sinistro com vítima, o estado de lugar, de coisa ou de pessoa para induzir a erro o agente policial, o perito ou o juiz é crime punido com",["detenção de seis meses a um ano, ou multa.","reclusão de dois a cinco anos.","multa apenas.","prisão perpétua.","nada."],"Art. 312.")
q(1,"A suspensão da habilitação como medida cautelar pode ser decretada pelo",["juiz, em decisão motivada.","guarda municipal.","delegado, sozinho.","promotor, sozinho.","vizinho."],"Art. 294.")
q(1,"A suspensão da habilitação será comunicada pela autoridade judiciária ao Contran e ao órgão de trânsito do Estado",["do domicílio ou residência do réu.","do crime, apenas.","de qualquer Estado.","do juiz.","vizinho."],"Art. 295.")
q(1,"A multa reparatória consiste no pagamento, mediante depósito judicial em favor da vítima, ou seus sucessores, de quantia, sempre que houver prejuízo",["material resultante do crime.","moral apenas.","fiscal.","ambiental.","imaginário."],"Art. 297.")
q(1,"No texto da fiscalização de embriaguez, o resultado de 0,4 mg/L de ar alveolar indica concentração",["igual ou superior a 0,3 mg/L, configurando o crime do art. 306.","inferior ao limite legal.","irrelevante.","apenas infração.","nula."],"Art. 306, § 1º, I.","ctb10b")
q(1,"No texto do racha no centro, a disputa de corrida sem autorização, gerando risco, configura o crime do",["art. 308.","art. 303.","art. 304.","art. 309.","art. 312."],"Art. 308.","ctb10c")
q(1,"No texto do sinistro com vítima, o condutor que deixou o local sem socorrer o pedestre cometeu o crime de",["omissão de socorro, ainda que terceiros suprissem a omissão.","furto.","estelionato.","apropriação.","nenhum."],"Art. 304, parágrafo único.","ctb10a")
# n=2
q(2,"Na lesão corporal culposa de trânsito, aplicam-se os arts. 74, 76 e 88 da Lei 9.099/1995, exceto se o agente estiver sob influência de",["álcool ou outra substância psicoativa que determine dependência.","remédio comum.","cansaço.","medo.","pressa."],"Art. 291, § 1º, I.")
q(2,"Na lesão culposa de trânsito, os benefícios da Lei 9.099/1995 não se aplicam se o agente transitava em velocidade superior à máxima da via em",["50 km/h.","10 km/h.","20 km/h.","30 km/h.","5 km/h."],"Art. 291, § 1º, III.")
q(2,"Nas hipóteses que excluem os benefícios da Lei 9.099/1995 na lesão culposa, deverá ser instaurado",["inquérito policial.","processo civil.","processo administrativo.","termo de ajuste.","edital."],"Art. 291, § 2º.")
q(2,"A penalidade de suspensão não se inicia enquanto o sentenciado, por efeito de condenação penal, estiver",["recolhido a estabelecimento prisional.","em viagem.","de férias.","doente.","empregado."],"Art. 293, § 2º.")
q(2,"Da decisão que decretar a suspensão como medida cautelar caberá recurso",["em sentido estrito, sem efeito suspensivo.","de apelação, com efeito suspensivo.","de agravo.","de revista.","nenhum."],"Art. 294, parágrafo único.")
q(2,"Se o réu for reincidente na prática de crime de trânsito, o juiz aplicará a penalidade de",["suspensão da permissão ou habilitação para dirigir.","advertência.","multa apenas.","reclusão sempre.","nada."],"Art. 296.")
q(2,"A multa reparatória não poderá ser superior ao valor do",["prejuízo demonstrado no processo.","carro.","salário.","imposto.","seguro."],"Art. 297, § 1º.")
q(2,"Entre as circunstâncias que sempre agravam as penalidades dos crimes de trânsito está cometer a infração utilizando veículo sem placas, com placas falsas ou",["adulteradas.","novas.","pretas.","antigas.","importadas."],"Art. 298, II.")
q(2,"No homicídio culposo de trânsito, a pena aumenta de um terço à metade se o agente praticá-lo em faixa de pedestres ou",["na calçada.","na rodovia.","na garagem.","no túnel.","no posto."],"Art. 302, § 1º, II.")
q(2,"No homicídio culposo de trânsito, a pena aumenta de um terço à metade se o agente deixar de prestar socorro, quando possível sem",["risco pessoal.","autorização.","ordem judicial.","pagamento.","comunicação."],"Art. 302, § 1º, III.")
q(2,"O homicídio culposo cometido por condutor sob a influência de álcool tem pena de reclusão de",["cinco a oito anos.","dois a quatro anos.","seis meses a um ano.","um a três anos.","dez a vinte anos."],"Art. 302, § 3º.")
q(2,"A lesão corporal culposa de trânsito, com capacidade psicomotora alterada e lesão grave ou gravíssima, tem pena de reclusão de",["dois a cinco anos.","seis meses a dois anos.","três a seis anos.","um a dois anos.","dez a vinte anos."],"Art. 303, § 2º.")
q(2,"A omissão de socorro do art. 304 incide ainda que a omissão seja suprida por terceiros ou que se trate de vítima com morte instantânea ou com",["ferimentos leves.","sorte.","seguro.","testemunha.","câmera."],"Art. 304, parágrafo único.")
q(2,"A verificação da embriaguez poderá ser obtida mediante teste de alcoolemia, exame clínico, perícia, vídeo, prova testemunhal ou outros meios, observado o direito à",["contraprova.","prescrição.","anistia.","fiança.","transação."],"Art. 306, § 2º.")
q(2,"Para determinar a concentração de álcool, poderá ser empregado qualquer aparelho homologado pelo",["Inmetro.","Detran.","Município.","Ministério da Educação.","Cetran."],"Art. 306, § 4º.")
q(2,"Nas mesmas penas do art. 307 incorre o condenado que deixa de entregar, no prazo do art. 293, § 1º, a",["Permissão para Dirigir ou a CNH.","carteira de trabalho.","identidade.","certidão.","licença do veículo."],"Art. 307, parágrafo único.")
q(2,"No texto do racha no centro, a lesão corporal grave sem dolo do ciclista leva à pena de reclusão de",["três a seis anos.","seis meses a um ano.","um a dois anos.","cinco a dez anos.","dois a quatro anos."],"Art. 308, § 1º.","ctb10c")
q(2,"No texto da fiscalização de embriaguez, além do teste, o crime pode ser constatado por",["sinais que indiquem alteração da capacidade psicomotora.","o cinto afivelado.","a placa do veículo.","o horário.","o modelo do carro."],"Art. 306, § 1º, II.","ctb10b")
q(2,"No texto do sinistro com vítima, a prisão em flagrante e a fiança do art. 301 só são afastadas se o condutor tivesse prestado",["pronto e integral socorro.","apenas o nome.","apenas o documento.","apenas o telefone.","nenhuma ajuda."],"Art. 301.","ctb10a")
q(2,"Na lesão corporal culposa de trânsito, aumenta-se a pena de um terço à metade se ocorrer qualquer das hipóteses do § 1º do",["art. 302.","art. 304.","art. 306.","art. 309.","art. 311."],"Art. 303, § 1º.")
# n=3
q(3,"Assinale a alternativa que traz penas corretas.",["Art. 304: detenção de seis meses a um ano ou multa; art. 306: detenção de seis meses a três anos, multa e suspensão.","Art. 304: reclusão de cinco anos; art. 306: multa.","Art. 305: reclusão; art. 309: detenção de dez anos.","Art. 306: apenas multa.","Art. 311: reclusão de dois a quatro anos."],"Arts. 304 e 306.")
q(3,"Considere. I. O homicídio culposo de trânsito tem detenção de dois a quatro anos. II. A suspensão da habilitação dura de dois meses a cinco anos. III. Quem presta socorro é preso em flagrante. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"Quem presta socorro não é preso em flagrante (art. 301).")
q(3,"Assinale a INCORRETA.",["A embriaguez ao volante exige sempre o teste, e não pode ser provada por vídeo.","A embriaguez pode ser provada por exame clínico.","A embriaguez tem como limite 0,3 mg/L de ar alveolar.","A recusa ao teste não impede o crime se há outras provas.","O aparelho deve ser homologado pelo Inmetro."],"A prova admite vídeo e outros meios (art. 306, § 2º).")
q(3,"Nas condutas do art. 291, § 1º, aplica-se o inquérito policial, e não a composição civil e a transação penal, se o agente estiver participando de",["corrida, disputa ou competição não autorizada pela autoridade.","passeio.","desfile autorizado.","rali autorizado.","carreata."],"Art. 291, § 1º, II.")
q(3,"O juiz fixará a pena-base nos crimes de trânsito segundo as diretrizes do art. 59 do Código Penal, dando especial atenção à culpabilidade e às circunstâncias e",["consequências do crime.","fortuna do réu.","origem do réu.","idade do veículo.","hora do dia."],"Art. 291, § 4º.")
q(3,"Entre as agravantes do art. 298 está ter o condutor cometido a infração sobre faixa de trânsito destinada a",["pedestres.","motos.","ônibus apenas.","carga.","bicicletas apenas."],"Art. 298, VII.")
q(3,"Nas circunstâncias agravantes, estão a ausência de habilitação e a habilitação de categoria",["diferente da do veículo.","igual à do veículo.","superior sempre.","vencida há um dia.","digital."],"Art. 298, III e IV.")
q(3,"A substituição da pena privativa de liberdade por restritiva de direitos, nos crimes dos arts. 302 a 312, deverá ser de prestação de",["serviço à comunidade em atividades ligadas ao atendimento a vítimas de trânsito.","multa apenas.","fiança.","trabalho doméstico.","curso de idiomas."],"Art. 312-A.")
q(3,"Ao crime do art. 302, § 3º, e ao do art. 303, § 2º, não se aplica a substituição da pena privativa de liberdade prevista no art. 44, I, do",["Código Penal.","Código de Trânsito.","Código Civil.","CPC.","Código Tributário."],"Art. 312-B.")
q(3,"O crime de racha com resultado de morte, sem dolo, tem pena de reclusão de",["cinco a dez anos.","três a seis anos.","seis meses a três anos.","um a dois anos.","dois a quatro anos."],"Art. 308, § 2º.")
q(3,"A violação da suspensão da habilitação gera, além da pena, nova imposição adicional de",["idêntico prazo de suspensão ou de proibição.","prisão perpétua.","perda do veículo.","multa de dez salários.","nada."],"Art. 307.")
q(3,"O crime do art. 305 consiste em afastar-se do local do sinistro para",["fugir à responsabilidade penal ou civil.","buscar socorro.","chamar polícia.","trocar o pneu.","abastecer."],"Art. 305.")
q(3,"No art. 311, o crime de velocidade incompatível com a segurança exige que a conduta gere",["perigo de dano.","dano efetivo.","morte.","lesão grave.","prisão."],"Art. 311.")
q(3,"No art. 309, o crime de dirigir sem habilitação exige que a conduta gere",["perigo de dano.","morte.","lesão grave.","fuga.","embriaguez."],"Art. 309.")
q(3,"A multa reparatória será descontada na indenização civil do",["dano.","imposto.","seguro.","aluguel.","salário."],"Art. 297, § 3º.")
q(3,"No texto do racha no centro, o condutor da prova, além das penas do art. 308, § 1º, está sujeito à",["suspensão ou proibição de se obter a habilitação.","advertência apenas.","multa apenas.","anistia.","absolvição."],"Art. 308, caput.","ctb10c")
q(3,"No texto da fiscalização de embriaguez, a verificação poderá ser obtida com o aparelho homologado pelo",["Inmetro.","Município.","Detran.","Cetran.","Contran, sozinho."],"Art. 306, § 4º.","ctb10b")
q(3,"No texto do sinistro com vítima, o crime de omissão de socorro tem pena de detenção de seis meses a um ano ou multa, se o fato",["não constituir elemento de crime mais grave.","for leve.","for grave.","for noturno.","for diurno."],"Art. 304.","ctb10a")
q(3,"No texto do sinistro com vítima, a fuga do local para escapar à responsabilidade caracteriza o crime do",["art. 305.","art. 303.","art. 309.","art. 312.","art. 311."],"Art. 305.","ctb10a")
q(3,"A suspensão da habilitação decretada como medida cautelar, em qualquer fase da investigação, tem como fundamento a necessidade de garantia da",["ordem pública.","vontade do réu.","pressa do juiz.","imprensa.","arrecadação."],"Art. 294.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes de trânsito",[
 ("ger","Disposições gerais",["CP, CPP e Lei 9.099","suspensão: 2 meses a 5 anos","quem socorre: sem prisão em flagrante"],"seção 1"),
 ("hom","Homicídio e lesão culposos",["homicídio: detenção, 2 a 4","com álcool: reclusão, 5 a 8","lesão: 6 meses a 2 anos"],"seção 2"),
 ("soc","Socorro e fuga",["art. 304","art. 305","detenção, 6 meses a 1 ano, ou multa"],"seção 3"),
 ("alc","Embriaguez",["6 dg/L ou 0,3 mg/L","detenção, 6 meses a 3 anos","vídeo, testemunha, exame"],"seção 3"),
 ("rac","Racha",["detenção, 6 meses a 3 anos","lesão grave: 3 a 6","morte: 5 a 10"],"seção 4"),
 ("hab","Habilitação e outros",["art. 307, 309, 310","velocidade perto de escolas","inovação artificiosa"],"seção 4")],
 "Na prova: pena de cada artigo; limites de álcool; quem socorre não é preso")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7],QR,4,svg,"A primeira linha traz as disposições gerais e os crimes contra a vida e a integridade; as demais, socorro, embriaguez, racha e habilitação.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 291 a 312-B, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-10","Crimes de trânsito (CTB, arts. 291 a 312-B)",Q,list(tx),
 cobertura=["Cobertos: arts. 291 a 298, 301 a 312-B. Não detalhados: arts. 299 e 300 (vetados), art. 297, §§ 2º e 3º (parcialmente)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto, pois há projetos de aumento de penas dos arts. 302 e 303.","No texto ctb10a, a vítima 'socorrida por terceiros' deve ser relida: a omissão ainda incide (art. 304, parágrafo único).","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb10a, ctb10b e ctb10c fictícios."],
 fontes_conferidas=["CTB, arts. 291 a 312-B: texto da Câmara, copiado por programa."])
gravar("ctb-10",aula_html,banco("ctb-10",Q),tx)
