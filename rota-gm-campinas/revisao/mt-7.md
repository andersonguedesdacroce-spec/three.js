# Revisão do posto mt-7: Sistemas de equações do 1º grau

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 7 com texto de apoio (mt7a, mt7b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 6, 7, 8 (questões resolvidas na seção 5).

## Fontes

Fontes: Edital 02/2026, Anexo I. Referências de base: Iezzi, Dolce e Murakami, <em>Fundamentos de Matemática Elementar</em>, v. 1; Dante, <em>Matemática: contexto e aplicações</em>. Exemplos criados para a aula.

## Verificação de cobertura

- Recorte do edital: situações-problema com duas incógnitas. Cobertos: substituição, adição, problemas de moedas, ingressos, rodas, idades, correnteza, mistura, sistema impossível e indeterminado.

## Pontos para revisão (não conferidos na fonte)

- Referências bibliográficas citadas como base; não foram consultadas página a página.
- Os sistemas do banco foram conferidos com um solucionador (regra de Cramer) em código para boa parte das questões; as demais, por conferência manual.

## Aula

**Sistema de equações do 1º grau é o recurso para problemas com duas incógnitas e duas pistas: preços de dois produtos, moedas de dois valores, idades de duas pessoas. A Vunesp cobra a montagem do sistema a partir do texto e sua resolução por substituição ou por adição, além de reconhecer quando o sistema não tem solução ou tem infinitas. Como em toda equação, a parte difícil é traduzir; a conta é curta.**

## 1. Por que duas equações

Uma equação com duas incógnitas, como x + y = 10, tem infinitas soluções: (1, 9), (2, 8), (5, 5) e tantas outras. Para fixar um par só, é preciso uma segunda informação, e a ela corresponde uma segunda equação. O conjunto das duas é um sistema, e a solução é o par (x, y) que satisfaz as duas ao mesmo tempo. Com x + y = 10 e x − y = 2, só o par (6, 4) serve: 6 + 4 = 10 e 6 − 4 = 2.

A imagem geométrica ajuda: cada equação é uma reta, e a solução é o ponto em que as retas se cruzam. Isso explica os dois casos especiais, tratados na seção 4.

## 2. Método da substituição

A ideia é isolar uma incógnita em uma equação e colocar o resultado na outra, que passa a ter só uma incógnita. Considere x + y = 11 e x = y + 3. A segunda já traz x isolado. Trocando na primeira, (y + 3) + y = 11, então 2y + 3 = 11, 2y = 8 e y = 4. De volta a x = y + 3, x = 7. Confira nas duas: 7 + 4 = 11 e 7 = 4 + 3.

Escolha para isolar a incógnita que tem coeficiente 1, porque evita frações. Em 2x + y = 9 e x − y = 0, isole y = 2x − ... ou melhor, perceba que x = y na segunda e troque: 2y + y = 9, y = 3, x = 3.

## 3. Método da adição

A ideia é somar (ou subtrair) as duas equações de modo que uma incógnita desapareça. Em x + y = 10 e x − y = 2, somando termo a termo, 2x = 12 e x = 6; depois, y = 4. Quando os coeficientes não se anulam, multiplica-se uma ou as duas equações por números que os igualem.

Exemplo resolvido. Duas canetas e um lápis custam R$ 7,00, e uma caneta e um lápis custam R$ 5,00. Quanto custa a caneta? Com c a caneta e l o lápis, 2c + l = 7 e c + l = 5. Subtraindo a segunda da primeira, o lápis some: c = 2. Então l = 3.

Outro exemplo. Resolva 3x + 2y = 16 e x + y = 6. Multiplicando a segunda por 2, 2x + 2y = 12. Subtraindo da primeira, x = 4, e então y = 2. Conferindo: 3 × 4 + 2 × 2 = 16.

## 4. Problemas e casos especiais

Para montar o sistema, dê um nome a cada incógnita e escreva uma equação para cada informação do texto. Em problemas de moedas e ingressos, uma equação conta quantos objetos há, e a outra soma os valores.

Exemplo resolvido 1. Em 25 notas de R$ 5,00 e de R$ 10,00, que somam R$ 190,00, quantas notas são de R$ 10,00? Sendo a o número de notas de 5 e b o de 10, a + b = 25 e 5a + 10b = 190. Multiplicando a primeira por 5, 5a + 5b = 125. Subtraindo, 5b = 65 e b = 13. Então a = 12.

Exemplo resolvido 2, com rodas. Em um pátio há 20 veículos, entre carros e motos, e 64 rodas. Quantos carros? Com c carros e m motos, c + m = 20 e 4c + 2m = 64. Multiplicando a primeira por 2, 2c + 2m = 40. Subtraindo, 2c = 24 e c = 12. Então m = 8.

Exemplo resolvido 3, com correnteza. Um barco faz um trecho a favor da correnteza com velocidade 18 km/h e, contra, com 12 km/h. A soma da velocidade do barco b com a da correnteza c é 18, e a diferença é 12. Somando, 2b = 30 e b = 15. Então c = 3.

Os casos especiais aparecem quando as retas não se cruzam num único ponto. Se as retas são paralelas, o sistema é impossível, sem solução: x + y = 3 e 2x + 2y = 8, porque a segunda dá x + y = 4, que contradiz a primeira. Se as retas coincidem, o sistema é possível e indeterminado, com infinitas soluções: x + y = 3 e 2x + 2y = 6, porque a segunda é só a primeira multiplicada por 2. O sistema com um único par é possível e determinado.

## 5. Questões resolvidas

### Questão 1

Duas canetas e um lápis custam R$ 7,00, e uma caneta e um lápis custam R$ 5,00. O preço de uma caneta é

- (A) R$ 3,00
- (B) R$ 1,50
- (C) R$ 2,00
- (D) R$ 2,50
- (E) R$ 4,00

**Resposta: C.** 2c + l = 7 e c + l = 5. Subtraindo, c = 2 (e l = 3).

### Questão 2

Em um pátio há 20 veículos, entre carros e motos, e 64 rodas. O número de motos é

- (A) 12
- (B) 6
- (C) 10
- (D) 14
- (E) 8

**Resposta: E.** c + m = 20 e 4c + 2m = 64. Multiplicando a primeira por 2 e subtraindo, 2c = 24: c = 12 e m = 8.

### Questão 3

A soma de dois números é 40 e a diferença entre eles é 12. O maior deles é

- (A) 26
- (B) 28
- (C) 14
- (D) 24
- (E) 32

**Resposta: A.** x + y = 40 e x − y = 12. Somando, 2x = 52 e x = 26.

### Questão 4

O sistema x + y = 3 e 2x + 2y = 8 é

- (A) possível e determinado.
- (B) possível e indeterminado.
- (C) satisfeito por (1, 2).
- (D) impossível.
- (E) satisfeito por (2, 1).

**Resposta: D.** A segunda equação, dividida por 2, dá x + y = 4, que contradiz x + y = 3. Não há solução.

## 6. Na rotina do guarda

- **Compras:** dois produtos e dois pedidos com quantidades diferentes formam um sistema, como as canetas e os lápis.
- **Pátio e frota:** número de veículos e número de rodas dão o sistema de carros e motos.
- **Rateios desiguais:** duas condições sobre dois valores, como “soma de R$ 1.000,00 e diferença de R$ 300,00”.
- **Idades:** quando a prova dá a relação entre as idades hoje e daqui a alguns anos, monta-se um sistema.

## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Montar duas equações iguais com palavras diferentes | Cada equação deve trazer uma informação nova |
| Esquecer de multiplicar todos os termos ao ajustar coeficientes | Multiplique os dois lados e todos os termos |
| Responder só x quando pedem x + y ou o maior valor | Releia a pergunta antes de responder |
| Trocar o sinal ao subtrair equações | Subtraia termo a termo, com atenção aos negativos |
| Dar por solução um par que só satisfaz uma equação | Teste nas duas equações |
| Achar que todo sistema tem solução única | Se os coeficientes são proporcionais, é impossível ou indeterminado |

## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Sistema | Duas equações; o par que satisfaz as duas |
| Substituição | Isola uma incógnita e troca na outra equação |
| Adição | Soma ou subtrai as equações para eliminar uma incógnita |
| Moedas e ingressos | Uma equação conta objetos; outra soma valores |
| Impossível | Retas paralelas: sem solução |
| Indeterminado | Retas coincidentes: infinitas soluções |
| Conferência | Teste o par nas duas equações |
