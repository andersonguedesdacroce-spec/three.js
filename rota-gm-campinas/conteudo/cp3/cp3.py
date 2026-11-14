import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes de perigo punem a conduta que expõe alguém a risco, mesmo sem dano. Nos arts. 130 a 137, o Código Penal reúne o contágio de doenças, o perigo para a vida ou a saúde, o abandono de incapaz e de recém-nascido, a omissão de socorro, os maus-tratos e a rixa. A Vunesp cobra esses crimes principalmente pela pena e pelo que muda quando o resultado é lesão grave ou morte, e a omissão de socorro é o que mais toca o trabalho do guarda. A aula segue a ordem do texto consolidado."
S={}
S[1]="## 1. Contágio e perigo para a vida ou a saúde\n\n"+L("art. 130","Art. 130. Expor alguém, por meio de relações sexuais","Perigo de contágio de moléstia grave")+"\n\n"+L("art. 131","Art. 131. Praticar, com o fim de transmitir","Perigo para a vida ou saúde de outrem")+"""

O perigo de contágio venéreo (art. 130) é expor alguém, por relação sexual ou ato libidinoso, a moléstia venérea de que o agente sabe ou deve saber que está contaminado, com detenção de três meses a um ano ou multa. Se a intenção é transmitir a doença, a pena sobe para reclusão de um a quatro anos e multa. Esse crime só se procede mediante representação. O art. 131 pune quem pratica, com o fim de transmitir moléstia grave, ato capaz de produzir o contágio, com reclusão de um a quatro anos e multa. Nos dois casos o crime existe pela exposição ao perigo, e a doença não precisa ser transmitida.

"""+L("art. 132","Art. 132. Expor a vida ou a saúde de outrem","Abandono de incapaz")+"""

O art. 132 é um crime subsidiário: a pena de detenção de três meses a um ano só se aplica se o fato não constitui crime mais grave. O perigo tem de ser direto e iminente, e a pena é aumentada de um sexto a um terço quando decorre do transporte de pessoas para prestação de serviços em estabelecimentos de qualquer natureza, em desacordo com as normas legais.
"""
S[2]="## 2. Abandono de incapaz e de recém-nascido\n\n"+L("art. 133","Art. 133. Abandonar pessoa que está sob seu cuidado","Exposição ou abandono de recém-nascido")+"\n\n"+L("art. 134","Art. 134. Expor ou abandonar recém-nascido","Omissão de socorro")+"""

O abandono de incapaz (art. 133) exige que a vítima esteja sob o cuidado, a guarda, a vigilância ou a autoridade do agente e não possa se defender dos riscos do abandono. A pena é de reclusão de dois a cinco anos. Se resulta lesão corporal grave, de três a sete anos, e, se resulta morte, de oito a quatorze. As penas aumentam de um terço se o abandono ocorre em lugar ermo, se o agente é ascendente, descendente, cônjuge, irmão, tutor ou curador da vítima, ou se a vítima é maior de 60 anos.

O art. 134 pune expor ou abandonar recém-nascido para ocultar desonra própria. É crime com pena de detenção de seis meses a dois anos, e a finalidade de ocultar a desonra própria é elemento do tipo. Com lesão grave a pena é de um a três anos, e com morte, de dois a seis anos.
"""
S[3]="## 3. Omissão de socorro e atendimento de emergência\n\n"+L("art. 135","Art. 135. Deixar de prestar assistência","Condicionamento de atendimento")+"\n\n"+L("art. 135-A","Art. 135-A. Exigir cheque-caução","Maus tratos")+"""

A omissão de socorro é o crime de quem deixa de prestar assistência, quando possível sem risco pessoal, a criança abandonada ou extraviada, ou a pessoa inválida ou ferida, ao desamparo ou em grave e iminente perigo, ou não pede, nesses casos, o socorro da autoridade pública. A pena é de detenção de um a seis meses, ou multa, aumentada de metade se resulta lesão grave e triplicada se resulta morte. Duas pegadinhas: a lei só obriga quando o socorro é possível sem risco pessoal e, quando não se pode socorrer, é preciso pedir o socorro da autoridade. Para o guarda, que tem o dever de agir, a omissão tem consequências ainda mais sérias.

O art. 135-A pune o condicionamento de atendimento médico-hospitalar emergencial: exigir cheque-caução, nota promissória, qualquer garantia ou o preenchimento prévio de formulários como condição para o atendimento de emergência. A pena é de detenção de três meses a um ano e multa, aumentada até o dobro se resulta lesão grave, e até o triplo se resulta morte.
"""
S[4]="## 4. Maus-tratos e rixa\n\n"+L("art. 136","Art. 136. Expor a perigo a vida ou a saúde","CAPÍTULO IV")+"\n\n"+L("art. 137","Art. 137. Participar de rixa","CAPÍTULO V")+"""

Nos maus-tratos, a vítima está sob autoridade, guarda ou vigilância do agente, para fim de educação, ensino, tratamento ou custódia, e o agente a expõe a perigo privando-a de alimentação ou cuidados indispensáveis, sujeitando-a a trabalho excessivo ou inadequado, ou abusando de meios de correção ou disciplina. A pena é de reclusão de dois a cinco anos, de três a sete anos se resulta lesão grave e de oito a quatorze se resulta morte, e é aumentada de um terço se a vítima é menor de catorze anos.

A rixa é a briga entre várias pessoas, em que todos agridem todos. A pena é de detenção de quinze dias a dois meses, ou multa, e quem participa para separar os contendores não comete o crime. Se ocorre morte ou lesão grave, aplica-se a quem participou da rixa a pena de detenção de seis meses a dois anos, ainda que não se saiba quem causou o resultado.
"""
S[6]="""## 6. Na rotina do guarda

- **Omissão de socorro:** o guarda que encontra pessoa ferida ou em perigo deve prestar assistência, se possível sem risco, ou pedir socorro da autoridade pública, e registrar o atendimento.
- **Rixa na rua:** quem intervém para separar os contendores não comete rixa; o guarda separa e conduz.
- **Maus-tratos:** o servidor que acolhe criança, idoso ou preso e o expõe a perigo responde por maus-tratos.
- **Atendimento de emergência:** negar atendimento por falta de garantia é crime, e a Guarda pode ser chamada para registrar a ocorrência.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena da omissão de socorro | Detenção de um a seis meses, ou multa |
| Aumento da omissão de socorro | Metade com lesão grave; triplicada com morte |
| Art. 132 é residual | Só vale se o fato não constitui crime mais grave |
| Pena do abandono de incapaz | Reclusão de dois a cinco anos |
| Pena dos maus-tratos | Reclusão de dois a cinco anos |
| Rixa: quem separa | Quem participa para separar não pratica o crime |
| Contágio venéreo: ação penal | Somente mediante representação (§ 2º do art. 130) |
| Condicionamento de atendimento | Aumento até o dobro (lesão grave) e até o triplo (morte) |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Contágio venéreo | Detenção, 3 meses a 1 ano, ou multa; representação |
| Contágio de moléstia grave | Reclusão, 1 a 4 anos, e multa |
| Perigo para a vida ou saúde | Detenção, 3 meses a 1 ano; subsidiário |
| Abandono de incapaz | Reclusão, 2 a 5 anos; grave 3 a 7; morte 8 a 14 |
| Abandono de recém-nascido | Detenção, 6 meses a 2 anos; ocultar desonra própria |
| Omissão de socorro | Detenção, 1 a 6 meses, ou multa |
| Condicionamento de atendimento | Detenção, 3 meses a 1 ano, e multa |
| Maus-tratos | Reclusão, 2 a 5 anos; aumento de 1/3 contra menor de 14 |
| Rixa | Detenção, 15 dias a 2 meses, ou multa |
"""
QR=[("Questão 1","A pena do crime de omissão de socorro é de",["detenção, de um a seis meses, ou multa.","detenção, de seis meses a dois anos.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","reclusão, de dois a cinco anos."],0,"Art. 135, caput."),
("Questão 2","Na omissão de socorro, a pena é aumentada de metade se resulta lesão corporal grave, e",["triplicada, se resulta a morte.","dobrada, se resulta a morte.","aumentada de um terço, se resulta a morte.","mantida, se resulta a morte.","reduzida, se resulta a morte."],2,"Art. 135, parágrafo único."),
("Questão 3","Participar de rixa é crime, salvo",["para separar os contendores.","em legítima defesa de terceiro, em qualquer caso.","se houver mais de cinco participantes.","se houver arma.","se ocorrer em via pública."],4,"Art. 137, caput."),
("Questão 4","Os maus-tratos têm pena de reclusão de",["dois a cinco anos.","um a quatro anos.","seis meses a dois anos.","três a sete anos.","oito a quatorze anos."],1,"Art. 136, caput.")]
t1="<strong>Idoso caído na calçada</strong><br><br>Pedestres passaram por um idoso caído na calçada, ferido e sem conseguir se levantar, e nenhum deles parou. Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, que passava pelo local, prestou os primeiros cuidados, acionou o serviço de emergência e permaneceu com a vítima. Uma câmera registrou a passagem dos pedestres."
t2="<strong>Briga generalizada após o jogo</strong><br><br>Após uma partida de futebol, uma briga envolveu cerca de vinte torcedores, que trocavam socos e chutes sem que se soubesse quem agredia quem. Uma pessoa saiu com lesão grave. Entre os presentes, um guarda municipal e um torcedor tentaram separar os contendores."
tx={"cp3a":t1,"cp3b":t2}
# n=1
q(1,"A pena do crime de omissão de socorro é de",["detenção, de um a seis meses, ou multa.","detenção, de seis meses a dois anos.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","reclusão, de dois a cinco anos."],"Art. 135, caput.")
q(1,"A omissão de socorro tem a pena aumentada de metade se da omissão resulta",["lesão corporal de natureza grave.","lesão leve.","qualquer dano patrimonial.","perda de bens.","nenhum resultado."],"Art. 135, parágrafo único.")
q(1,"A omissão de socorro tem a pena triplicada se da omissão resulta",["a morte.","lesão leve.","lesão grave.","dano moral.","perda de emprego."],"Art. 135, parágrafo único.")
q(1,"Participar de rixa, salvo para separar os contendores, tem pena de",["detenção, de quinze dias a dois meses, ou multa.","detenção, de três meses a um ano.","reclusão, de um a quatro anos.","detenção, de um a seis meses.","reclusão, de seis meses a dois anos."],"Art. 137, caput.")
q(1,"Na rixa, se ocorre morte ou lesão corporal de natureza grave, a pena, pelo fato da participação na rixa, é de",["detenção, de seis meses a dois anos.","detenção, de quinze dias a dois meses.","reclusão, de um a quatro anos.","reclusão, de seis a vinte anos.","detenção, de um a três anos."],"Art. 137, parágrafo único.")
q(1,"Os maus-tratos, no art. 136, têm pena de",["reclusão, de dois a cinco anos.","detenção, de dois meses a um ano.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","reclusão, de três a sete anos."],"Art. 136, caput.")
q(1,"Nos maus-tratos, se resulta morte, a pena é de",["reclusão, de oito a quatorze anos.","reclusão, de três a sete anos.","reclusão, de seis a vinte anos.","reclusão, de dois a cinco anos.","reclusão, de doze a trinta anos."],"Art. 136, § 2º.")
q(1,"A pena dos maus-tratos é aumentada de um terço se o crime é praticado contra pessoa",["menor de catorze anos.","maior de sessenta anos.","com deficiência.","do sexo feminino.","menor de dezoito anos."],"Art. 136, § 3º.")
q(1,"O abandono de incapaz tem pena de",["reclusão, de dois a cinco anos.","detenção, de seis meses a dois anos.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","reclusão, de três a sete anos."],"Art. 133, caput.")
q(1,"No abandono de incapaz, se resulta morte, a pena é de",["reclusão, de oito a quatorze anos.","reclusão, de três a sete anos.","reclusão, de seis a vinte anos.","reclusão, de dois a cinco anos.","reclusão, de doze a trinta anos."],"Art. 133, § 2º.")
q(1,"As penas do abandono de incapaz são aumentadas de um terço se o abandono ocorre em",["lugar ermo.","local público.","dia útil.","horário comercial.","qualquer local."],"Art. 133, § 3º, I.")
q(1,"No abandono de recém-nascido (art. 134), a finalidade do agente é",["ocultar desonra própria.","obter vantagem econômica.","vingar-se.","livrar-se de despesas.","proteger a criança."],"Art. 134.")
q(1,"A pena do crime do art. 134 (exposição ou abandono de recém-nascido) é de",["detenção, de seis meses a dois anos.","reclusão, de dois a cinco anos.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","detenção, de três meses a um ano."],"Art. 134, caput.")
q(1,"O perigo de contágio venéreo, previsto no art. 130, tem pena de",["detenção, de três meses a um ano, ou multa.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","reclusão, de dois a cinco anos.","multa, apenas."],"Art. 130, caput.")
q(1,"Praticar, com o fim de transmitir moléstia grave de que está contaminado, ato capaz de produzir o contágio é crime com pena de",["reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","reclusão, de dois a cinco anos.","detenção, de seis meses a dois anos.","multa, apenas."],"Art. 131.")
q(1,"A pena do crime de perigo para a vida ou saúde de outrem (art. 132) é de",["detenção, de três meses a um ano, se o fato não constitui crime mais grave.","reclusão, de dois a cinco anos.","detenção, de um a seis meses.","reclusão, de um a quatro anos.","multa, apenas."],"Art. 132, caput.")
q(1,"Exigir cheque-caução como condição para atendimento médico-hospitalar emergencial tem pena de",["detenção, de três meses a um ano, e multa.","reclusão, de dois a cinco anos.","detenção, de um a seis meses.","multa, apenas.","reclusão, de um a quatro anos."],"Art. 135-A.")
q(1,"No texto do idoso caído, a omissão dos pedestres, em tese, configura",["omissão de socorro.","maus-tratos.","rixa.","abandono de incapaz.","perigo de contágio."],"Art. 135.","cp3a")
q(1,"No texto da briga após o jogo, quem participa da briga para separar os contendores",["não pratica o crime de rixa.","pratica rixa, em qualquer caso.","pratica lesão grave.","pratica maus-tratos.","pratica omissão de socorro."],"Art. 137, caput.","cp3b")
q(1,"No abandono de incapaz, se resulta lesão corporal de natureza grave, a pena é de",["reclusão, de três a sete anos.","reclusão, de dois a cinco anos.","reclusão, de oito a quatorze anos.","detenção, de um a três anos.","reclusão, de seis a vinte anos."],"Art. 133, § 1º.")
# n=2
q(2,"A omissão de socorro só é crime se a assistência é possível",["sem risco pessoal.","sem custo.","durante o dia.","por profissional da saúde.","com o auxílio de terceiros."],"Art. 135.")
q(2,"A omissão de socorro também se configura se o agente",["não pede, nesses casos, o socorro da autoridade pública.","chama a polícia.","presta assistência.","pede socorro ao vizinho.","aciona o resgate."],"Art. 135.")
q(2,"O art. 132 (perigo para a vida ou saúde de outrem) só se aplica",["se o fato não constitui crime mais grave.","se houver lesão.","se houver dano.","se a vítima for criança.","se houver dolo de matar."],"Art. 132, caput.")
q(2,"O art. 132 aumenta a pena de um sexto a um terço quando a exposição ao perigo decorre do",["transporte de pessoas para a prestação de serviços em estabelecimentos, em desacordo com as normas legais.","transporte de cargas.","uso de arma.","trânsito intenso.","abandono de animais."],"Art. 132, parágrafo único.")
q(2,"No art. 130, o crime só se procede",["mediante representação.","de ofício.","por queixa.","por requisição do Ministro da Justiça.","por denúncia anônima."],"Art. 130, § 2º.")
q(2,"Se o agente tem a intenção de transmitir a moléstia venérea, a pena do art. 130, § 1º, é de",["reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","detenção, de seis meses a dois anos.","reclusão, de dois a cinco anos.","multa."],"Art. 130, § 1º.")
q(2,"No abandono de incapaz, a pena é aumentada de um terço se o agente é",["ascendente ou descendente, cônjuge, irmão, tutor ou curador da vítima.","vizinho.","funcionário público.","maior de 60 anos.","estrangeiro."],"Art. 133, § 3º, II.")
q(2,"No abandono de incapaz, a pena é aumentada de um terço se a vítima é",["maior de 60 anos.","maior de 18 anos.","menor de 14 anos.","mulher.","estrangeira."],"Art. 133, § 3º, III.")
q(2,"No abandono de recém-nascido, se resulta lesão corporal de natureza grave, a pena é de",["detenção, de um a três anos.","reclusão, de três a sete anos.","detenção, de dois a seis anos.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos."],"Art. 134, § 1º.")
q(2,"No abandono de recém-nascido, se resulta a morte, a pena é de",["detenção, de dois a seis anos.","reclusão, de oito a quatorze anos.","detenção, de um a três anos.","reclusão, de seis a vinte anos.","detenção, de seis meses a dois anos."],"Art. 134, § 2º.")
q(2,"No condicionamento de atendimento médico-hospitalar emergencial, a pena é aumentada até o dobro se da negativa resulta",["lesão corporal de natureza grave.","lesão leve.","dano patrimonial.","prejuízo financeiro.","atraso."],"Art. 135-A, parágrafo único.")
q(2,"No condicionamento de atendimento médico-hospitalar emergencial, a pena é aumentada até o triplo se resulta",["a morte.","lesão grave.","lesão leve.","prejuízo financeiro.","dano moral."],"Art. 135-A, parágrafo único.")
q(2,"Nos maus-tratos, é elemento do tipo a vítima estar sob autoridade, guarda ou vigilância do agente, para fim de",["educação, ensino, tratamento ou custódia.","lazer.","trabalho voluntário.","hospedagem.","recreação."],"Art. 136, caput.")
q(2,"Nos maus-tratos, a pena é de reclusão de três a sete anos se do fato resulta",["lesão corporal de natureza grave.","lesão leve.","qualquer ofensa.","perigo de vida.","dano moral."],"Art. 136, § 1º.")
q(2,"São formas de maus-tratos descritas no art. 136 privar a vítima de alimentação ou cuidados indispensáveis, sujeitá-la a trabalho excessivo ou inadequado e",["abusar de meios de correção ou disciplina.","agredi-la por vingança.","abandoná-la em lugar ermo.","expô-la ao contágio.","negar-lhe atendimento médico emergencial."],"Art. 136, caput.")
q(2,"A rixa é crime que exige, no mínimo,",["participação de várias pessoas, em briga confusa, na qual todos agridem todos.","uma pessoa agredida por outra.","duas pessoas.","participação de menores.","uso de arma."],"Conceito doutrinário da rixa; art. 137.")
q(2,"No texto do idoso caído, a atitude da equipe da Guarda, de prestar os primeiros cuidados e acionar a emergência,",["cumpre o dever de assistência do art. 135.","configura maus-tratos.","configura rixa.","configura abandono.","configura perigo de contágio."],"Art. 135: prestar assistência e pedir socorro.","cp3a")
q(2,"No texto da briga após o jogo, a lesão grave sofrida por uma das pessoas faz incidir sobre os participantes da rixa a pena de",["detenção, de seis meses a dois anos.","reclusão, de um a cinco anos.","reclusão, de seis a vinte anos.","detenção, de quinze dias a dois meses.","reclusão, de dois a oito anos."],"Art. 137, parágrafo único.","cp3b")
q(2,"No texto da briga após o jogo, o guarda e o torcedor que tentaram separar os contendores",["não respondem por rixa.","respondem por rixa.","respondem por lesão grave.","respondem por omissão.","respondem por perigo da vida."],"Art. 137: salvo para separar os contendores.","cp3b")
q(2,"O crime em que a lei menciona expressamente a criança abandonada ou extraviada como possível vítima é o de",["omissão de socorro.","maus-tratos.","rixa.","perigo de contágio.","condicionamento de atendimento emergencial."],"Art. 135, caput.")
# n=3
q(3,"Assinale a alternativa que contém duas penas corretas.",["Omissão de socorro: detenção de um a seis meses ou multa; rixa: detenção de quinze dias a dois meses ou multa.","Omissão de socorro: reclusão de um a quatro anos; rixa: detenção de seis meses a dois anos.","Maus-tratos: detenção de um a seis meses; abandono de incapaz: reclusão de dois a quatro anos.","Rixa: reclusão de um a três anos; omissão de socorro: multa.","Abandono de recém-nascido: reclusão de dois a cinco anos; maus-tratos: detenção de dois meses a um ano."],"Arts. 135 e 137.")
q(3,"Considere as afirmações. I. A omissão de socorro tem pena de detenção de um a seis meses ou multa. II. Se da omissão resulta lesão grave, a pena é aumentada de metade. III. Se resulta morte, a pena é duplicada. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"Com morte, a pena é triplicada (art. 135, parágrafo único).")
q(3,"Assinale a INCORRETA.",["O abandono de incapaz tem pena de detenção de um a três meses.","A rixa não é punida se a pessoa participa para separar os contendores.","O perigo para a vida ou saúde de outrem é crime subsidiário.","No abandono de incapaz, a lesão grave eleva a pena a reclusão de três a sete anos.","A omissão de socorro é aumentada de metade se resulta lesão grave."],"O abandono de incapaz tem reclusão de dois a cinco anos (art. 133).")
q(3,"No abandono de incapaz, o resultado lesão corporal de natureza grave eleva a pena a",["reclusão, de três a sete anos.","reclusão, de dois a cinco anos.","reclusão, de oito a quatorze anos.","detenção, de um a três anos.","reclusão, de seis a vinte anos."],"Art. 133, § 1º.")
q(3,"Assinale a alternativa que descreve corretamente o art. 134.",["Expor ou abandonar recém-nascido para ocultar desonra própria.","Expor ou abandonar qualquer criança para obter vantagem.","Abandonar idoso em lugar ermo.","Deixar de prestar socorro a ferido.","Maltratar recém-nascido por educação."],"Art. 134, caput.")
q(3,"O crime de perigo para a vida ou saúde de outrem (art. 132) exige perigo",["direto e iminente.","remoto.","potencial.","abstrato.","indireto."],"Art. 132, caput.")
q(3,"O condicionamento de atendimento médico-hospitalar emergencial (art. 135-A) é praticado por quem exige, como condição para o atendimento,",["cheque-caução, nota promissória ou qualquer garantia, ou o preenchimento prévio de formulários administrativos.","apenas documento de identidade.","apenas comprovante de residência.","apenas plano de saúde.","apenas carteirinha do SUS."],"Art. 135-A, caput.")
q(3,"A rixa difere da lesão corporal porque, na rixa,",["vários participantes agridem uns aos outros, e todos respondem pelo fato da participação.","apenas uma pessoa agride outra.","a vítima é sempre identificada.","há sempre morte.","há sempre uso de arma."],"Art. 137.")
q(3,"No art. 133, o que torna o agente garante da vítima é estar ela sob seu",["cuidado, guarda, vigilância ou autoridade.","poder econômico.","grupo político.","grupo religioso.","convívio social."],"Art. 133, caput.")
q(3,"Nos maus-tratos, a diferença em relação ao abandono de incapaz está em que, naqueles,",["o agente expõe a perigo a vida ou a saúde de quem está sob sua autoridade, guarda ou vigilância, para educação, ensino, tratamento ou custódia.","o agente abandona a vítima.","o agente não conhece a vítima.","o agente age por piedade.","a vítima é sempre idosa."],"Art. 136, caput.")
q(3,"A omissão de socorro a pessoa ferida, ao desamparo, é crime. Para o agente de segurança que dispõe de meios de socorrer, isso significa que",["deve prestar assistência quando possível sem risco pessoal, ou pedir socorro da autoridade pública.","pode permanecer inerte.","só responde se houver lesão.","só responde se for médico.","só responde se estiver de serviço."],"Art. 135, caput.")
q(3,"Se da omissão de socorro resulta lesão corporal grave, a pena é",["aumentada de metade.","triplicada.","dobrada.","reduzida.","aumentada de um terço."],"Art. 135, parágrafo único.")
q(3,"No art. 136, § 3º, a pena é aumentada de um terço se o crime é praticado contra pessoa",["menor de catorze anos.","maior de sessenta anos.","com deficiência.","do sexo feminino.","menor de dezoito anos."],"Art. 136, § 3º.")
q(3,"Considere as afirmações sobre o art. 130. I. O crime pune a exposição ao contágio venéreo. II. Exige que a doença seja transmitida. III. Procede-se mediante representação. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II e III, apenas.","I e II, apenas.","I, II e III."],"É crime de perigo: não exige a transmissão (art. 130).")
q(3,"A pena do art. 131 (perigo de contágio de moléstia grave) é de",["reclusão, de um a quatro anos, e multa.","reclusão, de um a quatro anos, ou multa.","detenção, de um a quatro anos, e multa.","reclusão, de dois a cinco anos.","detenção, de três meses a um ano."],"Art. 131.")
q(3,"No abandono de recém-nascido, se resulta lesão grave, a pena é de detenção de",["um a três anos.","seis meses a dois anos.","dois a seis anos.","três a sete anos.","oito a quatorze anos."],"Art. 134, § 1º.")
q(3,"Assinale a alternativa que traz apenas crimes cuja pena prevista é de detenção.",["Omissão de socorro, rixa e perigo para a vida ou saúde de outrem.","Abandono de incapaz, maus-tratos e rixa.","Maus-tratos, rixa e abandono de incapaz.","Abandono de incapaz, omissão de socorro e rixa.","Maus-tratos, contágio de moléstia grave e omissão de socorro."],"Arts. 135, 137 e 132 (detenção). Os arts. 133, 136 e 131 preveem reclusão.")
q(3,"Assinale a alternativa correta sobre a rixa.",["A pena básica é de detenção de quinze dias a dois meses, ou multa, e quem participa apenas para separar não pratica o crime.","A pena básica é de reclusão de um a quatro anos.","Todos os participantes respondem por homicídio se houver morte.","Quem separa os contendores responde por rixa.","Exige sempre o uso de arma."],"Art. 137, caput e parágrafo único.")
q(3,"No texto do idoso caído, a omissão dos pedestres seria punida com",["detenção, de um a seis meses, ou multa.","reclusão, de dois a cinco anos.","detenção, de seis meses a dois anos.","reclusão, de um a quatro anos.","multa, apenas."],"Art. 135, caput.","cp3a")
q(3,"No texto da briga após o jogo, não se sabendo quem causou a lesão grave, a pena aplicada aos que participaram da rixa é de",["detenção, de seis meses a dois anos.","detenção, de quinze dias a dois meses.","reclusão, de um a cinco anos.","reclusão, de dois a oito anos.","multa."],"Art. 137, parágrafo único: aplica-se pelo fato da participação.","cp3b")
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes de perigo e rixa",[
 ("cont","Contágio",["130: detenção, 3 meses a 1 ano","131: reclusão, 1 a 4 anos","só crime de perigo"],"seção 1"),
 ("perigo","Perigo para a vida",["art. 132","subsidiário","direto e iminente"],"seção 1"),
 ("aband","Abandono",["incapaz: 2 a 5 anos","recém-nascido: 6 meses a 2 anos","aumentos de 1/3"],"seção 2"),
 ("omis","Omissão de socorro",["1 a 6 meses, ou multa","metade com lesão grave","triplicada com morte"],"seção 3"),
 ("maus","Maus-tratos",["reclusão, 2 a 5 anos","grave 3 a 7; morte 8 a 14","1/3 contra menor de 14"],"seção 4"),
 ("rixa","Rixa",["15 dias a 2 meses, ou multa","quem separa não responde","morte ou lesão grave: 6 meses a 2 anos"],"seção 4")],
 "Na prova: omissão de socorro é detenção; maus-tratos e abandono de incapaz são reclusão")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As cinco primeiras caixas são crimes de perigo; a última é a briga em que todos se agridem.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 130 a 137, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-3","Periclitação da vida e da saúde e rixa (CP, arts. 130 a 137)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 130 a 137. Cobertos: arts. 130, 131, 132, 133, 134, 135, 135-A, 136 e 137."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","Trechos de lei copiados do arquivo fontes/cp.txt por programa.","Casos cp3a e cp3b fictícios."],
 fontes_conferidas=["CP, arts. 130 a 137: texto da Câmara, copiado por programa."])
gravar("cp-3",aula_html,banco("cp-3",Q),tx)
