import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='mp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Este é o posto da Lei Maria da Penha mais próximo do trabalho do guarda: política pública, assistência à mulher, atendimento pela autoridade policial e, no art. 12-C, o afastamento imediato do agressor do lar. O art. 8º, VII, manda capacitar a Guarda Municipal. A Vunesp cobra as diretrizes do art. 8º, as providências do art. 11, os procedimentos do art. 12 (prazo de 48 horas) e as autoridades que podem afastar o agressor (juiz, delegado e policial), com comunicação ao juiz em 24 horas."
S={}
S[1]="## 1. Política pública de prevenção\n\n"+L("art. 8º","Art. 8º A política pública","CAPÍTULO II")+"""

A política pública é um conjunto articulado de ações da União, dos Estados, do Distrito Federal e dos Municípios e de ações não governamentais. As diretrizes incluem a integração do Judiciário, do Ministério Público e da Defensoria com segurança pública, assistência social, saúde, educação, trabalho e habitação; estudos e estatísticas com perspectiva de gênero e raça; o respeito nos meios de comunicação; o atendimento policial especializado, em particular nas Delegacias de Atendimento à Mulher; campanhas educativas; convênios; a capacitação permanente das Polícias Civil e Militar, da Guarda Municipal, do Corpo de Bombeiros e dos profissionais dessas áreas; programas educacionais; e o destaque nos currículos escolares dos conteúdos sobre direitos humanos, equidade de gênero e violência doméstica.
"""
S[2]="## 2. Assistência à mulher\n\n"+L("art. 9º, caput a § 3º","Art. 9º A assistência","§ 4º Aquele que")+"\n\n"+L("art. 9º, §§ 4º a 8º","§ 4º Aquele que","CAPÍTULO III")+"""

A assistência é prestada em caráter prioritário no SUS e no Susp, de forma articulada e emergencialmente, quando for o caso. O juiz determina, por prazo certo, a inclusão da mulher no cadastro de programas assistenciais e assegura, para preservar a integridade física e psicológica, o acesso prioritário à remoção (servidora pública), a manutenção do vínculo trabalhista por até seis meses, quando necessário o afastamento do local de trabalho, e o encaminhamento à assistência judiciária. A assistência inclui contracepção de emergência e profilaxia de infecções sexualmente transmissíveis.

Quem causar lesão, violência ou dano à mulher fica obrigado a ressarcir os danos, inclusive os custos do SUS; o agressor ressarce os dispositivos de segurança para monitoramento das vítimas, sem ônus ao patrimônio da mulher. A mulher tem prioridade para matricular os dependentes em escola mais próxima do domicílio, e os dados são sigilosos.
"""
S[3]="## 3. Atendimento pela autoridade policial\n\n"+L("art. 10","Art. 10. Na hipótese da iminência","Art. 10-A.")+"\n\n"+L("art. 10-A, caput e § 1º","Art. 10-A. É direito da mulher","§ 2º Na inquirição")+"\n\n"+L("art. 11","Art. 11. No atendimento à mulher","Art. 12.")+"\n\n"+L("art. 12, caput","Art. 12. Em todos os casos","§ 1º O pedido da ofendida")+"\n\n"+L("art. 12-C","Art. 12-C. Verificada a existência","Art. 12-D.")+"""

Na iminência ou prática de violência doméstica, a autoridade policial que toma conhecimento adota de imediato as providências legais, inclusive no descumprimento de medida protetiva deferida. A mulher tem direito a atendimento policial e pericial especializado, ininterrupto, prestado por servidores preferencialmente do sexo feminino, previamente capacitados; a inquirição preserva a integridade da depoente, evita o contato com o agressor e a revitimização.

No atendimento, a autoridade garante proteção policial e comunica ao Ministério Público e ao Judiciário, encaminha ao hospital e ao IML, fornece transporte para abrigo ou local seguro quando houver risco de vida, acompanha a retirada de pertences e informa os direitos. O registro leva a procedimentos imediatos: ouvir a ofendida, lavrar o boletim e tomar a representação; colher provas; remeter ao juiz, em 48 horas, o pedido de medidas protetivas; determinar exame de corpo de delito; ouvir agressor e testemunhas; e juntar antecedentes e informação sobre arma de fogo.

Havendo risco atual ou iminente à vida ou à integridade, o agressor é imediatamente afastado do lar pela autoridade judicial, pelo delegado (se o Município não for sede de comarca) ou pelo policial (se não for sede de comarca e não houver delegado disponível). Nos dois últimos casos, o juiz é comunicado em até 24 horas e decide em igual prazo sobre a manutenção ou revogação. Havendo risco, não se concede liberdade provisória ao preso.
"""
S[5]="""## 5. Na rotina do guarda

- **Chegada ao local:** protege a mulher, comunica de imediato o Ministério Público e o Judiciário quando necessário e encaminha à delegacia.
- **Transporte:** a autoridade policial fornece transporte para abrigo ou local seguro, quando houver risco de vida.
- **Pertences:** acompanha a retirada dos pertences da mulher, quando necessário.
- **Afastamento do agressor:** o policial pode afastar o agressor do lar se o Município não for sede de comarca e não houver delegado disponível; o juiz é comunicado em até 24 horas.
- **Descumprimento de medida protetiva:** exige providências imediatas da autoridade policial.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Quem integra a política pública | União, Estados, DF, Municípios e ações não governamentais |
| Capacitação | Polícias Civil e Militar, Guarda Municipal, Bombeiros (art. 8º, VII) |
| Assistência prioritária | SUS e Susp |
| Vínculo trabalhista | Manutenção por até seis meses |
| Ressarcimento | Agressor ressarce o SUS e os dispositivos de segurança |
| Atendimento policial especializado | Ininterrupto; preferencialmente servidoras |
| Pedido de medidas protetivas | Remessa ao juiz em 48 horas |
| Afastamento do agressor | Juiz; delegado (município sem comarca); policial (sem comarca e sem delegado) |
| Comunicação ao juiz | Até 24 horas; decisão em igual prazo |
| Liberdade provisória | Não, havendo risco |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 8º | Política articulada; capacitação da Guarda Municipal |
| Art. 9º | Assistência prioritária no SUS e no Susp; vínculo por até 6 meses |
| Art. 10 | Providências imediatas |
| Art. 10-A | Atendimento especializado e não revitimização |
| Art. 11 | Proteção, hospital, IML, transporte, pertences, informação |
| Art. 12 | Boletim, provas, 48 horas, corpo de delito, antecedentes |
| Art. 12-C | Afastamento imediato; comunicação em 24 horas |
| Liberdade provisória | Vedada se há risco |
"""
QR=[("Questão 1","Em todos os casos de violência doméstica, a autoridade policial remeterá ao juiz, no prazo de 48 horas, expediente apartado com o pedido da ofendida para a concessão de",["medidas protetivas de urgência.","separação judicial.","pensão alimentícia.","guarda dos filhos.","tutela."],0,"Art. 12, III."),
("Questão 2","Verificado o risco, o agressor será imediatamente afastado do lar pela autoridade judicial, pelo delegado de polícia, quando o Município não for sede de comarca, ou pelo",["policial, quando o Município não for sede de comarca e não houver delegado disponível.","prefeito.","vereador.","síndico.","advogado."],1,"Art. 12-C, III."),
("Questão 3","Nas hipóteses de afastamento pelo delegado ou pelo policial, o juiz será comunicado no prazo máximo de",["vinte e quatro horas.","quarenta e oito horas.","dez dias.","cinco dias.","trinta dias."],2,"Art. 12-C, § 1º."),
("Questão 4","No atendimento à mulher em situação de violência, a autoridade policial deverá fornecer transporte para a ofendida e seus dependentes para abrigo ou local seguro, quando houver risco de",["vida.","greve.","chuva.","atraso.","falta de vaga."],3,"Art. 11, III.")]
t1="<strong>Chamado na madrugada</strong><br><br>Numa cidade fictícia sem sede de comarca, uma equipe da guarda de Vila Nova atendeu uma mulher com hematomas, que relatava ameaças de morte do marido, ainda no local. Não havia delegado disponível."
t2="<strong>Retirada de pertences</strong><br><br>Uma mulher de Vila Nova pediu que a guarda a acompanhasse até a casa para pegar seus documentos e roupas, pois o companheiro ainda estava lá."
t3="<strong>Pedido de medidas</strong><br><br>Na delegacia de Vila Nova, a ofendida registrou a ocorrência e pediu medidas protetivas de urgência."
tx={"mp2a":t1,"mp2b":t2,"mp2c":t3}
# n=1
q(1,"A política pública que visa coibir a violência doméstica far-se-á por meio de um conjunto articulado de ações da União, dos Estados, do Distrito Federal, dos Municípios e de ações",["não governamentais.","privadas apenas.","partidárias.","religiosas.","militares."],"Art. 8º.")
q(1,"Entre as diretrizes está a implementação de atendimento policial especializado para as mulheres, em particular nas Delegacias de Atendimento à",["Mulher.","Criança.","Família.","Comunidade.","Pessoa Idosa."],"Art. 8º, IV.")
q(1,"A capacitação permanente prevista no art. 8º, VII, inclui as Polícias Civil e Militar, o Corpo de Bombeiros e a",["Guarda Municipal.","Guarda Portuária.","Marinha.","Aeronáutica.","Receita."],"Art. 8º, VII.")
q(1,"A assistência à mulher em situação de violência será prestada em caráter prioritário no SUS e no",["Susp.","INSS.","Detran.","SUAS apenas.","BNDES."],"Art. 9º.")
q(1,"A manutenção do vínculo trabalhista, quando necessário o afastamento do local de trabalho, é de até",["seis meses.","um mês.","três meses.","um ano.","dois anos."],"Art. 9º, § 2º, II.")
q(1,"A mulher tem prioridade para matricular seus dependentes em instituição de educação básica mais próxima de seu",["domicílio.","trabalho.","parente.","consultório.","clube."],"Art. 9º, § 7º.")
q(1,"Serão sigilosos os dados da ofendida e de seus dependentes matriculados ou transferidos, e o acesso às informações será reservado ao juiz, ao Ministério Público e aos órgãos",["competentes do poder público.","da imprensa.","do agressor.","da escola.","do bairro."],"Art. 9º, § 8º.")
q(1,"Na hipótese de iminência ou prática de violência, a autoridade policial adotará, de imediato, as providências legais",["cabíveis.","facultativas.","eventuais.","futuras.","sugeridas."],"Art. 10.")
q(1,"O art. 10 aplica-se também ao descumprimento de medida protetiva de",["urgência deferida.","guarda.","pensão.","visita.","tutela."],"Art. 10, parágrafo único.")
q(1,"É direito da mulher o atendimento policial e pericial especializado, ininterrupto e prestado por servidores preferencialmente do sexo",["feminino, previamente capacitados.","masculino.","neutro.","indiferente.","sorteado."],"Art. 10-A.")
q(1,"No atendimento, a autoridade policial deve encaminhar a ofendida ao hospital ou posto de saúde e ao Instituto",["Médico Legal.","de Identificação.","de Previdência.","de Educação.","Geográfico."],"Art. 11, II.")
q(1,"A autoridade policial deve informar à ofendida os direitos a ela conferidos na lei e os serviços",["disponíveis.","pagos.","privados.","eventuais.","futuros."],"Art. 11, V.")
q(1,"Em todos os casos, feito o registro, a autoridade deve ouvir a ofendida, lavrar o boletim de ocorrência e tomar a representação a termo, se",["apresentada.","negada.","recusada.","omitida.","adiada."],"Art. 12, I.")
q(1,"Cabe à autoridade policial determinar o exame de corpo de delito da",["ofendida.","testemunha.","autoridade.","vizinha.","filha do agressor."],"Art. 12, IV.")
q(1,"O pedido de medidas protetivas é remetido ao juiz no prazo de",["quarenta e oito horas.","vinte e quatro horas.","dez dias.","cinco dias.","trinta dias."],"Art. 12, III.")
q(1,"Verificado o risco à vida, o agressor será imediatamente afastado do lar, domicílio ou local de convivência com a",["ofendida.","testemunha.","autoridade.","vizinhança.","empresa."],"Art. 12-C.")
q(1,"O afastamento imediato do agressor pode ser decretado, em primeiro lugar, pela autoridade",["judicial.","policial.","administrativa.","militar.","sanitária."],"Art. 12-C, I.")
q(1,"No texto do chamado na madrugada, o policial poderia afastar o agressor porque o Município não era sede de comarca e não havia",["delegado disponível.","vítima.","testemunha.","carro.","viatura."],"Art. 12-C, III.","mp2a")
q(1,"No texto da retirada de pertences, a autoridade policial acompanha a ofendida para assegurar a retirada de seus",["pertences do local da ocorrência ou do domicílio.","filhos.","bens do agressor.","carros.","terrenos."],"Art. 11, IV.","mp2b")
q(1,"No texto do pedido de medidas, o pedido da ofendida é remetido ao juiz em até",["quarenta e oito horas.","vinte e quatro horas.","cinco dias.","dez dias.","trinta dias."],"Art. 12, III.","mp2c")
# n=2
q(2,"Entre as diretrizes da política pública está a integração operacional do Judiciário, do Ministério Público e da Defensoria Pública com as áreas de segurança pública, assistência social, saúde, educação, trabalho e",["habitação.","turismo.","esporte.","agricultura.","indústria."],"Art. 8º, I.")
q(2,"A política pública inclui a promoção de campanhas educativas de prevenção voltadas ao público escolar e à",["sociedade em geral.","imprensa apenas.","polícia apenas.","família apenas.","empresa apenas."],"Art. 8º, V.")
q(2,"O art. 8º, IX, prevê o destaque, nos currículos escolares, de conteúdos relativos aos direitos humanos, à equidade de gênero e de raça ou etnia e ao problema da violência doméstica e",["familiar contra a mulher.","urbana.","rural.","esportiva.","política."],"Art. 8º, IX.")
q(2,"O juiz determinará, por prazo certo, a inclusão da mulher no cadastro de programas",["assistenciais do governo federal, estadual e municipal.","esportivos.","comerciais.","políticos.","religiosos."],"Art. 9º, § 1º.")
q(2,"A assistência à mulher inclui contracepção de emergência e profilaxia de doenças",["sexualmente transmissíveis.","respiratórias.","cardíacas.","dermatológicas.","ortopédicas."],"Art. 9º, § 3º.")
q(2,"O agressor fica obrigado a ressarcir os danos causados, inclusive ao",["Sistema Único de Saúde.","Banco Central.","Detran.","Tribunal.","Município."],"Art. 9º, § 4º.")
q(2,"Os dispositivos de segurança para monitoramento das vítimas terão seus custos ressarcidos pelo",["agressor.","Estado.","Município.","União.","juiz."],"Art. 9º, § 5º.")
q(2,"O ressarcimento não poderá importar ônus ao patrimônio da mulher e dos seus",["dependentes.","amigos.","vizinhos.","empregados.","colegas."],"Art. 9º, § 6º.")
q(2,"A inquirição da mulher deve garantir que, em nenhuma hipótese, ela tenha contato direto com",["investigados ou suspeitos.","advogados.","médicos.","juízes.","familiares dela."],"Art. 10-A, § 1º, II.")
q(2,"A não revitimização exige evitar sucessivas inquirições sobre o mesmo fato nos âmbitos criminal, cível e",["administrativo.","militar.","eleitoral.","tributário.","esportivo."],"Art. 10-A, § 1º, III.")
q(2,"A autoridade policial deve garantir proteção policial, quando necessário, comunicando de imediato ao Ministério Público e ao Poder",["Judiciário.","Legislativo.","Executivo municipal.","Eleitoral.","Militar."],"Art. 11, I.")
q(2,"Verificados indícios de condição análoga à de escravo da trabalhadora doméstica, a autoridade comunica em até quarenta e oito horas à unidade regional do Ministério do Trabalho e Emprego e ao",["Ministério Público do Trabalho.","Detran.","Conselho Tutelar.","Corpo de Bombeiros.","Procon."],"Art. 11, parágrafo único.")
q(2,"A autoridade policial deve verificar se o agressor possui registro de porte ou posse de",["arma de fogo.","veículo.","imóvel.","empresa.","conta bancária."],"Art. 12, VI-A.")
q(2,"A autoridade pode requisitar os serviços públicos necessários à defesa da mulher e de seus",["dependentes.","amigos.","vizinhos.","empregados.","clientes."],"Art. 12-B, § 3º.")
q(2,"Nos casos de risco à integridade física da ofendida ou à efetividade da medida protetiva, não será concedida liberdade provisória ao",["preso.","juiz.","delegado.","policial.","vizinho."],"Art. 12-C, § 2º.")
q(2,"No texto do chamado na madrugada, após afastar o agressor, o juiz deve ser comunicado em até",["vinte e quatro horas.","quarenta e oito horas.","cinco dias.","dez dias.","trinta dias."],"Art. 12-C, § 1º.","mp2a")
q(2,"No texto da retirada de pertences, a atuação da autoridade está prevista no art.",["11.","8º.","9º.","12-A.","12-D."],"Art. 11, IV.","mp2b")
q(2,"No texto do pedido de medidas, o pedido da ofendida é tomado a termo e deve conter, entre outros dados, a qualificação da ofendida e do",["agressor.","juiz.","delegado.","vizinho.","advogado."],"Art. 12, § 1º, I.","mp2c")
q(2,"A mulher em situação de violência tem direito a atendimento policial e pericial que seja, nos termos do art. 10-A,",["ininterrupto.","apenas diurno.","apenas em dias úteis.","apenas por escrito.","apenas por telefone."],"Art. 10-A.")
q(2,"O art. 12-A dá prioridade à criação de Delegacias Especializadas de Atendimento à Mulher no âmbito da Polícia",["Civil.","Militar.","Federal.","Rodoviária.","Penal."],"Art. 12-A.")
# n=3
q(3,"Assinale a alternativa correta sobre prazos da Lei Maria da Penha nos arts. 8º a 12-C.",["Pedido de medidas protetivas ao juiz: 48 horas; comunicação ao juiz do afastamento: 24 horas; vínculo trabalhista: até seis meses.","Pedido ao juiz: 24 horas; afastamento: 48 horas.","Vínculo trabalhista: um ano.","Comunicação do afastamento: 10 dias.","Pedido: 5 dias."],"Arts. 9º, 12 e 12-C.")
q(3,"Considere. I. O policial pode afastar o agressor se o Município não for sede de comarca e não houver delegado. II. O juiz é comunicado em 48 horas. III. Não se concede liberdade provisória se há risco. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A comunicação ao juiz é em 24 horas (art. 12-C, § 1º).")
q(3,"Assinale a INCORRETA.",["O delegado pode afastar o agressor mesmo se o Município for sede de comarca.","O juiz pode afastar o agressor.","O policial pode afastar se não houver delegado e o Município não for sede de comarca.","O juiz decide em 24 horas sobre a manutenção da medida.","Não há liberdade provisória em risco."],"O delegado afasta quando o Município não for sede de comarca (art. 12-C, II).")
q(3,"A monitoração eletrônica do agressor, havendo risco, pode ser determinada pela autoridade judicial ou pelo delegado quando o Município não for sede de",["comarca.","Estado.","região metropolitana.","distrito.","capital."],"Art. 12-D.")
q(3,"A inquirição da mulher será feita preferencialmente em recinto especialmente projetado, e o depoimento será registrado em meio",["eletrônico ou magnético.","apenas escrito.","apenas oral.","apenas fotográfico.","apenas manuscrito."],"Art. 10-A, § 2º.")
q(3,"A autoridade policial, ao tomar o pedido da ofendida, deve registrar informação sobre a condição de a ofendida ser pessoa com",["deficiência.","emprego.","imóvel.","estudo.","religião."],"Art. 12, § 1º, IV.")
q(3,"Serão admitidos como meios de prova os laudos ou prontuários médicos fornecidos por hospitais e",["postos de saúde.","escolas.","cartórios.","bancos.","empresas."],"Art. 12, § 3º.")
q(3,"Os Estados e o Distrito Federal darão prioridade, no âmbito da Polícia Civil, à criação de Delegacias Especializadas de Atendimento à Mulher e de núcleos investigativos de",["feminicídio.","trânsito.","patrimônio.","meio ambiente.","consumo."],"Art. 12-A.")
q(3,"A assistência à mulher será prestada de forma articulada e conforme princípios da Lei",["Orgânica da Assistência Social.","Orgânica da Saúde.","de Execução Penal.","do Inquilinato.","de Licitações."],"Art. 9º.")
q(3,"O juiz assegurará acesso prioritário à remoção quando a mulher for servidora pública, integrante da administração",["direta ou indireta.","apenas direta.","apenas federal.","apenas municipal.","apenas estadual."],"Art. 9º, § 2º, I.")
q(3,"A autoridade poderá juntar aos autos a folha de antecedentes do agressor, indicando a existência de mandado de prisão ou registro de outras ocorrências, conforme o art. 12, inciso",["VI.","IV.","V.","VII.","III."],"Art. 12, VI.")
q(3,"Ao verificar a existência de arma de fogo do agressor, a autoridade deve notificar a instituição responsável pela concessão do registro ou do porte, nos termos do Estatuto do",["Desarmamento.","Idoso.","Torcedor.","Desporto.","Índio."],"Art. 12, VI-A.")
q(3,"O risco atual ou iminente que autoriza o afastamento do agressor pode ser à vida ou à integridade física, sexual, psicológica, moral ou",["patrimonial.","eleitoral.","religiosa.","tributária.","comercial."],"Art. 12-C.")
q(3,"No texto do chamado na madrugada, o fato de o Município não ser sede de comarca e de não haver delegado disponível autoriza o afastamento pelo",["policial.","vizinho.","prefeito.","síndico.","vereador."],"Art. 12-C, III.","mp2a")
q(3,"No texto do chamado na madrugada, a decisão do juiz sobre a manutenção da medida deve ocorrer em",["vinte e quatro horas, igual prazo.","dez dias.","cinco dias.","trinta dias.","quarenta e oito horas."],"Art. 12-C, § 1º.","mp2a")
q(3,"No texto da retirada de pertences, além de acompanhar a retirada, a autoridade deve informar à ofendida os",["direitos conferidos na lei e os serviços disponíveis.","dados do agressor.","segredos da investigação.","valores dos bens.","nomes das testemunhas."],"Art. 11, V.","mp2b")
q(3,"No texto da retirada de pertences, o acompanhamento ocorre se necessário, para assegurar a retirada dos pertences do local da ocorrência ou do",["domicílio familiar.","trabalho.","clube.","bar.","carro."],"Art. 11, IV.","mp2b")
q(3,"No texto do pedido de medidas, o pedido da ofendida deve conter, além de qualificações, nome e idade dos",["dependentes.","vizinhos.","amigos.","empregados.","clientes."],"Art. 12, § 1º, II.","mp2c")
q(3,"No texto do pedido de medidas, à autoridade policial cabe anexar ao pedido o boletim de ocorrência e cópia de todos os documentos disponíveis em posse da",["ofendida.","testemunha.","autoridade.","agressora.","juíza."],"Art. 12, § 2º.","mp2c")
q(3,"No texto do pedido de medidas, o prazo de 48 horas é para a remessa do expediente ao",["juiz.","delegado superior.","prefeito.","promotor apenas.","advogado."],"Art. 12, III.","mp2c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Lei Maria da Penha: política, assistência e atendimento (arts. 8º a 12-C)",[
 ("pol","Política pública",["ações articuladas","atendimento especializado","capacitar a Guarda Municipal"],"seção 1"),
 ("ass","Assistência",["SUS e Susp","vínculo por 6 meses","ressarcimento pelo agressor"],"seção 2"),
 ("aut","Autoridade policial",["providências imediatas","atendimento sem revitimização","proteção e transporte"],"seção 3"),
 ("reg","Procedimentos",["boletim e provas","corpo de delito","medidas protetivas em 48 horas"],"seção 3"),
 ("afa","Afastamento do agressor",["juiz","delegado (sem comarca)","policial (sem comarca e sem delegado)"],"seção 3"),
 ("pra","Prazos",["48 horas ao juiz","24 horas de comunicação","24 horas de decisão"],"seção 3")],
 "Na prova: quem afasta o agressor e os prazos de 48 e 24 horas")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a política pública; as demais, a assistência, o atendimento policial e o afastamento do agressor.","Fontes: Edital 02/2026, Anexo I; Lei 11.340/2006 (Lei Maria da Penha), arts. 8º a 12-C, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("mp-2","Lei Maria da Penha: assistência e atendimento policial (arts. 8º a 12-C)",Q,list(tx),
 cobertura=["Cobertos: arts. 8º a 12-C. O art. 12-B (vetado em parte) e o art. 12-D (monitoração eletrônica) aparecem só em questões."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Conferir se o edital inclui o art. 12-D.","Trechos de lei copiados de fontes/mp.txt por programa.","Casos mp2a, mp2b e mp2c fictícios."],
 fontes_conferidas=["Lei 11.340/2006, arts. 8º a 12-C: texto da Câmara, copiado por programa."])
gravar("mp-2",aula_html,banco("mp-2",Q),tx)
