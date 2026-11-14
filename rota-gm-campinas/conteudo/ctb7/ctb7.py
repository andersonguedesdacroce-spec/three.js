import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Capítulo XV é o maior do Código: são mais de noventa artigos, cada um descrevendo uma conduta e dizendo, em três linhas fixas, a natureza da infração (leve, média, grave ou gravíssima), a penalidade (multa, suspensão, apreensão) e a medida administrativa (retenção, remoção, recolhimento). A Vunesp cobra as infrações mais comuns na rua: dirigir sem habilitação, embriaguez, cinto, criança, sinal vermelho, velocidade, contramão, estacionamento. O que mais derruba é a natureza da infração e a penalidade: o candidato acerta a conduta, mas erra se é grave ou gravíssima, ou se há suspensão. A aula traz a lei e separa as infrações por assunto; o valor das multas e a pontuação ficam para a aula seguinte."
S={}
S[1]="## 1. Direção sem habilitação e embriaguez\n\n"+L("art. 161","Art. 161. Constitui infração","Parágrafo único. [revogado]")+"\n\n"+L("art. 162","Art. 162. Dirigir veículo:","Art. 163.")+"\n\n"+L("art. 165 e 165-A","Art. 165. Dirigir sob a influência","Art. 165-B.")+"\n\n"+L("arts. 165-B a 165-D","Art. 165-B. Dirigir veículo sem realizar","Art. 166.")+"""

Dirigir sem habilitação, com habilitação cassada ou suspensa, com categoria diferente da do veículo ou com a CNH vencida há mais de 30 dias é infração gravíssima, e a medida administrativa é a retenção do veículo até que apareça um condutor habilitado. A multa varia: três vezes para quem não tem CNH ou está com ela cassada ou suspensa, duas vezes para categoria diferente, e multa simples para a CNH vencida há mais de 30 dias. O mesmo vale para quem entrega a direção ou permite que alguém nessas condições assuma o veículo.

Dirigir sob a influência de álcool ou de outra substância psicoativa que determine dependência, e recusar-se a fazer o teste ou exame, são infrações gravíssimas com multa de dez vezes e suspensão do direito de dirigir por 12 meses, com recolhimento do documento e retenção do veículo. A multa dobra na reincidência em até 12 meses. A recusa tem a mesma penalidade que a embriaguez. Quanto ao exame toxicológico, não realizá-lo (após o 30º dia do vencimento) ou dirigir com resultado positivo é gravíssima, com multa de cinco vezes.
"""
S[2]="## 2. Condução com segurança, corridas e sinistros\n\n"+L("arts. 166 a 172","Art. 166. Confiar ou entregar","Art. 173.")+"\n\n"+L("arts. 173 a 175","Art. 173. Disputar corrida:","Art. 176.")+"\n\n"+L("arts. 176 a 178","Art. 176. Deixar o condutor envolvido em sinistro com vítima:","Art. 181.")+"""

Cinto de segurança não usado é infração grave, com retenção do veículo até a colocação do cinto. Transportar crianças sem as normas de segurança especiais é gravíssima, com retenção até a irregularidade ser sanada. Dirigir sem atenção ou sem os cuidados indispensáveis é leve. Dirigir ameaçando pedestres ou outros veículos é gravíssima, com multa e suspensão. Arremessar água ou detritos e atirar objetos ou abandoná-los na via são infrações médias.

Disputar corrida, promover competição ou exibição de perícia sem permissão da autoridade e fazer manobra perigosa (arrancada brusca, derrapagem, frenagem com deslizamento) são gravíssimas, com multa de dez vezes, suspensão do direito de dirigir e apreensão do veículo; a multa dobra na reincidência em 12 meses. A penalidade alcança os promotores e os participantes.

Deixar o condutor envolvido em sinistro com vítima de prestar socorro, de evitar perigo para o trânsito, de preservar o local, de remover o veículo quando determinado ou de se identificar é gravíssima, com multa de cinco vezes e suspensão do direito de dirigir. Deixar de prestar socorro quando solicitado pela autoridade é grave. Deixar de remover o veículo após sinistro sem vítima, quando necessário, é média.
"""
S[3]="## 3. Circulação, sinal e velocidade\n\n"+L("art. 186","Art. 186. Transitar pela contramão","Art. 187.")+"\n\n"+L("arts. 191 a 196","Art. 191. Forçar passagem","Art. 203.")+"\n\n"+L("art. 203","Art. 203. Ultrapassar pela contramão","Art. 206.")+"\n\n"+L("arts. 208 e 210","Art. 208. Avançar o sinal vermelho","Art. 218.")+"\n\n"+L("art. 218","Art. 218. Transitar em velocidade superior","Art. 219.")+"""

Na contramão: nas vias de duplo sentido é grave (exceto para ultrapassar, e só pelo tempo necessário); nas vias de sentido único é gravíssima. Ultrapassar pela contramão em curva, faixa de pedestres, ponte, viaduto, túnel, fila parada ou onde houver linha dupla contínua é gravíssima, multa de cinco vezes. Forçar passagem entre veículos em sentidos opostos na ultrapassagem é gravíssima, com multa de dez vezes e suspensão.

Avançar o sinal vermelho é gravíssima. Transpor bloqueio viário policial é gravíssima, com multa, apreensão do veículo e suspensão do direito de dirigir; já o bloqueio viário comum é grave. Desobedecer às ordens do agente de trânsito é grave, e também é grave deixar de indicar a manobra com antecedência por seta ou gesto. Transitar em calçadas, passeios, ciclovias, ciclofaixas, canteiros e acostamentos é gravíssima, com multa de três vezes. Em todas as vias, deixar de manter a distância de segurança é grave.

O excesso de velocidade tem escala: até 20% acima da máxima, média; acima de 20% até 50%, grave; acima de 50%, gravíssima, com multa de três vezes e suspensão do direito de dirigir. Andar abaixo da metade da velocidade máxima da via, retardando o trânsito, é média.
"""
S[4]="## 4. Estacionar, parar e veículo irregular\n\n"+L("art. 181, I a V","Art. 181. Estacionar o veículo:","VI - junto ou sobre hidrantes")+"\n\n"+L("art. 183","Art. 183. Parar o veículo sobre a faixa","Art. 184.")+"\n\n"+L("art. 221","Art. 221. Portar no veículo placas","Art. 230.")+"\n\n"+L("art. 230, I a VI","Art. 230. Conduzir o veículo:","VII - com a cor")+"""

Estacionar a menos de cinco metros das esquinas é média; afastado do meio-fio de 50 cm a 1 m é leve, e a mais de 1 m é grave; na pista de rolamento de rodovias, vias de trânsito rápido ou vias com acostamento é gravíssima. Em todos esses casos a medida é a remoção do veículo. Parar sobre a faixa de pedestres na mudança do sinal é média.

As placas fora das especificações do Contran são infração média, com retenção do veículo e apreensão das placas. Conduzir veículo com identificação violada ou falsificada, sem placa, com placa ilegível, não registrado e licenciado, com dispositivo antirradar ou transportando passageiros em compartimento de carga é gravíssima, com multa e apreensão do veículo.
"""
S[5]="""## 5. Na rotina do guarda

- **Sem CNH ou suspensa:** o veículo é retido até aparecer outro condutor habilitado. Se a CNH está suspensa ou cassada, o documento é recolhido.
- **Embriaguez:** a recusa ao teste tem a mesma penalidade da embriaguez, e o agente deve registrar a recusa e os sinais de embriaguez.
- **Sinistro com vítima:** o guarda preserva o local e orienta o socorro; o condutor que foge responde pela infração gravíssima.
- **Velocidade:** a natureza depende do percentual acima do limite, não do valor em km/h.
- **Estacionamento:** a distância do meio-fio e o local mudam a natureza da infração.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Natureza da infração | Memorize as gravíssimas: sem CNH, álcool, recusa, sinal vermelho, contramão em via de sentido único, corrida, calçada |
| Suspensão do direito de dirigir | Aparece em álcool, recusa, corrida, manobra perigosa, ameaça a pedestres, velocidade acima de 50% |
| Multa em múltiplos | Sem CNH: 3 vezes; categoria diferente: 2 vezes; álcool: 10 vezes; corrida: 10 vezes |
| Reincidência em 12 meses | A multa dobra (álcool, recusa, corrida, manobra) |
| Velocidade | Até 20%: média; até 50%: grave; acima: gravíssima |
| Estacionar x parar | Estacionar mais de 1 m do meio-fio é grave; parar mais de 1 m é média |
| Bloqueio viário | Comum: grave; policial: gravíssima |
| Cinto | Grave, com retenção do veículo até colocar o cinto |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Sem CNH | Gravíssima; multa 3x; retenção do veículo |
| Álcool / recusa | Gravíssima; multa 10x; suspensão de 12 meses |
| Cinto | Grave |
| Criança sem equipamento | Gravíssima; retenção |
| Sem atenção | Leve |
| Corrida / manobra perigosa | Gravíssima; 10x; suspensão; apreensão |
| Sinistro com vítima (fuga) | Gravíssima; 5x; suspensão |
| Sinal vermelho | Gravíssima |
| Contramão | Duplo sentido: grave; sentido único: gravíssima |
| Velocidade | 20%: média; 50%: grave; acima: gravíssima |
| Calçadas e ciclovias | Gravíssima; 3x |
| Bloqueio policial | Gravíssima; multa, apreensão, suspensão |
"""
QR=[("Questão 1","Dirigir veículo sem possuir Carteira Nacional de Habilitação é infração",["gravíssima, com multa e retenção do veículo até a apresentação de condutor habilitado.","leve, com advertência.","média, com multa.","grave, sem medida administrativa.","gravíssima, sem multa."],0,"Art. 162, I."),
("Questão 2","Dirigir sob a influência de álcool tem como penalidade multa de dez vezes e suspensão do direito de dirigir por",["12 meses.","3 meses.","6 meses.","24 meses.","36 meses."],1,"Art. 165."),
("Questão 3","Transitar em velocidade superior à máxima permitida em mais de 20% e até 50% é infração",["grave.","leve.","média.","gravíssima.","sem natureza definida."],2,"Art. 218, II."),
("Questão 4","Deixar o condutor ou passageiro de usar o cinto de segurança é infração",["grave, com retenção do veículo até a colocação do cinto.","gravíssima.","leve.","média.","sem penalidade."],3,"Art. 167.")]
t1="<strong>Operação em avenida</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, fiscalizava uma avenida com limite de 60 km/h. Um veículo foi medido a 75 km/h por equipamento hábil. Mais adiante, outro condutor, ao ver a operação, recusou-se a fazer o teste do etilômetro."
t2="<strong>Sinistro na esquina</strong><br><br>Em Vila Nova, um motorista bateu em um ciclista e, sem prestar socorro, deixou o local. Uma testemunha anotou a placa e acionou a guarda."
t3="<strong>Veículo sem placa</strong><br><br>Durante o patrulhamento, uma equipe da guarda de Vila Nova parou um automóvel sem a placa traseira. O condutor tinha CNH da categoria B, mas a CNH estava vencida havia 40 dias."
tx={"ctb7a":t1,"ctb7b":t2,"ctb7c":t3}
# n=1
q(1,"Constitui infração de trânsito a inobservância de qualquer preceito do Código ou da legislação complementar, e o infrator sujeita-se às penalidades e às",["medidas administrativas indicadas em cada artigo do Capítulo.","regras do direito civil, apenas.","leis estaduais, apenas.","normas do condomínio.","sanções do contrato."],"Art. 161.")
q(1,"Dirigir veículo com a CNH vencida há mais de 30 dias é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 162, V.")
q(1,"Dirigir com CNH de categoria diferente da do veículo é infração gravíssima com multa de",["duas vezes.","três vezes.","cinco vezes.","dez vezes.","uma vez."],"Art. 162, III.")
q(1,"Dirigir com a CNH suspensa ou cassada é infração gravíssima, com multa de",["três vezes.","duas vezes.","cinco vezes.","dez vezes.","uma vez."],"Art. 162, II.")
q(1,"A medida administrativa de quem dirige sem possuir CNH é a retenção do veículo até a apresentação de",["condutor habilitado.","fiador.","advogado.","despachante.","perito."],"Art. 162, I.")
q(1,"Dirigir sob a influência de álcool é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 165.")
q(1,"Recusar-se a ser submetido a teste de alcoolemia é infração",["gravíssima, com a mesma penalidade da embriaguez.","leve.","média.","grave, sem multa.","sem penalidade."],"Art. 165-A.")
q(1,"A multa por dirigir sob influência de álcool é aplicada em dobro em caso de reincidência no período de até",["12 meses.","6 meses.","3 meses.","24 meses.","36 meses."],"Art. 165, parágrafo único.")
q(1,"Deixar o condutor ou passageiro de usar o cinto de segurança é infração",["grave.","leve.","média.","gravíssima.","sem natureza."],"Art. 167.")
q(1,"Transportar crianças em veículo automotor sem observância das normas de segurança especiais é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 168.")
q(1,"Dirigir sem atenção ou sem os cuidados indispensáveis à segurança é infração",["leve.","gravíssima.","média.","grave.","sem natureza."],"Art. 169.")
q(1,"Disputar corrida é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 173.")
q(1,"Avançar o sinal vermelho do semáforo é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 208.")
q(1,"Transitar pela contramão de direção em via com sinalização de sentido único de circulação é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 186, II.")
q(1,"Desobedecer às ordens emanadas da autoridade de trânsito ou de seus agentes é infração",["grave.","leve.","média.","gravíssima.","sem natureza."],"Art. 195.")
q(1,"Deixar de indicar com antecedência, por gesto ou luz indicadora de direção, a mudança de direção é infração",["grave.","leve.","média.","gravíssima.","sem natureza."],"Art. 196.")
q(1,"Transitar com o veículo em calçadas, passeios, ciclovias e ciclofaixas é infração gravíssima com multa de",["três vezes.","duas vezes.","cinco vezes.","dez vezes.","uma vez."],"Art. 193.")
q(1,"No texto da operação em avenida, o veículo medido a 75 km/h em via de 60 km/h estava acima do limite em",["25%, infração grave.","10%, infração média.","60%, infração gravíssima.","5%, infração leve.","50%, sem infração."],"75 é 25% acima de 60: mais de 20% e até 50%, grave (art. 218, II).","ctb7a")
q(1,"No texto do veículo sem placa, o condutor com a CNH vencida há 40 dias cometeu, quanto à CNH, infração",["gravíssima.","leve.","média.","grave.","nenhuma, pois vale 60 dias."],"Art. 162, V: vencida há mais de 30 dias.","ctb7c")
q(1,"No texto do sinistro na esquina, deixar o local sem prestar socorro configura, em tese, infração",["gravíssima, com multa de cinco vezes e suspensão do direito de dirigir.","leve.","média.","grave, apenas com multa.","sem natureza."],"Art. 176.","ctb7b")
# n=2
q(2,"Dirigir sob influência de álcool tem como medida administrativa o recolhimento do documento de habilitação e a",["retenção do veículo.","apreensão da CNH pela empresa.","remoção do condutor.","prisão em flagrante, sempre.","multa em dobro."],"Art. 165, medida administrativa.")
q(2,"Dirigir veículo sem realizar o exame toxicológico do art. 148-A é infração gravíssima com multa de",["cinco vezes.","três vezes.","dez vezes.","duas vezes.","uma vez."],"Art. 165-B.")
q(2,"A infração por não fazer o exame toxicológico periódico configura-se quando o condutor dirigir após o trigésimo dia do",["vencimento do prazo.","início do prazo.","exame anterior.","aniversário.","licenciamento."],"Art. 165-B, parágrafo único.")
q(2,"Dirigir tendo obtido resultado positivo no exame toxicológico é infração",["gravíssima, com multa de cinco vezes.","leve.","média.","grave, sem multa.","sem natureza."],"Art. 165-C.")
q(2,"Confiar a direção do veículo a pessoa que, mesmo habilitada, por seu estado físico ou psíquico não esteja em condições de dirigir, é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 166.")
q(2,"Dirigir ameaçando os pedestres que estejam atravessando a via pública é infração gravíssima com multa e",["suspensão do direito de dirigir.","apenas advertência.","prisão.","apenas remoção.","nenhuma outra penalidade."],"Art. 170.")
q(2,"Usar o veículo para arremessar, sobre os pedestres ou veículos, água ou detritos é infração",["média.","gravíssima.","leve.","grave.","sem natureza."],"Art. 171.")
q(2,"Atirar do veículo ou abandonar na via objetos ou substâncias é infração",["média.","gravíssima.","leve.","grave.","sem natureza."],"Art. 172.")
q(2,"Disputar corrida: a penalidade é multa de dez vezes, suspensão do direito de dirigir e",["apreensão do veículo.","advertência.","prisão.","curso de reciclagem apenas.","nada mais."],"Art. 173.")
q(2,"As penalidades pela promoção de competição ou exibição sem permissão da autoridade são aplicáveis aos promotores e aos",["condutores participantes.","espectadores.","fiscais.","fornecedores.","moradores."],"Art. 174, § 1º.")
q(2,"Utilizar veículo para demonstrar manobra perigosa, mediante arrancada brusca, derrapagem ou frenagem com deslizamento, é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 175.")
q(2,"Deixar o condutor, envolvido em sinistro com vítima, de prestar ou providenciar socorro, podendo fazê-lo, sujeita à multa de cinco vezes e",["suspensão do direito de dirigir.","apreensão do veículo.","advertência.","curso.","nada mais."],"Art. 176.")
q(2,"Deixar o condutor de prestar socorro à vítima de sinistro quando solicitado pela autoridade e seus agentes é infração",["grave.","leve.","média.","gravíssima.","sem natureza."],"Art. 177.")
q(2,"Estacionar o veículo nas esquinas e a menos de cinco metros do alinhamento da via transversal é infração",["média, com remoção do veículo.","leve.","grave.","gravíssima.","sem natureza."],"Art. 181, I.")
q(2,"Estacionar na pista de rolamento das estradas, das rodovias e das vias de trânsito rápido é infração",["gravíssima, com remoção do veículo.","leve.","média.","grave.","sem natureza."],"Art. 181, V.")
q(2,"Parar o veículo sobre a faixa de pedestres na mudança de sinal luminoso é infração",["média.","leve.","grave.","gravíssima.","sem natureza."],"Art. 183.")
q(2,"Transitar em faixa de trânsito exclusivo para transporte público coletivo de passageiros é infração gravíssima, com multa e",["apreensão do veículo.","advertência.","prisão.","curso.","nada mais."],"Art. 184, III.")
q(2,"No texto da operação em avenida, o condutor que se recusou a fazer o teste cometeu infração",["gravíssima, com multa de dez vezes e suspensão do direito de dirigir por 12 meses.","leve.","média.","grave.","nenhuma, pois o teste é facultativo."],"Art. 165-A.","ctb7a")
q(2,"No texto do veículo sem placa, a falta da placa traseira é infração",["gravíssima, com multa e apreensão do veículo.","leve.","média.","grave.","sem natureza."],"Art. 230, IV.","ctb7c")
q(2,"No texto do sinistro na esquina, a medida administrativa prevista para a infração do art. 176 é o",["recolhimento do documento de habilitação.","apreensão do veículo.","recolhimento da placa.","curso obrigatório.","pagamento imediato."],"Art. 176, medida administrativa.","ctb7b")
# n=3
q(3,"Assinale a alternativa correta quanto à infração por transitar em velocidade superior à máxima.",["Superior em mais de 50%: gravíssima, com multa de três vezes e suspensão do direito de dirigir.","Superior em até 20%: grave.","Superior em mais de 20% até 50%: gravíssima.","Superior em mais de 50%: grave.","Superior em até 20%: leve."],"Art. 218.")
q(3,"Considere. I. Dirigir sem CNH: gravíssima. II. Cinto de segurança: leve. III. Sinal vermelho: gravíssima. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Cinto: grave (art. 167).")
q(3,"Assinale a INCORRETA.",["Dirigir sem atenção é gravíssima.","Avançar o sinal vermelho é gravíssima.","Disputar corrida é gravíssima.","Calçadas e ciclovias: gravíssima.","Contramão em via de sentido único: gravíssima."],"Dirigir sem atenção é leve (art. 169).")
q(3,"A multa de dirigir sob influência de álcool é aplicada em dobro em caso de reincidência no período de até 12 meses, regra que também vale para",["a recusa ao teste.","o cinto de segurança.","a falta de atenção.","a seta.","o sinal vermelho."],"Art. 165-A, parágrafo único.")
q(3,"No art. 162, a multa é de três vezes para quem dirige sem CNH e de duas vezes para quem dirige com",["CNH de categoria diferente da do veículo.","CNH suspensa.","CNH cassada.","CNH vencida há mais de 30 dias.","CNH sem exame."],"Art. 162, III.")
q(3,"Transitar pela contramão de direção em via com duplo sentido de circulação, fora do caso de ultrapassagem, é infração",["grave.","gravíssima.","média.","leve.","sem natureza."],"Art. 186, I.")
q(3,"Forçar passagem entre veículos que, transitando em sentidos opostos, estejam na iminência de passar um pelo outro na ultrapassagem, tem como penalidade multa de dez vezes e",["suspensão do direito de dirigir.","apreensão.","advertência.","curso.","nada mais."],"Art. 191.")
q(3,"Ultrapassar pela contramão onde houver linha dupla contínua é infração gravíssima com multa de",["cinco vezes.","três vezes.","dez vezes.","duas vezes.","uma vez."],"Art. 203, V.")
q(3,"Transpor, sem autorização, bloqueio viário policial é infração gravíssima com multa, apreensão do veículo e",["suspensão do direito de dirigir.","advertência.","curso.","prisão.","nada mais."],"Art. 210.")
q(3,"Transpor, sem autorização, bloqueio viário que não seja policial é infração",["grave.","gravíssima.","média.","leve.","sem natureza."],"Art. 209.")
q(3,"Transitar em velocidade inferior à metade da máxima estabelecida para a via, retardando ou obstruindo o trânsito, é infração",["média.","leve.","grave.","gravíssima.","sem natureza."],"Art. 219.")
q(3,"Estacionar afastado do meio-fio a mais de um metro é infração",["grave, com remoção do veículo.","leve.","média.","gravíssima.","sem natureza."],"Art. 181, III.")
q(3,"Parar o veículo afastado do meio-fio a mais de um metro é infração",["média.","leve.","grave.","gravíssima.","sem natureza."],"Art. 182, III.")
q(3,"Portar placas de identificação em desacordo com as especificações do Contran é infração média com retenção do veículo para regularização e",["apreensão das placas irregulares.","advertência.","prisão.","curso.","nada mais."],"Art. 221.")
q(3,"Conduzir veículo que não esteja registrado e devidamente licenciado é infração",["gravíssima, com multa e apreensão do veículo.","leve.","média.","grave, apenas multa.","sem natureza."],"Art. 230, V.")
q(3,"Conduzir veículo com dispositivo antirradar é infração",["gravíssima, com multa e apreensão do veículo.","leve.","média.","grave.","sem natureza."],"Art. 230, III.")
q(3,"Deixar de reduzir a velocidade ao se aproximar de passeatas, aglomerações, cortejos e desfiles é infração",["gravíssima.","leve.","média.","grave.","sem natureza."],"Art. 220, I.")
q(3,"No texto da operação em avenida, o veículo a 75 km/h em via de 60 km/h cometeu infração",["grave, pois excedeu em mais de 20% e até 50%.","média, pois excedeu até 20%.","gravíssima.","leve.","sem infração."],"Art. 218, II.","ctb7a")
q(3,"No texto do veículo sem placa, a CNH vencida há 40 dias leva à medida administrativa de",["retenção do veículo até a apresentação de condutor habilitado.","prisão.","apreensão da placa apenas.","nenhuma.","curso."],"Art. 162, V.","ctb7c")
q(3,"No texto do sinistro na esquina, a infração do art. 176 sujeita o condutor a multa de cinco vezes e",["suspensão do direito de dirigir.","advertência.","curso apenas.","nada mais.","apreensão da placa."],"Art. 176.","ctb7b")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Infrações de trânsito (Cap. XV)",[
 ("hab","Habilitação",["sem CNH: gravíssima","categoria diferente","CNH vencida há mais de 30 dias"],"seção 1"),
 ("alc","Álcool",["gravíssima, 10x","suspensão de 12 meses","recusa = embriaguez"],"seção 1"),
 ("seg","Condução",["cinto: grave","criança: gravíssima","corrida: gravíssima"],"seção 2"),
 ("sin","Sinistro",["com vítima: 5x e suspensão","socorro","preservar local"],"seção 2"),
 ("cir","Circulação",["contramão","sinal vermelho","calçadas: 3x"],"seção 3"),
 ("vel","Velocidade e estacionamento",["20%: média; 50%: grave","acima: gravíssima","meio-fio: leve ou grave"],"seção 3 e 4")],
 "Na prova: natureza da infração e penalidade; confira a suspensão")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7],QR,4,svg,"A primeira linha traz a habilitação e o álcool; as demais, condução, sinistro, circulação, velocidade e estacionamento.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 161 a 230 (seleção), texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-7","Infrações (CTB, Cap. XV)",Q,list(tx),
 cobertura=["Cap. XV tem mais de 90 artigos; foram cobertos os de maior incidência: 161 a 178 (habilitação, álcool, condução, sinistro), 181 a 183 (estacionar e parar), 184 a 196, 203, 208 a 210, 218 a 221 e 230 (I a VI). Não cobertos: arts. 179, 180, 188 a 190, 194, 197 a 202, 204, 205, 207, 211 a 217, 222 a 229 e 231 a 255."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","O valor das multas e a pontuação estão no ctb-8 (arts. 256 a 279).","Conferir se o edital inclui outras infrações (equipamentos, documentos, transporte de carga e de passageiros).","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb7a, ctb7b e ctb7c fictícios."],
 fontes_conferidas=["CTB, arts. 161 a 230: texto da Câmara, copiado por programa."])
gravar("ctb-7",aula_html,banco("ctb-7",Q),tx)
