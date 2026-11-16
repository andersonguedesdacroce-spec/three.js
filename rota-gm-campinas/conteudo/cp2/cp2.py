import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A lesão corporal é o crime que mais aparece no dia a dia da Guarda Municipal, de brigas de rua à violência doméstica. A Vunesp cobra o art. 129 sempre pela gradação: lesão leve, grave, gravíssima e seguida de morte, cada uma com a sua pena, além da lesão culposa, das causas de diminuição e de aumento e da violência doméstica. O artigo foi muito alterado nos últimos anos, e o texto consolidado é a referência. A aula segue a ordem dos parágrafos, com a lei citada e a explicação logo abaixo."
S={}
S[1]="## 1. Lesão leve, grave e gravíssima\n\n"+L("art. 129, caput","Art. 129. Ofender a integridade corporal","Lesão corporal de natureza grave")+"""

Ofender a integridade corporal ou a saúde de outra pessoa é lesão corporal, e a pena básica, de detenção de três meses a um ano, é a da lesão leve. Repare que o tipo protege a integridade corporal e a saúde, e que a lesão em si mesmo, a autolesão, não é crime. A gravidade da lesão vem do resultado, e os parágrafos seguintes definem os resultados que aumentam a pena.

"""+L("§ 1º","§ 1º Se resulta:","§ 2º Se resulta:")+"\n\n"+L("§ 2º","§ 2º Se resulta:","Lesão corporal seguida de morte")+"""

A lesão corporal de natureza grave (§ 1º) tem pena de reclusão de um a cinco anos e ocorre quando resulta incapacidade para as ocupações habituais por mais de trinta dias, perigo de vida, debilidade permanente de membro, sentido ou função, ou aceleração de parto. A lesão gravíssima (§ 2º) tem pena de reclusão de dois a oito anos e ocorre quando resulta incapacidade permanente para o trabalho, enfermidade incurável, perda ou inutilização de membro, sentido ou função, deformidade permanente ou aborto. O truque da prova é a palavra “permanente”: debilidade permanente é grave; perda ou inutilização, incapacidade permanente e deformidade permanente são gravíssimas.
"""
S[2]="## 2. Lesão seguida de morte, diminuição de pena e lesão culposa\n\n"+L("§ 3º","§ 3º Se resulta morte e as circunstâncias","§ 3º-A.")+"\n\n"+L("§ 3º-A","§ 3º-A. No crime previsto","Diminuição de pena")+"\n\n"+L("§§ 4º e 5º","§ 4º Se o agente comete o crime impelido","Lesão corporal culposa")+"\n\n"+L("§§ 6º a 8º","§ 6º Se a lesão é culposa:","§ 8º-A.")+"""

A lesão seguida de morte é o crime preterdoloso: o agente quis lesionar, não matar, nem assumiu o risco da morte, e a pena é de reclusão de quatro a doze anos. Quando o fato ocorre no contexto da atuação de organização criminosa ultraviolenta, a pena sobe para vinte a quarenta anos (§ 3º-A). O § 4º repete a diminuição do homicídio privilegiado, de um sexto a um terço. O § 5º autoriza o juiz a substituir a detenção pela multa, se as lesões não são graves, quando ocorre o § 4º ou quando as lesões são recíprocas. A lesão culposa (§ 6º) tem pena de detenção de dois meses a um ano, e o § 7º manda aumentar a pena de um terço nas hipóteses do art. 121, §§ 4º e 6º, e o § 8º estende à lesão culposa o perdão judicial do art. 121, § 5º.
"""
S[3]="## 3. Violência doméstica e causas de aumento\n\n"+L("§§ 8º-A e 9º a 11","§ 8º-A. Com exceção do disposto","§ 12.")+"\n\n"+L("§ 12","§ 12. Aumenta-se a pena de:","§ 13.")+"\n\n"+L("§ 13","§ 13. Se a lesão é praticada contra a mulher","CAPÍTULO III")+"""

O § 9º é a lesão corporal no contexto doméstico: a vítima é ascendente, descendente, irmão, cônjuge ou companheiro, pessoa com relação de trabalho doméstico ou com quem o agente conviva ou tenha convivido, ou o agente se prevalece das relações domésticas, de coabitação ou de hospitalidade. A pena é de reclusão de dois a cinco anos. Os §§ 10 e 11 aumentam de um terço, respectivamente, quando o resultado é de lesão grave, gravíssima ou seguida de morte nessas circunstâncias, e quando a vítima é pessoa com deficiência.

O § 12 aumenta a pena em lesão dolosa contra agentes de segurança pública, integrantes do sistema prisional e da Força Nacional, membros do Judiciário, do Ministério Público, da Defensoria e da Advocacia Pública e oficiais de justiça, no exercício da função ou em decorrência dela, e nas dependências de instituição de ensino. Entre os agentes do art. 144 da Constituição estão as guardas municipais. O § 13 trata da lesão contra a mulher por razões da condição do sexo feminino, com reclusão de dois a cinco anos.
"""
S[5]="""## 5. Na rotina do guarda

- **Briga de rua:** em lesão leve, a infração costuma ser de menor potencial ofensivo; o guarda conduz as partes e o fato é registrado em termo circunstanciado ou auto, conforme a autoridade.
- **Violência doméstica:** a agressão contra companheiro, cônjuge ou familiar tem pena de reclusão e é crime grave, e o atendimento da Guarda deve registrar a situação com cuidado.
- **Agressão contra o guarda:** a lesão dolosa contra agente do art. 144 da Constituição, no exercício da função, tem aumento de pena (§ 12, I, a).
- **Socorro e perícia:** o exame de corpo de delito fixa a gravidade da lesão; preservar o local e a vítima é parte do trabalho.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena da lesão leve | Detenção de três meses a um ano |
| Pena da lesão grave | Reclusão de um a cinco anos |
| Pena da gravíssima | Reclusão de dois a oito anos |
| Debilidade permanente: grave ou gravíssima? | Grave (§ 1º, III); a perda ou inutilização é gravíssima |
| Aborto como resultado da lesão | Gravíssima (§ 2º, V); a aceleração de parto é grave |
| Lesão seguida de morte | Preterdolosa: reclusão de quatro a doze anos |
| Pena da lesão culposa | Detenção de dois meses a um ano |
| Violência doméstica | Reclusão de dois a cinco anos (§ 9º) |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Leve | Detenção, 3 meses a 1 ano |
| Grave | Reclusão, 1 a 5 anos (incapacidade por mais de 30 dias, perigo de vida, debilidade permanente, aceleração de parto) |
| Gravíssima | Reclusão, 2 a 8 anos (incapacidade permanente, enfermidade incurável, perda ou inutilização, deformidade, aborto) |
| Seguida de morte | Reclusão, 4 a 12 anos; preterdolosa |
| Culposa | Detenção, 2 meses a 1 ano |
| Diminuição | 1/6 a 1/3: valor social ou moral, violenta emoção |
| Doméstica | Reclusão, 2 a 5 anos (§ 9º) |
| Contra a mulher por razões do sexo feminino | Reclusão, 2 a 5 anos (§ 13) |
"""
QR=[("Questão 1","A pena da lesão corporal de natureza leve é de",["detenção, de três meses a um ano.","reclusão, de um a cinco anos.","detenção, de um a três anos.","reclusão, de dois a oito anos.","detenção, de seis meses a dois anos."],0,"Art. 129, caput."),
("Questão 2","Se da lesão resulta debilidade permanente de membro, sentido ou função, a lesão é",["grave, com reclusão de um a cinco anos.","gravíssima, com reclusão de dois a oito anos.","leve.","seguida de morte.","culposa."],2,"Art. 129, § 1º, III."),
("Questão 3","Se da lesão resulta deformidade permanente, a lesão é",["gravíssima, com reclusão de dois a oito anos.","grave, com reclusão de um a cinco anos.","leve.","culposa.","seguida de morte."],4,"Art. 129, § 2º, IV."),
("Questão 4","Se da lesão resulta morte, e as circunstâncias evidenciam que o agente não quis o resultado nem assumiu o risco de produzi-lo, a pena é de",["reclusão, de quatro a doze anos.","reclusão, de seis a vinte anos.","reclusão, de doze a trinta anos.","detenção, de um a três anos.","reclusão, de dois a oito anos."],1,"Art. 129, § 3º.")]
t1="<strong>Agressão em casa termina em fratura</strong><br><br>Em Vila Nova, cidade fictícia, um homem agrediu a companheira com socos e chutes durante uma discussão. A vítima sofreu fratura que a deixou incapacitada para suas ocupações habituais por 45 dias. A Guarda Municipal foi acionada pela vizinhança e conduziu o agressor à delegacia."
t2="<strong>Briga entre amigos na praça</strong><br><br>Dois amigos discutiram em uma praça e trocaram socos. Cada um sofreu escoriações leves, sem incapacidade ou perigo de vida, e as lesões foram recíprocas. A Guarda Municipal separou os dois e acionou a polícia."
tx={"cp2a":t1,"cp2b":t2}
# n=1
q(1,"A pena do crime de lesão corporal de natureza leve (art. 129, caput) é de",["detenção, de três meses a um ano.","reclusão, de um a cinco anos.","detenção, de um a três anos.","reclusão, de dois a oito anos.","detenção, de seis meses a dois anos."],"Art. 129, caput.")
q(1,"Ofender a integridade corporal ou a saúde de outrem é o crime de",["lesão corporal.","homicídio.","periclitação da vida.","maus-tratos.","rixa."],"Art. 129, caput.")
q(1,"A pena da lesão corporal de natureza grave é de",["reclusão, de um a cinco anos.","detenção, de três meses a um ano.","reclusão, de dois a oito anos.","reclusão, de quatro a doze anos.","detenção, de um a três anos."],"Art. 129, § 1º.")
q(1,"A pena da lesão corporal de natureza gravíssima é de",["reclusão, de dois a oito anos.","reclusão, de um a cinco anos.","detenção, de dois a oito anos.","reclusão, de quatro a doze anos.","reclusão, de três a dez anos."],"Art. 129, § 2º.")
q(1,"É lesão corporal de natureza grave a que resulta",["incapacidade para as ocupações habituais por mais de trinta dias.","incapacidade para as ocupações habituais por mais de dez dias.","qualquer dor.","escoriações leves.","um hematoma."],"Art. 129, § 1º, I.")
q(1,"É lesão corporal de natureza grave a que resulta",["perigo de vida.","perda de membro.","deformidade permanente.","enfermidade incurável.","aborto."],"Art. 129, § 1º, II.")
q(1,"É lesão corporal de natureza grave a que resulta",["aceleração de parto.","aborto.","deformidade permanente.","incapacidade permanente para o trabalho.","enfermidade incurável."],"Art. 129, § 1º, IV.")
q(1,"É lesão corporal de natureza gravíssima a que resulta",["incapacidade permanente para o trabalho.","incapacidade por mais de trinta dias.","perigo de vida.","aceleração de parto.","debilidade permanente."],"Art. 129, § 2º, I.")
q(1,"É lesão corporal de natureza gravíssima a que resulta",["enfermidade incurável.","perigo de vida.","incapacidade por 31 dias.","aceleração de parto.","debilidade permanente."],"Art. 129, § 2º, II.")
q(1,"É lesão corporal de natureza gravíssima a que resulta",["perda ou inutilização de membro, sentido ou função.","debilidade permanente de membro.","perigo de vida.","incapacidade por mais de trinta dias.","aceleração de parto."],"Art. 129, § 2º, III.")
q(1,"É lesão corporal de natureza gravíssima a que resulta",["deformidade permanente.","aceleração de parto.","perigo de vida.","debilidade permanente.","incapacidade por 40 dias."],"Art. 129, § 2º, IV.")
q(1,"É lesão corporal de natureza gravíssima a que resulta",["aborto.","aceleração de parto.","perigo de vida.","fratura simples.","hematoma."],"Art. 129, § 2º, V.")
q(1,"A pena da lesão corporal seguida de morte, nos termos do § 3º do art. 129, é de",["reclusão, de quatro a doze anos.","reclusão, de seis a vinte anos.","reclusão, de doze a trinta anos.","detenção, de um a três anos.","reclusão, de dois a oito anos."],"Art. 129, § 3º.")
q(1,"A pena da lesão corporal culposa é de",["detenção, de dois meses a um ano.","detenção, de três meses a um ano.","reclusão, de um a cinco anos.","detenção, de seis meses a dois anos.","reclusão, de dois a oito anos."],"Art. 129, § 6º.")
q(1,"O juiz pode reduzir a pena de um sexto a um terço, na lesão corporal, se o agente comete o crime impelido por motivo de relevante valor social ou moral, ou",["sob o domínio de violenta emoção, logo em seguida a injusta provocação da vítima.","por motivo fútil.","com emprego de veneno.","contra a mulher.","por motivo torpe."],"Art. 129, § 4º.")
q(1,"A lesão corporal praticada contra o companheiro, no contexto doméstico, tem pena de",["reclusão, de dois a cinco anos.","detenção, de três meses a um ano.","detenção, de seis meses a dois anos.","reclusão, de um a cinco anos.","reclusão, de quatro a doze anos."],"Art. 129, § 9º.")
q(1,"A lesão corporal praticada contra a mulher, por razões da condição do sexo feminino, tem pena de",["reclusão, de dois a cinco anos.","detenção, de três meses a um ano.","reclusão, de um a cinco anos.","reclusão, de quatro a doze anos.","detenção, de dois a cinco anos."],"Art. 129, § 13.")
q(1,"No texto da agressão doméstica, a incapacidade para as ocupações habituais por 45 dias qualifica a lesão como",["grave.","leve.","gravíssima.","culposa.","seguida de morte."],"Incapacidade por mais de trinta dias: § 1º, I.","cp2a")
q(1,"No texto, o agressor agrediu a companheira, o que se enquadra no § 9º, que prevê pena de",["reclusão, de dois a cinco anos.","detenção, de três meses a um ano.","reclusão, de quatro a doze anos.","detenção, de dois a seis anos.","reclusão, de seis a vinte anos."],"Art. 129, § 9º.","cp2a")
q(1,"O art. 129 do Código Penal protege",["a integridade corporal e a saúde de outra pessoa.","somente a vida.","somente o patrimônio.","a honra da vítima.","a liberdade sexual."],"Art. 129, caput.")
# n=2
q(2,"A lesão corporal em que resulta debilidade permanente de membro, sentido ou função é",["grave.","gravíssima.","leve.","culposa.","atenuada."],"Art. 129, § 1º, III.")
q(2,"A lesão seguida de morte, nos termos do § 3º, é crime",["preterdoloso.","doloso em relação à morte.","culposo em relação à lesão.","sempre culposo.","sempre doloso."],"O agente quis a lesão, mas não quis a morte nem assumiu o risco.")
q(2,"Na lesão corporal, o juiz, não sendo graves as lesões, pode substituir a pena de detenção pela de multa se",["as lesões são recíprocas.","a vítima é idosa.","o agente é reincidente.","há dolo eventual.","a lesão é gravíssima."],"Art. 129, § 5º, II.")
q(2,"A substituição da detenção pela multa, na lesão corporal leve, é possível se ocorre",["qualquer das hipóteses do § 4º ou se as lesões são recíprocas.","apenas o caso de lesões recíprocas.","apenas o caso de relevante valor social.","a confissão do agente.","a reparação do dano."],"Art. 129, § 5º, I e II.")
q(2,"Aumenta-se a pena de um terço na lesão culposa se ocorrer qualquer das hipóteses",["dos §§ 4º e 6º do art. 121.","do art. 128.","do art. 140.","do art. 155.","do art. 157."],"Art. 129, § 7º.")
q(2,"O perdão judicial do art. 121, § 5º, aplica-se, por força do § 8º do art. 129,",["à lesão culposa.","à lesão dolosa.","à lesão gravíssima.","à lesão seguida de morte.","a todas as lesões."],"Art. 129, § 8º.")
q(2,"No contexto da violência doméstica, a lesão do § 9º pode ocorrer contra",["ascendente, descendente, irmão, cônjuge ou companheiro.","qualquer estranho.","apenas o cônjuge.","apenas o companheiro.","apenas descendentes."],"Art. 129, § 9º.")
q(2,"O § 11 do art. 129 prevê aumento de um terço na hipótese do § 9º se o crime for cometido contra pessoa",["portadora de deficiência.","idosa.","gestante.","menor de 14 anos.","maior de 60 anos."],"Art. 129, § 11.")
q(2,"O § 10 do art. 129 prevê aumento de um terço nos casos dos §§ 1º a 3º se as circunstâncias são as do",["§ 9º.","§ 4º.","§ 5º.","§ 6º.","§ 8º."],"Art. 129, § 10.")
q(2,"Quanto ao § 12, a pena é aumentada se a lesão dolosa é praticada contra",["agente descrito nos arts. 142 e 144 da Constituição, no exercício da função ou em decorrência dela.","qualquer funcionário público, em qualquer caso.","somente autoridade judiciária.","somente agente penitenciário.","apenas militares."],"Art. 129, § 12, I, a.")
q(2,"O § 12, I, c, do art. 129 aumenta a pena da lesão dolosa praticada",["nas dependências de instituição de ensino.","em via pública.","à noite.","em local fechado.","contra qualquer estranho."],"Art. 129, § 12, I, c.")
q(2,"O § 3º-A do art. 129 prevê reclusão de 20 a 40 anos para a lesão seguida de morte no contexto de",["organização criminosa ultraviolenta, grupo paramilitar ou milícia privada.","rixa.","violência doméstica.","crime culposo.","legítima defesa."],"Art. 129, § 3º-A.")
q(2,"O § 8º-A do art. 129 aumenta a pena em 2/3 se a lesão é praticada por",["integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada.","reincidente.","cônjuge.","funcionário público.","agente menor de 21 anos."],"Art. 129, § 8º-A.")
q(2,"A lesão corporal que provoca aborto na vítima é",["gravíssima.","grave.","leve.","culposa.","atenuada."],"Art. 129, § 2º, V.")
q(2,"A lesão corporal que provoca aceleração de parto é",["grave.","gravíssima.","leve.","culposa.","seguida de morte."],"Art. 129, § 1º, IV.")
q(2,"Na lesão corporal, quem se autolesiona",["não comete o crime do art. 129, que protege a integridade corporal de outrem.","responde por lesão leve.","responde por lesão grave.","responde por perigo da vida.","responde por rixa."],"O tipo diz “integridade corporal ou a saúde de outrem”.")
q(2,"A lesão corporal culposa é aquela em que",["o agente causa lesão por imprudência, negligência ou imperícia, sem querer o resultado.","o agente quer o resultado.","o agente assume o risco.","a vítima consente.","a lesão é recíproca."],"Art. 129, § 6º.")
q(2,"No texto da briga de amigos, as lesões recíprocas e leves permitem ao juiz",["substituir a detenção pela multa.","aumentar a pena em um terço.","aplicar a pena de reclusão.","aplicar o § 9º.","aplicar o § 3º."],"Art. 129, § 5º, II.","cp2b")
q(2,"No texto da briga de amigos, a lesão é classificada como",["leve, com pena de detenção de três meses a um ano.","grave.","gravíssima.","seguida de morte.","culposa."],"Sem incapacidade ou perigo: art. 129, caput.","cp2b")
q(2,"No texto da agressão doméstica, a lesão contra a companheira, com incapacidade de 45 dias, é, ao mesmo tempo, grave e doméstica. Nessa hipótese, o § 10 prevê",["aumento da pena em um terço.","diminuição de um terço.","absolvição.","substituição por multa.","perdão judicial."],"Art. 129, § 10.","cp2a")
# n=3
q(3,"Assinale a alternativa que traz apenas hipóteses de lesão corporal gravíssima.",["Incapacidade permanente para o trabalho, enfermidade incurável e perda de membro.","Perigo de vida, aceleração de parto e debilidade permanente.","Incapacidade por mais de trinta dias, aborto e deformidade.","Aceleração de parto, aborto e enfermidade.","Perigo de vida, enfermidade e perda de sentido."],"Art. 129, § 2º.")
q(3,"Assinale a alternativa que traz apenas hipóteses de lesão corporal grave.",["Incapacidade por mais de trinta dias, perigo de vida, debilidade permanente e aceleração de parto.","Incapacidade permanente, enfermidade incurável e perda de membro.","Aborto, deformidade e perigo de vida.","Aceleração de parto, aborto e debilidade.","Perda de sentido, enfermidade e perigo de vida."],"Art. 129, § 1º.")
q(3,"Considere as afirmações. I. A lesão leve tem pena de detenção. II. A lesão grave tem pena de reclusão de um a cinco anos. III. A lesão gravíssima tem pena de reclusão de quatro a doze anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A gravíssima tem reclusão de dois a oito anos; de quatro a doze é a lesão seguida de morte.")
q(3,"Na lesão corporal seguida de morte, a pena de reclusão de quatro a doze anos justifica-se porque",["o agente não quis a morte nem assumiu o risco de produzi-la, havendo dolo apenas quanto à lesão.","o agente quis a morte.","há culpa quanto à lesão.","há legítima defesa.","a vítima consentiu."],"Art. 129, § 3º: crime preterdoloso.")
q(3,"Se a lesão dolosa é cometida em instituição de ensino e a vítima é pessoa com deficiência ou doença que acarrete condição limitante, a pena é aumentada de",["2/3 ao dobro.","1/3 a 2/3.","metade.","um sexto.","1/3, apenas."],"Art. 129, § 12, II, a.")
q(3,"Se a lesão dolosa, em instituição de ensino, é cometida por ascendente, tio, irmão, cônjuge, tutor ou por professor ou funcionário da instituição, a pena é aumentada de",["2/3 ao dobro.","1/3 a 2/3.","metade.","1/6.","1/3, apenas."],"Art. 129, § 12, II, b.")
q(3,"O § 9º do art. 129 trata da lesão corporal quando a vítima é, entre outros,",["pessoa com quem o agente conviva ou tenha convivido.","qualquer pessoa em via pública.","desconhecida do agente.","apenas pessoa idosa.","apenas criança."],"Art. 129, § 9º.")
q(3,"Assinale a INCORRETA.",["A lesão culposa tem pena de reclusão de um a cinco anos.","A lesão leve tem pena de detenção de três meses a um ano.","A lesão seguida de morte tem pena de reclusão de quatro a doze anos.","A lesão grave tem pena de reclusão de um a cinco anos.","A lesão doméstica tem pena de reclusão de dois a cinco anos."],"A lesão culposa tem detenção de dois meses a um ano.")
q(3,"Quanto à lesão corporal contra a mulher por razões da condição do sexo feminino, o § 13 prevê",["reclusão, de dois a cinco anos.","detenção, de três meses a um ano.","reclusão, de quatro a doze anos.","detenção, de dois a cinco anos.","reclusão, de um a cinco anos."],"Art. 129, § 13.")
q(3,"A causa de diminuição do § 4º do art. 129 reproduz a do art. 121, § 1º, e permite reduzir a pena de",["um sexto a um terço.","um terço à metade.","metade a dois terços.","um quinto a um quarto.","um décimo a um quinto."],"Art. 129, § 4º.")
q(3,"No § 5º, o juiz pode substituir a detenção pela multa, desde que",["as lesões não sejam graves.","a vítima concorde.","o autor seja primário.","a lesão seja gravíssima.","haja perdão judicial."],"Art. 129, § 5º: “não sendo graves as lesões”.")
q(3,"O § 10 do art. 129 aumenta em um terço a pena dos §§ 1º a 3º quando as circunstâncias são as do § 9º. Isso significa que",["a lesão grave, gravíssima ou seguida de morte em contexto doméstico tem pena aumentada em um terço.","a lesão leve em contexto doméstico tem pena menor.","a lesão doméstica é sempre leve.","o aumento só vale para a lesão culposa.","não há aumento."],"Art. 129, § 10.")
q(3,"A lesão dolosa contra agente de segurança pública, no exercício da função, tem pena aumentada de 1/3 a 2/3. Essa regra está no",["§ 12, I, a, do art. 129.","§ 4º do art. 129.","§ 5º do art. 129.","art. 121, § 4º.","art. 140."],"Art. 129, § 12, I, a.")
q(3,"A lesão corporal leve praticada por um dos contendores, quando as lesões são recíprocas,",["admite substituição da detenção pela multa, se as lesões não são graves.","é sempre punida com reclusão.","tem pena aumentada.","é crime hediondo.","não admite substituição."],"Art. 129, § 5º, II.")
q(3,"Considere o art. 129, § 7º. A pena da lesão culposa é aumentada de um terço quando",["resulta de inobservância de regra técnica de profissão, arte ou ofício, ou o agente deixa de prestar socorro, entre outras hipóteses do art. 121, § 4º.","o agente é reincidente.","o crime é praticado à noite.","a vítima é maior de 60 anos.","a lesão é leve."],"Art. 129, § 7º, com remissão ao art. 121, §§ 4º e 6º.")
q(3,"Assinale a alternativa que diferencia corretamente aborto e aceleração de parto como resultado da lesão corporal.",["O aborto torna a lesão gravíssima; a aceleração de parto a torna grave.","Ambos tornam a lesão gravíssima.","Ambos tornam a lesão grave.","O aborto torna a lesão grave; a aceleração de parto a torna gravíssima.","Nenhum dos dois altera a gravidade."],"Art. 129, § 2º, V, e § 1º, IV.")
q(3,"A lesão dolosa contra membro do Poder Judiciário, do Ministério Público, da Defensoria Pública ou da Advocacia Pública, no exercício da função ou em decorrência dela, tem a pena aumentada, segundo o § 12, I, b, de",["1/3 a 2/3.","2/3 ao dobro.","metade.","1/6.","dobro."],"Art. 129, § 12, I, b.")
q(3,"Considere o § 3º-A. Se a lesão seguida de morte é cometida no contexto da atuação de organização criminosa ultraviolenta, a pena é de",["reclusão, de 20 a 40 anos.","reclusão, de 4 a 12 anos.","reclusão, de 6 a 20 anos.","reclusão, de 12 a 30 anos.","reclusão, de 2 a 8 anos."],"Art. 129, § 3º-A.")
q(3,"No texto da agressão doméstica, a lesão grave cometida contra a companheira, nas circunstâncias do § 9º, sofre",["aumento de um terço, segundo o § 10.","diminuição de um terço.","substituição por multa.","absolvição.","perdão judicial."],"Art. 129, § 10.","cp2a")
q(3,"No texto da briga de amigos, o fato de as lesões serem recíprocas é circunstância que, segundo o art. 129,",["permite ao juiz substituir a pena de detenção pela de multa.","impede qualquer pena.","exige reclusão.","configura lesão grave.","configura crime hediondo."],"Art. 129, § 5º, II.","cp2b")
assert len(Q)==60,len(Q)
code,svg=mapa("Lesão corporal: da leve à seguida de morte",[
 ("leve","Leve",["detenção, 3 meses a 1 ano","art. 129, caput","integridade ou saúde de outrem"],"seção 1"),
 ("grave","Grave",["reclusão, 1 a 5 anos","mais de 30 dias, perigo de vida","debilidade permanente, aceleração de parto"],"seção 1"),
 ("grav","Gravíssima",["reclusão, 2 a 8 anos","incapacidade permanente, enfermidade incurável","perda, deformidade, aborto"],"seção 1"),
 ("morte","Seguida de morte",["reclusão, 4 a 12 anos","preterdolosa","20 a 40 com organização"],"seção 2"),
 ("culp","Culposa",["detenção, 2 meses a 1 ano","aumento de 1/3","perdão judicial"],"seção 2"),
 ("dom","Doméstica e aumentos",["§ 9º: reclusão, 2 a 5 anos","§ 12: agentes e escola","§ 13: sexo feminino"],"seção 3")],
 "Na prova: conte as palavras “permanente”, “perda” e “mais de trinta dias” para classificar a lesão")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As três primeiras caixas marcam a escada de gravidade; as demais, as figuras que fogem dela.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), art. 129, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-2","Lesões corporais (CP, art. 129)",Q,list(tx),
 cobertura=["Recorte do edital: art. 129. Cobertos: caput e §§ 1º a 13, incluindo §§ 3º-A e 8º-A."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; o art. 129 teve alterações muito recentes (2024 a 2026) e o texto deve ser reconferido no Planalto.","Os trechos de lei foram copiados do arquivo fontes/cp.txt por programa.","Os §§ 3º-A, 8º-A e 12 citam a “lei que institui o marco legal do combate ao crime organizado no Brasil” sem número; conferir.","Os casos cp2a e cp2b são fictícios."],
 fontes_conferidas=["CP, art. 129: texto da Câmara, copiado por programa."])
gravar("cp-2",aula_html,banco("cp-2",Q),tx)
