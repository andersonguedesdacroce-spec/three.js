import sys,pickle; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','gerador')); from aulas import *
LEAD="A segunda parte do Estatuto (arts. 6º a 22) trata da guarda como órgão: como é criada, qual o tamanho máximo, quem pode entrar, como é controlada e que prerrogativas seus integrantes têm. É a parte mais numérica da lei, e a Vunesp explora justamente os números: percentuais, idade, prazos e limites de efetivo."
S={}
S[1]="""## 1. Criação e subordinação

[[LEI|art. 6º|O Município pode criar, por lei, sua guarda municipal.]]

[[LEI|art. 6º, parágrafo único|A guarda municipal é subordinada ao chefe do Poder Executivo municipal.]]

Dois pontos: a criação é uma **faculdade** (“pode”), não uma obrigação, e exige **lei**, não decreto. A subordinação é ao **prefeito**, e não ao governador, à Câmara Municipal ou às polícias.
"""
S[2]="""## 2. Limite do efetivo e uso compartilhado

[[LEI|art. 7º, caput|As guardas municipais não poderão ter efetivo superior a:]]

| População do Município | Efetivo máximo | Condição |
| --- | --- | --- |
| até 50 mil habitantes | 0,4% da população | — |
| mais de 50 mil e menos de 500 mil | 0,3% da população | não inferior ao limite da faixa anterior |
| mais de 500 mil | 0,2% da população | não inferior ao limite da faixa anterior |

A condição da última coluna evita que uma cidade maior acabe com um teto menor do que o de uma cidade menor. Campinas, com cerca de 1,14 milhão de habitantes no Censo de 2022, está na última faixa: 0,2% dá um teto em torno de 2.280 guardas.

Se a população cair em censo ou estimativa oficial do IBGE, o efetivo existente é preservado e depois ajustado à variação populacional, nos termos de lei municipal (parágrafo único).

[[LEI|art. 8º|Municípios limítrofes podem, mediante consórcio público, utilizar, reciprocamente, os serviços da guarda municipal de maneira compartilhada.]]

[[NOTA: São três condições juntas: Municípios limítrofes, consórcio público e uso recíproco. Convênio com qualquer Município ou cessão sem consórcio não atendem ao art. 8º.]]
"""
S[3]="""## 3. Carreira e requisitos de investidura

[[LEI|art. 9º|A guarda municipal é formada por servidores públicos integrantes de carreira única e plano de cargos e remuneração, nos termos de lei municipal.]]

[[LEI|art. 10, caput|São requisitos básicos para investidura em cargo público na guarda municipal:]]

1. nacionalidade brasileira;
2. gozo dos direitos políticos;
3. quitação com as obrigações militares e eleitorais;
4. nível médio completo de escolaridade;
5. idade mínima de 18 (dezoito) anos;
6. aptidão física, mental e psicológica; e
7. idoneidade moral comprovada por investigação social e certidões expedidas perante o Poder Judiciário estadual, federal e distrital.

Outros requisitos podem ser fixados em lei municipal (parágrafo único). Repare que são requisitos **básicos**: o edital de Campinas pode exigir mais, como carteira de habilitação, desde que a lei municipal preveja.
"""
S[4]="""## 4. Formação e capacitação

O exercício do cargo exige **capacitação específica**, com matriz curricular compatível com as atividades. Pode ser adaptada a matriz curricular nacional para formação em segurança pública, formulada pela Senasp, do Ministério da Justiça (art. 11).

O Município **pode** criar órgão próprio de formação, treinamento e aperfeiçoamento, guiado pelos princípios do art. 3º (art. 12). Também pode firmar convênios ou consorciar-se com outros Municípios para isso (§ 1º). O Estado pode, por convênio, manter órgão de formação centralizado, com participação dos Municípios conveniados no conselho gestor (§ 2º).

[[LEI|art. 12, § 3º|O órgão referido no § 2º não pode ser o mesmo destinado a formação, treinamento ou aperfeiçoamento de forças militares.]]
"""
S[5]="""## 5. Controle interno, externo e social

[[LEI|art. 13, caput|O funcionamento das guardas municipais será acompanhado por órgãos próprios, permanentes, autônomos e com atribuições de fiscalização, investigação e auditoria, mediante:]]

São dois controles obrigatórios, com regras diferentes de cabimento:

1. **Controle interno, pela corregedoria.** Existe nas guardas com efetivo **superior a 50 servidores** e em **todas as que utilizam arma de fogo**. Serve para apurar as infrações disciplinares de seus integrantes (inciso I).
2. **Controle externo, pela ouvidoria.** Existe em **qualquer guarda**, qualquer que seja o número de servidores. É independente da direção da guarda e recebe, examina e encaminha reclamações, sugestões, elogios e denúncias sobre a conduta dos dirigentes e integrantes (inciso II).

O Executivo municipal **pode** criar órgão colegiado de **controle social** das atividades de segurança do Município (§ 1º). E corregedores e ouvidores têm **mandato**, cuja perda só pode ser decidida pela **maioria absoluta da Câmara Municipal**, fundada em razão relevante e específica prevista em lei municipal (§ 2º).

Para o controle interno, a guarda tem **código de conduta próprio**, conforme lei municipal (art. 14).

[[LEI|art. 14, parágrafo único|As guardas municipais não podem ficar sujeitas a regulamentos disciplinares de natureza militar.]]
"""
S[6]="""## 6. Comando e carreira

[[LEI|art. 15, caput|Os cargos em comissão das guardas municipais deverão ser providos por membros efetivos do quadro de carreira do órgão ou entidade.]]

A exceção está no § 1º: nos **primeiros 4 anos** de funcionamento, a guarda pode ser dirigida por profissional estranho a seus quadros, preferencialmente com experiência ou formação na área de segurança ou defesa social.

Para ocupar cargos em todos os níveis da carreira, deve ser observado **percentual mínimo para o sexo feminino**, definido em lei municipal (§ 2º). E é garantida a **progressão funcional** em todos os níveis (§ 3º).
"""
S[7]="""## 7. Prerrogativas e identidade

[[LEI|art. 16|Aos guardas municipais é autorizado o porte de arma de fogo, conforme previsto em lei.]]

O porte é suspenso em razão de **restrição médica**, **decisão judicial** ou **justificativa da adoção da medida pelo respectivo dirigente** (parágrafo único). O detalhamento do porte está no Estatuto do Desarmamento.

Os demais artigos garantem:

- **Telefone 153 e faixa de rádio:** a Anatel destina a linha 153 e faixa exclusiva de frequência de rádio aos Municípios que possuam guarda municipal (art. 17).
- **Cela separada:** o guarda municipal é recolhido à cela, isoladamente dos demais presos, quando sujeito à prisão antes de condenação definitiva (art. 18).
- **Sem denominação militar:** a hierarquia não pode usar denominação idêntica à das forças militares quanto a postos e graduações, títulos, uniformes, distintivos e condecorações (art. 19).
- **Representação:** as guardas têm representatividade no Conselho Nacional de Segurança Pública, no Conselho Nacional das Guardas Municipais e, no interesse dos Municípios, no Conselho Nacional de Secretários e Gestores Municipais de Segurança Pública (art. 20).
- **Uniforme:** padronizado, preferencialmente na cor **azul-marinho** (art. 21).
"""
S[8]="""## 8. Disposições finais e o nome da guarda

As guardas que já existiam em 2014 tiveram **2 anos** para se adaptar ao Estatuto (art. 22, caput).

[[LEI|art. 22, parágrafo único|É assegurada a utilização de outras denominações consagradas pelo uso, como guarda civil, guarda civil municipal, guarda metropolitana e guarda civil metropolitana.]]

É por isso que Campinas usa “Guarda Municipal” e São Paulo, “Guarda Civil Metropolitana”: ambas as formas são aceitas. Mas, em abril de 2026, o STF decidiu na **ADPF 1214** que nenhum Município pode trocar o nome por **“Polícia Municipal”** ou denominação semelhante. As variações permitidas são apenas as de “guarda”.
"""
S[10]="""## 10. Na rotina do guarda

- **Telefone da guarda:** o 153 é o número nacional destinado às guardas municipais.
- **Denúncia de abuso:** quem reclama da conduta de um agente procura a ouvidoria, que é externa e independente da direção.
- **Infração disciplinar:** é apurada pela corregedoria, segundo o código de conduta, e nunca por regulamento militar.
- **Afastamento médico:** a restrição médica suspende o porte de arma.
- **Patentes:** a guarda não usa “sargento”, “tenente” ou “capitão”; as classes têm nomes próprios.
"""
S[11]="""## 11. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Guarda criada por decreto, ou criação obrigatória | o Município pode criar, por lei |
| Subordinada ao governador ou ao secretário de segurança estadual | ao chefe do Executivo municipal |
| Trocar os percentuais 0,4%, 0,3% e 0,2% | quanto maior a cidade, menor o percentual |
| Uso compartilhado por convênio entre quaisquer Municípios | Municípios limítrofes, por consórcio público |
| Idade mínima de 21 anos ou nível superior | 18 anos e nível médio completo |
| Corregedoria em todas as guardas | só com mais de 50 servidores ou que usem arma de fogo |
| Ouvidoria só nas guardas grandes | em qualquer guarda |
| Perda de mandato de corregedor por decisão do prefeito | maioria absoluta da Câmara Municipal |
| Diretor externo por até 2 anos | primeiros 4 anos de funcionamento |
| Regulamento disciplinar militar | proibido |
| Uniforme obrigatoriamente azul-marinho | preferencialmente azul-marinho |
| “Polícia Municipal” como nome aceito | vedado pelo STF; só variações de “guarda” |
"""
S[12]="""## 12. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 6º | Município pode criar por lei; subordinada ao prefeito |
| Art. 7º | 0,4% até 50 mil; 0,3% até 500 mil; 0,2% acima |
| Art. 8º | limítrofes, consórcio público, uso recíproco |
| Art. 9º | carreira única e plano de cargos e remuneração |
| Art. 10 | brasileiro, direitos políticos, quitação, nível médio, 18 anos, aptidão, idoneidade |
| Arts. 11 e 12 | capacitação específica; órgão de formação não pode ser o das forças militares |
| Art. 13 | corregedoria: mais de 50 ou armada; ouvidoria: sempre; mandato perdido por maioria absoluta da Câmara |
| Art. 14 | código de conduta; nada de regulamento militar |
| Art. 15 | comissionados efetivos; externo nos 4 primeiros anos; cota feminina por lei municipal |
| Art. 16 | porte conforme lei; suspenso por restrição médica, decisão judicial ou dirigente |
| Arts. 17 a 21 | 153; cela separada; sem patentes militares; conselhos; azul-marinho |
| Art. 22 | 2 anos para adaptar; guarda civil, metropolitana etc.; “Polícia Municipal” vedado |
"""
QR=[("Questão 1","De acordo com a Lei 13.022/2014, a guarda municipal é subordinada",["ao chefe do Poder Executivo municipal.","ao governador do Estado.","à Câmara Municipal.","ao comandante da polícia militar.","ao secretário estadual de segurança pública."],2,"Art. 6º, parágrafo único."),
("Questão 2","Em Município com mais de 500 mil habitantes, o efetivo da guarda municipal não pode ser superior a",["0,2% da população, desde que não inferior ao limite da faixa anterior.","0,4% da população.","0,3% da população, sem outra condição.","0,5% da população.","0,1% da população."],0,"Art. 7º, III."),
("Questão 3","O controle interno, exercido por corregedoria, é obrigatório nas guardas",["com efetivo superior a 50 servidores e em todas as que utilizam arma de fogo.","com efetivo superior a 100 servidores, apenas.","de Municípios com mais de 500 mil habitantes, apenas.","que tenham ouvidoria.","em qualquer caso, independentemente do efetivo."],3,"Art. 13, I."),
("Questão 4","É requisito básico para investidura em cargo da guarda municipal",["idade mínima de 18 anos.","idade mínima de 21 anos.","nível superior completo.","carteira nacional de habilitação, por força da lei federal.","serviço militar prestado."],1,"Art. 10, V.")]
QRF=qr_md(QR,9)
Q=[]
def q(n,e,a,c,tx=None): Q.append((n,e,a,c,tx))
# FÁCEIS
q(1,"Segundo a Lei 13.022/2014, o Município pode criar sua guarda municipal por meio de",["lei.","decreto.","portaria.","resolução da Câmara.","convênio com o Estado."],"Art. 6º.")
q(1,"A guarda municipal é subordinada ao",["chefe do Poder Executivo municipal.","governador do Estado.","presidente da Câmara Municipal.","delegado de polícia.","juiz da comarca."],"Art. 6º, parágrafo único.")
q(1,"Em Municípios com até 50 mil habitantes, o efetivo da guarda não pode superar",["0,4% da população.","0,3% da população.","0,2% da população.","0,5% da população.","1% da população."],"Art. 7º, I.")
q(1,"Em Municípios com mais de 50 mil e menos de 500 mil habitantes, o efetivo da guarda não pode superar",["0,3% da população.","0,4% da população.","0,2% da população.","0,1% da população.","0,5% da população."],"Art. 7º, II.")
q(1,"A guarda municipal é formada por servidores públicos integrantes de",["carreira única e plano de cargos e remuneração.","carreiras múltiplas, conforme a especialidade.","cargos comissionados de livre nomeação.","contratos temporários.","quadro da polícia militar cedido ao Município."],"Art. 9º.")
q(1,"É requisito básico para investidura em cargo da guarda municipal a",["nacionalidade brasileira.","naturalidade do próprio Município.","residência no Município há mais de dois anos.","filiação partidária.","experiência prévia em segurança."],"Art. 10, I.")
q(1,"O nível de escolaridade exigido como requisito básico pela lei é",["nível médio completo.","nível fundamental completo.","nível superior completo.","nível técnico em segurança.","pós-graduação."],"Art. 10, IV.")
q(1,"A idade mínima exigida pela lei para investidura na guarda municipal é de",["18 anos.","21 anos.","16 anos.","20 anos.","25 anos."],"Art. 10, V.")
q(1,"O controle externo da guarda municipal é exercido por",["ouvidoria.","corregedoria.","polícia militar.","Câmara de Vereadores, diretamente.","Tribunal de Justiça."],"Art. 13, II.")
q(1,"O controle interno da guarda municipal é exercido por",["corregedoria.","ouvidoria.","Ministério Público.","Tribunal de Contas.","conselho comunitário."],"Art. 13, I.")
q(1,"Segundo a lei, as guardas municipais não podem ficar sujeitas a regulamentos disciplinares de natureza",["militar.","civil.","administrativa.","municipal.","ética."],"Art. 14, parágrafo único.")
q(1,"Aos guardas municipais é autorizado o porte de arma de fogo",["conforme previsto em lei.","em qualquer circunstância.","somente durante o serviço noturno.","apenas com autorização do prefeito.","apenas nas capitais."],"Art. 16.")
q(1,"A linha telefônica destinada pela Anatel aos Municípios que possuem guarda municipal é a de número",["153.","190.","192.","193.","197."],"Art. 17.")
q(1,"O uniforme das guardas municipais deve ser padronizado, preferencialmente na cor",["azul-marinho.","cinza.","preta.","verde-oliva.","caqui."],"Art. 21.")
q(1,"Quando sujeito à prisão antes de condenação definitiva, o guarda municipal tem assegurado o",["recolhimento à cela, isoladamente dos demais presos.","direito à prisão domiciliar.","direito de responder em liberdade, sempre.","recolhimento em quartel militar.","afastamento remunerado em sua casa."],"Art. 18.")
q(1,"A estrutura hierárquica da guarda municipal não pode utilizar denominação idêntica à das",["forças militares.","guardas de outros Municípios.","secretarias municipais.","polícias civis.","empresas de segurança privada."],"Art. 19.")
q(1,"Segundo o art. 8º, Municípios limítrofes podem usar reciprocamente os serviços da guarda municipal, de maneira compartilhada, mediante",["consórcio público.","decreto estadual.","contrato de terceirização.","portaria do comandante.","acordo verbal."],"Art. 8º.")
q(1,"O parágrafo único do art. 22 assegura o uso de outras denominações consagradas pelo uso, como",["guarda civil metropolitana.","polícia municipal.","polícia comunitária.","brigada municipal.","força municipal."],"Art. 22, parágrafo único.")
q(1,"O exercício das atribuições dos cargos da guarda municipal requer",["capacitação específica, com matriz curricular compatível com suas atividades.","formação militar prévia.","curso superior em direito.","estágio em unidade da polícia civil.","apenas o curso de tiro."],"Art. 11.")
q(1,"No caso narrado, a criação da guarda do Município de Vale Verde por decreto do prefeito",["contraria a lei, que exige lei para a criação.","está correta, pois o decreto basta.","está correta, desde que a Câmara seja informada.","contraria a lei, que exige autorização do Estado.","está correta se o efetivo for pequeno."],"Art. 6º: o Município pode criar, por lei, sua guarda.","tg2")
# MÉDIAS
q(2,"Em Município com mais de 500 mil habitantes, o efetivo máximo é de 0,2% da população, desde que",["não seja inferior ao limite da faixa anterior.","não ultrapasse mil guardas.","seja aprovado pelo governador.","haja convênio com a polícia militar.","a guarda seja armada."],"Art. 7º, III.")
q(2,"Se houver redução da população em censo ou estimativa oficial do IBGE, a lei garante",["a preservação do efetivo existente, que deverá ser ajustado à variação populacional, nos termos de lei municipal.","a demissão imediata dos guardas excedentes.","a transferência dos excedentes para a polícia militar.","a extinção da guarda municipal.","o congelamento do efetivo por dez anos."],"Art. 7º, parágrafo único.")
q(2,"É requisito básico de investidura previsto no art. 10 a",["quitação com as obrigações militares e eleitorais.","comprovação de renda mínima.","residência no Município.","aprovação em curso de formação militar.","apresentação de carta de recomendação."],"Art. 10, III.")
q(2,"A idoneidade moral, requisito de investidura, deve ser comprovada por",["investigação social e certidões expedidas perante o Poder Judiciário estadual, federal e distrital.","declaração do próprio candidato.","atestado do comandante da guarda.","certidão da Câmara Municipal.","entrevista com psicólogo."],"Art. 10, VII.")
q(2,"Quanto aos requisitos de investidura, o parágrafo único do art. 10 dispõe que",["outros requisitos poderão ser estabelecidos em lei municipal.","nenhum outro requisito pode ser exigido.","os requisitos podem ser dispensados por decreto.","os requisitos são definidos pelo Estado.","os requisitos valem só para guardas armadas."],"Art. 10, parágrafo único.")
q(2,"A matriz curricular da guarda municipal pode ser adaptada da matriz nacional para formação em segurança pública formulada pela",["Secretaria Nacional de Segurança Pública (Senasp) do Ministério da Justiça.","Secretaria Estadual de Educação.","Academia de Polícia Militar.","Escola Superior de Guerra.","Câmara Municipal."],"Art. 11, parágrafo único.")
q(2,"O órgão de formação mantido pelo Estado, mediante convênio com os Municípios,",["não pode ser o mesmo destinado à formação de forças militares.","deve ser o mesmo da polícia militar.","é obrigatório em todos os Estados.","dispensa a participação dos Municípios.","só forma guardas armados."],"Art. 12, § 3º.")
q(2,"A ouvidoria das guardas municipais existe",["qualquer que seja o número de servidores da guarda.","apenas nas guardas com mais de 50 servidores.","apenas nas guardas que utilizam arma de fogo.","apenas nas capitais.","por decisão facultativa do prefeito."],"Art. 13, II.")
q(2,"A ouvidoria da guarda municipal é",["independente em relação à direção da respectiva guarda.","subordinada ao comandante da guarda.","composta pelos próprios guardas.","órgão da polícia militar.","órgão do Ministério Público."],"Art. 13, II.")
q(2,"A perda do mandato de corregedores e ouvidores será decidida pela",["maioria absoluta da Câmara Municipal, fundada em razão relevante e específica prevista em lei municipal.","decisão do prefeito.","maioria simples da Câmara Municipal.","decisão do comandante da guarda.","decisão do Ministério Público."],"Art. 13, § 2º.")
q(2,"O órgão colegiado para controle social das atividades de segurança do Município",["poderá ser criado pelo Poder Executivo municipal.","é obrigatório em todos os Municípios.","é criado pela polícia militar.","substitui a ouvidoria.","é presidido pelo comandante da guarda."],"Art. 13, § 1º.")
q(2,"Para fins de controle interno, a guarda municipal terá",["código de conduta próprio, conforme dispuser lei municipal.","regulamento disciplinar do Exército.","regulamento disciplinar da polícia militar estadual.","código de ética da OAB.","apenas normas verbais do comandante."],"Art. 14.")
q(2,"Os cargos em comissão das guardas municipais devem ser providos por",["membros efetivos do quadro de carreira do órgão ou entidade.","pessoas de livre escolha do prefeito, em qualquer caso.","oficiais da polícia militar.","delegados de polícia.","vereadores."],"Art. 15, caput.")
q(2,"Nos primeiros anos de funcionamento, a guarda municipal poderá ser dirigida por profissional estranho a seus quadros pelo prazo de",["4 anos.","2 anos.","1 ano.","5 anos.","10 anos."],"Art. 15, § 1º.")
q(2,"Para ocupação dos cargos em todos os níveis da carreira, deverá ser observado",["o percentual mínimo para o sexo feminino, definido em lei municipal.","o percentual máximo de 30% para mulheres.","a preferência por candidatos com serviço militar.","a ordem de antiguidade exclusivamente.","o percentual de 50% para cada sexo, fixado na lei federal."],"Art. 15, § 2º.")
q(2,"Suspende-se o direito ao porte de arma de fogo do guarda municipal em razão de",["restrição médica, decisão judicial ou justificativa da adoção da medida pelo respectivo dirigente.","férias regulamentares.","mudança de turno.","transferência de setor.","licença-paternidade."],"Art. 16, parágrafo único.")
q(2,"A Anatel destinará aos Municípios que possuam guarda municipal",["linha telefônica de número 153 e faixa exclusiva de frequência de rádio.","linha 190 e viaturas.","faixa de televisão educativa.","apenas faixa de rádio compartilhada com a polícia.","linha 0800 gratuita."],"Art. 17.")
q(2,"As guardas que já existiam na data de publicação da lei deveriam adaptar-se às suas disposições no prazo de",["2 anos.","4 anos.","1 ano.","5 anos.","6 meses."],"Art. 22, caput.")
q(2,"No caso narrado, o efetivo de 80 guardas previsto para o Município de Vale Verde, com 40 mil habitantes,",["respeita o limite legal, que seria de até 160 guardas.","ultrapassa o limite legal, que seria de 40 guardas.","ultrapassa o limite legal, que seria de 60 guardas.","respeita o limite, que seria de até 80 guardas exatos, por ser 0,2%.","depende de autorização do Estado."],"Até 50 mil habitantes: 0,4% de 40.000 = 160.","tg2")
q(2,"No caso narrado, a proposta de o Município de Vale Verde usar a guarda do Município vizinho Serra Alta, com o qual faz divisa, é possível desde que",["seja firmado consórcio público.","haja decreto do governador.","os guardas sejam cedidos sem formalidade.","Serra Alta tenha mais de 500 mil habitantes.","a Câmara aprove por maioria simples."],"Art. 8º: limítrofes, mediante consórcio público.","tg2")
# DIFÍCEIS
q(3,"Assinale a alternativa INCORRETA de acordo com a Lei 13.022/2014.",["O Município é obrigado a criar guarda municipal quando ultrapassar 50 mil habitantes.","O Município pode criar, por lei, sua guarda municipal.","A guarda municipal é subordinada ao chefe do Executivo municipal.","A guarda é formada por servidores de carreira única.","Outros requisitos de investidura podem ser fixados em lei municipal."],"A criação é faculdade (“pode”).")
q(3,"Um Município tem 300 mil habitantes. Segundo o art. 7º, sua guarda pode ter, no máximo,",["900 guardas, desde que esse número não seja inferior ao limite da faixa anterior.","1.200 guardas.","600 guardas.","300 guardas.","1.500 guardas."],"Faixa de 50 mil a 500 mil: 0,3% de 300.000 = 900.")
q(3,"Considere as afirmações: I. A corregedoria é obrigatória em guardas com mais de 50 servidores. II. A corregedoria é obrigatória em todas as guardas que usam arma de fogo, ainda que pequenas. III. A ouvidoria só existe nas guardas armadas. Está correto o que se afirma em",["I e II, apenas.","I, II e III.","I e III, apenas.","II e III, apenas.","I, apenas."],"A ouvidoria existe em qualquer guarda.")
q(3,"Considere as afirmações sobre o art. 15: I. Cargos em comissão são providos por membros efetivos da carreira. II. Nos primeiros 4 anos, a guarda pode ser dirigida por profissional externo, preferencialmente com experiência em segurança. III. A progressão funcional é garantida em todos os níveis. Está correto o que se afirma em",["I, II e III.","I e II, apenas.","I e III, apenas.","II e III, apenas.","I, apenas."],"Art. 15, caput e §§ 1º e 3º.")
q(3,"Assinale a alternativa que NÃO constitui hipótese de suspensão do porte de arma de fogo prevista no art. 16.",["Pedido de vereador.","Restrição médica.","Decisão judicial.","Justificativa da adoção da medida pelo respectivo dirigente.","Decisão judicial em processo envolvendo o guarda."],"Só restrição médica, decisão judicial ou justificativa do dirigente.")
q(3,"Assinale a alternativa que NÃO é requisito básico de investidura previsto no art. 10.",["Carteira nacional de habilitação.","Nacionalidade brasileira.","Gozo dos direitos políticos.","Aptidão física, mental e psicológica.","Nível médio completo."],"A CNH pode ser exigida por lei municipal, mas não está no art. 10.")
q(3,"Segundo o art. 19, a hierarquia da guarda municipal não pode utilizar denominação idêntica à das forças militares quanto a",["postos e graduações, títulos, uniformes, distintivos e condecorações.","apenas postos e graduações.","apenas uniformes.","nomes das unidades e bases.","horários de serviço."],"Art. 19.")
q(3,"É reconhecida a representatividade das guardas municipais no",["Conselho Nacional de Segurança Pública, no Conselho Nacional das Guardas Municipais e no Conselho Nacional de Secretários e Gestores Municipais de Segurança Pública.","Conselho Nacional de Justiça.","Conselho Nacional do Ministério Público.","Conselho de Defesa Nacional.","Conselho Federal da OAB."],"Art. 20.")
q(3,"Assinale a alternativa correta sobre o uniforme das guardas municipais.",["Deve ser padronizado, preferencialmente na cor azul-marinho.","Deve ser obrigatoriamente azul-marinho, sob pena de nulidade.","Pode ser idêntico ao das forças militares.","É definido pela polícia militar estadual.","É livre, a critério de cada guarda."],"Art. 21: preferencialmente.")
q(3,"Considere as afirmações sobre o art. 12: I. É facultada ao Município a criação de órgão de formação. II. Os Municípios podem consorciar-se para esse fim. III. O órgão estadual de formação pode ser o mesmo das forças militares. Está correto o que se afirma em",["I e II, apenas.","I, II e III.","I e III, apenas.","II e III, apenas.","III, apenas."],"Art. 12, § 3º veda o mesmo órgão das forças militares.")
q(3,"Segundo decisão do STF de 2026 (ADPF 1214), assinale a denominação que um Município NÃO pode adotar para sua guarda.",["Polícia Municipal.","Guarda Civil Metropolitana.","Guarda Civil Municipal.","Guarda Metropolitana.","Guarda Municipal."],"O STF vedou a troca por “Polícia Municipal” e similares.")
q(3,"Assinale a alternativa correta sobre o controle das guardas municipais.",["Os órgãos de controle devem ser próprios, permanentes, autônomos e com atribuições de fiscalização, investigação e auditoria.","O controle é exercido exclusivamente pela polícia militar.","A corregedoria é subordinada à ouvidoria.","O controle social é obrigatório e substitui a ouvidoria.","O mandato dos corregedores é de livre exoneração pelo prefeito."],"Art. 13, caput.")
q(3,"Assinale a alternativa INCORRETA.",["Municípios de qualquer região podem compartilhar suas guardas por simples convênio.","Municípios limítrofes podem compartilhar suas guardas mediante consórcio público.","O compartilhamento previsto no art. 8º é recíproco.","O art. 8º exige consórcio público.","O art. 8º se refere a Municípios que fazem divisa."],"O art. 8º exige Municípios limítrofes e consórcio público.")
q(3,"Assinale a alternativa que associa corretamente o artigo ao conteúdo.",["Art. 18: cela separada em prisão antes de condenação definitiva.","Art. 17: uniforme azul-marinho.","Art. 21: telefone 153.","Art. 19: porte de arma de fogo.","Art. 16: denominações consagradas pelo uso."],"Os demais estão trocados.")
q(3,"Considere as afirmações: I. As guardas municipais podem adotar regulamento disciplinar da polícia militar. II. As guardas têm código de conduta próprio, conforme lei municipal. III. A corregedoria apura as infrações disciplinares atribuídas aos integrantes do quadro. Está correto o que se afirma em",["II e III, apenas.","I, II e III.","I e II, apenas.","I e III, apenas.","II, apenas."],"Art. 14, parágrafo único proíbe regulamento militar.")
q(3,"No caso narrado, a nomeação de um coronel da reserva, sem vínculo com a guarda, para comandá-la no primeiro ano de funcionamento é",["permitida, pois nos primeiros 4 anos a guarda pode ser dirigida por profissional estranho a seus quadros.","proibida, pois o comando deve ser de membro efetivo desde o início.","permitida por tempo indeterminado.","proibida, por se tratar de militar.","permitida somente com aprovação do Estado."],"Art. 15, § 1º.","tg2")
q(3,"No caso narrado, a proposta de que os agentes de Vale Verde usem as patentes de soldado, cabo e sargento",["contraria o art. 19, que proíbe denominação idêntica à das forças militares quanto a postos e graduações.","está de acordo com a lei, desde que aprovada pela Câmara.","contraria apenas o regulamento da polícia militar.","está de acordo com a lei, por serem guardas armados.","é permitida somente para os cargos de comando."],"Art. 19.","tg2")
q(3,"No caso narrado, a proposta de dispensar a ouvidoria por ser uma guarda pequena e desarmada",["contraria a lei, pois a ouvidoria existe qualquer que seja o número de servidores.","está correta, pois a ouvidoria só é exigida nas guardas armadas.","está correta, pois a ouvidoria só é exigida com mais de 50 servidores.","contraria a lei apenas se a guarda for armada.","depende de decisão do Ministério Público."],"Art. 13, II.","tg2")
q(3,"Um Município com 40 mil habitantes cria guarda desarmada com 30 servidores. Segundo o art. 13, ele está obrigado a manter",["ouvidoria, mas não corregedoria.","corregedoria e ouvidoria.","corregedoria, mas não ouvidoria.","nenhum órgão de controle.","apenas o conselho de controle social."],"Corregedoria só com mais de 50 servidores ou arma de fogo; ouvidoria sempre.")
q(3,"Assinale a alternativa correta sobre o art. 22 da Lei 13.022/2014.",["A lei se aplica a todas as guardas existentes na data de sua publicação, que deviam adaptar-se em 2 anos.","A lei se aplica apenas às guardas criadas após sua publicação.","As guardas existentes ficaram dispensadas de adaptação.","O prazo de adaptação foi de 4 anos.","O art. 22 autoriza a denominação “Polícia Municipal”."],"Art. 22, caput.")
assert len(Q)==60
tg2="<strong>Município de Vale Verde discute a criação de sua guarda</strong><br><br>O prefeito de Vale Verde, cidade fictícia de 40 mil habitantes, anunciou que pretende criar a guarda municipal por decreto, com efetivo de 80 agentes, todos desarmados no primeiro momento. Para comandar a corporação no primeiro ano, ele indicou um coronel da reserva da polícia militar, sem vínculo com a guarda.<br><br>O projeto apresentado à imprensa prevê que os agentes usem as patentes de soldado, cabo e sargento e propõe dispensar a ouvidoria, “por se tratar de uma guarda pequena e desarmada”.<br><br>Para cobrir a falta de efetivo nos primeiros meses, a prefeitura estuda usar os serviços da guarda de Serra Alta, município vizinho que faz divisa com Vale Verde."
code,svg=mapa("A guarda como órgão: criação, tamanho, ingresso, controle e prerrogativas",[
 ("criacao","Criação (arts. 6º a 8º)",["Município pode criar, por lei","subordinada ao prefeito","0,4% · 0,3% · 0,2%"],"seções 1 e 2"),
 ("ingresso","Ingresso (arts. 9º a 12)",["carreira única","18 anos; nível médio","capacitação específica"],"seções 3 e 4"),
 ("controle","Controle (arts. 13 e 14)",["corregedoria: >50 ou armada","ouvidoria: sempre","nada de regulamento militar"],"seção 5"),
 ("comando","Comando (art. 15)",["comissionados efetivos","externo nos 4 primeiros anos","cota feminina por lei municipal"],"seção 6"),
 ("prerrog","Prerrogativas (16 a 21)",["porte conforme lei","153; cela separada","sem patentes; azul-marinho"],"seção 7"),
 ("nome","Nome (art. 22)",["2 anos para adaptar","guarda civil, metropolitana","Polícia Municipal: vedado"],"seção 8")],
 "Na prova: números (0,4/0,3/0,2%; 18 anos; mais de 50; 4 anos; 2 anos) e as palavras “pode” e “preferencialmente”")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7,8,'QR',10,11,12],QR,9,svg,"Os grupos seguem a ordem da lei: do nascimento da guarda até o nome que ela pode usar.","Fontes: Lei 13.022/2014, arts. 6º a 22, texto consolidado da Câmara dos Deputados; STF, ADPF 1214 (2026); IBGE, Censo 2022, para a população de Campinas. Caso de apoio fictício, criado para a aula.")
revisao("gm-2",'Estatuto das Guardas Municipais (Lei 13.022/2014, parte 2)',Q,{'tg2':tg2},pendencias=['O teto de efetivo de Campinas (cerca de 2.280 guardas, 0,2% de 1,14 milhão) usa o Censo 2022, sem conferência no IBGE.', 'Parte dos artigos da Lei 13.022/2014 foi conferida por trechos; reconferir o texto integral no Planalto.'])
gravar("gm-2",aula_html,banco("gm-2",Q),{"tg2":tg2})
print(len(aula_html))
