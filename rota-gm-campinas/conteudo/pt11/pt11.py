import sys,pickle; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','gerador')); from aulas import *
LEAD="Colocação pronominal é a posição dos pronomes oblíquos átonos (me, te, se, o, a, lhe, nos, vos) em relação ao verbo. São três posições: antes (próclise), depois (ênclise) e no meio (mesóclise). A prova cobra a norma-padrão, que nem sempre coincide com a fala do dia a dia."
S={}
S[1]="""## 1. As três posições

O pronome oblíquo átono se apoia no verbo. A posição dele tem nome:

1. **Próclise**, antes do verbo: “Não **me** avisaram.”
2. **Ênclise**, depois do verbo, com hífen: “Avisaram-**me** tarde.”
3. **Mesóclise**, no meio do verbo, com dois hifens: “Avisar-**me**-ão amanhã.”

Quem decide a posição é, primeiro, a presença de uma **palavra atrativa** antes do verbo. Sem ela, contam o tempo do verbo e o lugar na frase.
"""
S[2]="""## 2. Próclise: quando a palavra puxa o pronome

Certas palavras atraem o pronome para antes do verbo. Com elas, a próclise é obrigatória:

- **Palavras negativas** (não, nunca, jamais, ninguém, nada, nem): “**Não me** avisaram.” “**Nunca se** esquecerá.”
- **Pronomes relativos**: “O guarda **que me** atendeu foi gentil.”
- **Pronomes indefinidos** (alguém, ninguém, tudo, todos, algo): “**Alguém me** chamou no rádio.” “**Tudo se** resolveu.”
- **Conjunções subordinativas** (quando, se, embora, que, como, porque): “**Quando o** vi, chamei a central.” “**Embora se** esforçasse...”
- **Advérbios**, sem vírgula depois: “**Aqui se** trabalha em silêncio.” “**Ontem o** encontrei.”
- **Frases interrogativas, exclamativas e de desejo**: “**Quem te** contou?” “**Quanto me** custou!” “Deus **o** acompanhe!”
- **Em + gerúndio**: “**Em se** tratando de segurança, todo cuidado é pouco.”

[[NOTA: A vírgula desfaz a atração do advérbio: “Ontem **o** encontrei” (próclise), mas “Ontem, encontrei-**o**” (ênclise).]]
"""
S[3]="""## 3. Ênclise: quando o pronome vai depois

Sem palavra atrativa, a ênclise é a posição de base da norma-padrão. Ela é obrigatória em quatro situações:

1. **Início de frase**: a norma-padrão não começa frase com pronome átono. “Diga-**me** a verdade”, e não “Me diga a verdade”.
2. **Imperativo afirmativo**: “Entregue-**me** os documentos.”
3. **Gerúndio sem “em”**: “Saiu, deixando-**o** sozinho na praça.”
4. **Depois de vírgula ou pausa**: “Ontem, encontrei-**o** na praça.”

Com **infinitivo**, a ênclise é a forma comum (“É preciso avisá-**lo**”); com palavra negativa antes, as duas posições são aceitas (“para não **o** avisar” ou “para não avisá-**lo**”).

Quando o sujeito vem expresso antes do verbo e não há palavra atrativa, as duas posições são aceitas: “Os guardas **se** aproximaram” ou “Os guardas aproximaram-**se**”.

| Evite | Use |
| --- | --- |
| Me avisaram tarde da mudança | Avisaram-**me** tarde da mudança |
| Me entregue os documentos | Entregue-**me** os documentos |
| Ninguém avisou-me | Ninguém **me** avisou |
| O guarda que atendeu-me | O guarda que **me** atendeu |
"""
S[4]="""## 4. Mesóclise: só com dois tempos

A mesóclise só existe com o **futuro do presente** e o **futuro do pretérito**, quando não há palavra atrativa e o verbo abre a frase ou vem depois de pausa. O pronome entra entre o radical e a terminação:

1. Entregar-**lhe**-ei o relatório amanhã. (entregarei)
2. Far-**se**-ia a vistoria se houvesse tempo. (faria)
3. Dir-**se**-ia que ninguém viu nada. (diria)

Com palavra atrativa, o futuro volta à próclise: “**Não lhe** entregarei.” E o futuro **nunca** aceita ênclise: “entregarei-lhe” e “faria-se” estão errados.
"""
S[5]="""## 5. Locuções verbais

Na locução, o pronome pode ficar depois do auxiliar ou depois do verbo principal, mas nunca solto entre os dois sem hífen na norma-padrão:

1. Com infinitivo ou gerúndio: “Vou-**lhe** entregar o relatório” ou “Vou entregar-**lhe** o relatório”.
2. Com palavra atrativa, antes do auxiliar ou depois do principal: “Não **lhe** vou entregar” ou “Não vou entregar-**lhe**”.
3. Com **particípio**, nunca depois do particípio: “Tinha-**me** avisado” ou “Não **me** tinha avisado”, e não “tinha avisado-me”.
"""
S[6]="""## 6. As formas lo, la, no, na

Os pronomes **o, a, os, as** mudam de forma depois de certos finais de verbo:

1. Verbo terminado em **-r, -s, -z**: a letra cai e o pronome vira **lo, la, los, las**. “entregar + o = entregá-**lo**”; “queremos + o = queremo-**lo**”; “fiz + o = fi-**lo**”; “fez + o = fê-**lo**”; “abordamos + o = abordamo-**lo**”.
2. Verbo terminado em **som nasal** (-am, -em, -ão, -õe): o pronome vira **no, na, nos, nas**. “encontraram + o = encontraram-**no**”; “põe + o = põe-**no**”.
3. Na mesóclise, a regra continua valendo: “encaminhar + o + ão = encaminhá-**lo**-ão”.

[[NOTA: Note o acento que aparece quando a última sílaba fica tônica: entregá-lo, fê-lo, pô-lo, vendê-lo.]]
"""
S[8]="""## 8. Na rotina do guarda

- **Ofício:** “Solicito-**lhe** as imagens” ou “Encaminho-**lhe** o relatório”, nunca começando por “Lhe”.
- **Relatório:** “Abordamo-**lo** na saída do terminal” ou “O abordamos”, se a frase não começar pelo pronome.
- **Ordem na abordagem:** “Entregue-**me** os documentos”, no imperativo, com ênclise.
- **Fato não ocorrido:** “Não **o** encontramos no local”, com a negativa puxando o pronome.
"""
S[9]="""## 9. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Frase começando com “me”, “te”, “lhe” | na norma, ênclise: diga-me |
| “Ninguém avisou-me”, “que atendeu-me” | negativa, indefinido e relativo atraem: ninguém me avisou |
| “Entregarei-lhe”, “faria-se” | futuro não aceita ênclise: entregar-lhe-ei, far-se-ia |
| “Não entregar-lhe-ei” | com atrativa, próclise: não lhe entregarei |
| “Tinha avisado-me” | nunca depois do particípio: tinha-me avisado |
| “Entregar-o”, “encontraram-o” | entregá-lo; encontraram-no |
| “Ontem encontrei-o” sem vírgula | advérbio atrai: ontem o encontrei |
| “Quanto custou-me!” | exclamativa atrai: quanto me custou |
"""
S[10]="""## 10. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Próclise | antes do verbo, com palavra atrativa |
| Palavras atrativas | negativas, relativos, indefinidos, conjunções subordinativas, advérbios sem vírgula |
| Frases especiais | interrogativa, exclamativa e de desejo pedem próclise |
| Ênclise | início de frase, imperativo afirmativo, gerúndio, depois de vírgula |
| Sujeito expresso | sem atrativa, próclise ou ênclise |
| Mesóclise | só futuro do presente e do pretérito, sem atrativa |
| Futuro | nunca com ênclise |
| Locução | vou-lhe entregar; vou entregar-lhe; não lhe vou entregar |
| Particípio | nunca pronome depois: tinha-me avisado |
| -r, -s, -z | lo, la: entregá-lo, fi-lo, queremo-lo |
| Som nasal | no, na: encontraram-no, põe-no |
"""
QR=[("Questão 1","Assinale a frase de acordo com a norma-padrão.",["Não me avisaram da escala.","Me avisaram tarde da escala.","Ninguém avisou-me da escala.","Avisarei-lhe da escala amanhã.","O guarda que avisou-me saiu."],2,"A negativa atrai o pronome. Nas demais: avisaram-me, ninguém me avisou, avisar-lhe-ei, que me avisou."),
("Questão 2","As formas corretas de “entregaram + o” e “entregar + o” são, respectivamente,",["entregaram-no / entregá-lo","entregaram-o / entregar-o","entregaram-lo / entregá-o","entregara-no / entregá-lo-o","entregaram-no / entregar-lo"],4,"Depois de som nasal, “no”; depois de -r, o r cai e entra “lo”, com acento."),
("Questão 3","Assinale a frase de acordo com a norma-padrão.",["Encaminhar-lhe-emos o ofício.","Encaminharemos-lhe o ofício.","Lhe encaminharemos o ofício.","Não encaminhar-lhe-emos o ofício.","Encaminharemo-lhe o ofício."],0,"Futuro do presente, sem atrativa, no início: mesóclise. Com “não”, seria “não lhe encaminharemos”."),
("Questão 4","Assinale a frase de acordo com a norma-padrão.",["Não lhe vou mentir.","Não vou-lhe mentir.","Lhe vou mentir.","Vou mentir-lhe-ia.","Não vou mentir-lhe-ei."],1,"Com palavra atrativa, o pronome vai antes do auxiliar (ou depois do principal: não vou mentir-lhe).")]
QRF=qr_md(QR,7)
Q=[]
def q(n,e,a,c,tx=None): Q.append((n,e,a,c,tx))
q(1,"Em “Não me avisaram da operação”, o pronome está em",["próclise, atraído pela palavra negativa.","ênclise.","mesóclise.","posição proibida pela norma.","próclise sem motivo, apenas aceita."],"A negativa “não” atrai o pronome.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Diga-me a verdade.","Me diga a verdade.","Me diga-me a verdade.","Lhe diga a verdade.","Te diga a verdade."],"A norma-padrão não inicia frase com pronome átono.")
q(1,"Assinale a frase em que o pronome está em mesóclise.",["Entregar-lhe-ei o relatório amanhã.","Entregarei-lhe o relatório amanhã.","Não lhe entregarei o relatório.","Vou entregar-lhe o relatório.","Entreguei-lhe o relatório."],"O pronome está no meio do verbo, no futuro do presente.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Ninguém me informou sobre a mudança.","Ninguém informou-me sobre a mudança.","Ninguém informou me sobre a mudança.","Me ninguém informou sobre a mudança.","Ninguém informar-me-ia-ou sobre a mudança."],"Ninguém atrai o pronome.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["O guarda que me atendeu foi gentil.","O guarda que atendeu-me foi gentil.","O guarda que atendeu me foi gentil.","O guarda me que atendeu foi gentil.","O guarda que atender-me-ou foi gentil."],"O pronome relativo atrai.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Quando o vi, chamei a central.","Quando vi-o, chamei a central.","Quando vi o, chamei a central.","Quando o vi-o, chamei a central.","O quando vi, chamei a central."],"A conjunção subordinativa atrai.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Entregue-me os documentos, por favor.","Me entregue os documentos, por favor.","Me entregue-me os documentos.","Lhe entregue os documentos.","Entregue me-os documentos."],"Imperativo afirmativo, sem atrativa: ênclise.")
q(1,"Em “Saiu, deixando-o sozinho na praça”, o pronome está em ênclise porque",["o verbo está no gerúndio, sem palavra atrativa.","o verbo está no futuro.","há palavra negativa antes do verbo.","o verbo está no particípio.","a frase é interrogativa."],"Gerúndio sem “em” pede ênclise.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Quem te contou sobre a operação?","Quem contou-te sobre a operação?","Quem contou te sobre a operação?","Te quem contou sobre a operação?","Quem contar-te-ia-ou sobre a operação?"],"Frase interrogativa com pronome interrogativo pede próclise.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Alguém me chamou no rádio.","Alguém chamou-me no rádio.","Alguém chamou me no rádio.","Me alguém chamou no rádio.","Alguém me chamou-me no rádio."],"O indefinido “alguém” atrai.")
q(1,"A forma de “entregar + o” de acordo com a norma-padrão é",["entregá-lo","entregar-o","entregar-lo","entregá-o","entrega-lo"],"O -r cai e o pronome vira “lo”; a última sílaba ganha acento.")
q(1,"A forma de “encontraram + o” de acordo com a norma-padrão é",["encontraram-no","encontraram-o","encontraram-lo","encontrara-no","encontraram-lhe"],"Depois de som nasal, o pronome vira “no”.")
q(1,"A forma de “fiz + o” de acordo com a norma-padrão é",["fi-lo","fiz-o","fiz-lo","fi-o","fizo"],"O -z cai e o pronome vira “lo”.")
q(1,"Assinale a frase em que o pronome está em ênclise.",["Aproximou-se do suspeito com calma.","Não se aproximou do suspeito.","Ninguém se aproximou do suspeito.","Quando se aproximou, viu a arma.","Aproximar-se-á do suspeito."],"O pronome está depois do verbo, com hífen.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Tudo se resolveu no fim do turno.","Tudo resolveu-se no fim do turno.","Tudo resolveu se no fim do turno.","Se tudo resolveu no fim do turno.","Tudo se resolveu-se no fim do turno."],"O indefinido “tudo” atrai.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Aqui se trabalha em silêncio.","Aqui trabalha se em silêncio.","Se aqui trabalha em silêncio.","Aqui se trabalha-se em silêncio.","Aqui trabalhar-se-ia-á em silêncio."],"O advérbio, sem vírgula depois, atrai o pronome.")
q(1,"Com o verbo no futuro do presente, sem palavra atrativa e no início da frase, a colocação de acordo com a norma-padrão é",["a mesóclise: entregar-lhe-ei.","a ênclise: entregarei-lhe.","a próclise: lhe entregarei.","qualquer uma das três.","nenhuma: o pronome deve ser omitido."],"Futuro sem atrativa, abrindo a frase: mesóclise.")
q(1,"Assinale a frase de acordo com a norma-padrão.",["Tinha-me avisado da escala.","Tinha avisado-me da escala.","Tinha avisado me da escala.","Me tinha avisado-me da escala.","Tinha-me avisado-me da escala."],"Nunca há pronome depois do particípio.")
q(1,"Em “Deus o acompanhe!”, a próclise ocorre porque a frase",["exprime desejo.","está no futuro.","começa com verbo.","tem verbo no gerúndio.","tem verbo no particípio."],"Frases de desejo (optativas) pedem próclise.")
q(1,"No terceiro parágrafo, a forma “Encaminhá-lo-ão” é exemplo de",["mesóclise com o verbo no futuro do presente.","ênclise com o verbo no infinitivo.","próclise com palavra atrativa.","erro de colocação, pois o certo seria “encaminharão-lo”.","mesóclise com o verbo no pretérito."],"Encaminharão + o: o pronome entra no meio do futuro, na forma “lo”.","tq")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Não lhe entregarei o relatório.","Não entregar-lhe-ei o relatório.","Não entregarei-lhe o relatório.","Entregarei-lhe não o relatório.","Não entregarei lhe o relatório."],"Com palavra atrativa, o futuro fica com próclise.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Far-se-ia a vistoria se houvesse tempo.","Faria-se a vistoria se houvesse tempo.","Se faria-se a vistoria se houvesse tempo.","Fazer-se-ia-se a vistoria.","Faria se a vistoria se houvesse tempo."],"Futuro do pretérito, sem atrativa, abrindo a frase: mesóclise.")
q(2,"Assinale a frase em que a colocação está INCORRETA.",["Ontem encontrei-o na praça.","Ontem o encontrei na praça.","Ontem, encontrei-o na praça.","Encontrei-o ontem na praça.","Não o encontrei ontem na praça."],"Advérbio sem vírgula atrai: ontem o encontrei.")
q(2,"Em “Ontem, encontrei-o na praça”, a ênclise é possível porque",["a vírgula depois do advérbio desfaz a atração.","o verbo está no futuro.","há palavra negativa.","o pronome é reflexivo.","a frase é exclamativa."],"A pausa marcada pela vírgula desfaz a atração do advérbio.")
q(2,"Assinale a locução verbal com colocação de acordo com a norma-padrão.",["Vou-lhe entregar o relatório.","Lhe vou entregar o relatório.","Vou entregar-lhe-ei o relatório.","Vou-lhe entregar-lhe o relatório.","Vou lhe-entregar o relatório."],"Na locução com infinitivo, o pronome pode ficar depois do auxiliar, com hífen.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Não lhe vou entregar o relatório.","Não vou-lhe entregar o relatório.","Lhe não vou entregar o relatório.","Não vou entregar-lhe-ei o relatório.","Não vou lhe-entregar o relatório."],"Com palavra atrativa, o pronome vai antes do auxiliar (ou depois do principal).")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Os agentes tinham-se preparado para a operação.","Os agentes tinham preparado-se para a operação.","Os agentes tinham preparado se para a operação.","Os agentes se tinham preparado-se para a operação.","Os agentes tinham-se preparado-se para a operação."],"Com particípio, o pronome fica junto do auxiliar.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["É preciso avisá-lo da mudança.","É preciso avisar-lo da mudança.","É preciso avisar-o da mudança.","É preciso avisá-o da mudança.","É preciso avisa-lo da mudança."],"Avisar + o = avisá-lo.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Em se tratando de segurança, todo cuidado é pouco.","Em tratando-se de segurança, todo cuidado é pouco.","Em tratando se de segurança, todo cuidado é pouco.","Se em tratando de segurança, todo cuidado é pouco.","Em tratar-se-ia de segurança, todo cuidado é pouco."],"Em + gerúndio pede próclise.")
q(2,"Assinale a frase de acordo com a norma-padrão.",["Embora se esforçasse, não alcançou a meta.","Embora esforçasse-se, não alcançou a meta.","Embora esforçasse se, não alcançou a meta.","Se embora esforçasse, não alcançou a meta.","Embora se esforçasse-se, não alcançou a meta."],"A conjunção subordinativa atrai.")
q(2,"A forma de “põe + o” de acordo com a norma-padrão é",["põe-no","põe-o","põe-lo","pô-lo","põe-lho"],"Depois de som nasal, “no”. “Pô-lo” é a forma de “pôr + o”.")
q(2,"A forma de “queremos + o” de acordo com a norma-padrão é",["queremo-lo","queremos-o","queremos-lo","queremo-no","querêmo-lo"],"O -s cai e o pronome vira “lo”.")
q(2,"Assinale a alternativa em que a combinação está de acordo com a norma-padrão.",["Ele fê-lo sem ajuda. (fez + o)","Ele fez-lo sem ajuda.","Ele fê-o sem ajuda.","Ele fez-o sem ajuda.","Ele fe-lo sem ajuda."],"Fez + o = fê-lo, com acento.")
q(2,"Assinale a frase em que a próclise é obrigatória.",["Jamais o abandonaremos.","Os guardas o abandonaram.","Abandonaram-no ontem.","Abandoná-lo-emos.","Vamos abandoná-lo."],"A palavra negativa “jamais” obriga a próclise. Em (B), com sujeito expresso, a próclise é apenas aceita.")
q(2,"Em “Os guardas se aproximaram com calma”, a próclise é",["aceita, pois com o sujeito expresso antes do verbo a próclise e a ênclise são possíveis.","obrigatória, por causa de palavra negativa.","proibida, pois a frase começa com pronome.","obrigatória, por causa do pronome relativo.","proibida, pois o verbo está no pretérito."],"Sem palavra atrativa e com sujeito expresso, as duas posições são aceitas.")
q(2,"Assinale a frase em que a colocação está INCORRETA.",["Me avisaram tarde da mudança na escala.","Avisaram-me tarde da mudança na escala.","Não me avisaram da mudança na escala.","Avisar-me-ão da mudança na escala.","Quem me avisou da mudança na escala?"],"A norma-padrão não inicia frase com pronome átono.")
q(2,"Assinale a frase em que a colocação está INCORRETA.",["Entregarei-lhe a chave amanhã.","Entregar-lhe-ei a chave amanhã.","Não lhe entregarei a chave amanhã.","Eu lhe entregarei a chave amanhã.","Vou entregar-lhe a chave amanhã."],"O futuro nunca aceita ênclise.")
q(2,"Em “Que Deus nos proteja nesta operação!”, a colocação do pronome se explica por",["tratar-se de frase que exprime desejo.","haver verbo no futuro.","haver verbo no gerúndio.","haver vírgula antes do pronome.","haver verbo no imperativo afirmativo."],"Frase de desejo pede próclise.")
q(2,"No segundo parágrafo, em “até que se lembrasse do nome da filha”, a próclise ocorre porque",["a conjunção subordinativa atrai o pronome.","o verbo está no futuro.","a frase é imperativa.","o verbo está no gerúndio.","há vírgula antes do pronome."],"“Até que” é locução conjuntiva subordinativa.","tq")
q(2,"No segundo parágrafo, em “Não se sabe ainda como ele chegou ao centro”, a colocação do pronome se deve",["à palavra negativa “não”.","ao advérbio “ainda”.","ao verbo no futuro.","ao início da frase.","ao gerúndio."],"A negativa atrai o pronome.","tq")
q(3,"No primeiro parágrafo, em “Os guardas avistaram-no”, a forma “no” aparece porque",["o verbo termina em som nasal.","o verbo termina em -r.","o verbo está no futuro.","o pronome é reflexivo.","o pronome é objeto indireto."],"Avistaram termina em som nasal: o pronome “o” vira “no”.","tq")
q(3,"No terceiro parágrafo, em “nunca se esquecerá do cuidado”, a próclise é obrigatória, e a mesóclise não seria possível, porque",["a palavra negativa “nunca” atrai o pronome para antes do verbo.","o verbo está no presente.","o pronome é objeto direto.","a frase é interrogativa.","o sujeito está oculto."],"Com palavra atrativa, o futuro fica com próclise.","tq")
q(3,"No segundo parágrafo, em “ofereceu-lhe água”, o pronome “lhe” se refere a",["o idoso.","a equipe.","a filha.","a água.","a corporação."],"A equipe ofereceu água ao idoso.","tq")
q(3,"Se o último período do texto começasse por “Não”, a forma de acordo com a norma-padrão seria",["Não o encaminharão, nos próximos dias, a uma avaliação médica.","Não encaminhá-lo-ão, nos próximos dias, a uma avaliação médica.","Não encaminharão-no, nos próximos dias, a uma avaliação médica.","Não encaminharão-o, nos próximos dias, a uma avaliação médica.","Não o encaminhá-lo-ão, nos próximos dias, a uma avaliação médica."],"Com a negativa, a mesóclise dá lugar à próclise.","tq")
q(3,"Assinale a alternativa em que as duas colocações estão de acordo com a norma-padrão.",["Vou entregar-lhe o relatório. / Vou-lhe entregar o relatório.","Tinha avisado-me. / Tinha-me avisado.","Entregarei-lhe. / Entregar-lhe-ei.","Me diga. / Diga-me.","Ninguém avisou-me. / Ninguém me avisou."],"Na locução com infinitivo, o pronome pode ficar depois do auxiliar ou do principal.")
q(3,"Assinale a frase em que a colocação está INCORRETA.",["Os documentos que entregaram-me estavam incompletos.","Os documentos que me entregaram estavam incompletos.","Entregaram-me documentos incompletos.","Não me entregaram os documentos.","Entregar-me-ão os documentos amanhã."],"O relativo “que” atrai: que me entregaram.")
q(3,"Assinale a frase em que a ênclise é obrigatória.",["Disseram-me que a escala mudou.","Não me disseram que a escala mudou.","Quem me disse que a escala mudou?","Ninguém me disse que a escala mudou.","Quando me disseram, já era tarde."],"Verbo no início da frase, sem atrativa: ênclise obrigatória.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["Ter-se-ia evitado o acidente com sinalização.","Teria-se evitado o acidente com sinalização.","Se teria evitado-se o acidente com sinalização.","Ter-se-ia-se evitado o acidente.","Teria evitado-se o acidente com sinalização."],"Auxiliar no futuro do pretérito, sem atrativa, abrindo a frase: mesóclise no auxiliar.")
q(3,"Assinale a frase em que a colocação dos pronomes está de acordo com a norma-padrão.",["Tudo se resolveu quando o encontramos.","Tudo resolveu-se quando encontramo-lo.","Tudo se resolveu quando encontramo-lo.","Tudo resolveu-se quando o encontramos.","Se tudo resolveu quando o encontramos."],"“Tudo” e “quando” atraem os dois pronomes.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["Abordamo-lo na saída do terminal.","Abordamos-lo na saída do terminal.","Abordamos-o na saída do terminal.","Abordamo-o na saída do terminal.","Abordámo-no na saída do terminal."],"Abordamos + o: o -s cai e o pronome vira “lo”.")
q(3,"Assinale a alternativa em que o pronome “o” assume a forma “lo”.",["Vamos vendê-lo no leilão.","Venderam-no no leilão.","Vendem-no no leilão.","Vendeu-o no leilão.","Não o venderam no leilão."],"Vender + o = vendê-lo (o -r cai).")
q(3,"Assinale a frase em que a colocação está INCORRETA.",["Tinha esquecido-me do crachá.","Tinha-me esquecido do crachá.","Não me tinha esquecido do crachá.","Eu me tinha esquecido do crachá.","Esquecera-me do crachá."],"Nunca há pronome depois do particípio.")
q(3,"Assinale a frase em que há próclise obrigatória por causa de pronome indefinido.",["Alguém nos avisou da blitz.","Não nos avisaram da blitz.","Quando nos avisaram da blitz, já era tarde.","O agente que nos avisou da blitz saiu.","Avisaram-nos da blitz."],"Em (A), a atração vem do indefinido “alguém”. Nas demais, de negativa, conjunção e relativo, ou não há próclise.")
q(3,"Assinale a frase em que há próclise obrigatória por causa de conjunção subordinativa.",["Se o virem, avisem a central.","Não o viram na praça.","Alguém o viu na praça.","O agente que o viu avisou a central.","Viram-no na praça."],"O “se” condicional é conjunção subordinativa.")
q(3,"Assinale a frase de acordo com a norma-padrão.",["Dir-se-ia que ninguém viu nada.","Diria-se que ninguém viu nada.","Se diria-se que ninguém viu nada.","Dizer-se-ia-se que ninguém viu nada.","Diria se que ninguém viu nada."],"Futuro do pretérito, sem atrativa, abrindo a frase: mesóclise.")
q(3,"Assinale a alternativa em que a colocação admite as duas formas.",["Eu o vi. / Eu vi-o.","Não o vi. / Não vi-o.","Quem o viu? / Quem viu-o?","Vê-lo-ei. / Verei-o.","Ninguém o viu. / Ninguém viu-o."],"Com sujeito expresso e sem atrativa, próclise e ênclise são aceitas.")
q(3,"Assinale a frase em que a colocação está INCORRETA.",["Quanto custou-me aquela multa!","Quanto me custou aquela multa!","Aquela multa custou-me caro.","Não me custou caro aquela multa.","Custar-me-ia caro aquela multa."],"Frase exclamativa com “quanto” pede próclise.")
q(3,"Assinale a frase em que a ênclise contraria a norma-padrão.",["Ninguém respondeu-me na central.","Responderam-me na central.","Ontem, responderam-me na central.","Responda-me pelo rádio.","Ao responder-me, saiu da sala."],"“Ninguém” atrai: ninguém me respondeu.")
q(3,"Assinale a afirmação INCORRETA sobre colocação pronominal.",["A mesóclise pode ocorrer com qualquer tempo verbal.","A norma-padrão não inicia frase com pronome oblíquo átono.","Palavras negativas atraem o pronome para antes do verbo.","Não há ênclise depois de particípio.","Com o futuro, sem palavra atrativa, usa-se a mesóclise."],"A mesóclise só ocorre com o futuro do presente e o futuro do pretérito.")
q(3,"Assinale a alternativa em que todas as frases seguem a norma-padrão.",["Não me avisaram; avisar-me-ão amanhã; diga-me a hora.","Não avisaram-me; avisar-me-ão amanhã; diga-me a hora.","Não me avisaram; me avisarão amanhã; diga-me a hora.","Não me avisaram; avisarão-me amanhã; diga-me a hora.","Não me avisaram; avisar-me-ão amanhã; me diga a hora."],"Negativa com próclise; futuro sem atrativa com mesóclise; imperativo com ênclise.")
tq="<strong>Guarda encontra idoso desaparecido</strong><br><br>Um idoso de 78 anos que estava desaparecido desde a manhã de domingo foi encontrado por agentes da Guarda Municipal na tarde de ontem. Os guardas avistaram-no sentado em um banco da praça central, confuso e com frio.<br><br>Segundo a corporação, a equipe aproximou-se com calma, ofereceu-lhe água e conversou com ele até que se lembrasse do nome da filha. Não se sabe ainda como ele chegou ao centro.<br><br>A família agradeceu aos agentes e disse que nunca se esquecerá do cuidado com que o idoso foi tratado. Encaminhá-lo-ão, nos próximos dias, a uma avaliação médica."
code,svg=mapa("Primeiro procure a palavra que atrai; sem ela, olhe o tempo do verbo",[
 ("proclise","Próclise: antes",["não, nunca, ninguém, tudo","que, quem; quando, se, embora","perguntas, exclamações, desejos"],"seção 2"),
 ("enclise","Ênclise: depois",["início de frase: diga-me","imperativo: entregue-me","gerúndio; depois de vírgula"],"seção 3"),
 ("mesoclise","Mesóclise: no meio",["só futuro do presente","e futuro do pretérito","entregar-lhe-ei; far-se-ia"],"seção 4"),
 ("locucao","Locuções verbais",["vou-lhe entregar","vou entregar-lhe","tinha-me avisado"],"seção 5"),
 ("formas","Lo, la, no, na",["entregá-lo; fi-lo; fê-lo","encontraram-no; põe-no","queremo-lo; abordamo-lo"],"seção 6"),
 ("proibido","O que nunca se faz",["começar frase com me","entregarei-lhe; faria-se","tinha avisado-me"],"seções 3 a 5")],
 "Na prova: palavra atrativa decide antes de tudo; sem ela, valem o tempo verbal e o início da frase")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,'QR',8,9,10],QR,7,svg,"Os três primeiros grupos são as posições; os três últimos, os casos que mais caem.","Fontes: Edital 02/2026, Anexo I. Referências de base: Bechara, <em>Moderna Gramática Portuguesa</em>; Cunha e Cintra, <em>Nova Gramática do Português Contemporâneo</em>. Exemplos criados para a aula.")
revisao("pt-11",'Colocação pronominal',Q,{'tq':tq},pendencias=["Aula escrita antes do padrão de revisão: não há registro do que foi conferido na fonte. Conferir exemplos e regras contra Bechara e Cunha e Cintra."])
gravar("pt-11",aula_html,banco("pt-11",Q),{"tq":tq})
print(len(aula_html)); print(QRF)
