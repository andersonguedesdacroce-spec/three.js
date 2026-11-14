import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Este posto reúne tudo o que o Código diz sobre o veículo: como se classifica, que equipamentos são obrigatórios, onde e como é registrado, o licenciamento anual e as regras especiais para o transporte escolar e o moto-frete. A Vunesp cobra os arts. 96 a 139-B pela classificação dos veículos, pela lista de equipamentos obrigatórios do art. 105, pela diferença entre registro (uma vez) e licenciamento (todo ano) e pelos requisitos do transporte escolar e do moto-frete. Para o guarda, é a base da fiscalização de documentos e de equipamentos. A aula segue o texto consolidado."
S={}
S[1]="## 1. Classificação e equipamentos obrigatórios\n\n"+L("art. 96, I","Art. 96. Os veículos classificam-se em:","II - quanto à espécie:")+"\n\n"+L("art. 96, III","III - quanto à categoria:","Art. 97.")+"""

Os veículos classificam-se quanto à tração (automotor, de propulsão humana, de tração animal, reboque ou semirreboque), quanto à espécie (de passageiros, de carga, misto, de competição, de tração, especial e de coleção) e quanto à categoria (oficial, de representação diplomática, particular, de aluguel e de aprendizagem). A espécie fala do que o veículo faz, e a categoria, de quem o utiliza: um automóvel de passageiros pode ser da categoria particular, de aluguel ou de aprendizagem.

"""+L("art. 105, caput","Art. 105. São equipamentos obrigatórios","§ 1º O CONTRAN disciplinará")+"\n\n"+L("art. 105, §§ 2º e 3º","§ 2º Nenhum veículo poderá transitar","§ 4º O CONTRAN estabelecerá o prazo")+"""

Entre os equipamentos obrigatórios estão o cinto de segurança (salvo veículos de transporte de passageiros em percursos em que se pode viajar em pé), o registrador instantâneo inalterável de velocidade e tempo (para os veículos de transporte e de condução escolar, os de transporte de passageiros com mais de dez lugares e os de carga com peso bruto total superior a 4.536 kg), o encosto de cabeça, o dispositivo de controle de emissão de gases e ruído, o air bag frontal para o condutor e o passageiro do banco dianteiro e as luzes de rodagem diurna. Para as bicicletas, são obrigatórias a campainha, a sinalização noturna dianteira, traseira, lateral e nos pedais e o espelho retrovisor do lado esquerdo. Nenhum veículo pode transitar com equipamento ou acessório proibido, e fabricantes, importadores, montadores, encarroçadores e revendedores devem comercializar os veículos com os equipamentos obrigatórios.
"""
S[2]="## 2. Registro e licenciamento\n\n"+L("art. 120, caput","Art. 120. Todo veículo automotor, articulado","§ 1º Os órgãos executivos")+"\n\n"+L("art. 121","Art. 121. Registrado o veículo","Art. 122.")+"\n\n"+L("art. 130","Art. 130. Todo veículo automotor","§ 1º O disposto neste artigo")+"\n\n"+L("art. 131, caput e §§ 1º a 3º","Art. 131. O Certificado de Licenciamento Anual","§ 4º As informações")+"""

O registro é feito uma vez, perante o órgão executivo de trânsito do Estado ou do Distrito Federal, no Município de domicílio ou residência do proprietário, e dele resulta o Certificado de Registro de Veículo (CRV), em meio físico ou digital, à escolha do proprietário. Os veículos oficiais só são registrados com indicação expressa, por pintura nas portas, do nome, sigla ou logotipo do órgão em cujo nome o veículo será registrado. O licenciamento, por sua vez, é anual: todo veículo automotor deve ser licenciado anualmente pelo órgão executivo de trânsito do Estado ou do Distrito Federal onde estiver registrado, e dele resulta o Certificado de Licenciamento Anual, vinculado ao CRV.

O primeiro licenciamento é feito simultaneamente ao registro. O veículo só é considerado licenciado estando quitados os débitos de tributos, encargos e multas de trânsito e ambientais vinculados a ele, independentemente da responsabilidade pelas infrações cometidas. E, ao licenciar, o proprietário deve comprovar aprovação nas inspeções de segurança veicular e de controle de emissões de gases e ruído, conforme o art. 104. No caso de transferência de residência ou domicílio, é válido, durante o exercício, o licenciamento de origem.
"""
S[3]="## 3. Transporte escolar e moto-frete\n\n"+L("art. 136","Art. 136. Os veículos especialmente destinados","Art. 137.")+"\n\n"+L("art. 137","Art. 137. A autorização a que se refere","CAPÍTULO XIII-A")+"\n\n"+L("art. 139-A","Art. 139-A. As motocicletas e motonetas","Art. 139-B.")+"""

Os veículos de condução coletiva de escolares só circulam com autorização do órgão executivo de trânsito do Estado ou do Distrito Federal, que exige registro como veículo de passageiros, inspeção semestral, faixa horizontal amarela de quarenta centímetros de largura, à meia altura, com o dístico ESCOLAR em preto, registrador instantâneo inalterável de velocidade e tempo, lanternas de luz branca, fosca ou amarela na parte superior dianteira e vermelhas na traseira, e cintos de segurança em número igual à lotação. A autorização é afixada na parte interna do veículo, em local visível, com a lotação permitida, e é vedada a condução de escolares em número superior à capacidade do fabricante.

As motocicletas e motonetas destinadas ao transporte remunerado de mercadorias, o moto-frete, só circulam com autorização do mesmo órgão, e exige-se registro como veículo da categoria de aluguel, protetor de motor (mata-cachorro), aparador de linha (antena corta-pipas) e inspeção semestral. É proibido o transporte de combustíveis, produtos inflamáveis ou tóxicos e de galões, com exceção do gás de cozinha e de galões de água mineral, desde que com o auxílio de side-car. O art. 139-B preserva a competência municipal ou estadual de aplicar exigências próprias para o moto-frete em suas circunscrições.
"""
S[5]="""## 5. Na rotina do guarda

- **Documentos do veículo:** o agente confere o Certificado de Registro (CRV) e o Certificado de Licenciamento Anual, em meio físico ou digital.
- **Transporte escolar:** o agente verifica a autorização afixada, a faixa amarela com o dístico ESCOLAR, o cinto em número igual à lotação e a lotação máxima.
- **Moto-frete:** o agente verifica o protetor de motor e o aparador de linha, além da categoria de aluguel.
- **Equipamentos:** o veículo não pode circular com equipamento ou acessório proibido, e o agente pode autuar.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Registro e licenciamento são a mesma coisa | Registro: uma vez, CRV. Licenciamento: todo ano, Certificado de Licenciamento Anual |
| Onde se registra o veículo | No órgão executivo de trânsito do Estado ou do DF, no Município de domicílio do proprietário |
| Espécie e categoria | Espécie: passageiros, carga, misto etc. Categoria: oficial, particular, de aluguel etc. |
| Equipamento obrigatório da bicicleta | Campainha, sinalização noturna e espelho retrovisor do lado esquerdo |
| Faixa do veículo escolar | Amarela, 40 cm de largura, à meia altura, com dístico ESCOLAR em preto |
| Inspeção do escolar e do moto-frete | Semestral |
| Moto-frete | Categoria de aluguel, mata-cachorro e corta-pipas |
| Licenciamento com débitos | Só é considerado licenciado se quitados tributos, encargos e multas |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Tração | Automotor, propulsão humana, tração animal, reboque |
| Espécie | Passageiros, carga, misto, competição, tração, especial, coleção |
| Categoria | Oficial, diplomática, particular, aluguel, aprendizagem |
| Equipamentos | Cinto, registrador (casos do inciso II), encosto de cabeça, air bag, luzes diurnas |
| Registro | Uma vez; órgão estadual; CRV |
| Licenciamento | Anual; débitos quitados; inspeções |
| Escolar | Autorização; faixa amarela; inspeção semestral; cintos pela lotação |
| Moto-frete | Aluguel; mata-cachorro; corta-pipas; inspeção semestral |
"""
QR=[("Questão 1","O licenciamento do veículo automotor deve ser feito",["anualmente, pelo órgão executivo de trânsito do Estado ou do DF onde estiver registrado.","uma única vez, na compra.","a cada cinco anos.","a cada dois anos, apenas.","apenas na transferência."],0,"Art. 130, caput."),
("Questão 2","O veículo só será considerado licenciado estando quitados os débitos relativos a",["tributos, encargos e multas de trânsito e ambientais vinculados ao veículo.","apenas multas de trânsito.","apenas tributos.","apenas IPVA.","apenas seguro obrigatório."],2,"Art. 131, § 2º."),
("Questão 3","Os veículos de condução coletiva de escolares devem passar por inspeção",["semestral.","anual.","mensal.","bienal.","trimestral."],1,"Art. 136, II."),
("Questão 4","A faixa horizontal dos veículos de condução de escolares é de cor",["amarela, com quarenta centímetros de largura, com o dístico ESCOLAR em preto.","branca, com 20 cm.","vermelha, com 40 cm.","azul, com 30 cm.","verde, com 10 cm."],4,"Art. 136, III.")]
t1="<strong>Van escolar em fiscalização</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, abordou uma van que transportava escolares. A van tinha 15 lugares e levava 20 crianças, não tinha faixa amarela nem o dístico ESCOLAR e a autorização não estava afixada."
t2="<strong>Entregador de moto</strong><br><br>Um entregador de aplicativo, que presta serviço de moto-frete em Vila Nova, circulava com uma motocicleta registrada como categoria particular, sem protetor de motor, transportando um galão de combustível."
tx={"ctb5a":t1,"ctb5b":t2}
# n=1
q(1,"Quanto à tração, os veículos classificam-se em automotor, de propulsão humana, de tração animal e",["reboque ou semirreboque.","de competição.","especial.","de aluguel.","oficial."],"Art. 96, I.")
q(1,"Quanto à espécie, os veículos de passageiros incluem, entre outros,",["bicicleta, automóvel e ônibus.","caminhão e caminhonete.","trator.","carroça.","carro de mão."],"Art. 96, II, a.")
q(1,"Quanto à categoria, os veículos classificam-se em oficial, de representação diplomática, particular, de aluguel e",["de aprendizagem.","de carga.","de passageiros.","de competição.","de tração."],"Art. 96, III.")
q(1,"As características dos veículos, suas especificações básicas e condições essenciais para registro, licenciamento e circulação serão estabelecidas pelo",["Contran.","Cetran.","Município.","Polícia Militar.","Ministério Público."],"Art. 97.")
q(1,"Entre os equipamentos obrigatórios dos veículos está o",["cinto de segurança, conforme regulamentação específica do Contran.","rádio.","ar-condicionado.","som.","porta-copos."],"Art. 105, I.")
q(1,"É equipamento obrigatório de todos os tipos de veículos automotores, segundo normas do Contran, o",["encosto de cabeça.","ar-condicionado.","câmbio automático.","direção hidráulica.","vidro elétrico."],"Art. 105, III.")
q(1,"Para as bicicletas, são equipamentos obrigatórios a campainha, a sinalização noturna dianteira, traseira, lateral e nos pedais, e o",["espelho retrovisor do lado esquerdo.","espelho dos dois lados.","buzina.","farol dianteiro apenas.","cinto."],"Art. 105, VI.")
q(1,"É equipamento obrigatório o equipamento suplementar de retenção, ou",["air bag frontal para o condutor e o passageiro do banco dianteiro.","air bag lateral.","air bag traseiro.","air bag de joelho.","air bag de teto."],"Art. 105, VII.")
q(1,"Nenhum veículo poderá transitar com equipamento ou acessório",["proibido.","novo.","importado.","nacional.","de série."],"Art. 105, § 2º.")
q(1,"Todo veículo automotor, articulado, reboque ou semirreboque deve ser registrado perante o órgão executivo de trânsito do",["Estado ou do Distrito Federal.","Município.","Governo federal, apenas.","Ministério Público.","Contran."],"Art. 120, caput.")
q(1,"O registro do veículo é feito no Município de",["domicílio ou residência de seu proprietário.","fabricação.","compra.","sede do banco.","sede da seguradora."],"Art. 120, caput.")
q(1,"Registrado o veículo, expedir-se-á o",["Certificado de Registro de Veículo (CRV).","Certificado de Habilitação.","alvará de circulação.","seguro obrigatório.","comprovante de multa."],"Art. 121.")
q(1,"Todo veículo automotor, para transitar na via, deverá ser licenciado",["anualmente.","apenas uma vez.","a cada dois anos.","a cada cinco anos.","a cada dez anos."],"Art. 130, caput.")
q(1,"O Certificado de Licenciamento Anual será expedido ao veículo licenciado, vinculado ao",["Certificado de Registro de Veículo.","Certificado de Habilitação.","seguro obrigatório.","comprovante de residência.","alvará municipal."],"Art. 131, caput.")
q(1,"No caso de transferência de residência ou de domicílio, é válido, durante o exercício, o licenciamento de",["origem.","destino.","qualquer um.","nenhum.","outro Estado."],"Art. 130, § 2º.")
q(1,"Os veículos de condução coletiva de escolares só podem circular com autorização emitida pelo órgão executivo de trânsito do",["Estado ou do Distrito Federal.","Município.","Contran.","Ministério da Educação.","Polícia Militar."],"Art. 136, caput.")
q(1,"No veículo escolar, o equipamento registrador instantâneo inalterável de velocidade e tempo é",["exigido.","dispensável.","facultativo.","vedado.","opcional."],"Art. 136, IV.")
q(1,"As motocicletas e motonetas do moto-frete só podem circular nas vias com autorização emitida pelo órgão executivo de trânsito do",["Estado ou do Distrito Federal.","Município, apenas.","Contran.","Ministério dos Transportes.","Cetran."],"Art. 139-A.")
q(1,"No texto da van escolar, a van exibia 20 crianças em 15 lugares. O art. 137 veda a condução de escolares em número superior à capacidade estabelecida pelo",["fabricante.","condutor.","dono da escola.","Município.","prefeito."],"Art. 137.","ctb5a")
q(1,"No texto do entregador de moto, a motocicleta de moto-frete deve ser registrada como veículo da categoria",["de aluguel.","particular.","oficial.","de aprendizagem.","diplomática."],"Art. 139-A, I.","ctb5b")
# n=2
q(2,"Os veículos oficiais de propriedade da administração direta só são registrados com indicação expressa, por pintura nas portas, do",["nome, sigla ou logotipo do órgão ou entidade em cujo nome o veículo será registrado.","nome do motorista.","número da placa.","preço.","ano de fabricação."],"Art. 120, § 1º.")
q(2,"O Certificado de Registro de Veículo pode ser expedido em meio físico e",["digital, à escolha do proprietário.","apenas físico.","apenas digital.","apenas por correio.","apenas presencial."],"Art. 121.")
q(2,"Para a expedição do CRV, o órgão executivo de trânsito consultará o cadastro do",["RENAVAM.","RENACH.","CPF.","CNPJ.","SPVAT."],"Art. 122.")
q(2,"Para a expedição do CRV, exige-se a nota fiscal fornecida pelo fabricante ou revendedor, ou documento",["equivalente expedido por autoridade competente.","particular.","verbal.","provisório.","de compra de peças."],"Art. 122, I.")
q(2,"O veículo somente será considerado licenciado estando quitados os débitos relativos a tributos, encargos e multas de trânsito e",["ambientais, vinculados ao veículo.","de outros veículos do proprietário.","trabalhistas.","de IPTU.","de seguro."],"Art. 131, § 2º.")
q(2,"Ao licenciar o veículo, o proprietário deverá comprovar aprovação nas inspeções de segurança veicular e de controle de emissões de gases poluentes e de ruído, conforme o art.",["104.","96.","105.","120.","136."],"Art. 131, § 3º.")
q(2,"O disposto sobre licenciamento anual não se aplica a veículo de",["uso bélico.","uso particular.","aluguel.","aprendizagem.","carga."],"Art. 130, § 1º.")
q(2,"O equipamento registrador instantâneo inalterável de velocidade e tempo é obrigatório nos veículos de carga com peso bruto total superior a",["quatro mil, quinhentos e trinta e seis quilogramas.","mil quilogramas.","dois mil quilogramas.","dez mil quilogramas.","vinte mil quilogramas."],"Art. 105, II.")
q(2,"Fabricantes, importadores, montadores, encarroçadores e revendedores devem comercializar os veículos com os equipamentos",["obrigatórios definidos no art. 105 e com os demais estabelecidos pelo Contran.","opcionais.","de luxo.","de série.","de competição."],"Art. 105, § 3º.")
q(2,"O veículo escolar precisa de registro como veículo de",["passageiros.","carga.","aluguel.","aprendizagem.","competição."],"Art. 136, I.")
q(2,"No veículo escolar, os cintos de segurança devem estar em número igual à",["lotação.","metade da lotação.","dobro da lotação.","terça parte da lotação.","capacidade do tanque."],"Art. 136, VI.")
q(2,"A autorização do veículo escolar deverá ser afixada",["na parte interna do veículo, em local visível, com inscrição da lotação permitida.","na parte externa.","na escola.","no órgão de trânsito.","na casa do condutor."],"Art. 137.")
q(2,"No moto-frete, exige-se a instalação de protetor de motor, chamado de",["mata-cachorro.","corta-pipas.","para-lama.","side-car.","aparador."],"Art. 139-A, II.")
q(2,"No moto-frete, o aparador de linha é chamado de",["antena corta-pipas.","mata-cachorro.","para-choque.","side-car.","protetor de motor."],"Art. 139-A, III.")
q(2,"No moto-frete, é proibido o transporte de combustíveis, produtos inflamáveis ou tóxicos e de galões, com exceção do gás de cozinha e de galões de água mineral, desde que com o auxílio de",["side-car.","bagageiro comum.","mochila.","carretinha.","caixa térmica."],"Art. 139-A, § 2º.")
q(2,"A competência municipal ou estadual de aplicar exigências próprias para o moto-frete é preservada pelo art.",["139-B.","139-A.","136.","137.","120."],"Art. 139-B.")
q(2,"No texto da van escolar, a falta da faixa amarela com o dístico ESCOLAR viola a exigência do",["inciso III do art. 136.","inciso I do art. 136.","art. 105.","art. 130.","art. 131."],"Art. 136, III.","ctb5a")
q(2,"No texto do entregador de moto, a ausência de protetor de motor viola o",["inciso II do art. 139-A.","inciso I do art. 139-A.","art. 136.","art. 130.","art. 105."],"Art. 139-A, II.","ctb5b")
q(2,"No texto do entregador de moto, o transporte de galão de combustível é",["proibido, pois só se admite gás de cozinha e galões de água mineral, com side-car.","permitido.","facultativo.","obrigatório.","regulamentado pelo Contran apenas."],"Art. 139-A, § 2º.","ctb5b")
q(2,"O primeiro licenciamento é feito simultaneamente ao registro, e o Certificado de Licenciamento Anual será expedido ao veículo licenciado, vinculado ao",["CRV.","CNH.","alvará municipal.","seguro obrigatório.","comprovante de multa."],"Art. 131, caput e § 1º.")
# n=3
q(3,"Assinale a alternativa que associa corretamente o conceito à classificação.",["Espécie: de passageiros, de carga, misto; categoria: oficial, particular, de aluguel; tração: automotor, propulsão humana.","Espécie: oficial; categoria: de carga.","Tração: particular; espécie: automotor.","Categoria: de competição; espécie: aluguel.","Espécie: aprendizagem; categoria: misto."],"Art. 96.")
q(3,"Considere as afirmações. I. O registro do veículo é feito uma vez. II. O licenciamento é anual. III. O licenciamento dispensa a quitação de multas. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"O licenciamento exige a quitação de tributos, encargos e multas (art. 131, § 2º).")
q(3,"Assinale a INCORRETA.",["O veículo escolar dispensa a inspeção semestral.","O veículo escolar tem faixa amarela com o dístico ESCOLAR.","O moto-frete exige inspeção semestral.","O registro é feito no órgão estadual de trânsito.","O CRV é o certificado do registro."],"A inspeção semestral é exigida do escolar (art. 136, II).")
q(3,"O registro é diferente do licenciamento porque o registro identifica o veículo e o proprietário e o licenciamento, a cada ano, atesta",["a regularidade do veículo para circular, com débitos quitados e inspeções aprovadas.","o preço do veículo.","a quilometragem.","o seguro de vida.","o consumo."],"Arts. 121 e 131.")
q(3,"O moto-frete exige, entre outros requisitos, registro como veículo de aluguel e inspeção",["semestral.","anual.","mensal.","bienal.","trimestral."],"Art. 139-A, I e IV.")
q(3,"Assinale a alternativa que traz apenas requisitos do veículo escolar previstos no art. 136.",["Inspeção semestral, faixa amarela com dístico ESCOLAR, registrador de velocidade e tempo e cintos em número igual à lotação.","Faixa vermelha, inspeção anual e cinto para o motorista.","Faixa azul, sem cinto.","Faixa amarela, sem inspeção.","Faixa verde e inspeção semestral."],"Art. 136.")
q(3,"A inspeção de segurança veicular e de controle de emissões de gases poluentes e de ruído é comprovada, ao licenciar, nos termos do",["art. 104.","art. 105.","art. 120.","art. 130.","art. 136."],"Art. 131, § 3º.")
q(3,"As informações sobre campanhas de chamamento para substituição ou reparo de veículos não atendidas no prazo de um ano deverão constar do",["Certificado de Licenciamento Anual.","CRV.","CNH.","alvará.","seguro."],"Art. 131, § 4º.")
q(3,"Após a inclusão das informações sobre campanhas de chamamento no Certificado de Licenciamento Anual, o veículo somente será licenciado mediante",["comprovação do atendimento às campanhas de chamamento.","pagamento em dobro.","novo registro.","nova placa.","inspeção em outro Estado."],"Art. 131, § 5º.")
q(3,"O Contran poderá, excepcionalmente, prorrogar a exigência do § 5º diante da comprovada falta de peças ou da necessidade de",["escalonamento para o atendimento ao chamamento, avaliadas as questões de segurança viária.","redução de multas.","isenção de IPVA.","pedido do proprietário.","pedido do fabricante."],"Art. 131, § 7º.")
q(3,"A regra de que o veículo oficial seja identificado, por pintura nas portas, aplica-se aos veículos de propriedade da administração direta da União, dos Estados, do DF e dos Municípios, excetuando-se os veículos de representação e os previstos no",["art. 116.","art. 96.","art. 105.","art. 130.","art. 136."],"Art. 120, § 1º.")
q(3,"O art. 120 não se aplica ao",["veículo de uso bélico.","veículo particular.","veículo de aluguel.","veículo oficial.","veículo escolar."],"Art. 120, § 2º.")
q(3,"No veículo escolar, as lanternas de luz branca, fosca ou amarela, ficam nas extremidades da parte superior dianteira, e as de luz vermelha, na",["extremidade superior da parte traseira.","parte lateral.","parte inferior.","parte do capô.","porta."],"Art. 136, V.")
q(3,"A faixa horizontal do veículo escolar tem a cor amarela, com quarenta centímetros de largura, à meia altura, em toda a extensão das partes laterais e traseira da carroçaria. Se a carroçaria é amarela,",["as cores devem ser invertidas.","a faixa é dispensada.","a faixa é vermelha.","a faixa é azul.","a faixa é branca."],"Art. 136, III.")
q(3,"Assinale a alternativa correta sobre o moto-frete.",["Exige registro como veículo da categoria de aluguel, protetor de motor, aparador de linha e inspeção semestral.","Exige registro como particular.","Dispensa a inspeção.","Permite transportar combustíveis.","Dispensa autorização."],"Art. 139-A.")
q(3,"Assinale a alternativa correta sobre o transporte de escolares.",["É vedada a condução de escolares em número superior à capacidade estabelecida pelo fabricante.","A lotação é livre.","A autorização é dispensável.","O cinto é facultativo.","A faixa pode ser de qualquer cor."],"Art. 137.")
q(3,"A diferença entre espécie e categoria é que a espécie se refere à destinação do veículo (passageiros, carga, misto) e a categoria,",["a quem o utiliza (oficial, particular, de aluguel).","à potência.","ao ano de fabricação.","à cor.","ao tamanho."],"Art. 96, II e III.")
q(3,"No texto da van escolar, a quantidade de crianças acima da lotação e sem autorização afixada importa descumprimento do",["art. 137.","art. 130.","art. 120.","art. 105.","art. 96."],"Art. 137.","ctb5a")
q(3,"No texto da van escolar, o dístico ESCOLAR deve ser em",["preto, sobre a faixa amarela.","branco.","vermelho.","azul.","verde."],"Art. 136, III.","ctb5a")
q(3,"No texto do entregador de moto, a moto registrada como categoria particular descumpre a exigência de registro como veículo de",["aluguel.","passageiros.","competição.","coleção.","tração."],"Art. 139-A, I.","ctb5b")
assert len(Q)==60,len(Q)
code,svg=mapa("Veículos, registro e licenciamento",[
 ("clas","Classificação",["tração","espécie","categoria"],"seção 1"),
 ("equip","Equipamentos",["cinto e encosto de cabeça","air bag e luzes diurnas","bicicleta: campainha, espelho"],"seção 1"),
 ("reg","Registro",["uma vez","órgão estadual","CRV"],"seção 2"),
 ("lic","Licenciamento",["anual","débitos quitados","inspeções"],"seção 2"),
 ("esc","Escolar",["autorização","faixa amarela, ESCOLAR","inspeção semestral"],"seção 3"),
 ("moto","Moto-frete",["categoria de aluguel","mata-cachorro e corta-pipas","inspeção semestral"],"seção 3")],
 "Na prova: registro é uma vez (CRV); licenciamento é todo ano")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As duas primeiras caixas tratam do veículo em geral; as demais, de duas atividades com regras especiais.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 96 a 139-B, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-5","Veículos, registro e licenciamento (CTB, arts. 96 a 139-B)",Q,list(tx),
 cobertura=["Recorte do edital: classificação, equipamentos e documentação. Cobertos: arts. 96, 97, 105, 120 a 122, 130, 131, 136, 137, 139-A e 139-B. Não detalhados: arts. 98 a 104, 106 a 119 e 123 a 129, 132 a 135."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","Equipamentos obrigatórios detalhados em resoluções do Contran não foram consultados.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb5a e ctb5b fictícios."],
 fontes_conferidas=["CTB, arts. 96 a 139-B: texto da Câmara, copiado por programa."])
gravar("ctb-5",aula_html,banco("ctb-5",Q),tx)
