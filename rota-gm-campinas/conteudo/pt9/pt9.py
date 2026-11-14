import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','gerador')); from aulas import *
LEAD="Concordância é o ajuste de forma entre palavras que se referem umas às outras: o verbo acompanha o sujeito, e o adjetivo acompanha o substantivo. A regra geral é curta; a prova mora nos casos especiais, quase sempre com o sujeito longe do verbo ou depois dele."
S={}
S[1]="""## 1. A regra geral da concordância verbal

O verbo concorda em **número** e **pessoa** com o núcleo do sujeito. O difícil não é a regra, é achar o núcleo. Duas situações escondem o sujeito.

A primeira é o **sujeito depois do verbo**. Pergunte “quem?” ou “o quê?” ao verbo e a resposta é o sujeito, mesmo que venha no fim:

1. **Chegaram** os reforços da Guarda.
2. **Faltam** dois agentes na escala.
3. **Ocorreram**, durante a madrugada, três furtos na região.

A segunda é o **sujeito longe do verbo**, com palavras no meio. O verbo concorda com o núcleo, não com a palavra mais próxima:

1. A **lista** com os nomes dos suspeitos **foi** entregue ao delegado.
2. O **número** de ocorrências nos bairros **aumentou**.

| Evite | Use |
| --- | --- |
| Chegou os reforços da Guarda | **Chegaram** os reforços da Guarda |
| Falta dois agentes na escala | **Faltam** dois agentes na escala |
| A lista com os nomes dos suspeitos foram entregues | A lista com os nomes dos suspeitos **foi entregue** |
"""
S[2]="""## 2. Sujeito composto

Com sujeito composto **antes do verbo**, o verbo vai para o plural: “O guarda e o motorista **discutiram**.”

Com sujeito composto **depois do verbo**, o verbo pode ir para o plural ou concordar com o núcleo mais próximo: “**Chegaram** o guarda e o motorista” ou “**Chegou** o guarda e o motorista”.

Quando os núcleos são de **pessoas diferentes**, vence a 1ª pessoa; sem a 1ª, vence a 2ª ou se usa a 3ª do plural:

1. Eu e você **iremos** à reunião. (eu + você = nós)
2. Tu e ele **ireis** à reunião, ou tu e ele **irão**.

Três situações pedem atenção:

- Núcleos ligados por **ou** com sentido de exclusão levam o verbo ao singular: “O guarda ou o fiscal **assinará** o termo” (só um assina). Com sentido de inclusão, plural: “Furto ou roubo **exigem** registro.”
- Núcleos resumidos por **tudo, nada, ninguém** levam o verbo ao singular: “Viaturas, armas, coletes, **tudo foi** conferido.”
- Núcleos sinônimos ou em gradação admitem singular ou plural: “O medo e o pavor **tomou** (ou **tomaram**) conta da rua.”
"""
S[3]="""## 3. Casos especiais do verbo

**Coletivo e expressão partitiva.** Coletivo no singular leva o verbo ao singular: “A multidão **invadiu** a praça.” Expressões como “a maioria de”, “grande parte de”, “metade de” seguidas de plural admitem singular ou plural: “A maioria dos guardas **votou** (ou **votaram**) pela nova escala.”

**Porcentagem.** Sem termo depois, o verbo concorda com o número: “30% **faltaram**”; “1% **faltou**”. Com termo depois, pode concordar com ele: “30% da tropa **faltou** (ou **faltaram**)”.

**Mais de um.** O verbo fica no singular: “**Mais de um** guarda **faltou**.”

**Um dos que.** O verbo vai, de preferência, para o plural: “Ele é um dos que mais **trabalham**.”

**Pronome relativo.** Com “que”, o verbo concorda com o antecedente: “Fui **eu que fiz** o registro.” Com “quem”, vai para a 3ª pessoa do singular ou concorda com o antecedente: “Fui eu **quem fez** (ou **quem fiz**).”

**Nome próprio no plural.** Com artigo no plural, o verbo vai ao plural: “**Os Estados Unidos são** um país grande.” Sem artigo, singular: “**Campinas cresceu** nas últimas décadas.”

**Horas com dar, bater e soar.** O verbo concorda com o número de horas: “**Deram** três horas.” Se o sujeito for o relógio, concorda com ele: “O relógio **deu** três horas.”

**Haver, fazer e o “se”.** Como no posto 7: haver de existir e fazer de tempo ficam no singular (houve ocorrências; faz dois anos); o “se” apassivador concorda (vendem-se casas); o de indeterminação, não (precisa-se de guardas).
"""
S[4]="""## 4. O verbo ser

O verbo **ser** é o único que costuma concordar com o predicativo, não com o sujeito. As situações cobradas são estas:

1. **Horas, datas e distâncias:** concorda com o número. “**São** duas horas”; “**É** uma hora”; “Hoje **são** 12 de novembro” (ou “hoje **é** dia 12”); “Daqui à praça **são** dois quilômetros”.
2. **Pessoa:** quando um dos termos é pronome pessoal, o verbo concorda com ele. “O responsável **sou** eu.”
3. **Tudo, isto, isso, aquilo + plural:** o verbo prefere o plural. “Tudo **são** flores”; “Isso **são** problemas da escala.”
4. **Quantidade com pouco, muito, suficiente:** o verbo fica no singular. “Dez reais **é** pouco”; “Dois agentes **é** muito para essa praça.”
"""
S[5]="""## 5. A regra geral da concordância nominal

Artigo, adjetivo, pronome e numeral concordam em **gênero** e **número** com o substantivo a que se referem: “as **novas** viaturas”, “os **dois** guardas **escalados**”.

Quando um adjetivo se refere a **dois ou mais substantivos**, a posição decide:

- **Depois** dos substantivos: concorda com o mais próximo ou vai para o plural, com o masculino prevalecendo. “Guardas e agentes **treinados**”; “camisa e calça **novas**” (ou “nova”).
- **Antes** dos substantivos: concorda com o mais próximo. “**Nova** camisa e calça”; “**Novos** coletes e luvas”.
"""
S[6]="""## 6. Casos especiais do nome

**É proibido, é necessário, é bom.** Sem artigo ou pronome antes do substantivo, a expressão fica invariável; com eles, concorda:

1. **É proibido** entrada de pessoas estranhas. / **É proibida a** entrada de pessoas estranhas.
2. **É necessário** paciência. / **É necessária a** paciência.

**Anexo, incluso, obrigado, mesmo, próprio, quite** concordam com o termo a que se referem: “Seguem **anexas** as fotos”; “**Obrigada**, disse a vítima”; “Estamos **quites**”. A locução **em anexo** não varia: “Seguem **em anexo** as fotos.”

**Meio, bastante, só.** Como adjetivo ou numeral, variam; como advérbio, não:

1. Comeu **meia** pizza. / A vítima estava **meio** assustada.
2. Havia **bastantes** agentes. / Os agentes estavam **bastante** atentos.
3. Elas ficaram **sós** (sozinhas). / **Só** elas ficaram (somente).

**Menos** não varia: “**menos** pessoas”; a forma “menas” não existe.

**Possível** concorda com o artigo da expressão: “**o** mais rápido **possível**”; “**as** respostas mais rápidas **possíveis**”.

**Cores.** Adjetivo composto de cor varia só no último elemento (“olhos verde-**claros**”), mas cor indicada por substantivo não varia (“uniformes **azul-marinho**”, “camisas **cinza**”, “cones **laranja**”).

[[NOTA: “Junto” varia como adjetivo (“elas chegaram **juntas**”), mas “junto a” e “junto de” não variam (“ficaram **junto ao** portão”).]]
"""
S[8]="""## 8. Na rotina do guarda

- **Relatório com sujeito no fim:** “**Foram apreendidos** dois celulares e uma faca.” Ache o sujeito antes de escrever o verbo.
- **Escala:** “**Faltam** três agentes no turno da noite”, não “falta”.
- **Ofício com anexos:** “Seguem **anexos** os documentos” ou “Seguem **em anexo** os documentos”.
- **Placa e aviso:** “**É proibida a** entrada” ou “**É proibido** entrada”, nunca “é proibida entrada”.
- **Uniforme:** “uniformes **azul-marinho**”, com a cor invariável.
"""
S[9]="""## 9. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Sujeito depois do verbo | pergunte “quem?” ao verbo: chegaram os reforços |
| Verbo concordando com a palavra mais próxima | concorde com o núcleo: a lista de nomes foi entregue |
| “Houveram”, “fazem dois anos” | haver de existir e fazer de tempo ficam no singular |
| “Vende-se casas” | se apassivador concorda: vendem-se casas |
| “Mais de um guardas faltaram” | mais de um leva o verbo ao singular |
| “É proibida entrada” | sem artigo, invariável: é proibido entrada |
| “Segue anexo as fotos” | seguem anexas as fotos, ou em anexo |
| “Meia cansada”, “menas pessoas” | meio advérbio não varia; menos não varia |
| “Uniformes azuis-marinhos” | cor por substantivo não varia: azul-marinho |
| “São uma hora” | é uma hora; são duas horas |
"""
S[10]="""## 10. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Regra geral verbal | verbo concorda com o núcleo do sujeito |
| Sujeito posposto | pergunte “quem?”: faltam dois agentes |
| Sujeito composto | antes, plural; depois, plural ou o mais próximo |
| Pessoas diferentes | 1ª vence: eu e você iremos |
| Ou, tudo, ninguém | ou excludente e resumo levam ao singular |
| Partitivo e porcentagem | singular ou plural; sem termo, com o número |
| Mais de um, um dos que | singular; plural preferido |
| Que e quem | que concorda com o antecedente; quem, 3ª pessoa ou antecedente |
| Verbo ser | horas, datas, pessoa e “tudo são” |
| Regra geral nominal | adjetivo, artigo e numeral concordam com o substantivo |
| Adjetivo e dois substantivos | depois: plural ou o mais próximo; antes: o mais próximo |
| É proibido | sem artigo, invariável; com artigo, concorda |
| Anexo, obrigado, quite | variam; em anexo não |
| Meio, bastante, só, menos | advérbio não varia; menos nunca varia |
| Cores | azul-marinho, cinza, laranja não variam |
"""
QR=[("Questão 1","Assinale a frase de acordo com a norma-padrão.",["Faltam dois agentes no turno da noite.","Falta dois agentes no turno da noite.","Houveram dois chamados no turno.","Fazem dois anos que a praça foi reformada.","Vende-se motos apreendidas."],2,"“Dois agentes” é o sujeito de “faltar”, posposto: faltam. Nas demais: houve, faz, vendem-se."),
("Questão 2","Assinale a alternativa em que a concordância nominal está correta.",["Seguem anexas as fotos da ocorrência.","Seguem anexo as fotos da ocorrência.","É proibida entrada de pessoas estranhas.","A vítima estava meia assustada.","Havia menas pessoas na praça."],0,"Anexo concorda com “fotos”. Nas demais: é proibido entrada (ou é proibida a entrada), meio assustada, menos pessoas."),
("Questão 3","Assinale a frase correta quanto à concordância do verbo ser.",["É uma hora da tarde.","São uma hora da tarde.","É duas horas da tarde.","Eram uma hora quando chegaram.","Daqui à praça é dois quilômetros."],3,"Com horas, ser concorda com o número: é uma hora; são duas horas; são dois quilômetros."),
("Questão 4","Na frase “A lista com os nomes dos suspeitos ____ entregue ao delegado”, a lacuna é preenchida por",["foi","foram","foi-se","foram-se","eram"],1,"O núcleo do sujeito é “lista”: a lista foi entregue.")]
QRF=qr_md(QR,7)
Q=[]
def q(n,e,a,c,tx=None): Q.append((n,e,a,c,tx))
# FÁCEIS
q(1,"Assinale a frase em que o verbo concorda corretamente com o sujeito.",["Chegaram os reforços da Guarda.","Chegou os reforços da Guarda.","Chegou-se os reforços da Guarda.","Chegaram o reforço da Guarda.","Chegam-se os reforços da Guarda."],"O sujeito “os reforços” está depois do verbo e pede plural.")
q(1,"Complete: “____ dois agentes na escala desta noite.”",["Faltam","Falta","Faltou","Faltava","Falte"],"Dois agentes faltam: sujeito plural posposto.")
q(1,"Assinale a frase correta.",["O guarda e o motorista discutiram.","O guarda e o motorista discutiu.","O guarda e o motorista discutiu-se.","O guarda e o motorista discutem-se ontem.","O guarda e o motorista discutira."],"Sujeito composto antes do verbo leva o verbo ao plural.")
q(1,"Complete: “Eu e você ____ à reunião amanhã.”",["iremos","irão","irei","irá","ireis"],"Com a 1ª pessoa entre os núcleos, o verbo vai para a 1ª do plural (nós).")
q(1,"Assinale a frase correta.",["Houve três ocorrências na madrugada.","Houveram três ocorrências na madrugada.","Haviam três ocorrências na madrugada.","Houveram-se três ocorrências.","Hão três ocorrências."],"Haver no sentido de existir é impessoal: singular.")
q(1,"Assinale a frase correta.",["Faz dois anos que entrei na Guarda.","Fazem dois anos que entrei na Guarda.","Fizeram dois anos que entrei na Guarda.","Fazem-se dois anos que entrei na Guarda.","Faziam dois anos que entrei na Guarda."],"Fazer de tempo decorrido é impessoal.")
q(1,"Assinale a frase correta.",["Vendem-se motos apreendidas.","Vende-se motos apreendidas.","Vendem-se moto apreendidas.","Vende-se as motos apreendidas.","Vendeu-se motos apreendidas."],"Se apassivador: o verbo concorda com o sujeito “motos”.")
q(1,"Assinale a frase correta.",["A multidão invadiu a praça.","A multidão invadiram a praça.","A multidão invadiu-se a praça.","As multidão invadiu a praça.","A multidão invadimos a praça."],"Coletivo no singular leva o verbo ao singular.")
q(1,"Complete: “Mais de um guarda ____ ao treinamento.”",["faltou","faltaram","faltamos","faltaste","faltáramos"],"Mais de um leva o verbo ao singular.")
q(1,"Complete: “Fui eu que ____ o registro.”",["fiz","fez","fizeram","fizemos","fazia-se"],"Com “que”, o verbo concorda com o antecedente “eu”.")
q(1,"Assinale a frase correta.",["São duas horas da tarde.","É duas horas da tarde.","São uma hora da tarde.","Era duas horas da tarde.","Será duas horas da tarde."],"Com horas, ser concorda com o número: duas horas → são.")
q(1,"Assinale a frase correta.",["Seguem anexas as fotos.","Seguem anexo as fotos.","Segue anexas as fotos.","Seguem anexos as fotos.","Segue anexa as fotos."],"Anexo concorda com “fotos” (feminino plural), e o verbo também.")
q(1,"Assinale a frase correta.",["A vítima estava meio assustada.","A vítima estava meia assustada.","A vítima estava meias assustada.","As vítimas estavam meias assustadas.","A vítima estava meio assustadas."],"Meio = um pouco é advérbio e não varia.")
q(1,"Assinale a frase correta.",["Havia menos pessoas na praça.","Havia menas pessoas na praça.","Haviam menos pessoas na praça.","Haviam menas pessoas na praça.","Havia menos pessoa na praças."],"Menos não varia, e haver de existir fica no singular.")
q(1,"Assinale a frase correta.",["Os guardas usam uniformes azul-marinho.","Os guardas usam uniformes azuis-marinhos.","Os guardas usam uniformes azuis-marinho.","Os guardas usam uniformes azul-marinhos.","Os guardas usam uniforme azuis-marinho."],"Cor indicada por substantivo (marinho) não varia: azul-marinho.")
q(1,"Assinale a frase correta.",["É proibido entrada de pessoas estranhas.","É proibida entrada de pessoas estranhas.","É proibidos entrada de pessoas estranhas.","São proibido entrada de pessoas estranhas.","É proibida entradas de pessoas estranhas."],"Sem artigo antes de “entrada”, a expressão fica invariável. Com artigo: é proibida a entrada.")
q(1,"Complete: “A agente agradeceu: — Muito ____.”",["obrigada","obrigado","obrigados","obrigadas","obrigado-a"],"Obrigado concorda com quem agradece: a agente diz obrigada.")
q(1,"Assinale a frase correta.",["Os agentes estavam bastante atentos.","Os agentes estavam bastantes atentos.","Havia bastante agentes atentos.","Os agente estavam bastante atentos.","Os agentes estava bastante atentos."],"Bastante modificando o adjetivo “atentos” é advérbio e não varia.")
q(1,"Complete: “O responsável pelo plantão ____ eu.”",["sou","é","era","foi","seria"],"Quando um dos termos é pronome pessoal, o verbo ser concorda com ele.")
q(1,"No primeiro parágrafo, a forma “foram registrados” concorda com",["“furtos”.","“bairro”.","“semana”.","“Guarda”.","“moradores”."],"O sujeito da passiva é “três furtos”, que pede plural.","tn")
# MÉDIAS
q(2,"Assinale a frase correta.",["A lista com os nomes dos suspeitos foi entregue ao delegado.","A lista com os nomes dos suspeitos foram entregues ao delegado.","A lista com os nomes dos suspeitos foram entregue ao delegado.","A lista com os nomes dos suspeitos foi entregues ao delegado.","A lista com os nome dos suspeitos foram entregue ao delegado."],"O núcleo do sujeito é “lista”, singular.")
q(2,"Assinale a frase em que a concordância admite as duas formas indicadas.",["Chegou o guarda e o motorista. / Chegaram o guarda e o motorista.","O guarda e o motorista chegou. / O guarda e o motorista chegaram.","Houve ocorrências. / Houveram ocorrências.","Faz dois anos. / Fazem dois anos.","Mais de um faltou. / Mais de um faltaram."],"Sujeito composto posposto: plural ou concordância com o núcleo mais próximo.")
q(2,"Assinale a frase em que o verbo no singular é o adequado, porque “ou” indica exclusão.",["O guarda ou o fiscal assinará o termo.","Furto ou roubo exigem registro.","O calor ou o frio afetam a ronda.","A chuva ou o vento derrubaram a placa.","O prefeito ou o vice estarão presentes juntos."],"Só um dos dois assinará: o “ou” exclui.")
q(2,"Assinale a frase correta.",["Viaturas, armas, coletes, tudo foi conferido.","Viaturas, armas, coletes, tudo foram conferidos.","Viaturas, armas, coletes, tudo foram conferido.","Viaturas, armas, coletes, tudo foi conferidos.","Viaturas, armas, coletes, tudo eram conferidos."],"O resumo “tudo” leva o verbo ao singular.")
q(2,"Assinale a frase em que a concordância está correta.",["A maioria dos guardas votou pela nova escala.","A maioria dos guardas votamos pela nova escala.","A maioria dos guardas votastes pela nova escala.","A maioria dos guarda votaram pela nova escala.","As maioria dos guardas votou pela nova escala."],"Com “a maioria de” + plural, o verbo pode ficar no singular (ou ir ao plural, votaram).")
q(2,"Complete: “Ele é um dos agentes que mais ____ na região.”",["patrulham","patrulhamos","patrulhais","patrulhas","patrulhe"],"Com “um dos que”, a preferência é pelo plural.")
q(2,"Assinale a frase correta.",["Os Estados Unidos são um país grande.","Os Estados Unidos é um país grande.","Os Estados Unidos foi um país grande.","Os Estados Unidos sou um país grande.","Os Estados Unidos era um país grande."],"Nome próprio no plural com artigo plural leva o verbo ao plural.")
q(2,"Assinale a frase correta.",["Deram três horas no relógio da praça.","Deu três horas no relógio da praça.","Bateu três horas no relógio da praça.","Soou três horas no relógio da praça.","Dava três horas no relógio da praça."],"Sem o relógio como sujeito, dar, bater e soar concordam com o número de horas.")
q(2,"Assinale a frase correta.",["O relógio da praça deu três horas.","O relógio da praça deram três horas.","O relógio da praça bateram três horas.","O relógio da praça soaram três horas.","O relógio da praça davam três horas."],"Com “o relógio” como sujeito, o verbo concorda com ele.")
q(2,"Assinale a frase correta.",["Dez reais é pouco para o lanche do plantão.","Dez reais são pouco para o lanche do plantão.","Dez reais são poucos para o lanche do plantão.","Dez reais é poucos para o lanche do plantão.","Dez reais foram pouca para o lanche do plantão."],"Com pouco, muito e suficiente indicando quantidade, o verbo ser fica no singular.")
q(2,"Assinale a frase correta.",["Guardas e agentes treinados atenderam a ocorrência.","Guardas e agentes treinadas atenderam a ocorrência.","Guardas e agentes treinado atenderam a ocorrência.","Guardas e agentes treinada atenderam a ocorrência.","Guardas e agente treinados atendeu a ocorrência."],"Adjetivo depois de dois substantivos masculinos vai para o masculino plural.")
q(2,"Assinale a frase correta.",["É proibida a entrada de pessoas estranhas.","É proibido a entrada de pessoas estranhas.","É proibidas a entrada de pessoas estranhas.","É proibido as entradas de pessoas estranhas.","É proibida as entrada de pessoas estranhas."],"Com artigo antes do substantivo, a expressão concorda: é proibida a entrada.")
q(2,"Assinale a frase correta.",["Seguem em anexo os documentos.","Seguem em anexos os documentos.","Seguem em anexas os documentos.","Segue em anexos os documentos.","Seguem em anexa os documentos."],"A locução “em anexo” não varia.")
q(2,"Assinale a frase em que “só” é adjetivo e, por isso, varia.",["As vítimas ficaram sós na praça.","Só as vítimas ficaram na praça.","As vítimas só ficaram na praça.","Só depois as vítimas ficaram na praça.","As vítimas ficaram a sós na praça."],"Sós = sozinhas (adjetivo). Nas demais, só = somente (advérbio) ou a locução “a sós”, invariável.")
q(2,"Assinale a frase correta.",["Os relatórios foram feitos o mais rápido possível.","Os relatórios foram feitos o mais rápido possíveis.","Os relatórios foram feitos os mais rápido possível.","Os relatórios foram feitos o mais rápidos possíveis.","Os relatórios foram feitos o mais rápido possívels."],"“Possível” concorda com o artigo da expressão: o mais... possível.")
q(2,"Assinale a frase correta.",["Os agentes ficaram junto ao portão.","Os agentes ficaram juntos ao portão.","Os agentes ficaram junta ao portão.","As agentes ficaram juntas ao portão.","Os agentes ficaram juntos à portão."],"A locução “junto a” não varia.")
q(2,"Assinale a frase correta.",["Estamos quites com o almoxarifado.","Estamos quite com o almoxarifado.","Estamos quitos com o almoxarifado.","Estamos quitas com o almoxarifado.","Estamos quites com os almoxarifado."],"Quite concorda com o sujeito: estamos quites.")
q(2,"Assinale a frase correta.",["Comeu meia pizza antes do plantão.","Comeu meio pizza antes do plantão.","Comeu meia-pizza antes do plantão.","Comeu meio-pizza antes do plantão.","Comeu meias pizza antes do plantão."],"Meio como numeral (metade) concorda: meia pizza.")
q(2,"No segundo parágrafo, a forma “Faltam” concorda com",["“dois agentes”.","“a escala”.","“a noite”.","“o comando”.","“a praça”."],"O sujeito posposto “dois agentes” pede plural.","tn")
q(2,"No último parágrafo, “Seguem anexas” concorda com",["“as imagens das câmeras”.","“o relatório”.","“a Guarda”.","“o delegado”.","“o comandante”."],"O sujeito posposto é “as imagens das câmeras”, feminino plural.","tn")
# DIFÍCEIS
q(3,"Assinale a alternativa em que a concordância verbal está INCORRETA.",["Mais de um guarda faltaram ao treinamento.","Faltam dois agentes na escala.","Chegaram os reforços da Guarda.","Fui eu que fiz o registro.","A multidão invadiu a praça."],"Mais de um leva o verbo ao singular: mais de um guarda faltou.")
q(3,"Assinale a alternativa em que a concordância nominal está INCORRETA.",["É proibida entrada de pessoas estranhas.","É proibido entrada de pessoas estranhas.","É proibida a entrada de pessoas estranhas.","Seguem anexas as fotos.","Os agentes estavam bastante atentos."],"Sem artigo, a expressão fica invariável: é proibido entrada.")
q(3,"Complete as lacunas: “____ três chamados na madrugada; ____ dois anos que a praça não registrava tantos.”",["Houve / faz","Houveram / fazem","Houve / fazem","Houveram / faz","Haviam / fazem"],"Haver de existir e fazer de tempo decorrido são impessoais.")
q(3,"Assinale a alternativa em que o verbo deve ir obrigatoriamente para o plural.",["O guarda e o fiscal ____ o termo juntos. (assinar)","O guarda ou o fiscal ____ o termo. (assinar)","____ o guarda e o fiscal. (chegar)","Mais de um fiscal ____. (faltar)","Viaturas, armas, tudo ____ conferido. (ser)"],"Sujeito composto antes do verbo leva ao plural: assinaram. Nas demais, o singular é possível ou obrigatório.")
q(3,"Assinale a frase correta.",["30% da tropa faltaram ao treinamento.","30% da tropa faltou-se ao treinamento.","30% faltou ao treinamento.","1% faltaram ao treinamento.","1% dos agentes faltamos ao treinamento."],"Com termo depois da porcentagem, o verbo pode concordar com o número (faltaram) ou com o termo (faltou). Sem termo, concorda com o número: 30% faltaram; 1% faltou.")
q(3,"Assinale a frase correta quanto à concordância do verbo ser.",["Hoje são 12 de novembro.","Eram uma hora quando chegaram.","Daqui à praça é dois quilômetros.","É duas horas da tarde.","São uma hora e meia."],"Com datas sem a palavra “dia”, o verbo concorda com o número: são 12. Com “dia”: hoje é dia 12.")
q(3,"Assinale a frase correta.",["Isso são problemas da escala, não do efetivo.","Isso é problemas da escala, não do efetivo.","Isso foram problema da escala, não do efetivo.","Isso é problema das escalas, não dos efetivo.","Isso são problema da escala, não do efetivo."],"Com isso, isto, aquilo ou tudo + predicativo plural, o verbo ser prefere o plural.")
q(3,"Assinale a frase em que o adjetivo concorda corretamente.",["Novos coletes e luvas chegaram ao almoxarifado.","Novas coletes e luvas chegaram ao almoxarifado.","Novo coletes e luvas chegaram ao almoxarifado.","Nova coletes e luvas chegaram ao almoxarifado.","Novos coletes e luva chegou ao almoxarifado."],"Adjetivo antes de dois substantivos concorda com o mais próximo: novos coletes.")
q(3,"Assinale a alternativa em que a cor está corretamente flexionada.",["Os agentes tinham olhos verde-claros.","Os agentes usavam coletes laranjas.","Os cones cinzas foram trocados.","As fardas azuis-marinho chegaram.","Os agentes tinham olhos verdes-claros."],"Adjetivo composto de cor varia só no último elemento: verde-claros. Cor por substantivo não varia: laranja, cinza, azul-marinho.")
q(3,"Assinale a frase correta.",["Fui eu quem fez o registro.","Fui eu quem fizeram o registro.","Fui eu que fez o registro.","Foi eu que fiz o registro.","Fomos eu quem fiz o registro."],"Com “quem”, o verbo vai para a 3ª pessoa do singular (ou concorda com o antecedente: quem fiz). Com “que”, concorda com “eu”: que fiz.")
q(3,"Assinale a alternativa em que as duas concordâncias estão corretas.",["Chegaram os agentes e o delegado. / Chegou o delegado e os agentes.","Chegou os agentes e o delegado. / Chegaram o delegado e os agentes.","O delegado e os agentes chegou. / Os agentes e o delegado chegou.","Houveram agentes. / Fazem dois anos.","É proibida entrada. / Segue anexo as fotos."],"Com sujeito composto posposto, o verbo pode ir ao plural ou concordar com o núcleo mais próximo (o delegado → chegou).")
q(3,"Assinale a frase em que a concordância está correta.",["Precisa-se de agentes com experiência.","Precisam-se de agentes com experiência.","Precisam-se agentes de experiência.","Precisa-se de agentes com experiências e precisam-se de motoristas.","Precisaram-se de agentes."],"Verbo transitivo indireto com se: índice de indeterminação, verbo no singular.")
q(3,"Assinale a frase em que a concordância está correta.",["Alugam-se salas comerciais no centro.","Aluga-se salas comerciais no centro.","Alugam-se sala comerciais no centro.","Aluga-se as salas comerciais no centro.","Alugou-se salas comerciais no centro."],"Verbo transitivo direto + se: o termo seguinte é o sujeito e o verbo concorda com ele.")
q(3,"No primeiro parágrafo, se “três furtos” fosse trocado por “um furto”, a frase correta seria",["Na última semana, foi registrado um furto em residências do bairro.","Na última semana, foram registrados um furto em residências do bairro.","Na última semana, foram registrado um furto em residências do bairro.","Na última semana, foi registrados um furto em residências do bairro.","Na última semana, registraram-se um furto em residências do bairro."],"O verbo e o particípio acompanham o novo sujeito, singular masculino.","tn")
q(3,"No segundo parágrafo, se “a maioria dos moradores” for mantido, a forma verbal que também estaria correta no lugar de “aprovou” é",["aprovaram","aprovamos","aprovastes","aprovou-se","aprovarão-se"],"Com “a maioria de” + plural, o verbo admite singular ou plural.","tn")
q(3,"No último parágrafo do texto, “É necessário cautela” está correto porque",["o substantivo “cautela” aparece sem artigo, e a expressão fica invariável.","“cautela” é masculino.","o verbo ser concorda com o predicativo.","a frase está na voz passiva.","“necessário” concorda com “Guarda”."],"Sem artigo ou pronome antes do substantivo, “é necessário” não varia. Com artigo: é necessária a cautela.","tn")
q(3,"Assinale a alternativa que completa corretamente: “Os agentes ____ cansados e ____ pessoas ficaram na praça depois da meia-noite.”",["estavam meio / menos","estavam meios / menas","estava meio / menos","estavam meio / menas","estavam meios / menos"],"Meio (advérbio) e menos não variam; o verbo concorda com “os agentes”.")
q(3,"Assinale a alternativa em que a palavra destacada deveria variar e não variou.",["Seguem anexo as declarações das testemunhas.","A agente ficou meio confusa com a ordem.","Os guardas falaram alto com o motorista.","As motos custaram caro.","Os cones laranja foram recolhidos."],"Anexo é adjetivo e concorda: seguem anexas as declarações. Nas demais, as palavras são invariáveis.")
q(3,"Assinale a afirmação INCORRETA sobre concordância.",["O verbo sempre concorda com a palavra mais próxima dele.","O verbo concorda com o núcleo do sujeito.","Haver no sentido de existir é impessoal.","O verbo ser pode concordar com o predicativo.","“Menos” é palavra invariável."],"O verbo concorda com o núcleo do sujeito, que pode estar longe dele.")
q(3,"Assinale a alternativa em que a concordância segue a norma-padrão em todos os pontos.",["Devem existir soluções, mas deve haver também cautela.","Devem haver soluções, mas deve existir também cautela.","Deve existir soluções, mas devem haver também cautelas.","Devem haver soluções, mas devem existir também cautela.","Deve haver soluções, mas devem existir também cautela."],"Existir concorda (devem existir soluções); haver de existir é impessoal (deve haver cautela).")
assert len(Q)==60
tn="<strong>Bairro tem aumento de furtos em residências</strong><br><br>Na última semana, foram registrados três furtos em residências do bairro, todos no período da tarde. Segundo a Guarda Municipal, os autores aproveitaram horários em que os moradores estavam no trabalho.<br><br>Faltam dois agentes na escala da região, informou o comando, que prometeu reforço até o fim do mês. Em reunião com a corporação, a maioria dos moradores aprovou a criação de uma rede de vizinhos por aplicativo.<br><br>O comandante pediu que qualquer movimentação estranha seja comunicada pelo telefone 153. Seguem anexas ao relatório entregue ao delegado as imagens das câmeras da rua. É necessário cautela antes de divulgar fotos de suspeitos nas redes."
texts={"tn":tn}
code,svg=mapa("A concordância segue o núcleo, mesmo quando ele se esconde",[
 ("geral","Regra geral do verbo",["verbo concorda com o núcleo","sujeito no fim: pergunte quem","sujeito longe: ache o núcleo"],"seções 1 e 2"),
 ("especial","Casos especiais do verbo",["coletivo, porcentagem","mais de um, um dos que","haver, fazer e o se"],"seção 3"),
 ("ser","O verbo ser",["horas, datas, distâncias","pronome pessoal manda","tudo são; dez reais é pouco"],"seção 4"),
 ("nominal","Regra geral do nome",["adjetivo com o substantivo","depois: plural ou o próximo","antes: o mais próximo"],"seção 5"),
 ("nomesp","Casos especiais do nome",["é proibido entrada","anexo, obrigado, quite","meio, bastante, só, menos"],"seção 6"),
 ("cores","Cores",["verde-claros (varia o fim)","azul-marinho, cinza","laranja: não variam"],"seção 6")],
 "Na prova: o sujeito vem depois do verbo ou longe dele, e a palavra parece variar sem variar")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,'QR',8,9,10],QR,7,svg,"Dos seis grupos, os três de cima tratam do verbo e os três de baixo, do nome; os dois lados dependem de achar o termo certo.","Fontes: Edital 02/2026, Anexo I. Referências de base: Bechara, <em>Moderna Gramática Portuguesa</em>; Cunha e Cintra, <em>Nova Gramática do Português Contemporâneo</em>; ABL, VOLP. Exemplos criados para a aula.")
import pickle
revisao("pt-9",'Concordância verbal e nominal',Q,{'tn':tn},pendencias=["Aula escrita antes do padrão de revisão: não há registro do que foi conferido na fonte. Conferir exemplos e regras contra Bechara e Cunha e Cintra."])
gravar("pt-9",aula_html,banco("pt-9",Q),texts)
print(len(aula_html)); print(code[:200])
