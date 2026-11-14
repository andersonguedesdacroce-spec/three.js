import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='idoso.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes do Estatuto da Pessoa Idosa (arts. 95 a 108) são o capítulo mais cobrado do Estatuto nas provas de segurança pública. A Vunesp pergunta a pena de cada crime, o aumento de pena, a natureza da ação penal (pública incondicionada) e a conduta que cada artigo descreve: discriminar, abandonar, expor a perigo, apropriar-se de bens, reter cartão, coagir. Para o guarda municipal, que atende ocorrências de idosos em situação de abandono ou maus-tratos, o conteúdo vira rotina."
S={}
S[1]="## 1. Ação penal, discriminação, omissão, abandono e perigo\n\n"+L("art. 95","Art. 95. Os crimes definidos nesta Lei","Art. 96.")+"\n\n"+L("art. 96","Art. 96. Discriminar pessoa idosa","Art. 97.")+"\n\n"+L("art. 97","Art. 97. Deixar de prestar assistência","Art. 98.")+"\n\n"+L("art. 98","Art. 98. Abandonar a pessoa idosa","Art. 99.")+"\n\n"+L("art. 99","Art. 99. Expor a perigo","Art. 100.")+"""

Os crimes do Estatuto são de ação penal pública incondicionada, e não se aplicam os arts. 181 e 182 do Código Penal (as escusas absolutórias entre familiares). Discriminar a pessoa idosa, impedindo ou dificultando o acesso a operações bancárias, transporte, contratação ou outro meio necessário ao exercício da cidadania, por motivo de idade, tem reclusão de seis meses a um ano e multa; na mesma pena incorre quem desdenhar, humilhar, menosprezar ou discriminar por qualquer motivo, e a pena aumenta de um terço se a vítima está sob os cuidados do agente. A negativa de crédito por superendividamento não é crime.

Deixar de prestar assistência, podendo fazê-lo sem risco pessoal, em situação de iminente perigo, ou recusar, retardar ou dificultar a assistência à saúde, tem detenção de seis meses a um ano e multa, com aumento de metade se resulta lesão grave e triplicação se resulta a morte. Abandonar a pessoa idosa em hospitais, casas de saúde ou entidades de longa permanência, ou não prover suas necessidades básicas quando obrigado, tem detenção de seis meses a três anos e multa. Expor a perigo a integridade e a saúde da pessoa idosa, em condições desumanas ou privando-a de alimentos e cuidados, tem reclusão de dois a cinco anos; com lesão grave, três a sete anos; com morte, oito a catorze anos.
"""
S[2]="## 2. Obstáculos, ordens judiciais, bens e retenção\n\n"+L("art. 100","Art. 100. Constitui crime","Art. 101.")+"\n\n"+L("arts. 101 e 102","Art. 101. Deixar de cumprir","Art. 103.")+"\n\n"+L("arts. 103 e 104","Art. 103. Negar o acolhimento","Art. 105.")+"""

Constitui crime, com reclusão de seis meses a um ano e multa, obstar o acesso a cargo público por motivo de idade, negar emprego ou trabalho por motivo de idade, recusar, retardar ou dificultar atendimento ou assistência à saúde, descumprir ordem judicial da ação civil do Estatuto e recusar dados técnicos requisitados pelo Ministério Público. Descumprir ordem judicial nas ações em que a pessoa idosa seja parte tem detenção de seis meses a um ano e multa.

Apropriar-se ou desviar bens, proventos, pensão ou rendimento da pessoa idosa, dando-lhes aplicação diversa da finalidade, tem reclusão de um a quatro anos e multa. Negar o acolhimento ou a permanência por recusa em outorgar procuração à entidade tem detenção de seis meses a um ano e multa. Reter o cartão magnético de conta de benefícios, proventos ou pensão, ou outro documento, para assegurar recebimento de dívida, tem detenção de seis meses a dois anos e multa.
"""
S[3]="## 3. Imagem, procuração, coação e ato notarial\n\n"+L("arts. 105 a 108","Art. 105. Exibir ou veicular","TÍTULO VII")+"""

Exibir ou veicular, por qualquer meio de comunicação, informações ou imagens depreciativas ou injuriosas à pessoa idosa tem detenção de um a três anos e multa. Induzir pessoa idosa sem discernimento a outorgar procuração para administração de bens ou disposição livre tem reclusão de dois a quatro anos. Coagir a pessoa idosa a doar, contratar, testar ou outorgar procuração tem reclusão de dois a cinco anos. Lavrar ato notarial envolvendo pessoa idosa sem discernimento, sem a devida representação legal, tem reclusão de dois a quatro anos.
"""
S[5]="""## 5. Na rotina do guarda

- **Idoso abandonado:** o guarda registra, acolhe e comunica a autoridade policial; o abandono é crime com detenção de seis meses a três anos.
- **Maus-tratos e privação de alimentos:** expor a perigo a integridade e a saúde é crime com reclusão de dois a cinco anos; ação penal pública incondicionada.
- **Furto de benefício:** apropriar-se de proventos do idoso é crime, assim como reter o cartão magnético.
- **Discriminação:** negar atendimento, emprego ou acesso por motivo de idade é crime; humilhar o idoso também.
- **Omissão:** deixar de prestar assistência em perigo iminente, podendo fazê-lo sem risco, é crime.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Ação penal | Pública incondicionada; não se aplicam os arts. 181 e 182 do CP |
| Discriminação (art. 96) | Reclusão de 6 meses a 1 ano e multa; aumento de 1/3 se a vítima está sob cuidados do agente |
| Omissão de assistência (art. 97) | Detenção de 6 meses a 1 ano e multa; metade se lesão grave, triplicada se morte |
| Abandono (art. 98) | Detenção de 6 meses a 3 anos e multa |
| Exposição a perigo (art. 99) | Reclusão de 2 a 5 anos; lesão grave 3 a 7; morte 8 a 14 |
| Apropriação (art. 102) | Reclusão de 1 a 4 anos e multa |
| Retenção de cartão (art. 104) | Detenção de 6 meses a 2 anos e multa |
| Imagens depreciativas (art. 105) | Detenção de 1 a 3 anos e multa |
| Procuração por indução (art. 106) | Reclusão de 2 a 4 anos |
| Coação (art. 107) | Reclusão de 2 a 5 anos |
| Reclusão x detenção | Observe o tipo da pena em cada artigo |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 95 | Ação penal pública incondicionada |
| Art. 96 | Discriminar: reclusão de 6 meses a 1 ano e multa |
| Art. 97 | Omissão de assistência: detenção de 6 meses a 1 ano |
| Art. 98 | Abandonar: detenção de 6 meses a 3 anos |
| Art. 99 | Expor a perigo: reclusão de 2 a 5 anos |
| Art. 100 | Obstar cargo ou emprego: reclusão de 6 meses a 1 ano |
| Art. 102 | Apropriar-se de bens: reclusão de 1 a 4 anos |
| Art. 104 | Reter cartão: detenção de 6 meses a 2 anos |
| Art. 105 | Imagens depreciativas: detenção de 1 a 3 anos |
| Art. 106 | Procuração por indução: reclusão de 2 a 4 anos |
| Art. 107 | Coagir: reclusão de 2 a 5 anos |
| Art. 108 | Ato notarial sem representação: reclusão de 2 a 4 anos |
"""
QR=[("Questão 1","Abandonar a pessoa idosa em hospitais, casas de saúde ou entidades de longa permanência, ou não prover suas necessidades básicas, quando obrigado por lei ou mandado, tem pena de",["detenção de seis meses a três anos e multa.","reclusão de dois a cinco anos.","detenção de seis meses a um ano.","reclusão de um a quatro anos.","multa apenas."],0,"Art. 98."),
("Questão 2","Os crimes definidos no Estatuto da Pessoa Idosa são de ação penal",["pública incondicionada.","privada.","pública condicionada.","subsidiária.","condicionada à representação."],1,"Art. 95."),
("Questão 3","Expor a perigo a integridade e a saúde da pessoa idosa, privando-a de alimentos e cuidados indispensáveis, quando obrigado a fazê-lo, tem pena de",["reclusão de dois a cinco anos.","detenção de seis meses a um ano.","detenção de um a três anos.","reclusão de seis meses a um ano.","multa apenas."],2,"Art. 99."),
("Questão 4","Apropriar-se de ou desviar bens, proventos, pensão ou qualquer outro rendimento da pessoa idosa, dando-lhes aplicação diversa da finalidade, tem pena de",["reclusão de um a quatro anos e multa.","detenção de seis meses a um ano.","reclusão de dois a cinco anos.","detenção de um a três anos.","multa apenas."],3,"Art. 102.")]
t1="<strong>Abandono na rodoviária</strong><br><br>Um filho deixou o pai de 82 anos, dependente dele, numa rodoviária de Vila Nova, cidade fictícia, com um bilhete e sem recursos. A guarda municipal o encontrou."
t2="<strong>Cartão retido</strong><br><br>Um comerciante de Vila Nova recebeu o cartão magnético da conta da pensão de uma idosa como garantia de dívida e o reteve por meses."
t3="<strong>Procuração induzida</strong><br><br>Uma cuidadora de Vila Nova levou uma senhora de 88 anos, sem discernimento de seus atos, ao cartório e a fez assinar procuração para administrar todos os seus bens."
tx={"idoso3a":t1,"idoso3b":t2,"idoso3c":t3}
# n=1
q(1,"Os crimes do Estatuto da Pessoa Idosa não se aplicam os arts. 181 e 182 do",["Código Penal.","Código Civil.","Código de Trânsito.","Código Tributário.","Estatuto da Criança."],"Art. 95.")
q(1,"Discriminar pessoa idosa, impedindo ou dificultando seu acesso a operações bancárias, por motivo de idade, tem pena de reclusão de seis meses a",["um ano e multa.","dois anos.","três anos.","quatro anos.","cinco anos."],"Art. 96.")
q(1,"A pena do art. 96 é aumentada de um terço se a vítima se encontrar sob os cuidados ou responsabilidade do",["agente.","juiz.","delegado.","vizinho.","empregador."],"Art. 96, § 2º.")
q(1,"Não constitui crime a negativa de crédito motivada por",["superendividamento da pessoa idosa.","idade.","raça.","cor.","religião."],"Art. 96, § 3º.")
q(1,"Deixar de prestar assistência à pessoa idosa, quando possível fazê-lo sem risco pessoal, em situação de iminente perigo, tem pena de detenção de seis meses a",["um ano e multa.","dois anos.","três anos.","quatro anos.","cinco anos."],"Art. 97.")
q(1,"Expor a perigo a integridade e a saúde da pessoa idosa tem pena de reclusão de dois a",["cinco anos.","três anos.","quatro anos.","seis anos.","dez anos."],"Art. 99.")
q(1,"Se da exposição a perigo resulta lesão corporal de natureza grave, a pena é de reclusão de três a",["sete anos.","cinco anos.","oito anos.","dez anos.","doze anos."],"Art. 99, § 1º.")
q(1,"Se da exposição a perigo resulta a morte, a pena é de reclusão de oito a",["catorze anos.","dez anos.","doze anos.","vinte anos.","trinta anos."],"Art. 99, § 2º.")
q(1,"Obstar o acesso de alguém a qualquer cargo público por motivo de idade é crime punível com reclusão de seis meses a um ano e",["multa.","prisão perpétua.","detenção.","perda de bens.","advertência."],"Art. 100, I.")
q(1,"Negar a alguém, por motivo de idade, emprego ou trabalho é crime com reclusão de seis meses a",["um ano e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 100, II.")
q(1,"Deixar de cumprir ordem judicial expedida nas ações em que for parte a pessoa idosa tem pena de",["detenção de seis meses a um ano e multa.","reclusão de dois anos.","multa apenas.","reclusão de cinco anos.","detenção de dois anos."],"Art. 101.")
q(1,"Negar o acolhimento da pessoa idosa por recusa em outorgar procuração à entidade tem pena de detenção de seis meses a",["um ano e multa.","dois anos.","três anos.","quatro anos.","cinco anos."],"Art. 103.")
q(1,"Reter o cartão magnético de conta relativa a benefícios ou pensão da pessoa idosa tem pena de detenção de seis meses a",["dois anos e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 104.")
q(1,"Exibir ou veicular informações ou imagens depreciativas ou injuriosas à pessoa idosa tem pena de detenção de um a",["três anos e multa.","dois anos.","quatro anos.","cinco anos.","seis meses."],"Art. 105.")
q(1,"Induzir pessoa idosa sem discernimento a outorgar procuração para administração de bens tem pena de reclusão de dois a",["quatro anos.","três anos.","cinco anos.","seis anos.","um ano."],"Art. 106.")
q(1,"Coagir a pessoa idosa a doar, contratar, testar ou outorgar procuração tem pena de reclusão de dois a",["cinco anos.","três anos.","quatro anos.","seis anos.","um ano."],"Art. 107.")
q(1,"Lavrar ato notarial que envolva pessoa idosa sem discernimento, sem representação legal, tem pena de reclusão de dois a",["quatro anos.","três anos.","cinco anos.","seis anos.","um ano."],"Art. 108.")
q(1,"No texto do abandono na rodoviária, o filho que deixou o pai idoso sem recursos pratica, em tese, o crime de",["abandono de pessoa idosa.","furto.","roubo.","estelionato.","receptação."],"Art. 98.","idoso3a")
q(1,"No texto do cartão retido, a conduta do comerciante corresponde ao art.",["104.","98.","102.","106.","108."],"Art. 104.","idoso3b")
q(1,"No texto da procuração induzida, a conduta da cuidadora corresponde ao art.",["106.","98.","102.","104.","108."],"Art. 106.","idoso3c")
# n=2
q(2,"Na mesma pena do art. 96 incorre quem desdenhar, humilhar, menosprezar ou discriminar pessoa idosa, por qualquer",["motivo.","valor.","local.","horário.","dia."],"Art. 96, § 1º.")
q(2,"No crime do art. 97, a pena é aumentada de metade se da omissão resulta lesão corporal de natureza",["grave.","leve.","média.","qualquer.","nenhuma."],"Art. 97, parágrafo único.")
q(2,"No crime do art. 97, a pena é triplicada se da omissão resulta a",["morte.","lesão leve.","fuga.","prisão.","doença."],"Art. 97, parágrafo único.")
q(2,"O art. 97 também pune recusar, retardar ou dificultar a assistência à saúde, sem",["justa causa.","dolo.","culpa.","pagamento.","documento."],"Art. 97.")
q(2,"No art. 98, o abandono pune quem não prover as necessidades básicas, quando obrigado por lei ou",["mandado.","vontade.","costume.","tradição.","contrato verbal."],"Art. 98.")
q(2,"No art. 99, a exposição a perigo inclui sujeitar a pessoa idosa a trabalho excessivo ou",["inadequado.","remunerado.","leve.","voluntário.","noturno apenas."],"Art. 99.")
q(2,"Constitui crime com reclusão de seis meses a um ano e multa recusar, retardar ou omitir dados técnicos indispensáveis à propositura da ação civil, quando requisitados pelo",["Ministério Público.","juiz de paz.","delegado.","prefeito.","vereador."],"Art. 100, V.")
q(2,"É crime recusar, retardar ou dificultar atendimento ou deixar de prestar assistência à saúde, sem justa causa, a pessoa",["idosa.","jovem.","estrangeira.","rica.","militar."],"Art. 100, III.")
q(2,"Apropriar-se dos bens da pessoa idosa, dando-lhes aplicação diversa da sua finalidade, tem pena de reclusão de um a quatro anos e",["multa.","prisão perpétua.","perda de cargo.","advertência.","nenhuma outra pena."],"Art. 102.")
q(2,"O art. 104 pune quem retém o cartão magnético da pessoa idosa, bem como qualquer outro documento com objetivo de assegurar recebimento ou ressarcimento de",["dívida.","herança.","doação.","imposto.","aluguel."],"Art. 104.")
q(2,"O art. 105 pune a veiculação de informações ou imagens depreciativas ou injuriosas por qualquer meio de",["comunicação.","transporte.","pagamento.","cobrança.","moradia."],"Art. 105.")
q(2,"A indução prevista no art. 106 refere-se à pessoa idosa sem",["discernimento de seus atos.","renda.","moradia.","família.","emprego."],"Art. 106.")
q(2,"O art. 107 pune a coação para doar, contratar, testar ou outorgar",["procuração.","emprego.","viagem.","abrigo.","documentos escolares."],"Art. 107.")
q(2,"O art. 108 pune lavrar ato notarial sem a devida",["representação legal.","assinatura do cartório.","testemunha.","certidão.","taxa."],"Art. 108.")
q(2,"O art. 109 pune impedir ou embaraçar ato do representante do Ministério Público ou de qualquer outro agente",["fiscalizador.","político.","comercial.","escolar.","esportivo."],"Art. 109.")
q(2,"Os crimes do Estatuto são de ação penal pública",["incondicionada.","condicionada.","privada.","subsidiária da privada.","mista."],"Art. 95.")
q(2,"No texto do abandono na rodoviária, a pena para o filho é de detenção de seis meses a",["três anos e multa.","um ano.","dois anos.","cinco anos.","dez anos."],"Art. 98.","idoso3a")
q(2,"No texto do cartão retido, a retenção do cartão de pensão tem pena de detenção de seis meses a",["dois anos e multa.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 104.","idoso3b")
q(2,"No texto da procuração induzida, a pena para a cuidadora é de reclusão de",["dois a quatro anos.","seis meses a um ano.","um a três anos.","dois a cinco anos.","oito a catorze anos."],"Art. 106.","idoso3c")
q(2,"Deixar de cumprir, retardar ou frustrar, sem justo motivo, a execução de ordem judicial nas ações em que for parte ou interveniente a pessoa idosa é o crime do art.",["101.","98.","99.","102.","104."],"Art. 101.")
# n=3
q(3,"Assinale a alternativa correta sobre as penas.",["Art. 98: detenção de seis meses a três anos; art. 99: reclusão de dois a cinco anos; art. 102: reclusão de um a quatro anos.","Art. 98: reclusão; art. 99: detenção.","Art. 99: detenção de um ano.","Art. 102: detenção de dois anos.","Art. 104: reclusão de quatro anos."],"Arts. 98, 99 e 102.")
q(3,"Considere. I. A ação penal dos crimes do Estatuto é pública incondicionada. II. A exposição a perigo com morte tem reclusão de 8 a 14 anos. III. Reter cartão de pensão é crime com reclusão de 5 anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Reter cartão tem detenção de seis meses a dois anos (art. 104).")
q(3,"Assinale a INCORRETA.",["A coação para outorgar procuração tem detenção de um mês.","Induzir idoso sem discernimento a outorgar procuração é crime.","Lavrar ato notarial sem representação é crime.","Apropriar-se de proventos é crime.","Discriminar é crime."],"A coação tem reclusão de dois a cinco anos (art. 107).")
q(3,"A pena do art. 97 é aumentada de metade, e triplicada se resulta a morte, e o aumento de metade ocorre se resulta lesão corporal de natureza",["grave.","leve.","média.","qualquer.","nenhuma."],"Art. 97, parágrafo único.")
q(3,"O crime do art. 100, IV, consiste em deixar de cumprir, retardar ou frustrar, sem justo motivo, a execução de ordem judicial expedida na ação",["civil a que alude a lei.","criminal.","trabalhista.","eleitoral.","tributária."],"Art. 100, IV.")
q(3,"Para o art. 96, a vítima sob cuidados ou responsabilidade do agente gera aumento de",["um terço.","metade.","dobro.","um quarto.","dois terços."],"Art. 96, § 2º.")
q(3,"A conduta de negar o acolhimento por recusa em outorgar procuração à entidade tem pena menor que a de",["induzir a outorgar procuração.","reter o cartão.","discriminar.","omitir assistência.","abandonar."],"Art. 103 (6 meses a 1 ano) e art. 106 (2 a 4 anos).")
q(3,"A pena de reclusão de dois a quatro anos é a do crime de",["lavrar ato notarial sem representação legal.","coagir a doar.","apropriar-se de bens.","reter cartão.","abandonar."],"Art. 108.")
q(3,"A pena de reclusão de um a quatro anos e multa é a do crime de",["apropriar-se de ou desviar bens, proventos ou rendimentos.","reter cartão.","coagir a doar.","abandonar.","discriminar."],"Art. 102.")
q(3,"A pena de detenção de um a três anos e multa é a do crime de",["exibir imagens depreciativas ou injuriosas.","apropriar-se de bens.","coagir a doar.","abandonar.","discriminar."],"Art. 105.")
q(3,"A pena de detenção de seis meses a dois anos e multa é a do crime de",["reter cartão magnético de conta de benefícios.","exibir imagens.","coagir.","induzir procuração.","discriminar."],"Art. 104.")
q(3,"Impedir ou embaraçar ato do representante do Ministério Público ou de qualquer outro agente fiscalizador tem pena de reclusão de seis meses a",["um ano e multa.","dois anos.","três anos.","quatro anos.","cinco anos."],"Art. 109.")
q(3,"Nos crimes do Estatuto, as escusas do art. 181 e 182 do Código Penal, que isentam de pena, entre familiares, em crimes patrimoniais,",["não se aplicam.","aplicam-se sempre.","aplicam-se aos ascendentes.","aplicam-se aos descendentes.","aplicam-se ao cônjuge."],"Art. 95.")
q(3,"No texto do abandono na rodoviária, a ação penal é pública incondicionada, ou seja, independe de",["representação da vítima.","denúncia do MP.","inquérito.","testemunha.","fiança."],"Art. 95.","idoso3a")
q(3,"No texto do abandono na rodoviária, o abandono do idoso dependente pelo filho, obrigado a prover, configura o crime do art.",["98.","97.","99.","102.","104."],"Art. 98.","idoso3a")
q(3,"No texto do cartão retido, a retenção como garantia de dívida da conta de pensão viola o art. 104, que veda reter o cartão ou outro documento para assegurar",["recebimento ou ressarcimento de dívida.","herança.","doação.","imposto.","aluguel."],"Art. 104.","idoso3b")
q(3,"No texto do cartão retido, a pena de detenção de seis meses a dois anos e multa é aplicável a",["quem retém o cartão.","quem divulga imagens.","quem coage.","quem abandona.","quem discrimina."],"Art. 104.","idoso3b")
q(3,"No texto da procuração induzida, além da cuidadora, o notário que lavra o ato sem a devida representação legal comete o crime do art.",["108.","106.","107.","102.","104."],"Art. 108.","idoso3c")
q(3,"No texto da procuração induzida, a senhora sem discernimento é vítima do crime de induzir a outorga de procuração para fins de",["administração de bens ou de deles dispor livremente.","venda de veículo.","abrigo.","viagem.","saúde."],"Art. 106.","idoso3c")
q(3,"A pena de reclusão de seis meses a um ano e multa, no art. 100, aplica-se, entre outras condutas, a quem nega, por motivo de idade,",["emprego ou trabalho.","moradia.","passagem de ônibus.","crédito por superendividamento.","visita."],"Art. 100, II.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Estatuto da Pessoa Idosa: crimes (arts. 95 a 108)",[
 ("aco","Ação penal",["pública incondicionada","sem arts. 181 e 182 do CP"],"seção 1"),
 ("dis","Discriminação",["reclusão 6 meses a 1 ano","+1/3 sob cuidados","superendividamento: não é crime"],"seção 1"),
 ("aba","Abandono e perigo",["abandono: detenção 6m a 3a","perigo: reclusão 2 a 5","morte: 8 a 14"],"seção 1"),
 ("ben","Bens e cartão",["apropriar: reclusão 1 a 4","reter cartão: detenção 6m a 2a","doc. e dívida"],"seção 2"),
 ("ima","Imagem",["detenção 1 a 3 anos","depreciativas ou injuriosas"],"seção 3"),
 ("pro","Procuração e coação",["indução: reclusão 2 a 4","coação: reclusão 2 a 5","ato notarial: 2 a 4"],"seção 3")],
 "Na prova: pena de cada artigo, reclusão x detenção")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a ação penal e os crimes de discriminação, abandono e perigo; as demais, bens, imagem, procuração e coação.","Fontes: Edital 02/2026, Anexo I; Lei 10.741/2003 (Estatuto da Pessoa Idosa), arts. 95 a 108, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("idoso-3","Estatuto da Pessoa Idosa: crimes em espécie (arts. 95 a 108)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (95 a 108). O art. 109 aparece em questões de apoio, fora do recorte."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Conferir se o edital cobra o art. 109 e os arts. 94 e anteriores (Juizados Especiais).","Trechos de lei copiados de fontes/idoso.txt por programa.","Casos idoso3a, idoso3b e idoso3c fictícios."],
 fontes_conferidas=["Estatuto da Pessoa Idosa, arts. 95 a 108: texto da Câmara, copiado por programa."])
gravar("idoso-3",aula_html,banco("idoso-3",Q),tx)
