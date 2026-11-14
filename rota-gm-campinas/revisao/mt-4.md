# Revisão do posto mt-4: Razão e proporção

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 7 com texto de apoio (mt4a, mt4b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 6, 7, 8 (questões resolvidas na seção 5).

## Fontes

Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 11; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula; resultados recalculados em código.

Conferidas nesta produção:

- Cálculos: assert no script conteudo/mt4/mt4.py.

## Verificação de cobertura

- Recorte do edital: “grandezas diretamente e inversamente proporcionais”. Cobertos: razão, escala, proporção e suas propriedades, grandezas direta e inversamente proporcionais, divisão proporcional direta e inversa.

## Pontos para revisão (não conferidos na fonte)

- Referências bibliográficas citadas como base; não foram consultadas página a página.
- Cálculos conferidos por código; redação para revisão humana. Uma questão (rateio entre 23 ocorrências) usa valor aproximado em reais: conferir.

## Aula

**Razão e proporção é o assunto que explica por que a regra de três funciona. A Vunesp cobra três coisas: calcular e comparar razões (inclusive com unidades diferentes e escalas), resolver proporções e reconhecer se duas grandezas variam na mesma direção ou em direções opostas, para então dividir um valor proporcionalmente. A ideia central cabe em uma frase: duas grandezas são proporcionais quando mudam juntas, mantendo uma relação fixa.**

## 1. Razão: comparar por divisão

Razão entre dois números é o quociente entre eles. Dizer que há 12 guardas para cada 20 viaturas é dizer que a razão entre guardas e viaturas é 12/20, ou 3/5. Lê-se “3 para 5”, e significa que, a cada 3 guardas, há 5 viaturas. A ordem importa: a razão entre viaturas e guardas é 5/3, outro número.

Para comparar, as unidades precisam ser iguais. A razão entre 40 minutos e 2 horas não é 40/2. Primeiro converta: 2 horas são 120 minutos, e a razão é 40/120 = 1/3. Quando as unidades são diferentes de propósito, a razão ganha nome e unidade própria: velocidade é a razão entre distância e tempo (120 km em 2 h dão 60 km/h); densidade é a razão entre massa e volume; escala é a razão entre o desenho e a realidade.

Escala 1:50.000 significa que 1 cm no mapa representa 50.000 cm no terreno. Como 50.000 cm são 500 m, cada centímetro do mapa vale meio quilômetro. Uma distância de 3 cm no mapa equivale a 3 × 500 = 1.500 m, ou 1,5 km. Na escala 1:100, 5 cm no desenho são 500 cm, ou 5 m, no real.

## 2. Proporção: duas razões iguais

Proporção é a igualdade entre duas razões: a/b = c/d. Em 3/4 = 15/20, os dois lados valem 0,75. Os termos de fora, a e d, são os extremos; os de dentro, b e c, são os meios. A propriedade fundamental diz que o produto dos meios é igual ao produto dos extremos: a × d = b × c. No exemplo, 3 × 20 = 4 × 15 = 60. É a conhecida “multiplicação em cruz”, e ela existe porque multiplicar os dois lados da igualdade por b e por d elimina os denominadores.

Para achar o termo que falta, aplique a propriedade. Em 5/x = 10/4, tem-se 10x = 5 × 4 = 20, logo x = 2. Em x/6 = 10/15, tem-se 15x = 60, logo x = 4.

Há uma segunda propriedade, muito usada em divisões: em uma proporção, a soma dos antecedentes está para a soma dos consequentes como cada antecedente para o seu consequente. Em a/b = c/d, vale (a + c)/(b + d) = a/b. Com 3/4 = 15/20, (3 + 15)/(4 + 20) = 18/24 = 3/4.

## 3. Grandezas diretamente e inversamente proporcionais

Duas grandezas são diretamente proporcionais quando, dobrando uma, a outra também dobra; triplicando uma, a outra triplica. A razão entre elas é constante. Oito canetas a R$ 3,00 custam R$ 24,00, e 16 canetas custam R$ 48,00: a razão preço por caneta é sempre 3. O distanciamento acompanha o tempo, a velocidade se mantendo.

Duas grandezas são inversamente proporcionais quando, dobrando uma, a outra cai pela metade; triplicando uma, a outra cai à terça parte. Neste caso, o que se mantém constante é o produto. Se 4 guardas fazem uma vistoria em 6 horas, então 8 guardas, o dobro, fazem em 3 horas, a metade: 4 × 6 = 8 × 3 = 24 “guarda-horas” de trabalho. Velocidade e tempo, para uma mesma distância, são inversamente proporcionais.

A pergunta que decide o caso é: “se uma aumentar, a outra aumenta ou diminui?”. Se as duas crescem juntas, é direta; se uma cresce e a outra decresce, é inversa. Cuidado com o falso proporcional: a idade de uma pessoa e a sua altura crescem juntas, mas não de forma proporcional, porque a razão entre elas não é constante.

> **Nota:** Na direta, as razões são iguais (a/b = c/d). Na inversa, uma razão é igual ao inverso da outra (a/b = d/c), ou seja, o produto é constante.

## 4. Divisão proporcional

Dividir um valor em partes proporcionais é repartir de modo que cada parte siga a razão dada. A ideia é achar a constante k que multiplica cada número do grupo. Dividir R$ 12.000,00 entre três guardas, proporcionalmente ao número de ocorrências que atenderam (5, 7 e 8), funciona assim: some os números, 5 + 7 + 8 = 20; divida o total pela soma, 12.000 ÷ 20 = 600, que é o valor de cada “unidade”; e multiplique: 5 × 600 = 3.000, 7 × 600 = 4.200 e 8 × 600 = 4.800. A soma volta a ser 12.000.

Na divisão inversamente proporcional, usam-se os inversos. Dividir 130 em partes inversamente proporcionais a 2 e 3 é dividir proporcionalmente a 1/2 e 1/3. Com denominador comum, 3/6 e 2/6, as razões são 3 e 2. Soma 5, constante 130 ÷ 5 = 26, partes 78 e 52. Note que a parte maior foi para o menor número, como pede a inversão.

Exemplo resolvido. Dividir 90 em partes proporcionais a 2 e 3. Soma 5; 90 ÷ 5 = 18; partes 36 e 54.

## 5. Questões resolvidas

### Questão 1

Em um mapa de escala 1:25.000, a distância entre dois postos é de 8 cm. A distância real é de

- (A) 200 m.
- (B) 20 km.
- (C) 2 km.
- (D) 3,2 km.
- (E) 2,5 km.

**Resposta: C.** 1 cm no mapa são 25.000 cm, ou 250 m. Então 8 cm são 8 × 250 = 2.000 m = 2 km.

### Questão 2

Quatro guardas fazem uma vistoria em 6 horas. Mantido o ritmo, 6 guardas fariam a mesma vistoria em

- (A) 9 horas.
- (B) 3 horas.
- (C) 5 horas.
- (D) 8 horas.
- (E) 4 horas.

**Resposta: E.** Guardas e tempo são inversamente proporcionais: o produto é constante. 4 × 6 = 24 e 24 ÷ 6 = 4 horas.

### Questão 3

Um prêmio de R$ 1.800,00 será dividido, de forma diretamente proporcional ao tempo de serviço, entre dois guardas de 4 e 5 anos de casa. O guarda de 5 anos receberá

- (A) R$ 1.000,00
- (B) R$ 800,00
- (C) R$ 900,00
- (D) R$ 1.080,00
- (E) R$ 720,00

**Resposta: A.** Soma 4 + 5 = 9; 1.800 ÷ 9 = 200 por unidade. O de 5 anos recebe 5 × 200 = 1.000; o de 4 anos, 800.

### Questão 4

Dividir 130 em partes inversamente proporcionais a 2 e a 3 resulta em

- (A) 52 e 78.
- (B) 65 e 65.
- (C) 80 e 50.
- (D) 78 e 52.
- (E) 60 e 70.

**Resposta: D.** Usam-se os inversos 1/2 e 1/3, que valem 3/6 e 2/6, razões 3 e 2. Constante 130 ÷ 5 = 26: 3 × 26 = 78 e 2 × 26 = 52. A maior parte vai ao menor número.

## 6. Na rotina do guarda

- **Mapa e escala:** ao medir 8 cm entre dois pontos num mapa 1:25.000, a distância real é 8 × 250 = 2.000 m, ou 2 km.
- **Rateio de gratificação:** valor proporcional às ocorrências atendidas, como na divisão proporcional da seção 4.
- **Efetivo e tempo:** inversamente proporcionais; dobrar as equipes em uma vistoria reduz o tempo à metade, mantidas as condições.
- **Consumo e distância:** a viatura que faz 10 km por litro gasta 5 litros em 50 km, e o gasto é diretamente proporcional.

## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Montar a razão sem converter as unidades | Converta antes: 40 min e 2 h viram 40 e 120 |
| Inverter a ordem da razão | A razão “de A para B” é A/B |
| Tratar como direta uma grandeza inversa | Pergunte: aumentando uma, a outra aumenta ou diminui? |
| Dividir inversamente usando os próprios números | Use os inversos e leve a maior parte ao menor número |
| Errar a escala trocando cm por km | 1:50.000 é 1 cm para 500 m |
| Esquecer de conferir a soma das partes | As partes devem somar o total |

## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Razão | Quociente a/b; mesmas unidades |
| Escala | Desenho para real; 1:50.000 é 1 cm para 500 m |
| Proporção | a/b = c/d; a × d = b × c |
| Grandezas diretas | Razão constante; crescem juntas |
| Grandezas inversas | Produto constante; uma cresce, a outra decresce |
| Divisão proporcional | Soma das razões; k = total ÷ soma; parte = razão × k |
| Divisão inversa | Usa os inversos dos números |
