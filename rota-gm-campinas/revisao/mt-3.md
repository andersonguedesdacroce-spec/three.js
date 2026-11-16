# Revisão do posto mt-3: Porcentagem

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 9 com texto de apoio (mt3a, mt3b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 5, 7, 8, 9 (questões resolvidas na seção 6).

## Fontes

Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 11 (Matemática comercial); Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.

Conferidas nesta produção:

- Cálculos: assert no script conteudo/mt3/mt3.py.

## Verificação de cobertura

- Recorte do edital: “aumentos, descontos e variações sucessivas”. Cobertos: por cento como fração e decimal, cálculo de parte, taxa e todo, fator multiplicador, variação percentual, variações sucessivas (aumentos e descontos, crescimento composto de 3 períodos), recuperação do valor original, pontos percentuais e mistura.
- Não coberto de propósito: juros compostos com fórmula M = C(1+i)^n em fórmula fechada para períodos longos e logaritmos; ficam fora do nível do cargo.

## Pontos para revisão (não conferidos na fonte)

- Referências bibliográficas (Iezzi et al.; Dante) citadas como base; não foram consultadas página a página.
- Gabaritos e exemplos conferidos por código (Fraction); a redação dos enunciados continua para revisão humana.
- A questão sobre salário líquido usa percentuais de desconto fictícios (11% e 7,5%), sem relação com a tabela real do INSS ou do IR.

## Aula

**Porcentagem é a ferramenta mais cobrada da prova de Matemática, porque aparece em quase tudo: preço, salário, estatística de ocorrências, tabelas e gráficos. A Vunesp cobra quatro habilidades: calcular a porcentagem de um valor, descobrir a taxa ou o total quando se conhece o resto, aplicar aumento e desconto, e encadear variações sucessivas. Os erros de prova quase sempre vêm de uma única confusão, a de somar percentuais que deveriam ser multiplicados. Esta aula constrói a ideia, depois a regra, e fecha com as armadilhas.**

## 1. A ideia de “por cento”

Por cento quer dizer “por cem”. Dizer que 25% dos guardas estão de folga é dizer que, a cada 100 guardas, 25 estão de folga; é a fração 25/100, ou 1/4, ou o decimal 0,25. Porcentagem, fração e decimal são três nomes para a mesma coisa. Para passar de porcentagem a decimal, divide-se por 100, ou seja, anda-se com a vírgula duas casas para a esquerda: 35% = 0,35; 8% = 0,08; 150% = 1,5. Para voltar, multiplica-se por 100.

Calcular uma porcentagem de um valor é multiplicar o valor pelo decimal. A palavra “de” continua sendo multiplicação: 20% de 300 é 0,20 × 300 = 60. Alguns atalhos poupam conta. Para achar 10%, divida por 10. Para 1%, divida por 100. Para 50%, divida por 2; para 25%, divida por 4. Os demais saem por combinação: 15% de 80 é 10% mais a metade de 10%, ou 8 + 4 = 12. Porcentagem acima de 100% é válida e significa mais que o todo: 150% de 40 é 60.

Se o todo é o preço de um produto, 100% é o preço inteiro. Um produto que custa R$ 200,00 e tem 15% de desconto custa 85% do preço original, porque 100% − 15% = 85%. Guarde esta ideia, porque ela vai simplificar tudo mais adiante: em vez de calcular o desconto e subtrair, calcule direto quanto sobra.

## 2. Parte, todo e taxa

Todo problema simples de porcentagem tem três ingredientes: o todo, a parte e a taxa. A relação entre eles é parte = taxa × todo. A pergunta é que ingrediente falta, e há três versões.

Na primeira, falta a parte. Quanto é 30% de 250? A parte é 0,30 × 250 = 75. Na segunda, falta a taxa. 15 é quantos por cento de 60? A taxa é parte ÷ todo = 15 ÷ 60 = 0,25, ou 25%. Na terceira, falta o todo. Se 35% de um número é 70, que número é esse? O todo é parte ÷ taxa = 70 ÷ 0,35 = 200.

A dica de leitura é perguntar “em relação a quê?”. A palavra que vem depois de “de”, ou depois de “em relação a”, é o todo, e é por ele que se divide quando se quer a taxa. Se 8 pessoas são aprovadas num grupo de 32, a taxa de aprovação é 8 ÷ 32 = 25%, e não 32 ÷ 8.

Exemplo resolvido. Em um grupo de 60 guardas, 45% são mulheres. Quantos são homens? Há dois caminhos. No primeiro, calcula-se o número de mulheres, 0,45 × 60 = 27, e subtrai-se: 60 − 27 = 33 homens. No segundo, usa-se o complemento: se 45% são mulheres, 55% são homens, e 0,55 × 60 = 33. O segundo caminho é mais curto e é o que a prova premia.

## 3. Aumento e desconto: o fator multiplicador

Aumentar um valor em 15% é ficar com 100% + 15% = 115% dele, e 115% é 1,15. Descontar 20% é ficar com 100% − 20% = 80% dele, e 80% é 0,80. Esses números, 1,15 e 0,80, são os fatores multiplicadores. Em vez de calcular o aumento e depois somar, multiplica-se uma só vez.

Com taxa de aumento i, o fator é 1 + i. Com taxa de desconto i, o fator é 1 − i. Assim, um produto de R$ 80,00 com aumento de 15% passa a custar 80 × 1,15 = R$ 92,00. Um produto de R$ 150,00 com desconto de 20% passa a custar 150 × 0,80 = R$ 120,00. Aumento de 30% tem fator 1,30; desconto de 15% tem fator 0,85; aumento de 100% tem fator 2, porque o valor dobra.

O fator multiplicador também resolve a pergunta inversa, a de descobrir a variação. Se um valor passou de 80 para 100, o fator é 100 ÷ 80 = 1,25, e a variação é fator − 1 = 0,25, um aumento de 25%. Se passou de 100 para 80, o fator é 0,80, e a variação é −20%, uma queda de 20%. Note que a mesma diferença de 20 unidades vale 25% quando a base é 80 e 20% quando a base é 100. A variação percentual é sempre calculada sobre o valor inicial.

> **Nota:** Variação percentual = (valor final − valor inicial) ÷ valor inicial. A base é o valor de antes, nunca o de depois.

## 4. Variações sucessivas

Quando há dois aumentos, dois descontos ou um aumento seguido de desconto, os percentuais não se somam. O segundo incide sobre o resultado do primeiro, e por isso os fatores se multiplicam. A razão é simples: depois do primeiro aumento, o valor é outro, e a segunda porcentagem é calculada sobre esse valor novo.

O caso que a prova ama é o de um aumento de 20% seguido de um desconto de 20%. Muita gente conclui que o valor volta ao que era. Não volta. Os fatores são 1,20 e 0,80, e 1,20 × 0,80 = 0,96. O resultado final é 96% do valor original, uma queda de 4%. Com um preço de R$ 100,00, o aumento leva a R$ 120,00, e 20% de 120 é 24, que deixa R$ 96,00. O desconto de 20% foi aplicado sobre uma base maior, e por isso tirou mais do que o aumento acrescentou.

O mesmo vale para dois descontos. Um desconto de 10% seguido de outro de 20% tem fator 0,90 × 0,80 = 0,72, e o desconto total é 1 − 0,72 = 28%, não 30%. Dois aumentos de 10% têm fator 1,10 × 1,10 = 1,21, ou seja, aumento total de 21%. Três descontos de 10% têm fator 0,90<sup>3</sup> = 0,729, e o desconto total é 27,1%.

O mesmo raciocínio explica o crescimento composto: um valor que cresce 10% ao mês durante 3 meses fica multiplicado por 1,10<sup>3</sup> = 1,331, ou seja, 33,1% de aumento total, e não 30%.

Exemplo resolvido. O salário de R$ 2.400,00 recebeu um aumento de 15% e, no mês seguinte, outro de 10%. Qual o salário final? Os fatores são 1,15 e 1,10. Então 2.400 × 1,15 = 2.760 e 2.760 × 1,10 = 3.036. O salário final é R$ 3.036,00, e o aumento total foi de 26,5%, e não de 25%, porque 1,15 × 1,10 = 1,265.

## 5. Voltar ao valor original e outras armadilhas

Se um valor foi multiplicado por um fator, para recuperar o original divide-se pelo mesmo fator. Um produto que, depois de um aumento de 25%, custa R$ 150,00, tinha preço original de 150 ÷ 1,25 = R$ 120,00. Um produto que, depois de um desconto de 20%, foi vendido por R$ 144,00, custava 144 ÷ 0,80 = R$ 180,00. O erro típico é calcular 25% de 150 e subtrair, o que dá R$ 112,50, porque o aumento incidiu sobre o valor antigo e não sobre o novo.

Pela mesma lógica, o aumento que desfaz um desconto não é igual ao desconto. Depois de um desconto de 20%, o valor é 0,80 do original, e para voltar a 1 é preciso multiplicar por 1 ÷ 0,80 = 1,25, ou seja, um aumento de 25%. Da mesma forma, um aumento de 25% é desfeito por um desconto de 20%, porque 1,25 × 0,80 = 1.

Outra confusão é entre porcentagem e pontos percentuais. Se a taxa de aprovação subiu de 40% para 55%, a diferença é de 15 pontos percentuais. Já o aumento relativo é de 15 ÷ 40 = 37,5%. Quando o enunciado diz “pontos percentuais”, é a subtração das taxas; quando diz “aumento de X%”, é a variação relativa.

Por fim, em problemas de mistura, como 40 litros de uma solução a 30% de álcool com 60 litros de outra a 20%, somam-se as partes e divide-se pelo total. O álcool é 0,30 × 40 + 0,20 × 60 = 12 + 12 = 24 litros, num total de 100 litros: concentração de 24%. A média simples dos percentuais, 25%, estaria errada, porque as quantidades são diferentes.

## 6. Questões resolvidas

### Questão 1

O preço de uma jaqueta recebeu dois descontos sucessivos, o primeiro de 20% e o segundo de 10%. O desconto total sobre o preço original foi de

- (A) 30%
- (B) 32%
- (C) 27%
- (D) 28%
- (E) 25%

**Resposta: D.** Fatores 0,80 e 0,90: 0,80 × 0,90 = 0,72. O preço final é 72% do original, e o desconto total é 100% − 72% = 28%. Os descontos não se somam.

### Questão 2

Em uma sala, 40% dos candidatos são mulheres. Depois de 10 homens saírem, as mulheres passam a ser 50% dos presentes. O número inicial de candidatos era

- (A) 50
- (B) 40
- (C) 60
- (D) 80
- (E) 100

**Resposta: A.** Seja N o total. Mulheres: 0,4N; homens: 0,6N. Saindo 10 homens, as mulheres (0,4N) igualam os homens restantes (0,6N − 10). Então 0,4N = 0,6N − 10, e 0,2N = 10, logo N = 50. Conferindo: 20 mulheres e 30 homens; saem 10, ficam 20 e 20.

### Questão 3

Depois de um aumento de 25%, um produto passou a custar R$ 150,00. O preço antes do aumento era

- (A) R$ 112,50
- (B) R$ 125,00
- (C) R$ 120,00
- (D) R$ 130,00
- (E) R$ 187,50

**Resposta: C.** O preço novo é 125% do antigo: 1,25 × antigo = 150, então antigo = 150 ÷ 1,25 = 120. O erro seria tirar 25% de 150, que dá 112,50, porque os 25% incidiram sobre o preço antigo.

### Questão 4

A taxa de aprovação em um curso passou de 40% para 55%. É correto afirmar que a taxa

- (A) aumentou 15%, em termos relativos.
- (B) aumentou 15 pontos percentuais, ou 37,5% em termos relativos.
- (C) aumentou 15 pontos percentuais, ou 15% em termos relativos.
- (D) aumentou 37,5 pontos percentuais.
- (E) aumentou 27,5%, em termos relativos.

**Resposta: B.** A diferença entre as taxas é 55 − 40 = 15 pontos percentuais. A variação relativa é 15 ÷ 40 = 0,375, ou 37,5%. Pontos percentuais e porcentagem são medidas diferentes.

## 7. Na rotina do guarda

- **Estatística de ocorrências:** “os furtos caíram 20% em relação ao semestre anterior” exige calcular sobre o valor do semestre anterior. Se foram 250 e caíram 20%, passaram a 200.
- **Compras do órgão:** em uma licitação, dois descontos sucessivos de 10% e 5% não valem 15%; valem 1 − 0,90 × 0,95 = 14,5%.
- **Relatório de efetivo:** “45% do efetivo é feminino” vira número de pessoas só depois de multiplicar pelo total.
- **Orçamento de combustível:** um reajuste de 8% sobre R$ 2.500,00 leva a R$ 2.700,00, e esse novo valor é a base do reajuste seguinte.
- **Leitura de gráficos e tabelas:** “aumentou 10 pontos percentuais” e “aumentou 10%” são afirmações diferentes, e a prova costuma explorar a diferença.

## 8. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Somar 20% e −20% e dizer que volta ao original | Multiplique os fatores: 1,20 × 0,80 = 0,96, queda de 4% |
| Somar 10% e 20% de descontos como 30% | Multiplique 0,90 × 0,80 = 0,72, desconto de 28% |
| Calcular 25% sobre o preço novo para achar o original | Divida o preço novo pelo fator: 150 ÷ 1,25 |
| Calcular a variação sobre o valor final | A base é sempre o valor inicial |
| Confundir pontos percentuais com porcentagem | De 40% para 55% são 15 pontos e 37,5% relativos |
| Fazer a média simples de percentuais com bases diferentes | Some as partes e divida pelo total |
| Achar que 100% mais 100% é o triplo | Aumento de 100% dobra: fator 2 |
| Dar a resposta como fração quando pedem porcentagem | Multiplique por 100 e escreva o símbolo % |

## 9. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Por cento | Fração de denominador 100: 35% = 35/100 = 0,35 |
| Parte, todo e taxa | parte = taxa × todo; taxa = parte ÷ todo; todo = parte ÷ taxa |
| Aumento de i | Fator 1 + i |
| Desconto de i | Fator 1 − i |
| Variação percentual | (final − inicial) ÷ inicial |
| Variações sucessivas | Multiplicam-se os fatores; não se somam as taxas |
| Voltar ao original | Divide-se pelo fator |
| Pontos percentuais | Diferença entre duas taxas |
