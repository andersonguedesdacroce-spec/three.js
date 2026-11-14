import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); from _mt import *
from statistics import mean, median, mode
LEAD="Tabelas, gráficos e média aritmética formam o assunto mais próximo do dia a dia de quem trabalha com relatórios. A Vunesp cobra a leitura de dados em tabelas e gráficos (barras, linhas e setores), o cálculo da média aritmética simples e problemas em que a média muda quando um valor entra ou sai. A ideia por trás da média cabe numa imagem: é o valor que cada um receberia se a soma de tudo fosse repartida igualmente."
S={}
S[1]="""## 1. Ler tabelas e gráficos

Antes de qualquer conta, leia o título, as unidades e os eixos. Em uma tabela, cada linha é um caso e cada coluna é uma grandeza. Em um gráfico de barras, a altura da barra mostra o valor, e é fácil comparar categorias. Em um gráfico de linhas, a inclinação mostra como o valor varia no tempo: subida, descida ou estabilidade. Em um gráfico de setores (a pizza), cada fatia mostra a parte do todo, e o círculo inteiro vale 100% e 360°.

A leitura correta evita erros que a prova explora. Confira se o gráfico trata de quantidades ou de porcentagens, e se a escala começa no zero. Para converter um setor em ângulo, multiplique a porcentagem por 360°: 40% correspondem a 0,40 × 360° = 144°. Para achar a quantidade de um setor, multiplique a porcentagem pelo total: 25% de 200 pessoas são 50 pessoas.

Para comparar duas leituras de um gráfico de linhas, calcule a variação relativa: (valor final − valor inicial) ÷ valor inicial. Se as ocorrências foram de 50 para 40, a variação é −10/50 = −20%; se depois foram de 40 para 60, a variação é +20/40 = +50%.
"""
S[2]="""## 2. Média aritmética simples

A média aritmética de um conjunto de valores é a soma deles dividida pela quantidade. Em 4, 6 e 8, a soma é 18, e dividindo por 3 vem 6. A imagem é a de repartir: se três guardas têm 4, 6 e 8 ocorrências para atender e elas forem redistribuídas igualmente, cada um fica com 6.

Dessa imagem sai a relação mais útil: soma = média × quantidade. Se a média de 5 números é 8, a soma é 40. Quase todos os problemas de média se resolvem passando pela soma. Quando um valor sai, subtrai-se da soma; quando entra, soma-se; e só no fim divide-se pela nova quantidade.

Exemplo resolvido 1. A média de 5 números é 12. Se um deles, que vale 20, for retirado, qual a média dos 4 restantes? A soma era 5 × 12 = 60. Sem o 20, a soma é 40. A nova média é 40 ÷ 4 = 10.

Exemplo resolvido 2. Em 3 provas, um candidato tirou 5 e 7. Qual deve ser a terceira nota para a média ser 7? A soma precisa ser 3 × 7 = 21. As duas primeiras somam 12. A terceira é 21 − 12 = 9.

Exemplo resolvido 3. A idade média de 10 pessoas é 30 anos. Entra uma pessoa de 41 anos. A soma era 300; passa a 341; e há 11 pessoas. A nova média é 341 ÷ 11 = 31.

A média é sensível aos valores extremos. Duas medidas ajudam a descrever um conjunto sem se deixar levar por eles: a mediana é o valor do meio, depois de ordenar os dados (se a quantidade for par, é a média dos dois centrais), e a moda é o valor que mais se repete. Em 2, 3, 3, 4, 5, a moda é 3 e a mediana é 3; em 2, 4, 6, 8, a mediana é (4 + 6)/2 = 5.
"""
S[3]="""## 3. Propriedades úteis da média

Algumas propriedades poupam contas. Somar um mesmo valor a todos os dados soma esse valor à média: se cada nota recebe 5 pontos de bônus, a média sobe 5. Multiplicar todos os dados por um número multiplica a média por ele: se todas as notas dobram, a média dobra. A média está sempre entre o menor e o maior valor do conjunto. E a soma dos desvios em relação à média é zero: o que sobra em uns compensa o que falta em outros.

Quando se juntam dois grupos, a média do conjunto não é a média das médias, a não ser que os grupos tenham o mesmo tamanho. Um grupo de 3 números com média 5 e outro de 2 números com média 10 formam um conjunto de 5 números cuja média é (15 + 20) ÷ 5 = 7, e não (5 + 10) ÷ 2 = 7,5.
"""
S[5]="""## 5. Na rotina do guarda

- **Relatório mensal:** a média de ocorrências por mês dá a referência para dizer se um mês ficou acima ou abaixo do normal.
- **Gráficos de setores nos balanços:** a fatia dos furtos em 40% de 400 ocorrências são 160 casos e, no círculo, 144°.
- **Planejamento de efetivo:** a média de atendimentos por guarda orienta a escala.
- **Variação de um mês para outro:** calcula-se sobre o mês anterior, como em qualquer porcentagem.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Dividir a soma pela quantidade errada | Conte os valores antes de dividir |
| Tirar a média das médias de grupos de tamanhos diferentes | Some tudo e divida pelo total de elementos |
| Esquecer que um valor que entra muda a quantidade | Nova média = nova soma ÷ nova quantidade |
| Confundir mediana com média | Mediana é o valor do meio dos dados ordenados |
| Calcular a variação percentual sobre o valor final | A base é o valor inicial |
| Ler o gráfico de setores como quantidades | Setor é parte do todo: multiplique pelo total |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Média aritmética | Soma ÷ quantidade |
| Relação básica | Soma = média × quantidade |
| Mediana | Valor central dos dados ordenados |
| Moda | Valor que mais se repete |
| Setor | 100% = 360°; 40% = 144° |
| Variação | (final − inicial) ÷ inicial |
| Grupos distintos | Some tudo e divida pelo total |
"""
assert mean([4,6,8])==6 and 5*12-20==40 and 40/4==10 and 3*7-12==9 and (300+41)/11==31 and (15+20)/5==7
assert median([2,4,6,8])==5 and mode([2,3,3,4,5])==3 and Fr(4,10)*360==144 and Fr(25,100)*200==50
QR=[("Questão 1","A média de cinco números é 12. Retirando-se um deles, que vale 20, a média dos quatro restantes é",["10","12","8","15","16"],0,"Soma: 5 × 12 = 60. Sem o 20, 40. Média: 40 ÷ 4 = 10."),
("Questão 2","Um candidato fez duas provas e tirou 5 e 7. Para obter média 7 em três provas, a terceira nota deve ser",["9","7","8","10","6"],0,"A soma precisa ser 21; já tem 12; faltam 9."),
("Questão 3","Em um gráfico de setores, o setor dos furtos representa 40% do total de 400 ocorrências. Esse setor corresponde a",["160 ocorrências e 144°.","160 ocorrências e 40°.","40 ocorrências e 144°.","100 ocorrências e 90°.","160 ocorrências e 100°."],0,"0,40 × 400 = 160 ocorrências; 0,40 × 360° = 144°."),
("Questão 4","Um grupo de 3 números tem média 5 e outro de 2 números tem média 10. A média dos 5 números juntos é",["7","7,5","8","6","5,5"],0,"Somas: 15 e 20. Total 35. 35 ÷ 5 = 7. A média das médias, 7,5, seria um erro, porque os grupos têm tamanhos diferentes.")]
QR=[(a,b,c,[3,2,0,4][k],e) for k,(a,b,c,d,e) in enumerate(QR)]
QRF=qr_md(QR,4)
t1="<strong>Ocorrências atendidas, de janeiro a maio</strong><br><br>A tabela mostra o número de ocorrências atendidas pela Guarda Municipal de Vila Nova, cidade fictícia, em cada mês.<br><br><table><thead><tr><th>Mês</th><th>Ocorrências</th></tr></thead><tbody><tr><td>Janeiro</td><td>42</td></tr><tr><td>Fevereiro</td><td>38</td></tr><tr><td>Março</td><td>50</td></tr><tr><td>Abril</td><td>46</td></tr><tr><td>Maio</td><td>54</td></tr></tbody></table>"
t2="<strong>Ocorrências do semestre por tipo</strong><br><br>No semestre, a Guarda registrou 400 ocorrências. O gráfico de setores do relatório mostra: furtos, 40%; perturbação do sossego, 25%; trânsito, 20%; outras, 15%."
tx={"mt9a":t1,"mt9b":t2}
assert mean([42,38,50,46,54])==46 and 54-38==16 and 6*50-230==70 and Fr(46-50,50)==Fr(-2,25) and Fr(20,100)*400==80 and 0.4*400==160
# n=1
qv(1,"A média aritmética de 4, 6 e 8 é","{}",6,[18,8,5,7],"(4 + 6 + 8) ÷ 3 = 6.")
qv(1,"A média aritmética de 10, 20, 30 e 40 é","{}",25,[100,20,30,35],"100 ÷ 4 = 25.")
qv(1,"A média aritmética de 5, 5 e 5 é","{}",5,[15,3,10,1],"Todos iguais: a média é 5.")
qv(1,"A média de cinco números é 8. A soma desses números é","{}",40,[13,16,8,45],"Soma = média × quantidade = 40.")
qv(1,"A média aritmética de 7 e 9 é","{}",8,[16,7,9,63],"(7 + 9) ÷ 2 = 8.")
qv(1,"A média das notas 6, 7, 8, 9 e 10 é","{}",8,[7,9,40,6],"40 ÷ 5 = 8.")
qv(1,"A moda do conjunto 2, 3, 3, 4, 5 é","{}",3,[4,2,5,3.4],"3 aparece duas vezes.")
qv(1,"A mediana do conjunto 3, 5, 9 é","{}",5,[3,9,7,6],"O valor do meio, com os dados em ordem, é 5.")
qv(1,"A média aritmética de 12, 14, 16 e 18 é","{}",15,[60,14,16,17],"60 ÷ 4 = 15.")
qv(1,"Um aluno fez 4 provas e a média foi 7. A soma das notas é","{}",28,[11,21,14,7],"4 × 7 = 28.")
qv(1,"A média aritmética dos números de 1 a 9 é","{}",5,[4.5,45,9,6],"45 ÷ 9 = 5.")
qv(1,"A mediana do conjunto 4, 8, 2, 6 é","{}",5,[4,6,5.5,20],"Ordenando: 2, 4, 6, 8. Média dos centrais: (4 + 6)/2 = 5.")
qv(1,"Em um gráfico de setores, um setor de 25% em um total de 200 pessoas representa","{} pessoas",50,[25,25.5,100,75],"0,25 × 200 = 50.")
qv(1,"Em um gráfico de barras, as barras valem 30, 45 e 60. A diferença entre a maior e a menor é","{}",30,[15,45,60,135],"60 − 30 = 30.")
q(1,"Na tabela, A vale 12 e B vale 8. A razão entre A e B é",["3/2","2/3","12/20","4","1/3"],"12/8 = 3/2.")
qv(1,"A média aritmética de 0,5 e 1,5 é","{}",1,[2,0.5,0.75,1.5],"2 ÷ 2 = 1.")
qv(1,"Se a média de três números é 10, a soma deles é","{}",30,[13,10,7,100],"3 × 10 = 30.")
qv(1,"A média de idades de duas pessoas, de 20 e 30 anos, é","{} anos",25,[50,20,30,10],"50 ÷ 2 = 25.")
qv(1,"Segundo o texto, a média mensal de ocorrências de janeiro a maio é","{}",46,[230,50,42,48],"(42 + 38 + 50 + 46 + 54) ÷ 5 = 46.","mt9a")
qv(1,"Segundo o texto, o número de ocorrências de furtos no semestre foi","{}",160,[100,40,120,200],"40% de 400 = 160.","mt9b")
# n=2
qv(2,"A média das notas 6,5; 7; 8 e 9,5 é","{}",7.75,[8.5,7.5,31,8],"31 ÷ 4 = 7,75.")
qv(2,"A média de cinco números é 12. Retirando-se um deles, igual a 20, a média dos quatro restantes é","{}",10,[12,8,15,16],"(60 − 20) ÷ 4 = 10.")
qv(2,"A média de 4 números é 15. Acrescentando-se um quinto número, 25, a nova média é","{}",17,[20,18,16,15],"(60 + 25) ÷ 5 = 17.")
qv(2,"Um candidato tirou 5 e 7 em duas provas. Para média 7 em três provas, a terceira nota deve ser","{}",9,[7,8,10,6],"21 − 12 = 9.")
qv(2,"Os salários de quatro funcionários são R$ 2.000,00, R$ 2.500,00, R$ 3.000,00 e R$ 4.500,00. O salário médio é","R$ {},00",3000,[2750,3250,3500,12000],"12.000 ÷ 4 = 3.000.")
qv(2,"A média de 6 valores é 8. Dois deles são 10 e 14. A média dos outros quatro é","{}",6,[8,7,9,12],"Soma 48; 48 − 24 = 24; 24 ÷ 4 = 6.")
qv(2,"A mediana do conjunto 8, 3, 9, 5, 1 é","{}",5,[8,3,9,5.2],"Ordenando: 1, 3, 5, 8, 9. O central é 5.")
qv(2,"A idade média de 10 pessoas é 30 anos. Entra uma pessoa de 41 anos. A nova média é","{} anos",31,[30,35.5,41,32],"(300 + 41) ÷ 11 = 31.")
qv(2,"A média de 5 provas foi 7,2. Quatro notas foram 6, 8, 7 e 5. A quinta nota foi","{}",10,[9,8,7.5,9.5],"Soma 36; 36 − 26 = 10.")
qv(2,"Em um gráfico de setores, um setor de 40% corresponde a um ângulo de","{}°",144,[40,100,90,160],"0,40 × 360 = 144.")
qv(2,"A média mensal de vendas em três meses foi 120. Se o quarto mês teve 160, a média dos quatro meses é","{}",130,[140,125,135,150],"(360 + 160) ÷ 4 = 130.")
q(2,"A média aritmética entre 3/4 e 1/4 é",["1/2","1","2","1/4","3/8"],"(3/4 + 1/4) ÷ 2 = 1/2.")
qv(2,"A média aritmética de 0,2; 0,5 e 0,8 é","{}",0.5,[1.5,0.4,0.6,0.3],"1,5 ÷ 3 = 0,5.")
qv(2,"Um aluno tem notas 4, 6 e 8 e quer média 7 em quatro provas. A quarta nota deve ser","{}",10,[7,9,8,6],"28 − 18 = 10.")
qv(2,"Em uma tabela, o valor 1 aparece 3 vezes, o 2 aparece 2 vezes e o 3 aparece 5 vezes. A média é","{}",2.2,[2,2.5,6,1.8],"(3 + 4 + 15) ÷ 10 = 2,2.")
qv(2,"A mediana de 2, 4, 6, 8, 10, 12, 14, 16, 18 e 20 é","{}",11,[10,12,10.5,110],"Média de 10 e 12.")
qv(2,"Um valor passou de 80 para 100. A variação percentual foi de","{}%",25,[20,125,80,10],"20 ÷ 80 = 0,25.")
qv(2,"Segundo o texto, a diferença entre o maior e o menor número mensal de ocorrências é","{}",16,[12,8,20,54],"54 − 38 = 16.","mt9a")
qv(2,"Segundo o texto, se junho tivesse 58 ocorrências, a média dos seis meses seria","{}",48,[46,50,52,58],"(230 + 58) ÷ 6 = 48.","mt9a")
qv(2,"Segundo o texto, o número de ocorrências de trânsito no semestre foi","{}",80,[100,60,40,120],"20% de 400 = 80.","mt9b")
# n=3
qv(3,"A média de 10 números é 8. Cinco deles têm média 6. A média dos outros cinco é","{}",10,[8,7,12,14],"Soma 80; 5 × 6 = 30; restam 50; 50 ÷ 5 = 10.")
qv(3,"A média de 4 números é 10. Retirando-se um, a média dos três restantes é 9. O número retirado é","{}",13,[9,10,12,19],"40 − 27 = 13.")
qv(3,"As médias de A e B, de B e C e de A e C são 12, 14 e 16. O valor de C é","{}",18,[12,16,14,20],"Somas dos pares: 24, 28, 32; total 84 = 2(A + B + C), logo A + B + C = 42. C = 42 − 24 = 18.")
qv(3,"A média dos salários de 20 funcionários é R$ 3.000,00. Entram 5 funcionários com média de R$ 4.000,00. A nova média é","R$ {},00",3200,[3500,3400,3300,3100],"(60.000 + 20.000) ÷ 25 = 3.200.")
qv(3,"Em uma turma, 29 alunos têm idade média 19 e, com o professor, a média passa a ser 20 (30 pessoas). A idade do professor é","{} anos",49,[39,50,45,59],"30 × 20 = 600; 29 × 19 = 551; 600 − 551 = 49.")
qv(3,"A média de cinco números inteiros consecutivos é 12. O maior deles é","{}",14,[12,13,15,16],"Os números são 10, 11, 12, 13, 14.")
qv(3,"A média dos números x, x + 2 e x + 4 é 10. O valor de x é","{}",8,[6,10,4,12],"A média é x + 2 = 10.")
qv(3,"A média de dois números é 15 e a diferença entre eles é 6. O maior é","{}",18,[21,12,16,20],"Soma 30; (30 + 6) ÷ 2 = 18.")
qv(3,"Em um gráfico de barras, os valores são 20, 35 e 45. O maior valor representa, do total, o percentual de","{}%",45,[35,40,50,20],"Total 100; 45 ÷ 100.")
qv(3,"A temperatura média de 7 dias foi 24 °C. Nos seis primeiros, a média foi 23,5 °C. No sétimo dia, a temperatura foi","{} °C",27,[24,25,26,28],"Soma 168; 6 × 23,5 = 141; 168 − 141 = 27.")
qv(3,"A média de n números é 20. Acrescentando o número 26, a média passa a 21. O valor de n é","{}",5,[4,6,7,3],"(20n + 26)/(n + 1) = 21 → n = 5.")
qv(3,"A mediana de 1, 3, 3, 6, 7, 8 e 9 é","{}",6,[3,5.3,7,5],"O quarto valor, em ordem, é 6.")
qv(3,"Um grupo de 3 números tem média 5 e outro de 2 números tem média 10. A média dos cinco juntos é","{}",7,[7.5,8,6,5.5],"(15 + 20) ÷ 5 = 7.")
qv(3,"As ocorrências foram 50, 40 e 60 em três meses seguidos. A variação do segundo para o terceiro mês foi","+{}%",50,[20,10,25,100],"20 ÷ 40 = 0,5.")
qv(3,"Em um gráfico de setores com 600 pessoas, um setor tem 120°. Ele representa","{} pessoas",200,[120,300,100,240],"120/360 = 1/3 de 600.")
qv(3,"A média de uma lista é 15. Se cada valor for multiplicado por 2 e acrescido de 3, a nova média é","{}",33,[30,36,18,45],"15 × 2 + 3 = 33.")
qv(3,"Somando-se 5 a cada número de uma lista, a média da lista","aumenta {}",5,[2.5,10,0,15],"A média acompanha a soma em cada elemento.")
qv(3,"Segundo o texto, para que a média dos seis primeiros meses seja 50, junho deve ter","{} ocorrências",70,[54,58,60,65],"6 × 50 = 300; 300 − 230 = 70.","mt9a")
qv(3,"Segundo o texto, a variação percentual das ocorrências de março para abril foi de","{}%",-8,[-4,8,-10,-12],"(46 − 50) ÷ 50 = −0,08.","mt9a")
qv(3,"Segundo o texto, no gráfico de setores, o ângulo do setor dos furtos é de","{}°",144,[90,160,100,120],"0,40 × 360 = 144.","mt9b")
assert Fr(20+26,1)==46 and mean([20]*5+[26])==21 and (20*5+26)/6==21 and 41+0==41
QQ=fechar()
assert len(QQ)==60, len(QQ)
code,svg=mapa("Média e gráficos: do dado à conclusão",[
 ("ler","Ler tabelas e gráficos",["título, unidades, eixos","setor: 100% = 360°","barras e linhas"],"seção 1"),
 ("media","Média aritmética",["soma ÷ quantidade","soma = média × quantidade","repartir igualmente"],"seção 2"),
 ("mudar","Quando a média muda",["valor que sai","valor que entra","nova soma ÷ nova quantidade"],"seção 2"),
 ("med","Mediana e moda",["mediana: valor do meio","moda: o que mais se repete","média é sensível a extremos"],"seção 2"),
 ("prop","Propriedades",["somar k soma k à média","multiplicar multiplica","média das médias só se iguais"],"seção 3"),
 ("var","Variação",["(final − inicial) ÷ inicial","base = valor inicial","queda e alta não se anulam"],"seção 1")],
 "Na prova: passe pela soma (soma = média × quantidade) e confira a quantidade")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A soma é a ponte entre a média e todos os problemas de entrada e saída de valores.","Fontes: Edital 02/2026, Anexo I. Referências de base: IBGE, <em>Tabulações e gráficos: noções de estatística</em> (apoio didático); Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 11. Exemplos criados para a aula.")
revisao("mt-9","Relação entre grandezas e média aritmética",QQ,list(tx),
 cobertura=["Recorte do edital: tabelas, gráficos e média aritmética simples. Cobertos: leitura de tabelas e de gráficos (barras, linhas e setores), média, relação soma = média × quantidade, mediana, moda, média de grupos, variação percentual."],
 pendencias=["A referência ao IBGE (apoio didático) é genérica; não foi consultada uma publicação específica.","Os gabaritos foram conferidos em parte por código (módulo statistics) e em parte por conta manual. Os gráficos são descritos em texto e tabela; não há figuras desenhadas."],
 fontes_conferidas=[])
gravar("mt-9",aula_html,banco("mt-9",QQ),tx)
