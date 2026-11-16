import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _geo import *
b=B(); q=b.q
LEAD="Campinas tem a sede e seis distritos: Barão Geraldo, Sousas, Joaquim Egídio, Nova Aparecida, Campo Grande e Ouro Verde. Cada um tem história, localização e papel administrativo próprios. A banca costuma perguntar em que região fica cada distrito, como foram criados (os dois mais novos, Campo Grande e Ouro Verde, por plebiscito em 2014 e leis municipais de 2015) e o que se destaca em cada um (a Unicamp em Barão Geraldo, o Rio Atibaia em Sousas, o caráter rural de Joaquim Egídio, a população do Ouro Verde)."
S={}
S[1]="## 1. Os distritos mais antigos\n\n"+C("Wikipédia, verbete Barão Geraldo","Barão Geraldo é um distrito do município brasileiro de Campinas, no interior do estado de São Paulo,")+"\n\n"+C("Wikipédia, verbete Sousas","Distrito criado pela Lei nº 416 de 24/07/1896, com as divisas do distrito policial de Arraial dos Sousas")+"\n\n"+C("Wikipédia, verbete Joaquim Egídio","Distrito criado pela Lei n° 5.285 de 18/02/1959, com sede no povoado de igual nome e território desmembrado do distrito de Sousas")+"\n\n"+C("Lei Municipal 16.490/2023, art. 1º","Fica instituída no calendário oficial do município de Campinas a comemoração do aniversário de criação do distrito de Nova Aparecida, a ser celebrado no mês de fevereiro de cada ano, em vista da Lei Estadual nº 8.092, de 28 de fevereiro de 1964, que oficializou a criação do distrito.")+"""

**O que é um distrito, em uma frase:** é uma divisão territorial do município criada por lei, com subprefeitura própria para a gestão local.

- **Barão Geraldo (Região Norte):** surgiu nos anos 1920 em torno da Estação Barão Geraldo do Ramal Funilense. Sedia a Unicamp, o Hospital de Clínicas da Unicamp, o Centro Infantil Boldrini e polos de pesquisa (CNPEM, Laboratório Nacional de Luz Síncrotron). Em 2000 era o distrito mais populoso além da sede.
- **Sousas (Região Leste):** criado pela Lei estadual 416, de 1896. O nome homenageia o brigadeiro Luís António de Sousa Queirós. Fica às margens do Rio Atibaia, principal fonte de água da cidade. Censo 2010: 18.152 habitantes.
- **Joaquim Egídio (Região Leste):** criado em 1959, com território desmembrado de Sousas. O nome homenageia Joaquim Egídio de Sousa Aranha, o Marquês de Três Rios. É o distrito menos populoso e mais rural; ali fica o ponto mais alto do município.
- **Nova Aparecida (Região Norte):** criação oficializada pela Lei estadual 8.092, de 28 de fevereiro de 1964; o aniversário é comemorado em fevereiro.
"""
S[2]="## 2. Os distritos criados em 2015: Campo Grande e Ouro Verde\n\n"+S_("Lei Municipal 15.058/2015, art. 1º","Art. 1º - Fica criado o Distrito de Campo Grande","Art. 2º - O Poder Executivo definirá o local da subprefeitura")+"\n\n"+S_("Lei Municipal 15.059/2015, art. 1º","Art. 1º - Fica criado o Distrito da Região de Ouro Verde","Art. 2º - O Poder Executivo definirá o local da subprefeitura")+"\n\n"+C("Lei Municipal 15.058/2015, art. 2º","Art. 2º - O Poder Executivo definirá o local da subprefeitura, estrutura operacional, estrutura administrativa e as responsabilidades básicas, bem como respectivo quadro funcional e atribuições.")+"""

Campo Grande e Ouro Verde foram aprovados em plebiscito em 5 de outubro de 2014, homologado pela Justiça Eleitoral, e criados pelas Leis Municipais 15.058 e 15.059, de 10 de setembro de 2015, com base em estudo do Instituto Geográfico e Cartográfico do Estado (IGC).

- **Campo Grande (Região Noroeste):** a divisa com Ouro Verde é o Rio Capivari; a divisa com o distrito-sede é a Rodovia dos Bandeirantes (SP-348). Concentra cerca de 190 mil habitantes, em bairros ao longo da Avenida John Boyd Dunlop.
- **Ouro Verde (Região Sudoeste):** a divisa com Campo Grande é o Rio Capivari; com o distrito-sede, a Rodovia dos Bandeirantes e a Rodovia Santos Dumont (SP-075). É o distrito mais populoso (cerca de 240 mil habitantes), com população mais jovem que a média.

**Lembre:** a lei manda o Executivo definir a subprefeitura de cada distrito, a estrutura e as atribuições. Essa é a "importância administrativa" que o edital menciona: os distritos aproximam a gestão municipal dos moradores.
"""
S[3]="## 3. Visão de conjunto\n\n"+C("Wikipédia, verbete Campinas, quadro de informações","Distritos: Barão Geraldo, Campo Grande, Joaquim Egídio, Nova Aparecida, Ouro Verde e Sousas.")+"""

| Distrito | Região | Criação | Destaque |
| --- | --- | --- | --- |
| Barão Geraldo | Norte | Anos 1920 (estação) | Unicamp, polo de pesquisa |
| Nova Aparecida | Norte | Lei estadual 8.092/1964 | Aniversário em fevereiro |
| Sousas | Leste | Lei estadual 416/1896 | Rio Atibaia, abastecimento |
| Joaquim Egídio | Leste | Lei 5.285/1959 (desmembrado de Sousas) | Menos populoso, rural, ponto mais alto |
| Campo Grande | Noroeste | Lei municipal 15.058/2015 (plebiscito 2014) | Av. John Boyd Dunlop |
| Ouro Verde | Sudoeste | Lei municipal 15.059/2015 (plebiscito 2014) | Mais populoso, perto de Viracopos |

**Macete:** "Os dois do Leste são irmãos": Joaquim Egídio nasceu de Sousas. "Os dois de 2015 são gêmeos": Campo Grande e Ouro Verde, separados pelo Rio Capivari.
"""
S[5]="""## 5. Na rotina do guarda

- **Subprefeituras:** cada distrito tem subprefeitura; o guarda pode ser acionado para apoio a ações de fiscalização local.
- **Rodovias como divisa:** a Bandeirantes separa Campo Grande e Ouro Verde da sede; a Santos Dumont delimita o Ouro Verde.
- **Barão Geraldo:** grande fluxo universitário e de pesquisa; eventos estudantis e segurança no entorno da Unicamp.
- **Sousas e Joaquim Egídio:** turismo rural e áreas de mananciais; atenção a ocorrências ambientais.
- **Ouro Verde e Campo Grande:** os distritos mais populosos, com grande demanda de serviços públicos.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Número de distritos | Seis, além da sede |
| Joaquim Egídio | Desmembrado de Sousas em 1959 |
| Distrito menos populoso | Joaquim Egídio |
| Distrito mais populoso | Ouro Verde (cerca de 240 mil) |
| Criação de Campo Grande e Ouro Verde | Plebiscito de 2014 e leis municipais de 2015 |
| Divisa entre Campo Grande e Ouro Verde | Rio Capivari |
| Divisa com o distrito-sede | Rodovia dos Bandeirantes (e Santos Dumont, no Ouro Verde) |
| Unicamp | Barão Geraldo |
| Nova Aparecida | Lei estadual 8.092/1964; Região Norte |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Distritos | Barão Geraldo, Sousas, Joaquim Egídio, Nova Aparecida, Campo Grande, Ouro Verde |
| Norte | Barão Geraldo, Nova Aparecida |
| Leste | Sousas, Joaquim Egídio |
| Noroeste | Campo Grande |
| Sudoeste | Ouro Verde |
| Mais antigo | Sousas (1896) |
| Mais novos | Campo Grande e Ouro Verde (2015) |
| Gestão | Subprefeituras |
"""
QR=[("Questão 1","Os distritos de Campo Grande e Ouro Verde foram criados por",["leis municipais de 2015, após plebiscito realizado em 2014.","lei estadual de 1896.","decreto federal de 1964.","lei estadual de 1959.","emenda à Lei Orgânica em 1990."],0,"Leis 15.058 e 15.059/2015; plebiscito de 05/10/2014."),
("Questão 2","O distrito de Joaquim Egídio foi criado com território desmembrado do distrito de",["Sousas.","Barão Geraldo.","Nova Aparecida.","Campo Grande.","Ouro Verde."],1,"Lei 5.285/1959."),
("Questão 3","A divisa entre os distritos de Campo Grande e Ouro Verde é o",["Rio Capivari.","Rio Atibaia.","Ribeirão Anhumas.","Rio Tietê.","Rio Jaguari."],2,"Leis 15.058 e 15.059/2015."),
("Questão 4","A Universidade Estadual de Campinas (Unicamp) fica no distrito de",["Barão Geraldo.","Sousas.","Ouro Verde.","Joaquim Egídio.","Campo Grande."],3,"Wikipédia, Barão Geraldo.")]
t1="<strong>Plebiscito</strong><br><br>Em 2014, os eleitores de Campinas responderam se eram a favor da criação de dois novos distritos na região oeste da cidade."
t2="<strong>Turismo rural</strong><br><br>Uma família visitou o distrito menos populoso de Campinas, conhecido pelo caráter rural e pelo ponto mais alto do município."
t3="<strong>Subprefeitura</strong><br><br>Moradores do Campo Grande procuraram a subprefeitura do distrito para pedir melhorias de iluminação."
tx={"geo4a":t1,"geo4b":t2,"geo4c":t3}
# n=1
q(1,"Além da sede, Campinas tem quantos distritos?",["Seis.","Dois.","Quatro.","Oito.","Dez."],"Quadro de informações e leis de 2015.")
q(1,"É distrito de Campinas",["Barão Geraldo.","Valinhos.","Paulínia.","Vinhedo.","Itupeva."],"Distritos de Campinas.")
q(1,"É distrito de Campinas",["Sousas.","Sumaré.","Hortolândia.","Americana.","Indaiatuba."],"Distritos de Campinas.")
q(1,"É distrito de Campinas",["Nova Aparecida.","Nova Odessa.","Jaguariúna.","Pedreira.","Monte Mor."],"Nova Odessa é município.")
q(1,"O distrito de Campo Grande foi criado pela Lei Municipal",["15.058/2015.","15.059/2015.","870/2000.","1.399/1955.","189/2018."],"SAPL.")
q(1,"O distrito de Ouro Verde foi criado pela Lei Municipal",["15.059/2015.","15.058/2015.","8.092/1964.","416/1896.","5.285/1959."],"SAPL.")
q(1,"O plebiscito que aprovou a criação de Campo Grande e Ouro Verde ocorreu em",["5 de outubro de 2014.","10 de setembro de 2015.","19 de junho de 2000.","14 de julho de 1774.","28 de fevereiro de 1964."],"Leis 15.058 e 15.059/2015, parágrafo único.")
q(1,"O distrito de Sousas foi criado pela Lei nº 416, de",["1896.","1959.","1964.","2015.","1774."],"Wikipédia, Sousas.")
q(1,"O distrito de Joaquim Egídio foi criado em",["1959.","1896.","2015.","1964.","1920."],"Lei 5.285/1959.")
q(1,"O nome Joaquim Egídio homenageia Joaquim Egídio de Sousa Aranha, o",["Marquês de Três Rios.","Barão de Campinas.","Visconde de Mauá.","Duque de Caxias.","Barão Geraldo de Rezende."],"Wikipédia, Joaquim Egídio.")
q(1,"O distrito menos populoso de Campinas é",["Joaquim Egídio.","Ouro Verde.","Campo Grande.","Barão Geraldo.","Nova Aparecida."],"Wikipédia, Joaquim Egídio.")
q(1,"O distrito mais populoso de Campinas é",["Ouro Verde.","Joaquim Egídio.","Sousas.","Nova Aparecida.","Barão Geraldo."],"Wikipédia, Ouro Verde.")
q(1,"A criação do distrito de Nova Aparecida foi oficializada pela Lei Estadual nº",["8.092, de 1964.","416, de 1896.","5.285, de 1959.","870, de 2000.","15.059, de 2015."],"Lei Municipal 16.490/2023, art. 1º.")
q(1,"O aniversário do distrito de Nova Aparecida é comemorado no mês de",["fevereiro.","julho.","dezembro.","outubro.","setembro."],"Lei 16.490/2023, art. 1º.")
q(1,"O distrito de Barão Geraldo surgiu nos anos 1920 a partir de uma estação do Ramal",["Funilense.","Mogiana.","Paulista.","Sorocabana Central.","Bragantina."],"Wikipédia, Barão Geraldo.")
q(1,"O distrito de Sousas fica às margens do Rio",["Atibaia.","Capivari.","Tietê.","Jaguari.","Piracicaba."],"Wikipédia.")
q(1,"O distrito de Ouro Verde fica na Região",["Sudoeste.","Leste.","Norte.","Central.","Noroeste."],"Wikipédia.")
q(1,"No texto do plebiscito, os dois distritos aprovados foram",["Campo Grande e Ouro Verde.","Sousas e Joaquim Egídio.","Barão Geraldo e Nova Aparecida.","Viracopos e DIC.","Taquaral e Cambuí."],"Leis 15.058 e 15.059/2015.","geo4a")
q(1,"No texto do turismo rural, o distrito visitado é",["Joaquim Egídio.","Ouro Verde.","Campo Grande.","Nova Aparecida.","Barão Geraldo."],"Menos populoso e mais rural.","geo4b")
q(1,"No texto da subprefeitura, a lei de criação do Campo Grande atribui ao Poder Executivo definir o local da",["subprefeitura.","câmara.","delegacia.","escola.","catedral."],"Lei 15.058/2015, art. 2º.","geo4c")
# n=2
q(2,"Os distritos de Sousas e Joaquim Egídio ficam na Região",["Leste.","Norte.","Sudoeste.","Noroeste.","Central."],"Wikipédia.")
q(2,"Os distritos de Barão Geraldo e Nova Aparecida ficam na Região",["Norte.","Leste.","Sul.","Sudoeste.","Noroeste."],"Wikipédia.")
q(2,"A divisa entre o Distrito de Campo Grande e o distrito-sede é a Rodovia",["dos Bandeirantes (SP-348).","D. Pedro I.","Anhanguera.","Dutra.","SP-304."],"Lei 15.058/2015, art. 1º, II.")
q(2,"A divisa entre o Distrito de Ouro Verde e o distrito-sede segue pelas rodovias",["dos Bandeirantes e Santos Dumont (SP-075).","Anhanguera e D. Pedro I.","Dutra e Fernão Dias.","SP-304 e SP-101.","Anhanguera e Dutra."],"Lei 15.059/2015, art. 1º, II.")
q(2,"A área de abrangência dos distritos de Campo Grande e Ouro Verde segue estudo do",["Instituto Geográfico e Cartográfico do Estado de São Paulo.","IBGE, apenas.","Exército Brasileiro.","INSS.","Tribunal de Contas."],"Leis 15.058 e 15.059/2015, art. 1º.")
q(2,"O resultado do plebiscito que aprovou os distritos foi homologado no âmbito da",["Justiça Eleitoral (TRE-SP e TSE).","Câmara dos Deputados.","Assembleia Legislativa.","Polícia Federal.","Receita Federal."],"Leis 15.058 e 15.059/2015, parágrafo único.")
q(2,"O nome do distrito de Sousas homenageia",["o brigadeiro Luís António de Sousa Queirós.","o Marquês de Três Rios.","Barão Geraldo de Rezende.","o prefeito Orosimbo Maia.","Dom Pedro I."],"Wikipédia, Sousas.")
q(2,"Segundo o Censo de 2010, a população total do distrito de Sousas era de",["18.152 habitantes.","2.264 habitantes.","240 mil habitantes.","1,1 milhão de habitantes.","500 habitantes."],"Wikipédia, Sousas.")
q(2,"Segundo o Censo de 2010, a população total de Joaquim Egídio era de",["2.264 habitantes.","18.152 habitantes.","190 mil habitantes.","45.585 habitantes.","1 milhão de habitantes."],"Wikipédia, Joaquim Egídio.")
q(2,"No ano 2000, o distrito mais populoso de Campinas, além da sede, era",["Barão Geraldo.","Joaquim Egídio.","Sousas.","Nova Aparecida.","Ouro Verde."],"Wikipédia, Campinas. Ouro Verde só foi criado em 2015.")
q(2,"Em Barão Geraldo ficam, além da Unicamp,",["centros de pesquisa como o CNPEM e o Laboratório Nacional de Luz Síncrotron.","o Paço Municipal.","o Aeroporto de Viracopos.","a Câmara Municipal.","o Mercado Municipal."],"Wikipédia, Barão Geraldo.")
q(2,"O distrito de Campo Grande concentra bairros ao longo da Avenida",["John Boyd Dunlop.","Anchieta.","Norte-Sul.","Francisco Glicério.","da Saudade."],"Wikipédia, Campo Grande.")
q(2,"O distrito de Ouro Verde tem população",["mais jovem que a média da cidade.","mais idosa que a média.","majoritariamente rural.","de cerca de 2 mil habitantes.","inexistente."],"Wikipédia, Ouro Verde.")
q(2,"Sousas, criado em 1896, perdeu terras em 1959 para a criação do distrito de",["Joaquim Egídio.","Barão Geraldo.","Nova Aparecida.","Campo Grande.","Ouro Verde."],"Wikipédia, Sousas.")
q(2,"A gestão local dos distritos de Campinas é feita por",["subprefeituras.","conselhos tutelares.","delegacias.","cartórios.","paróquias."],"Leis 15.058 e 15.059/2015, art. 2º.")
q(2,"O distrito que fica no extremo leste e rural de Campinas, onde está o ponto mais alto do município, é",["Joaquim Egídio.","Campo Grande.","Ouro Verde.","Nova Aparecida.","Barão Geraldo."],"Wikipédia.")
q(2,"A Lei Municipal 16.490/2023 instituiu no calendário oficial a comemoração do aniversário do distrito de",["Nova Aparecida.","Sousas.","Joaquim Egídio.","Barão Geraldo.","Campo Grande."],"SAPL.")
q(2,"No texto do plebiscito, os eleitores votaram em 2014, e as leis de criação foram sancionadas em",["2015.","2014.","2010.","2020.","2000."],"Leis de 10/09/2015.","geo4a")
q(2,"No texto do turismo rural, o distrito visitado foi desmembrado, em 1959, do distrito de",["Sousas.","Barão Geraldo.","Ouro Verde.","Campo Grande.","Nova Aparecida."],"Lei 5.285/1959.","geo4b")
q(2,"No texto da subprefeitura, o Campo Grande fica na Região",["Noroeste.","Sudoeste.","Leste.","Norte.","Central."],"Wikipédia.","geo4c")
# n=3
q(3,"Assinale a alternativa correta sobre os distritos de Campinas.",["Joaquim Egídio foi desmembrado de Sousas; Campo Grande e Ouro Verde foram criados em 2015, após plebiscito.","Sousas foi desmembrado de Joaquim Egídio.","Campo Grande foi criado em 1896.","Ouro Verde fica na Região Leste.","Barão Geraldo foi criado em 2015."],"Wikipédia e leis municipais.")
q(3,"Considere. I. O Rio Capivari divide Campo Grande e Ouro Verde. II. Joaquim Egídio é o distrito mais populoso. III. Nova Aparecida teve sua criação oficializada por lei estadual de 1964. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Joaquim Egídio é o menos populoso.")
q(3,"Assinale a INCORRETA.",["Ouro Verde fica na Região Norte.","Barão Geraldo fica na Região Norte.","Sousas fica na Região Leste.","Campo Grande fica na Região Noroeste.","Joaquim Egídio fica na Região Leste."],"Ouro Verde fica na Região Sudoeste.")
q(3,"A ordem cronológica correta de criação dos distritos é",["Sousas (1896), Joaquim Egídio (1959), Nova Aparecida (1964), Campo Grande e Ouro Verde (2015).","Joaquim Egídio, Sousas, Nova Aparecida, Ouro Verde.","Campo Grande, Ouro Verde, Sousas, Joaquim Egídio.","Nova Aparecida, Sousas, Joaquim Egídio, Campo Grande.","Ouro Verde, Campo Grande, Nova Aparecida, Sousas."],"Datas das leis.")
q(3,"Pela Lei 15.059/2015, a divisa do Ouro Verde com o distrito de Campinas segue o eixo da Bandeirantes no sentido",["cidade de São Paulo, até encontrar a Rodovia Santos Dumont.","Campinas, até o Rio Atibaia.","Piracicaba, até o Rio Jaguari.","Ribeirão Preto.","Rio de Janeiro."],"Lei 15.059/2015, art. 1º, II.")
q(3,"Pela Lei 15.058/2015, a divisa do Campo Grande com o distrito de Campinas começa no divisor dos rios",["Quilombo-Capivari, no cruzamento com a Rodovia dos Bandeirantes.","Atibaia-Jaguari.","Tietê-Piracicaba.","Anhumas-Atibaia.","Capivari-Mirim e Jundiaí."],"Lei 15.058/2015, art. 1º, II.")
q(3,"A importância administrativa dos distritos, segundo as leis de 2015, está na previsão de que o Executivo definirá",["a subprefeitura, a estrutura operacional e administrativa e o quadro funcional.","a criação de nova câmara municipal.","a eleição de prefeito distrital.","um novo município.","um tribunal próprio."],"Art. 2º das leis.")
q(3,"Os distritos de Campo Grande e Ouro Verde têm em comum",["a criação em 2015 e a localização na porção oeste (Noroeste e Sudoeste).","a localização na Região Leste.","a criação por lei estadual.","a população inferior a 5 mil habitantes.","a criação em 1896."],"Leis e Wikipédia.")
q(3,"Os distritos de Sousas e Joaquim Egídio têm em comum",["a Região Leste e a origem comum, pois Joaquim Egídio saiu de Sousas.","a criação em 2015.","a Região Sudoeste.","a localização às margens do Rio Capivari.","a população superior a 200 mil habitantes."],"Wikipédia.")
q(3,"Barão Geraldo e Nova Aparecida têm em comum",["a Região Norte.","a Região Leste.","a criação em 2015.","o Aeroporto de Viracopos.","o Rio Atibaia como divisa."],"Wikipédia.")
q(3,"A enciclopédia que fala em 'quatro distritos e mais dois em criação' está desatualizada porque",["Campo Grande e Ouro Verde já foram criados por leis de 2015.","Sousas foi extinto.","Barão Geraldo virou município.","Joaquim Egídio foi incorporado a Valinhos.","Nova Aparecida virou bairro."],"Leis 15.058 e 15.059/2015.")
q(3,"O Hospital de Clínicas da Unicamp e o Centro Infantil Boldrini ficam no distrito de",["Barão Geraldo.","Sousas.","Ouro Verde.","Campo Grande.","Joaquim Egídio."],"Wikipédia, Barão Geraldo.")
q(3,"A área territorial de Joaquim Egídio (cerca de 90 km²) em comparação com a de Sousas (cerca de 66 km²) é",["maior, embora tenha menos habitantes.","menor e mais populosa.","igual.","dez vezes menor.","inexistente."],"Wikipédia: 89,970 km² x 65,791 km².")
q(3,"O plebiscito sobre os distritos foi votado por",["todo o eleitorado de Campinas.","apenas os moradores dos bairros afetados.","apenas os vereadores.","o Estado de São Paulo inteiro.","apenas os moradores de Sousas."],"Wikipédia, Ouro Verde: a população de todo o município votou.")
q(3,"Assinale a correspondência correta entre distrito e marco natural ou viário.",["Sousas – Rio Atibaia; Ouro Verde – Rodovia Santos Dumont; Campo Grande – Avenida John Boyd Dunlop.","Sousas – Rio Capivari; Ouro Verde – Rodovia D. Pedro I.","Campo Grande – Rio Atibaia.","Joaquim Egídio – Aeroporto de Viracopos.","Barão Geraldo – Rodovia Santos Dumont."],"Leis e Wikipédia.")
q(3,"No texto do plebiscito, a votação foi homologada pela Justiça Eleitoral, e o fundamento da criação dos distritos são leis",["municipais de 2015.","estaduais de 2014.","federais de 2015.","complementares estaduais.","orgânicas."],"Leis 15.058 e 15.059/2015.","geo4a")
q(3,"No texto do plebiscito, os dois distritos criados ficam, na organização do município, nas regiões",["Noroeste e Sudoeste.","Leste e Norte.","Central e Sul.","Norte e Sul.","Leste e Sudoeste."],"Wikipédia.","geo4a")
q(3,"No texto do turismo rural, a família estava no distrito cujo nome homenageia",["o Marquês de Três Rios.","o brigadeiro Sousa Queirós.","o barão Geraldo de Rezende.","Dom Pedro II.","Santos Dumont."],"Wikipédia, Joaquim Egídio.","geo4b")
q(3,"No texto do turismo rural, o distrito visitado fica na mesma região de",["Sousas.","Ouro Verde.","Campo Grande.","Barão Geraldo.","Nova Aparecida."],"Ambos na Região Leste.","geo4b")
q(3,"No texto da subprefeitura, o distrito do Campo Grande tem divisa com o Ouro Verde pelo",["Rio Capivari.","Rio Atibaia.","Ribeirão Quilombo, apenas.","Rio Tietê.","Rio Jaguari."],"Lei 15.058/2015, art. 1º, I.","geo4c")
b.fim()
code,svg=mapa("Distritos de Campinas",[
 ("bg","Barão Geraldo (N)",["Unicamp","polo de pesquisa"],"seção 1"),
 ("na","Nova Aparecida (N)",["Lei estadual 8.092/1964","aniversário em fevereiro"],"seção 1"),
 ("so","Sousas (L)",["Lei 416/1896","Rio Atibaia"],"seção 1"),
 ("je","Joaquim Egídio (L)",["1959, de Sousas","menos populoso"],"seção 1"),
 ("cg","Campo Grande (NO)",["Lei 15.058/2015","Bandeirantes; Capivari"],"seção 2"),
 ("ov","Ouro Verde (SO)",["Lei 15.059/2015","mais populoso"],"seção 2")],
 "Na prova: região, ano de criação e destaque de cada distrito")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"Cada caixa é um distrito, com região, lei e destaque.","Fontes: Edital 02/2026, Anexo I; Leis Municipais 15.058/2015, 15.059/2015 e 16.490/2023 (SAPL); Wikipédia (verbetes Campinas, Barão Geraldo, Sousas, Joaquim Egídio, Campo Grande, Ouro Verde). Exemplos criados para a aula.")
revisao("geo-4","Geografia: distritos de Campinas",b.Q,list(tx),
 cobertura=["Características, localização e importância administrativa dos seis distritos (recorte do edital)."],
 pendencias=["Leis municipais de criação de Campo Grande e Ouro Verde e a lei do aniversário de Nova Aparecida vêm do SAPL. Datas de Sousas, Joaquim Egídio e números de população vêm da Wikipédia: conferir no IBGE e na Fundação Seade.","População de Campo Grande (190 mil) e Ouro Verde (240 mil) são estimativas da Wikipédia.","Casos geo4a, geo4b e geo4c fictícios."],
 fontes_conferidas=["Leis 15.058/2015, 15.059/2015 e 16.490/2023 (SAPL)."])
gravar("geo-4",aula_html,banco("geo-4",b.Q),tx)
