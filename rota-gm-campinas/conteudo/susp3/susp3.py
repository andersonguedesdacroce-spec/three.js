import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEI, LEIS
F='susp.txt'
C=lambda ref,txt: LEI(ref,txt,F)
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os postos susp-1 e susp-2 trataram da política nacional (princípios, diretrizes, objetivos) e da composição do Susp. Este posto fecha a Lei 13.675/2018 com o que costuma aparecer no fim das provas: as metas anuais e como cada atividade é medida, as diretrizes para os planos, o Sinesp (o banco nacional de dados da segurança pública), a formação dos profissionais (Sievap, matriz curricular, Renaesp e Rede EaD) e o cuidado com quem trabalha na segurança (Pró-Vida, prevenção do suicídio, identidade funcional e conferências a cada cinco anos)."
S={}
S[1]="## 1. Metas e diretrizes dos planos (arts. 11 a 14 e 24 a 27)\n\n"+C("art. 11","Art. 11. O Ministério Extraordinário da Segurança Pública fixará, anualmente, metas de excelência no âmbito das respectivas competências, visando à prevenção e à repressão das infrações penais e administrativas e à prevenção dos desastres, e utilizará indicadores públicos que demonstrem de forma objetiva os resultados pretendidos.")+"\n\n"+C("art. 12, III","III - as atividades de polícia ostensiva e de preservação da ordem pública serão aferidas, entre outros fatores, pela maior ou menor incidência de infrações penais e administrativas em determinada área, seguindo os parâmetros do Sinesp;")+"\n\n"+C("art. 13, III","III - efetivar o intercâmbio de experiências técnicas e operacionais entre os órgãos policiais federais, estaduais, distrital e as guardas municipais;")+"\n\n"+C("art. 24, XII","XII - fomentar estudos de planejamento urbano para que medidas de prevenção da criminalidade façam parte do plano diretor das cidades, de forma a estimular, entre outras ações, o reforço na iluminação pública e a verificação de pessoas e de famílias em situação de risco social e criminal.")+"\n\n"+C("art. 26, caput","Art. 26. É instituído, no âmbito do Susp, o Sistema Nacional de Acompanhamento e Avaliação das Políticas de Segurança Pública e Defesa Social (Sinaped),")+"""

**Como cada atividade é medida (art. 12)**

| Atividade | Indicador |
| --- | --- |
| Polícia judiciária | **Elucidação** de delitos (sobretudo mortes dolosas e roubos), prisões, mandados cumpridos, recuperação do produto do crime |
| Perícia | Critérios técnicos; laudos e qualidade da prova |
| **Polícia ostensiva** e preservação da ordem | **Incidência** de infrações em determinada área (parâmetros do Sinesp) |
| Bombeiros | Prevenção, tempo de resposta e recuperação de áreas |
| Sistema prisional | Vagas, relação presos/vagas, **reincidência** dos egressos |

> **Cuidado!** Na polícia judiciária, a aferição deve **distinguir** autoria por **prisão em flagrante** da autoria obtida por **investigação** (art. 12, § 2º).

> **Cai muito:** entre as diretrizes dos planos (art. 24) está levar a prevenção da criminalidade ao **plano diretor** das cidades, com reforço da **iluminação pública**. É o ponto em que o Município e a guarda entram de forma direta.
"""
S[2]="## 2. Sinesp: dados e informações (arts. 36 e 37)\n\n"+L("art. 36, I a IV","Art. 36. O Sinesp tem por objetivos:","V - produzir dados sobre a qualidade de vida")+"\n\n"+C("art. 37, caput","Art. 37. Integram o Sinesp todos os entes federados, por intermédio de órgãos criados ou designados para esse fim.")+"\n\n"+C("art. 37, § 2º","§ 2º O integrante que deixar de fornecer ou atualizar seus dados e informações no Sinesp poderá não receber recursos nem celebrar parcerias com a União para financiamento de programas, projetos ou ações de segurança pública e defesa social e do sistema prisional, na forma do regulamento.")+"\n\n"+C("art. 37, § 4º","§ 4º A omissão no fornecimento das informações legais implica responsabilidade administrativa do agente público.")+"""

**O que é, em uma frase:** o Sinesp é o sistema que reúne e padroniza os dados de segurança pública, prisionais e sobre drogas de todo o país.

- **Quem integra:** **todos os entes federados** (União, Estados, DF e **Municípios**).
- **Também produz dados sobre o próprio profissional:** qualidade de vida e saúde, vitimização (inclusive fora do horário), deficiência por vitimização, dependência química e **transtornos mentais e comportamento suicida**.
- **Padrões:** integridade, disponibilidade, confidencialidade, confiabilidade e tempestividade.

> **Cai muito:** quem **não fornece ou não atualiza** dados pode **ficar sem recursos** e sem parcerias com a União; e a omissão gera **responsabilidade administrativa** do agente público.
"""
S[3]="## 3. Formação e valorização: Sievap e Pró-Vida (arts. 38 a 45)\n\n"+L("art. 38, § 1º","§ 1º O Sievap é constituído, entre outros, pelos seguintes programas:","§ 2º Os órgãos integrantes do Susp terão acesso")+"\n\n"+C("art. 39, § 1º","§ 1º A matriz curricular é pautada nos direitos humanos, nos princípios da andragogia e nas teorias que enfocam o processo de construção do conhecimento.")+"\n\n"+C("art. 41","Art. 41. A Rede EaD-Senasp é escola virtual destinada aos profissionais de segurança pública e defesa social e tem como objetivo viabilizar o acesso aos processos de aprendizagem, independentemente das limitações geográficas e sociais existentes, com o propósito de democratizar a educação em segurança pública e defesa social.")+"\n\n"+C("art. 42-A, caput","Art. 42-A. O Pró-Vida produzirá diretrizes direcionadas à prevenção da violência autoprovocada e do suicídio.")+"\n\n"+C("art. 43","Art. 43. Os documentos de identificação funcional dos profissionais da área de segurança pública e defesa social serão padronizados mediante ato do Ministro de Estado Extraordinário da Segurança Pública e terão fé pública e validade em todo o território nacional.")+"\n\n"+C("art. 45","Art. 45. Deverão ser realizadas conferências a cada 5 (cinco) anos para debater as diretrizes dos planos nacional, estaduais e municipais de segurança pública e defesa social.")+"""

**Mapa das siglas**

| Sigla | O que é |
| --- | --- |
| **Sievap** | Sistema Integrado de **Educação e Valorização** Profissional |
| Matriz curricular nacional | Referencial teórico, metodológico e avaliativo; pautada em **direitos humanos** e **andragogia** |
| **Renaesp** | Rede Nacional de **Altos Estudos**: instituições de ensino superior; graduação, extensão e pós |
| **Rede EaD-Senasp** | **Escola virtual**; democratiza a educação |
| **Pró-Vida** | Qualidade de vida: saúde biopsicossocial, ocupacional, segurança do trabalho, prevenção do suicídio |
| **Sinaped** | Acompanhamento e **avaliação** das políticas |
| **Sinesp** | Dados e **informações** |

**Pró-Vida: prevenção em três níveis (art. 42-A)**
- **Primária:** todos os profissionais (convívio, palestras, saúde mental na formação, espaços de escuta).
- **Secundária:** quem já está em risco (álcool e drogas, acompanhamento psicológico, inclusive após ocorrências traumáticas).
- **Terciária:** quem comunicou ideação suicida ou tem histórico de violência autoprovocada (aproximação da família, combate ao isolamento, **restrição do porte e uso de arma de fogo**, acompanhamento psicológico e médico).

> **Macete:** **andragogia** = educação de **adultos**. **Atendimento não compulsório** é diretriz do Pró-Vida.
"""
S[5]="""## 5. Na rotina do guarda

- **Dados da ocorrência:** o boletim da guarda alimenta estatísticas estaduais e o Sinesp; registro incompleto prejudica o Município (art. 37).
- **Avaliação da guarda:** como atividade de patrulhamento preventivo, é medida pela incidência de infrações em determinada área (art. 12, III).
- **Formação:** cursos da Rede EaD-Senasp são acessíveis a guardas municipais, que integram o Susp.
- **Saúde mental:** depois de ocorrência traumática, a lei prevê acompanhamento psicológico (art. 42-A, § 5º, V).
- **Identidade funcional:** tem fé pública e validade nacional, conforme padrão federal (art. 43).
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Periodicidade das metas | Anual |
| Conferências de segurança pública | A cada 5 anos |
| Quem integra o Sinesp | Todos os entes federados |
| Sanção por não fornecer dados ao Sinesp | Pode não receber recursos nem celebrar parcerias com a União |
| Omissão do agente no fornecimento | Responsabilidade administrativa |
| Matriz curricular | Direitos humanos e andragogia |
| Renaesp x Rede EaD | Ensino superior x escola virtual |
| Sinaped x Sinesp | Avaliação de políticas x dados e informações |
| Atendimento do Pró-Vida | Não compulsório |
| Identidade funcional | Fé pública e validade nacional |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Arts. 11 e 12 | Metas anuais; indicadores por atividade |
| Arts. 13 e 14 | Gestão federal: aparelhamento, Sinesp, intercâmbio com guardas, inteligência |
| Art. 24 | Diretrizes dos planos: articulação, participação social, escola, egressos, plano diretor |
| Arts. 26 e 27 | Sinaped e relatório de avaliação enviado aos Conselhos |
| Arts. 36 e 37 | Sinesp: objetivos; todos os entes; sanção e responsabilidade |
| Arts. 38 a 41 | Sievap: matriz curricular, Renaesp, Rede EaD, Pró-Vida |
| Arts. 42 e 42-A | Pró-Vida e prevenção do suicídio em três níveis |
| Art. 43 | Identidade funcional padronizada, fé pública, validade nacional |
| Art. 45 | Conferências a cada 5 anos |
"""
QR=[("Questão 1","Nos termos da Lei 13.675/2018, deverão ser realizadas conferências para debater as diretrizes dos planos de segurança pública e defesa social a cada",["5 anos.","2 anos.","10 anos.","4 anos.","ano."],0,"Art. 45."),
("Questão 2","Integram o Sinesp",["todos os entes federados, por intermédio de órgãos criados ou designados para esse fim.","apenas a União.","apenas a União e os Estados.","apenas as polícias federais.","apenas os Municípios com guarda."],1,"Art. 37."),
("Questão 3","As atividades de polícia ostensiva e de preservação da ordem pública serão aferidas, entre outros fatores, pela",["maior ou menor incidência de infrações penais e administrativas em determinada área.","quantidade de multas aplicadas.","número de viaturas.","quantidade de prisões em flagrante apenas.","arrecadação de taxas."],2,"Art. 12, III."),
("Questão 4","A matriz curricular nacional é pautada",["nos direitos humanos, nos princípios da andragogia e nas teorias de construção do conhecimento.","exclusivamente na doutrina militar.","no treinamento de tiro.","na legislação de trânsito.","em critérios de antiguidade."],3,"Art. 39, § 1º.")]
t1="<strong>Os dados atrasados</strong><br><br>Um Município deixou de atualizar por meses seus registros de ocorrências no sistema nacional de informações de segurança pública e, depois, pediu recursos federais para equipar a guarda."
t2="<strong>Depois da ocorrência</strong><br><br>Uma guarda municipal participou do atendimento a um homicídio com várias vítimas e, nas semanas seguintes, passou a ter insônia e crises de ansiedade."
t3="<strong>A praça escura</strong><br><br>Moradores reclamaram de roubos frequentes em uma praça mal iluminada, e a Prefeitura passou a discutir a revisão do plano diretor e um projeto de iluminação."
tx={"susp3a":t1,"susp3b":t2,"susp3c":t3}
# n=1
q(1,"As metas de excelência previstas na Lei 13.675/2018 são fixadas",["anualmente.","mensalmente.","a cada 5 anos.","a cada 10 anos.","semestralmente."],"Arts. 11 e 25.")
q(1,"Sinesp é o sistema nacional de",["informações de segurança pública.","educação profissional.","avaliação de políticas.","qualidade de vida.","altos estudos."],"Art. 35 e seguintes.")
q(1,"Sievap é o Sistema Integrado de",["Educação e Valorização Profissional.","Estatística e Vigilância Policial.","Emergência e Vigilância.","Educação Viária e Pública.","Execução de Penas."],"Art. 38.")
q(1,"A Rede EaD-Senasp é uma escola",["virtual.","militar.","presencial obrigatória.","privada.","estadual."],"Art. 41.")
q(1,"O Pró-Vida é o programa nacional de",["qualidade de vida para profissionais de segurança pública.","proteção a vítimas.","proteção a testemunhas.","prevenção à violência doméstica.","prevenção a desastres."],"Art. 42.")
q(1,"O Pró-Vida produzirá diretrizes direcionadas à prevenção da violência autoprovocada e do",["suicídio.","furto.","tráfico.","roubo.","homicídio culposo."],"Art. 42-A.")
q(1,"Os documentos de identificação funcional dos profissionais de segurança pública terão fé pública e validade",["em todo o território nacional.","apenas no Estado.","apenas no Município.","apenas em serviço.","por um ano."],"Art. 43.")
q(1,"As conferências de segurança pública e defesa social devem ser realizadas a cada",["5 anos.","ano.","2 anos.","10 anos.","3 anos."],"Art. 45.")
q(1,"Integram o Sinesp",["todos os entes federados.","apenas a União.","apenas os Estados.","apenas as polícias civis.","apenas os Municípios."],"Art. 37.")
q(1,"A omissão no fornecimento das informações legais ao Sinesp implica responsabilidade",["administrativa do agente público.","penal da União.","civil do cidadão.","eleitoral.","nenhuma."],"Art. 37, § 4º.")
q(1,"A matriz curricular nacional é pautada nos direitos humanos e nos princípios da",["andragogia.","pedagogia infantil.","hierarquia militar.","economia.","engenharia."],"Art. 39, § 1º.")
q(1,"A Renaesp é integrada por instituições de ensino",["superior.","fundamental.","infantil.","técnico militar exclusivamente.","religiosas."],"Art. 40.")
q(1,"O Sinaped é o sistema de acompanhamento e",["avaliação das políticas de segurança pública.","arrecadação de multas.","registro de armas.","pagamento de servidores.","licenciamento de veículos."],"Art. 26.")
q(1,"Entre as ações do órgão gestor do Susp está efetivar o intercâmbio de experiências técnicas e operacionais entre os órgãos policiais e as",["guardas municipais.","empresas privadas.","escolas particulares.","igrejas.","clubes."],"Art. 13, III.")
q(1,"A aferição das atividades do sistema prisional considera, entre outros, o índice de reiteração criminal dos",["egressos.","servidores.","advogados.","juízes.","visitantes."],"Art. 12, V, c.")
q(1,"Entre as diretrizes dos planos está fomentar estudos de planejamento urbano para que a prevenção da criminalidade faça parte do",["plano diretor das cidades.","orçamento federal.","código penal.","regimento da Câmara.","calendário escolar."],"Art. 24, XII.")
q(1,"O Sinesp adota padrões de integridade, disponibilidade, confidencialidade, confiabilidade e",["tempestividade.","publicidade irrestrita.","gratuidade.","anonimato.","exclusividade."],"Art. 36, parágrafo único.")
q(1,"No texto dos dados atrasados, o Município que deixou de atualizar dados no Sinesp",["poderá não receber recursos nem celebrar parcerias com a União.","receberá recursos em dobro.","será dissolvido.","perderá a guarda municipal.","ficará isento de fornecer dados."],"Art. 37, § 2º.","susp3a")
q(1,"No texto depois da ocorrência, o programa federal voltado à saúde da guarda é o",["Pró-Vida.","Sinesp.","Renaesp.","Sinaped.","Funpen."],"Art. 42.","susp3b")
q(1,"No texto da praça escura, a medida de prevenção prevista entre as diretrizes dos planos é o reforço na",["iluminação pública.","arrecadação de tributos.","venda de imóveis.","fiscalização de trânsito apenas.","construção de presídios."],"Art. 24, XII.","susp3c")
# n=2
q(2,"As atividades de polícia judiciária serão aferidas, entre outros fatores, pelos índices de",["elucidação dos delitos.","multas aplicadas.","viaturas adquiridas.","horas extras.","denúncias anônimas."],"Art. 12, I.")
q(2,"As atividades periciais serão aferidas mediante critérios técnicos, considerando os laudos periciais e o resultado na produção qualificada das",["provas relevantes à instrução criminal.","multas de trânsito.","certidões de nascimento.","licenças ambientais.","escalas de serviço."],"Art. 12, II.")
q(2,"As atividades dos corpos de bombeiros militares serão aferidas, entre outros, pelos índices de",["tempo de resposta aos desastres.","prisões efetuadas.","multas aplicadas.","inquéritos concluídos.","armas apreendidas."],"Art. 12, IV.")
q(2,"Na polícia judiciária, a aferição deve distinguir as autorias definidas em razão de prisão em flagrante das autorias resultantes de",["diligências investigatórias.","denúncias anônimas.","confissões.","delações.","pedidos da vítima."],"Art. 12, § 2º.")
q(2,"A aferição de metas considera aspectos relativos à estrutura de trabalho físico, de equipamentos e de",["efetivo.","propaganda.","eleições.","imóveis particulares.","horário de verão."],"Art. 12, § 1º.")
q(2,"Entre as ações do órgão gestor do Susp está valorizar a autonomia técnica, científica e funcional dos institutos oficiais de criminalística, medicina legal e",["identificação.","trânsito.","engenharia.","educação.","comércio."],"Art. 13, IV.")
q(2,"Entre as ações do órgão gestor está coordenar as atividades de inteligência da segurança pública integradas ao",["Sisbin.","Sinarm.","Sigma.","Renach.","Sinaped."],"Art. 13, VII.")
q(2,"Entre as diretrizes dos planos está incentivar a inclusão das disciplinas de prevenção da violência e de prevenção de desastres nos",["conteúdos curriculares dos diversos níveis de ensino.","contratos de trabalho.","editais de licitação.","programas de televisão.","regulamentos de condomínio."],"Art. 24, V.")
q(2,"Entre as diretrizes dos planos está ampliar as alternativas de inserção econômica e social dos",["egressos do sistema prisional.","turistas.","empresários.","estudantes estrangeiros.","aposentados."],"Art. 24, VI.")
q(2,"O relatório da avaliação do Plano Nacional deve ser encaminhado aos respectivos",["Conselhos de Segurança Pública e Defesa Social.","Tribunais de Contas apenas.","partidos políticos.","sindicatos.","órgãos de imprensa."],"Art. 27, § 2º.")
q(2,"O Sinesp tem por objetivo promover a integração das redes e sistemas de dados de segurança pública, criminais, do sistema prisional e sobre",["drogas.","trânsito apenas.","educação.","turismo.","agricultura."],"Art. 36, III.")
q(2,"O Sinesp também produzirá dados sobre transtornos mentais e comportamento suicida dos",["profissionais de segurança pública e defesa social.","presos provisórios.","adolescentes infratores.","vigilantes privados.","estudantes."],"Art. 36, IX.")
q(2,"O Sinesp produzirá dados sobre a vitimização dos profissionais de segurança pública, inclusive",["fora do horário de trabalho.","apenas em serviço.","apenas em operações federais.","apenas em rodovias.","apenas em presídios."],"Art. 36, VI.")
q(2,"Compõem o Sievap, entre outros: matriz curricular nacional, Renaesp, Rede EaD-Senasp e o programa nacional de",["qualidade de vida para segurança pública e defesa social.","armamento.","combate ao tráfico.","proteção de fronteiras.","defesa civil."],"Art. 38, § 1º.")
q(2,"A matriz curricular deve ser observada nas atividades formativas de ingresso, aperfeiçoamento, atualização, capacitação e especialização, nas modalidades",["presencial e a distância.","apenas presencial.","apenas a distância.","apenas militar.","apenas universitária."],"Art. 39.")
q(2,"Entre os objetivos da Renaesp está difundir a cidadania, os direitos humanos e a educação para a",["paz.","guerra.","competição.","disciplina militar.","obediência."],"Art. 40, IV.")
q(2,"O Pró-Vida desenvolverá ações direcionadas à saúde biopsicossocial, à saúde ocupacional e à",["segurança do trabalho.","arrecadação fiscal.","política partidária.","propaganda institucional.","logística de armas."],"Art. 42, § 1º.")
q(2,"No texto dos dados atrasados, além da restrição de recursos, o agente público omisso responde",["administrativamente.","penalmente, com prisão.","apenas civilmente.","eleitoralmente.","de nenhuma forma."],"Art. 37, § 4º.","susp3a")
q(2,"No texto depois da ocorrência, a lei prevê, na prevenção secundária, acompanhamento psicológico para profissionais que tenham se envolvido em",["ocorrência de risco e em experiências traumáticas.","processos de promoção.","férias prolongadas.","atividades administrativas.","eventos esportivos."],"Art. 42-A, § 5º, V.","susp3b")
q(2,"No texto da praça escura, avaliar a atividade de patrulhamento preventivo na área considera a",["incidência de infrações penais e administrativas naquela área.","quantidade de multas.","arrecadação do IPTU.","quantidade de viaturas.","número de eventos culturais."],"Art. 12, III.","susp3c")
# n=3
q(3,"Assinale a alternativa correta.",["O Sinaped acompanha e avalia políticas; o Sinesp reúne dados e informações; o Sievap trata da educação e valorização profissional.","O Sinesp avalia políticas; o Sinaped reúne dados.","O Sievap reúne dados criminais.","A Renaesp é escola virtual.","A Rede EaD integra apenas universidades."],"Arts. 26, 35, 38, 40 e 41.")
q(3,"Considere. I. As conferências de segurança pública ocorrem a cada 5 anos. II. As metas de excelência são fixadas anualmente. III. A identidade funcional padronizada vale apenas no Estado de origem. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Arts. 11, 43 e 45.")
q(3,"Assinale a INCORRETA sobre o Pró-Vida.",["O atendimento é compulsório para todos os profissionais.","Produz diretrizes de prevenção da violência autoprovocada e do suicídio.","Desenvolve ações de saúde biopsicossocial.","Publica anualmente dados sobre saúde e vitimização dos profissionais.","Tem implementação pactuada entre União, Estados, DF e Municípios."],"Art. 42-A, § 2º, VI: atendimento não compulsório.")
q(3,"A prevenção primária do suicídio entre profissionais de segurança destina-se a",["todos os profissionais da segurança pública e defesa social.","apenas quem tentou suicídio.","apenas os aposentados.","apenas a família.","apenas os comandantes."],"Art. 42-A, § 4º.")
q(3,"A prevenção secundária destina-se aos profissionais",["que já se encontram em situação de risco de violência autoprovocada.","recém-ingressos.","aposentados.","de outros países.","que nunca apresentaram risco."],"Art. 42-A, § 5º.")
q(3,"Entre as diretrizes do art. 42-A, § 2º, para a prevenção do suicídio está o",["atendimento não compulsório e o respeito à intimidade.","afastamento obrigatório de todos.","atendimento público com exposição do caso.","atendimento apenas por chefia.","desligamento imediato."],"Art. 42-A, § 2º, III e VI.")
q(3,"Os casos de ideação e de tentativa de suicídio de profissionais de segurança serão notificados no Sistema Nacional de Vigilância Epidemiológica,",["resguardada a identidade do profissional.","com divulgação do nome.","apenas se houver morte.","apenas com autorização judicial.","com publicação em diário oficial."],"Art. 42-A, § 5º, III.")
q(3,"O Pró-Vida publicará anualmente as informações dos incisos V a IX do art. 36, que tratam de",["qualidade de vida, vitimização, deficiência, dependência química e saúde mental dos profissionais.","estatísticas de multas.","número de presos.","orçamento dos Estados.","licitações."],"Art. 42, § 2º.")
q(3,"A implementação das ações do Pró-Vida será pactuada, nos termos dos planos de segurança pública, entre",["a União, os Estados, o Distrito Federal e os Municípios.","apenas a União e os Estados.","apenas a União.","apenas os Municípios.","as empresas privadas."],"Art. 42, § 4º.")
q(3,"A Lei 13.675/2018 autoriza o órgão federal a celebrar convênios com o Poder Judiciário e o Ministério Público para compatibilização de sistemas, desde que o objeto fundamental seja",["a prevenção e a repressão da violência.","a arrecadação de tributos.","a propaganda institucional.","a contratação de pessoal.","o comércio de armas."],"Art. 37, § 3º.")
q(3,"Os resultados da avaliação das políticas serão utilizados, entre outros fins, para melhorar e ampliar a capacitação dos",["operadores do Susp.","juízes eleitorais.","empresários.","parlamentares.","advogados."],"Art. 27, § 1º, VI.")
q(3,"O Sinaped visa garantir, entre outros, a verificação da eficácia da utilização dos",["recursos públicos.","recursos privados.","recursos de partidos.","tributos municipais apenas.","prêmios de loteria."],"Art. 26, III, b.")
q(3,"A Lei 13.675/2018 entrou em vigor após decorridos",["30 dias de sua publicação oficial.","90 dias.","180 dias.","1 ano.","na data da publicação."],"Art. 50.")
q(3,"No art. 12, a eficiência do sistema prisional é aferida, entre outros fatores, pela relação entre o número de presos e a quantidade de",["vagas ofertadas.","agentes penitenciários.","visitas.","processos.","advogados."],"Art. 12, V, b.")
q(3,"Os integrantes do Susp fixam metas anuais com finalidades como apoiar e promover o sistema de saúde e o sistema",["habitacional para os profissionais de segurança pública.","eleitoral.","bancário.","tributário.","de transportes urbanos."],"Art. 25, V e VI.")
q(3,"No texto dos dados atrasados, a regra que relaciona dados no Sinesp e recursos federais está no art. 37, § 2º, e alcança programas de segurança pública e do",["sistema prisional.","sistema eleitoral.","sistema de trânsito.","sistema tributário.","sistema de saúde."],"Art. 37, § 2º.","susp3a")
q(3,"No texto depois da ocorrência, as ações do Pró-Vida para a guarda devem observar, entre outras diretrizes,",["discrição e respeito à intimidade nos atendimentos.","exposição pública do caso.","afastamento compulsório.","punição disciplinar.","transferência obrigatória."],"Art. 42-A, § 2º, III.","susp3b")
q(3,"No texto depois da ocorrência, o caso da guarda se enquadra na prevenção",["secundária.","primária.","terciária.","quaternária.","judicial."],"Art. 42-A, § 5º.","susp3b")
q(3,"No texto da praça escura, a diretriz do art. 24, XII, também prevê a verificação de",["pessoas e de famílias em situação de risco social e criminal.","imóveis abandonados para venda.","empresas em débito.","veículos licenciados.","escolas particulares."],"Art. 24, XII.","susp3c")
q(3,"No texto da praça escura, outra diretriz útil dos planos é viabilizar ampla participação",["social na formulação, implementação e avaliação das políticas.","apenas militar.","apenas do Judiciário.","apenas de empresas.","apenas federal."],"Art. 24, III.","susp3c")
from collections import Counter; c=Counter(x[0] for x in Q); print(c); assert c=={1:20,2:20,3:20}
code,svg=mapa("Lei 13.675/2018: metas, dados e valorização",[
 ("met","Metas (arts. 11 e 12)",["anuais","indicadores por atividade","ostensiva: incidência na área"],"seção 1"),
 ("pla","Planos (art. 24)",["articulação e participação social","escola e egressos","plano diretor e iluminação"],"seção 1"),
 ("sin","Sinesp (arts. 36 e 37)",["todos os entes","sem dados, sem recursos","omissão: responsabilidade"],"seção 2"),
 ("sie","Sievap (arts. 38 a 41)",["matriz curricular","Renaesp","Rede EaD"],"seção 3"),
 ("pro","Pró-Vida (arts. 42 e 42-A)",["saúde e segurança do trabalho","prevenção do suicídio","não compulsório"],"seção 3"),
 ("fin","Finais (arts. 43 e 45)",["identidade com fé pública","validade nacional","conferências a cada 5 anos"],"seção 3")],
 "Na prova: metas anuais, conferências a cada 5 anos, Sinesp com todos os entes")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha trata das metas, dos planos e dos dados; a segunda, da formação e da valorização do profissional.","Fontes: Edital 02/2026, Anexo I; Lei 13.675/2018, consolidação da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("susp-3","Lei 13.675/2018: metas, Sinesp, Sievap e Pró-Vida",Q,list(tx),
 cobertura=["Arts. 11 a 14, 24 a 27, 36 a 43, 45 e 50. Com susp-1 e susp-2, a Lei 13.675/2018 fica coberta, salvo arts. 17, 18, 28 a 33 (resumidos) e 46 a 49 (alterações de outras leis)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin); a lei ainda cita o 'Ministério Extraordinário da Segurança Pública'; hoje a pasta é o Ministério da Justiça e Segurança Pública.","Casos susp3a, susp3b e susp3c fictícios."],
 fontes_conferidas=["Lei 13.675/2018, arts. 11 a 50: texto da Câmara, copiado por programa."])
gravar("susp-3",aula_html,banco("susp-3",Q),tx)
