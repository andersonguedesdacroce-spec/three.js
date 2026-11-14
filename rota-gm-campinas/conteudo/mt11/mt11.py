import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
import itertools
imp=lambda a,b: (not a) or b
def eq(f,g,n=2): return all(f(*v)==g(*v) for v in itertools.product([True,False],repeat=n))
def taut(f,n=2): return all(f(*v) for v in itertools.product([True,False],repeat=n))
LEAD="Estruturas lógicas e lógica de argumentação é a parte da prova em que não há número para calcular, e sim afirmações para analisar. A Vunesp cobra quatro habilidades: reconhecer proposições e seus valores lógicos, operar com os conectivos (e, ou, se...então, se e somente se), negar e reescrever proposições de forma equivalente e decidir se um argumento é válido. A chave é a tabela-verdade e algumas regras de negação que valem decorar, porque elas resolvem a maioria das questões em segundos."
S={}
S[1]="""## 1. Proposições

Proposição é uma frase declarativa, à qual se pode atribuir o valor lógico verdadeiro (V) ou falso (F), mas nunca os dois. “Campinas é uma cidade paulista” é proposição verdadeira; “2 + 2 = 5” é proposição falsa. Não são proposições as perguntas (“Que horas são?”), as ordens (“Feche a porta”), as exclamações (“Que bom!”) e as sentenças abertas, em que o valor depende de uma variável não definida (“x + 2 = 5”).

A negação de uma proposição p, escrita ¬p (“não p”), inverte o valor: se p é verdadeira, ¬p é falsa, e vice-versa. A negação de “O guarda está de serviço” é “O guarda não está de serviço”. Negar duas vezes volta ao início: ¬(¬p) = p. Uma proposição que contém outras ligadas por conectivos é composta; as que não contêm são simples.
"""
S[2]="""## 2. Conectivos e tabelas-verdade

Os conectivos ligam proposições. A conjunção “p e q” (p ∧ q) é verdadeira só quando as duas são verdadeiras. A disjunção “p ou q” (p ∨ q) é falsa só quando as duas são falsas; é o “ou” inclusivo, que admite as duas verdadeiras. A disjunção exclusiva “ou p ou q” é verdadeira quando exatamente uma delas é. O condicional “se p, então q” (p → q) é falso só quando p é verdadeira e q é falsa: a promessa só é quebrada se a condição ocorre e o resultado não. O bicondicional “p se e somente se q” (p ↔ q) é verdadeiro quando p e q têm o mesmo valor.

A tabela-verdade reúne todas as combinações de valores. Com duas proposições há 4 linhas; com três, 8; com n, 2<sup>n</sup>.

| p | q | p ∧ q | p ∨ q | p → q | p ↔ q |
| --- | --- | --- | --- | --- | --- |
| V | V | V | V | V | V |
| V | F | F | V | F | F |
| F | V | F | V | V | F |
| F | F | F | F | V | V |

O condicional intriga porque é verdadeiro quando p é falsa. A razão é a da promessa: “Se chover, levo guarda-chuva” não é quebrada num dia de sol, qualquer que seja o que eu faça. Só se chover e eu esquecer o guarda-chuva, a frase é falsa.

Uma proposição composta que é verdadeira em todas as linhas é uma tautologia, como p ∨ ¬p. Se é falsa em todas, é uma contradição, como p ∧ ¬p. Nos demais casos, é uma contingência.
"""
S[3]="""## 3. Negações

As negações são o ponto mais cobrado. As leis de De Morgan mostram que a negação troca o conectivo: ¬(p ∧ q) = ¬p ∨ ¬q e ¬(p ∨ q) = ¬p ∧ ¬q. A negação de “Ana é guarda e Bruno é fiscal” é “Ana não é guarda ou Bruno não é fiscal”. A negação de “Ana é guarda ou Bruno é fiscal” é “Ana não é guarda e Bruno não é fiscal”.

A negação do condicional é “p e não q”, porque a única forma de o condicional ser falso é p verdadeira e q falsa: ¬(p → q) = p ∧ ¬q. A negação de “Se chove, a rua molha” é “Chove e a rua não molha”. A negação do bicondicional é o “ou exclusivo”.

Com os quantificadores, a regra é trocar “todo” por “algum... não”, e “algum” por “nenhum”. A negação de “Todo guarda é pontual” é “Algum guarda não é pontual”. A negação de “Algum guarda usa óculos” é “Nenhum guarda usa óculos”. A negação de “Nenhum guarda é pontual” é “Algum guarda é pontual”.
"""
S[4]="""## 4. Equivalências

Duas proposições são equivalentes quando têm a mesma tabela-verdade. As equivalências do condicional resolvem muitas questões: “se p, então q” é equivalente à sua contrapositiva, “se não q, então não p”, e também a “não p ou q”. “Se estudo, passo” equivale a “Se não passei, então não estudei” e a “Não estudo ou passo”.

Atenção para o que não é equivalente: a recíproca, “se q, então p”, e a inversa, “se não p, então não q”, não equivalem ao condicional original. “Se chove, a rua molha” não significa que, se a rua molhou, choveu: pode ter sido um caminhão-pipa.

As demais equivalências úteis são as de De Morgan (seção 3), a dupla negação e a absorção: p ∧ (p ∨ q) equivale a p.
"""
S[5]="""## 5. Argumentos

Um argumento é um conjunto de premissas (afirmações dadas como verdadeiras) e uma conclusão. O argumento é válido quando, sendo todas as premissas verdadeiras, a conclusão não pode ser falsa. Validade não é verdade: um argumento pode ser válido com premissas falsas, e a prova só pergunta se a conclusão decorre das premissas.

Duas formas válidas aparecem sempre. A primeira é o modus ponens: “Se p, então q; p; logo q.” Se o alarme dispara, a equipe é acionada; o alarme disparou; logo a equipe foi acionada. A segunda é o modus tollens: “Se p, então q; não q; logo não p.” Se a equipe não foi acionada, o alarme não disparou. Há também o silogismo hipotético: “se p, então q; se q, então r; logo, se p, então r.”

Duas formas parecem válidas, mas são falácias. A afirmação do consequente: “Se p, então q; q; logo p.” Se o alarme dispara, a equipe é acionada; a equipe foi acionada; logo o alarme disparou? Não, a equipe pode ter sido acionada por outro motivo. A negação do antecedente: “Se p, então q; não p; logo não q.” Se o alarme não disparou, a equipe pode ainda ter sido acionada por outra via.

Nos silogismos com quantificadores, “Todo A é B; todo B é C; logo todo A é C” é válido. Com “algum”, é preciso cuidado: “Todo guarda é treinado; algum treinado é jovem” não leva a nenhuma conclusão sobre guardas jovens.

Exemplo resolvido, de quem disse a verdade. Três guardas, Ana, Bruno e Carla, discutem quem deixou uma viatura ligada. Ana diz: “Foi Bruno.” Bruno diz: “Foi Ana.” Carla diz: “Foi Ana.” Só um disse a verdade. Teste cada culpado. Se foi Ana, Bruno e Carla dizem a verdade, dois verdadeiros, o que não serve. Se foi Carla, ninguém diz a verdade, o que também não serve. Se foi Bruno, só Ana diz a verdade: um verdadeiro, como o enunciado pede. O culpado é Bruno.
"""
S[7]="""## 7. Na rotina do guarda

- **Regulamentos:** “Se ocorre X, então o guarda deve fazer Y” é um condicional; saber a contrapositiva ajuda a aplicar a regra no sentido inverso.
- **Depoimentos:** quando as versões se contradizem, o método do culpado hipotético permite descobrir quem mentiu.
- **Relatórios:** negar uma afirmação do relato (“todos estavam armados”) exige a negação correta (“algum não estava armado”).
- **Ofícios e ordens de serviço:** “e” e “ou” mudam o alcance da ordem e pedem leitura atenta.
"""
S[8]="""## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Negar “todo” como “nenhum” | A negação de “todo” é “algum não” |
| Negar “e” mantendo o “e” | De Morgan: a negação troca e por ou |
| Negar “se p então q” como “se p então não q” | A negação é “p e não q” |
| Tomar a recíproca pela contrapositiva | Contrapositiva: “se não q, então não p” |
| Concluir de “se p então q” e “q” que p | É a falácia da afirmação do consequente |
| Achar que condicional com p falso é falso | Com p falso o condicional é verdadeiro |
| Confundir validade com verdade | Válido é a conclusão decorrer das premissas |
"""
S[9]="""## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Proposição | Declarativa, verdadeira ou falsa |
| Conjunção | Verdadeira só se as duas forem verdadeiras |
| Disjunção | Falsa só se as duas forem falsas |
| Condicional | Falso só se p verdadeiro e q falso |
| Negação do e / ou | De Morgan: troca o conectivo e nega as partes |
| Negação do condicional | p e não q |
| Negação de todo / algum | Algum não / nenhum |
| Equivalente do condicional | Contrapositiva e “não p ou q” |
| Argumento válido | Modus ponens e modus tollens |
| Linhas da tabela | 2 elevado ao número de proposições |
"""
assert eq(lambda p,q: imp(p,q), lambda p,q: (not p) or q) and eq(lambda p,q: imp(p,q), lambda p,q: imp(not q,not p))
assert eq(lambda p,q: not (p and q), lambda p,q: (not p) or (not q)) and eq(lambda p,q: not imp(p,q), lambda p,q: p and (not q))
assert taut(lambda p: p or not p,1) and not any(p and not p for p in (True,False))
assert not eq(lambda p,q: imp(p,q), lambda p,q: imp(q,p))
def val(w,x,cul): return (cul==x)
sol=[c for c in 'ABC' if sum([val('A','B',c),val('B','A',c),val('C','A',c)])==1]; assert sol==['B']
QR=[("Questão 1","A negação da proposição “Se chove, então a rua molha” é",["Chove e a rua não molha.","Não chove e a rua molha.","Se não chove, então a rua não molha.","Se a rua molha, então chove.","Não chove ou a rua não molha."],0,"A negação do condicional é “p e não q”: chove e a rua não molha."),
("Questão 2","Todo guarda é pontual. A negação dessa afirmação é",["Algum guarda não é pontual.","Nenhum guarda é pontual.","Todo guarda é impontual.","Algum guarda é pontual.","Nem todo guarda é pontual, mas alguns são."],0,"Negação de “todo” é “algum não”. “Nenhum” é uma afirmação mais forte que a negação."),
("Questão 3","Sabe-se que “se o alarme dispara, a equipe é acionada” é verdadeira e que a equipe não foi acionada. Conclui-se que",["o alarme não disparou.","o alarme disparou.","a equipe foi acionada por outro motivo.","nada se pode concluir.","a regra é falsa."],0,"Modus tollens: se p então q; não q; logo não p."),
("Questão 4","Em uma tabela-verdade com três proposições simples, o número de linhas é",["8","6","9","3","4"],0,"2 × 2 × 2 = 8.")]
QR=[(a,b,c,[2,4,1,3][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
QRF=qr_md(QR,6)
t1="<strong>Regra do plantão</strong><br><br>O regulamento do plantão da Guarda Municipal de Vila Nova, cidade fictícia, diz: “Se o alarme dispara, então a equipe é acionada.” Em uma noite de plantão, o alarme disparou."
t2="<strong>A viatura ligada</strong><br><br>Três guardas, Ana, Bruno e Carla, foram questionados sobre quem deixou uma viatura ligada. Ana disse: “Foi Bruno.” Bruno disse: “Foi Ana.” Carla disse: “Foi Ana.” Sabe-se que apenas um deles disse a verdade e que um dos três é o culpado."
tx={"mt11a":t1,"mt11b":t2}
# n=1
q(1,"Entre as frases abaixo, a que é uma proposição é",["Campinas é uma cidade paulista.","Que horas são?","Feche a porta.","Que dia lindo!","x + 2 = 5"],"Só a primeira é declarativa e tem valor lógico definido.")
q(1,"A negação de “O guarda está de serviço” é",["O guarda não está de serviço.","O guarda está de folga.","O guarda está de serviço e de folga.","Todo guarda está de serviço.","Nenhum guarda está de serviço."],"A negação simples acrescenta “não” ao verbo.")
q(1,"A proposição “p e q” é verdadeira quando",["p e q são verdadeiras.","p é verdadeira.","q é verdadeira.","ao menos uma é verdadeira.","p e q são falsas."],"A conjunção exige as duas verdadeiras.")
q(1,"A proposição “p ou q” é falsa quando",["p e q são falsas.","p é falsa.","q é falsa.","p é falsa e q é verdadeira.","ao menos uma é falsa."],"A disjunção só é falsa se as duas forem.")
q(1,"A proposição “se p, então q” é falsa quando",["p é verdadeira e q é falsa.","p é falsa e q é verdadeira.","p e q são falsas.","p e q são verdadeiras.","p é falsa."],"A promessa só é quebrada com p verdadeira e q falsa.")
q(1,"A negação de “Todo guarda é pontual” é",["Algum guarda não é pontual.","Nenhum guarda é pontual.","Todo guarda é impontual.","Algum guarda é pontual.","Todo guarda não é pontual."],"Troca-se “todo” por “algum... não”.")
q(1,"A negação de “Algum policial é jovem” é",["Nenhum policial é jovem.","Algum policial não é jovem.","Todo policial é jovem.","Todo policial não é jovem, mas alguns são.","Algum policial é velho."],"A negação de “algum” é “nenhum”.")
q(1,"O valor lógico de “V ∧ F” é",["falso.","verdadeiro.","indeterminado.","verdadeiro e falso.","contingente."],"Conjunção exige as duas verdadeiras.")
q(1,"O valor lógico de “V ∨ F” é",["verdadeiro.","falso.","indeterminado.","contraditório.","nulo."],"Disjunção só é falsa com as duas falsas.")
q(1,"Em “Se chove, então a rua molha”, o antecedente é",["Chove.","A rua molha.","Não chove.","A rua não molha.","Se chove."],"O antecedente é a parte depois do “se”.")
q(1,"A contrapositiva de “se p, então q” é",["se não q, então não p.","se q, então p.","se não p, então não q.","p e não q.","não p ou não q."],"Troca-se e nega-se: se não q, então não p.")
q(1,"A negação da proposição falsa “2 + 2 = 5” é",["verdadeira.","falsa.","contraditória.","indeterminada.","uma tautologia."],"Negando uma falsa, obtém-se uma verdadeira.")
q(1,"Uma tabela-verdade com três proposições simples tem",["8 linhas.","6 linhas.","9 linhas.","3 linhas.","4 linhas."],"2<sup>3</sup> = 8.")
q(1,"A proposição “p ↔ q” é verdadeira quando",["p e q têm o mesmo valor lógico.","p é verdadeira.","q é verdadeira.","p e q têm valores diferentes.","p é falsa."],"O bicondicional exige valores iguais.")
q(1,"Uma tautologia é uma proposição",["sempre verdadeira.","sempre falsa.","às vezes verdadeira.","sem valor lógico.","que só tem conectivo “ou”."],"Verdadeira em todas as linhas da tabela.")
q(1,"Uma contradição é uma proposição",["sempre falsa.","sempre verdadeira.","às vezes falsa.","sem valor lógico.","que usa a negação."],"Falsa em todas as linhas da tabela.")
q(1,"Entre as frases abaixo, a que NÃO é uma proposição é",["Feche a porta.","Campinas fica em São Paulo.","3 é maior que 5.","O Brasil é um país.","10 é um número par."],"Uma ordem não tem valor lógico.")
q(1,"A disjunção exclusiva “ou p ou q” é verdadeira quando",["exatamente uma delas é verdadeira.","as duas são verdadeiras.","as duas são falsas.","pelo menos uma é verdadeira.","p é falsa."],"Ou uma, ou outra, mas não as duas.")
q(1,"Segundo o texto, pode-se concluir, naquela noite, que",["a equipe foi acionada.","a equipe não foi acionada.","o alarme não disparou.","a regra é falsa.","nada se pode concluir."],"Modus ponens: se p então q; p; logo q.","mt11a")
q(1,"No regulamento do texto, o antecedente do condicional é",["O alarme dispara.","A equipe é acionada.","O plantão.","O regulamento.","A equipe não é acionada."],"O antecedente vem depois do “se”.","mt11a")
# n=2
q(2,"A negação de “Se chove, a rua molha” é",["Chove e a rua não molha.","Não chove e a rua molha.","Se não chove, a rua não molha.","Se a rua molha, chove.","Não chove ou a rua não molha."],"¬(p → q) = p ∧ ¬q.")
q(2,"A negação de “Ana é guarda e Bruno é fiscal” é",["Ana não é guarda ou Bruno não é fiscal.","Ana não é guarda e Bruno não é fiscal.","Ana é guarda ou Bruno é fiscal.","Se Ana é guarda, Bruno não é fiscal.","Ana não é guarda ou Bruno é fiscal."],"De Morgan: a negação do “e” é o “ou” das negações.")
q(2,"A negação de “Ana é guarda ou Bruno é fiscal” é",["Ana não é guarda e Bruno não é fiscal.","Ana não é guarda ou Bruno não é fiscal.","Ana é guarda e Bruno é fiscal.","Se Ana não é guarda, Bruno é fiscal.","Ana não é guarda ou Bruno é fiscal."],"De Morgan: a negação do “ou” é o “e” das negações.")
q(2,"Uma proposição equivalente a “Se estudo, passo” é",["Se não passei, não estudei.","Se passei, estudei.","Se não estudo, não passo.","Estudo e não passo.","Passo e não estudo."],"A contrapositiva é equivalente. A recíproca e a inversa não são.")
q(2,"Sabe-se que “se estudo, passo” é verdadeira e que passei. Pode-se concluir que",["nada se pode concluir sobre o estudo.","estudei.","não estudei.","a frase é falsa.","passei sem estudar."],"Afirmação do consequente: não permite concluir o antecedente.")
q(2,"Sabe-se que “se estudo, passo” é verdadeira e que não passei. Conclui-se que",["não estudei.","estudei.","passei por outro motivo.","nada se pode concluir.","a frase é falsa."],"Modus tollens.")
q(2,"O valor lógico de “(V ∧ F) ∨ V” é",["verdadeiro.","falso.","contraditório.","indeterminado.","depende de V."],"(F) ∨ V = V.")
q(2,"O valor lógico de “se F, então V” é",["verdadeiro.","falso.","indeterminado.","nulo.","depende do contexto."],"Com antecedente falso, o condicional é verdadeiro.")
q(2,"Na tabela-verdade de “p ∨ q”, o número de linhas em que o resultado é verdadeiro é",["3","1","2","4","0"],"Só é falso quando p e q são falsos.")
q(2,"Se a proposição “p → q” é falsa, então",["p é verdadeira e q é falsa.","p é falsa e q é verdadeira.","p e q são verdadeiras.","p e q são falsas.","p é falsa."],"A única linha falsa do condicional.")
q(2,"A negação de “Nenhum guarda é pontual” é",["Algum guarda é pontual.","Todo guarda é pontual.","Algum guarda não é pontual.","Todo guarda é impontual.","Nenhum guarda é impontual."],"Negação de “nenhum” é “algum”.")
q(2,"A negação de “Existe guarda que usa óculos” é",["Nenhum guarda usa óculos.","Todo guarda usa óculos.","Algum guarda não usa óculos.","Existe guarda que não usa óculos.","Todo guarda é míope."],"Negação de “existe” é “nenhum”.")
q(2,"A proposição “p ∧ ¬p” é",["uma contradição.","uma tautologia.","uma contingência.","equivalente a p.","equivalente a ¬p."],"Nunca pode ser verdadeira.")
q(2,"A proposição “p ∨ ¬p” é",["uma tautologia.","uma contradição.","uma contingência.","equivalente a p.","falsa quando p é falsa."],"Sempre verdadeira.")
q(2,"A proposição “se p, então q” é equivalente a",["não p ou q.","p ou não q.","p e não q.","não p e q.","p e q."],"p → q equivale a ¬p ∨ q.")
q(2,"A proposição “p ↔ q” é falsa quando",["p e q têm valores diferentes.","p e q são verdadeiras.","p e q são falsas.","p é verdadeira.","q é falsa."],"O bicondicional exige valores iguais.")
q(2,"Em uma tabela-verdade com três proposições, o número de linhas é",["8","6","9","3","12"],"2<sup>3</sup> = 8.")
q(2,"Segundo o texto, se a equipe não foi acionada, então",["o alarme não disparou.","o alarme disparou.","a regra é falsa.","nada se pode concluir.","a equipe foi acionada depois."],"Modus tollens: não q, logo não p.","mt11a")
q(2,"Pelo texto, o culpado é",["Bruno.","Ana.","Carla.","Ana e Bruno.","nenhum deles."],"Com Bruno culpado, só Ana diz a verdade.","mt11b")
q(2,"Pelo texto, se o culpado fosse Ana, o número de afirmações verdadeiras seria",["2","0","1","3","4"],"Bruno e Carla diriam a verdade.","mt11b")
# n=3
q(3,"O argumento “Se A, então B; B; logo A” é",["inválido, pois afirma o consequente.","válido (modus ponens).","válido (modus tollens).","válido (silogismo).","válido, se B for verdadeira."],"É a falácia da afirmação do consequente.")
q(3,"O argumento “Todo A é B; todo B é C; logo todo A é C” é",["válido.","inválido.","válido só se A = C.","inválido, pois falta uma premissa.","válido só se algum A for C."],"Silogismo categórico válido.")
q(3,"Se “p → q” e “q → r” são verdadeiras, então é verdadeira também",["p → r","r → p","q → p","¬r → q","p ∧ r"],"Silogismo hipotético.")
q(3,"A negação de “Se p, então q ou r” é",["p e não q e não r.","p e não q ou não r.","não p e q e r.","não p ou não q.","p e q e r."],"¬(p → (q ∨ r)) = p ∧ ¬q ∧ ¬r.")
q(3,"A negação de “p se e somente se q” é equivalente a",["ou p ou q (exclusivo).","p e q.","p ou q.","não p e não q.","p → q."],"A negação do bicondicional é o ou exclusivo.")
q(3,"A proposição “(p ∧ q) → p” é",["uma tautologia.","uma contradição.","uma contingência.","equivalente a q.","equivalente a ¬p."],"Se p e q são verdadeiras, p é verdadeira.")
q(3,"A negação de “p ∨ q” é equivalente a",["¬p ∧ ¬q","¬p ∨ ¬q","p ∧ q","p ∧ ¬q","¬p ∨ q"],"De Morgan.")
q(3,"Sabe-se que “p → q” é verdadeira e que q é falsa. Então p é",["falsa.","verdadeira.","indeterminada.","tautológica.","contraditória."],"Modus tollens.")
q(3,"A negação de “Todo guarda que corre cansa” é",["Algum guarda corre e não cansa.","Nenhum guarda que corre cansa.","Algum guarda que corre cansa.","Todo guarda que não corre cansa.","Algum guarda não corre e cansa."],"A negação de “todo A é B” é “algum A não é B”: algum guarda que corre não cansa.")
q(3,"O número de linhas da tabela-verdade de uma proposição com quatro proposições simples é",["16","8","12","4","24"],"2<sup>4</sup> = 16.")
q(3,"A proposição “p ∧ (p ∨ q)” é equivalente a",["p","q","p ∨ q","p ∧ q","¬p"],"Absorção.")
q(3,"O valor lógico de “(V → F) ↔ F” é",["verdadeiro.","falso.","indeterminado.","contraditório.","depende do contexto."],"(V → F) é F; F ↔ F é V.")
q(3,"Sabe-se que: se Ana vai, Bruno vai; se Bruno vai, Carla não vai; Ana foi. Então",["Carla não foi.","Carla foi.","Bruno não foi.","nada se pode concluir sobre Carla.","Ana e Carla foram."],"Ana foi, logo Bruno foi; Bruno foi, logo Carla não foi.")
q(3,"Na tabela-verdade de “p → q”, o número de linhas verdadeiras é",["3","1","2","4","0"],"Só falha com p verdadeiro e q falso.")
q(3,"A disjunção exclusiva “p ⊕ q” é equivalente a",["¬(p ↔ q)","p ↔ q","p ∧ q","p ∨ q","¬p ∧ ¬q"],"Verdadeira quando p e q diferem.")
q(3,"A proposição “q ou não p” é equivalente a",["se p, então q.","se q, então p.","p e não q.","não p e não q.","p ou q."],"¬p ∨ q equivale a p → q.")
q(3,"A recíproca de “se p, então q” é",["se q, então p, que não é equivalente à original.","se não q, então não p, equivalente à original.","se não p, então não q, equivalente à original.","p e não q.","não p ou q."],"A recíproca troca antecedente e consequente, mas não preserva o valor lógico.")
q(3,"A contrapositiva da proposição “se o alarme dispara, a equipe é acionada” é",["Se a equipe não é acionada, o alarme não dispara.","Se a equipe é acionada, o alarme dispara.","Se o alarme não dispara, a equipe não é acionada.","O alarme dispara e a equipe não é acionada.","O alarme não dispara ou a equipe não é acionada."],"Inverte e nega: se não q, então não p.","mt11a")
q(3,"A negação do regulamento do texto é",["O alarme dispara e a equipe não é acionada.","O alarme não dispara e a equipe é acionada.","Se o alarme não dispara, a equipe não é acionada.","Se a equipe é acionada, o alarme dispara.","O alarme não dispara ou a equipe é acionada."],"¬(p → q) = p ∧ ¬q.","mt11a")
q(3,"Pelo texto, o guarda que disse a verdade é",["Ana.","Bruno.","Carla.","Ana e Carla.","nenhum."],"O culpado é Bruno, e só a afirmação de Ana (“Foi Bruno”) é verdadeira.","mt11b")
assert eq(lambda p,q: not (p or q), lambda p,q: (not p) and (not q)) and eq(lambda p,q: p and (p or q), lambda p,q: p) and taut(lambda p,q: imp(p and q,p))
assert eq(lambda p,q: (not p) or q, lambda p,q: imp(p,q)) and eq(lambda p,q: p!=q, lambda p,q: not (p==q))
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("Lógica: do conectivo ao argumento",[
 ("prop","Proposições",["declarativa, V ou F","negação inverte o valor","sentença aberta não é"],"seção 1"),
 ("conect","Conectivos",["e: só V com V e V","ou: só F com F e F","se...então: só F com V e F"],"seção 2"),
 ("neg","Negações",["e ↔ ou (De Morgan)","condicional: p e não q","todo ↔ algum não"],"seção 3"),
 ("eq","Equivalências",["contrapositiva","não p ou q","recíproca não vale"],"seção 4"),
 ("arg","Argumentos",["modus ponens e tollens","silogismo hipotético","falácias"],"seção 5"),
 ("tab","Tabela-verdade",["2 elevado a n linhas","tautologia: sempre V","contradição: sempre F"],"seção 2")],
 "Na prova: use a negação certa e teste o argumento com a hipótese contrária")
aula_html=aula(LEAD,S,[1,2,3,4,5,'QR',7,8,9],QR,6,svg,"Conectivos e tabelas-verdade são a base; negações e equivalências resolvem a maioria das questões; os argumentos fecham o assunto.","Fontes: Edital 02/2026, Anexo I. Referências de base: Alencar Filho, <em>Iniciação à Lógica Matemática</em>; Copi, <em>Introdução à Lógica</em>. Exemplos criados para a aula.")
revisao("mt-11","Estruturas lógicas e lógica de argumentação",QQ,list(tx),
 cobertura=["Recorte do edital: proposições, conectivos, negação e argumentos. Cobertos: valores lógicos, conectivos e tabelas-verdade, tautologia e contradição, De Morgan, negação do condicional e de quantificadores, equivalências, modus ponens e tollens, silogismos, falácias."],
 pendencias=["Referências citadas como base (Alencar Filho; Copi); não foram consultadas página a página.","As equivalências e negações foram conferidas por força bruta em código; as questões de interpretação textual por conferência manual."],
 fontes_conferidas=[])
gravar("mt-11",aula_html,banco("mt-11",QQ),tx)
