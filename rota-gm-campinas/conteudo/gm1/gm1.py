import sys,pickle; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','..','gerador')); from aulas import *
LEAD="A Lei 13.022/2014, o Estatuto Geral das Guardas Municipais, é a norma que define o que a guarda é e o que ela pode fazer em qualquer cidade do país. Esta primeira parte cobre os arts. 1º a 5º: natureza, princípios e competências. A Vunesp cobra quase sempre a letra da lei, trocando uma palavra para ver se o candidato percebe."
S={}
S[1]="""## 1. O que a lei faz

A Constituição diz, no art. 144, § 8º, que os Municípios podem constituir guardas municipais destinadas à proteção de seus bens, serviços e instalações, conforme dispuser a lei. A Lei 13.022/2014 é essa lei: ela traz as **normas gerais** que valem para todas as guardas do país.

[[LEI|art. 1º|Esta Lei institui normas gerais para as guardas municipais, disciplinando o § 8º do art. 144 da Constituição Federal.]]

“Normas gerais” quer dizer que a lei federal fixa o piso comum. Cada Município, ao criar sua guarda, completa os detalhes por lei municipal, mas não pode contrariar o Estatuto.
"""
S[2]="""## 2. Natureza: civil, uniformizada e preventiva

[[LEI|art. 2º|Incumbe às guardas municipais, instituições de caráter civil, uniformizadas e armadas conforme previsto em lei, a função de proteção municipal preventiva, ressalvadas as competências da União, dos Estados e do Distrito Federal.]]

Quatro palavras deste artigo aparecem em quase toda prova:

1. **Civil.** A guarda não é instituição militar. Por isso, mais adiante, a lei proíbe regulamento disciplinar militar e denominações militares (arts. 14 e 19, no posto gm-2).
2. **Uniformizadas.** O uniforme é característica da instituição.
3. **Armadas conforme previsto em lei.** O porte de arma não vem deste artigo; depende do que a lei específica autorizar.
4. **Proteção municipal preventiva.** A função central é prevenir, no âmbito do Município, sem invadir o que cabe à União, aos Estados e ao Distrito Federal.

[[NOTA: A Vunesp gosta de trocar “civil” por “militar” e “preventiva” por “repressiva” ou “ostensiva”. A letra da lei diz caráter civil e proteção municipal preventiva.]]
"""
S[3]="""## 3. Princípios mínimos de atuação

[[LEI|art. 3º, caput|São princípios mínimos de atuação das guardas municipais:]]

1. proteção dos direitos humanos fundamentais, do exercício da cidadania e das liberdades públicas;
2. preservação da vida, redução do sofrimento e diminuição das perdas;
3. patrulhamento preventivo;
4. compromisso com a evolução social da comunidade; e
5. uso progressivo da força.

A palavra “mínimos” importa: a lei municipal pode acrescentar princípios, mas não retirar estes cinco. E repare no último: o uso da força é **progressivo**, ou seja, proporcional à resistência encontrada, começando pela simples presença e pela verbalização. A lei não fala em uso “máximo”, “imediato” ou “irrestrito” da força.
"""
S[4]="""## 4. Competência geral

[[LEI|art. 4º, caput|É competência geral das guardas municipais a proteção de bens, serviços, logradouros públicos municipais e instalações do Município.]]

[[LEI|art. 4º, parágrafo único|Os bens mencionados no caput abrangem os de uso comum, os de uso especial e os dominiais.]]

As três espécies de bens públicos vêm do Código Civil e costumam aparecer com exemplos:

- **Uso comum do povo:** os que qualquer pessoa usa livremente, como praças, ruas, parques e calçadas.
- **Uso especial:** os destinados a um serviço público, como o prédio da prefeitura, a escola municipal e o posto de saúde.
- **Dominiais:** os que pertencem ao Município sem destinação pública específica, como um terreno vago ou um imóvel desocupado da prefeitura.

Como a lei protege as três espécies, uma alternativa que limite a proteção a “bens de uso especial” ou exclua os dominiais está errada.
"""
S[5]="""## 5. Competências específicas

[[LEI|art. 5º, caput|São competências específicas das guardas municipais, respeitadas as competências dos órgãos federais e estaduais:]]

O art. 5º tem dezoito incisos. Decorar a ordem não ajuda; ajuda saber agrupá-los pelo que a guarda faz.

**Proteger e prevenir.** Zelar pelos bens, equipamentos e prédios públicos do Município (I); prevenir e inibir, pela presença e vigilância, bem como coibir, infrações penais ou administrativas e atos infracionais que atentem contra os bens, serviços e instalações municipais (II); atuar preventiva e permanentemente no território do Município, para a proteção sistêmica da população que utiliza os bens, serviços e instalações municipais (III); proteger o patrimônio ecológico, histórico, cultural, arquitetônico e ambiental do Município, inclusive com ações preventivas e educativas (VII).

**Integrar-se a outros órgãos.** Colaborar, de forma integrada com os órgãos de segurança pública, em ações conjuntas que contribuam com a paz social (IV); cooperar com os demais órgãos de defesa civil (VIII); firmar parcerias com órgãos estaduais, da União ou de Municípios vizinhos, por convênios ou consórcios (X); articular-se com os órgãos municipais de políticas sociais (XI); integrar-se com os demais órgãos de poder de polícia administrativa, para o ordenamento urbano (XII); desenvolver ações de prevenção primária à violência (XVI).

**Trânsito.** Exercer as competências de trânsito que lhes forem conferidas, nas vias e logradouros municipais, nos termos do Código de Trânsito Brasileiro, ou de forma concorrente, mediante convênio com órgão de trânsito estadual ou municipal (VI).

**Comunidade e cidade.** Interagir com a sociedade civil para discutir soluções e projetos locais de segurança (IX); contribuir no estudo de impacto na segurança local, conforme o plano diretor, quando houver construção de empreendimentos de grande porte (XV).

**Atuar na ocorrência.** Três incisos descrevem a guarda agindo diretamente:

[[LEI|art. 5º, V|colaborar com a pacificação de conflitos que seus integrantes presenciarem, atentando para o respeito aos direitos fundamentais das pessoas;]]

[[LEI|art. 5º, XIII|garantir o atendimento de ocorrências emergenciais, ou prestá-lo direta e imediatamente quando deparar-se com elas;]]

[[LEI|art. 5º, XIV|encaminhar ao delegado de polícia, diante de flagrante delito, o autor da infração, preservando o local do crime, quando possível e sempre que necessário;]]

Completam a lista o auxílio na segurança de grandes eventos e na proteção de autoridades e dignatários (XVII) e a atuação preventiva na segurança escolar, zelando pelo entorno e participando de ações educativas com o corpo discente e docente das unidades de ensino municipal (XVIII).

Por fim, o parágrafo único trata do encontro com as polícias:

[[LEI|art. 5º, parágrafo único|No exercício de suas competências, a guarda municipal poderá colaborar ou atuar conjuntamente com órgãos de segurança pública da União, dos Estados e do Distrito Federal ou de congêneres de Municípios vizinhos e, nas hipóteses previstas nos incisos XIII e XIV deste artigo, diante do comparecimento de órgão descrito nos incisos do caput do art. 144 da Constituição Federal, deverá a guarda municipal prestar todo o apoio à continuidade do atendimento.]]

Em outras palavras: na ocorrência emergencial e no flagrante, a guarda age primeiro; quando a polícia chega, a guarda passa a dar apoio para o atendimento continuar.

[[NOTA: No flagrante, o autor é encaminhado ao delegado de polícia, não ao juiz nem ao Ministério Público. E o local do crime é preservado “quando possível e sempre que necessário”, não em qualquer caso.]]
"""
S[6]="""## 6. O que o STF já decidiu

O Estatuto é lido hoje junto com três decisões do Supremo Tribunal Federal, que a prova pode cobrar como atualidade:

1. **ADPF 995 (2023):** reconheceu que as guardas municipais integram o Sistema de Segurança Pública. Por isso o art. 4º do Estatuto traz, na versão consolidada, a remissão a essa ação.
2. **Tema 656 da repercussão geral (fevereiro de 2025):** é constitucional que as guardas exerçam ações de segurança urbana, inclusive policiamento ostensivo e comunitário, respeitadas as atribuições dos demais órgãos de segurança pública e excluída qualquer atividade de polícia judiciária. Elas ficam sujeitas ao controle externo da atividade policial pelo Ministério Público, e as leis municipais devem observar as normas gerais fixadas pelo Congresso Nacional.
3. **ADPF 1214 (abril de 2026):** os Municípios não podem trocar o nome “Guarda Municipal” por “Polícia Municipal” ou denominação semelhante. O tema volta no art. 22, no posto gm-2.

Em síntese: a guarda pode fazer policiamento preventivo e ostensivo, mas não investiga crimes nem conduz inquérito, que é atividade de polícia judiciária.
"""
S[8]="""## 8. Na rotina do guarda

- **Flagrante na praça:** o guarda conduz o autor ao delegado de polícia e, quando possível e necessário, preserva o local até a chegada da perícia.
- **Acidente com vítima:** a guarda presta o atendimento direta e imediatamente; quando o Samu ou a polícia chegam, passa a apoiar a continuidade.
- **Briga presenciada:** a atuação é colaborar com a pacificação, respeitando os direitos fundamentais dos envolvidos.
- **Entorno da escola:** ronda preventiva e participação em ações educativas com alunos e professores.
- **Terreno vago da prefeitura invadido:** também é bem público (dominial) e está sob a proteção da guarda.
"""
S[9]="""## 9. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| “Instituição de caráter militar” | caráter civil |
| “Proteção municipal repressiva” | proteção municipal preventiva |
| “Uso proporcional da força” ou “uso imediato da força” | a lei diz uso progressivo da força |
| Bens só de uso especial | uso comum, uso especial e dominiais |
| Autor do flagrante levado ao juiz ou ao Ministério Público | ao delegado de polícia |
| Local do crime preservado “sempre” | quando possível e sempre que necessário |
| Guarda assume a ocorrência depois que a polícia chega | presta todo o apoio à continuidade do atendimento |
| Guarda conduz inquérito | atividade de polícia judiciária está excluída |
| Princípios “taxativos” | são princípios mínimos |
"""
S[10]="""## 10. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | normas gerais; disciplina o art. 144, § 8º, da CF |
| Art. 2º | caráter civil; uniformizadas; armadas conforme lei; proteção municipal preventiva |
| Art. 3º | cinco princípios mínimos; uso progressivo da força |
| Art. 4º | bens, serviços, logradouros e instalações; bens de uso comum, especial e dominiais |
| Art. 5º, XIII | ocorrência emergencial: garantir ou prestar direta e imediatamente |
| Art. 5º, XIV | flagrante: autor ao delegado; preservar o local quando possível e necessário |
| Art. 5º, VI | trânsito nos termos do CTB ou por convênio |
| Art. 5º, XVIII | segurança escolar preventiva e ações educativas |
| Art. 5º, p. único | polícia chegou: apoio à continuidade |
| STF | integra a segurança pública; policiamento ostensivo sim, polícia judiciária não; nome “Guarda Municipal” |
"""
QR=[("Questão 1","De acordo com a Lei 13.022/2014, as guardas municipais são instituições de caráter",["civil, uniformizadas e armadas conforme previsto em lei, com função de proteção municipal preventiva.","militar, uniformizadas e armadas, com função de proteção municipal repressiva.","civil, não uniformizadas, com função exclusiva de proteção do patrimônio.","militar, auxiliares da polícia militar, com função de policiamento ostensivo estadual.","civil, desarmadas, com função de fiscalização de posturas municipais."],2,"Art. 2º: caráter civil, uniformizadas, armadas conforme previsto em lei, proteção municipal preventiva."),
("Questão 2","Constitui princípio mínimo de atuação das guardas municipais, nos termos da lei,",["o uso progressivo da força.","o uso imediato da força.","o patrulhamento repressivo.","a subordinação à polícia militar.","a investigação de infrações penais."],0,"Art. 3º, V. O patrulhamento é preventivo (inciso III)."),
("Questão 3","Diante de flagrante delito, compete à guarda municipal encaminhar o autor da infração",["ao delegado de polícia, preservando o local do crime, quando possível e sempre que necessário.","ao juiz de plantão, preservando o local do crime em qualquer caso.","ao Ministério Público, sem necessidade de preservar o local.","ao comandante da guarda, que decidirá sobre a lavratura do flagrante.","à polícia militar, que fará o registro e a investigação."],4,"Art. 5º, XIV."),
("Questão 4","Os bens protegidos pela guarda municipal, conforme o parágrafo único do art. 4º, abrangem",["os de uso comum, os de uso especial e os dominiais.","apenas os de uso especial.","apenas os de uso comum do povo.","os de uso comum e os de uso especial, excluídos os dominiais.","os bens particulares situados no Município."],1,"Art. 4º, parágrafo único.")]
QRF=qr_md(QR,7)
Q=[]
def q(n,e,a,c,tx=None): Q.append((n,e,a,c,tx))
# FÁCEIS
q(1,"A Lei 13.022/2014 institui normas gerais para as guardas municipais, disciplinando o",["§ 8º do art. 144 da Constituição Federal.","§ 4º do art. 144 da Constituição Federal.","art. 30 da Constituição Federal.","art. 5º da Constituição Federal.","§ 7º do art. 144 da Constituição Federal."],"Art. 1º.")
q(1,"Segundo a Lei 13.022/2014, as guardas municipais são instituições de caráter",["civil.","militar.","paramilitar.","policial militar.","auxiliar do Exército."],"Art. 2º.")
q(1,"De acordo com o art. 2º da Lei 13.022/2014, incumbe às guardas municipais a função de proteção municipal",["preventiva.","repressiva.","judiciária.","investigativa.","exclusivamente patrimonial."],"Art. 2º: proteção municipal preventiva.")
q(1,"As guardas municipais são, nos termos da lei, uniformizadas e armadas",["conforme previsto em lei.","em qualquer caso, por determinação do prefeito.","somente com armas não letais.","somente em Municípios com mais de 500 mil habitantes.","apenas durante grandes eventos."],"Art. 2º: armadas conforme previsto em lei.")
q(1,"É princípio mínimo de atuação das guardas municipais o",["patrulhamento preventivo.","patrulhamento repressivo.","policiamento judiciário.","uso irrestrito da força.","controle de fronteiras."],"Art. 3º, III.")
q(1,"Entre os princípios mínimos de atuação, a lei prevê o uso",["progressivo da força.","imediato da força.","máximo da força.","exclusivo de armas de fogo.","preventivo de armas letais."],"Art. 3º, V.")
q(1,"Assinale o princípio mínimo de atuação previsto no art. 3º da Lei 13.022/2014.",["Preservação da vida, redução do sofrimento e diminuição das perdas.","Hierarquia e disciplina militares.","Primazia do interesse arrecadatório do Município.","Repressão imediata de qualquer infração.","Sigilo absoluto das ações."],"Art. 3º, II.")
q(1,"É competência geral das guardas municipais a proteção de",["bens, serviços, logradouros públicos municipais e instalações do Município.","bens particulares e estabelecimentos comerciais.","rodovias federais e estaduais.","presídios estaduais.","fronteiras e portos."],"Art. 4º.")
q(1,"Uma praça pública é exemplo de bem de",["uso comum do povo.","uso especial.","dominial.","propriedade privada.","uso exclusivo da guarda."],"Bens de uso comum podem ser usados por todos livremente.")
q(1,"O prédio de uma escola municipal é exemplo de bem de",["uso especial.","uso comum do povo.","dominial.","propriedade particular.","uso restrito da União."],"Bem destinado a um serviço público: uso especial.")
q(1,"Um terreno vago pertencente ao Município, sem destinação pública, é bem",["dominial.","de uso comum do povo.","de uso especial.","particular.","da União."],"Dominiais são bens do Município sem destinação pública específica.")
q(1,"Compete à guarda municipal zelar pelos",["bens, equipamentos e prédios públicos do Município.","imóveis particulares do Município.","presídios estaduais.","quartéis da polícia militar.","prédios do Poder Judiciário estadual."],"Art. 5º, I.")
q(1,"Diante de flagrante delito, a guarda municipal deve encaminhar o autor da infração",["ao delegado de polícia.","ao juiz de direito.","ao promotor de justiça.","ao prefeito.","ao comandante da polícia militar."],"Art. 5º, XIV.")
q(1,"Compete à guarda municipal auxiliar na segurança de",["grandes eventos e na proteção de autoridades e dignatários.","instituições financeiras privadas.","presídios federais.","embaixadas estrangeiras, com exclusividade.","fronteiras internacionais."],"Art. 5º, XVII.")
q(1,"Na segurança escolar, a guarda municipal deve atuar mediante ações",["preventivas, zelando pelo entorno e participando de ações educativas.","repressivas dentro das salas de aula.","de revista diária de todos os alunos.","exclusivamente nas escolas estaduais.","de fiscalização pedagógica dos professores."],"Art. 5º, XVIII.")
q(1,"As competências de trânsito da guarda municipal são exercidas",["nas vias e logradouros municipais, nos termos do Código de Trânsito Brasileiro, ou de forma concorrente, mediante convênio.","nas rodovias federais, por delegação da Polícia Rodoviária Federal.","em todas as vias do Estado, sem necessidade de convênio.","somente em dias de grandes eventos.","apenas mediante autorização do Ministério Público."],"Art. 5º, VI.")
q(1,"Cabe à guarda municipal cooperar com os demais órgãos de",["defesa civil em suas atividades.","polícia judiciária na condução de inquéritos.","inteligência das Forças Armadas.","fiscalização tributária federal.","administração penitenciária."],"Art. 5º, VIII.")
q(1,"A guarda municipal pode proteger o patrimônio",["ecológico, histórico, cultural, arquitetônico e ambiental do Município.","privado de empresas instaladas no Município.","federal localizado no Município, com exclusividade.","artístico estrangeiro.","exclusivamente arquitetônico."],"Art. 5º, VII.")
q(1,"A Lei 13.022/2014 é conhecida como",["Estatuto Geral das Guardas Municipais.","Estatuto do Desarmamento.","Lei Orgânica das Polícias Militares.","Código de Trânsito Brasileiro.","Lei do Sistema Único de Segurança Pública."],"Nome dado à lei.")
q(1,"No caso narrado, ao encontrar o autor do furto em flagrante, a conduta correta da equipe, segundo a lei, foi",["encaminhá-lo ao delegado de polícia.","levá-lo à prefeitura para registro.","liberá-lo após identificar a vítima.","encaminhá-lo diretamente ao fórum.","mantê-lo na base da guarda até o dia seguinte."],"Art. 5º, XIV.","tg1")
# MÉDIAS
q(2,"Assinale a alternativa que reproduz corretamente o art. 2º da Lei 13.022/2014.",["Incumbe às guardas municipais, instituições de caráter civil, uniformizadas e armadas conforme previsto em lei, a função de proteção municipal preventiva, ressalvadas as competências da União, dos Estados e do Distrito Federal.","Incumbe às guardas municipais, instituições de caráter militar, a função de policiamento ostensivo estadual.","Incumbe às guardas municipais, instituições de caráter civil, desarmadas, a função de proteção patrimonial exclusiva.","Incumbe às guardas municipais, instituições de caráter civil, a função de polícia judiciária no Município.","Incumbe às guardas municipais, instituições auxiliares da polícia militar, a função de proteção preventiva estadual."],"Texto literal do art. 2º.")
q(2,"Os princípios previstos no art. 3º da Lei 13.022/2014 são",["mínimos, podendo a lei municipal acrescentar outros.","taxativos, não admitindo complementação.","facultativos, a critério do comandante.","aplicáveis apenas às guardas armadas.","exclusivos das guardas de capitais."],"O caput fala em princípios mínimos.")
q(2,"Assinale a alternativa que NÃO corresponde a princípio mínimo de atuação das guardas municipais.",["Hierarquia e disciplina militares.","Proteção dos direitos humanos fundamentais, do exercício da cidadania e das liberdades públicas.","Patrulhamento preventivo.","Compromisso com a evolução social da comunidade.","Uso progressivo da força."],"As guardas são civis; hierarquia militar não está no art. 3º.")
q(2,"Quanto às ocorrências emergenciais, compete à guarda municipal",["garantir o atendimento, ou prestá-lo direta e imediatamente quando deparar-se com elas.","apenas comunicá-las à polícia militar, sem prestar atendimento.","prestar atendimento somente quando solicitada pelo Corpo de Bombeiros.","atendê-las apenas se ocorrerem em bens municipais.","registrá-las para posterior encaminhamento ao Ministério Público."],"Art. 5º, XIII.")
q(2,"Na hipótese de flagrante delito, a preservação do local do crime pela guarda municipal deve ocorrer",["quando possível e sempre que necessário.","em todos os casos, sem exceção.","apenas por ordem judicial.","somente nos crimes contra a vida.","apenas quando solicitada pelo delegado."],"Art. 5º, XIV.")
q(2,"Nas hipóteses de ocorrência emergencial e de flagrante delito, diante do comparecimento de órgão do art. 144 da Constituição, a guarda municipal deverá",["prestar todo o apoio à continuidade do atendimento.","retirar-se imediatamente do local.","assumir o comando da ocorrência.","exigir autorização do prefeito para permanecer.","encerrar o atendimento e lavrar relatório."],"Art. 5º, parágrafo único.")
q(2,"Quanto aos conflitos que seus integrantes presenciarem, compete à guarda municipal",["colaborar com a pacificação, atentando para o respeito aos direitos fundamentais das pessoas.","intervir com o uso imediato da força.","apenas registrar o fato, sem intervir.","conduzir os envolvidos ao juiz de paz.","encaminhar o caso ao Conselho Tutelar em qualquer hipótese."],"Art. 5º, V.")
q(2,"A atuação da guarda municipal para prevenir e inibir infrações, prevista no art. 5º, II, se dá",["pela presença e vigilância, bem como pela coibição de infrações penais ou administrativas e atos infracionais que atentem contra bens, serviços e instalações municipais.","pela investigação de crimes e instauração de inquérito.","pela aplicação de penas administrativas aos infratores.","exclusivamente pela fiscalização de posturas.","pela prisão preventiva de suspeitos."],"Art. 5º, II.")
q(2,"Ao exercer competências de trânsito, a guarda municipal atua",["nas vias e logradouros municipais, nos termos do CTB, ou de forma concorrente, mediante convênio com órgão de trânsito estadual ou municipal.","em qualquer via do país, independentemente de convênio.","apenas nas rodovias estaduais.","somente em apoio à Polícia Rodoviária Federal.","exclusivamente na educação para o trânsito."],"Art. 5º, VI.")
q(2,"A guarda municipal pode firmar parcerias com órgãos estaduais e da União, ou de Municípios vizinhos, por meio de",["convênios ou consórcios.","decretos estaduais.","portarias do comandante.","contratos de terceirização.","acordos informais."],"Art. 5º, X.")
q(2,"Para o ordenamento urbano, a guarda municipal deve",["integrar-se com os demais órgãos de poder de polícia administrativa.","substituir os fiscais de posturas.","aplicar multas tributárias.","conceder alvarás de funcionamento.","fiscalizar obras federais."],"Art. 5º, XII.")
q(2,"Por ocasião da construção de empreendimentos de grande porte, a guarda municipal pode",["contribuir no estudo de impacto na segurança local, conforme o plano diretor municipal.","embargar a obra por conta própria.","conceder licença ambiental.","fiscalizar o recolhimento de tributos.","definir o plano diretor."],"Art. 5º, XV.")
q(2,"Compete à guarda municipal desenvolver ações de prevenção",["primária à violência, isoladamente ou em conjunto com outros órgãos.","exclusivamente terciária, após o crime.","apenas no interior das escolas.","somente com autorização do Ministério Público.","apenas em parceria com a iniciativa privada."],"Art. 5º, XVI.")
q(2,"Segundo o art. 5º, IX, a guarda municipal deve interagir com",["a sociedade civil para discussão de soluções de problemas e projetos locais voltados à melhoria das condições de segurança.","os partidos políticos para definir a escala.","as empresas de segurança privada para dividir competências.","os tribunais para fixar penas.","as Forças Armadas para o controle de fronteiras."],"Art. 5º, IX.")
q(2,"As competências específicas do art. 5º são exercidas",["respeitadas as competências dos órgãos federais e estaduais.","com preferência sobre as da polícia militar.","independentemente das competências federais.","apenas quando a polícia não puder atuar.","mediante autorização prévia do governador."],"Caput do art. 5º.")
q(2,"Segundo o STF, no julgamento do Tema 656 da repercussão geral (2025), as guardas municipais podem realizar",["policiamento ostensivo e comunitário, excluída qualquer atividade de polícia judiciária.","investigação criminal e instauração de inquérito.","policiamento ostensivo estadual, em substituição à polícia militar.","apenas a proteção de prédios públicos.","atividades de polícia judiciária, sob controle do delegado."],"Tese do Tema 656.")
q(2,"De acordo com a tese do Tema 656 do STF, as guardas municipais",["são submetidas ao controle externo da atividade policial pelo Ministério Público.","não se submetem a nenhum controle externo.","são controladas exclusivamente pelo Tribunal de Contas.","são controladas pela polícia militar.","são controladas pelo Poder Judiciário estadual."],"Tese do Tema 656.")
q(2,"Na ADPF 995, o STF reconheceu que as guardas municipais",["integram o Sistema de Segurança Pública.","são órgãos auxiliares das Forças Armadas.","não podem portar arma de fogo.","são instituições de caráter militar.","podem exercer funções de polícia judiciária."],"ADPF 995.")
q(2,"No caso narrado, ao se deparar com o motociclista ferido, a equipe agiu conforme a lei porque",["prestou o atendimento direta e imediatamente à ocorrência emergencial.","aguardou a chegada da polícia para agir.","limitou-se a registrar a ocorrência.","encaminhou a vítima ao delegado de polícia.","assumiu a investigação do acidente."],"Art. 5º, XIII.","tg1")
q(2,"No caso narrado, a postura da equipe após a chegada da polícia militar está de acordo com a lei porque a guarda",["prestou todo o apoio à continuidade do atendimento.","assumiu o comando da ocorrência.","retirou-se sem prestar informações.","entregou o caso ao Ministério Público.","exigiu a lavratura do flagrante na base da guarda."],"Art. 5º, parágrafo único.","tg1")
# DIFÍCEIS
q(3,"Assinale a alternativa INCORRETA de acordo com a Lei 13.022/2014.",["As guardas municipais são instituições de caráter militar, armadas conforme previsto em lei.","Incumbe às guardas municipais a proteção municipal preventiva.","São ressalvadas as competências da União, dos Estados e do Distrito Federal.","O patrulhamento preventivo é princípio mínimo de atuação.","O uso progressivo da força é princípio mínimo de atuação."],"O caráter é civil.")
q(3,"Assinale a alternativa INCORRETA quanto aos bens protegidos pela guarda municipal.",["Os bens dominiais estão excluídos da proteção da guarda.","Os bens de uso comum estão incluídos.","Os bens de uso especial estão incluídos.","Logradouros públicos municipais estão incluídos.","Instalações do Município estão incluídas."],"O parágrafo único do art. 4º inclui os dominiais.")
q(3,"Considere as afirmações: I. Diante de flagrante, a guarda encaminha o autor ao delegado de polícia. II. A preservação do local do crime é obrigatória em todos os casos. III. Chegando a polícia, a guarda presta apoio à continuidade do atendimento. Está correto o que se afirma em",["I e III, apenas.","I, II e III.","I e II, apenas.","II e III, apenas.","III, apenas."],"II erra: é quando possível e sempre que necessário.")
q(3,"Considere as afirmações: I. Os princípios do art. 3º são mínimos. II. O uso da força pela guarda é progressivo. III. O patrulhamento previsto como princípio é ostensivo e repressivo. Está correto o que se afirma em",["I e II, apenas.","I, II e III.","I e III, apenas.","II e III, apenas.","I, apenas."],"O princípio é patrulhamento preventivo.")
q(3,"Segundo a tese do Tema 656 do STF, ao exercer ações de segurança urbana, as guardas municipais devem",["respeitar as atribuições dos demais órgãos de segurança pública e não exercer atividade de polícia judiciária.","substituir a polícia militar no policiamento ostensivo.","conduzir inquéritos policiais em crimes de menor potencial ofensivo.","atuar apenas em bens de uso especial.","submeter-se ao controle externo do Tribunal de Justiça."],"Tese do Tema 656.")
q(3,"Assinale a alternativa que associa corretamente o inciso do art. 5º à competência.",["XIV: encaminhar ao delegado de polícia, diante de flagrante delito, o autor da infração.","XIII: auxiliar na segurança de grandes eventos.","XVIII: exercer competências de trânsito.","VI: atuar na segurança escolar.","XVII: atender ocorrências emergenciais."],"XIV é o flagrante; os demais estão trocados.")
q(3,"Assinale a alternativa que associa corretamente o inciso do art. 5º à competência.",["XIII: garantir o atendimento de ocorrências emergenciais.","XIV: proteger o patrimônio ecológico.","V: estudo de impacto em empreendimentos de grande porte.","I: segurança escolar.","XV: pacificação de conflitos presenciados."],"XIII é a ocorrência emergencial.")
q(3,"Na segurança escolar, segundo o art. 5º, XVIII, a guarda municipal participa de ações educativas com",["o corpo discente e docente das unidades de ensino municipal.","os pais dos alunos das escolas particulares, com exclusividade.","os diretores das escolas estaduais apenas.","a Secretaria Estadual de Educação.","os conselhos tutelares, que coordenam a ação."],"Art. 5º, XVIII.")
q(3,"Assinale a alternativa em que a substituição altera o sentido da lei.",["“proteção municipal preventiva” por “proteção municipal repressiva”.","“instituições de caráter civil” por “instituições civis”.","“uso progressivo da força” por “uso da força de forma progressiva”.","“patrulhamento preventivo” por “patrulhamento de caráter preventivo”.","“preservação da vida” por “preservar a vida”."],"Preventiva e repressiva têm sentidos opostos.")
q(3,"Segundo a lei, a guarda municipal pode colaborar ou atuar conjuntamente com",["órgãos de segurança pública da União, dos Estados e do Distrito Federal ou de congêneres de Municípios vizinhos.","apenas a polícia militar de seu Estado.","empresas de segurança privada, com exclusividade.","as Forças Armadas, como força auxiliar.","somente as guardas de Municípios da mesma região metropolitana."],"Art. 5º, parágrafo único.")
q(3,"No caso narrado, a equipe deixou o portão do galpão como estava e impediu a entrada de curiosos até a chegada da perícia. Essa conduta corresponde a",["preservar o local do crime, quando possível e sempre que necessário.","usar a força de forma progressiva.","exercer competência de trânsito.","colaborar com a defesa civil.","atuar na segurança escolar."],"Art. 5º, XIV.","tg1")
q(3,"No caso narrado, o galpão abandonado onde o furto ocorreu pertence à prefeitura e não tem uso público. Trata-se de bem",["dominial, também protegido pela guarda municipal.","de uso especial, único protegido pela guarda.","de uso comum, protegido pela guarda.","particular, fora da proteção da guarda.","dominial, excluído da proteção da guarda."],"Art. 4º, parágrafo único: os dominiais estão incluídos.","tg1")
q(3,"No caso narrado, se a equipe tivesse algemado e agredido o suspeito que já estava rendido, violaria principalmente o princípio",["do uso progressivo da força.","do patrulhamento preventivo.","do compromisso com a evolução social da comunidade.","da competência geral sobre logradouros.","da cooperação com a defesa civil."],"A força deve ser proporcional e progressiva à resistência.","tg1")
q(3,"Assinale a alternativa correta sobre a decisão do STF na ADPF 1214 (2026).",["Os Municípios não podem substituir a denominação “Guarda Municipal” por “Polícia Municipal” ou denominação similar.","Os Municípios podem adotar a denominação “Polícia Municipal” por lei local.","A guarda municipal passou a ter caráter militar.","As guardas municipais deixaram de integrar a segurança pública.","A denominação passou a ser escolhida por decreto do prefeito."],"Tese da ADPF 1214.")
q(3,"Assinale a alternativa INCORRETA sobre as competências específicas das guardas municipais.",["A guarda municipal pode instaurar inquérito policial nos crimes ocorridos em bens municipais.","A guarda municipal pode auxiliar na proteção de autoridades e dignatários.","A guarda municipal pode cooperar com a defesa civil.","A guarda municipal pode exercer competências de trânsito.","A guarda municipal pode atuar na segurança escolar."],"Inquérito é atividade de polícia judiciária, excluída das guardas.")
q(3,"A expressão “ressalvadas as competências da União, dos Estados e do Distrito Federal”, no art. 2º, significa que a guarda municipal",["exerce sua função sem invadir as atribuições desses entes.","está subordinada ao governador do Estado.","pode substituir as polícias estaduais quando necessário.","depende de autorização federal para atuar.","exerce competência exclusiva sobre a segurança pública."],"A ressalva preserva as competências dos outros entes.")
q(3,"Considere as afirmações: I. A guarda pode atuar nas vias municipais conforme o CTB. II. Pode exercer competência de trânsito de forma concorrente, mediante convênio. III. Pode fiscalizar o trânsito em rodovias federais por ato próprio. Está correto o que se afirma em",["I e II, apenas.","I, II e III.","I e III, apenas.","II e III, apenas.","III, apenas."],"Art. 5º, VI. Rodovia federal não é via municipal.")
q(3,"De acordo com a Lei 13.022/2014, é correto afirmar que",["a guarda municipal deve articular-se com os órgãos municipais de políticas sociais, visando à adoção de ações interdisciplinares de segurança.","a guarda municipal é órgão de polícia judiciária do Município.","os princípios de atuação das guardas são definidos exclusivamente por lei municipal.","as guardas municipais são forças auxiliares e reserva do Exército.","a guarda municipal só pode atuar em bens de uso especial."],"Art. 5º, XI.")
q(3,"Assinale a alternativa que contém apenas competências específicas previstas no art. 5º da Lei 13.022/2014.",["Cooperar com a defesa civil; auxiliar na segurança de grandes eventos; atuar na segurança escolar.","Instaurar inquérito; cooperar com a defesa civil; atuar na segurança escolar.","Auxiliar na segurança de grandes eventos; julgar infrações de trânsito; proteger o patrimônio cultural.","Policiar fronteiras; atuar na segurança escolar; cooperar com a defesa civil.","Lavrar auto de prisão em flagrante; proteger autoridades; zelar por prédios públicos."],"Incisos VIII, XVII e XVIII. Inquérito e auto de prisão em flagrante cabem à polícia judiciária.")
q(3,"Assinale a alternativa correta sobre o art. 1º da Lei 13.022/2014.",["A lei institui normas gerais, cabendo aos Municípios complementá-las sem contrariá-las.","A lei proíbe os Municípios de legislar sobre suas guardas.","A lei regulamenta o art. 144, § 5º, que trata das polícias militares.","A lei só se aplica às guardas criadas depois de 2014.","A lei institui normas específicas para cada guarda."],"Normas gerais definem o piso comum; a lei municipal completa.")
assert len(Q)==60
tg1="<strong>Equipe da Guarda atende duas ocorrências na mesma noite</strong><br><br>Durante ronda preventiva no Jardim Proença, uma equipe da Guarda Municipal se deparou com um motociclista caído na via, ferido após uma queda. Os agentes prestaram os primeiros socorros, sinalizaram o local e acionaram o Samu. Quando uma viatura da polícia militar chegou, a equipe repassou as informações e permaneceu dando apoio até a remoção da vítima.<br><br>Pouco depois, a equipe foi chamada a um galpão abandonado que pertence à prefeitura e não tem uso público. Lá, flagrou um homem saindo com fios de cobre retirados da instalação elétrica. O suspeito não resistiu e foi contido sem uso de força além da necessária.<br><br>Os agentes deixaram o portão do galpão como estava, impediram a entrada de curiosos até a chegada da perícia e conduziram o suspeito ao delegado de polícia de plantão."
code,svg=mapa("O que a guarda é e o que ela faz (arts. 1º a 5º)",[
 ("natureza","Natureza (art. 2º)",["caráter civil","uniformizada; armada conforme lei","proteção municipal preventiva"],"seções 1 e 2"),
 ("principios","Princípios (art. 3º)",["cinco princípios mínimos","patrulhamento preventivo","uso progressivo da força"],"seção 3"),
 ("bens","Competência geral (art. 4º)",["bens, serviços, logradouros","uso comum, uso especial","e dominiais"],"seção 4"),
 ("prevenir","Proteger e integrar",["zelar por prédios e bens","defesa civil; convênios","trânsito conforme o CTB"],"seção 5"),
 ("ocorrencia","Atuar na ocorrência",["emergência: atender já","flagrante: ao delegado","polícia chegou: apoio"],"seção 5"),
 ("stf","O que o STF decidiu",["integra a segurança pública","ostensivo sim, judiciária não","nome: Guarda Municipal"],"seção 6")],
 "Na prova: civil, preventiva, progressiva, delegado de polícia e “quando possível e sempre que necessário”")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,'QR',8,9,10],QR,7,svg,"Os três primeiros grupos dizem o que a guarda é; os três últimos, o que ela faz e como o STF lê a lei hoje.","Fontes: Lei 13.022/2014, arts. 1º a 5º, texto consolidado da Câmara dos Deputados; Constituição Federal, art. 144, § 8º; STF, ADPF 995, Tema 656 (RE 608.588) e ADPF 1214. Caso de apoio criado para a aula.")
revisao("gm-1",'Estatuto das Guardas Municipais (Lei 13.022/2014, arts. 1º a 5º)',Q,{'tg1':tg1},pendencias=['A ADPF 995 (STF, 2023) foi citada sem conferir na página do STF.', 'Parte dos artigos da Lei 13.022/2014 foi conferida por trechos; reconferir o texto integral no Planalto.'])
gravar("gm-1",aula_html,banco("gm-1",Q),{"tg1":tg1})
print(len(aula_html))
