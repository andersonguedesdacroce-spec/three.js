import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes contra a vida abrem a parte especial do Código Penal e são, junto com os crimes contra o patrimônio, os mais cobrados. A Vunesp cobra os arts. 121 a 128 de três maneiras: a pena de cada crime, o que qualifica ou privilegia o homicídio, e quem pratica o quê no feminicídio, no infanticídio e no aborto. Esta aula usa o texto consolidado vigente, que mudou bastante nos últimos anos (feminicídio como crime autônomo, vicaricídio, novas qualificadoras), e aponta onde a prova costuma trocar um número."
S={}
S[1]="## 1. Homicídio: simples, privilegiado e qualificado\n\n"+L("art. 121, caput","Art. 121. Matar alguém:","Caso de diminuição de pena")+"""

O homicídio simples é matar alguém, e a pena é de seis a vinte anos de reclusão. Tudo no art. 121 vai se somando a esse tipo básico: o juiz pode diminuir a pena (homicídio privilegiado), o crime pode ser qualificado e ter pena maior, e há aumentos para casos especiais.

"""+L("§ 1º","§ 1º Se o agente comete o crime impelido","Homicídio qualificado")+"""

A diminuição de um sexto a um terço depende de motivo de relevante valor social ou moral, ou de violenta emoção logo em seguida a injusta provocação da vítima. O sentimento tem de ser forte e a reação, imediata. É uma causa de diminuição de pena, não uma exclusão do crime.

"""+L("§ 2º, caput e incisos I a V","§ 2º Se o homicídio é cometido:","Feminicídio")+"\n\n"+L("§ 2º, incisos VII, IX e X (parte)","VII - contra:","VIII - com emprego")+"\n\n"+L("§ 2º, incisos IX e X e pena","IX - contra menor de 14 (quatorze) anos:","§ 2º-A.")+"""

O homicídio qualificado tem pena de reclusão de doze a trinta anos. A prova cobra as qualificadoras pelo motivo (paga, promessa de recompensa, torpe, fútil), pelo meio (veneno, fogo, explosivo, asfixia, tortura, meio insidioso ou cruel) e pelo modo (traição, emboscada, dissimulação, recurso que dificulte ou impossibilite a defesa), além da finalidade de assegurar a execução, a ocultação, a impunidade ou a vantagem de outro crime. Há ainda qualificadoras ligadas à vítima: autoridade ou agente dos arts. 142 e 144 da Constituição (que inclui as guardas municipais, art. 144, § 8º), integrantes do sistema prisional e da Força Nacional, membros do Judiciário, do Ministério Público, da Defensoria e da Advocacia Pública, oficial de justiça, menor de 14 anos e crime nas dependências de instituição de ensino.

[[NOTA: O inciso VIII, que qualificaria o homicídio praticado com arma de fogo de uso restrito ou proibido, foi vetado e o veto foi mantido pelo Congresso: não está em vigor, ainda que o texto apareça nas compilações. O inciso VI, do feminicídio, foi revogado, porque o feminicídio passou a crime autônomo (art. 121-A).]]
"""
S[2]="## 2. Aumentos, homicídio culposo e crime organizado\n\n"+L("§ 2º-D","§ 2º-D. Se o homicídio doloso é cometido por integrante","Homicídio culposo")+"\n\n"+L("§ 3º","§ 3º Se o homicídio é culposo:","Aumento de pena")+"\n\n"+L("§ 4º","§ 4º No homicídio culposo, a pena é aumentada","§ 5º")+"\n\n"+L("§ 5º","§ 5º Na hipótese de homicídio culposo, o juiz poderá","§ 6º")+"\n\n"+L("§ 6º","§ 6º A pena é aumentada de 1/3 (um terço) até a metade se o crime","§ 7º")+"""

O homicídio culposo, quando não há intenção, é punido com detenção de um a três anos. A pena aumenta em um terço se o crime resulta de inobservância de regra técnica de profissão, arte ou ofício, ou se o agente deixa de prestar socorro imediato, não procura diminuir as consequências ou foge para evitar o flagrante. A segunda parte do § 4º trata do homicídio doloso: aumenta-se um terço se a vítima é menor de 14 ou maior de 60 anos. É a pegadinha clássica: o mesmo parágrafo, duas situações diferentes.

O § 5º prevê o perdão judicial para o homicídio culposo em que as consequências atingem o próprio agente de modo tão grave que a pena se torna desnecessária. O § 6º aumenta a pena de um terço até a metade quando o crime é praticado por milícia privada, sob pretexto de prestação de serviço de segurança, ou por grupo de extermínio. E o § 2º-D, mais recente, fixa reclusão de vinte a quarenta anos para o homicídio doloso praticado por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada.
"""
S[3]="## 3. Feminicídio e vicaricídio\n\n"+L("art. 121-A","Art. 121-A. Matar mulher","§ 2º A pena do feminicídio")+"\n\n"+L("art. 121-A, § 2º","§ 2º A pena do feminicídio é aumentada","Coautoria")+"\n\n"+L("art. 121-A, § 3º","§ 3º Comunicam-se ao coautor ou partícipe","Vicaricídio")+"""

O feminicídio deixou de ser qualificadora do homicídio e é hoje crime autônomo, com pena de reclusão de vinte a quarenta anos. Ocorre por razões da condição do sexo feminino, e a lei diz quando: violência doméstica e familiar, ou menosprezo ou discriminação à condição de mulher. A pena aumenta de um terço até a metade em hipóteses como a gestação, a vítima menor de 14 ou maior de 60 anos ou com deficiência, a presença de descendente ou ascendente e o descumprimento de medida protetiva da Lei Maria da Penha.

"""+L("art. 121-B","Art. 121-B. Matar descendente","Induzimento, instigação ou auxílio")+"""

O vicaricídio é a morte de filho, ascendente, dependente, enteado ou pessoa sob guarda da mulher, com o fim específico de causar-lhe sofrimento, punição ou controle, no contexto de violência doméstica e familiar. A pena é a mesma do feminicídio, de vinte a quarenta anos, com aumentos para os casos em que o crime é praticado na presença da mulher, contra criança, adolescente, idoso ou pessoa com deficiência, ou em descumprimento de medida protetiva.
"""
S[4]="## 4. Induzimento ao suicídio e infanticídio\n\n"+L("art. 122, caput e §§ 1º e 2º","Art. 122. Induzir ou instigar","§ 3º A pena é duplicada")+"\n\n"+L("art. 122, §§ 3º a 5º","§ 3º A pena é duplicada","§ 6º")+"""

A conduta é induzir ou instigar alguém ao suicídio ou à automutilação, ou prestar auxílio material para que o faça. A pena é de reclusão de seis meses a dois anos. Se da automutilação ou da tentativa de suicídio resulta lesão corporal de natureza grave ou gravíssima, a reclusão é de um a três anos; se o suicídio se consuma, ou se da automutilação resulta morte, a reclusão é de dois a seis anos. A pena é duplicada se o motivo é egoístico, torpe ou fútil, ou se a vítima é menor ou tem diminuída a capacidade de resistência, e aumentada até o dobro se feito por rede de computadores, rede social ou transmissão em tempo real.

"""+L("art. 123","Art. 123. Matar, sob a influência","Aborto provocado pela gestante")+"""

O infanticídio é crime próprio: só a mãe o pratica, sob a influência do estado puerperal, durante o parto ou logo após, contra o próprio filho. A pena é de detenção de dois a seis anos, bem mais branda que a do homicídio, justamente por causa do estado puerperal.
"""
S[5]="## 5. Aborto\n\n"+L("art. 124","Art. 124. Provocar aborto em si mesma","Aborto provocado por terceiro")+"\n\n"+L("arts. 125 e 126","Art. 125. Provocar aborto, sem o consentimento","Forma qualificada")+"\n\n"+L("art. 127","Art. 127. As penas cominadas","Art. 128.")+"""

O aborto é a interrupção da gravidez com a morte do feto. Há três figuras: o autoaborto ou o consentimento para que outro o provoque (art. 124, detenção de um a três anos); o aborto provocado por terceiro sem o consentimento da gestante (art. 125, reclusão de três a dez anos); e o aborto provocado por terceiro com o consentimento dela (art. 126, reclusão de um a quatro anos). Se a gestante não é maior de 14 anos, é alienada ou débil mental, ou se o consentimento é obtido por fraude, grave ameaça ou violência, aplica-se a pena do art. 125. No art. 127, as penas dos arts. 125 e 126 aumentam um terço se a gestante sofre lesão grave, e dobram se ela morre.

"""+L("art. 128","Art. 128. Não se pune o aborto praticado por médico:","CAPÍTULO II")+"""

As exceções do art. 128 exigem que o aborto seja praticado por médico: o aborto necessário, quando não há outro meio de salvar a vida da gestante, e o aborto da gravidez resultante de estupro, com consentimento da gestante ou, se incapaz, de seu representante legal. Na prova, repare que a lei não exige autorização judicial nem boletim de ocorrência nesses casos.
"""
S[7]="""## 7. Na rotina do guarda

- **Local de morte violenta:** isolar a área e preservar vestígios até a chegada da polícia judiciária e da perícia, porque o homicídio exige prova técnica.
- **Violência doméstica contra a mulher:** reconhecer sinais que levam ao feminicídio e acionar a rede de proteção; o descumprimento de medida protetiva é causa de aumento.
- **Socorro à vítima:** o agente que deixa de prestar socorro imediato pode ter a pena aumentada no homicídio culposo, e a omissão de socorro é crime autônomo (art. 135).
- **Crime contra o próprio agente:** matar guarda municipal no exercício da função ou em razão dela qualifica o homicídio, por força do art. 144 da Constituição, citado no art. 121, § 2º, VII.
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do homicídio simples | Reclusão de seis a vinte anos |
| Pena do qualificado | Reclusão de doze a trinta anos |
| Pena do culposo | Detenção de um a três anos |
| Feminicídio como qualificadora | Hoje é crime autônomo (art. 121-A), reclusão de vinte a quarenta anos |
| Aumento do § 4º só para o culposo | A segunda parte vale para o doloso: menor de 14 ou maior de 60 anos |
| Pena do infanticídio | Detenção de dois a seis anos; crime próprio da mãe |
| Aborto com consentimento | Art. 126, reclusão de um a quatro anos |
| Exigir autorização judicial para o aborto legal | O art. 128 exige apenas médico e os requisitos de cada inciso |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Homicídio simples | Reclusão de 6 a 20 anos |
| Privilegiado | Redução de 1/6 a 1/3: valor social ou moral, violenta emoção |
| Qualificado | Reclusão de 12 a 30 anos; motivo, meio, modo, fim, vítima |
| Culposo | Detenção de 1 a 3 anos; aumento de 1/3 em hipóteses do § 4º |
| Milícia e extermínio | Aumento de 1/3 até a metade (§ 6º) |
| Feminicídio | Art. 121-A: reclusão de 20 a 40 anos |
| Induzimento | Art. 122: reclusão de 6 meses a 2 anos |
| Infanticídio | Detenção de 2 a 6 anos; só a mãe, estado puerperal |
| Aborto | 124: 1 a 3 (detenção); 125: 3 a 10; 126: 1 a 4 |
| Aborto legal | Médico; risco de vida ou estupro |
"""
QR=[("Questão 1","Segundo o Código Penal, a pena do homicídio simples é de",["reclusão, de seis a vinte anos.","reclusão, de doze a trinta anos.","detenção, de um a três anos.","reclusão, de oito a quinze anos.","detenção, de seis a vinte anos."],0,"Art. 121, caput."),
("Questão 2","O homicídio cometido por motivo fútil é",["qualificado, com reclusão de doze a trinta anos.","simples, com reclusão de seis a vinte anos.","privilegiado, com redução de pena.","culposo, com detenção.","crime autônomo, com reclusão de oito a doze anos."],1,"Art. 121, § 2º, II."),
("Questão 3","O art. 121, § 4º, prevê aumento de um terço no homicídio doloso se a vítima é",["menor de 14 ou maior de 60 anos.","menor de 18 ou maior de 65 anos.","mulher ou criança.","maior de 70 anos.","menor de 12 anos."],4,"Art. 121, § 4º, segunda parte."),
("Questão 4","O feminicídio, hoje, é previsto",["como crime autônomo, no art. 121-A, com reclusão de vinte a quarenta anos.","como qualificadora do art. 121, § 2º, VI.","como causa de aumento do § 4º.","apenas na Lei Maria da Penha.","como contravenção penal."],3,"Art. 121-A.")]
t1="<strong>Briga de bar termina em morte</strong><br><br>Em uma madrugada, em Vila Nova, cidade fictícia, um homem matou outro a facadas depois de uma discussão por causa de uma conta de bar. Segundo testemunhas, o autor, que estava sob forte emoção, reagiu imediatamente a uma provocação injusta da vítima. A Guarda Municipal isolou o local, e a polícia civil instaurou inquérito."
t2="<strong>Mulher morta pelo companheiro</strong><br><br>Uma mulher foi morta pelo companheiro em casa, na presença do filho de 8 anos, após um histórico de ameaças. Ela havia obtido, dias antes, medida protetiva de urgência, que o autor descumpriu. A Guarda Municipal foi chamada pela vizinhança e prestou os primeiros atendimentos."
tx={"cp1a":t1,"cp1b":t2}
# n=1
q(1,"Segundo o art. 121 do Código Penal, a pena do homicídio simples é de",["reclusão, de seis a vinte anos.","reclusão, de doze a trinta anos.","detenção, de um a três anos.","reclusão, de oito a quinze anos.","detenção, de seis meses a dois anos."],"Art. 121, caput.")
q(1,"A pena do homicídio qualificado é de",["reclusão, de doze a trinta anos.","reclusão, de seis a vinte anos.","reclusão, de vinte a quarenta anos.","detenção, de um a três anos.","reclusão, de oito a quinze anos."],"Art. 121, § 2º.")
q(1,"A pena do homicídio culposo é de",["detenção, de um a três anos.","reclusão, de um a três anos.","detenção, de seis meses a dois anos.","reclusão, de dois a quatro anos.","detenção, de dois a seis anos."],"Art. 121, § 3º.")
q(1,"O homicídio cometido mediante paga ou promessa de recompensa, ou por outro motivo torpe, é",["qualificado.","simples.","privilegiado.","culposo.","atenuado."],"Art. 121, § 2º, I.")
q(1,"O homicídio cometido por motivo fútil é",["qualificado.","simples.","privilegiado.","culposo.","excluído de pena."],"Art. 121, § 2º, II.")
q(1,"É qualificadora do homicídio o emprego de",["veneno, fogo, explosivo, asfixia, tortura ou outro meio insidioso ou cruel.","arma de fogo de uso permitido.","faca de cozinha.","qualquer meio, desde que doloso.","objeto contundente apenas."],"Art. 121, § 2º, III.")
q(1,"É qualificadora do homicídio cometê-lo",["à traição, de emboscada ou mediante dissimulação que dificulte a defesa do ofendido.","por impulso.","em legítima defesa.","durante o dia.","sem premeditação."],"Art. 121, § 2º, IV.")
q(1,"O homicídio cometido para assegurar a execução, a ocultação, a impunidade ou a vantagem de outro crime é",["qualificado.","simples.","privilegiado.","culposo.","atenuado."],"Art. 121, § 2º, V.")
q(1,"No homicídio privilegiado, o juiz pode reduzir a pena de",["um sexto a um terço.","um terço à metade.","metade a dois terços.","um quinto a um quarto.","um décimo a um quinto."],"Art. 121, § 1º.")
q(1,"No homicídio culposo, o juiz poderá deixar de aplicar a pena, se as consequências da infração atingirem o próprio agente de forma tão grave que a sanção penal se torne desnecessária. Esse instituto é o",["perdão judicial.","indulto.","anistia.","graça.","livramento condicional."],"Art. 121, § 5º.")
q(1,"A pena do feminicídio, previsto no art. 121-A, é de",["reclusão, de vinte a quarenta anos.","reclusão, de doze a trinta anos.","reclusão, de seis a vinte anos.","detenção, de dois a seis anos.","reclusão, de oito a quinze anos."],"Art. 121-A.")
q(1,"Há razões da condição do sexo feminino, no feminicídio, quando o crime envolve",["violência doméstica e familiar ou menosprezo e discriminação à condição de mulher.","qualquer homicídio praticado contra mulher.","apenas violência doméstica.","apenas discriminação religiosa.","apenas crime em via pública."],"Art. 121-A, § 1º.")
q(1,"A pena do crime de induzimento, instigação ou auxílio a suicídio ou automutilação (art. 122, caput) é de",["reclusão, de seis meses a dois anos.","reclusão, de um a três anos.","detenção, de seis meses a dois anos.","reclusão, de dois a seis anos.","detenção, de um a três anos."],"Art. 122, caput.")
q(1,"O infanticídio consiste em matar, sob a influência do estado puerperal, o próprio filho",["durante o parto ou logo após.","em até um ano de vida.","em qualquer momento da infância.","somente antes do parto.","somente com premeditação."],"Art. 123.")
q(1,"Provocar aborto em si mesma ou consentir que outrem lho provoque (art. 124) tem pena de",["detenção, de um a três anos.","reclusão, de um a quatro anos.","reclusão, de três a dez anos.","detenção, de seis meses a um ano.","reclusão, de dois a quatro anos."],"Art. 124.")
q(1,"Provocar aborto sem o consentimento da gestante (art. 125) tem pena de",["reclusão, de três a dez anos.","reclusão, de um a quatro anos.","detenção, de um a três anos.","reclusão, de seis a vinte anos.","detenção, de três a dez anos."],"Art. 125.")
q(1,"Provocar aborto com o consentimento da gestante (art. 126) tem pena de",["reclusão, de um a quatro anos.","reclusão, de três a dez anos.","detenção, de um a três anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos."],"Art. 126.")
q(1,"Não se pune o aborto praticado por médico se não há outro meio de salvar a vida da gestante. Esse aborto é chamado de",["aborto necessário.","aborto eugênico.","aborto honoris causa.","aborto sentimental.","aborto econômico."],"Art. 128, I.")
q(1,"No texto, o autor reagiu sob forte emoção a uma provocação injusta da vítima. Se essa for a situação do § 1º do art. 121, o juiz",["pode reduzir a pena de um sexto a um terço.","deve absolver.","deve aplicar a pena em dobro.","deve aumentar a pena.","deve extinguir a punibilidade."],"Art. 121, § 1º: violenta emoção logo em seguida a injusta provocação.","cp1a")
q(1,"No texto da briga de bar, a medida de isolar o local pela Guarda Municipal serve, principalmente, para",["preservar os vestígios do crime até a perícia.","prender o suspeito.","julgar o autor.","encerrar o inquérito.","identificar a testemunha."],"Art. 6º, I, do CPP.","cp1a")
# n=2
q(2,"É causa de aumento de pena, em um terço, no homicídio culposo, se o crime resulta de",["inobservância de regra técnica de profissão, arte ou ofício.","motivo fútil.","emboscada.","violenta emoção.","motivo torpe."],"Art. 121, § 4º, primeira parte.")
q(2,"No homicídio culposo, a pena é aumentada de um terço se o agente",["deixa de prestar imediato socorro à vítima.","é primário.","é maior de 60 anos.","é funcionário público.","atua em legítima defesa."],"Art. 121, § 4º.")
q(2,"Sendo doloso o homicídio, a pena é aumentada de um terço se o crime é praticado contra pessoa",["menor de 14 ou maior de 60 anos.","menor de 18 ou maior de 65 anos.","do sexo feminino.","com deficiência, apenas.","menor de 12 anos."],"Art. 121, § 4º, segunda parte.")
q(2,"A pena é aumentada de um terço até a metade se o crime for praticado por",["milícia privada, sob pretexto de prestação de serviço de segurança, ou por grupo de extermínio.","funcionário público.","pessoa reincidente.","agente em estado de embriaguez.","agente menor de 21 anos."],"Art. 121, § 6º.")
q(2,"A pena do homicídio doloso cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada é de",["reclusão, de vinte a quarenta anos.","reclusão, de doze a trinta anos.","reclusão, de seis a vinte anos.","reclusão, de trinta a quarenta anos.","reclusão, de vinte a trinta anos."],"Art. 121, § 2º-D.")
q(2,"O homicídio cometido contra autoridade ou agente descrito nos arts. 142 e 144 da Constituição Federal, no exercício da função ou em decorrência dela, é",["qualificado.","simples.","privilegiado.","culposo.","atenuado."],"Art. 121, § 2º, VII, a.")
q(2,"Entre as vítimas que qualificam o homicídio, o art. 121, § 2º, inclui",["menor de 14 anos e membros do Judiciário, do Ministério Público e da Defensoria Pública, no exercício da função ou em decorrência dela.","apenas mulheres.","apenas idosos.","pessoas com mais de 70 anos.","apenas funcionários públicos."],"Art. 121, § 2º, VII, b, e IX.")
q(2,"O art. 121, § 2º, VIII (arma de fogo de uso restrito ou proibido) foi",["vetado, com o veto mantido pelo Congresso, e não está em vigor.","aprovado e vigente.","revogado em 2024.","declarado inconstitucional.","sancionado em 2019."],"A nota do texto consolidado indica veto mantido.")
q(2,"O feminicídio, no Código Penal, é",["crime autônomo previsto no art. 121-A.","qualificadora do homicídio, no art. 121, § 2º, VI.","contravenção penal.","causa de aumento do homicídio.","atenuante do homicídio."],"Art. 121-A. O inciso VI foi revogado.")
q(2,"A pena do feminicídio é aumentada de um terço até a metade se o crime é praticado, entre outras hipóteses,",["durante a gestação, nos três meses posteriores ao parto ou se a vítima é mãe ou responsável por criança, adolescente ou pessoa com deficiência.","em via pública.","por pessoa sem antecedentes.","de dia.","por mais de uma pessoa, em qualquer caso."],"Art. 121-A, § 2º, I.")
q(2,"No feminicídio, comunicam-se ao coautor ou partícipe",["as circunstâncias pessoais elementares do crime previstas no § 1º.","apenas as circunstâncias de caráter pessoal, em qualquer caso.","nenhuma circunstância.","apenas a pena.","apenas o motivo."],"Art. 121-A, § 3º.")
q(2,"O vicaricídio consiste em matar descendente, ascendente, dependente, enteado ou pessoa sob guarda da mulher",["com o fim específico de causar-lhe sofrimento, punição ou controle, no contexto de violência doméstica e familiar.","por motivo de herança.","em legítima defesa.","em qualquer circunstância.","por culpa."],"Art. 121-B.")
q(2,"Se o suicídio se consuma, ou se da automutilação resulta morte, a pena do art. 122, § 2º, é de",["reclusão, de dois a seis anos.","reclusão, de um a três anos.","reclusão, de seis meses a dois anos.","reclusão, de seis a vinte anos.","detenção, de dois a seis anos."],"Art. 122, § 2º.")
q(2,"A pena do induzimento a suicídio é duplicada se o crime é praticado",["por motivo egoístico, torpe ou fútil, ou se a vítima é menor ou tem diminuída a capacidade de resistência.","por funcionário público.","em via pública.","de dia.","por reincidente."],"Art. 122, § 3º.")
q(2,"Se a gestante não é maior de 14 anos, é alienada ou débil mental, ou se o consentimento é obtido mediante fraude, grave ameaça ou violência, aplica-se a pena",["do art. 125, aborto provocado sem consentimento.","do art. 124.","do art. 126.","do art. 123.","do art. 128."],"Art. 126, parágrafo único.")
q(2,"As penas dos arts. 125 e 126 são aumentadas de um terço se, em consequência do aborto ou dos meios empregados, a gestante",["sofre lesão corporal de natureza grave.","sofre lesão leve.","se arrepende.","é maior de 30 anos.","é casada."],"Art. 127.")
q(2,"No aborto da gravidez resultante de estupro, a exceção do art. 128 exige",["consentimento da gestante ou, quando incapaz, de seu representante legal.","autorização judicial prévia.","boletim de ocorrência.","laudo do IML.","idade gestacional inferior a 12 semanas."],"Art. 128, II.")
q(2,"Segundo o texto, a briga de bar terminou em morte. Para que haja homicídio privilegiado, o § 1º do art. 121 exige",["violenta emoção logo em seguida a injusta provocação da vítima.","premeditação.","motivo torpe.","uso de arma de fogo.","reincidência."],"Art. 121, § 1º.","cp1a")
q(2,"No texto da mulher morta pelo companheiro, o crime, em tese, é",["feminicídio, previsto no art. 121-A.","homicídio simples.","homicídio culposo.","infanticídio.","lesão corporal."],"Violência doméstica e familiar: art. 121-A, § 1º, I.","cp1b")
q(2,"No texto do feminicídio, a presença do filho e o descumprimento da medida protetiva",["são causas de aumento de pena.","são irrelevantes.","são causas de diminuição de pena.","extinguem a punibilidade.","transformam o crime em culposo."],"Art. 121-A, § 2º, III e IV.","cp1b")
# n=3
q(3,"Assinale a alternativa que contém apenas qualificadoras do homicídio previstas no art. 121, § 2º.",["Motivo fútil, emboscada e uso de veneno.","Violenta emoção, motivo torpe e legítima defesa.","Relevante valor moral, tortura e surpresa.","Culpa, dolo eventual e traição.","Estado puerperal, motivo fútil e asfixia."],"Art. 121, § 2º, I a IV.")
q(3,"Considere as afirmações sobre o art. 121. I. O homicídio privilegiado tem a pena reduzida de um sexto a um terço. II. O perdão judicial pode ser aplicado ao homicídio culposo. III. O homicídio qualificado tem pena de reclusão de seis a vinte anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"A pena do qualificado é de doze a trinta anos (III é falsa).")
q(3,"A causa de aumento do art. 121, § 4º (menor de 14 ou maior de 60 anos), aplica-se",["ao homicídio doloso.","ao homicídio culposo, apenas.","a qualquer homicídio, doloso ou culposo.","somente ao feminicídio.","somente ao infanticídio."],"Art. 121, § 4º, segunda parte.")
q(3,"No homicídio culposo, o aumento de um terço do § 4º NÃO se aplica quando o agente",["é primário.","foge para evitar a prisão em flagrante.","deixa de prestar socorro imediato.","não procura diminuir as consequências do ato.","age com inobservância de regra técnica de profissão."],"Art. 121, § 4º: a primariedade não é causa de aumento.")
q(3,"A pena do homicídio contra menor de 14 anos é aumentada, em 2/3, se o autor é",["ascendente, padrasto ou madrasta, tio, irmão, cônjuge, companheiro, tutor, curador, preceptor ou empregador da vítima, ou tem autoridade sobre ela.","qualquer pessoa.","funcionário público.","estrangeiro.","reincidente."],"Art. 121, § 2º-B, II.")
q(3,"No feminicídio, é causa de aumento de pena o crime praticado em descumprimento de medidas protetivas de urgência previstas",["nos incisos I, II e III do caput do art. 22 da Lei Maria da Penha.","em qualquer lei penal.","no art. 5º da Constituição.","na Lei de Contravenções Penais.","na Lei de Execução Penal."],"Art. 121-A, § 2º, IV.")
q(3,"Assinale a alternativa INCORRETA sobre o art. 121-A.",["A pena do feminicídio é de reclusão de seis a vinte anos.","Há razões de condição do sexo feminino quando o crime envolve violência doméstica e familiar.","O feminicídio é crime autônomo.","A pena é aumentada se o crime é praticado na presença de descendente ou de ascendente da vítima.","A pena é aumentada se a vítima é menor de 14 ou maior de 60 anos."],"A pena do feminicídio é de vinte a quarenta anos.")
q(3,"A pena do vicaricídio (art. 121-B) é aumentada de um terço até a metade se o crime é praticado",["na presença da mulher a quem se pretende causar sofrimento, punição ou controle.","em local público.","por reincidente.","com arma de fogo, em qualquer caso.","à noite."],"Art. 121-B, parágrafo único, I.")
q(3,"No art. 122, se da automutilação ou da tentativa de suicídio resulta lesão corporal de natureza grave ou gravíssima, a pena é de",["reclusão, de um a três anos.","reclusão, de dois a seis anos.","reclusão, de seis meses a dois anos.","detenção, de um a três anos.","reclusão, de três a oito anos."],"Art. 122, § 1º.")
q(3,"No art. 122, a pena é aumentada até o dobro se a conduta é realizada",["por meio da rede de computadores, de rede social ou transmitida em tempo real.","em lugar ermo.","à noite.","em local fechado.","por mais de duas pessoas."],"Art. 122, § 4º.")
q(3,"Se o crime de induzimento ao suicídio (§ 2º do art. 122) é cometido contra menor de 14 anos ou contra quem não tem o necessário discernimento, responde o agente pelo crime de",["homicídio, nos termos do art. 121.","infanticídio.","aborto.","lesão corporal grave.","omissão de socorro."],"Art. 122, § 7º.")
q(3,"Assinale a alternativa correta sobre o infanticídio.",["É crime próprio, praticado pela mãe contra o próprio filho, sob a influência do estado puerperal, durante o parto ou logo após.","Qualquer pessoa pode praticá-lo.","Exige premeditação.","A pena é de reclusão de seis a vinte anos.","Pode ser praticado a qualquer tempo após o parto."],"Art. 123.")
q(3,"Considere as afirmações. I. O aborto provocado por terceiro, sem consentimento da gestante, tem pena de reclusão de três a dez anos. II. O aborto com consentimento da gestante, praticado por médico, é sempre punido. III. O aborto necessário, praticado por médico, não é punido. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II e III, apenas.","I e II, apenas.","I, II e III."],"O art. 128 afasta a pena do aborto necessário e do aborto em gravidez resultante de estupro, quando feitos por médico.")
q(3,"A forma qualificada do aborto (art. 127) prevê aumento de um terço se a gestante sofre lesão corporal de natureza grave e duplicação da pena se",["lhe sobrevém a morte.","sofre lesão leve.","há dois abortos.","a gestante é menor.","há concurso de agentes."],"Art. 127.")
q(3,"O art. 121, § 2º, VIII, que tratava do emprego de arma de fogo de uso restrito ou proibido,",["foi vetado e o veto foi mantido; o dispositivo não está em vigor.","está em vigor e qualifica o homicídio.","foi revogado e substituído pelo art. 121-A.","foi declarado constitucional.","passou a integrar o § 6º."],"A consolidação marca o dispositivo como vetado.")
q(3,"A qualificadora que atinge a morte de agente descrito nos arts. 142 e 144 da Constituição inclui, entre outros, os integrantes",["das guardas municipais, por força do art. 144, § 8º.","apenas do Exército.","apenas da polícia militar.","apenas da polícia civil.","apenas dos agentes penitenciários."],"O art. 144, § 8º, trata das guardas municipais; o inciso VII, a, remete ao art. 144.")
q(3,"Assinale a alternativa correta sobre as penas dos crimes contra a vida.",["Homicídio culposo: detenção de um a três anos; homicídio qualificado: reclusão de doze a trinta anos.","Homicídio culposo: reclusão de um a três anos; qualificado: reclusão de seis a vinte anos.","Infanticídio: reclusão de seis a vinte anos; aborto com consentimento: detenção de um a quatro anos.","Feminicídio: reclusão de doze a trinta anos.","Autoaborto: reclusão de três a dez anos."],"Arts. 121, §§ 2º e 3º.")
q(3,"Considere as afirmações. I. O autoaborto (art. 124) tem pena de detenção de um a três anos. II. O aborto sem consentimento (art. 125) tem pena de reclusão de três a dez anos. III. O aborto com consentimento (art. 126) tem pena de detenção de um a quatro anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"O art. 126 prevê reclusão, não detenção.")
q(3,"No texto da briga de bar, o juiz reconheceu o homicídio privilegiado. A pena de seis a vinte anos pode ser reduzida de",["um sexto a um terço.","um terço à metade.","metade.","dois terços.","um quarto a um terço."],"Art. 121, § 1º.","cp1a")
q(3,"No texto do feminicídio, a pena do art. 121-A, com os aumentos dos incisos III e IV do § 2º, é aumentada de",["um terço até a metade.","metade a dois terços.","dois terços ao dobro.","um sexto a um terço.","apenas um sexto."],"Art. 121-A, § 2º.","cp1b")
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes contra a vida: do homicídio ao aborto",[
 ("hom","Homicídio",["simples: 6 a 20 anos","qualificado: 12 a 30 anos","privilegiado: reduz 1/6 a 1/3"],"seção 1"),
 ("cul","Culposo e aumentos",["detenção de 1 a 3 anos","§ 4º: 1/3","milícia: 1/3 até a metade"],"seção 2"),
 ("fem","Feminicídio",["art. 121-A: 20 a 40 anos","violência doméstica","menosprezo à condição de mulher"],"seção 3"),
 ("vic","Vicaricídio",["art. 121-B","fim de causar sofrimento","20 a 40 anos"],"seção 3"),
 ("sui","Suicídio e infanticídio",["art. 122: 6 meses a 2 anos","art. 123: só a mãe","detenção de 2 a 6 anos"],"seção 4"),
 ("abo","Aborto",["124: 1 a 3 (detenção)","125: 3 a 10; 126: 1 a 4","128: médico, 2 hipóteses"],"seção 5")],
 "Na prova: confira a pena de cada artigo e se o crime é doloso ou culposo")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"As três primeiras caixas tratam das mortes em sentido estrito; as demais, das figuras especiais.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 121 a 128, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-1","Crimes contra a vida (CP, arts. 121 a 128)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 121 a 128. Cobertos: arts. 121 (inclui §§ 2º-B a 2º-D e 6º), 121-A, 121-B, 122, 123, 124, 125, 126, 127 e 128."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir a redação vigente no Planalto, porque os arts. 121, 121-A e 121-B têm alterações muito recentes (2024 a 2026).","Os dispositivos do texto indicados como vetados ou revogados foram excluídos da aula (art. 121, § 2º, VIII, vetado, e VI, revogado).","Os quadros de lei foram copiados do arquivo fontes/cp.txt, sem digitação manual.","O § 2º-D e o § 2º-C citam a “lei que institui o marco legal do combate ao crime organizado no Brasil”, sem número na consolidação; conferir no Planalto.","Os casos cp1a e cp1b são fictícios."],
 fontes_conferidas=["CP, arts. 121 a 128: texto da Câmara, copiado por programa."])
gravar("cp-1",aula_html,banco("cp-1",Q),tx)
