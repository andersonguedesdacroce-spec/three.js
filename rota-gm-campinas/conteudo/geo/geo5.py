import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _geo import *
b=B(); q=b.q
LEAD="Próprios públicos são os imóveis e equipamentos que pertencem ao poder público municipal: sedes administrativas, unidades de saúde e de educação, equipamentos de segurança e centros de referência. O guarda municipal tem o dever constitucional de proteger esses bens, serviços e instalações, por isso o edital cobra onde ficam os principais deles. A banca também gosta de misturar com equipamentos que ficam em Campinas, mas não são municipais, como a Cidade Judiciária (Estado), a Unicamp (Estado) e o Aeroporto de Viracopos (União, sob concessão)."
S={}
S[1]="## 1. Sedes administrativas\n\n"+C("Wikipédia, verbete Palácio dos Jequitibás","Palácio dos Jequitibás, também conhecido como Paço Municipal de Campinas (PCM), é o edifício no qual se localiza a prefeitura de Campinas,")+"\n\n"+C("Wikipédia, verbete Palácio dos Jequitibás","Localizado à Avenida Anchieta, nº 200, o prédio tem dezenove pavimentos,")+"\n\n"+C("Câmara Municipal de Campinas (SAPL), rodapé dos documentos","Avenida da Saudade, nº 1.004 – Ponte Preta – CEP: 13041-670 – Campinas – SP")+"""

**O que é, em uma frase:** próprio público municipal é o imóvel ou equipamento que pertence ao Município e serve à administração ou à população.

- **Paço Municipal (Palácio dos Jequitibás):** sede da Prefeitura desde 1969, na Avenida Anchieta, 200, no Centro. Inaugurado em 28 de outubro de 1968, substituiu o antigo Palácio dos Azulejos. O nome lembra os jequitibás centenários do terreno. Até 2005 abrigou também a Câmara.
- **Câmara Municipal:** sede própria na Avenida da Saudade, 1.004, no bairro Ponte Preta (transferência concluída em 2006). Tem 33 vereadores.
- **Subprefeituras e Administrações Regionais:** atendem os distritos e as regiões da cidade.
"""
S[2]="## 2. Saúde, educação e assistência social\n\n"+C("Wikipédia, verbete Hospital Municipal Doutor Mário Gatti","O Hospital Municipal Doutor Mário Gatti é um hospital público municipal, localizado na cidade de Campinas, fundado em 14 de julho de 1974,")+"\n\n"+C("Wikipédia, verbete Campinas","Também há 61 Centros de Saúde (Unidades Básicas de Saúde), aproximadamente 1 para cada 20 mil habitantes.")+"\n\n"+C("Portal da Prefeitura de Campinas, título de página","DAS – Distrito de Assistência Social e CRAS – Centro de Referência de Assistência Social")+"""

- **Hospital Municipal Dr. Mário Gatti:** hospital público municipal, inaugurado em 14 de julho de 1974 (bicentenário da cidade), referência em urgência e emergência para a região, com status de hospital de ensino desde 2004.
- **Centros de Saúde (UBS):** cerca de 61 unidades, organizadas por Distritos de Saúde (Norte, Sul, Leste, Noroeste e Sudoeste).
- **SAMU:** atendimento móvel de urgência.
- **Assistência social:** CRAS (Centros de Referência de Assistência Social), organizados em Distritos de Assistência Social (DAS).
- **Educação:** a rede municipal tem escolas de educação infantil e ensino fundamental; a Unicamp e a PUC-Campinas **não** são municipais.
"""
S[3]="## 3. Cultura, mobilidade, serviços e segurança\n\n"+C("Wikipédia, verbete Estação Cultura (Campinas)","Estação Cultura Prefeito Antônio da Costa Santos. Uso atual: Centro cultural. Administração: Prefeitura de Campinas.")+"\n\n"+C("Wikipédia, verbete Campinas","O Terminal Multimodal Ramos de Azevedo é a principal estação de transporte intermunicipal e interestadual da cidade de Campinas.")+"\n\n"+C("Wikipédia, verbete Campinas","Por força da Constituição Federal do Brasil, Campinas possui também uma Guarda Municipal, responsável pela proteção dos bens, serviços e instalações públicas do município.")+"\n\n"+C("Wikipédia, verbete Campinas","Campinas é a sede de uma comarca do poder judiciário estadual,")+"""

- **Estação Cultura:** antiga estação ferroviária (inaugurada em 1872, fechada como estação em 2001), hoje centro cultural administrado pela Prefeitura, na Praça Marechal Floriano Peixoto, no Centro.
- **Terminal Multimodal Ramos de Azevedo:** principal terminal rodoviário intermunicipal e interestadual, inaugurado em 2008.
- **EMDEC:** empresa municipal subordinada à Secretaria de Transportes; regulamenta o transporte público, gerencia o trânsito e autua por meio de seus Agentes de Trânsito.
- **SANASA:** empresa municipal de água e esgoto; capta 95% da água no Rio Atibaia.
- **Guarda Municipal:** proteção dos bens, serviços e instalações do Município.

**Pegadinha (não são próprios municipais):** a Cidade Judiciária, no Jardim Santana (Região Leste), é do Poder Judiciário estadual; a Unicamp e o Hospital de Clínicas da Unicamp são estaduais; o Aeroporto de Viracopos é federal, operado por concessão.
"""
S[5]="""## 5. Na rotina do guarda

- **Proteção dos próprios:** a Guarda protege o Paço, a Câmara, as unidades de saúde, as escolas municipais e os equipamentos culturais; a vigilância patrimonial é atribuição central (Lei 13.022/2014).
- **Unidades de saúde:** o guarda atua em ocorrências de agressão a servidores e de dano ao patrimônio em Centros de Saúde e no Mário Gatti.
- **Escolas municipais:** a ronda escolar previne violência no entorno.
- **Estação Cultura e Centro:** eventos com grande público exigem planejamento integrado.
- **Fora da competência:** na Cidade Judiciária (Estado) e em Viracopos (União), a guarda atua em apoio, respeitando a competência dos demais órgãos.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Sede da Prefeitura | Paço Municipal (Palácio dos Jequitibás), Av. Anchieta, 200 |
| Sede da Câmara | Av. da Saudade, 1.004, Ponte Preta (desde 2006) |
| Hospital municipal de urgência | Mário Gatti (inaugurado em 1974) |
| Unicamp e HC da Unicamp | Estaduais, não municipais |
| Cidade Judiciária | Judiciário estadual, Jardim Santana, Região Leste |
| Viracopos | Federal (concessão), não municipal |
| Estação Cultura | Centro cultural administrado pela Prefeitura |
| EMDEC e SANASA | Empresas municipais (trânsito e transporte; água e esgoto) |
| CRAS | Centro de Referência de Assistência Social |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Paço Municipal | Palácio dos Jequitibás, Av. Anchieta, 200, desde 1969 |
| Câmara Municipal | Av. da Saudade, 1.004, Ponte Preta; 33 vereadores |
| Saúde | Mário Gatti; 61 Centros de Saúde; Distritos de Saúde; SAMU |
| Assistência | CRAS e Distritos de Assistência Social |
| Cultura | Estação Cultura |
| Mobilidade | Terminal Multimodal Ramos de Azevedo; EMDEC |
| Água | SANASA |
| Segurança | Guarda Municipal |
"""
QR=[("Questão 1","A sede da Prefeitura de Campinas, conhecida como Paço Municipal, é o",["Palácio dos Jequitibás.","Palácio dos Azulejos.","Palácio dos Bandeirantes.","Palácio da Justiça.","Palácio do Planalto."],0,"Wikipédia, Palácio dos Jequitibás."),
("Questão 2","Assinale o equipamento que fica em Campinas, mas NÃO é próprio público municipal.",["A Cidade Judiciária.","O Paço Municipal.","O Hospital Municipal Dr. Mário Gatti.","A Estação Cultura.","Os Centros de Saúde."],1,"A Cidade Judiciária é do Judiciário estadual."),
("Questão 3","O hospital público municipal de Campinas inaugurado em 1974, referência em urgência e emergência, é o",["Hospital Municipal Dr. Mário Gatti.","Hospital de Clínicas da Unicamp.","Centro Infantil Boldrini.","Hospital das Clínicas de São Paulo.","Casa de Saúde Campinas."],2,"Wikipédia, Mário Gatti."),
("Questão 4","A Câmara Municipal de Campinas tem sede própria na",["Avenida da Saudade, no bairro Ponte Preta.","Avenida Anchieta, no Paço Municipal.","Avenida Norte-Sul, no Cambuí.","Rua Barão de Jaguara, no Centro.","Avenida John Boyd Dunlop, no Campo Grande."],3,"Rodapé dos documentos da Câmara (SAPL).")]
t1="<strong>Protesto no Paço</strong><br><br>Uma manifestação reuniu servidores em frente à sede da Prefeitura, e a Guarda Municipal foi acionada para proteger o prédio."
t2="<strong>Agressão no Centro de Saúde</strong><br><br>Um usuário agrediu uma enfermeira em um Centro de Saúde da Região Noroeste, e a guarda foi chamada."
t3="<strong>Evento na Estação</strong><br><br>Um festival cultural aconteceu na antiga estação ferroviária do Centro, hoje centro cultural."
tx={"geo5a":t1,"geo5b":t2,"geo5c":t3}
# n=1
q(1,"O Palácio dos Jequitibás é também conhecido como",["Paço Municipal de Campinas.","Câmara Municipal.","Cidade Judiciária.","Estação Cultura.","Palácio dos Azulejos."],"Wikipédia.")
q(1,"O Paço Municipal de Campinas fica na Avenida",["Anchieta, nº 200.","da Saudade, nº 1.004.","Norte-Sul, nº 1.","Paulista, nº 1.000.","John Boyd Dunlop, nº 100."],"Wikipédia.")
q(1,"O Palácio dos Jequitibás é sede da Prefeitura desde",["1969.","1774.","1872.","2006.","1990."],"Wikipédia.")
q(1,"O nome Palácio dos Jequitibás refere-se a",["árvores centenárias que havia no terreno.","um antigo prefeito.","um rio da cidade.","uma fazenda de café.","um bairro."],"Wikipédia.")
q(1,"A Câmara Municipal de Campinas fica no bairro",["Ponte Preta.","Cambuí.","Taquaral.","Barão Geraldo.","Sousas."],"SAPL.")
q(1,"O Hospital Municipal Dr. Mário Gatti foi inaugurado em",["14 de julho de 1974.","28 de outubro de 1968.","11 de agosto de 1872.","19 de junho de 2000.","5 de outubro de 2014."],"Wikipédia.")
q(1,"O Hospital Municipal Dr. Mário Gatti é um hospital",["público municipal.","privado.","federal.","estadual universitário.","filantrópico estrangeiro."],"Wikipédia.")
q(1,"Segundo a enciclopédia, Campinas conta com cerca de quantos Centros de Saúde?",["61.","6.","14.","600.","1."],"Wikipédia.")
q(1,"CRAS significa",["Centro de Referência de Assistência Social.","Centro Regional de Atendimento à Saúde.","Comando Regional de Ação de Segurança.","Conselho Regional de Assistência Social.","Central de Registro de Atos Sociais."],"Portal da Prefeitura.")
q(1,"A Estação Cultura, antiga estação ferroviária, é hoje um",["centro cultural administrado pela Prefeitura.","terminal de ônibus federal.","hospital.","quartel.","shopping center."],"Wikipédia.")
q(1,"A principal estação de transporte intermunicipal e interestadual de Campinas é o",["Terminal Multimodal Ramos de Azevedo.","Terminal Central.","Aeroporto Campo dos Amarais.","Terminal Ouro Verde.","Estação Cultura."],"Wikipédia.")
q(1,"A empresa municipal que gerencia o trânsito e o transporte público em Campinas é a",["EMDEC.","SANASA.","CPFL.","EMTU.","CETESB."],"Wikipédia.")
q(1,"A empresa municipal responsável pela água e pelo esgoto em Campinas é a",["SANASA.","EMDEC.","CPFL.","SABESP.","CETESB."],"Wikipédia.")
q(1,"A Guarda Municipal de Campinas é responsável pela proteção dos bens, serviços e",["instalações públicas do município.","propriedades privadas.","bancos privados.","rodovias federais.","fronteiras."],"Wikipédia.")
q(1,"A Cidade Judiciária de Campinas pertence ao",["Poder Judiciário estadual.","Município de Campinas.","Governo Federal, Executivo.","Câmara Municipal.","Exército."],"Wikipédia.")
q(1,"A Unicamp é uma universidade",["estadual.","municipal.","federal.","privada.","filantrópica."],"Universidade Estadual de Campinas.")
q(1,"A Câmara Municipal de Campinas é formada por",["33 vereadores.","13 vereadores.","55 vereadores.","9 vereadores.","100 vereadores."],"Wikipédia.")
q(1,"No texto do protesto no Paço, o prédio protegido é o",["Palácio dos Jequitibás.","Palácio dos Azulejos.","Cidade Judiciária.","Estação Cultura.","Terminal Multimodal."],"Sede da Prefeitura.","geo5a")
q(1,"No texto da agressão no Centro de Saúde, a unidade é um próprio público",["municipal.","federal.","estadual.","privado.","estrangeiro."],"Centros de Saúde são municipais.","geo5b")
q(1,"No texto do evento na Estação, o centro cultural é a",["Estação Cultura.","Cidade Judiciária.","Câmara Municipal.","Unicamp.","Viracopos."],"Wikipédia.","geo5c")
# n=2
q(2,"O Paço Municipal substituiu, como sede da municipalidade, o antigo",["Palácio dos Azulejos.","Palácio dos Bandeirantes.","Palácio da Justiça.","Solar do Barão.","Mercado Municipal."],"Wikipédia.")
q(2,"O Paço Municipal foi inaugurado oficialmente em",["28 de outubro de 1968.","14 de julho de 1974.","11 de agosto de 1872.","10 de setembro de 2015.","19 de junho de 2000."],"Wikipédia.")
q(2,"Até 2005, o Palácio dos Jequitibás abrigou também",["a Câmara Municipal.","a Unicamp.","a Cidade Judiciária.","o Aeroporto.","a SANASA."],"Wikipédia.")
q(2,"A transferência da Câmara Municipal para imóvel próprio no bairro Ponte Preta foi concluída em",["2006.","1969.","1974.","2015.","2000."],"Wikipédia.")
q(2,"O Hospital Mário Gatti foi inaugurado no ano do",["bicentenário de Campinas.","centenário da República.","cinquentenário da Unicamp.","sesquicentenário do Brasil.","milênio."],"Wikipédia: 14/07/1974, bicentenário da cidade.")
q(2,"O Hospital Mário Gatti teve reconhecido o status de hospital de ensino em",["2004.","1974.","1990.","2015.","1968."],"Wikipédia.")
q(2,"Os Centros de Saúde de Campinas correspondem, segundo a enciclopédia, a cerca de um para cada",["20 mil habitantes.","2 mil habitantes.","200 mil habitantes.","1 milhão de habitantes.","500 habitantes."],"Wikipédia.")
q(2,"A assistência social municipal organiza-se em Distritos de Assistência Social e em",["Centros de Referência de Assistência Social (CRAS).","Conselhos Tutelares, apenas.","Delegacias.","Fóruns.","Batalhões."],"Portal da Prefeitura.")
q(2,"A Estação Cultura fica na Praça",["Marechal Floriano Peixoto.","Carlos Gomes.","Rui Barbosa.","da Sé.","Bento Quirino."],"Wikipédia.")
q(2,"A Estação Cultura foi inaugurada como estação ferroviária em",["1872.","1969.","2001.","2008.","1774."],"Wikipédia.")
q(2,"O Terminal Multimodal Ramos de Azevedo foi inaugurado em",["2008.","1968.","1974.","2015.","1990."],"Wikipédia.")
q(2,"A EMDEC é subordinada à Secretaria Municipal de",["Transportes.","Saúde.","Educação.","Cultura.","Fazenda."],"Wikipédia.")
q(2,"A EMDEC aplica autuações aos motoristas por meio de seus",["Agentes de Trânsito.","guardas florestais.","policiais rodoviários federais.","fiscais sanitários.","oficiais de justiça."],"Wikipédia.")
q(2,"A maior parte da água captada pela SANASA vem do Rio",["Atibaia.","Tietê.","Capivari.","Jaguari.","Piracicaba, em Piracicaba."],"Wikipédia: 95%.")
q(2,"A Cidade Judiciária de Campinas fica no bairro Jardim Santana, na Região",["Leste.","Sudoeste.","Noroeste.","Norte.","Sul."],"Wikipédia.")
q(2,"O Hospital de Clínicas da Unicamp, em Barão Geraldo, é",["estadual, ligado à Unicamp.","municipal.","federal.","privado.","militar."],"Unicamp é estadual.")
q(2,"O Aeroporto de Viracopos, em Campinas, NÃO é próprio público municipal porque",["é aeroporto federal operado por concessão.","é bem privado de pessoa física.","pertence a Indaiatuba.","é estadual.","não está em Campinas."],"Viracopos é federal (concessão).")
q(2,"No texto do protesto no Paço, a atuação da guarda é de proteção a próprio público, conforme a função de proteger bens, serviços e",["instalações do Município.","empresas privadas.","rodovias federais.","bancos.","igrejas."],"Wikipédia; Lei 13.022/2014.","geo5a")
q(2,"No texto da agressão no Centro de Saúde, a unidade pertence a um Distrito de Saúde organizado por região; neste caso, o Distrito de Saúde",["Noroeste.","Leste.","Sul.","Norte.","Central."],"Lei 15.780/2019 menciona o Distrito de Saúde Noroeste.","geo5b")
q(2,"No texto do evento na Estação, a antiga estação fechou como estação ferroviária em",["2001.","1872.","1969.","2008.","1974."],"Wikipédia.","geo5c")
# n=3
q(3,"Assinale a alternativa que traz apenas próprios públicos municipais de Campinas.",["Paço Municipal, Hospital Mário Gatti e Estação Cultura.","Paço Municipal, Unicamp e Estação Cultura.","Cidade Judiciária, Mário Gatti e Paço.","Viracopos, Paço e Estação Cultura.","HC da Unicamp, Mário Gatti e Paço."],"Unicamp, HC, Cidade Judiciária e Viracopos não são municipais.")
q(3,"Considere. I. O Paço Municipal fica na Av. Anchieta. II. A Câmara fica na Av. da Saudade, Ponte Preta. III. A Cidade Judiciária é municipal. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A Cidade Judiciária é do Judiciário estadual.")
q(3,"Assinale a INCORRETA.",["A Unicamp é universidade municipal de Campinas.","O Mário Gatti é hospital público municipal.","A SANASA cuida da água e do esgoto.","A EMDEC gerencia o trânsito.","A Estação Cultura é administrada pela Prefeitura."],"A Unicamp é estadual.")
q(3,"A Prefeitura de Campinas fica no Centro, e a Câmara Municipal, em",["sede própria no bairro Ponte Preta, desde 2006.","um anexo do Paço Municipal até hoje.","Barão Geraldo.","Sousas.","Viracopos."],"Wikipédia e SAPL.")
q(3,"Na organização da saúde municipal, os Centros de Saúde se agrupam em",["Distritos de Saúde por região.","Comarcas.","Zonas eleitorais.","Macrozonas do Plano Diretor.","Seções policiais."],"Lei 15.780/2019 (Distrito de Saúde Noroeste).")
q(3,"O Hospital Mário Gatti é muito demandado para emergências e urgências na",["Região Metropolitana de Campinas.","capital paulista, apenas.","Baixada Santista.","região Sul do país.","fronteira."],"Wikipédia.")
q(3,"A Estação Cultura leva também o nome de Prefeito Antônio da Costa Santos e é administrada pela",["Prefeitura de Campinas.","União.","Unicamp.","CPFL.","Rede Ferroviária Federal."],"Wikipédia.")
q(3,"O Terminal Multimodal Ramos de Azevedo substituiu, em 2008, a antiga Estação Rodoviária",["Dr. Barbosa de Barros.","Ramos de Azevedo.","Mogiana.","Paulista.","Funilense."],"Wikipédia.")
q(3,"Assinale a associação correta entre órgão ou empresa e função.",["EMDEC – trânsito e transporte; SANASA – água e esgoto; Guarda – proteção de bens, serviços e instalações.","EMDEC – água; SANASA – trânsito.","Guarda – arrecadação de tributos.","SANASA – segurança pública.","EMDEC – saúde."],"Wikipédia.")
q(3,"A Cidade Judiciária e a Unicamp, embora em Campinas, pertencem",["ao Estado de São Paulo (Judiciário estadual e universidade estadual).","ao Município.","à União.","a particulares.","à RMC."],"Wikipédia.")
q(3,"Em relação ao Aeroporto de Viracopos, o Município de Campinas",["não é proprietário; trata-se de aeroporto federal sob concessão.","é proprietário.","administra diretamente pela EMDEC.","administra pela SANASA.","administra pela Guarda."],"Viracopos é federal.")
q(3,"O Aeroporto Campo dos Amarais, voltado a aviões de pequeno e médio porte e ao ensino de pilotagem, fica na Região",["Norte.","Sudoeste.","Leste.","Sul.","Central."],"Wikipédia.")
q(3,"Os 61 Centros de Saúde são Unidades Básicas de Saúde, ou seja, porta de entrada da",["atenção básica do SUS.","Justiça estadual.","assistência privada.","educação superior.","segurança federal."],"Wikipédia: Centros de Saúde (UBS).")
q(3,"A proteção dos próprios públicos municipais é atribuição da Guarda Municipal prevista, em âmbito federal, na",["Lei 13.022/2014 (Estatuto Geral das Guardas Municipais).","Lei 9.503/1997.","Lei 8.069/1990.","Lei 11.340/2006.","Lei 5.172/1966."],"Lei 13.022/2014.")
q(3,"O Palácio dos Jequitibás tem dezenove pavimentos e foi projetado após concurso organizado pelo",["IAB-SP.","Exército.","Unicamp.","IBGE.","Detran."],"Wikipédia.")
q(3,"Na hipótese de dano a um Centro de Saúde, o bem lesado é",["público municipal, sob proteção da Guarda.","privado.","federal.","estadual.","de ninguém."],"Centros de Saúde são municipais.")
q(3,"No texto do protesto no Paço, o prédio fica na Avenida",["Anchieta, 200, no Centro.","da Saudade, 1.004.","John Boyd Dunlop.","Norte-Sul.","Moraes Salles."],"Wikipédia.","geo5a")
q(3,"No texto do protesto no Paço, se a manifestação fosse em frente à Câmara, a guarda seria acionada para o bairro",["Ponte Preta.","Cambuí.","Taquaral.","Barão Geraldo.","Ouro Verde."],"SAPL.","geo5a")
q(3,"No texto da agressão no Centro de Saúde, a agressão à enfermeira no exercício da função também pode configurar crime contra a pessoa e, por ser servidora pública, exige atenção à",["proteção do serviço público e do servidor.","propriedade privada.","jurisdição federal.","competência militar.","imunidade parlamentar."],"Proteção de serviços e instalações municipais.","geo5b")
q(3,"No texto do evento na Estação, o festival ocorre em local administrado pela Prefeitura, situado na Praça",["Marechal Floriano Peixoto, no Centro.","Carlos Gomes, no Cambuí.","da Sé, em São Paulo.","Arautos da Paz, no Taquaral.","Imprensa Fluminense."],"Wikipédia.","geo5c")
b.fim()
code,svg=mapa("Próprios públicos de Campinas",[
 ("adm","Sedes administrativas",["Paço: Av. Anchieta, 200","Câmara: Av. da Saudade, 1.004","subprefeituras e ARs"],"seção 1"),
 ("sau","Saúde",["Hospital Mário Gatti","61 Centros de Saúde","Distritos de Saúde"],"seção 2"),
 ("ass","Assistência e educação",["CRAS","rede municipal de ensino"],"seção 2"),
 ("cul","Cultura e mobilidade",["Estação Cultura","Terminal Multimodal","EMDEC"],"seção 3"),
 ("srv","Serviços e segurança",["SANASA","Guarda Municipal"],"seção 3"),
 ("nao","Não municipais",["Cidade Judiciária","Unicamp e HC","Viracopos"],"seção 3")],
 "Na prova: separe o que é municipal do que é estadual ou federal")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As primeiras caixas trazem os próprios municipais; a última, os equipamentos que a banca usa como pegadinha.","Fontes: Edital 02/2026, Anexo I; Câmara Municipal de Campinas (SAPL); Portal da Prefeitura de Campinas; Wikipédia (verbetes Campinas, Palácio dos Jequitibás, Hospital Municipal Doutor Mário Gatti, Estação Cultura). Exemplos criados para a aula.")
revisao("geo-5","Geografia: principais próprios públicos de Campinas",b.Q,list(tx),
 cobertura=["Sedes administrativas, saúde, educação, segurança e centros de referência (recorte do edital). Educação coberta apenas de forma geral (rede municipal); faltam nomes de escolas de referência."],
 pendencias=["A maior parte das informações vem da Wikipédia; conferir no portal da Prefeitura (endereços, número de Centros de Saúde, CRAS).","O número de vereadores (33) e de Centros de Saúde (61) pode ter mudado.","Educação municipal: incluir, se a banca cobrar, os tipos de unidade (CEI, EMEF) e centros de referência.","Casos geo5a, geo5b e geo5c fictícios."],
 fontes_conferidas=["Endereço da Câmara (SAPL).","Título CRAS/DAS (portal da Prefeitura)."])
gravar("geo-5",aula_html,banco("geo-5",b.Q),tx)
