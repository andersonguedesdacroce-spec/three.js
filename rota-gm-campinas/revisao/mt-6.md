# Revisão do posto mt-6: Equações do 1º e do 2º graus

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 8 com texto de apoio (mt6a, mt6b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 6, 7, 8 (questões resolvidas na seção 5).

## Fontes

Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula.

## Verificação de cobertura

- Recorte do edital: montagem e resolução de equações. Cobertos: 1º grau com parênteses e frações, tradução de enunciados (consecutivos, idades, moedas), 2º grau incompleto e completo, discriminante, soma e produto das raízes, equações fracionárias e problemas de geometria e velocidade.

## Pontos para revisão (não conferidos na fonte)

- Referências bibliográficas citadas como base; não foram consultadas página a página.
- Parte dos gabaritos foi conferida por substituição na equação (exemplos e QR) e por asserts no script; as demais por conferência manual. Recomendo uma segunda checagem das questões do banco.

## Aula

**Equação é uma igualdade com um valor desconhecido, e resolvê-la é descobrir esse valor. A Vunesp cobra duas coisas: resolver equações do 1º e do 2º graus e, principalmente, montar a equação a partir de um problema escrito. A conta costuma ser curta; o trabalho difícil é traduzir o texto. Esta aula começa pela imagem da balança, passa à resolução passo a passo e dedica uma seção inteira à tradução do enunciado.**

## 1. A equação como uma balança

Pense numa balança de dois pratos em equilíbrio. Num prato há uma caixa de peso desconhecido x mais 3 pesos de 1 kg; no outro, 10 pesos de 1 kg. A balança só continua equilibrada se, para qualquer coisa que se faça num prato, se faça a mesma coisa no outro. Tirando 3 kg de cada lado, resta x = 7. Essa é toda a técnica: aplicar a mesma operação nos dois lados para isolar a incógnita.

Na prática, a operação inversa isola o x. Se algo foi somado, subtrai-se; se foi multiplicado, divide-se. Em x + 3 = 10, subtrai-se 3: x = 7. Em 3x = 21, divide-se por 3: x = 7. Em x/4 = 6, multiplica-se por 4: x = 24. É o que se resume na frase “muda de lado, muda de sinal”: ela é só um atalho para somar ou subtrair o mesmo valor dos dois lados.

## 2. Equação do 1º grau, passo a passo

A equação do 1º grau tem a forma ax + b = 0, com a diferente de zero, e uma única solução, x = −b/a. Quando a equação vem desarrumada, a ordem é sempre a mesma: eliminar parênteses, eliminar denominadores multiplicando tudo pelo MMC, juntar os termos com x de um lado e os números do outro, e dividir pelo coeficiente de x.

Exemplo resolvido 1. Resolva 3(x − 2) = 2x + 5. Eliminando os parênteses, 3x − 6 = 2x + 5. Passando 2x para a esquerda e −6 para a direita, 3x − 2x = 5 + 6, ou seja, x = 11. Conferindo: 3 × 9 = 27 e 2 × 11 + 5 = 27.

Exemplo resolvido 2, com frações. Resolva x/3 + x/2 = 10. O MMC de 3 e 2 é 6. Multiplicando tudo por 6, 2x + 3x = 60, então 5x = 60 e x = 12. Conferindo: 12/3 + 12/2 = 4 + 6 = 10.

Sempre vale substituir a resposta na equação original: é a conferência que a prova permite.

## 3. Do texto à equação

Quase toda questão cobra a tradução. O método é escolher a incógnita, escrever o que o texto diz sobre ela e montar a igualdade. Algumas traduções aparecem o tempo todo: “o dobro de um número” é 2x; “o triplo” é 3x; “a metade” é x/2; “um número aumentado de 5” é x + 5; “a soma de dois números consecutivos” é x + (x + 1); “três números consecutivos” são x, x + 1 e x + 2; “a idade de Ana daqui a 5 anos” é x + 5; “há 3 anos” é x − 3; “é igual a” ou “resulta em” é o sinal de igual.

Exemplo resolvido 1. A soma de três números inteiros consecutivos é 72. Quais são eles? Sendo x o menor, o texto diz x + (x + 1) + (x + 2) = 72. Então 3x + 3 = 72, 3x = 69, x = 23. Os números são 23, 24 e 25.

Exemplo resolvido 2. Cinco coletes e um frete de R$ 30,00 custaram R$ 280,00. Qual o preço de cada colete? Com x o preço do colete, 5x + 30 = 280, então 5x = 250 e x = 50.

Exemplo resolvido 3. Em 50 moedas de 5 e de 10 centavos, que somam R$ 3,50, quantas são de 10 centavos? Seja a o número de moedas de 5 centavos. As de 10 centavos são 50 − a, e o valor em centavos fica 5a + 10(50 − a) = 350. Então 500 − 5a = 350, 5a = 150 e a = 30. As de 10 centavos são 50 − 30 = 20.

## 4. Equação do 2º grau

A equação do 2º grau tem a forma ax<sup>2</sup> + bx + c = 0, com a diferente de zero, e pode ter duas soluções, uma ou nenhuma entre os reais. Os casos incompletos resolvem-se sem fórmula. Se falta o termo em x (b = 0), isola-se o quadrado: x<sup>2</sup> = 49 dá x = 7 ou x = −7, porque ambos ao quadrado dão 49. Se falta o termo independente (c = 0), coloca-se x em evidência: x<sup>2</sup> − 5x = 0 vira x(x − 5) = 0, e um produto é zero quando um dos fatores é zero, então x = 0 ou x = 5.

Para a equação completa, usa-se a fórmula de Bhaskara. Calcula-se o discriminante Δ = b<sup>2</sup> − 4ac, que diz quantas soluções existem: Δ positivo dá duas soluções reais diferentes; Δ igual a zero dá uma solução dupla; Δ negativo não dá solução real. As soluções são x = (−b ± √Δ) / (2a).

Exemplo resolvido. Resolva 2x<sup>2</sup> − 3x − 2 = 0. Aqui a = 2, b = −3 e c = −2. Δ = (−3)<sup>2</sup> − 4 × 2 × (−2) = 9 + 16 = 25 e √Δ = 5. Então x = (3 ± 5) / 4, ou seja, x = 8/4 = 2 e x = −2/4 = −1/2.

Há um caminho mais rápido em muitas questões, o da soma e produto das raízes. Se x<sub>1</sub> e x<sub>2</sub> são as raízes, então x<sub>1</sub> + x<sub>2</sub> = −b/a e x<sub>1</sub> × x<sub>2</sub> = c/a. Em x<sup>2</sup> − 7x + 12 = 0, a soma é 7 e o produto é 12, o que leva a 3 e 4, porque 3 + 4 = 7 e 3 × 4 = 12. Essas relações permitem dizer a soma ou o produto das raízes sem resolver a equação.

> **Nota:** Em problemas, nem toda raiz serve. Se a incógnita é uma idade, um comprimento ou um número de pessoas, a raiz negativa é descartada.

## 5. Questões resolvidas

### Questão 1

A solução da equação 3(x − 2) = 2x + 5 é

- (A) −1
- (B) 7
- (C) 11
- (D) 3
- (E) 1

**Resposta: C.** 3x − 6 = 2x + 5, então 3x − 2x = 5 + 6, x = 11.

### Questão 2

As raízes da equação x<sup>2</sup> − 7x + 12 = 0 são

- (A) −3 e −4
- (B) 2 e 6
- (C) 1 e 12
- (D) −3 e 4
- (E) 3 e 4

**Resposta: E.** Soma 7 e produto 12: 3 e 4.

### Questão 3

A soma de três números inteiros consecutivos é 72. O menor deles é

- (A) 24
- (B) 23
- (C) 22
- (D) 21
- (E) 25

**Resposta: B.** x + (x + 1) + (x + 2) = 72, 3x + 3 = 72, x = 23.

### Questão 4

As raízes da equação 2x<sup>2</sup> − 3x − 2 = 0 são

- (A) −2 e 1/2
- (B) 3 e −2
- (C) 1 e −2
- (D) 2 e −1/2
- (E) 2 e 1/2

**Resposta: D.** Δ = 9 + 16 = 25; x = (3 ± 5)/4: 2 e −1/2.

## 6. Na rotina do guarda

- **Compras e orçamento:** valor unitário desconhecido, frete fixo e total conhecido formam uma equação do 1º grau, como a dos coletes.
- **Rateios:** dividir uma verba entre um número de guardas que muda leva a equações com fração, resolvidas ao multiplicar tudo pelo MMC.
- **Áreas de terrenos e salas:** lados que se relacionam por “3 m a mais” levam a equações do 2º grau.
- **Escalas e tempos:** distâncias e velocidades entre duas viaturas também levam a equações.

## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Errar o sinal ao mudar de lado | Subtraia ou some o mesmo valor dos dois lados |
| Esquecer de multiplicar todos os termos pelo MMC | Multiplique também os termos sem denominador |
| Aplicar Bhaskara com o sinal de b errado | Calcule −b com cuidado: se b = −3, −b = 3 |
| Dividir os dois lados por x e perder a raiz x = 0 | Coloque x em evidência em vez de dividir |
| Aceitar raiz negativa para comprimento ou idade | Descarte a raiz que não faz sentido |
| Traduzir mal “a mais que” e “vezes mais” | Escreva a relação em símbolos antes de calcular |

## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| 1º grau | Operação inversa dos dois lados; x = −b/a |
| Frações | Multiplicar tudo pelo MMC |
| Tradução | Defina a incógnita; “é” vira igual |
| 2º grau incompleto | b = 0: raiz quadrada; c = 0: x em evidência |
| Bhaskara | Δ = b² − 4ac; x = (−b ± √Δ) / 2a |
| Soma e produto | x₁ + x₂ = −b/a; x₁ × x₂ = c/a |
| Conferência | Substitua na equação original |
