import sys,pickle; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','gerador')); from aulas import *
LEAD="Crase é a fusão de duas vogais “a”, marcada pelo acento grave. Ela só existe quando duas coisas acontecem ao mesmo tempo: uma palavra pede a preposição “a” e a palavra seguinte aceita o artigo “a”. Quase toda questão de crase se resolve com dois testes rápidos."
S={}
S[1]="""## 1. O que é crase e os dois testes

Crase é a fusão da **preposição “a”** com:

1. o **artigo “a” ou “as”**: chegou **à** delegacia (a + a delegacia);
2. o “a” inicial de **aquele, aquela, aquilo**: refiro-me **àquele** guarda;
3. o pronome **“a” ou “as”** equivalente a “aquela(s)”: esta ocorrência é igual **à** de ontem (à = àquela).

O primeiro teste é **trocar a palavra feminina por uma masculina**. Se aparecer “ao”, há crase:

1. Fui **à** praça → Fui **ao** parque. (crase)
2. Fui **a** pé → nem precisa trocar: “pé” já é masculino. (sem crase)
3. Comecei **a** correr → Comecei **a** andar. (sem crase: não há artigo antes de verbo)

O segundo teste serve para **nomes de lugar**: troque “ir a” por “voltar de”. Se aparecer “da”, há crase; se aparecer só “de”, não há:

1. Vou **a** Campinas → volto **de** Campinas. (sem crase)
2. Vou **à** Bahia → volto **da** Bahia. (crase)
"""
S[2]="""## 2. Crase obrigatória

- **Termo que pede “a” + palavra feminina com artigo:** “Chegou **à** delegacia”; “Obedeça **à** sinalização”; “Procedeu **à** vistoria”; “Prefiro a ronda **à** base”.
- **Horas determinadas:** “**às** 22h”; “**à** meia-noite”; “**à** uma hora”; “das 8h **às** 18h”.
- **Locuções femininas:** **à** noite, **à** tarde, **às** pressas, **às** vezes, **à** esquerda, **à** direita, **à** vista, **à** venda, **à** disposição, **à** espera de, **à** procura de, **à** frente de, **à** medida que.
- **Aquele, aquela, aquilo** depois de termo que pede “a”: “Refiro-me **àquele** relatório”; “Assisti **àquilo** de perto”.
- **A qual, as quais** quando o verbo pede “a”: “A escala **à qual** me refiro foi alterada.”
- **“À moda de”**, mesmo escondida, inclusive antes de masculino: “bife **à** parmegiana”; “dribla **à** Garrincha”.
"""
S[3]="""## 3. Crase proibida

| Evite | Use |
| --- | --- |
| Os agentes foram à pé | Os agentes foram **a** pé |
| Começou à chover | Começou **a** chover |
| Entreguei o crachá à ela | Entreguei o crachá **a** ela |
| Dirijo-me à Vossa Excelência | Dirijo-me **a** Vossa Excelência |
| Chegamos à uma conclusão | Chegamos **a** uma conclusão |
| Ficou cara à cara com o suspeito | Ficou cara **a** cara com o suspeito |
| Vou à Campinas na sexta | Vou **a** Campinas na sexta |
| Fui à reuniões a semana toda | Fui **a** reuniões a semana toda |
| A operação vai de 10 à 30 de novembro | A operação vai de 10 **a** 30 de novembro |

As razões são sempre as mesmas: palavra masculina, verbo, pronome que não aceita artigo (pessoal, de tratamento, indefinido, “esta” e “essa”), artigo indefinido “uma” (que não seja hora), palavras repetidas, cidade sem artigo, “a” no singular antes de plural e numeral sem artigo.

Dois casos com determinante mudam a regra: “Voltou **a** casa” (o lar, sem determinante), mas “Voltou **à** casa dos pais”; “Vou **a** Campinas”, mas “Vou **à** Campinas da minha infância”.

[[NOTA: “Senhora”, “senhorita” e “dona” aceitam artigo: “Entreguei o termo **à** senhora”. Os demais pronomes de tratamento, não: “a Vossa Senhoria”.]]
"""
S[4]="""## 4. Crase facultativa

Em três situações, a crase pode aparecer ou não, porque o artigo é opcional:

1. Antes de **pronome possessivo feminino no singular**: “Refiro-me **a** sua escala” ou “Refiro-me **à** sua escala”.
2. Antes de **nome próprio feminino de pessoa**: “Entreguei o relatório **a** Mariana” ou “**à** Mariana”.
3. Depois de **até**: “Foi até **a** delegacia” ou “até **à** delegacia”.
"""
S[5]="""## 5. Há ou a?

A confusão entre “há” e “a” aparece em quase toda prova com crase.

1. **Há** é o verbo haver e indica **tempo passado**: “**Há** dez anos, ele entrou na Guarda.” Dá para trocar por “faz”.
2. **A** é preposição e indica **tempo futuro** ou **distância**: “Daqui **a** dois dias, a escala muda”; “O posto fica **a** dois quilômetros”.

Nunca se escreve “daqui há”: o “daqui” já aponta para o futuro.
"""
S[7]="""## 7. Na rotina do guarda

- **Relatório:** “A equipe chegou **à** delegacia **às** 23h e entregou o conduzido **à** autoridade de plantão.”
- **Escala:** “Plantão das 19h **às** 7h”; “operação de 10 **a** 30 de novembro”, sem crase entre numerais.
- **Deslocamento:** “Seguiram **a** pé até **a** praça” (ou “até **à** praça”).
- **Ofício:** “Encaminho **a** Vossa Senhoria o relatório” e “Fico **à** disposição”.
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Crase antes de verbo | nunca: começou a chover |
| Crase antes de masculino | só com “à moda de”: a pé, mas bife à parmegiana |
| Crase antes de “ela”, “Vossa Excelência” | pessoais e de tratamento não aceitam artigo |
| “À uma conclusão” | artigo indefinido não leva crase; só “à uma hora” |
| “Vou à Campinas” | volto de Campinas: sem crase |
| “Fui à reuniões” | “a” no singular antes de plural é só preposição |
| “De 10 à 30” | numeral sem artigo: de 10 a 30 |
| “Daqui há dois dias” | futuro: daqui a dois dias |
| “A escala à que me refiro” | antes do relativo “que”, não há artigo: a que me refiro |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| O que é | preposição a + artigo a; ou a + aquele, aquela, aquilo |
| Teste do masculino | se virar “ao”, há crase |
| Teste do lugar | volto da: crase; volto de: sem crase |
| Obrigatória | pedido de “a” + feminino com artigo; horas; locuções femininas |
| À moda de | bife à parmegiana; dribla à Garrincha |
| Proibida | masculino, verbo, pronome sem artigo, “uma”, repetição, plural sem artigo |
| Casa e cidade | sem determinante, sem crase; com determinante, crase |
| Senhora | aceita artigo: à senhora |
| Facultativa | possessivo feminino singular, nome de mulher, depois de até |
| Há ou a | há = passado (faz); a = futuro ou distância |
"""
QR=[("Questão 1","Assinale a frase em que o acento grave está correto.",["A equipe chegou à delegacia às 23h.","O tempo começou à fechar.","Os agentes saíram à pé.","Entregou o termo à ele.","Chegou à uma conclusão rápida."],3,"Chegar pede a, e delegacia aceita artigo; às 23h é hora determinada. Nas demais: verbo, masculino, pronome pessoal e artigo indefinido."),
("Questão 2","Assinale a frase em que a crase é facultativa.",["Foi até à praça.","Foi à praça.","Chegou às 10h.","Saiu às pressas.","Refiro-me àquela praça."],1,"Depois de “até”, o artigo é opcional. Nas demais, a crase é obrigatória."),
("Questão 3","Complete: “____ três dias, o posto fechou; daqui ____ dois dias, reabrirá.”",["Há / a","A / há","À / há","Há / à","A / a"],0,"Passado: há (faz três dias). Futuro: daqui a."),
("Questão 4","Assinale a frase de acordo com a norma-padrão.",["Vou a Campinas e depois à Bahia.","Vou à Campinas e depois à Bahia.","Vou a Campinas e depois a Bahia.","Vou à Campinas e depois a Bahia.","Vou há Campinas e depois à Bahia."],4,"Volto de Campinas (sem crase); volto da Bahia (com crase).")]
QRF=qr_md(QR,6)
Q=[]
def q(n,e,a,c,tx=None): Q.append((n,e,a,c,tx))
q(1,"Assinale a frase em que o acento grave está correto.",["A viatura chegou à delegacia.","A viatura chegou à um posto.","Começou à chover.","Fomos à pé.","Entregou o relatório à ele."],"Chegar pede a; delegacia aceita artigo.")
q(1,"Complete: “O plantão vai das 18h ____ 6h.”",["às","as","à","a","há"],"Horas determinadas: das 18h às 6h.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Os agentes foram a pé até o terminal.","Os agentes foram à pé até o terminal.","Os agentes foram à cavalo até o terminal.","Os agentes começaram à correr.","Os agentes chegaram à uma conclusão."],"Pé é masculino: a pé.")
q(1,"Assinale a locução que leva acento grave.",["às pressas","a pé","a cavalo","a prazo","a lápis"],"Locução formada com palavra feminina: às pressas.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Refiro-me àquele guarda da praça.","Refiro-me aquele guarda da praça.","Refiro-me à aquele guarda da praça.","Refiro-me á aquele guarda da praça.","Refiro-me há aquele guarda da praça."],"Referir-se a + aquele = àquele.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Entreguei o crachá a ela.","Entreguei o crachá à ela.","Entreguei o crachá á ela.","Entreguei o crachá há ela.","Entreguei o crachá às ela."],"Pronome pessoal não aceita artigo.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Vou a Campinas na sexta-feira.","Vou à Campinas na sexta-feira.","Vou á Campinas na sexta-feira.","Vou há Campinas na sexta-feira.","Vou às Campinas na sexta-feira."],"Volto de Campinas: sem crase.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Vou à Bahia nas férias.","Vou a Bahia nas férias.","Vou há Bahia nas férias.","Vou á Bahia nas férias.","Vou às Bahia nas férias."],"Volto da Bahia: crase.")
q(1,"Complete: “O motorista ficou cara ____ cara com o guarda.”",["a","à","às","há","á"],"Palavras repetidas: sem crase.")
q(1,"Complete: “Chegamos ____ uma conclusão.”",["a","à","às","há","á"],"Artigo indefinido “uma”: sem crase.")
q(1,"Complete: “Dirijo-me ____ Vossa Excelência.”",["a","à","às","há","á"],"Pronome de tratamento não aceita artigo.")
q(1,"Complete: “A reunião será ____ uma hora da tarde.”",["à","a","há","às","á"],"Hora determinada: à uma hora.")
q(1,"Complete: “____ dez anos, ele entrou na Guarda.”",["Há","A","À","Às","Ah"],"Tempo passado: há (faz dez anos).")
q(1,"Complete: “O posto fica ____ dois quilômetros daqui.”",["a","há","à","às","á"],"Distância: preposição a.")
q(1,"Complete: “Os agentes estão ____ disposição da população.”",["à","a","há","ás","as"],"Locução feminina: à disposição.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Ele começou a trabalhar cedo.","Ele começou à trabalhar cedo.","Ele começou há trabalhar cedo.","Ele começou á trabalhar cedo.","Ele começou às trabalhar cedo."],"Antes de verbo, nunca há crase.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["O carro estava à venda na esquina.","O carro estava há venda na esquina.","O carro estava á venda na esquina.","O carro estava às venda na esquina.","O carro estava àa venda na esquina."],"Locução feminina: à venda.")
q(1,"Assinale a frase em que há crase obrigatória.",["Obedeça à sinalização.","Obedeça a todas as regras.","Obedeça a esta regra.","Obedeça a ela.","Obedeça a qualquer ordem."],"Obedecer a + a sinalização. Nas demais, o termo não aceita artigo.")
q(1,"Complete: “Prefiro a ronda ____ base.”",["à","a","há","às","á"],"Preferir A a B; “base” aceita artigo: à base.")
q(1,"No primeiro parágrafo, em “das 18h às 23h”, o acento grave se justifica porque",["indica horas determinadas, com preposição e artigo.","antecede verbo.","antecede palavra masculina.","antecede nome de cidade.","é facultativo."],"Horas determinadas levam crase.","tr")
q(2,"Assinale a frase em que o acento grave é facultativo.",["Refiro-me à sua escala.","Refiro-me à escala.","Refiro-me àquela escala.","Cheguei às 22h.","Saiu às pressas."],"Antes de possessivo feminino singular, o artigo é opcional.")
q(2,"Assinale a frase em que o acento grave é facultativo.",["Foi até à delegacia.","Foi à delegacia.","Foi às pressas.","Voltou à noite.","Assistiu à palestra."],"Depois de “até”, a crase é facultativa.")
q(2,"Assinale a frase em que o acento grave é facultativo.",["Entreguei o relatório à Mariana.","Entreguei o relatório à delegada.","Entreguei o relatório à chefia.","Entreguei o relatório à equipe.","Entreguei o relatório às 18h."],"Antes de nome próprio feminino de pessoa, o artigo é opcional.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Voltou a casa depois do plantão.","Voltou à casa depois do plantão.","Voltou há casa depois do plantão.","Voltou às casa depois do plantão.","Voltou á casa depois do plantão."],"Casa no sentido de lar, sem determinante: sem crase.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Voltou à casa dos pais depois do plantão.","Voltou a casa dos pais depois do plantão.","Voltou há casa dos pais depois do plantão.","Voltou ás casa dos pais depois do plantão.","Voltou às casa dos pais depois do plantão."],"Com determinante (dos pais), casa aceita artigo: crase.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Fui à Campinas da minha infância.","Fui a Campinas da minha infância.","Fui há Campinas da minha infância.","Fui às Campinas da minha infância.","Fui á Campinas da minha infância."],"Cidade com determinante aceita artigo: crase.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["A ocorrência de hoje é semelhante à de ontem.","A ocorrência de hoje é semelhante a de ontem.","A ocorrência de hoje é semelhante há de ontem.","A ocorrência de hoje é semelhante á de ontem.","A ocorrência de hoje é semelhante àa de ontem."],"Semelhante a + a (= aquela) de ontem: à de ontem.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["A escala à qual me refiro foi alterada.","A escala a qual me refiro foi alterada.","A escala há qual me refiro foi alterada.","A escala á qual me refiro foi alterada.","A escala às qual me refiro foi alterada."],"Referir-se a + a qual: à qual.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Fui a reuniões a semana toda.","Fui à reuniões a semana toda.","Fui às reunião a semana toda.","Fui á reuniões a semana toda.","Fui há reuniões a semana toda."],"“A” no singular antes de plural é só preposição.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["A operação vai de 10 a 30 de novembro.","A operação vai de 10 à 30 de novembro.","A operação vai de 10 há 30 de novembro.","A operação vai de 10 às 30 de novembro.","A operação vai de 10 á 30 de novembro."],"Numeral sem artigo: sem crase.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Daqui a dois dias, a escala muda.","Daqui à dois dias, a escala muda.","Daqui há dois dias, a escala muda.","Daqui á dois dias, a escala muda.","Daqui às dois dias, a escala muda."],"Futuro: daqui a.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Pedi bife à parmegiana no intervalo.","Pedi bife a parmegiana no intervalo.","Pedi bife há parmegiana no intervalo.","Pedi bife á parmegiana no intervalo.","Pedi bife às parmegiana no intervalo."],"Expressão “à moda de” subentendida.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["O sargento ficou frente a frente com o suspeito.","O sargento ficou frente à frente com o suspeito.","O sargento ficou frente há frente com o suspeito.","O sargento ficou frente á frente com o suspeito.","O sargento ficou frente às frente com o suspeito."],"Palavras repetidas: sem crase.")
q(2,"Assinale a frase em que o acento grave está INCORRETO.",["Entregou a carta à Vossa Senhoria.","Entregou a carta à senhora.","Entregou a carta à chefe.","Entregou a carta àquela agente.","Entregou a carta às 10h."],"Vossa Senhoria não aceita artigo; “senhora” aceita.")
q(2,"Assinale a frase em que o acento grave está INCORRETO.",["Os agentes saíram à cavalo.","Os agentes saíram à noite.","Os agentes saíram às pressas.","Os agentes saíram à procura do suspeito.","Os agentes saíram à tarde."],"Cavalo é masculino: a cavalo.")
q(2,"Complete: “A Guarda respondeu ____ reclamações dos moradores ____ partir de segunda-feira.”",["às / a","as / à","às / à","há / a","as / há"],"Responder a + as reclamações = às; antes do verbo partir, só a.")
q(2,"Em “Refiro-me àquilo que você disse”, o acento grave resulta da fusão de",["preposição “a” com o pronome “aquilo”.","artigo com artigo.","preposição com verbo.","dois pronomes.","preposição com advérbio."],"Referir-se a + aquilo = àquilo.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Estou disposto a colaborar com a investigação.","Estou disposto à colaborar com a investigação.","Estou disposto há colaborar com a investigação.","Estou disposto á colaborar com a investigação.","Estou disposto às colaborar com a investigação."],"Antes de verbo, sem crase.")
q(2,"No primeiro parágrafo, em “A medida atende às reclamações”, há crase porque",["o verbo foi construído com a preposição “a”, e “reclamações” vem com o artigo “as”.","antecede hora.","é locução adverbial.","antecede verbo.","é facultativa antes de plural."],"Atender a + as reclamações = às reclamações.","tr")
q(2,"No segundo parágrafo, em “Os agentes circularão a pé”, não há crase porque",["“pé” é palavra masculina.","antecede verbo.","antecede pronome.","antecede nome de cidade.","é locução facultativa."],"Antes de masculino, sem crase.","tr")
q(3,"No terceiro parágrafo, “Há duas semanas” está escrito com “há”, e não com “a”, porque",["indica tempo passado, com o verbo haver.","indica distância.","indica tempo futuro.","é preposição antes de numeral.","é crase facultativa."],"Há = faz: tempo passado.","tr")
q(3,"No segundo parágrafo, em “de 10 a 30 de novembro”, não há crase porque",["não há artigo antes do numeral, apenas a preposição.","“novembro” é masculino.","antecede verbo.","antecede pronome.","a crase é facultativa entre numerais."],"Entre numerais sem artigo, só preposição.","tr")
q(3,"No terceiro parágrafo, em “dirigir-se a qualquer agente”, não há crase porque",["“qualquer agente” não admite artigo feminino.","antecede verbo.","indica hora.","é locução adverbial.","a crase é facultativa antes de pronome indefinido."],"Pronome indefinido não aceita artigo.","tr")
q(3,"No terceiro parágrafo, em “à frente da bilheteria”, o acento grave se justifica por se tratar de",["locução prepositiva formada com palavra feminina.","hora determinada.","nome próprio de pessoa.","pronome possessivo.","verbo no infinitivo."],"À frente de é locução feminina.","tr")
q(3,"Assinale a alternativa em que o acento grave está correto em todas as ocorrências.",["Fui à delegacia às 10h e voltei à noite.","Fui à delegacia às 10h e voltei à pé.","Fui a delegacia às 10h e voltei à noite.","Fui à delegacia as 10h e voltei à noite.","Fui à delegacia às 10h e comecei à escrever."],"Ir a + a delegacia; hora determinada; locução feminina.")
q(3,"Assinale a alternativa em que o acento grave está INCORRETO.",["Chegou à uma conclusão rapidamente.","Chegou à uma hora da manhã.","Chegou à praça às 22h.","Chegou à conclusão certa.","Chegou à noite."],"Artigo indefinido “uma” não leva crase, salvo na indicação de hora.")
q(3,"Complete: “Entreguei o termo ____ Vossa Senhoria, mas o original ficou ____ disposição da chefe ____ partir de hoje.”",["a / à / a","à / à / à","a / a / à","à / a / a","a / à / à"],"Tratamento sem artigo; locução feminina; antes de verbo, sem crase.")
q(3,"Assinale a alternativa em que a troca por uma palavra masculina comprova a crase.",["Fui à praça. / Fui ao parque.","Fui a Campinas. / Fui a Sorocaba.","Comecei a correr. / Comecei a andar.","Entreguei a ela. / Entreguei a ele.","Fiquei cara a cara. / Fiquei frente a frente."],"Se o masculino pede “ao”, o feminino pede “à”.")
q(3,"Assinale a frase em que há erro no uso de “há” ou “a”.",["Daqui há dez minutos a viatura chega.","Há dez minutos a viatura chegou.","Daqui a dez minutos a viatura chega.","A viatura está a dez metros.","Há muito tempo não chove."],"Futuro: daqui a dez minutos.")
q(3,"Assinale a frase em que o acento grave é obrigatório.",["Assisti à operação inteira.","Assisti a uma operação.","Assisti a esta operação.","Assisti a ela.","Assisti a operações."],"Assistir a + a operação. Nas demais: artigo indefinido, demonstrativo, pessoal e plural sem artigo.")
q(3,"Assinale a alternativa em que as duas formas são aceitas.",["Foi até a praça. / Foi até à praça.","Foi a pé. / Foi à pé.","Chegou às 10h. / Chegou as 10h.","Vou a Campinas. / Vou à Campinas.","Começou a chover. / Começou à chover."],"Depois de “até”, a crase é facultativa.")
q(3,"Assinale a alternativa em que as duas formas são aceitas.",["Refiro-me a sua escala. / Refiro-me à sua escala.","Refiro-me a escala. / Refiro-me à escala.","Refiro-me aquela escala. / Refiro-me àquela escala.","Refiro-me a ela. / Refiro-me à ela.","Refiro-me a esta escala. / Refiro-me à esta escala."],"Antes de possessivo feminino singular, a crase é facultativa.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["O guarda aspira à promoção desde o ano passado.","O guarda aspira a promoção desde o ano passado.","O guarda aspira há promoção desde o ano passado.","O guarda aspira á promoção desde o ano passado.","O guarda aspira às promoção desde o ano passado."],"Aspirar (desejar) pede a; “promoção” aceita artigo: à promoção.")
q(3,"Assinale a frase em que o acento grave está INCORRETO.",["A medida não agradou à todos.","A medida não agradou à população.","A medida não agradou às famílias.","A medida não agradou àquela comissão.","A medida não agradou à equipe."],"“Todos” é masculino e indefinido: agradou a todos.")
q(3,"Assinale a frase em que a crase ocorre antes de nome masculino por indicar “à moda de”.",["Ele dribla à Garrincha.","Ele chegou à praça.","Ele saiu à noite.","Ele dirigiu-se à chefe.","Ele obedeceu à regra."],"À Garrincha = à moda de Garrincha.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["Os ambulantes ficaram à espera da fiscalização.","Os ambulantes ficaram a espera da fiscalização.","Os ambulantes ficaram há espera da fiscalização.","Os ambulantes ficaram á espera da fiscalização.","Os ambulantes ficaram às espera da fiscalização."],"Locução feminina: à espera de.")
q(3,"Complete: “Ele não se referiu ____ você nem ____ ninguém; referiu-se apenas ____ delegada.”",["a / a / à","à / à / à","a / à / a","à / a / à","a / a / a"],"Você e ninguém não aceitam artigo; “delegada” aceita.")
q(3,"Assinale a alternativa em que o acento grave está correto.",["Esta ocorrência é igual à que registramos ontem.","A escala à que me refiro mudou.","Entreguei o termo à quem pediu.","Fui à uma reunião.","Estou à seu dispor."],"À que = àquela que. Nas demais: a que (relativo), a quem, a uma, a seu dispor.")
q(3,"Assinale a afirmação INCORRETA sobre crase.",["Há crase antes de verbo no infinitivo.","Há crase nas horas determinadas.","Não há crase antes de palavra masculina, salvo com “à moda de”.","Depois de “até”, a crase é facultativa.","Antes de pronome possessivo feminino singular, a crase é facultativa."],"Antes de verbo nunca há crase.")
q(3,"Complete: “Das 8h ____ 18h, os agentes ficam ____ porta do prédio; ____ noite, o turno passa ____ uma equipe reserva.”",["às / à / À / a","às / a / A / à","as / à / À / à","às / à / A / à","as / a / À / a"],"Horas; à porta (ficar à porta); locução à noite; artigo indefinido uma, sem crase.")
tr="<strong>Guarda reforça rondas no terminal à noite</strong><br><br>A partir da próxima segunda-feira, a Guarda Municipal reforçará as rondas no terminal central, das 18h às 23h. A medida atende às reclamações de passageiros, que relataram furtos à saída das plataformas.<br><br>Os agentes circularão a pé e ficarão à disposição dos usuários para qualquer orientação. Segundo a coordenação, a operação deve durar de 10 a 30 de novembro e poderá ser estendida a outros terminais.<br><br>Há duas semanas, a corporação já havia instalado uma base móvel à frente da bilheteria. Quem precisar de ajuda deve dirigir-se a qualquer agente uniformizado."
code,svg=mapa("Crase exige duas coisas ao mesmo tempo: preposição pedida e artigo aceito",[
 ("oque","O que é",["a (preposição) + a (artigo)","a + aquele, aquela, aquilo","teste: troque por masculino"],"seção 1"),
 ("obrig","Obrigatória",["chegou à delegacia","às 22h; à meia-noite","à noite, às pressas, à frente de"],"seção 2"),
 ("proib","Proibida",["a pé; começou a chover","a ela; a Vossa Excelência","cara a cara; de 10 a 20"],"seção 3"),
 ("facult","Facultativa",["a sua ou à sua escala","a Mariana ou à Mariana","até a ou até à praça"],"seção 4"),
 ("lugar","Nomes de lugar",["vou a Campinas (volto de)","vou à Bahia (volto da)","à Campinas da infância"],"seções 1 e 3"),
 ("ha","Há ou a",["há dez anos: passado","daqui a dez dias: futuro","a dois quilômetros: distância"],"seção 5")],
 "Na prova: troque por masculino; se surgir “ao”, há crase")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"Os quatro primeiros grupos são a regra e seus três casos; os dois últimos, as confusões mais cobradas.","Fontes: Edital 02/2026, Anexo I. Referências de base: Bechara, <em>Moderna Gramática Portuguesa</em>; Cunha e Cintra, <em>Nova Gramática do Português Contemporâneo</em>. Exemplos criados para a aula.")
revisao("pt-12",'Crase',Q,{'tr':tr},pendencias=["Aula escrita antes do padrão de revisão: não há registro do que foi conferido na fonte. Conferir exemplos e regras contra Bechara e Cunha e Cintra."])
gravar("pt-12",aula_html,banco("pt-12",Q),{"tr":tr})
print(len(aula_html)); print(QRF)
