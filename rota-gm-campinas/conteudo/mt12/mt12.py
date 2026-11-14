import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
LEAD="Diagramas lógicos e sequências fecham a parte de raciocínio da prova. Nos diagramas, a Vunesp cobra as relações todo, algum e nenhum, e a contagem de elementos em conjuntos que se cruzam. Nas sequências, cobra o padrão de uma lista de números ou de figuras e a posição dos termos em ciclos. O método é o mesmo nos dois casos: desenhar, ou escrever os primeiros termos, antes de procurar a fórmula."
S={}
S[1]="""## 1. Diagramas: todo, algum e nenhum

Os diagramas de Venn representam conjuntos por regiões. A afirmação “todo A é B” é o diagrama em que a região de A está dentro da de B. “Nenhum A é B” é o diagrama em que as regiões não se tocam. “Algum A é B” é o diagrama em que as regiões têm uma parte em comum, ao menos um elemento. “Algum A não é B” indica que há pelo menos um elemento de A fora de B.

O que os diagramas ensinam é a diferença entre o que a premissa garante e o que ela apenas permite. Se “todo guarda é servidor” e Ana é guarda, então Ana é servidora: a conclusão é necessária. Se “todo guarda é servidor” e Bruno é servidor, nada se pode dizer sobre Bruno ser guarda: a região de servidor é maior que a de guarda. Duas regras úteis: “algum A é B” equivale a “algum B é A”, mas “todo A é B” não equivale a “todo B é A”.

Com duas premissas, desenha-se o caso mais geral e vê-se o que vale em todos os desenhos possíveis. Se “todo A é B” e “nenhum B é C”, então nenhum A é C: os A estão dentro de B, que não toca C. Se “todo A é B” e “algum B é C”, nada se conclui sobre A e C: o pedaço de B que toca C pode ficar fora de A.
"""
S[2]="""## 2. Contagem em conjuntos

Quando dois grupos se cruzam, somar os dois conta duas vezes a parte comum. A correção é a regra da união: n(A ∪ B) = n(A) + n(B) − n(A ∩ B). Em um grupo de 100 guardas, 60 falam inglês, 45 falam espanhol e 20 falam as duas línguas. Quantos falam pelo menos uma? 60 + 45 − 20 = 85. Quantos não falam nenhuma? 100 − 85 = 15. Quantos falam só inglês? 60 − 20 = 40. Quantos falam exatamente uma língua? 40 + 25 = 65, porque só espanhol é 45 − 20 = 25.

O jeito mais seguro é preencher o diagrama de dentro para fora: primeiro a interseção (20), depois o que resta de cada conjunto (40 e 25) e por fim o que está fora de todos (15). A soma das regiões deve dar o total.

Com três conjuntos, a regra é n(A ∪ B ∪ C) = n(A) + n(B) + n(C) − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) + n(A ∩ B ∩ C). Com n(A) = 20, n(B) = 18, n(C) = 15, interseções de dois a dois 8, 6 e 5 e a tripla 3, a união é 20 + 18 + 15 − 8 − 6 − 5 + 3 = 37. A parte tripla é somada de volta, porque foi subtraída demais.
"""
S[3]="""## 3. Sequências numéricas

Para descobrir o padrão, escreva os termos e olhe as diferenças e as razões entre vizinhos. Se a diferença é constante, é uma progressão aritmética (PA). Se a razão é constante, é uma progressão geométrica (PG). Se nenhuma das duas é constante, olhe as diferenças das diferenças.

Em uma PA de primeiro termo a<sub>1</sub> e razão r, o termo de ordem n é a<sub>n</sub> = a<sub>1</sub> + (n − 1) r. Na sequência 3, 7, 11, 15, a razão é 4, e o 20º termo é 3 + 19 × 4 = 79. A soma dos n primeiros termos é a média do primeiro e do último, vezes n: S = (a<sub>1</sub> + a<sub>n</sub>) × n ÷ 2. A soma de 1 a 100 é (1 + 100) × 100 ÷ 2 = 5.050; é a história de Gauss, que emparelhou 1 com 100, 2 com 99 e assim por diante, 50 pares de 101.

Em uma PG de primeiro termo a<sub>1</sub> e razão q, a<sub>n</sub> = a<sub>1</sub> × q<sup>n−1</sup>. Na sequência 3, 6, 12, 24, a razão é 2, e o 8º termo é 3 × 2<sup>7</sup> = 384. A soma dos n primeiros termos é a<sub>1</sub> (q<sup>n</sup> − 1) ÷ (q − 1). Em 2, 6, 18, 54, 162, a soma é 2 × (3<sup>5</sup> − 1) ÷ 2 = 242.

Algumas sequências famosas valem reconhecer. Os quadrados: 1, 4, 9, 16, 25. Os triangulares: 1, 3, 6, 10, 15, em que se soma 1, 2, 3, 4 em cada passo. Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, em que cada termo é a soma dos dois anteriores. Quando as diferenças crescem de 1 em 1, como em 1, 2, 4, 7, 11, 16, o termo de ordem n é 1 mais a soma de 1 a n − 1. Há ainda as sequências alternadas, em que os termos de ordem ímpar seguem um padrão e os de ordem par seguem outro.
"""
S[4]="""## 4. Sequências com ciclo

Quando o padrão se repete em ciclos, a posição de um termo distante sai do resto da divisão. Se as letras A, B, C, D, E se repetem sem parar, a 2.026ª letra é calculada dividindo 2.026 por 5: o resto é 1, e então a letra é A, a primeira do ciclo. Se o resto for 0, o termo é o último do ciclo. Com figuras, vale o mesmo: um ciclo de triângulo, quadrado e círculo tem a 7ª figura igual à 1ª, porque 7 dividido por 3 deixa resto 1.

Para dias da semana, o ciclo é 7. Se hoje é quinta-feira, daqui a 100 dias será que dia? 100 dividido por 7 dá resto 2, e dois dias depois de quinta é sábado. O resto é o que importa, porque cada bloco de 7 dias volta ao mesmo dia.

Exemplo resolvido. Os códigos das viaturas seguem a sequência V1, V2, V4, V7, V11, e assim por diante. As diferenças são 1, 2, 3, 4, logo as próximas são 5, 6 e 7. O sexto termo é 11 + 5 = 16 e o sétimo, 16 + 6 = 22. O décimo termo é 1 mais a soma de 1 a 9, ou seja, 1 + 45 = 46.
"""
S[6]="""## 6. Na rotina do guarda

- **Cadastro de línguas e habilitações:** contar quantos têm pelo menos uma habilitação exige descontar a interseção.
- **Escalas cíclicas:** um plantão que se repete a cada certo número de dias cai no mesmo dia da semana segundo o resto da divisão.
- **Numeração de viaturas, ocorrências e boletins:** os códigos seguem padrões, e saber identificá-los evita erro de registro.
- **Depoimentos:** testar o que a premissa garante e o que apenas permite é o mesmo exercício dos diagramas.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Somar dois conjuntos sem descontar a interseção | n(A ∪ B) = n(A) + n(B) − n(A ∩ B) |
| Concluir “todo B é A” de “todo A é B” | Desenhe: a região de B é maior |
| Tirar conclusão de duas premissas com “algum” | Se nem todo desenho obriga a conclusão, ela não vale |
| Errar a posição em ciclos quando o resto é zero | Resto 0 é o último termo do ciclo |
| Usar a fórmula da PA em sequência que não é PA | Confira a diferença entre termos vizinhos |
| Contar o primeiro termo duas vezes ou esquecê-lo | O n-ésimo termo vem depois de n − 1 passos |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Todo A é B | Região de A dentro da de B |
| Nenhum A é B | Regiões separadas |
| Algum A é B | Regiões com parte comum |
| União | n(A) + n(B) − n(A ∩ B) |
| PA | a<sub>n</sub> = a<sub>1</sub> + (n − 1) r; soma = (a<sub>1</sub> + a<sub>n</sub>) n / 2 |
| PG | a<sub>n</sub> = a<sub>1</sub> q<sup>n−1</sup> |
| Ciclo | Posição = resto da divisão pelo tamanho do ciclo |
| Fibonacci | Cada termo é a soma dos dois anteriores |
"""
assert 60+45-20==85 and 100-85==15 and 60-20==40 and 45-20==25 and 40+25==65 and 20+18+15-8-6-5+3==37
assert 3+19*4==79 and (1+100)*100//2==5050 and 3*2**7==384 and 2*(3**5-1)//2==242 and 2026%5==1 and 100%7==2
terms=[1]; 
for d in range(1,10): terms.append(terms[-1]+d)
assert terms[:6]==[1,2,4,7,11,16] and terms[9]==46
QR=[("Questão 1","Em um grupo de 100 guardas, 60 falam inglês, 45 falam espanhol e 20 falam as duas línguas. O número de guardas que não falam nenhuma delas é",["15","25","40","55","0"],0,"Pelo menos uma: 60 + 45 − 20 = 85. Nenhuma: 100 − 85 = 15."),
("Questão 2","Considere as premissas: todo guarda é servidor; nenhum servidor é aposentado. Conclui-se que",["nenhum guarda é aposentado.","algum guarda é aposentado.","todo aposentado é guarda.","algum servidor é guarda e aposentado.","todo servidor é guarda."],0,"Os guardas estão dentro de servidor, que não toca aposentado. Logo nenhum guarda é aposentado."),
("Questão 3","A sequência 3, 7, 11, 15, ... tem o 20º termo igual a",["79","75","83","80","77"],0,"PA de razão 4: 3 + 19 × 4 = 79."),
("Questão 4","Se as letras A, B, C, D, E se repetem indefinidamente, a 2.026ª letra é",["A","B","C","D","E"],0,"2.026 ÷ 5 deixa resto 1: primeira letra do ciclo, A.")]
QR=[(a,b,c,[1,3,2,0][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
QRF=qr_md(QR,5)
t1="<strong>Línguas na Guarda</strong><br><br>Em um grupo de 100 guardas municipais de Vila Nova, cidade fictícia, 60 falam inglês, 45 falam espanhol e 20 falam as duas línguas."
t2="<strong>Códigos das viaturas</strong><br><br>As viaturas da Guarda Municipal de Vila Nova são numeradas segundo a sequência V1, V2, V4, V7, V11, V16 e assim por diante, em que a diferença entre dois termos consecutivos aumenta sempre uma unidade."
tx={"mt12a":t1,"mt12b":t2}
a=[1]
for d in range(1,12): a.append(a[-1]+d)
assert a[5]==16 and a[6]-a[5]==6 and a[9]==46 and next(i for i,x in enumerate(a,1) if x>30)==9
# n=1
qv(1,"O próximo termo da sequência 3, 7, 11, 15 é","{}",19,[18,20,22,17],"Soma-se 4.")
qv(1,"O próximo termo da sequência 2, 4, 8, 16 é","{}",32,[24,20,18,30],"Multiplica-se por 2.")
qv(1,"O próximo termo da sequência 1, 4, 9, 16 é","{}",25,[20,23,24,32],"Quadrados: 5² = 25.")
qv(1,"O 6º termo da sequência 10, 20, 30, ... é","{}",60,[50,70,66,120],"10 × 6.")
qv(1,"Se n(A) = 12, n(B) = 8 e n(A ∩ B) = 3, então n(A ∪ B) é","{}",17,[20,23,15,9],"12 + 8 − 3 = 17.")
q(1,"Se todo guarda é servidor e Ana é guarda, então",["Ana é servidora.","Ana não é servidora.","todo servidor é guarda.","Ana pode ou não ser servidora.","nenhum guarda é servidor."],"A região de guarda está dentro da de servidor.")
q(1,"“Nenhum A é B” é representado por regiões",["que não se tocam.","com parte comum.","uma dentro da outra.","iguais.","que cobrem todo o diagrama."],"Conjuntos disjuntos.")
q(1,"Se o diagrama de A está inteiro dentro do de B, então vale",["todo A é B.","todo B é A.","nenhum A é B.","algum B não é A, e nenhum A é B.","A e B são iguais."],"A contido em B: todo A é B.")
qv(1,"O 8º termo da sequência 5, 10, 15, ... é","{}",40,[35,45,50,80],"5 × 8.")
qv(1,"O próximo termo da sequência 1, 1, 2, 3, 5, 8 é","{}",13,[11,12,16,10],"Fibonacci: 5 + 8.")
qv(1,"Em um grupo de 30 pessoas, 18 gostam de A e 20 gostam de B. Todas gostam de pelo menos um dos dois. As que gostam dos dois são","{}",8,[2,10,12,38],"18 + 20 − 30 = 8.")
q(1,"Se as letras A, B, C se repetem indefinidamente, a 10ª letra é",["A","B","C","D","E"],"10 dividido por 3 deixa resto 1: A.")
qv(1,"O próximo termo da sequência 100, 90, 80 é","{}",70,[60,75,85,110],"Subtrai-se 10.")
q(1,"A afirmação “algum A é B” equivale a",["algum B é A.","todo A é B.","todo B é A.","nenhum A é B.","algum A não é B."],"A relação é simétrica.")
qv(1,"A soma dos cinco primeiros números pares positivos é","{}",30,[25,20,15,35],"2 + 4 + 6 + 8 + 10.")
q(1,"Se hoje é terça-feira, daqui a 7 dias será",["terça-feira.","quarta-feira.","segunda-feira.","sábado.","domingo."],"Uma semana depois, o mesmo dia.")
q(1,"Em uma sequência cíclica de figuras (triângulo, quadrado, círculo), a 7ª figura é",["triângulo.","quadrado.","círculo.","pentágono.","losango."],"7 dividido por 3 deixa resto 1: a primeira.")
qv(1,"O próximo termo da sequência 3, 6, 12, 24 é","{}",48,[36,30,42,27],"Multiplica-se por 2.")
qv(1,"Segundo o texto, o número de guardas que falam pelo menos uma das duas línguas é","{}",85,[105,60,100,65],"60 + 45 − 20 = 85.","mt12a")
qv(1,"Segundo o texto, o número de guardas que falam inglês, mas não espanhol, é","{}",40,[20,60,25,45],"60 − 20 = 40.","mt12a")
# n=2
qv(2,"O 20º termo da sequência 5, 9, 13, ... é","{}",81,[85,77,80,100],"5 + 19 × 4 = 81.")
qv(2,"O 8º termo da sequência 3, 6, 12, ... é","{}",384,[192,768,48,24],"3 × 2<sup>7</sup> = 384.")
qv(2,"A soma dos números inteiros de 1 a 20 é","{}",210,[200,420,190,230],"(1 + 20) × 20 ÷ 2 = 210.")
qv(2,"O próximo termo da sequência 2, 5, 10, 17, 26 é","{}",37,[35,36,38,40],"n² + 1: 6² + 1 = 37.")
qv(2,"Se n(A ∪ B) = 30, n(A) = 18 e n(B) = 17, então n(A ∩ B) é","{}",5,[13,35,12,0],"18 + 17 − 30 = 5.")
qv(2,"Em um grupo de 60 pessoas, 35 leem jornal, 28 leem revista e 10 leem os dois. O número de pessoas que não leem nenhum dos dois é","{}",7,[0,10,17,25],"Pelo menos um: 35 + 28 − 10 = 53. 60 − 53 = 7.")
q(2,"Se as letras A, B, C, D, E se repetem indefinidamente, a 2.026ª letra é",["A","B","C","D","E"],"2.026 ÷ 5 deixa resto 1.")
q(2,"Se todo A é B e nenhum B é C, então",["nenhum A é C.","algum A é C.","todo C é A.","todo A é C.","algum C é A."],"A está dentro de B, que não toca C.")
q(2,"Se alguns A são B e todo B é C, então",["algum A é C.","todo A é C.","nenhum A é C.","todo C é A.","nenhum C é A."],"Os A que são B estão em C.")
qv(2,"O 9º termo da sequência de Fibonacci 1, 1, 2, 3, 5, ... é","{}",34,[21,55,32,29],"1, 1, 2, 3, 5, 8, 13, 21, 34.")
qv(2,"O próximo termo da sequência 100, 95, 85, 70 é","{}",50,[55,45,60,35],"As diferenças são −5, −10, −15, logo a próxima é −20.")
qv(2,"O 10º termo da sequência 1, 2, 4, 5, 7, 8, ... (soma-se 1 e 2 alternadamente) é","{}",14,[15,13,16,17],"1, 2, 4, 5, 7, 8, 10, 11, 13, 14.")
q(2,"Se hoje é quinta-feira, daqui a 100 dias será",["sábado.","sexta-feira.","domingo.","quinta-feira.","segunda-feira."],"100 ÷ 7 deixa resto 2; quinta + 2 dias = sábado.")
qv(2,"O 15º termo da sequência 3, 5, 7, ... é","{}",31,[33,29,45,35],"3 + 14 × 2 = 31.")
qv(2,"Em um grupo, 20 pessoas estão em A, 15 estão em B e 10 estão nos dois. O número de pessoas que estão em exatamente um dos dois é","{}",15,[25,35,5,10],"União 25; exatamente um: 25 − 10 = 15.")
qv(2,"O 6º termo da sequência 2, 6, 18, 54, ... é","{}",486,[324,162,972,500],"2 × 3<sup>5</sup> = 486.")
qv(2,"A soma 1 + 3 + 5 + ... + 19 (dez números ímpares) é","{}",100,[90,110,95,200],"Soma dos n primeiros ímpares é n²: 10² = 100.")
qv(2,"Segundo o texto, o número de guardas que não falam nenhuma das duas línguas é","{}",15,[40,25,20,85],"100 − 85.","mt12a")
q(2,"Segundo o texto, o código do 7º termo é",["V22","V21","V23","V24","V20"],"Soma-se 6 ao 6º termo: 16 + 6 = 22.","mt12b")
qv(2,"Segundo o texto, a diferença entre o 7º e o 6º termos é","{}",6,[5,7,4,22],"Os incrementos são 1, 2, 3, 4, 5, 6.","mt12b")
# n=3
qv(3,"A soma dos números inteiros de 1 a 100 é","{}",5050,[5000,10100,5100,4950],"(1 + 100) × 100 ÷ 2.")
qv(3,"A soma dos cinco primeiros termos da PG 2, 6, 18, ... é","{}",242,[162,243,484,120],"2 × (3<sup>5</sup> − 1) ÷ 2 = 242.")
qv(3,"Em três conjuntos, n(A) = 20, n(B) = 18, n(C) = 15, n(A ∩ B) = 8, n(A ∩ C) = 6, n(B ∩ C) = 5 e n(A ∩ B ∩ C) = 3. O valor de n(A ∪ B ∪ C) é","{}",37,[53,40,34,31],"20 + 18 + 15 − 8 − 6 − 5 + 3 = 37.")
q(3,"Sendo todo A é B e algum B é C, é correto concluir que",["nada se pode concluir sobre A e C.","algum A é C.","todo A é C.","nenhum A é C.","todo C é A."],"O pedaço de B que toca C pode ficar fora de A.")
qv(3,"O 10º termo da sequência 2, 3, 5, 8, 12, 17, ... é","{}",47,[45,48,52,50],"Os incrementos crescem de 1 em 1: 2 + (1 + 2 + ... + 9) = 47.")
q(3,"Em um ciclo de 4 figuras, a 2.026ª figura é igual à",["2ª","1ª","3ª","4ª","5ª"],"2.026 ÷ 4 deixa resto 2.")
qv(3,"Em uma PA, o 3º termo é 11 e o 7º termo é 27. O 10º termo é","{}",39,[35,43,31,41],"Razão 4; a<sub>1</sub> = 3; a<sub>10</sub> = 3 + 36 = 39.")
qv(3,"Em um grupo de 40 pessoas, 25 falam inglês, 18 falam espanhol e 5 não falam nenhuma das duas. O número que fala as duas é","{}",8,[3,13,10,6],"Pelo menos uma: 35. 25 + 18 − 35 = 8.")
qv(3,"A soma dos 10 primeiros termos da PA 5, 8, 11, ... é","{}",185,[160,200,205,170],"a<sub>10</sub> = 32; soma = (5 + 32) × 10 ÷ 2 = 185.")
qv(3,"O 12º termo da sequência 1, 3, 6, 10, 15, ... é","{}",78,[66,72,84,90],"Triangulares: 12 × 13 ÷ 2 = 78.")
q(3,"Se hoje é segunda-feira, daqui a 1.024 dias será",["quarta-feira.","terça-feira.","segunda-feira.","quinta-feira.","sexta-feira."],"1.024 ÷ 7 deixa resto 2; segunda + 2 = quarta.")
q(3,"Se todos os A são B e nenhum C é B, então",["nenhum C é A.","algum C é A.","todo C é A.","algum A é C.","todo A é C."],"Os A estão em B, e C está fora de B.")
qv(3,"O 6º termo da sequência 1, 2, 6, 24, 120, ... é","{}",720,[600,840,480,360],"Fatorial: 6! = 720.")
qv(3,"O 8º termo da PG 64, 32, 16, ... é","{}",0.5,[1,2,0.25,4],"64 × (1/2)<sup>7</sup> = 0,5.")
qv(3,"A soma dos múltiplos de 3 de 1 a 50 é","{}",408,[400,450,425,390],"3 + 6 + ... + 48 = 3 × (1 + ... + 16) = 3 × 136 = 408.")
qv(3,"Entre os números de 1 a 100, os que não são múltiplos de 2 nem de 5 são","{}",40,[30,50,60,70],"100 − 50 − 20 + 10 = 40.")
q(3,"Se alguns A são B e nenhum B é C, então",["algum A não é C.","nenhum A é C.","todo A é C.","todo C é A.","algum C é A."],"Os A que são B não são C.")
qv(3,"Segundo o texto, o número de guardas que falam exatamente uma das duas línguas é","{}",65,[85,40,45,25],"Só inglês 40 e só espanhol 25.","mt12a")
qv(3,"Segundo o texto, o 10º código da sequência é V","{}",46,[45,55,44,50],"1 + (1 + 2 + ... + 9) = 46.","mt12b")
qv(3,"Segundo o texto, a posição do primeiro termo maior que 30 é","{}",9,[8,10,7,11],"Termos: 1, 2, 4, 7, 11, 16, 22, 29, 37. O 9º é o primeiro acima de 30.","mt12b")
assert 25+18-35==8 and (5+32)*10//2==185 and 12*13//2==78 and 1024%7==2 and 64/2**7==0.5 and sum(range(3,51,3))==408
assert sum(1 for k in range(1,101) if k%2 and k%5)==40 and 2+sum(range(1,10))==47 and 3+9*4==39
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("Diagramas e sequências: desenhar antes de calcular",[
 ("venn","Diagramas de Venn",["todo: dentro","nenhum: separados","algum: parte comum"],"seção 1"),
 ("uniao","Contagem",["união: soma menos interseção","três conjuntos","preencher de dentro para fora"],"seção 2"),
 ("pa","PA",["diferença constante","aₙ = a₁ + (n − 1)r","soma = (a₁ + aₙ)n/2"],"seção 3"),
 ("pg","PG",["razão constante","aₙ = a₁ qⁿ⁻¹","soma geométrica"],"seção 3"),
 ("famosas","Sequências famosas",["quadrados e triangulares","Fibonacci","diferenças crescentes"],"seção 3"),
 ("ciclo","Ciclos",["posição = resto","resto 0 = último","dias da semana: ciclo 7"],"seção 4")],
 "Na prova: escreva os primeiros termos e olhe as diferenças; em ciclos, use o resto")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"Os diagramas e a contagem cuidam dos conjuntos; as sequências e os ciclos, dos padrões numéricos e de posição.","Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1 (Conjuntos) e v. 4 (Sequências); Alencar Filho, <em>Iniciação à Lógica Matemática</em>. Exemplos criados para a aula.")
revisao("mt-12","Diagramas lógicos e sequências",QQ,list(tx),
 cobertura=["Recorte do edital: todo, algum, nenhum; sequências numéricas e de figuras. Cobertos: diagramas de Venn, silogismos com quantificadores, contagem em dois e três conjuntos, PA, PG, Fibonacci, triangulares, diferenças crescentes, sequências cíclicas e dias da semana.","Sequências de figuras são tratadas em texto (ciclos); não há desenhos."],
 pendencias=["Referências bibliográficas citadas como base; não foram consultadas página a página.","Cálculos conferidos por código em boa parte; as questões de conclusão lógica foram conferidas manualmente."],
 fontes_conferidas=[])
gravar("mt-12",aula_html,banco("mt-12",QQ),tx)
