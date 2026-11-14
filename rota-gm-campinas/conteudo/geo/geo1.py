import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _geo import *
b=B(); q=b.q
LEAD="A Região Metropolitana de Campinas (RMC) é o primeiro tema de Geografia do edital. A prova cobra três coisas: quais são os 20 municípios (e quais ficam de fora, como Itupeva e Jundiaí), quando e por qual lei a RMC foi criada (Lei Complementar Estadual 870, de 19 de junho de 2000) e por que a região é relevante (indústria, tecnologia, rodovias e o Aeroporto de Viracopos). Para o guarda municipal de Campinas, a RMC é o território vizinho de onde vem e para onde vai boa parte das ocorrências: as rodovias, o aeroporto e a conurbação com Sumaré, Hortolândia, Valinhos e Paulínia."
S={}
S[1]="## 1. O que é a RMC e quem faz parte\n\n"+C("AGEMCAMP, página RMC","RMC: Unidade regional do Estado de São Paulo criada pela Lei Complementar Estadual nº 870, de 19 de Junho de 2000, sendo constituída pelo agrupamento de 20 municípios: Americana, Artur Nogueira, Campinas, Cosmópolis, Engenheiro Coelho, Holambra, Hortolândia, Indaiatuba, Itatiba, Jaguariúna, Monte Mor, Morungaba, Nova Odessa, Paulínia, Pedreira, Santa Bárbara d’Oeste, Santo Antônio de Posse, Sumaré, Valinhos e Vinhedo.")+"""

**O que é, em uma frase:** a RMC é uma unidade regional do Estado de São Paulo, criada por lei complementar estadual, que agrupa 20 municípios em torno de Campinas.

**Regra principal:** são 20 municípios, criados pela LC Estadual 870/2000. A sede é Campinas. A gestão metropolitana tem apoio da AGEMCAMP (Agência Metropolitana de Campinas), ligada ao Governo do Estado.

**Macete para os 20:** separe por inicial. *A*: Americana, Artur Nogueira. *C*: Campinas, Cosmópolis. *E*: Engenheiro Coelho. *H*: Holambra, Hortolândia. *I*: Indaiatuba, Itatiba. *J*: Jaguariúna. *M*: Monte Mor, Morungaba. *N*: Nova Odessa. *P*: Paulínia, Pedreira. *S*: Santa Bárbara d’Oeste, Santo Antônio de Posse, Sumaré. *V*: Valinhos, Vinhedo.

**Pegadinha:** Itupeva faz divisa com Campinas, mas **não** está na RMC (fica na região de Jundiaí). Jundiaí, Piracicaba, Mogi Guaçu e Mogi Mirim também **não** estão na RMC.
"""
S[2]="## 2. Números, população e economia\n\n"+C("AGEMCAMP, página RMC","Possui uma área de 3.792 Km2 e uma população de 3.178.601 (três milhões cento e setenta e oito mil e seiscentos e um habitantes), com crescimento anual de 1,04% entre 2010-2022, segundo os dados do censo/seade de 2022.")+"\n\n"+C("AGEMCAMP, página RMC","A Região apresenta uma diversificada produção industrial, principalmente em setores dinâmicos e de alto “input” científico/tecnológico, com resultados crescentes em ganhos de competitividade nos mercados internos e externos.")+"\n\n"+C("AGEMCAMP, página RMC","Neste cenário, destaque para a Região Metropolitana de Campinas, em especial as cidades de Campinas (PIB de R$ 72,9 bilhões) e Paulínia (PIB de R$ 52,3 bilhões).")+"\n\n"+C("Wikipédia, verbete Campinas","É uma das mais dinâmicas no cenário econômico brasileiro e representa 2,7%o do produto interno bruto nacional e 7,83% do produto interno bruto paulista, ou seja, cerca de 77,7 bilhões de reais por ano.")+"""

A RMC tem cerca de 3,8 mil km² e pouco mais de 3,1 milhões de habitantes (Censo/Seade 2022). Sua economia combina indústria moderna e diversificada, agricultura e agroindústria fortes, serviços especializados e centros de pesquisa e universidades de renome. Os maiores PIBs da região são de Campinas e de Paulínia (refinaria e polo petroquímico). Campinas é a cidade mais populosa do interior do país e a terceira do Estado (Censo 2022: 1.139.047 habitantes).

**Cuidado com números de fontes diferentes:** a AGEMCAMP traz os dados do Censo 2022; a Wikipédia traz estimativas de anos diversos. Na prova, a banca costuma pedir a ordem de grandeza (cerca de 3 milhões de habitantes; 20 municípios; LC 870/2000), e não o número exato.
"""
S[3]="## 3. Relevância regional: rodovias, aeroporto e macrometrópole\n\n"+C("AGEMCAMP, página RMC","A RMC é servida por um sistema viário amplo e de boa qualidade, contando como eixos principais as rodovias Bandeirantes e Anhanguera ligando a região à Capital e ao interior paulista, a Rodovia SP-304 rumo a Piracicaba, a Rodovia D. Pedro I que faz ligação com o Vale do Paraíba e a Rodovia Dutra com destino ao Rio de Janeiro.")+"\n\n"+C("AGEMCAMP, página RMC","O Aeroporto Internacional de Viracopos, em Campinas (SP), estabeleceu em 2023 um novo recorde anual de movimentação de passageiros com 12.524.219 (doze milhões quinhentos e vinte quatro mil e duzentos e dezenove) pessoas embarcando ou desembarcando pelo terminal, com reconhecimento no ranking mundial top 10 (dez) em pontualidade.")+"\n\n"+C("Wikipédia, verbete Campinas","O Aeroporto Internacional de Viracopos/Campinas, localizado no extremo sul do município, é o segundo maior terminal aéreo de cargas do país,")+"""

A RMC é contígua à Região Metropolitana de São Paulo e integra o chamado Complexo Metropolitano Expandido (macrometrópole paulista). Os eixos viários são as Rodovias Bandeirantes e Anhanguera (Capital e interior), a SP-304 (Piracicaba), a D. Pedro I (Vale do Paraíba) e a ligação com a Dutra (Rio de Janeiro). O Aeroporto de Viracopos fica no extremo sul de Campinas e é um dos maiores terminais de carga do país.

**Fluxo de pensamento para a prova:**

1. A questão fala em "região metropolitana" e lista cidades? Confira se todas estão entre as 20.
2. Aparece Itupeva, Jundiaí ou Piracicaba? Não são RMC.
3. A questão pede a lei de criação? LC **Estadual** 870/2000 (não é lei federal nem municipal).
"""
S[5]="""## 5. Na rotina do guarda

- **Conurbação:** Campinas, Sumaré, Hortolândia, Valinhos e Paulínia formam manchas urbanas contínuas; uma ocorrência pode "atravessar" o limite municipal sem que se perceba.
- **Rodovias:** Anhanguera, Bandeirantes, D. Pedro I e Santos Dumont cortam o município; acidentes e ocorrências nelas envolvem a polícia rodoviária, e a Guarda atua de forma integrada (Susp).
- **Viracopos:** fica no extremo sul de Campinas; o fluxo de passageiros e cargas exige atenção à segurança no entorno.
- **Integração metropolitana:** a Guarda de Campinas coopera com as guardas e polícias dos municípios vizinhos.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Número de municípios | 20 (fonte oficial: AGEMCAMP) |
| Lei de criação | Lei Complementar **Estadual** 870, de 19/06/2000 |
| Itupeva | Faz divisa com Campinas, mas não está na RMC |
| Jundiaí, Piracicaba | Têm regiões próprias; não estão na RMC |
| Itatiba e Morungaba | Estão na RMC |
| Maiores PIBs | Campinas e Paulínia |
| Área e população | Cerca de 3,8 mil km² e 3,1 milhões de habitantes (2022) |
| Rodovias principais | Bandeirantes, Anhanguera, SP-304, D. Pedro I, ligação com a Dutra |
| Viracopos | Extremo sul de Campinas; grande terminal de cargas |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Criação | LC Estadual 870/2000 |
| Municípios | 20, com sede em Campinas |
| Gestão | AGEMCAMP (Estado) |
| Área | Cerca de 3.792 km² |
| População | 3.178.601 (Censo/Seade 2022) |
| Economia | Indústria de alta tecnologia, agroindústria, serviços, pesquisa |
| Maiores PIBs | Campinas (R$ 72,9 bi) e Paulínia (R$ 52,3 bi) |
| Viracopos | 12,5 milhões de passageiros em 2023 |
| Posição | Contígua à RMSP; parte da macrometrópole |
"""
QR=[("Questão 1","A Região Metropolitana de Campinas foi criada pela",["Lei Complementar Estadual nº 870, de 2000.","Lei Federal nº 870, de 2000.","Lei Orgânica de Campinas, de 1990.","Constituição Estadual, de 1989.","Lei Municipal nº 870, de 2000."],0,"AGEMCAMP: criada pela LC Estadual 870, de 19/06/2000."),
("Questão 2","Assinale o município que faz divisa com Campinas, mas NÃO integra a Região Metropolitana de Campinas.",["Itupeva.","Valinhos.","Paulínia.","Sumaré.","Hortolândia."],1,"Itupeva é limítrofe, mas não está entre os 20 municípios da RMC."),
("Questão 3","A Região Metropolitana de Campinas é formada por quantos municípios?",["20.","15.","19.","22.","25."],2,"AGEMCAMP: agrupamento de 20 municípios."),
("Questão 4","Entre os municípios da RMC, os dois maiores PIBs destacados pela AGEMCAMP são os de",["Campinas e Paulínia.","Campinas e Americana.","Sumaré e Hortolândia.","Indaiatuba e Valinhos.","Itatiba e Vinhedo."],3,"AGEMCAMP: Campinas (R$ 72,9 bi) e Paulínia (R$ 52,3 bi).")]
t1="<strong>Ocorrência na divisa</strong><br><br>Uma equipe da Guarda Municipal de Campinas acompanhava um veículo pela Rodovia Anhanguera, rumo a Valinhos, e recebeu a informação de que o veículo seguiria para Jundiaí."
t2="<strong>Reunião metropolitana</strong><br><br>Representantes de municípios vizinhos foram convidados para uma reunião da RMC sobre segurança: Sumaré, Hortolândia, Itupeva, Valinhos e Americana."
t3="<strong>Aeroporto</strong><br><br>Durante uma operação no extremo sul de Campinas, a guarda apoiou a segurança no entorno do maior aeroporto da região."
tx={"geo1a":t1,"geo1b":t2,"geo1c":t3}
# n=1
q(1,"A Região Metropolitana de Campinas é uma unidade regional do Estado de",["São Paulo.","Minas Gerais.","Paraná.","Rio de Janeiro.","Goiás."],"AGEMCAMP.")
q(1,"A RMC foi criada em",["19 de junho de 2000.","14 de julho de 1774.","5 de outubro de 1988.","1º de janeiro de 2010.","19 de junho de 1990."],"AGEMCAMP: LC Estadual 870, de 19/06/2000.")
q(1,"A cidade-sede da Região Metropolitana de Campinas é",["Campinas.","Americana.","Sumaré.","Paulínia.","Indaiatuba."],"Campinas é a sede da RMC.")
q(1,"Integra a Região Metropolitana de Campinas o município de",["Americana.","Jundiaí.","Piracicaba.","Itupeva.","Mogi Guaçu."],"Americana está entre os 20 municípios.")
q(1,"Integra a RMC o município de",["Holambra.","Atibaia.","Bragança Paulista.","Limeira.","Rio Claro."],"Holambra está entre os 20.")
q(1,"Integra a RMC o município de",["Vinhedo.","Jundiaí.","Sorocaba.","Itu.","Salto."],"Vinhedo está entre os 20.")
q(1,"Integra a RMC o município de",["Santa Bárbara d’Oeste.","Limeira.","Piracicaba.","São Carlos.","Mogi Mirim."],"Santa Bárbara d’Oeste está entre os 20.")
q(1,"NÃO integra a Região Metropolitana de Campinas o município de",["Jundiaí.","Cosmópolis.","Nova Odessa.","Engenheiro Coelho.","Artur Nogueira."],"Jundiaí tem região metropolitana própria.")
q(1,"NÃO integra a RMC o município de",["Piracicaba.","Paulínia.","Pedreira.","Jaguariúna.","Monte Mor."],"Piracicaba não está entre os 20.")
q(1,"A RMC é servida por eixos viários como as Rodovias Bandeirantes e",["Anhanguera.","Régis Bittencourt.","Fernão Dias.","Castello Branco.","Raposo Tavares."],"AGEMCAMP.")
q(1,"A Rodovia D. Pedro I faz a ligação da RMC com o",["Vale do Paraíba.","litoral sul.","oeste paulista.","Paraná.","Mato Grosso do Sul."],"AGEMCAMP.")
q(1,"A Rodovia SP-304 segue, a partir da RMC, rumo a",["Piracicaba.","Santos.","Sorocaba.","Ribeirão Preto.","São José dos Campos."],"AGEMCAMP.")
q(1,"O Aeroporto Internacional de Viracopos fica no município de",["Campinas.","Indaiatuba.","Valinhos.","Sumaré.","Paulínia."],"AGEMCAMP: Aeroporto Internacional de Viracopos, em Campinas.")
q(1,"A produção industrial da RMC concentra-se principalmente em setores dinâmicos e de alto",["“input” científico e tecnológico.","consumo de carvão.","uso de mão de obra infantil.","extrativismo mineral.","subsídio estrangeiro."],"AGEMCAMP.")
q(1,"A população da RMC, segundo o Censo/Seade de 2022, é de cerca de",["3,2 milhões de habitantes.","500 mil habitantes.","1,1 milhão de habitantes.","10 milhões de habitantes.","20 milhões de habitantes."],"AGEMCAMP: 3.178.601.")
q(1,"A área da RMC é de aproximadamente",["3.792 km².","794 km².","10.000 km².","248.000 km².","1.500 km²."],"AGEMCAMP.")
q(1,"A RMC é contígua à Região Metropolitana de",["São Paulo.","Belo Horizonte.","Curitiba.","Rio de Janeiro.","Ribeirão Preto."],"AGEMCAMP: área contígua à RMSP.")
q(1,"No texto da ocorrência na divisa, o veículo segue pela Rodovia Anhanguera, que é um dos eixos que ligam a RMC à",["Capital e ao interior paulista.","região Sul do país.","fronteira com o Paraguai.","Bahia.","Amazônia."],"AGEMCAMP.","geo1a")
q(1,"No texto da reunião metropolitana, o município convidado que NÃO pertence à RMC é",["Itupeva.","Sumaré.","Hortolândia.","Valinhos.","Americana."],"Itupeva não está entre os 20.","geo1b")
q(1,"No texto do aeroporto, o maior aeroporto da região, no extremo sul de Campinas, é o",["Aeroporto Internacional de Viracopos.","Aeroporto de Congonhas.","Aeroporto de Guarulhos.","Aeroporto Campo dos Amarais.","Aeroporto Santos Dumont."],"Viracopos fica no extremo sul do município.","geo1c")
# n=2
q(2,"Assinale a alternativa que traz apenas municípios da RMC.",["Americana, Sumaré e Vinhedo.","Americana, Jundiaí e Vinhedo.","Itupeva, Sumaré e Vinhedo.","Piracicaba, Paulínia e Valinhos.","Limeira, Hortolândia e Itatiba."],"Jundiaí, Itupeva, Piracicaba e Limeira não são RMC.")
q(2,"Assinale a alternativa que traz apenas municípios da RMC.",["Cosmópolis, Holambra e Morungaba.","Cosmópolis, Atibaia e Morungaba.","Holambra, Mogi Mirim e Pedreira.","Itupeva, Holambra e Pedreira.","Jundiaí, Cosmópolis e Morungaba."],"Atibaia, Mogi Mirim, Itupeva e Jundiaí não são RMC.")
q(2,"A lei que criou a RMC é uma lei complementar",["estadual.","federal.","municipal.","distrital.","constitucional federal."],"LC Estadual 870/2000.")
q(2,"O órgão estadual voltado à gestão da RMC é a",["AGEMCAMP – Agência Metropolitana de Campinas.","EMDEC.","SANASA.","CETESB, exclusivamente.","Câmara Municipal de Campinas."],"AGEMCAMP, ligada ao Governo do Estado.")
q(2,"O crescimento anual da população da RMC entre 2010 e 2022, segundo o censo/Seade, foi de cerca de",["1,04%.","10%.","0,01%.","5%.","20%."],"AGEMCAMP.")
q(2,"Além da indústria, a AGEMCAMP destaca na RMC uma estrutura",["agrícola e agroindustrial bastante significativa.","exclusivamente extrativista.","mineradora de ouro.","pesqueira marítima.","baseada em turismo de praia."],"AGEMCAMP.")
q(2,"A RMC destaca-se pela presença de centros inovadores no campo das pesquisas científicas e tecnológicas e de",["universidades de renome.","portos marítimos.","usinas nucleares.","bases militares estrangeiras.","minas de carvão."],"AGEMCAMP.")
q(2,"O município da RMC com o segundo maior PIB destacado pela AGEMCAMP, depois de Campinas, é",["Paulínia.","Americana.","Sumaré.","Holambra.","Morungaba."],"AGEMCAMP: Paulínia, R$ 52,3 bi.")
q(2,"Em 2023, o Aeroporto de Viracopos bateu recorde com cerca de",["12,5 milhões de passageiros.","1 milhão de passageiros.","50 milhões de passageiros.","300 mil passageiros.","100 milhões de passageiros."],"AGEMCAMP.")
q(2,"O Aeroporto de Viracopos tem destaque nacional especialmente no transporte de",["cargas.","passageiros militares, apenas.","combustível nuclear.","gado.","minério de ferro."],"Wikipédia: segundo maior terminal aéreo de cargas do país.")
q(2,"A Rodovia Dutra é citada pela AGEMCAMP como eixo com destino a",["Rio de Janeiro.","Belo Horizonte.","Curitiba.","Santos.","Brasília."],"AGEMCAMP.")
q(2,"O município de Campinas, segundo o Censo 2022, tinha cerca de",["1,14 milhão de habitantes.","300 mil habitantes.","3 milhões de habitantes.","500 mil habitantes.","12 milhões de habitantes."],"Censo 2022: 1.139.047.")
q(2,"Campinas é, segundo o Censo 2022, o município mais populoso",["do interior paulista.","do Brasil.","do Estado de São Paulo.","da região Sul.","do litoral."],"Wikipédia: mais populoso do interior paulista e do interior do Brasil.")
q(2,"Integram a RMC municípios que formam conurbação com Campinas, como",["Sumaré, Hortolândia e Valinhos.","Jundiaí, Itupeva e Louveira.","Piracicaba, Limeira e Rio Claro.","Sorocaba, Itu e Salto.","Santos, Guarujá e Cubatão."],"Wikipédia: conurbação atinge Sumaré, Valinhos, Paulínia e outros.")
q(2,"Mogi Guaçu, Mogi Mirim e Itapira",["não fazem parte da RMC.","fazem parte da RMC.","são distritos de Campinas.","formam a sede da RMC.","são bairros de Campinas."],"Não estão entre os 20 municípios da AGEMCAMP.")
q(2,"A RMC integra o chamado Complexo Metropolitano Expandido, também conhecido como",["macrometrópole paulista.","Vale do Ribeira.","Pontal do Paranapanema.","Baixada Fluminense.","Triângulo Mineiro."],"Wikipédia.")
q(2,"Sobre a RMC, é correto afirmar que tem cerca de 3,8 mil km² e",["mais de 3 milhões de habitantes.","menos de 500 mil habitantes.","um único município.","sede em Americana.","nenhuma indústria."],"AGEMCAMP.")
q(2,"No texto da ocorrência na divisa, o veículo ia de Campinas para Valinhos e depois para Jundiaí. Dos três municípios, NÃO integra a RMC",["Jundiaí.","Campinas.","Valinhos.","nenhum deles.","todos integram."],"Jundiaí não é RMC.","geo1a")
q(2,"No texto da reunião metropolitana, os municípios convidados que integram a RMC são",["Sumaré, Hortolândia, Valinhos e Americana.","apenas Sumaré e Itupeva.","apenas Itupeva e Americana.","todos os cinco.","nenhum deles."],"Itupeva não é RMC.","geo1b")
q(2,"No texto do aeroporto, a importância de Viracopos para a RMC deve-se, entre outros fatores, ao fluxo de",["cargas e passageiros.","navios.","trens de alta velocidade.","barcos de pesca.","dutos de gás."],"AGEMCAMP e Wikipédia.","geo1c")
# n=3
q(3,"Assinale a alternativa correta sobre a RMC.",["Foi criada por lei complementar estadual em 2000 e reúne 20 municípios, entre eles Itatiba e Morungaba.","Foi criada por lei federal em 1988 e reúne 10 municípios.","Inclui Jundiaí e Itupeva.","Tem sede em Americana.","Reúne 30 municípios, incluindo Piracicaba."],"AGEMCAMP.")
q(3,"Considere. I. Itatiba integra a RMC. II. Itupeva integra a RMC. III. Engenheiro Coelho integra a RMC. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Itupeva não é RMC.")
q(3,"Assinale a INCORRETA.",["A RMC foi criada por lei municipal de Campinas.","A RMC tem 20 municípios.","A RMC é contígua à Região Metropolitana de São Paulo.","Paulínia integra a RMC.","Santo Antônio de Posse integra a RMC."],"A RMC foi criada por lei complementar estadual.")
q(3,"Entre os 20 municípios da RMC, quantos começam com a letra 'S'?",["Três: Santa Bárbara d’Oeste, Santo Antônio de Posse e Sumaré.","Um: Sumaré.","Dois: Sumaré e Sorocaba.","Quatro: Sumaré, Salto, Santa Bárbara e Santo Antônio.","Nenhum."],"Macete das iniciais.")
q(3,"Entre os municípios da RMC, começam com 'H' os municípios de",["Holambra e Hortolândia.","Hortolândia e Itatiba.","Holambra e Indaiatuba.","Hortolândia, apenas.","Holambra, apenas."],"Macete das iniciais.")
q(3,"Entre os municípios da RMC, começam com 'I' os municípios de",["Indaiatuba e Itatiba.","Itupeva e Itatiba.","Indaiatuba e Itu.","Itapira e Itatiba.","Itupeva e Indaiatuba."],"Itupeva, Itu e Itapira não são RMC.")
q(3,"A RMC, segundo a AGEMCAMP, possui a Rodovia SP-304 como eixo rumo a Piracicaba. Piracicaba, porém,",["não integra a RMC.","é a sede da RMC.","é distrito de Campinas.","integra a RMC desde 2000.","foi incorporada em 2022."],"Piracicaba não está na lista.")
q(3,"O município de Campinas tem área de cerca de",["794,6 km².","3.792 km².","50 km².","2.000 km².","10.000 km²."],"IBGE 2022, via Wikipédia: 794,571 km². Não confunda com a área da RMC.")
q(3,"Segundo a AGEMCAMP, o PIB da Região Administrativa de Campinas teve, de outubro de 2020 a setembro de 2021, crescimento de",["9,9%, o maior do Estado no período.","1%, o menor do Estado.","50%.","0%.","3,9%, igual ao nacional."],"AGEMCAMP, com dados do Seade.")
q(3,"Distinguem-se os dados de área: 3.792 km² correspondem à",["RMC; 794,6 km², ao município de Campinas.","Campinas; 794,6 km², à RMC.","Região Leste de Campinas.","área urbana de Campinas apenas.","área do Aeroporto de Viracopos."],"AGEMCAMP e IBGE.")
q(3,"Assinale a alternativa que traz apenas municípios que NÃO integram a RMC.",["Jundiaí, Itupeva e Piracicaba.","Jundiaí, Itatiba e Piracicaba.","Itupeva, Vinhedo e Piracicaba.","Jundiaí, Holambra e Itupeva.","Piracicaba, Paulínia e Itupeva."],"Itatiba, Vinhedo, Holambra e Paulínia são RMC.")
q(3,"Assinale a alternativa que traz um município da RMC que NÃO faz divisa com Campinas.",["Americana.","Valinhos.","Sumaré.","Paulínia.","Hortolândia."],"Americana é RMC, mas não é limítrofe de Campinas.")
q(3,"A relevância regional da RMC, segundo a AGEMCAMP, decorre, entre outros fatores, de",["indústria diversificada, agroindústria, serviços especializados e centros de pesquisa.","turismo de praia.","produção de petróleo em alto-mar.","mineração de ouro.","exportação de pescado."],"AGEMCAMP.")
q(3,"Campinas e a RMC fazem parte da macrometrópole que une, entre outras, as regiões metropolitanas de",["São Paulo, Jundiaí, Sorocaba, Vale do Paraíba e Baixada Santista.","Belo Horizonte e Rio de Janeiro.","Curitiba e Florianópolis.","Ribeirão Preto e Uberlândia.","Goiânia e Brasília."],"Wikipédia, verbete Campinas.")
q(3,"Quanto à fonte dos dados, a população de 3.178.601 habitantes da RMC refere-se a",["Censo/Seade 2022.","estimativa de 1990.","Censo 2000.","projeção para 2040.","dados municipais de 1974."],"AGEMCAMP.")
q(3,"Assinale a alternativa que traz apenas municípios da RMC que começam com 'M'.",["Monte Mor e Morungaba.","Monte Mor e Mogi Mirim.","Morungaba e Mogi Guaçu.","Mogi Mirim e Mogi Guaçu.","Monte Mor, apenas."],"Mogi Mirim e Mogi Guaçu não são RMC.")
q(3,"No texto da reunião metropolitana, a inclusão de Itupeva configura erro porque Itupeva",["faz divisa com Campinas, mas não integra a RMC.","não faz divisa com Campinas e não é RMC.","é distrito de Campinas.","é a sede da RMC.","integra a RMC desde 2000."],"Itupeva é limítrofe, mas fora da RMC.","geo1b")
q(3,"No texto da reunião metropolitana, Americana integra a RMC, mas, quanto à divisa com Campinas,",["não faz divisa com Campinas.","faz divisa a oeste.","faz divisa ao norte.","faz divisa ao sul.","é distrito de Campinas."],"Americana não é limítrofe.","geo1b")
q(3,"No texto da ocorrência na divisa, a Rodovia Anhanguera, como a Bandeirantes, liga a RMC à",["Capital e ao interior paulista.","Bahia.","Argentina.","Mato Grosso.","Amazônia."],"AGEMCAMP.","geo1a")
q(3,"No texto do aeroporto, a localização de Viracopos no município é o extremo",["sul.","norte.","leste.","oeste.","centro."],"Wikipédia: extremo sul do município.","geo1c")
b.fim()
code,svg=mapa("Região Metropolitana de Campinas",[
 ("lei","Criação",["LC Estadual 870","19/06/2000","AGEMCAMP"],"seção 1"),
 ("mun","20 municípios",["macete das iniciais","sede: Campinas"],"seção 1"),
 ("fora","Fora da RMC",["Itupeva (limítrofe)","Jundiaí, Piracicaba","Mogi Guaçu, Mogi Mirim"],"seção 1"),
 ("num","Números",["3.792 km²","3,18 milhões (2022)","Campinas: 1,14 milhão"],"seção 2"),
 ("eco","Economia",["alta tecnologia","agroindústria","PIBs: Campinas e Paulínia"],"seção 2"),
 ("rel","Relevância",["rodovias","Viracopos","macrometrópole"],"seção 3")],
 "Na prova: confira se cada cidade está entre os 20")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a criação e os municípios; as demais, os números, a economia e a relevância regional.","Fontes: Edital 02/2026, Anexo I; AGEMCAMP (página RMC); Wikipédia, verbete Campinas (dados de apoio). Exemplos criados para a aula.")
revisao("geo-1","Geografia: Região Metropolitana de Campinas",b.Q,list(tx),
 cobertura=["Municípios integrantes, características socioeconômicas e relevância regional (recorte do edital)."],
 pendencias=["Fonte oficial principal: AGEMCAMP (página RMC, 14/11/2026). Dados de apoio da Wikipédia (população de Campinas, posição, macrometrópole) devem ser conferidos no IBGE.","A Wikipédia menciona 21 municípios em um trecho; a fonte oficial (AGEMCAMP) diz 20. Usamos 20.","Casos geo1a, geo1b e geo1c fictícios."],
 fontes_conferidas=["AGEMCAMP: lista de municípios, LC 870/2000, área, população, economia, rodovias, Viracopos."])
gravar("geo-1",aula_html,banco("geo-1",b.Q),tx)
