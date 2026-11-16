import sys,pickle; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','gerador')); from aulas import *
LEAD="Regência é a relação entre uma palavra que exige um complemento e esse complemento. Na prática, é saber se depois do verbo ou do nome vem preposição, e qual. A Vunesp cobra três coisas: verbos que mudam de sentido conforme a regência, verbos que a fala usa errado e a preposição que sobe para antes do pronome relativo."
S={}
S[1]="""## 1. O que é regência

Toda palavra que pede complemento é o **termo regente**; o complemento é o **termo regido**. Quando a ligação entre os dois exige preposição, é ela que a regência controla. Em “Os agentes obedecem **ao** regulamento”, “obedecer” é o regente e exige a preposição “a”.

O verbo que liga o complemento sem preposição é **transitivo direto** (registrou a ocorrência). O que liga com preposição é **transitivo indireto** (precisou de ajuda). Alguns verbos mudam de sentido conforme a regência, e é aí que mora a maior parte das questões.
"""
S[2]="""## 2. Verbos que mudam de sentido com a regência

**Assistir.** No sentido de ver, presenciar, pede “a” e não aceita “lhe”: “Assisti **ao** jogo”; “Assisti **a ele**”. No sentido de ajudar, prestar assistência, é transitivo direto: “O médico assistiu **o** ferido.” No sentido de caber, ser de direito, pede “a”: “Assiste **ao** preso o direito de permanecer calado.”

**Aspirar.** No sentido de desejar, pretender, pede “a”: “Ele aspira **ao** cargo de inspetor.” No sentido de respirar, é transitivo direto: “Aspirou **o** ar frio da madrugada.”

**Visar.** No sentido de mirar ou de pôr visto, é transitivo direto: “Visou **o** alvo”; “O fiscal visou **o** documento.” No sentido de pretender, a norma tradicional pede “a”: “A operação visa **à** redução dos furtos.”

**Proceder.** No sentido de realizar, dar início, pede “a”: “Procederam **à** vistoria.” No sentido de ter fundamento, não tem complemento: “A denúncia não procede.” No sentido de vir de, pede “de”: “O carregamento procede **de** Santos.”

**Querer.** No sentido de desejar, é transitivo direto: “Quero **o** relatório até as 18h.” No sentido de estimar, ter afeto, pede “a”: “O comandante quer bem **aos** seus agentes”; “Quero-**lhe** muito bem.”

**Chamar.** No sentido de convocar, é transitivo direto: “Chamei **o** guarda para a reunião” (chamei-**o**). No sentido de dar nome, qualificar, aceita as duas formas, com ou sem “de”: “Chamou-**o** (de) covarde” ou “Chamou-**lhe** (de) covarde”.
"""
S[3]="""## 3. Verbos que a fala usa diferente da norma

Estes verbos aparecem errados no dia a dia, e a prova cobra justamente a forma da norma-padrão.

| Evite | Use |
| --- | --- |
| Os agentes obedecem o regulamento | Os agentes obedecem **ao** regulamento |
| Prefiro patrulhar do que ficar na base | Prefiro patrulhar **a** ficar na base |
| A viatura chegou na delegacia | A viatura chegou **à** delegacia |
| O guarda foi no centro | O guarda foi **ao** centro |
| O suspeito reside à Rua das Flores | O suspeito reside **na** Rua das Flores |
| A demora implica em prejuízo | A demora implica prejuízo |
| Esqueci do crachá | Esqueci o crachá / Esqueci-**me do** crachá |
| Ela namora com um colega | Ela namora um colega |
| Me simpatizo com a ideia | Simpatizo **com** a ideia |
| Eu custei a entender | Custou-**me** entender |

Alguns verbos têm **dois complementos**, um de coisa e um de pessoa, e a preposição vai para um só deles:

1. **Informar** e **avisar**: informar alguém **de** algo, ou informar algo **a** alguém. “Informei o motorista **da** multa” ou “Informei a multa **ao** motorista”, nunca “informei ao motorista da multa”.
2. **Comunicar**: comunicar algo **a** alguém. “Comunicou o fato **à** delegacia.”
3. **Pagar**, **perdoar** e **agradecer**: a coisa sem preposição, a pessoa com “a”. “Paguei o conserto **ao** mecânico”; “Agradeci **ao** guarda a ajuda.”

[[NOTA: “Preferir” já significa “querer mais”: não leva “mais”, “antes” nem “do que”. O segundo termo vem com “a”: “Prefiro a ronda **à** base.”]]
"""
S[4]="""## 4. Regência nominal

Substantivos, adjetivos e advérbios também pedem preposição. Não há regra que dispense a memória; o que ajuda é agrupar pelos mais cobrados.

- **Pedem “a”:** acessível, alheio, aversão (ou “por”), contrário, favorável, fiel, imune (ou “de”), inerente, necessário (ou “para”), obediência, paralelo, preferível, propenso, relativo. “A medida é **favorável aos** moradores.”
- **Pedem “com”:** compatível, conforme, cuidadoso, solidário. “A decisão é **compatível com** a lei.”
- **Pedem “de”:** capaz, cheio, digno, passível, suspeito. “O ato é **passível de** multa.”
- **Pedem “em”:** residente, situado, domiciliado, versado. “Ele é **residente em** Campinas.”
- **Pedem “para” ou “a”:** apto, útil, prejudicial. “Ele é **apto para** o serviço.”
- **Pedem “por”:** ansioso, responsável. “Está **ansioso por** resultados.”
"""
S[5]="""## 5. Preposição antes do pronome relativo

Quando o verbo da oração com “que”, “quem” ou “cujo” exige preposição, ela vai para **antes do relativo**. O teste é desfazer a frase e ver a preposição aparecer:

1. Assisti **ao** filme → o filme **a que** assisti.
2. Aspiro **ao** cargo → o cargo **a que** aspiro.
3. Todos obedecem **ao** regulamento → o regulamento **a que** todos obedecem.
4. Discordo **da** escala → a escala **de que** discordo.
5. Trabalho **com** essas pessoas → as pessoas **com quem** trabalho.
6. Moro **na** rua → a rua **em que** moro.
7. Atendemos **ao** pedido do inspetor → o inspetor **a cujo** pedido atendemos.

Se o verbo não pede preposição, o relativo vem sozinho: “a escala **que** todos preferem” (preferir algo).

[[NOTA: Regência e crase andam juntas: quando o verbo pede “a” e o nome é feminino com artigo, surge a crase (chegou **à** delegacia; procederam **à** vistoria). O assunto completo está no posto 12.]]
"""
S[7]="""## 7. Na rotina do guarda

- **Relatório:** “A equipe procedeu **à** vistoria do local” e “chegou **à** delegacia às 23h”, não “chegou na delegacia”.
- **Qualificação:** “O conduzido reside **na** Rua das Flores, 120”, não “à Rua”.
- **Ofício:** “Informo Vossa Senhoria **de** que...” ou “Informo **a** Vossa Senhoria que...”; “Comunico o ocorrido **a** esta chefia.”
- **Abordagem:** “Os condutores devem obedecer **à** sinalização.”
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| “Assisti o jogo” | ver: assistir a; ajudar: assistir alguém |
| “Assisti-lhe” (ao jogo) | assistir no sentido de ver não aceita lhe: assisti a ele |
| “Aspiro o cargo” | desejar: aspirar a |
| “Prefiro mais isto do que aquilo” | preferir isto a aquilo |
| “Implica em atraso” | implicar (acarretar) é direto: implica atraso |
| “Chegou na delegacia”, “foi no centro” | chegar a, ir a |
| “Esqueci do crachá” | esqueci o crachá ou esqueci-me do crachá |
| “Informei ao motorista da multa” | só um complemento leva preposição |
| “O filme que assisti” | o filme a que assisti |
| “Reside à Rua X” | reside na Rua X |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Assistir | ver: a (sem lhe); ajudar: direto; caber: a |
| Aspirar | desejar: a; respirar: direto |
| Proceder | realizar: a; ter fundamento: sem complemento |
| Querer | desejar: direto; estimar: a |
| Obedecer | obedecer a |
| Preferir | preferir A a B, sem mais e sem do que |
| Ir, chegar | a; residir, morar: em |
| Implicar | acarretar: direto, sem em |
| Esquecer, lembrar | o crachá; ou esquecer-se do crachá |
| Informar | alguém de algo, ou algo a alguém |
| Pagar, agradecer | a coisa direta; a pessoa com a |
| Custar | custou-me entender |
| Regência nominal | favorável a, compatível com, passível de, residente em |
| Relativo | o filme a que assisti; as pessoas com quem trabalho |
"""
QR=[("Questão 1","Assinale a frase em que o verbo assistir está no sentido de ver e com a regência da norma-padrão.",["Os guardas assistiram à palestra.","Os guardas assistiram a palestra no auditório? Não: a palestra.","Os guardas assistiram-lhe com atenção.","Os guardas assistiram na palestra.","O médico assistiu o ferido."],2,"No sentido de ver, assistir pede a: à palestra. Em (E), o sentido é ajudar."),
("Questão 2","Complete: “O cargo ____ ele aspira exige experiência; a vistoria ____ procedemos durou duas horas.”",["a que / a que","que / que","de que / a que","a que / que","que / em que"],3,"Aspirar (desejar) e proceder (realizar) pedem a: a que, a que."),
("Questão 3","Assinale a frase de acordo com a norma-padrão.",["Prefiro orientar a multar.","Prefiro mais orientar do que multar.","Prefiro orientar do que multar.","Prefiro antes orientar que multar.","Prefiro muito mais orientar a multar."],1,"Preferir pede “a” no segundo termo, sem “mais”, “antes” ou “do que”."),
("Questão 4","Assinale a alternativa em que o nome está seguido da preposição que exige.",["A medida é favorável aos moradores.","Tenho aversão com barulho.","Ele é residente à Rua das Flores.","A lei é compatível ao decreto.","O guarda é apto em dirigir."],4,"Favorável a. Nas demais: aversão a (ou por), residente em, compatível com, apto para (ou a).")]
QR[0]=("Questão 1",QR[0][1],["Os guardas assistiram à palestra.","Os guardas assistiram a palestra.","Os guardas assistiram-lhe com atenção.","Os guardas assistiram na palestra.","O médico assistiu o ferido."],2,QR[0][4])
QRF=qr_md(QR,6)
Q=[]
def q(n,e,a,c,tx=None): Q.append((n,e,a,c,tx))
q(1,"Assinale a frase de acordo com a norma-padrão.",["Assisti ao jogo na casa do parceiro.","Assisti o jogo na casa do parceiro.","Assisti no jogo na casa do parceiro.","Assisti com o jogo na casa do parceiro.","Assisti do jogo na casa do parceiro."],"No sentido de ver, assistir pede a preposição a.")
q(1,"Em “O médico assistiu o ferido na calçada”, o verbo assistir significa",["prestar assistência, socorrer.","ver, presenciar.","morar.","caber, pertencer.","desejar."],"Transitivo direto, no sentido de ajudar.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["O guarda aspira ao cargo de inspetor.","O guarda aspira o cargo de inspetor.","O guarda aspira pelo cargo de inspetor.","O guarda aspira no cargo de inspetor.","O guarda aspira com o cargo de inspetor."],"No sentido de desejar, aspirar pede a preposição a.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Os agentes obedecem ao regulamento.","Os agentes obedecem o regulamento.","Os agentes obedecem do regulamento.","Os agentes obedecem no regulamento.","Os agentes obedecem pelo regulamento."],"Obedecer é transitivo indireto: obedecer a.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Prefiro patrulhar a ficar na base.","Prefiro patrulhar do que ficar na base.","Prefiro mais patrulhar do que ficar na base.","Prefiro patrulhar que ficar na base.","Prefiro mil vezes patrulhar do que ficar na base."],"Preferir A a B, sem “mais” nem “do que”.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["A viatura chegou à delegacia às 23h.","A viatura chegou na delegacia às 23h.","A viatura chegou em a delegacia às 23h.","A viatura chegou pela delegacia às 23h.","A viatura chegou com a delegacia às 23h."],"Chegar pede a: chegou à delegacia.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["O suspeito reside na Rua das Flores.","O suspeito reside à Rua das Flores.","O suspeito reside a Rua das Flores.","O suspeito reside pela Rua das Flores.","O suspeito reside para a Rua das Flores."],"Residir pede em.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Esqueci o crachá na viatura.","Esqueci do crachá na viatura.","Esqueci-me o crachá na viatura.","Me esqueci o crachá na viatura.","Esqueci com o crachá na viatura."],"Esquecer algo (sem pronome) ou esquecer-se de algo.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Lembrei-me do horário da escala.","Lembrei do horário da escala.","Lembrei-me o horário da escala.","Me lembrei o horário da escala.","Lembrei-me com o horário da escala."],"Lembrar-se de algo, ou lembrar algo.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["A demora implica prejuízo à investigação.","A demora implica em prejuízo à investigação.","A demora implica no prejuízo à investigação.","A demora implica para prejuízo à investigação.","A demora implica com prejuízo à investigação."],"Implicar, no sentido de acarretar, é transitivo direto.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Ela namora um colega da Guarda.","Ela namora com um colega da Guarda.","Ela namora de um colega da Guarda.","Ela namora a um colega da Guarda.","Ela namora por um colega da Guarda."],"Namorar é transitivo direto.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Simpatizo com a nova escala.","Simpatizo-me com a nova escala.","Me simpatizo com a nova escala.","Simpatizo a nova escala.","Simpatizo-me a nova escala."],"Simpatizar não é pronominal: simpatizo com.")
q(1,"Em “Procederam à vistoria do prédio”, o verbo proceder significa",["dar início, realizar.","ter fundamento.","originar-se.","comportar-se.","desistir."],"Proceder a = realizar.")
q(1,"Em “A denúncia não procede”, o verbo proceder significa",["ter fundamento.","realizar.","originar-se.","dar início.","comportar-se mal."],"Sem complemento, proceder = ter fundamento.")
q(1,"Assinale o nome que pede a preposição “a”.",["favorável","capaz","compatível","residente","ansioso"],"Favorável a. Capaz de; compatível com; residente em; ansioso por.")
q(1,"Complete: “A medida é compatível ____ o orçamento.”",["com","de","em","por","sobre"],"Compatível com.")
q(1,"Complete: “Ele é residente ____ Campinas.”",["em","a","de","para","com"],"Residente em.")
q(1,"Complete: “O filme ____ assisti era longo.”",["a que","que","de que","em que","com que"],"Assisti ao filme → o filme a que assisti.")
q(1,"Complete: “O cargo ____ aspiro exige curso superior.”",["a que","que","de que","com que","em que"],"Aspiro ao cargo → o cargo a que aspiro.")
q(1,"No primeiro parágrafo, em “procedeu [...] à vistoria”, o verbo proceder significa",["realizar, dar início.","ter fundamento.","originar-se.","desistir.","comportar-se."],"Proceder a = realizar: a Guarda fez a vistoria.","tp")
q(2,"Assinale a frase em que “assistir” está empregado no sentido de “caber, ser de direito”.",["Assiste ao preso o direito de permanecer calado.","Assisti ao jogo no domingo.","O médico assistiu o ferido.","Os guardas assistiram à palestra.","Ninguém assistiu ao acidente."],"Assistir a = caber: o direito cabe ao preso.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["O jogo? Assisti a ele no domingo.","O jogo? Assisti-lhe no domingo.","O jogo? Assisti-o no domingo.","O jogo? Lhe assisti no domingo.","O jogo? O assisti no domingo."],"No sentido de ver, assistir não aceita lhe: assisti a ele.")
q(2,"Em “O guarda aspirou o ar frio da madrugada”, o verbo aspirar significa",["respirar, sorver.","desejar.","pretender um cargo.","mirar.","ajudar."],"Transitivo direto, no sentido de respirar.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["O atirador visou o alvo com cuidado.","O atirador visou ao alvo com cuidado.","O atirador visou no alvo com cuidado.","O atirador visou para o alvo com cuidado.","O atirador visou com o alvo com cuidado."],"No sentido de mirar, visar é transitivo direto.")
q(2,"Em “Quero-lhe muito bem”, o verbo querer significa",["estimar, ter afeto.","desejar possuir.","exigir.","procurar.","permitir."],"No sentido de estimar, querer pede a: quero-lhe bem.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Informei o motorista da multa.","Informei o motorista a multa.","Informei ao motorista da multa.","Informei do motorista a multa.","Informei para o motorista da multa."],"Informar alguém de algo. Só um dos complementos leva preposição.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Comunicou o fato à delegacia.","Comunicou à delegacia do fato.","Comunicou do fato a delegacia.","Comunicou a delegacia o fato.","Comunicou-se o fato a delegacia."],"Comunicar algo a alguém.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Paguei o conserto ao mecânico.","Paguei o mecânico.","Paguei do mecânico o conserto.","Paguei ao conserto o mecânico.","Paguei o conserto do mecânico a ele."],"Pagar a coisa (direto) a alguém (com a).")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Agradeci ao guarda pela ajuda.","Agradeci o guarda pela ajuda.","Agradeci do guarda pela ajuda.","Agradeci com o guarda pela ajuda.","Agradeci pelo guarda a ajuda."],"Agradecer a alguém.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Custou-me entender a nova escala.","Custei-me entender a nova escala.","Custou-me de entender a nova escala.","Custei-me a entender a nova escala.","Eu custo de entender a nova escala."],"No sentido de ser difícil, custar tem como sujeito a coisa difícil: entender custou a mim.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["O guarda foi ao centro buscar a viatura.","O guarda foi no centro buscar a viatura.","O guarda foi em o centro buscar a viatura.","O guarda foi com o centro buscar a viatura.","O guarda foi sobre o centro buscar a viatura."],"Ir pede a: foi ao centro.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Chamei o guarda para a reunião.","Chamei ao guarda para a reunião.","Chamei do guarda para a reunião.","Chamei-lhe para a reunião.","Chamei com o guarda para a reunião."],"No sentido de convocar, chamar é transitivo direto: chamei-o.")
q(2,"Assinale a alternativa em que as duas formas estão de acordo com a norma-padrão.",["Chamou-o de covarde. / Chamou-lhe covarde.","Assisti o jogo. / Assisti ao jogo.","Implica em atraso. / Implica atraso.","Prefiro isto do que aquilo. / Prefiro isto a aquilo.","Obedeço o regulamento. / Obedeço ao regulamento."],"No sentido de qualificar, chamar aceita objeto direto ou indireto, com ou sem de.")
q(2,"Complete: “O regulamento ____ todos devem obedecer está na parede.”",["a que","que","de que","com que","em que"],"Obedecer a: o regulamento a que todos obedecem.")
q(2,"Complete: “A escala ____ discordo foi publicada ontem.”",["de que","que","a que","com que","em que"],"Discordar de: a escala de que discordo.")
q(2,"Complete: “As pessoas ____ trabalho são pontuais.”",["com quem","que","quem","a quem","de quem"],"Trabalhar com: as pessoas com quem trabalho.")
q(2,"Complete: “A rua ____ moro é escura.”",["em que","que","a que","de que","com que"],"Morar em: a rua em que moro.")
q(2,"Complete: “Ele é fiel ____ seus princípios.”",["a","com","de","em","por"],"Fiel a.")
q(2,"Assinale a frase em que a regência nominal está de acordo com a norma-padrão.",["A obediência às normas é inerente ao cargo.","A obediência com as normas é inerente do cargo.","A obediência das normas é inerente no cargo.","A obediência pelas normas é inerente com o cargo.","A obediência em as normas é inerente para o cargo."],"Obediência a; inerente a.")
q(2,"No segundo parágrafo, “o descumprimento implica multa” está de acordo com a norma-padrão porque",["implicar, no sentido de acarretar, é transitivo direto.","implicar exige sempre a preposição “em”.","“multa” é sujeito de implicar.","implicar é verbo intransitivo.","o verbo está na voz passiva."],"Implicar algo: implica multa.","tp")
q(3,"No último parágrafo, “as regras a que todos devem obedecer” está de acordo com a norma-padrão porque",["obedecer exige a preposição “a”, que vem antes do relativo.","o relativo “que” sempre pede a preposição “a”.","“regras” é palavra feminina.","a preposição indica lugar.","obedecer é transitivo direto."],"Todos obedecem às regras → as regras a que todos obedecem.","tp")
q(3,"No último parágrafo, “A Guarda prefere orientar a multar” poderia ser reescrito, de acordo com a norma-padrão, como",["A Guarda prefere a orientação à multa.","A Guarda prefere mais orientar do que multar.","A Guarda prefere orientar do que multar.","A Guarda prefere a orientação do que a multa.","A Guarda prefere mais a orientação que a multa."],"Preferir A a B: a orientação à multa (com crase, porque “multa” tem artigo).","tp")
q(3,"No primeiro parágrafo, em “A ação atende a um pedido dos frequentadores”, a preposição “a”",["é aceita, pois atender, nesse sentido, admite complemento com ou sem preposição.","é obrigatória, e sem ela a frase estaria errada.","indica lugar.","indica tempo.","está errada, pois atender só admite objeto direto."],"Atender a um pedido e atender um pedido são formas aceitas.","tp")
q(3,"No terceiro parágrafo, “com quem a Guarda se reuniu” está de acordo com a norma-padrão porque",["reunir-se pede a preposição “com”, que antecede o relativo.","“quem” dispensa preposição.","a preposição indica instrumento.","o relativo retoma “a medida”.","reunir-se é transitivo direto."],"A Guarda se reuniu com os moradores → os moradores com quem a Guarda se reuniu.","tp")
q(3,"No segundo parágrafo, “Os comerciantes foram informados das novas regras”. Na voz ativa, a frase de acordo com a norma-padrão é",["A Guarda informou os comerciantes das novas regras.","A Guarda informou aos comerciantes das novas regras.","A Guarda informou os comerciantes as novas regras.","A Guarda informou dos comerciantes as novas regras.","A Guarda informou-lhes das novas regras."],"Informar alguém de algo: um complemento direto e outro com de.","tp")
q(3,"Assinale a frase em que a regência verbal está INCORRETA.",["Assisti o filme da operação no auditório.","Aspiro ao cargo de inspetor.","Obedeço ao regulamento.","Prefiro a ronda à base.","Esqueci-me do crachá."],"No sentido de ver, assistir pede a: assisti ao filme.")
q(3,"Assinale a frase em que a regência verbal está INCORRETA.",["Ele namora com a irmã do colega.","Procedemos à leitura do relatório.","A denúncia não procede.","O fiscal visou o passaporte do estrangeiro.","Simpatizo com a ideia."],"Namorar é transitivo direto: namora a irmã do colega.")
q(3,"Assinale a alternativa em que o pronome “lhe” está empregado de acordo com a norma-padrão.",["Obedeço-lhe sem discutir. (ao comandante)","Assisti-lhe no estádio. (ao jogo)","Aspiro-lhe há anos. (ao cargo)","Chamei-lhe para a reunião. (o guarda, convocando)","Vi-lhe na praça. (o suspeito)"],"Obedecer a uma pessoa aceita lhe. Assistir (ver) e aspirar (desejar) pedem a ele; chamar (convocar) e ver pedem o.")
q(3,"Assinale a alternativa em que a preposição antes do relativo está de acordo com a norma-padrão.",["O inspetor a cujo pedido atendemos é novo.","O inspetor cujo o pedido atendemos é novo.","O inspetor de cujo pedido atendemos é novo.","O inspetor com cujo pedido atendemos é novo.","O inspetor que o pedido atendemos é novo."],"Atendemos ao pedido do inspetor → o inspetor a cujo pedido atendemos.")
q(3,"Complete: “Esta é a escala ____ você se referiu, e aquela é a ____ todos preferem.”",["a que / que","que / a que","de que / que","a que / a que","em que / de que"],"Referir-se a → a que; preferir algo → que.")
q(3,"Assinale a alternativa em que a regência nominal está INCORRETA.",["Ele tem aversão com barulho.","Ele é apto para o serviço.","A medida é favorável aos moradores.","O suspeito é residente em Campinas.","A decisão é compatível com a lei."],"Aversão a ou por.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["O dinheiro é necessário à compra dos coletes.","O dinheiro é necessário com a compra dos coletes.","O dinheiro é necessário em a compra dos coletes.","O dinheiro é necessário pela compra dos coletes.","O dinheiro é necessário sobre a compra dos coletes."],"Necessário a (ou para).")
q(3,"Assinale a frase de acordo com a norma-padrão.",["Prefiro o turno da noite ao da manhã.","Prefiro o turno da noite do que o da manhã.","Prefiro mais o turno da noite que o da manhã.","Prefiro antes o turno da noite do que o da manhã.","Prefiro o turno da noite mais do que o da manhã."],"Preferir A a B.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["Os comerciantes foram informados de que haveria vistoria.","Os comerciantes foram informados a vistoria.","Os comerciantes foram informados com que haveria vistoria.","Os comerciantes foram informados em que haveria vistoria.","Os comerciantes foram informados para que haveria vistoria."],"Informar alguém de algo: informados de que haveria vistoria.")
q(3,"Assinale a alternativa em que a mudança de regência altera o sentido do verbo.",["Assisti o doente. / Assisti ao jogo.","Esqueci o crachá. / Esqueci-me do crachá.","Lembrei o horário. / Lembrei-me do horário.","Atendi o pedido. / Atendi ao pedido.","Chamou-o covarde. / Chamou-lhe covarde."],"Assistir alguém = ajudar; assistir a algo = ver. Nas demais, o sentido não muda.")
q(3,"Em “Custa-me acreditar na versão do motorista”, o sujeito de “custar” é",["acreditar na versão do motorista.","me.","o motorista.","a versão.","indeterminado."],"O que custa é acreditar: o sujeito é a oração.")
q(3,"Assinale a frase de acordo com a norma-padrão quanto à regência de “ir” e “chegar”.",["Fomos ao local e chegamos à conclusão de que era furto.","Fomos no local e chegamos na conclusão de que era furto.","Fomos ao local e chegamos na conclusão de que era furto.","Fomos no local e chegamos à conclusão de que era furto.","Fomos ao local e chegamos em conclusão de que era furto."],"Ir a e chegar a.")
q(3,"Assinale a frase em que o verbo “visar” significa “pretender, ter em vista”.",["A operação visa à redução dos furtos.","O atirador visou o alvo.","O fiscal visou o documento.","O soldado visou a placa do carro com a arma.","O gerente visou o cheque."],"Visar à redução = ter como objetivo. Nas demais: mirar ou pôr visto.")
q(3,"Assinale a afirmação INCORRETA sobre regência.",["A preposição exigida pelo verbo da oração relativa desaparece diante do pronome relativo.","Alguns verbos mudam de sentido conforme a regência.","Preferir pede a preposição “a” no segundo termo.","Implicar, no sentido de acarretar, é transitivo direto.","Nomes também podem exigir preposição."],"A preposição não desaparece: ela vai para antes do relativo (o filme a que assisti).")
q(3,"Assinale a alternativa em que a regência está correta em todas as frases.",["Obedeço ao regulamento; prefiro a ronda à base; resido em Campinas.","Obedeço o regulamento; prefiro a ronda à base; resido em Campinas.","Obedeço ao regulamento; prefiro a ronda do que a base; resido em Campinas.","Obedeço ao regulamento; prefiro a ronda à base; resido à Rua Campinas.","Obedeço ao regulamento; prefiro mais a ronda à base; resido em Campinas."],"Obedecer a; preferir A a B sem mais; residir em.")
tp="<strong>Guarda vistoria quiosques da orla do lago</strong><br><br>A Guarda Municipal procedeu, na manhã de ontem, à vistoria dos quiosques instalados às margens do lago do parque. A ação atende a um pedido dos frequentadores, que reclamavam do som alto nos fins de semana.<br><br>Os comerciantes foram informados das novas regras e terão 15 dias para se adequar. Segundo a coordenação, o descumprimento implica multa e, em caso de reincidência, a suspensão da licença.<br><br>A medida agradou aos moradores do entorno, com quem a Guarda se reuniu na semana passada. A corporação prefere orientar a multar, mas lembra que as regras a que todos devem obedecer estão afixadas em cada quiosque."
code,svg=mapa("A preposição certa depende da palavra que manda",[
 ("sentido","Muda o sentido",["assistir: ver (a) / ajudar","aspirar: desejar (a) / respirar","proceder: realizar (a)"],"seção 2"),
 ("fala","A fala erra, a prova cobra",["obedecer a; preferir A a B","ir e chegar a; residir em","implicar sem em"],"seção 3"),
 ("pron","Com pronome ou sem",["esquecer-se de; lembrar-se de","simpatizar com (sem se)","custou-me entender"],"seção 3"),
 ("dupla","Dois complementos",["informar alguém de algo","comunicar algo a alguém","pagar algo a alguém"],"seção 3"),
 ("nominal","Regência nominal",["favorável a; apto para","compatível com; residente em","aversão a; passível de"],"seção 4"),
 ("relativo","Relativo com preposição",["o filme a que assisti","a escala de que discordo","as pessoas com quem trabalho"],"seção 5")],
 "Na prova: desfaça o relativo para achar a preposição: assisti ao filme, o filme a que assisti")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"Os quatro primeiros grupos tratam do verbo; os dois últimos, do nome e do relativo. Em todos, quem decide a preposição é a palavra regente.","Fontes: Edital 02/2026, Anexo I. Referências de base: Bechara, <em>Moderna Gramática Portuguesa</em>; Cunha e Cintra, <em>Nova Gramática do Português Contemporâneo</em>; Celso Pedro Luft, <em>Dicionário Prático de Regência Verbal</em>. Exemplos criados para a aula.")
revisao("pt-10",'Regência verbal e nominal',Q,{'tp':tp},pendencias=["Aula escrita antes do padrão de revisão: não há registro do que foi conferido na fonte. Conferir exemplos e regras contra Bechara e Cunha e Cintra."])
gravar("pt-10",aula_html,banco("pt-10",Q),{"tp":tp})
print(len(aula_html)); print(QRF[:900])
