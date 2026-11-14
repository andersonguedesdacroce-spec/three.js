import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Depois de saber qual conduta é infração, vem o que acontece com o infrator. Os arts. 256 a 279 tratam de dois assuntos que a Vunesp mistura: as penalidades (advertência, multa, suspensão, cassação, curso de reciclagem), que punem, e as medidas administrativas (retenção, remoção, recolhimento de documento), que são complementares e servem para sanar a irregularidade. O guarda aplica as medidas na rua e precisa saber a diferença. A aula traz os pontos por infração, os limites de pontos para suspensão, a cassação, as medidas administrativas e as regras sobre álcool."
S={}
S[1]="## 1. Penalidades, responsabilidade, multa e pontos\n\n"+L("art. 256","Art. 256. A autoridade de trânsito","§ 2º (VETADO) § 3º A imposição")+"\n\n"+L("art. 257, caput e §§ 1º a 3º","Art. 257. As penalidades serão","§ 4º O embarcador")+"\n\n"+L("art. 257, § 7º","§ 7º Quando não for imediata","§ 8º Após o prazo")+"\n\n"+L("art. 258","Art. 258. As infrações punidas","§ 1º [revogado]")+"\n\n"+L("art. 259","Art. 259. A cada infração","§ 1º (VETADO)")+"""

As penalidades são a advertência por escrito, a multa, a suspensão do direito de dirigir, a cassação da CNH, a cassação da Permissão para Dirigir e a frequência obrigatória em curso de reciclagem. Elas não afastam as punições penais dos crimes de trânsito. Quem responde? O condutor, pelos atos praticados na direção; o proprietário, pela regularização do veículo (licenciamento, características, habilitação legal de quem dirige); e, nas cargas, o embarcador e o transportador. Quando o infrator não é identificado na hora, o proprietário tem 30 dias, contados da notificação da autuação, para indicar o condutor.

As multas classificam-se por natureza em gravíssima, grave, média e leve, e os valores constam do art. 258 (podem ser atualizados). Os pontos por infração são: gravíssima, sete; grave, cinco; média, quatro; leve, três.
"""
S[2]="## 2. Suspensão, cassação e reciclagem\n\n"+L("art. 261, caput e § 1º","Art. 261. A penalidade de suspensão","§ 2º Quando ocorrer a suspensão")+"\n\n"+L("art. 261, §§ 2º e 3º","§ 2º Quando ocorrer a suspensão","§ 4º (VETADO na Lei nº 12.619")+"\n\n"+L("art. 263, caput e § 2º","Art. 263. A cassação","§ 1º Constatada")+"\n\n"+L("art. 263, § 2º","§ 2º Decorridos dois anos","§ 3º (VETADO na Lei nº 14.304")+"\n\n"+L("arts. 265 a 268","Art. 265. As penalidades","Parágrafo único. Além do curso")+"""

A suspensão do direito de dirigir é aplicada quando o condutor soma, em 12 meses, 20 pontos (se tiver duas ou mais infrações gravíssimas), 30 pontos (se tiver uma gravíssima) ou 40 pontos (sem nenhuma gravíssima), ou quando comete infração que prevê a suspensão de forma específica. O prazo é de 6 meses a 1 ano no caso dos pontos (8 meses a 2 anos na reincidência) e de 2 a 8 meses no caso das infrações específicas. A CNH é devolvida só depois de cumprida a penalidade e feito o curso de reciclagem, e a suspensão zera os pontos.

A cassação decorre de dirigir com a habilitação suspensa, de reincidir em 12 meses em infrações graves como dirigir sob álcool ou disputar corrida, ou de condenação judicial por crime de trânsito. Só depois de dois anos o infrator pode pedir a reabilitação, refazendo todos os exames. Suspensão e cassação exigem processo administrativo com decisão fundamentada e amplo direito de defesa. A advertência por escrito só vale para infração leve ou média e para quem não tenha cometido outra infração nos últimos 12 meses. O curso de reciclagem é exigido de quem teve a direção suspensa, se envolveu em sinistro grave para o qual contribuiu, foi condenado por crime de trânsito ou coloca em risco a segurança.
"""
S[3]="## 3. Medidas administrativas\n\n"+L("art. 269, caput","Art. 269. A autoridade de trânsito","§ 1º A ordem, o consentimento")+"\n\n"+L("art. 269, §§ 1º a 3º","§ 1º A ordem, o consentimento","§ 4º Aplica-se aos animais")+"\n\n"+L("art. 270","Art. 270. O veiculo poderá ser retido","§ 5º A critério do agente")+"\n\n"+L("art. 271, caput e § 1º","Art. 271. O veiculo será removido","§ 1º, com redação dada")+"\n\n"+L("arts. 272 a 275","Art. 272. O recolhimento da Carteira","Art. 276.")+"""

Medidas administrativas são retenção e remoção do veículo, recolhimento dos documentos (CNH, Permissão, Certificado de Registro, Licenciamento Anual), transbordo do excesso de carga, teste de alcoolemia e perícia de substância entorpecente, recolhimento de animais soltos e realização de exames de aptidão. O objetivo prioritário é a proteção à vida e à incolumidade física da pessoa, e as medidas não eliminam a penalidade, apenas a complementam.

Na retenção, se a irregularidade puder ser sanada no local, o veículo é liberado logo. Se não, e se o veículo oferecer condições de segurança, é entregue a condutor habilitado mediante recolhimento do Certificado de Licenciamento Anual, com prazo de até 30 dias para regularizar. Sem condutor habilitado no local, o veículo é removido a depósito. Na remoção, a restituição só ocorre após o pagamento de multas, taxas e despesas de remoção e estada, e a liberação exige reparo de componente obrigatório defeituoso. O recolhimento da CNH e da Permissão se faz mediante recibo, além dos casos previstos, quando houver suspeita de adulteração; o Certificado de Registro, quando o veículo alienado não tiver a propriedade transferida em 30 dias; o Licenciamento Anual, quando vencido ou na retenção sem possibilidade de sanar no local.
"""
S[4]="## 4. Álcool, fiscalização e outros casos\n\n"+L("arts. 276 e 277","Art. 276. Qualquer concentração","Art. 278.")+"\n\n"+L("arts. 278 a 279","Art. 278. Ao condutor que se evadir","Art. 279-A.")+"""

Qualquer concentração de álcool por litro de sangue ou de ar alveolar sujeita o condutor às penalidades do art. 165, e o Contran disciplina as margens de tolerância dos aparelhos de medição. O condutor envolvido em sinistro ou que for alvo de fiscalização pode ser submetido a teste, exame clínico ou perícia. A embriaguez também pode ser caracterizada por imagem, vídeo, sinais de alteração da capacidade psicomotora ou outras provas admitidas. Quem se recusa a qualquer procedimento sofre as penalidades e medidas do art. 165-A.

Quem foge à pesagem obrigatória sofre a penalidade do art. 209 e deve retornar ao ponto de evasão; quem foge da ação policial tem o veículo apreendido assim que localizado, com as penalidades do art. 210. O condutor condenado por usar veículo em receptação, descaminho ou contrabando tem a habilitação cassada ou fica proibido de obtê-la por 5 anos. O disco ou a unidade do registrador instantâneo de velocidade e tempo, em sinistro com vítima, só pode ser retirado pelo perito oficial.
"""
S[5]="""## 5. Na rotina do guarda

- **Documentos:** o guarda recolhe a CNH quando suspensa ou cassada, ou se houver suspeita de adulteração, sempre mediante recibo.
- **Retenção:** se o problema pode ser resolvido ali, o veículo é liberado; se não, entrega-se a condutor habilitado, recolhendo-se o Licenciamento Anual.
- **Remoção:** sem condutor habilitado, o veículo vai ao depósito, e a restituição exige pagamento de multas, taxas e despesas.
- **Teste do bafômetro:** a recusa tem a mesma penalidade da embriaguez; sinais de alteração e vídeo também provam a infração.
- **Pontos:** o agente registra a infração; a suspensão decorre de processo administrativo, não da abordagem.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pontos por natureza | Gravíssima 7, grave 5, média 4, leve 3 |
| Limite para suspensão | 20 (2 ou mais gravíssimas), 30 (1 gravíssima), 40 (nenhuma), em 12 meses |
| Prazo da suspensão | 6 meses a 1 ano (pontos); 2 a 8 meses (infração específica) |
| Cassação | Dirigir suspenso, reincidência em 12 meses, condenação judicial |
| Reabilitação | Depois de 2 anos da cassação |
| Advertência | Só leve ou média e sem outra infração em 12 meses |
| Retenção x remoção | Retenção: libera se sanar ou entrega a habilitado; remoção: depósito |
| Prazo na retenção | Até 30 dias para regularizar, com o Licenciamento recolhido |
| Penalidade x medida | Medida complementa, não substitui, a penalidade |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Penalidades | Advertência, multa, suspensão, cassação, reciclagem |
| Pontos | 7, 5, 4 e 3 |
| Suspensão por pontos | 20, 30 ou 40 em 12 meses |
| Suspensão: prazo | 6 meses a 1 ano |
| Cassação | Dirigir suspenso; reincidência; condenação |
| Reabilitação | 2 anos após cassação |
| Medidas administrativas | Retenção, remoção, recolhimento, transbordo, teste |
| Retenção | Liberar se sanado; 30 dias com CRLV recolhido |
| Remoção | Depósito; pagamento de multas e despesas |
| Álcool | Qualquer concentração; recusa = art. 165-A |
"""
QR=[("Questão 1","De acordo com o Código, a cada infração gravíssima são computados",["sete pontos.","três pontos.","quatro pontos.","cinco pontos.","dez pontos."],0,"Art. 259, I."),
("Questão 2","A penalidade de suspensão do direito de dirigir é imposta, por pontuação, em 12 meses, quando o infrator atingir 20 pontos, caso constem",["duas ou mais infrações gravíssimas.","nenhuma infração gravíssima.","uma infração gravíssima.","apenas infrações leves.","apenas infrações médias."],1,"Art. 261, I, a."),
("Questão 3","A cassação do documento de habilitação ocorre, entre outros casos, quando o infrator, suspenso o direito de dirigir,",["conduzir qualquer veículo.","pagar a multa.","fizer o curso.","vender o veículo.","mudar de endereço."],2,"Art. 263, I."),
("Questão 4","A medida administrativa de retenção do veículo, quando não for possível sanar a irregularidade no local, permite a liberação a condutor habilitado mediante recolhimento do",["Certificado de Licenciamento Anual, com prazo de até 30 dias para regularizar.","Certificado de Registro.","CNH do proprietário.","título de eleitor.","recibo do IPVA."],3,"Art. 270, § 2º.")]
t1="<strong>Pontuação do motorista</strong><br><br>Um motorista particular de Vila Nova, cidade fictícia, acumulou em 12 meses duas infrações gravíssimas, uma grave e uma média. O órgão de trânsito analisa a aplicação de penalidades."
t2="<strong>Veículo sem licenciamento</strong><br><br>Uma equipe da guarda abordou um automóvel com licenciamento vencido, dirigido por um condutor habilitado. A irregularidade não pôde ser sanada no local."
t3="<strong>Recusa em fiscalização</strong><br><br>Em operação de fiscalização, um condutor com odor de álcool e fala arrastada recusou-se a fazer o teste do etilômetro e o exame clínico."
tx={"ctb8a":t1,"ctb8b":t2,"ctb8c":t3}
# n=1
q(1,"Entre as penalidades previstas no Código estão a advertência por escrito, a multa e a",["suspensão do direito de dirigir.","prisão administrativa.","perda do veículo, sempre.","demissão.","interdição da via."],"Art. 256.")
q(1,"As penalidades de trânsito não elidem as punições originárias de ilícitos penais decorrentes de",["crimes de trânsito.","contravenções de trabalho.","infrações tributárias, apenas.","infrações civis.","atos de condomínio."],"Art. 256, § 1º.")
q(1,"Ao condutor caberá a responsabilidade pelas infrações decorrentes de atos praticados",["na direção do veículo.","na venda do veículo.","na garagem.","no licenciamento.","na compra."],"Art. 257, § 3º.")
q(1,"Quando não for imediata a identificação do infrator, o prazo para apresentá-lo é de",["30 dias, contado da notificação da autuação.","5 dias.","10 dias.","60 dias.","90 dias."],"Art. 257, § 7º.")
q(1,"A infração de natureza média gera, por infração, o seguinte número de pontos:",["quatro.","sete.","cinco.","três.","dois."],"Art. 259, III.")
q(1,"A infração de natureza grave gera",["cinco pontos.","sete pontos.","quatro pontos.","três pontos.","dois pontos."],"Art. 259, II.")
q(1,"A infração de natureza leve gera",["três pontos.","sete pontos.","cinco pontos.","quatro pontos.","um ponto."],"Art. 259, IV.")
q(1,"Segundo o Código, as infrações punidas com multa classificam-se, de acordo com a gravidade, em",["quatro categorias.","duas categorias.","três categorias.","cinco categorias.","seis categorias."],"Art. 258.")
q(1,"O infrator que atinge, em 12 meses, 40 pontos, sem nenhuma infração gravíssima, fica sujeito à",["suspensão do direito de dirigir.","advertência.","cassação imediata.","prisão.","multa em dobro."],"Art. 261, I, c.")
q(1,"A suspensão do direito de dirigir por pontos tem prazo de seis meses a",["um ano.","dois anos.","três anos.","oito meses.","dezoito meses."],"Art. 261, § 1º, I.")
q(1,"Cumprida a suspensão do direito de dirigir, a CNH será devolvida após cumprida a penalidade e o curso de",["reciclagem.","direção defensiva, apenas.","idiomas.","formação.","primeiros socorros, apenas."],"Art. 261, § 2º.")
q(1,"Decorridos dois anos da cassação, o infrator poderá requerer sua",["reabilitação.","renovação.","transferência.","aposentadoria.","anistia."],"Art. 263, § 2º.")
q(1,"As penalidades de suspensão e de cassação são aplicadas por decisão fundamentada, em processo administrativo, assegurado ao infrator amplo direito de",["defesa.","recurso ao Judiciário, apenas.","prescrição.","transação.","anistia."],"Art. 265.")
q(1,"Quando o infrator cometer simultaneamente duas ou mais infrações, serão aplicadas as respectivas penalidades",["cumulativamente.","apenas a mais grave.","apenas a mais leve.","alternativamente.","em ordem alfabética."],"Art. 266.")
q(1,"A medida administrativa de retenção do veículo pode ser aplicada nos casos",["expressos no Código.","a critério do dono do veículo.","apenas em rodovias.","apenas à noite.","apenas em dias úteis."],"Art. 270, caput.")
q(1,"O veículo será removido, nos casos previstos no Código, para o",["depósito fixado pelo órgão ou entidade competente.","pátio da residência do proprietário.","posto de combustível.","consultório.","cartório."],"Art. 271, caput.")
q(1,"O objetivo prioritário das medidas administrativas é a proteção à vida e à",["incolumidade física da pessoa.","arrecadação.","propriedade do veículo.","fluidez, apenas.","imagem do órgão."],"Art. 269, § 1º.")
q(1,"A CNH, a Permissão para Dirigir e a Autorização para Conduzir Ciclomotor são",["documentos de habilitação.","documentos do veículo.","certificados de registro.","licenças de transporte.","títulos."],"Art. 269, § 3º.")
q(1,"No texto do veículo sem licenciamento, a medida administrativa prevista no art. 270, § 2º, é o recolhimento do Certificado de Licenciamento Anual e a liberação do veículo a",["condutor regularmente habilitado.","qualquer pessoa.","fiador.","oficial de justiça.","despachante."],"Art. 270, § 2º.","ctb8b")
q(1,"No texto da recusa em fiscalização, a recusa ao teste e ao exame sujeita o condutor às penalidades e medidas do",["art. 165-A.","art. 167.","art. 169.","art. 172.","art. 181."],"Art. 277, § 3º.","ctb8c")
# n=2
q(2,"As penalidades serão impostas ao condutor, ao proprietário, ao embarcador e ao",["transportador.","vizinho.","fiscal.","vendedor.","comprador."],"Art. 257, caput.")
q(2,"Ao proprietário caberá sempre a responsabilidade pela infração referente à prévia regularização e às formalidades exigidas para o trânsito do",["veículo na via terrestre.","condutor no exterior.","pedestre.","agente.","semáforo."],"Art. 257, § 2º.")
q(2,"Ao condutor identificado será atribuída pontuação pelas infrações de sua responsabilidade, exceto, entre outras, as",["puníveis de forma específica com suspensão do direito de dirigir.","de natureza leve.","de natureza média.","cometidas à noite.","cometidas na cidade."],"Art. 259, § 4º, III.")
q(2,"As multas serão impostas e arrecadadas pelo órgão ou entidade de trânsito",["com circunscrição sobre a via onde haja ocorrido a infração.","do licenciamento do veículo.","do domicílio do condutor.","da União, sempre.","do Estado vizinho."],"Art. 260.")
q(2,"Quando a infração for cometida com veículo licenciado no exterior, a multa deverá ser paga",["antes de sua saída do País.","depois de 1 ano.","apenas no exterior.","em 10 anos.","nunca."],"Art. 260, § 4º.")
q(2,"A imposição da suspensão do direito de dirigir elimina a quantidade de",["pontos computados, para fins de contagem subsequente.","multas já pagas.","infrações.","registros.","documentos."],"Art. 261, § 3º.")
q(2,"Em caso de reincidência em 12 meses, a suspensão do direito de dirigir por pontos terá prazo de",["8 meses a 2 anos.","6 meses a 1 ano.","2 a 8 meses.","1 a 3 anos.","3 a 5 anos."],"Art. 261, § 1º, I.")
q(2,"A suspensão do direito de dirigir por infração que a preveja de forma específica tem prazo, em regra, de",["2 a 8 meses.","6 meses a 1 ano.","1 a 2 anos.","3 a 5 anos.","10 anos."],"Art. 261, § 1º, II.")
q(2,"O condutor que exerce atividade remunerada ao veículo é suspenso ao atingir 40 pontos, e pode fazer curso preventivo de reciclagem ao atingir",["30 pontos em 12 meses.","20 pontos.","10 pontos.","50 pontos.","60 pontos."],"Art. 261, § 5º.")
q(2,"A cassação do documento de habilitação dar-se-á no caso de reincidência, em 12 meses, das infrações dos arts. 163, 164, 165, 173, 174 e 175 e do inciso III do",["art. 162.","art. 167.","art. 169.","art. 172.","art. 181."],"Art. 263, II.")
q(2,"A penalidade de advertência por escrito é aplicada à infração leve ou média passível de multa, se o infrator não tiver cometido nenhuma outra infração nos últimos",["12 meses.","6 meses.","3 meses.","24 meses.","36 meses."],"Art. 267.")
q(2,"O infrator será submetido a curso de reciclagem quando suspenso do direito de dirigir ou quando se envolver em",["sinistro grave para o qual haja contribuído.","qualquer sinistro.","infração leve.","infração média.","multa."],"Art. 268, II e III.")
q(2,"Os documentos recolhidos pela autoridade, entre as medidas administrativas, incluem o Certificado de Registro e o",["Certificado de Licenciamento Anual.","título de eleitor.","comprovante de residência.","passaporte.","contrato de seguro."],"Art. 269, V e VI.")
q(2,"A restituição do veículo removido ocorrerá mediante prévio pagamento de multas, taxas e despesas com",["remoção e estada.","combustível.","reparo, apenas.","seguro.","publicidade."],"Art. 271, § 1º.")
q(2,"O recolhimento do Certificado de Registro dar-se-á, entre outros casos, se, alienado o veículo, não for transferida sua propriedade no prazo de",["trinta dias.","dez dias.","sessenta dias.","noventa dias.","um ano."],"Art. 273, II.")
q(2,"O transbordo da carga com peso excedente é condição para que o veículo possa prosseguir viagem e será efetuado às expensas do",["proprietário do veículo.","poder público.","agente.","vizinho.","embarcador, sempre."],"Art. 275.")
q(2,"Qualquer concentração de álcool por litro de sangue ou de ar alveolar sujeita o condutor às penalidades do",["art. 165.","art. 167.","art. 169.","art. 181.","art. 208."],"Art. 276.")
q(2,"No texto da pontuação do motorista, com 23 pontos em 12 meses e duas infrações gravíssimas, o órgão de trânsito pode aplicar a penalidade de",["suspensão do direito de dirigir.","cassação imediata da CNH.","apenas advertência por escrito.","prisão administrativa.","nenhuma penalidade, pois não atingiu 40 pontos."],"Duas gravíssimas somam 14; com a grave e a média, 23, acima do limite de 20 pontos (art. 261, I, a).","ctb8a")
q(2,"No texto da recusa em fiscalização, além do teste, também poderia ser usada, para caracterizar a infração do art. 165, a constatação de sinais que indiquem",["alteração da capacidade psicomotora.","o cinto não afivelado.","a placa suja.","o veículo velho.","a música alta."],"Art. 277, § 2º.","ctb8c")
q(2,"No texto do veículo sem licenciamento, o prazo razoável para regularizar a situação, que não pode ser superior, é de",["30 dias.","10 dias.","60 dias.","90 dias.","1 ano."],"Art. 270, § 2º.","ctb8b")
# n=3
q(3,"Assinale a alternativa correta sobre a suspensão por pontos em 12 meses.",["20 pontos se houver duas ou mais gravíssimas; 30 se houver uma; 40 se não houver nenhuma.","20 pontos se não houver gravíssima.","30 pontos se houver duas gravíssimas.","40 pontos se houver uma gravíssima.","10 pontos em qualquer caso."],"Art. 261, I.")
q(3,"Considere. I. Gravíssima, 7 pontos. II. Média, 4 pontos. III. Leve, 5 pontos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A leve gera 3 pontos (art. 259, IV).")
q(3,"Assinale a INCORRETA.",["A cassação decorre de qualquer multa leve.","A cassação decorre de dirigir com a CNH suspensa.","A cassação decorre de condenação judicial por crime de trânsito.","A reabilitação pode ser requerida após 2 anos da cassação.","A suspensão elimina os pontos computados."],"A multa leve não gera cassação (art. 263).")
q(3,"A pontuação de infração praticada por passageiro de ônibus de longa distância, em rodovias, não é atribuída ao condutor quando for relativa ao",["cinto de segurança dos passageiros usuários.","álcool do condutor.","excesso de velocidade.","sinal vermelho.","documento do veículo."],"Art. 259, § 4º, I, com o art. 65.")
q(3,"O proprietário poderá indicar o principal condutor do veículo, que, após aceitar a indicação, terá seu nome inscrito no cadastro do veículo no",["Renavam.","Renach.","Sinesp.","Detran.","Caged."],"Art. 257, § 10.")
q(3,"Se, após o prazo de 30 dias, o infrator não tiver sido identificado e o veículo for de pessoa jurídica, será lavrada nova multa ao proprietário, de valor igual a",["2 vezes o da multa originária.","3 vezes.","1 vez.","5 vezes.","10 vezes."],"Art. 257, § 8º.")
q(3,"Na retenção, se não for possível sanar a falha no local, o veículo que ofereça condições de segurança deverá ser liberado a condutor habilitado, mediante recolhimento do",["Certificado de Licenciamento Anual, contra recibo.","Certificado de Registro.","CNH.","documento de identidade.","título."],"Art. 270, § 2º.")
q(3,"Não se apresentando condutor habilitado no local da infração, o veículo será",["removido a depósito.","entregue a qualquer pessoa.","liberado.","destruído.","vendido."],"Art. 270, § 4º.")
q(3,"A critério do agente, não se dará a retenção imediata do veículo de transporte coletivo que transporte passageiros, desde que ofereça",["condições de segurança para circulação.","luxo.","seguro de vida.","placa nova.","pintura."],"Art. 270, § 5º.")
q(3,"Não caberá remoção nos casos em que a irregularidade for",["sanada no local da infração.","grave.","gravíssima.","leve.","de documentos."],"Art. 271, § 9º.")
q(3,"O pagamento das despesas de remoção e estada é limitado ao prazo de",["6 meses.","30 dias.","1 ano.","2 anos.","3 meses."],"Art. 271, § 10.")
q(3,"O recolhimento do Certificado de Licenciamento Anual dar-se-á, entre outros casos, se o prazo de licenciamento estiver",["vencido.","em vigor.","em andamento.","suspenso.","em dobro."],"Art. 274, II.")
q(3,"O condutor que se evadir da fiscalização, não submetendo o veículo à pesagem obrigatória, sofre a penalidade do art. 209, além da obrigação de",["retornar ao ponto de evasão para a pesagem.","pagar pensão.","fazer curso.","vender o veículo.","mudar de rota."],"Art. 278.")
q(3,"No caso de fuga do condutor à ação policial, o veículo será apreendido tão logo seja localizado, aplicando-se também as penalidades do",["art. 210.","art. 169.","art. 172.","art. 181.","art. 208."],"Art. 278, parágrafo único.")
q(3,"O condutor condenado em decisão transitada em julgado por usar veículo para receptação, descaminho ou contrabando terá a habilitação cassada ou será proibido de obtê-la por",["5 anos.","1 ano.","2 anos.","10 anos.","6 meses."],"Art. 278-A.")
q(3,"No texto da pontuação do motorista, a soma de pontos do motorista, com duas gravíssimas, uma grave e uma média, é de",["23 pontos.","12 pontos.","14 pontos.","18 pontos.","30 pontos."],"7 + 7 + 5 + 4 = 23.","ctb8a")
q(3,"No texto da pontuação do motorista, o limite para suspensão com duas ou mais gravíssimas é de",["20 pontos em 12 meses.","30 pontos.","40 pontos.","10 pontos.","15 pontos."],"Art. 261, I, a.","ctb8a")
q(3,"No texto do veículo sem licenciamento, o veículo não removido é liberado e o condutor é considerado notificado para regularizar a situação",["na mesma ocasião.","em 90 dias.","no ano seguinte.","por edital apenas.","depois do depósito."],"Art. 270, § 2º.","ctb8b")
q(3,"No texto da recusa em fiscalização, a recusa a qualquer dos procedimentos do art. 277 sujeita o condutor às penalidades e às medidas administrativas do",["art. 165-A.","art. 165-C.","art. 167.","art. 169.","art. 183."],"Art. 277, § 3º.","ctb8c")
q(3,"No texto da recusa em fiscalização, a infração do art. 165-A é do tipo",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 165-A.","ctb8c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Penalidades e medidas administrativas",[
 ("pen","Penalidades",["advertência, multa","suspensão, cassação","reciclagem"],"seção 1"),
 ("pts","Pontos",["gravíssima 7, grave 5","média 4, leve 3","20, 30 ou 40 em 12 meses"],"seção 2"),
 ("sus","Suspensão e cassação",["6 meses a 1 ano","dirigir suspenso: cassação","reabilitação em 2 anos"],"seção 2"),
 ("med","Medidas administrativas",["retenção","remoção","recolhimento de documento"],"seção 3"),
 ("ret","Retenção e remoção",["sanar no local","30 dias com CRLV","depósito e pagamento"],"seção 3"),
 ("alc","Álcool",["qualquer concentração","recusa = art. 165-A","sinais e vídeo"],"seção 4")],
 "Na prova: penalidade pune; medida complementa; confira os pontos e os prazos")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7],QR,4,svg,"A primeira linha traz as penalidades e os pontos; as demais, suspensão, medidas administrativas e álcool.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 256 a 279-A, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-8","Penalidades e medidas administrativas (CTB, arts. 256 a 279-A)",Q,list(tx),
 cobertura=["Cobertos: arts. 256 a 263, 265 a 271, 272 a 279. Não detalhados: art. 257, §§ 4º a 6º (embarcador e transportador), art. 260, §§ 1º a 3º, art. 268-A (RNPC), art. 271, §§ 3º a 9º-D."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Os valores das multas (art. 258) não são cobrados nas questões; o texto da aula adverte que podem ser atualizados.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb8a, ctb8b e ctb8c fictícios."],
 fontes_conferidas=["CTB, arts. 256 a 279-A: texto da Câmara, copiado por programa."])
gravar("ctb-8",aula_html,banco("ctb-8",Q),tx)
