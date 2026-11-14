import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _geo import *
b=B(); q=b.q
LEAD="Cidades limítrofes são os municípios que fazem divisa com Campinas. A Vunesp gosta deste tema porque mistura geografia com pegadinha: Americana, Nova Odessa e Vinhedo estão na RMC mas não encostam em Campinas; Itupeva encosta em Campinas mas não está na RMC. A aula organiza as divisas como uma rosa dos ventos, que é a forma mais fácil de memorizar, e mostra onde as fontes divergem."
S={}
S[1]="## 1. As divisas de Campinas, pela rosa dos ventos\n\n"+C("Wikipédia, verbete Campinas, quadro de informações","Municípios limítrofes: Norte: Jaguariúna; Nordeste: Pedreira; Leste: Morungaba; Sudeste: Valinhos; Sul: Indaiatuba e Itupeva; Sudoeste: Monte Mor; Oeste: Sumaré e Hortolândia; Noroeste: Paulínia.")+"\n\n"+C("Wikidata, propriedade 'faz fronteira com'","Municípios que fazem fronteira com Campinas segundo o Wikidata: Paulínia, Indaiatuba, Itupeva, Monte Mor, Pedreira, Sumaré, Hortolândia, Valinhos, Morungaba, Jaguariúna.")+"""

**O que é, em uma frase:** cidades limítrofes são os municípios que têm divisa territorial direta com Campinas.

**Regra principal (10 municípios, nas duas fontes consultadas):**

| Direção | Município |
| --- | --- |
| Norte | Jaguariúna |
| Nordeste | Pedreira |
| Leste | Morungaba |
| Sudeste | Valinhos |
| Sul | Indaiatuba e Itupeva |
| Sudoeste | Monte Mor |
| Oeste | Sumaré e Hortolândia |
| Noroeste | Paulínia |

**Macete:** comece pelo norte e gire no sentido horário: "*Jaguar Pede Morango em Valinhos, Indo a Itupeva, Monte Sumaré, Horta e Paulínia*" (Jaguariúna, Pedreira, Morungaba, Valinhos, Indaiatuba, Itupeva, Monte Mor, Sumaré, Hortolândia, Paulínia).
"""
S[2]="## 2. Divergência entre fontes: Itatiba\n\n"+C("Wikipédia, verbete Campinas, seção Geografia","Seus municípios limítrofes são Paulínia, Jaguariúna e Pedreira, a norte; Morungaba, Itatiba e Valinhos, a leste; Itupeva, Indaiatuba e Monte Mor, a sul; e Hortolândia e Sumaré, a oeste.")+"""

O texto da seção Geografia da mesma enciclopédia inclui Itatiba entre os limítrofes, a leste, chegando a 11 municípios; já o quadro de informações e o Wikidata trazem 10, sem Itatiba. A diferença é pequena e está na região rural de Joaquim Egídio e Sousas, a leste.

**Como agir na prova:** a Vunesp costuma cobrar os casos indiscutíveis. Se uma alternativa listar Itatiba como limítrofe e outra trouxer um município claramente fora (Americana, Vinhedo, Jundiaí), a errada é a de fora. Se a questão depender só de Itatiba, confira a fonte que a própria banca indicar.
"""
S[3]="## 3. Limítrofe x metropolitano: a tabela que a banca confunde\n\n"+C("AGEMCAMP, página RMC","Americana, Artur Nogueira, Campinas, Cosmópolis, Engenheiro Coelho, Holambra, Hortolândia, Indaiatuba, Itatiba, Jaguariúna, Monte Mor, Morungaba, Nova Odessa, Paulínia, Pedreira, Santa Bárbara d’Oeste, Santo Antônio de Posse, Sumaré, Valinhos e Vinhedo.")+"""

| Situação | Municípios |
| --- | --- |
| Limítrofe **e** RMC | Jaguariúna, Pedreira, Morungaba, Valinhos, Indaiatuba, Monte Mor, Sumaré, Hortolândia, Paulínia |
| Limítrofe, **mas fora** da RMC | Itupeva |
| RMC, **mas não** limítrofe | Americana, Artur Nogueira, Cosmópolis, Engenheiro Coelho, Holambra, Nova Odessa, Santa Bárbara d’Oeste, Santo Antônio de Posse, Vinhedo (e Itatiba, conforme a fonte) |
| Nem limítrofe nem RMC | Jundiaí, Louveira, Piracicaba, Limeira, Atibaia |

**Pegadinha clássica:** Vinhedo fica pertinho, entre Valinhos e Jundiaí, mas não encosta em Campinas. Americana e Nova Odessa ficam além de Sumaré.
"""
S[5]="""## 5. Na rotina do guarda

- **Divisa e competência:** a Guarda Municipal atua no território do Município; numa ocorrência na divisa com Sumaré ou Hortolândia, o guarda aciona a guarda ou a polícia do município vizinho.
- **Conurbação a oeste:** com Sumaré e Hortolândia a mancha urbana é contínua; o limite pode ser uma rua.
- **Divisas rurais a leste:** com Morungaba e Pedreira, as divisas passam por áreas rurais e de proteção ambiental.
- **Sul:** Indaiatuba e Itupeva fazem divisa na região de Viracopos e do Distrito Industrial.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Vinhedo | Não faz divisa com Campinas |
| Americana, Nova Odessa | Não fazem divisa |
| Itupeva | Faz divisa, mas não é RMC |
| Jundiaí | Nem divisa nem RMC |
| Norte | Jaguariúna |
| Sudeste | Valinhos |
| Sul | Indaiatuba e Itupeva |
| Oeste | Sumaré e Hortolândia |
| Noroeste | Paulínia |
| Itatiba | Fontes divergem: confira a fonte indicada pela banca |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Total | 10 limítrofes (11 se incluir Itatiba) |
| N / NE / L | Jaguariúna / Pedreira / Morungaba |
| SE / S | Valinhos / Indaiatuba e Itupeva |
| SO / O / NO | Monte Mor / Sumaré e Hortolândia / Paulínia |
| Limítrofe fora da RMC | Itupeva |
| RMC sem divisa | Americana, Nova Odessa, Vinhedo, Cosmópolis e outros |
"""
QR=[("Questão 1","Faz divisa com Campinas ao norte o município de",["Jaguariúna.","Americana.","Vinhedo.","Jundiaí.","Nova Odessa."],0,"Quadro de informações: Norte, Jaguariúna."),
("Questão 2","Assinale o município que NÃO faz divisa com Campinas.",["Vinhedo.","Valinhos.","Sumaré.","Paulínia.","Indaiatuba."],1,"Vinhedo não é limítrofe."),
("Questão 3","A oeste, Campinas faz divisa com",["Sumaré e Hortolândia.","Valinhos e Vinhedo.","Pedreira e Morungaba.","Jaguariúna e Paulínia.","Itupeva e Indaiatuba."],2,"Quadro de informações."),
("Questão 4","Faz divisa com Campinas, mas não integra a Região Metropolitana de Campinas, o município de",["Itupeva.","Valinhos.","Paulínia.","Hortolândia.","Monte Mor."],3,"Itupeva fica fora da RMC.")]
t1="<strong>Perseguição a oeste</strong><br><br>Uma equipe da Guarda Municipal de Campinas acompanhava um veículo que seguia pela região oeste da cidade e cruzou a divisa municipal."
t2="<strong>Mapa da sala</strong><br><br>Em um treinamento da guarda, o instrutor pediu que os alunos listassem os municípios vizinhos de Campinas ao sul."
t3="<strong>Lista errada</strong><br><br>Um candidato listou como cidades limítrofes de Campinas: Valinhos, Vinhedo, Sumaré, Paulínia e Americana."
tx={"geo2a":t1,"geo2b":t2,"geo2c":t3}
# n=1
q(1,"Faz divisa com Campinas a nordeste o município de",["Pedreira.","Vinhedo.","Americana.","Jundiaí.","Itu."],"Quadro de informações.")
q(1,"Faz divisa com Campinas a leste o município de",["Morungaba.","Americana.","Sumaré.","Monte Mor.","Paulínia."],"Quadro de informações.")
q(1,"Faz divisa com Campinas a sudeste o município de",["Valinhos.","Sumaré.","Paulínia.","Monte Mor.","Jaguariúna."],"Quadro de informações.")
q(1,"Fazem divisa com Campinas ao sul os municípios de",["Indaiatuba e Itupeva.","Sumaré e Hortolândia.","Pedreira e Morungaba.","Jaguariúna e Paulínia.","Americana e Nova Odessa."],"Quadro de informações.")
q(1,"Faz divisa com Campinas a sudoeste o município de",["Monte Mor.","Pedreira.","Jaguariúna.","Morungaba.","Vinhedo."],"Quadro de informações.")
q(1,"Faz divisa com Campinas a noroeste o município de",["Paulínia.","Valinhos.","Indaiatuba.","Morungaba.","Itupeva."],"Quadro de informações.")
q(1,"É município limítrofe de Campinas",["Hortolândia.","Americana.","Vinhedo.","Jundiaí.","Limeira."],"Hortolândia, a oeste.")
q(1,"É município limítrofe de Campinas",["Indaiatuba.","Nova Odessa.","Holambra.","Cosmópolis.","Artur Nogueira."],"Indaiatuba, ao sul.")
q(1,"NÃO é município limítrofe de Campinas",["Americana.","Sumaré.","Paulínia.","Pedreira.","Monte Mor."],"Americana não faz divisa.")
q(1,"NÃO é município limítrofe de Campinas",["Jundiaí.","Valinhos.","Itupeva.","Jaguariúna.","Hortolândia."],"Jundiaí não faz divisa.")
q(1,"NÃO é município limítrofe de Campinas",["Nova Odessa.","Morungaba.","Indaiatuba.","Monte Mor.","Pedreira."],"Nova Odessa não faz divisa.")
q(1,"Segundo o Wikidata e o quadro de informações da enciclopédia, Campinas tem",["10 municípios limítrofes.","3 municípios limítrofes.","20 municípios limítrofes.","5 municípios limítrofes.","1 município limítrofe."],"Dez municípios.")
q(1,"Valinhos fica, em relação a Campinas, a",["sudeste.","norte.","oeste.","noroeste.","nordeste."],"Quadro de informações.")
q(1,"Jaguariúna fica, em relação a Campinas, ao",["norte.","sul.","oeste.","sudeste.","sudoeste."],"Quadro de informações.")
q(1,"Paulínia fica, em relação a Campinas, a",["noroeste.","sudeste.","sul.","leste.","nordeste."],"Quadro de informações.")
q(1,"Sumaré fica, em relação a Campinas, a",["oeste.","leste.","norte.","sul.","nordeste."],"Quadro de informações.")
q(1,"Indaiatuba fica, em relação a Campinas, ao",["sul.","norte.","leste.","noroeste.","nordeste."],"Quadro de informações.")
q(1,"No texto da perseguição a oeste, o veículo pode ter cruzado a divisa com",["Sumaré ou Hortolândia.","Valinhos ou Vinhedo.","Pedreira ou Morungaba.","Jaguariúna ou Pedreira.","Indaiatuba ou Itupeva."],"A oeste: Sumaré e Hortolândia.","geo2a")
q(1,"No texto do mapa da sala, os municípios vizinhos de Campinas ao sul são",["Indaiatuba e Itupeva.","Jaguariúna e Paulínia.","Sumaré e Hortolândia.","Pedreira e Morungaba.","Valinhos e Vinhedo."],"Quadro de informações.","geo2b")
q(1,"No texto da lista errada, os municípios que NÃO fazem divisa com Campinas são",["Vinhedo e Americana.","Valinhos e Sumaré.","Paulínia e Valinhos.","Sumaré e Paulínia.","Valinhos e Americana."],"Vinhedo e Americana não são limítrofes.","geo2c")
# n=2
q(2,"Assinale a alternativa que traz apenas municípios limítrofes de Campinas.",["Jaguariúna, Pedreira e Morungaba.","Jaguariúna, Americana e Morungaba.","Vinhedo, Pedreira e Morungaba.","Jundiaí, Valinhos e Sumaré.","Nova Odessa, Paulínia e Monte Mor."],"Americana, Vinhedo, Jundiaí e Nova Odessa não são limítrofes.")
q(2,"Assinale a alternativa que traz apenas municípios limítrofes de Campinas.",["Monte Mor, Sumaré e Hortolândia.","Monte Mor, Americana e Hortolândia.","Cosmópolis, Sumaré e Hortolândia.","Sumaré, Nova Odessa e Paulínia.","Vinhedo, Valinhos e Itupeva."],"Americana, Cosmópolis, Nova Odessa e Vinhedo não são limítrofes.")
q(2,"O município de Itupeva, em relação a Campinas,",["faz divisa ao sul, mas não integra a RMC.","faz divisa e integra a RMC.","não faz divisa, mas integra a RMC.","não faz divisa nem integra a RMC.","é distrito de Campinas."],"Itupeva é limítrofe fora da RMC.")
q(2,"O município de Vinhedo, em relação a Campinas,",["integra a RMC, mas não faz divisa.","faz divisa e integra a RMC.","faz divisa, mas não integra a RMC.","não faz divisa nem integra a RMC.","é distrito de Campinas."],"Vinhedo é RMC sem divisa.")
q(2,"O município de Americana, em relação a Campinas,",["integra a RMC, mas não faz divisa.","faz divisa a oeste.","faz divisa ao norte.","não integra a RMC.","é distrito de Campinas."],"Americana é RMC sem divisa.")
q(2,"O município de Jundiaí, em relação a Campinas,",["não faz divisa nem integra a RMC.","faz divisa ao sul.","integra a RMC.","é distrito de Campinas.","faz divisa e integra a RMC."],"Jundiaí não é limítrofe nem RMC.")
q(2,"Dos municípios limítrofes de Campinas, o único que NÃO integra a RMC é",["Itupeva.","Indaiatuba.","Monte Mor.","Pedreira.","Morungaba."],"Os demais estão entre os 20.")
q(2,"Fazem divisa com Campinas, entre outros, os municípios de",["Pedreira e Morungaba, na porção norte e leste.","Americana e Nova Odessa, a oeste.","Vinhedo e Louveira, ao sul.","Limeira e Piracicaba, a noroeste.","Atibaia e Bragança, a leste."],"Pedreira (NE) e Morungaba (L).")
q(2,"Segundo o texto da seção Geografia da enciclopédia, a leste de Campinas ficam Morungaba, Itatiba e",["Valinhos.","Sumaré.","Paulínia.","Monte Mor.","Hortolândia."],"Wikipédia, seção Geografia.")
q(2,"As fontes consultadas divergem quanto à inclusão de qual município entre os limítrofes de Campinas?",["Itatiba.","Valinhos.","Sumaré.","Paulínia.","Indaiatuba."],"Seção Geografia inclui Itatiba; quadro e Wikidata não.")
q(2,"Entre os limítrofes de Campinas, o que está na direção nordeste e integra a RMC é",["Pedreira.","Sumaré.","Monte Mor.","Hortolândia.","Indaiatuba."],"Pedreira, a nordeste.")
q(2,"Os municípios limítrofes de Campinas a oeste, com os quais há forte conurbação, são",["Sumaré e Hortolândia.","Valinhos e Vinhedo.","Jaguariúna e Pedreira.","Morungaba e Itatiba.","Indaiatuba e Itupeva."],"Quadro de informações.")
q(2,"Assinale a alternativa que traz um município limítrofe e outro não limítrofe, nessa ordem.",["Valinhos e Vinhedo.","Vinhedo e Valinhos.","Americana e Sumaré.","Jundiaí e Itupeva.","Nova Odessa e Paulínia."],"Valinhos é limítrofe; Vinhedo não.")
q(2,"Monte Mor faz divisa com Campinas a",["sudoeste.","nordeste.","norte.","leste.","sudeste."],"Quadro de informações.")
q(2,"Morungaba faz divisa com Campinas a",["leste.","oeste.","sul.","noroeste.","sudoeste."],"Quadro de informações.")
q(2,"Pedreira faz divisa com Campinas a",["nordeste.","sudoeste.","sul.","oeste.","sudeste."],"Quadro de informações.")
q(2,"Hortolândia faz divisa com Campinas a",["oeste.","leste.","sul.","nordeste.","sudeste."],"Quadro de informações.")
q(2,"No texto da perseguição a oeste, se o veículo seguisse a noroeste, cruzaria a divisa com",["Paulínia.","Valinhos.","Indaiatuba.","Pedreira.","Morungaba."],"Noroeste: Paulínia.","geo2a")
q(2,"No texto do mapa da sala, dos dois municípios do sul, o que não integra a RMC é",["Itupeva.","Indaiatuba.","os dois.","nenhum.","Valinhos."],"Itupeva fica fora da RMC.","geo2b")
q(2,"No texto da lista errada, os municípios corretamente listados como limítrofes são",["Valinhos, Sumaré e Paulínia.","Vinhedo e Americana.","apenas Valinhos.","todos os cinco.","nenhum."],"Vinhedo e Americana não fazem divisa.","geo2c")
# n=3
q(3,"Assinale a alternativa correta.",["Campinas faz divisa com Jaguariúna ao norte, Valinhos a sudeste e Paulínia a noroeste.","Campinas faz divisa com Vinhedo ao sul.","Campinas faz divisa com Americana a oeste.","Campinas faz divisa com Jundiaí ao sul.","Campinas faz divisa com Nova Odessa a noroeste."],"Quadro de informações.")
q(3,"Considere. I. Itupeva é limítrofe e não integra a RMC. II. Vinhedo é limítrofe. III. Monte Mor é limítrofe. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Vinhedo não é limítrofe.")
q(3,"Assinale a INCORRETA.",["Americana faz divisa com Campinas.","Sumaré faz divisa com Campinas.","Hortolândia faz divisa com Campinas.","Paulínia faz divisa com Campinas.","Indaiatuba faz divisa com Campinas."],"Americana não faz divisa.")
q(3,"Partindo do norte e girando no sentido horário, a sequência correta de municípios limítrofes é",["Jaguariúna, Pedreira, Morungaba, Valinhos, Indaiatuba e Itupeva, Monte Mor, Sumaré e Hortolândia, Paulínia.","Paulínia, Pedreira, Valinhos, Jaguariúna, Morungaba.","Valinhos, Vinhedo, Jundiaí, Itupeva.","Sumaré, Americana, Nova Odessa, Paulínia.","Jaguariúna, Americana, Vinhedo, Itupeva."],"Rosa dos ventos do quadro de informações.")
q(3,"Assinale a alternativa que traz apenas municípios da RMC que NÃO fazem divisa com Campinas.",["Americana, Nova Odessa e Vinhedo.","Americana, Sumaré e Vinhedo.","Valinhos, Nova Odessa e Vinhedo.","Paulínia, Americana e Holambra.","Itupeva, Americana e Vinhedo."],"Sumaré, Valinhos e Paulínia são limítrofes; Itupeva não é RMC.")
q(3,"Assinale a alternativa que traz apenas municípios que fazem divisa com Campinas e integram a RMC.",["Jaguariúna, Pedreira e Indaiatuba.","Jaguariúna, Itupeva e Indaiatuba.","Vinhedo, Pedreira e Indaiatuba.","Americana, Pedreira e Indaiatuba.","Jundiaí, Pedreira e Valinhos."],"Itupeva, Vinhedo, Americana e Jundiaí não atendem aos dois requisitos.")
q(3,"Se um município está a sudeste de Campinas e é limítrofe, trata-se de",["Valinhos.","Sumaré.","Paulínia.","Monte Mor.","Pedreira."],"Quadro de informações.")
q(3,"Se um município está ao sul de Campinas, é limítrofe e integra a RMC, trata-se de",["Indaiatuba.","Itupeva.","Jundiaí.","Vinhedo.","Louveira."],"Itupeva é limítrofe fora da RMC.")
q(3,"O número de municípios limítrofes de Campinas, considerando a inclusão de Itatiba feita no texto da seção Geografia, seria de",["11.","10.","9.","20.","5."],"Dez mais Itatiba.")
q(3,"Ao norte e ao noroeste, Campinas faz divisa, respectivamente, com",["Jaguariúna e Paulínia.","Paulínia e Jaguariúna.","Pedreira e Sumaré.","Valinhos e Monte Mor.","Indaiatuba e Hortolândia."],"Quadro de informações.")
q(3,"A sudoeste e a oeste, Campinas faz divisa, respectivamente, com",["Monte Mor e Sumaré/Hortolândia.","Sumaré e Monte Mor.","Indaiatuba e Valinhos.","Paulínia e Jaguariúna.","Itupeva e Pedreira."],"Quadro de informações.")
q(3,"Na região leste de Campinas, onde ficam Sousas e Joaquim Egídio, a divisa é com",["Morungaba (e, conforme a fonte, Itatiba).","Sumaré e Hortolândia.","Monte Mor.","Paulínia.","Indaiatuba."],"Leste: Morungaba; Itatiba conforme a seção Geografia.")
q(3,"A forte conurbação a oeste de Campinas ocorre com",["Sumaré e Hortolândia.","Morungaba e Pedreira.","Jaguariúna.","Itupeva.","Indaiatuba."],"Mancha urbana contínua a oeste.")
q(3,"Entre os limítrofes de Campinas, os que têm divisa em área predominantemente rural a leste e nordeste são",["Morungaba e Pedreira.","Sumaré e Hortolândia.","Valinhos e Vinhedo.","Americana e Nova Odessa.","Paulínia e Monte Mor."],"Leste e nordeste rurais.")
q(3,"No texto da perseguição a oeste, a guarda deve observar que, ao cruzar a divisa, o veículo entra no território de",["outro município, cuja guarda ou polícia deve ser acionada.","Campinas ainda.","um distrito de Campinas.","um bairro de Campinas.","território federal."],"Divisa municipal.","geo2a")
q(3,"No texto da perseguição a oeste, a mancha urbana contínua entre Campinas e Sumaré é exemplo de",["conurbação.","desertificação.","êxodo rural.","emancipação.","plebiscito."],"Conurbação.","geo2a")
q(3,"No texto do mapa da sala, se o instrutor perguntasse pelos vizinhos a leste, a resposta segura seria",["Morungaba.","Sumaré.","Monte Mor.","Paulínia.","Itupeva."],"Leste: Morungaba.","geo2b")
q(3,"No texto da lista errada, a correção mais simples é trocar Vinhedo e Americana por, por exemplo,",["Hortolândia e Indaiatuba.","Jundiaí e Nova Odessa.","Holambra e Cosmópolis.","Louveira e Limeira.","Itu e Salto."],"Hortolândia e Indaiatuba são limítrofes.","geo2c")
q(3,"No texto da lista errada, Vinhedo é município da RMC que fica entre Valinhos e Jundiaí, e, quanto a Campinas,",["não faz divisa.","faz divisa a leste.","faz divisa ao sul.","é distrito.","é bairro."],"Vinhedo não é limítrofe.","geo2c")
q(3,"No texto da lista errada, Americana integra a RMC, mas fica além de",["Sumaré e Nova Odessa, sem divisa com Campinas.","Valinhos.","Jaguariúna.","Morungaba.","Indaiatuba."],"Americana não é limítrofe.","geo2c")
b.fim()
code,svg=mapa("Cidades limítrofes de Campinas",[
 ("n","Norte e nordeste",["Jaguariúna (N)","Pedreira (NE)"],"seção 1"),
 ("l","Leste e sudeste",["Morungaba (L)","Valinhos (SE)","Itatiba: fontes divergem"],"seção 1 e 2"),
 ("s","Sul e sudoeste",["Indaiatuba e Itupeva (S)","Monte Mor (SO)"],"seção 1"),
 ("o","Oeste e noroeste",["Sumaré e Hortolândia (O)","Paulínia (NO)"],"seção 1"),
 ("x","Limítrofe fora da RMC",["Itupeva"],"seção 3"),
 ("y","RMC sem divisa",["Americana, Nova Odessa","Vinhedo, Cosmópolis"],"seção 3")],
 "Na prova: rosa dos ventos e as pegadinhas Itupeva e Vinhedo")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A rosa dos ventos organiza os 10 vizinhos; as duas últimas caixas trazem as pegadinhas.","Fontes: Edital 02/2026, Anexo I; Wikipédia (verbete Campinas); Wikidata (Q171617, P47); AGEMCAMP (lista da RMC). Exemplos criados para a aula.")
revisao("geo-2","Geografia: cidades limítrofes de Campinas",b.Q,list(tx),
 cobertura=["Municípios que fazem divisa com Campinas (recorte do edital)."],
 pendencias=["Fontes secundárias (Wikipédia e Wikidata). Conferir no IBGE (Cidades) ou no IGC-SP; o IBGE estava inacessível nesta sessão.","Divergência sobre Itatiba: a seção Geografia da Wikipédia inclui; o quadro de informações e o Wikidata não. Aula e questões evitam depender só desse ponto.","Casos geo2a, geo2b e geo2c fictícios."],
 fontes_conferidas=["Wikipédia e Wikidata: lista e direção dos limítrofes.","AGEMCAMP: municípios da RMC."])
gravar("geo-2",aula_html,banco("geo-2",b.Q),tx)
