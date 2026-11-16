import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _geo import *
b=B(); q=b.q
LEAD="O edital pede 'noções de localização na cidade de Campinas: divisão por zonas geográficas (Norte, Sul, Leste e Oeste), com base na organização territorial e administrativa do município'. Na prática, a Prefeitura organiza a cidade em grandes regiões (Central, Norte, Sul, Leste, Noroeste e Sudoeste), que aparecem nos serviços de saúde (Distritos de Saúde), nas administrações regionais e nas subprefeituras. A 'zona oeste' do edital corresponde, na organização municipal, às regiões Noroeste e Sudoeste. O Plano Diretor, por sua vez, divide o território em quatro macrozonas. Para o guarda, saber onde fica cada bairro e equipamento é parte do trabalho de rua."
S={}
S[1]="## 1. As regiões de Campinas\n\n"+C("Wikipédia, verbete Campinas","Também divide-se em seis regiões: Central, Norte, Leste, Sul e Noroeste e Sudoeste.")+"\n\n"+C("Wikipédia, verbete Campinas","O município de Campinas possui, além das subprefeituras dos seus quatro distritos (além de mais dois em processo de criação), quatorze administrações regionais, cada uma delas, por sua vez, dividida em vários bairros.")+"\n\n"+C("Lei Municipal 15.780/2019, ementa","DENOMINA CENTRO DE SAÚDE VICENTE PISANI NETO UMA UNIDADE DE SAÚDE DO DISTRITO DE SAÚDE NOROESTE DO MUNICÍPIO DE CAMPINAS.")+"""

**O que é, em uma frase:** a divisão em regiões é a forma como a cidade é organizada para administração e serviços: cada região reúne bairros, e os distritos ficam dentro delas.

**Regra principal:**

| Edital | Organização do município | Onde ficam |
| --- | --- | --- |
| Norte | Região Norte | Barão Geraldo, Nova Aparecida, Amarais |
| Leste | Região Leste | Sousas, Joaquim Egídio, Taquaral, Nova Campinas |
| Sul | Região Sul | Jardim Proença, Parque Prado, Campinas Shopping |
| Oeste | Regiões Noroeste e Sudoeste | Campo Grande (NO); Ouro Verde, Viracopos, DICs (SO) |
| (Centro) | Região Central | Centro, Cambuí, Vila Itapura |

A saúde municipal usa a mesma lógica: há Distritos de Saúde por região (por exemplo, o Distrito de Saúde Noroeste). As administrações regionais (ARs) e as subprefeituras dos distritos fazem a gestão local de serviços urbanos. **Atenção:** a enciclopédia diz "quatro distritos (além de mais dois em processo de criação)"; esses dois, Campo Grande e Ouro Verde, foram criados por lei em 2015 (aula do posto seguinte).
"""
S[2]="## 2. O que caracteriza cada região\n\n"+C("Wikipédia, verbete Campinas","Região Central: É a que está mais densamente urbanizada, sendo predominantemente verticalizada, possuindo a maior concentração de estabelecimentos comerciais, médicos e de serviços de toda a cidade.")+"\n\n"+C("Wikipédia, verbete Campinas","Região Leste: Nela, há predomínio de bairros residenciais de alto padrão (como o Alphaville, Nova Campinas, Gramado e o Taquaral) e alguns bairros próximos a favelas (Vila Brandina). Os distritos de Sousas e Joaquim Egídio situam-se nesta região.")+"\n\n"+C("Wikipédia, verbete Campinas","Região Noroeste: Ocupa a região entre as rodovias SP-101 (a sul) e SP-348 (a oeste), com bairros mais antigos, e engloba o distrito do Campo Grande.")+"\n\n"+C("Wikipédia, verbete Campinas","Região Norte: Engloba os distritos de Barão Geraldo e Nova Aparecida, a Região dos Amarais, do Jardim Chapadão e do Jardim Aurélia.")+"\n\n"+C("Wikipédia, verbete Campinas","Região Sudoeste: É a região na qual está o distrito de Ouro Verde e outras regiões tais como a do Aeroporto de Viracopos e dos DICs (conjuntos habitacionais pertencentes ao Distrito Industrial). Nela também se localiza o Distrito Industrial.")+"""

- **Central:** a mais urbanizada e verticalizada; concentra comércio, serviços médicos e órgãos públicos (o Paço Municipal fica no Centro).
- **Leste:** bairros de alto padrão (Taquaral, Nova Campinas, Gramado), os distritos de Sousas e Joaquim Egídio, os shoppings Iguatemi e Parque D. Pedro e áreas rurais e de proteção ambiental. Ali está o ponto mais alto do município (Serra das Cabras, Observatório Jean Nicolini, 1.033 m).
- **Norte:** distritos de Barão Geraldo (Unicamp) e Nova Aparecida, Amarais, Chapadão e Jardim Aurélia.
- **Noroeste:** entre a SP-101 e a Rodovia dos Bandeirantes (SP-348); distrito de Campo Grande.
- **Sudoeste:** distrito de Ouro Verde, Aeroporto de Viracopos, DICs e Distrito Industrial; historicamente, a região com mais núcleos de pobreza.
- **Sul:** ocupação muito variada, de bairros de classe média alta (Jardim Proença, Parque Prado) a ocupações em regularização (Parque Oziel).
"""
S[3]="## 3. Macrozonas do Plano Diretor e o relevo e as águas\n\n"+S_("Plano Diretor (LC 189/2018), art. 5º","Art. 5º O Macrozoneamento","[[ORIGEM: Wikipédia, verbete 'Campinas'")+"\n\n"+C("Wikipédia, verbete Campinas, seção Geografia","O ponto mais alto de Campinas está próximo ao Observatório Municipal Jean Nicolini,")+"""

O Plano Diretor Estratégico (Lei Complementar Municipal 189/2018) divide o município em quatro macrozonas: Macrometropolitana (área urbana impactada por grandes estruturas viárias e econômicas, como rodovias e aeroporto), de Estruturação Urbana (área urbana consolidada e em consolidação), de Desenvolvimento Ordenado (zona rural, com usos rurais e urbanos compatíveis) e de Relevância Ambiental (maior parte na zona rural, com áreas estratégicas para preservação e recursos hídricos).

Campinas está em duas bacias hidrográficas: a do Rio Piracicaba (Atibaia, Anhumas e Quilombo; regiões Norte, Central e Leste) e a do Rio Capivari (Piçarrão; regiões Noroeste, Sudoeste e Sul). O Rio Atibaia, que passa em Sousas, é a principal fonte de água da cidade. O ponto mais alto (cerca de 1.033 m) fica na Serra das Cabras, em Joaquim Egídio, na Região Leste.

**Não confunda:** *região* (Norte, Sul, Leste, Noroeste, Sudoeste, Central) é divisão administrativa e de localização; *macrozona* é divisão do Plano Diretor para o planejamento urbano; *distrito* é divisão territorial criada por lei.
"""
S[5]="""## 5. Na rotina do guarda

- **Despacho de viaturas:** as ocorrências são distribuídas por região; saber que Ouro Verde é Sudoeste e Barão Geraldo é Norte agiliza o atendimento.
- **Rodovias como referência:** a Rodovia dos Bandeirantes e a Santos Dumont limitam Campo Grande e Ouro Verde; a SP-101 delimita a Região Noroeste.
- **Região Leste rural:** Sousas e Joaquim Egídio têm áreas de proteção ambiental e de mananciais; atenção a crimes ambientais.
- **Centro:** maior concentração de comércio e serviços; foco de policiamento preventivo e de fiscalização de posturas.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| "Zona Oeste" | Corresponde às regiões Noroeste (Campo Grande) e Sudoeste (Ouro Verde, Viracopos) |
| Sousas e Joaquim Egídio | Região Leste |
| Barão Geraldo e Nova Aparecida | Região Norte |
| Campo Grande | Região Noroeste |
| Ouro Verde, Viracopos, DICs | Região Sudoeste |
| Taquaral, Nova Campinas | Região Leste |
| Macrozonas | Quatro, no Plano Diretor (LC 189/2018) |
| Região x macrozona x distrito | Administração e localização x planejamento urbano x divisão territorial por lei |
| Rio que abastece a cidade | Atibaia (região Leste, Sousas) |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Regiões | Central, Norte, Sul, Leste, Noroeste e Sudoeste |
| Administrações regionais | Catorze, segundo a enciclopédia |
| Saúde | Distritos de Saúde por região |
| Macrozonas (LC 189/2018) | Macrometropolitana, Estruturação Urbana, Desenvolvimento Ordenado, Relevância Ambiental |
| Bacias | Piracicaba (N, C, L) e Capivari (NO, SO, S) |
| Ponto mais alto | Serra das Cabras, Joaquim Egídio, Região Leste |
"""
QR=[("Questão 1","Os distritos de Sousas e Joaquim Egídio localizam-se na Região",["Leste de Campinas.","Norte de Campinas.","Sudoeste de Campinas.","Noroeste de Campinas.","Sul de Campinas."],0,"Wikipédia, Região Leste."),
("Questão 2","O distrito de Ouro Verde e o Aeroporto de Viracopos localizam-se na Região",["Sudoeste.","Leste.","Norte.","Central.","Noroeste."],1,"Wikipédia, Região Sudoeste."),
("Questão 3","O Plano Diretor Estratégico de Campinas divide o município em quantas macrozonas?",["Quatro.","Duas.","Seis.","Catorze.","Vinte."],2,"LC 189/2018, art. 5º."),
("Questão 4","A Região Norte de Campinas engloba os distritos de",["Barão Geraldo e Nova Aparecida.","Sousas e Joaquim Egídio.","Ouro Verde e Campo Grande.","Campo Grande e Barão Geraldo.","Nova Aparecida e Sousas."],3,"Wikipédia, Região Norte.")]
t1="<strong>Chamado no Ouro Verde</strong><br><br>A central da Guarda Municipal recebeu um chamado de um bairro do distrito de Ouro Verde, próximo ao Aeroporto de Viracopos, e precisou acionar a base regional correspondente."
t2="<strong>Ronda na Unicamp</strong><br><br>Uma viatura fazia ronda no entorno da Unicamp, no distrito de Barão Geraldo."
t3="<strong>Mananciais</strong><br><br>A guarda recebeu denúncia de despejo de entulho às margens do Rio Atibaia, no distrito de Sousas."
tx={"geo3a":t1,"geo3b":t2,"geo3c":t3}
# n=1
q(1,"Segundo a enciclopédia, Campinas divide-se em seis regiões: Central, Norte, Leste, Sul, Noroeste e",["Sudoeste.","Oeste.","Nordeste.","Sudeste.","Centro-Oeste."],"Wikipédia.")
q(1,"A região mais densamente urbanizada e verticalizada de Campinas é a",["Central.","Leste.","Sudoeste.","Noroeste.","Norte."],"Wikipédia, Região Central.")
q(1,"O distrito de Campo Grande localiza-se na Região",["Noroeste.","Leste.","Norte.","Central.","Sul."],"Wikipédia, Região Noroeste.")
q(1,"O distrito de Barão Geraldo localiza-se na Região",["Norte.","Sul.","Leste.","Sudoeste.","Noroeste."],"Wikipédia, Região Norte.")
q(1,"O distrito de Nova Aparecida localiza-se na Região",["Norte.","Leste.","Sudoeste.","Sul.","Central."],"Wikipédia, Região Norte.")
q(1,"O distrito de Sousas localiza-se na Região",["Leste.","Oeste.","Sul.","Noroeste.","Sudoeste."],"Wikipédia, Região Leste.")
q(1,"O Aeroporto de Viracopos localiza-se na Região",["Sudoeste.","Norte.","Leste.","Central.","Noroeste."],"Wikipédia, Região Sudoeste.")
q(1,"Os DICs, conjuntos habitacionais ligados ao Distrito Industrial, ficam na Região",["Sudoeste.","Leste.","Norte.","Central.","Noroeste."],"Wikipédia, Região Sudoeste.")
q(1,"O Taquaral e a Nova Campinas são bairros da Região",["Leste.","Sudoeste.","Noroeste.","Norte.","Sul."],"Wikipédia, Região Leste.")
q(1,"O Jardim Proença e o Parque Prado são bairros da Região",["Sul.","Norte.","Leste.","Noroeste.","Sudoeste."],"Wikipédia, Região Sul.")
q(1,"A Região dos Amarais e o Jardim Chapadão ficam na Região",["Norte.","Sul.","Sudoeste.","Leste.","Central."],"Wikipédia, Região Norte.")
q(1,"O Plano Diretor Estratégico de Campinas é a Lei Complementar Municipal",["189/2018.","870/2000.","1.399/1955.","15.058/2015.","21.019/2020."],"SAPL.")
q(1,"Uma das macrozonas do Plano Diretor é a Macrozona de Relevância",["Ambiental.","Comercial.","Turística.","Militar.","Portuária."],"LC 189/2018, art. 5º, IV.")
q(1,"Uma das macrozonas do Plano Diretor é a Macrozona",["Macrometropolitana.","Litorânea.","Fronteiriça.","Amazônica.","Industrial Federal."],"LC 189/2018, art. 5º, I.")
q(1,"A Secretaria de Saúde organiza a cidade em Distritos de Saúde, como o Distrito de Saúde",["Noroeste.","Litoral.","Central Federal.","Metropolitano.","Paulista."],"Lei 15.780/2019, ementa.")
q(1,"O rio que é a principal fonte de abastecimento de água de Campinas é o",["Atibaia.","Tietê.","Paraíba do Sul.","Piracicaba, em Piracicaba.","Capivari-Mirim."],"Wikipédia, hidrografia.")
q(1,"O ponto mais alto de Campinas fica na Serra das Cabras, no distrito de",["Joaquim Egídio.","Barão Geraldo.","Ouro Verde.","Campo Grande.","Nova Aparecida."],"Wikipédia.")
q(1,"No texto do chamado no Ouro Verde, a ocorrência fica na Região",["Sudoeste.","Norte.","Leste.","Central.","Noroeste."],"Ouro Verde e Viracopos: Sudoeste.","geo3a")
q(1,"No texto da ronda na Unicamp, a viatura está na Região",["Norte.","Sul.","Leste.","Sudoeste.","Noroeste."],"Barão Geraldo: Região Norte.","geo3b")
q(1,"No texto dos mananciais, a ocorrência em Sousas fica na Região",["Leste.","Oeste.","Sul.","Noroeste.","Sudoeste."],"Sousas: Região Leste.","geo3c")
# n=2
q(2,"A 'zona oeste' mencionada no edital corresponde, na organização do município, às regiões",["Noroeste e Sudoeste.","Norte e Leste.","Sul e Central.","Leste e Sul.","Central e Norte."],"A Prefeitura usa Noroeste e Sudoeste.")
q(2,"A Região Noroeste ocupa a área entre as rodovias",["SP-101 e SP-348 (Bandeirantes).","Anhanguera e D. Pedro I.","Dutra e Fernão Dias.","Santos Dumont e D. Pedro I.","SP-304 e Anhanguera."],"Wikipédia, Região Noroeste.")
q(2,"A Região Central concentra",["a maior parte dos estabelecimentos comerciais, médicos e de serviços.","as áreas rurais da cidade.","o Aeroporto de Viracopos.","os distritos de Sousas e Joaquim Egídio.","a Unicamp."],"Wikipédia, Região Central.")
q(2,"Os shoppings Iguatemi e Parque D. Pedro ficam na Região",["Leste.","Sudoeste.","Noroeste.","Norte.","Central."],"Wikipédia, Região Leste.")
q(2,"O Distrito Industrial de Campinas fica na Região",["Sudoeste.","Leste.","Norte.","Central.","Noroeste."],"Wikipédia, Região Sudoeste.")
q(2,"Segundo a enciclopédia, Campinas tem quantas administrações regionais?",["Catorze.","Quatro.","Seis.","Vinte.","Duas."],"Wikipédia.")
q(2,"A Macrozona de Estruturação Urbana abrange região situada integralmente no",["perímetro urbano, com áreas consolidadas e em consolidação.","perímetro rural.","território de outro município.","Aeroporto de Viracopos, apenas.","leito dos rios."],"LC 189/2018, art. 5º, II.")
q(2,"A Macrozona de Desenvolvimento Ordenado abrange região situada integralmente na",["zona rural.","área central.","Região Leste urbana.","zona portuária.","área do aeroporto, apenas."],"LC 189/2018, art. 5º, III.")
q(2,"A Macrozona Macrometropolitana abrange área urbana impactada por estruturas viárias, equipamentos e atividades econômicas de abrangência",["regional, nacional e internacional.","apenas municipal.","apenas de bairro.","apenas rural.","apenas estadual."],"LC 189/2018, art. 5º, I.")
q(2,"A Macrozona de Relevância Ambiental apresenta áreas estratégicas à preservação ambiental e dos",["recursos hídricos.","shoppings.","rodovias.","aeroportos.","centros comerciais."],"LC 189/2018, art. 5º, IV.")
q(2,"A bacia do Rio Piracicaba, que abrange o Atibaia e os ribeirões Anhumas e Quilombo, ocupa as regiões",["Norte, Central e Leste.","Sudoeste e Sul, apenas.","Noroeste, apenas.","Sul e Sudoeste.","Leste e Sudoeste."],"Wikipédia, hidrografia.")
q(2,"A bacia do Rio Capivari, que abrange o ribeirão Piçarrão, ocupa as regiões",["Noroeste, Sudoeste e Sul.","Norte e Leste.","Central e Leste.","Leste, apenas.","Norte, apenas."],"Wikipédia, hidrografia.")
q(2,"O Observatório Municipal Jean Nicolini, próximo ao ponto mais alto da cidade, fica na Região",["Leste.","Sudoeste.","Noroeste.","Norte.","Sul."],"Wikipédia.")
q(2,"Historicamente, a região de Campinas com a maior parte dos núcleos de pobreza, segundo a enciclopédia, era a",["Sudoeste.","Leste.","Central.","Norte.","Noroeste."],"Wikipédia, pobreza e desigualdade.")
q(2,"O Parque Oziel, ocupação em processo de legalização, fica na Região",["Sul.","Norte.","Leste.","Central.","Noroeste."],"Wikipédia, Região Sul.")
q(2,"O Cambuí e a Vila Itapura são bairros da Região",["Central.","Sudoeste.","Norte.","Noroeste.","Sul."],"Wikipédia, Região Central.")
q(2,"Barão Geraldo, além de distrito da Região Norte, é conhecido por sediar a",["Unicamp.","Prefeitura.","Câmara Municipal.","Viracopos.","Cidade Judiciária."],"Wikipédia, Barão Geraldo.")
q(2,"No texto do chamado no Ouro Verde, a ocorrência fica numa região cuja bacia hidrográfica é a do Rio",["Capivari.","Atibaia.","Tietê.","Paraíba do Sul.","Jaguari."],"Sudoeste: bacia do Capivari.","geo3a")
q(2,"No texto da ronda na Unicamp, o mesmo distrito da Região Norte dessa ronda abriga também, segundo a enciclopédia, o",["Hospital de Clínicas da Unicamp.","Paço Municipal.","Aeroporto de Viracopos.","Mercado Municipal.","Terminal Multimodal."],"Wikipédia, Barão Geraldo.","geo3b")
q(2,"No texto dos mananciais, o Rio Atibaia é importante porque dele vem",["a maior parte da água captada para Campinas.","toda a energia elétrica.","o petróleo da região.","a água do mar.","o gás natural."],"Wikipédia: 95% da captação.","geo3c")
# n=3
q(3,"Assinale a alternativa correta sobre a localização em Campinas.",["Sousas e Joaquim Egídio ficam na Região Leste; Campo Grande, na Noroeste; Ouro Verde, na Sudoeste.","Sousas fica na Região Sudoeste.","Campo Grande fica na Região Leste.","Ouro Verde fica na Região Norte.","Barão Geraldo fica na Região Sul."],"Wikipédia.")
q(3,"Considere. I. Barão Geraldo e Nova Aparecida ficam na Região Norte. II. Viracopos fica na Região Leste. III. O Distrito Industrial fica na Região Sudoeste. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Viracopos fica na Região Sudoeste.")
q(3,"Assinale a INCORRETA.",["O Plano Diretor divide o município em seis macrozonas.","O Plano Diretor tem a Macrozona de Relevância Ambiental.","A Macrozona de Desenvolvimento Ordenado é rural.","A Macrozona Macrometropolitana é urbana.","A Macrozona de Estruturação Urbana é urbana."],"São quatro macrozonas.")
q(3,"Diferencie: região, macrozona e distrito são, respectivamente,",["divisão administrativa e de localização; divisão do Plano Diretor; divisão territorial criada por lei.","sinônimos.","divisão eleitoral; divisão judiciária; divisão policial.","divisão estadual; federal; municipal.","divisão de saúde; de educação; de trânsito."],"Ver seção 3.")
q(3,"Segundo o Plano Diretor, as áreas das macrozonas serão descritas em",["decreto.","lei federal.","resolução do Senado.","portaria da Câmara.","emenda constitucional."],"LC 189/2018, art. 5º, § 2º.")
q(3,"Na Macrozona de Desenvolvimento Ordenado poderá haver expansão do perímetro urbano mediante estudos técnicos e",["lei complementar específica.","decreto do prefeito, apenas.","resolução do Conselho Tutelar.","portaria da Guarda.","consulta informal."],"LC 189/2018, art. 5º, § 1º.")
q(3,"A regra de localização usada pela enciclopédia para a Região Noroeste é estar a norte da SP-101 e a leste da",["Rodovia dos Bandeirantes (SP-348).","Rodovia D. Pedro I.","Rodovia Anhanguera.","Rodovia Dutra.","Rodovia SP-304."],"Wikipédia: entre a SP-101 (a sul) e a SP-348 (a oeste).")
q(3,"Assinale a correspondência correta entre bairro e região.",["Taquaral – Leste; DICs – Sudoeste; Jardim Proença – Sul.","Taquaral – Sudoeste; DICs – Leste.","Jardim Proença – Norte; Taquaral – Sul.","DICs – Norte; Taquaral – Central.","Cambuí – Sudoeste; DICs – Central."],"Wikipédia.")
q(3,"Ao descrever quatro distritos e dois 'em processo de criação', a enciclopédia está desatualizada porque Campo Grande e Ouro Verde foram criados em",["2015, por leis municipais.","1896, por lei estadual.","1959, por lei estadual.","2024, por decreto.","1964, por lei federal."],"Leis 15.058 e 15.059/2015.")
q(3,"A região de Campinas com bairros residenciais de alto padrão, distritos turísticos e áreas rurais e de proteção ambiental é a",["Leste.","Sudoeste.","Noroeste.","Central.","Sul."],"Wikipédia, Região Leste.")
q(3,"O ponto mais baixo do perímetro urbano, segundo a enciclopédia, ocorre em lados opostos da cidade, próximo ao Rio das Pedras (Barão Geraldo) e ao Rio",["Capivari (Ouro Verde).","Atibaia (Sousas).","Tietê.","Jaguari.","Anhumas (Centro)."],"Wikipédia, Geografia.")
q(3,"A região mais alta dentro do perímetro urbano de Campinas é o Jardim São Gabriel, na Região",["Sul.","Leste.","Norte.","Sudoeste.","Noroeste."],"Wikipédia, Geografia.")
q(3,"Geomorfologicamente, Campinas fica em área de transição entre a Depressão Periférica Paulista, mais notada a oeste, e o",["Planalto Ocidental, mais perceptível a leste.","Planalto Atlântico, a oeste.","litoral, a leste.","Pantanal.","Planalto Central."],"Wikipédia, Geografia.")
q(3,"Assinale a alternativa que associa corretamente distrito e região.",["Nova Aparecida – Norte; Joaquim Egídio – Leste; Campo Grande – Noroeste.","Nova Aparecida – Sudoeste; Joaquim Egídio – Norte.","Campo Grande – Leste; Ouro Verde – Norte.","Sousas – Noroeste; Barão Geraldo – Sul.","Joaquim Egídio – Sudoeste; Ouro Verde – Leste."],"Wikipédia.")
q(3,"No texto do chamado no Ouro Verde, se o chamado viesse do Campo Grande, a região seria a",["Noroeste.","Sudoeste.","Leste.","Norte.","Central."],"Campo Grande: Noroeste.","geo3a")
q(3,"No texto do chamado no Ouro Verde, a ocorrência fica próxima ao aeroporto, área que, no Plano Diretor, se liga à macrozona impactada por estruturas de abrangência internacional, a",["Macrometropolitana.","de Relevância Ambiental.","de Desenvolvimento Ordenado.","Rural.","Litorânea."],"LC 189/2018, art. 5º, I.","geo3a")
q(3,"No texto da ronda na Unicamp, a viatura que seguisse para Nova Aparecida permaneceria na Região",["Norte.","Leste.","Sudoeste.","Sul.","Noroeste."],"Ambos na Norte.","geo3b")
q(3,"No texto dos mananciais, a área às margens do Rio Atibaia em Sousas tende a estar na macrozona voltada à preservação ambiental e dos recursos hídricos, a",["de Relevância Ambiental.","Macrometropolitana.","de Estruturação Urbana.","Industrial.","Portuária."],"LC 189/2018, art. 5º, IV.","geo3c")
q(3,"No texto dos mananciais, a conduta de despejar entulho às margens do rio pode configurar crime ambiental, por exemplo, de",["poluição (Lei 9.605/1998, art. 54).","furto.","dano ao patrimônio privado, apenas.","contravenção de trânsito.","estelionato."],"Lei 9.605/1998, art. 54.","geo3c")
q(3,"No texto dos mananciais, a guarda deve também comunicar o órgão ambiental, porque a área está na bacia do Rio",["Piracicaba (sub-bacia do Atibaia).","Capivari.","Tietê.","Paraná.","Grande."],"Wikipédia, hidrografia.","geo3c")
b.fim()
code,svg=mapa("Zonas e regiões de Campinas",[
 ("c","Central",["Centro, Cambuí","mais verticalizada"],"seção 2"),
 ("n","Norte",["Barão Geraldo","Nova Aparecida, Amarais"],"seção 2"),
 ("l","Leste",["Sousas, Joaquim Egídio","Taquaral, Nova Campinas"],"seção 2"),
 ("o","Oeste (NO + SO)",["Campo Grande (NO)","Ouro Verde, Viracopos (SO)"],"seção 1"),
 ("s","Sul",["Jardim Proença, Parque Prado","Parque Oziel"],"seção 2"),
 ("m","Macrozonas",["quatro","LC 189/2018"],"seção 3")],
 "Na prova: ligue cada distrito à sua região")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"Cada caixa traz uma região e seus distritos e bairros; a última, as macrozonas do Plano Diretor.","Fontes: Edital 02/2026, Anexo I; Lei Complementar Municipal 189/2018 (Plano Diretor), art. 5º (SAPL); Lei Municipal 15.780/2019 (SAPL); Wikipédia, verbete Campinas (descrição das regiões). Exemplos criados para a aula.")
revisao("geo-3","Geografia: zonas geográficas de Campinas",b.Q,list(tx),
 cobertura=["Divisão por zonas e regiões, organização territorial e administrativa (recorte do edital)."],
 pendencias=["A descrição das regiões vem da Wikipédia; conferir no portal da Prefeitura (mapa das Administrações Regionais e dos Distritos de Saúde).","O edital fala em Norte, Sul, Leste e Oeste; a organização municipal usa Noroeste e Sudoeste. A aula trata 'Oeste' como Noroeste + Sudoeste: confirmar como a banca cobrará.","Casos geo3a, geo3b e geo3c fictícios."],
 fontes_conferidas=["Plano Diretor (LC 189/2018), art. 5º: SAPL.","Wikipédia: regiões, hidrografia, relevo."])
gravar("geo-3",aula_html,banco("geo-3",b.Q),tx)
