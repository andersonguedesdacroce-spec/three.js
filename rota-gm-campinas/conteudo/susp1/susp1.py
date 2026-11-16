import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='susp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Lei 13.675/2018 instituiu o Sistema Único de Segurança Pública (Susp) e a Política Nacional de Segurança Pública e Defesa Social (PNSPDS). Para a Guarda Municipal, ela é a lei que a reconhece como integrante operacional do sistema. Neste primeiro posto, o foco são os arts. 1º a 8º: a finalidade, a competência de cada ente, os princípios, as diretrizes, os objetivos, as estratégias e os meios e instrumentos. A Vunesp cobra a letra da lei: a finalidade (preservação da ordem pública e da incolumidade das pessoas e do patrimônio), os princípios (como o uso comedido e proporcional da força) e siglas como Sinesp, Sinaped e Sievap."
S={}
S[1]="## 1. Finalidade e competências\n\n"+L("art. 1º","Art. 1º Esta Lei institui","Art. 2º")+"\n\n"+L("art. 2º","Art. 2º A segurança pública é dever do Estado","CAPÍTULO II")+"\n\n"+L("art. 3º","Art. 3º Compete à União","Seção II")+"""

A lei institui o Susp e cria a PNSPDS, com a finalidade de preservação da ordem pública e da incolumidade das pessoas e do patrimônio, por meio de atuação conjunta, coordenada, sistêmica e integrada dos órgãos de segurança pública e defesa social da União, dos Estados, do Distrito Federal e dos Municípios, em articulação com a sociedade. A segurança pública é dever do Estado e responsabilidade de todos, compreendendo a União, os Estados, o Distrito Federal e os Municípios, no âmbito de suas competências. Compete à União estabelecer a PNSPDS, e os demais entes estabelecem suas políticas, observadas as diretrizes da política nacional.
"""
S[2]="## 2. Princípios\n\n"+L("art. 4º","Art. 4º São princípios da PNSPDS","Art. 4º-A.")+"\n\n"+L("art. 4º-A","Art. 4º-A. A lei do ente federado","Seção III")+"""

Os princípios incluem o respeito ao ordenamento jurídico e aos direitos e garantias individuais e coletivos; a proteção, valorização e reconhecimento dos profissionais; a proteção dos direitos humanos e a promoção da cidadania; a eficiência na prevenção, no controle e na repressão das infrações penais; a participação e o controle social; a resolução pacífica de conflitos; o uso comedido e proporcional da força pelos agentes, pautado nos documentos internacionais de direitos humanos; a proteção da vida, do patrimônio e do meio ambiente; a publicidade das informações não sigilosas; a otimização dos recursos; a simplicidade, informalidade, economia procedimental e celeridade; a relação harmônica entre os Poderes; e a transparência, responsabilização e prestação de contas. A lei do ente federado deve exigir, para ingresso na instituição, exame de saúde e exame toxicológico com larga janela de detecção.
"""
S[3]="## 3. Diretrizes\n\n"+L("art. 5º, I a V","Art. 5º São diretrizes da PNSPDS","VI - formação e capacitação")+"\n\n"+L("art. 5º, VI","VI - formação e capacitação","VII - fortalecimento")+"\n\n"+L("art. 5º, XII","XII - ênfase","XIII - modernização")+"\n\n"+L("art. 5º, XXI a XXIII","XXI - deontologia","XXIV - (VETADO)")+"""

Entre as diretrizes estão o atendimento imediato ao cidadão; o planejamento estratégico e sistêmico; o fortalecimento das ações de prevenção e resolução pacífica de conflitos, com redução da letalidade violenta; a atuação integrada entre os entes; a coordenação, cooperação e colaboração dos órgãos; a formação e capacitação continuada dos profissionais; a ênfase no policiamento de proximidade, com foco na resolução de problemas; a deontologia policial e de bombeiro militar comuns, a unidade de registro de ocorrência policial e o uso de sistema integrado de informações e dados eletrônicos.
"""
S[4]="## 4. Objetivos, estratégias e instrumentos\n\n"+L("art. 6º, I a III","Art. 6º São objetivos da PNSPDS","IV - estimular e apoiar")+"\n\n"+L("art. 6º, IV","IV - estimular e apoiar a realização","V - promover a participação social")+"\n\n"+L("art. 6º, parágrafo único","Parágrafo único. Os objetivos estabelecidos","Seção V")+"\n\n"+L("art. 7º","Art. 7º A PNSPDS será implementada","Seção VI")+"\n\n"+L("art. 8º","Art. 8º São meios e instrumentos","III - (VETADO)")+"""

Os objetivos incluem fomentar a integração em ações estratégicas e operacionais, em inteligência e em gerenciamento de crises; apoiar a manutenção da ordem pública e da incolumidade das pessoas e do patrimônio; incentivar a modernização de equipamentos; estimular ações de prevenção à violência, com prioridade para as relacionadas à letalidade da população jovem negra, das mulheres e de outros grupos vulneráveis; e promover a participação social nos Conselhos. Os objetivos direcionam a formulação do Plano Nacional de Segurança Pública e Defesa Social, com estratégias, metas, indicadores e ações.

Os meios e instrumentos são os planos de segurança pública e defesa social; o Sistema Nacional de Informações e de Gestão de Segurança Pública e Defesa Social, que inclui o Sinaped, o Sinesp, o Sievap, a Renaesp e o Pró-Vida; o Plano Nacional de Enfrentamento de Homicídios de Jovens; os mecanismos de prevenção a atos ilícitos contra a Administração Pública; e o Plano Nacional de Prevenção e Enfrentamento à Violência contra a Mulher.
"""
S[5]="""## 5. Na rotina do guarda

- **Uso da força:** o princípio do uso comedido e proporcional da força orienta a atuação do guarda, pautado nos documentos internacionais de direitos humanos.
- **Policiamento de proximidade:** a diretriz de ênfase no policiamento de proximidade, com foco na resolução de problemas, é a vocação da Guarda Municipal.
- **Registro de ocorrência:** a aceitação mútua e a unidade de registro de ocorrência policial integram a lógica do sistema.
- **Prevenção:** a prioridade de políticas de prevenção à violência com foco em grupos vulneráveis orienta o atendimento.
- **Integração:** o guarda atua articulado com as demais forças e com a sociedade.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Finalidade da lei | Preservação da ordem pública e da incolumidade das pessoas e do patrimônio |
| Quem estabelece a PNSPDS | A União; os demais entes estabelecem as suas, observadas as diretrizes |
| Natureza da segurança pública | Dever do Estado e responsabilidade de todos |
| Princípio do uso da força | Comedido e proporcional |
| Exame do ingresso | Saúde e toxicológico com larga janela de detecção |
| Diretriz de proximidade | Policiamento de proximidade com foco na resolução de problemas |
| Sinesp | Segurança pública, prisionais, rastreabilidade de armas e munições, material genético, digitais e drogas |
| Sievap | Educação e valorização profissional |
| Pró-Vida | Qualidade de vida dos profissionais |
| Plano Nacional | Estratégias, metas, indicadores e ações |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Susp e PNSPDS; ordem pública e incolumidade |
| Art. 2º | Dever do Estado e responsabilidade de todos |
| Art. 3º | União estabelece a PNSPDS |
| Art. 4º | 16 princípios; uso comedido e proporcional da força |
| Art. 4º-A | Exame de saúde e toxicológico no ingresso |
| Art. 5º | Diretrizes; proximidade |
| Art. 6º | Objetivos; Plano Nacional |
| Art. 7º | Estratégias |
| Art. 8º | Planos, Sinaped, Sinesp, Sievap, Renaesp, Pró-Vida |
"""
QR=[("Questão 1","A segurança pública é dever do Estado e responsabilidade de",["todos.","apenas da polícia.","apenas da União.","apenas do Município.","apenas dos Estados."],0,"Art. 2º."),
("Questão 2","Compete à União estabelecer a Política Nacional de Segurança Pública e Defesa Social e aos demais entes estabelecer suas respectivas políticas, observadas as",["diretrizes da política nacional.","vontades locais.","normas privadas.","sugestões dos vizinhos.","decisões do Judiciário."],1,"Art. 3º."),
("Questão 3","Entre os princípios da PNSPDS está o uso comedido e proporcional da",["força pelos agentes da segurança pública.","arma de fogo apenas.","algema apenas.","informação.","viatura."],2,"Art. 4º, IX."),
("Questão 4","O Sinesp é o Sistema Nacional de Informações de Segurança Pública, Prisionais, de Rastreabilidade de Armas e Munições, de Material Genético, de Digitais e de",["Drogas.","Imóveis.","Veículos.","Empresas.","Escolas."],3,"Art. 8º, II, b.")]
t1="<strong>Guarda de proximidade</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, passou a fazer rondas a pé nos bairros, conversando com moradores e comerciantes para resolver problemas locais antes que virem crimes."
t2="<strong>Ocorrência em outro município</strong><br><br>Um registro de ocorrência de Vila Nova foi aceito por uma polícia de município vizinho, sem que a vítima precisasse registrar novamente."
t3="<strong>Uso da força na abordagem</strong><br><br>Numa abordagem, um guarda de Vila Nova imobilizou um homem que resistia, usando apenas a força necessária, e cessou assim que ele se acalmou."
tx={"susp1a":t1,"susp1b":t2,"susp1c":t3}
# n=1
q(1,"A Lei 13.675/2018 institui o Sistema Único de Segurança Pública (Susp) e cria a Política Nacional de Segurança Pública e",["Defesa Social.","Justiça Criminal.","Combate ao Crime.","Prevenção ao Delito.","Ordem Pública."],"Art. 1º.")
q(1,"A finalidade da lei é a preservação da ordem pública e da incolumidade das pessoas e do",["patrimônio.","comércio.","governo.","mercado.","trânsito."],"Art. 1º.")
q(1,"A atuação dos órgãos de segurança pública é conjunta, coordenada, sistêmica e",["integrada.","isolada.","eventual.","facultativa.","reservada."],"Art. 1º.")
q(1,"A segurança pública compreende a União, os Estados, o Distrito Federal e os",["Municípios.","clubes.","empresas.","sindicatos.","partidos."],"Art. 2º.")
q(1,"Compete à União estabelecer a",["Política Nacional de Segurança Pública e Defesa Social.","política local de cada Município.","lei orgânica municipal.","lei estadual.","regimento da guarda."],"Art. 3º.")
q(1,"É princípio da PNSPDS o respeito ao ordenamento jurídico e aos direitos e garantias individuais e",["coletivos.","empresariais.","partidários.","religiosos.","estatais."],"Art. 4º, I.")
q(1,"É princípio da PNSPDS a proteção, valorização e reconhecimento dos profissionais de",["segurança pública.","saúde.","educação.","transporte.","comércio."],"Art. 4º, II.")
q(1,"É princípio da PNSPDS a resolução pacífica de",["conflitos.","contratos.","dívidas.","mandatos.","tributos."],"Art. 4º, VIII.")
q(1,"É princípio da PNSPDS a participação e o controle",["social.","privado.","partidário.","militar.","judicial."],"Art. 4º, VII.")
q(1,"É princípio da PNSPDS a proteção da vida, do patrimônio e do meio",["ambiente.","comércio.","imóvel.","trabalho.","turismo."],"Art. 4º, X.")
q(1,"É princípio da PNSPDS a publicidade das informações não",["sigilosas.","públicas.","oficiais.","policiais.","estatísticas."],"Art. 4º, XI.")
q(1,"A lei do ente federado deverá exigir para ingresso na instituição exame de saúde e exame",["toxicológico com larga janela de detecção.","de capacidade física apenas.","psicotécnico apenas.","grafológico.","de aptidão artística."],"Art. 4º-A.")
q(1,"É diretriz da PNSPDS o atendimento imediato ao",["cidadão.","juiz.","delegado.","prefeito.","promotor."],"Art. 5º, I.")
q(1,"É diretriz da PNSPDS o planejamento estratégico e",["sistêmico.","eventual.","isolado.","privado.","ocasional."],"Art. 5º, II.")
q(1,"É diretriz a ênfase nas ações de policiamento de",["proximidade, com foco na resolução de problemas.","choque.","gabinete.","fronteira.","trânsito."],"Art. 5º, XII.")
q(1,"É objetivo da PNSPDS promover a participação social nos Conselhos de",["segurança pública.","saúde.","educação.","trânsito.","esportes."],"Art. 6º, V.")
q(1,"Entre os meios e instrumentos estão os planos de segurança pública e",["defesa social.","trânsito.","saúde.","educação.","turismo."],"Art. 8º, I.")
q(1,"No texto da guarda de proximidade, a atuação a pé nos bairros corresponde à diretriz do policiamento de",["proximidade, com foco na resolução de problemas.","choque.","gabinete.","fronteira.","fiscalização."],"Art. 5º, XII.","susp1a")
q(1,"No texto da ocorrência em outro município, a aceitação do registro por outra polícia é compatível com a ideia da",["unidade de registro de ocorrência policial.","dupla notificação.","reserva de competência.","separação de bancos de dados.","autonomia absoluta."],"Art. 5º, XXII.","susp1b")
q(1,"No texto do uso da força na abordagem, o uso apenas da força necessária atende ao princípio do uso",["comedido e proporcional da força.","máximo da força.","ilimitado.","eventual.","privado."],"Art. 4º, IX.","susp1c")
# n=2
q(2,"A atuação do Susp é feita em articulação com a",["sociedade.","imprensa.","iniciativa privada apenas.","universidade apenas.","igreja."],"Art. 1º.")
q(2,"A segurança pública é exercida no âmbito das competências e atribuições legais de cada um dos",["entes federados.","vizinhos.","clubes.","empresas.","partidos."],"Art. 2º.")
q(2,"Os Estados, o Distrito Federal e os Municípios estabelecem suas políticas, observadas as diretrizes da política",["nacional.","local.","estadual.","privada.","regional."],"Art. 3º.")
q(2,"O princípio do uso comedido e proporcional da força é pautado nos documentos internacionais de proteção aos direitos",["humanos de que o Brasil seja signatário.","civis.","tributários.","comerciais.","militares."],"Art. 4º, IX.")
q(2,"É princípio a eficiência na prevenção e no controle das infrações",["penais.","civis.","tributárias.","trabalhistas.","eleitorais."],"Art. 4º, IV.")
q(2,"É princípio a simplicidade, informalidade, economia procedimental e",["celeridade no serviço prestado à sociedade.","lentidão.","burocracia.","sigilo.","gratuidade."],"Art. 4º, XIV.")
q(2,"É princípio a relação harmônica e colaborativa entre os",["Poderes.","vizinhos.","municípios apenas.","clubes.","sindicatos."],"Art. 4º, XV.")
q(2,"O exame toxicológico do art. 4º-A tem larga janela de",["detecção.","aplicação.","cobrança.","descarte.","coleta."],"Art. 4º-A.")
q(2,"O regulamento da lei estabelecerá as regras do exame toxicológico",["aleatório.","anual.","bianual.","mensal.","obrigatório sempre."],"Art. 4º-A, parágrafo único.")
q(2,"É diretriz a formação e capacitação continuada e qualificada dos profissionais, em consonância com a matriz curricular",["nacional.","local.","estadual.","privada.","militar."],"Art. 5º, VI.")
q(2,"É diretriz a deontologia policial e de bombeiro militar comuns, respeitados os regimes jurídicos e as peculiaridades de cada",["instituição.","cidade.","região.","empresa.","escola."],"Art. 5º, XXI.")
q(2,"É diretriz o uso de sistema integrado de informações e dados",["eletrônicos.","impressos.","manuscritos.","orais.","privados."],"Art. 5º, XXIII.")
q(2,"Entre os objetivos está estimular ações de prevenção à violência, com prioridade para a letalidade da população jovem negra, das mulheres e de outros grupos",["vulneráveis.","privilegiados.","urbanos.","rurais.","esportivos."],"Art. 6º, IV.")
q(2,"Os objetivos direcionam a formulação do Plano Nacional de Segurança Pública e Defesa Social, que estabelece estratégias, metas, indicadores e",["ações.","impostos.","prêmios.","cargos.","verbas."],"Art. 6º, parágrafo único.")
q(2,"O Sinaped é o Sistema Nacional de Acompanhamento e Avaliação das Políticas de Segurança Pública e",["Defesa Social.","Trânsito.","Justiça.","Penitenciárias.","Bombeiros."],"Art. 8º, II, a.")
q(2,"O Sievap é o Sistema Integrado de Educação e Valorização",["Profissional.","Policial.","Pública.","Penitenciária.","Municipal."],"Art. 8º, II, c.")
q(2,"A Renaesp é a Rede Nacional de Altos Estudos em Segurança",["Pública.","Privada.","Municipal.","Nacional.","Penal."],"Art. 8º, II, d.")
q(2,"O Pró-Vida é o Programa Nacional de Qualidade de Vida para Profissionais de Segurança",["Pública.","Privada.","Municipal.","Estadual.","Nacional."],"Art. 8º, II, e.")
q(2,"No texto da guarda de proximidade, o policiamento a pé busca a resolução de problemas antes que se tornem",["crimes.","dívidas.","contratos.","festas.","reuniões."],"Art. 5º, XII.","susp1a")
q(2,"No texto da ocorrência em outro município, a aceitação do registro está ligada à integração dos",["órgãos do Susp.","cartórios.","bancos.","clubes.","sindicatos."],"Art. 10, III.","susp1b")
# n=3
q(3,"Assinale a alternativa correta sobre a Lei 13.675/2018.",["A finalidade é a preservação da ordem pública e da incolumidade das pessoas e do patrimônio, por atuação integrada dos órgãos dos entes federados, em articulação com a sociedade.","A segurança pública é dever exclusivo da polícia.","A União executa toda a segurança pública.","Os Municípios não integram o sistema.","A lei dispensa a sociedade."],"Arts. 1º e 2º.")
q(3,"Considere. I. O uso da força deve ser comedido e proporcional. II. O ingresso exige exame toxicológico com larga janela de detecção. III. Compete aos Municípios estabelecer a PNSPDS. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A PNSPDS é estabelecida pela União (art. 3º).")
q(3,"Assinale a INCORRETA.",["O Sinesp reúne dados apenas sobre trânsito.","O Sievap trata de educação e valorização profissional.","O Pró-Vida trata de qualidade de vida.","A Renaesp trata de altos estudos.","O Sinaped avalia políticas."],"O Sinesp abrange segurança pública, prisionais, armas, material genético, digitais e drogas (art. 8º, II, b).")
q(3,"A lei estabelece como princípio a transparência, responsabilização e",["prestação de contas.","sigilo.","gratuidade.","anonimato.","omissão."],"Art. 4º, XVI.")
q(3,"Entre as diretrizes está o atendimento prioritário, qualificado e humanizado às pessoas em situação de",["vulnerabilidade.","riqueza.","viagem.","moradia.","trabalho."],"Art. 5º, X.")
q(3,"Entre as diretrizes está a padronização de estruturas, de capacitação, de tecnologia e de equipamentos de interesse da",["segurança pública.","saúde.","educação.","cultura.","indústria."],"Art. 5º, XI.")
q(3,"Entre as diretrizes está a celebração de termo de parceria e protocolos com agências de vigilância privada, respeitada a lei de",["licitações.","imprensa.","trânsito.","propriedade.","posse."],"Art. 5º, XXVI.")
q(3,"Entre os objetivos está fomentar ações permanentes para o combate ao crime organizado e à",["corrupção.","moda.","imprensa.","pesca.","cultura."],"Art. 6º, XVII.")
q(3,"Entre os objetivos está fortalecer as ações de fiscalização de armas de fogo e munições, com vistas à redução da violência",["armada.","urbana.","rural.","sexual.","doméstica."],"Art. 6º, XXV.")
q(3,"Entre os objetivos está fortalecer as ações de prevenção e repressão aos crimes",["cibernéticos.","tributários.","trabalhistas.","eleitorais.","ambientais."],"Art. 6º, XXVI.")
q(3,"A PNSPDS será implementada por estratégias que garantam, entre outros, integração, coordenação e cooperação federativa, interoperabilidade e",["liderança situacional.","sigilo absoluto.","isolamento.","centralização.","privatização."],"Art. 7º.")
q(3,"A PNSPDS será implementada com garantia da regularidade orçamentária para execução de planos e programas de",["segurança pública.","saúde.","educação.","turismo.","esporte."],"Art. 7º.")
q(3,"Entre os meios e instrumentos consta o Plano Nacional de Enfrentamento de Homicídios de",["Jovens.","Idosos.","Mulheres.","Crianças.","Policiais."],"Art. 8º, IV.")
q(3,"Entre os meios e instrumentos consta o Plano Nacional de Prevenção e Enfrentamento à Violência contra a",["Mulher.","Criança.","Pessoa Idosa.","Pessoa com Deficiência.","Comunidade."],"Art. 8º, VI.")
q(3,"No texto da guarda de proximidade, a atuação junto a moradores e comerciantes envolve também a diretriz da participação",["social nas questões de segurança pública.","partidária.","empresarial exclusiva.","judicial.","militar."],"Art. 5º, XIV.","susp1a")
q(3,"No texto da guarda de proximidade, a integração com a comunidade se ajusta ao princípio da participação e controle",["social.","privado.","judicial.","militar.","legislativo."],"Art. 4º, VII.","susp1a")
q(3,"No texto da ocorrência em outro município, a aceitação mútua do registro está listada como forma de integração no art.",["10, inciso III.","8º, inciso I.","6º, inciso I.","4º, inciso I.","3º."],"Art. 10, III.","susp1b")
q(3,"No texto da ocorrência em outro município, a diretriz que se relaciona é a unidade de registro de ocorrência",["policial.","civil.","tributária.","judicial.","eleitoral."],"Art. 5º, XXII.","susp1b")
q(3,"No texto do uso da força na abordagem, o princípio aplicado está no art. 4º, inciso",["IX.","I.","II.","V.","XV."],"Art. 4º, IX.","susp1c")
q(3,"No texto do uso da força na abordagem, o princípio exige que a força seja pautada em documentos internacionais de",["direitos humanos.","direito comercial.","direito tributário.","direito marítimo.","direito aduaneiro."],"Art. 4º, IX.","susp1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Susp: PNSPDS (arts. 1º a 8º)",[
 ("fin","Finalidade",["ordem pública e incolumidade","atuação integrada","articulação com a sociedade"],"seção 1"),
 ("com","Competências",["União estabelece a PNSPDS","entes estabelecem as suas"],"seção 1"),
 ("pri","Princípios",["direitos humanos","uso comedido da força","participação social"],"seção 2"),
 ("dir","Diretrizes",["atendimento imediato","policiamento de proximidade","registro único"],"seção 3"),
 ("obj","Objetivos",["integração","prevenção à violência","Plano Nacional"],"seção 4"),
 ("ins","Meios e instrumentos",["planos","Sinaped, Sinesp, Sievap","Renaesp, Pró-Vida"],"seção 4")],
 "Na prova: finalidade, princípios (força comedida) e siglas")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',5,6,7],QR,5,svg,"A primeira linha traz a finalidade e os princípios; as demais, as diretrizes, os objetivos e os instrumentos.","Fontes: Edital 02/2026, Anexo I; Lei 13.675/2018 (Susp), arts. 1º a 8º, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("susp-1","Susp: Política Nacional de Segurança Pública e Defesa Social (arts. 1º a 8º)",Q,list(tx),
 cobertura=["Cobertos: arts. 1º a 8º. Do art. 5º foram citados os incisos I a VI, XII, XXI a XXIII; do art. 6º, I a IV e o parágrafo único. Demais incisos não detalhados."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Numeração (VI, X, XII, XXI a XXVI do art. 5º e XXV, XXVI do art. 6º) a conferir no Planalto.","Trechos de lei copiados de fontes/susp.txt por programa.","Casos susp1a, susp1b e susp1c fictícios."],
 fontes_conferidas=["Lei 13.675/2018, arts. 1º a 8º: texto da Câmara, copiado por programa."])
gravar("susp-1",aula_html,banco("susp-1",Q),tx)
