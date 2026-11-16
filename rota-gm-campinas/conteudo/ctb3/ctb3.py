import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Código de Trânsito protege quem anda a pé e quem usa veículo não motorizado, dá ao cidadão o direito de pedir providências aos órgãos de trânsito e manda educar para o trânsito. A Vunesp cobra os arts. 68 a 79 pela regra do pedestre (passeios, travessia, prioridade nas faixas), pelo ciclista que desmonta, pelo direito de petição do cidadão e pelas obrigações de educação no sistema. O guarda municipal lida com tudo isso no dia a dia, das faixas de pedestres às campanhas educativas. A aula segue o texto consolidado."
S={}
S[1]="## 1. O pedestre e o ciclista desmontado\n\n"+L("art. 68, caput e § 1º","Art. 68. É assegurada ao pedestre","§ 2º Nas áreas urbanas")+"\n\n"+L("art. 68, §§ 2º e 3º","§ 2º Nas áreas urbanas","§ 4º (VETADO)")+"""

O pedestre tem assegurada a utilização dos passeios ou passagens apropriadas das vias urbanas e dos acostamentos das vias rurais. O ciclista desmontado, empurrando a bicicleta, equipara-se ao pedestre em direitos e deveres. Quando não há passeio, ou não é possível usá-lo, o pedestre circula na pista de rolamento com prioridade sobre os veículos, pelos bordos da pista, em fila única. A diferença entre a zona urbana e a rural está no sentido: nas vias rurais, sem acostamento, o pedestre caminha em sentido contrário ao deslocamento dos veículos, o que lhe permite ver quem vem.

"""+L("art. 69, caput","Art. 69. Para cruzar a pista de rolamento","I - onde não houver faixa")+"\n\n"+L("art. 70","Art. 70. Os pedestres que estiverem atravessando","Art. 71.")+"""

Para cruzar a pista, o pedestre toma precauções (visibilidade, distância e velocidade dos veículos) e usa sempre as faixas ou passagens destinadas a ele quando existirem a até cinquenta metros. Onde não houver faixa, o cruzamento é perpendicular ao eixo da via. O pedestre que atravessa nas faixas delimitadas tem prioridade de passagem, exceto nos locais com sinalização semafórica, onde se respeitam as disposições do Código. E, onde houver semáforo, o pedestre que não concluiu a travessia tem preferência, ainda que o semáforo tenha mudado para liberar os veículos.
"""
S[2]="## 2. O direito do cidadão\n\n"+L("art. 72","Art. 72. Todo cidadão ou entidade civil","Art. 73.")+"\n\n"+L("art. 73","Art. 73. Os órgãos ou entidades pertencentes","CAPÍTULO VI")+"""

Todo cidadão ou entidade civil pode solicitar, por escrito, aos órgãos do Sistema Nacional de Trânsito, sinalização, fiscalização e implantação de equipamentos de segurança, e sugerir alterações em normas e legislação. É um direito de petição específico do trânsito. Em contrapartida, os órgãos têm o dever de analisar as solicitações e responder, por escrito, sobre a possibilidade ou não de atendimento, justificando a análise e, se for pertinente, informando quando o evento ocorrerá. As campanhas de trânsito devem esclarecer as atribuições dos órgãos e como proceder a essas solicitações.
"""
S[3]="## 3. A educação para o trânsito\n\n"+L("art. 74","Art. 74. A educação para o trânsito","Art. 75.")+"\n\n"+L("art. 75, caput","Art. 75. O CONTRAN estabelecerá, anualmente","§ 1º Os órgãos ou entidades do Sistema Nacional de Trânsito deverão promover")+"\n\n"+L("art. 76, caput","Art. 76. A educação para o trânsito","Parágrafo único. Para a finalidade prevista neste artigo")+"\n\n"+L("art. 77","Art. 77. No âmbito da educação para o trânsito","Parágrafo único. As campanhas terão")+"""

A educação para o trânsito é direito de todos e dever prioritário dos componentes do Sistema Nacional de Trânsito. Cada órgão deve ter uma coordenação educacional, e os órgãos executivos de trânsito devem promover, na própria estrutura ou por convênio, Escolas Públicas de Trânsito, nos moldes do Contran. O Contran estabelece, anualmente, os temas e cronogramas das campanhas nacionais, em especial nos períodos de férias escolares, feriados prolongados e na Semana Nacional de Trânsito, e os órgãos podem promover campanhas locais. As campanhas têm caráter permanente, e o rádio e a televisão do poder público são obrigados a difundi-las gratuitamente. A educação para o trânsito é promovida nas escolas, com planejamento coordenado entre o trânsito e a educação, e o Ministério da Saúde estabelece campanha nacional sobre primeiros socorros em caso de sinistros.

A publicidade da indústria automobilística deve incluir mensagem educativa de trânsito (art. 77-B), e o desrespeito a essa regra gera advertência por escrito, suspensão de outra propaganda do produto por até 60 dias e multa (art. 77-E). Os órgãos executivos de trânsito podem firmar convênio com os órgãos de educação (art. 79).
"""
S[5]="""## 5. Na rotina do guarda

- **Faixa de pedestres:** o guarda que fiscaliza a travessia deve lembrar que o pedestre na faixa tem prioridade, salvo no semáforo, onde vale a sinalização.
- **Ciclista desmontado:** quem empurra a bicicleta é tratado como pedestre.
- **Atendimento ao cidadão:** pedidos de sinalização, de fiscalização ou de equipamento chegam por escrito, e o órgão responde por escrito.
- **Educação para o trânsito:** a Guarda participa de campanhas, de escolas de trânsito e de ações educativas, como determina o art. 74.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Ciclista que empurra a bicicleta | Equipara-se ao pedestre |
| Pedestre na pista, sem passeio, em via urbana | Pelos bordos, em fila única, com prioridade |
| Pedestre na via rural, sem acostamento | Em sentido contrário ao dos veículos |
| Travessia sem faixa | Perpendicular ao eixo da via |
| Prioridade do pedestre na faixa | Exceto onde há semáforo, onde valem as indicações |
| Pedido do cidadão | Por escrito, com resposta por escrito |
| Educação para o trânsito | Direito de todos e dever prioritário do sistema |
| Campanhas nacionais | O Contran define os temas e cronogramas todo ano |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Pedestre | Passeio, passagem apropriada, acostamento |
| Ciclista desmontado | Equipara-se ao pedestre |
| Faixa de pedestres | Prioridade, exceto onde há semáforo |
| Faixa a até 50 m | O pedestre deve usá-la |
| Direito do cidadão | Solicitar por escrito; órgão responde por escrito |
| Educação | Direito de todos; dever prioritário do sistema |
| Campanhas | Contran fixa anualmente; permanentes; rádio e TV públicos difundem |
| Publicidade de veículos | Deve incluir mensagem educativa de trânsito |
"""
QR=[("Questão 1","O ciclista desmontado, empurrando a bicicleta, equipara-se ao pedestre",["em direitos e deveres.","apenas em direitos.","apenas em deveres.","apenas nas vias rurais.","apenas nas calçadas."],0,"Art. 68, § 1º."),
("Questão 2","Os pedestres que estiverem atravessando a via sobre as faixas delimitadas para esse fim terão prioridade de passagem, exceto",["nos locais com sinalização semafórica, onde deverão ser respeitadas as disposições do Código.","nas vias rurais.","à noite.","em dias de chuva.","nas vias locais."],2,"Art. 70, caput."),
("Questão 3","Todo cidadão ou entidade civil tem o direito de solicitar, aos órgãos do Sistema Nacional de Trânsito, sinalização, fiscalização e equipamentos de segurança,",["por escrito.","apenas verbalmente.","apenas por meio de advogado.","apenas pelo Ministério Público.","apenas pelo juiz."],1,"Art. 72."),
("Questão 4","A educação para o trânsito é direito de todos e constitui",["dever prioritário para os componentes do Sistema Nacional de Trânsito.","dever apenas das escolas.","dever apenas das famílias.","dever apenas do Município.","faculdade dos órgãos."],4,"Art. 74.")]
t1="<strong>Travessia em frente à escola</strong><br><br>Em Vila Nova, cidade fictícia, um grupo de crianças atravessava a avenida sobre a faixa de pedestres em frente a uma escola, sem semáforo. Um motorista não parou. Uma equipe da Guarda Municipal presenciou a cena."
t2="<strong>Pedido da associação de moradores</strong><br><br>Uma associação de moradores de Vila Nova pediu, por escrito, ao órgão de trânsito do Município, a colocação de uma faixa de pedestres e de uma placa de velocidade em frente a uma praça. O órgão recebeu o pedido e não deu resposta."
tx={"ctb3a":t1,"ctb3b":t2}
# n=1
q(1,"É assegurada ao pedestre a utilização dos passeios ou passagens apropriadas das vias urbanas e dos acostamentos das vias",["rurais.","urbanas apenas.","particulares.","estaduais apenas.","municipais apenas."],"Art. 68, caput.")
q(1,"Nas áreas urbanas, quando não houver passeios, a circulação de pedestres na pista de rolamento será feita com",["prioridade sobre os veículos, pelos bordos da pista, em fila única.","atenção, no meio da pista.","preferência da bicicleta.","preferência dos veículos.","preferência dos ciclistas."],"Art. 68, § 2º.")
q(1,"Nas vias rurais, quando não houver acostamento, o pedestre circula na pista de rolamento pelos bordos, em fila única, em sentido",["contrário ao deslocamento de veículos.","igual ao deslocamento de veículos.","oblíquo.","perpendicular.","indiferente."],"Art. 68, § 3º.")
q(1,"Onde não houver faixa ou passagem, o cruzamento da via pelo pedestre deverá ser feito em sentido",["perpendicular ao de seu eixo.","paralelo ao eixo.","oblíquo.","diagonal.","qualquer."],"Art. 69, I.")
q(1,"O pedestre deve usar sempre as faixas ou passagens a ele destinadas, quando existirem a uma distância de até",["cinquenta metros dele.","dez metros dele.","vinte metros dele.","cem metros dele.","duzentos metros dele."],"Art. 69, caput.")
q(1,"Onde houver foco de pedestres, o pedestre deve, ao atravessar uma passagem sinalizada,",["obedecer às indicações das luzes.","atravessar a qualquer momento.","atravessar correndo.","ignorar a luz.","aguardar o agente."],"Art. 69, II, a.")
q(1,"Os pedestres que estiverem atravessando a via sobre as faixas delimitadas para esse fim terão",["prioridade de passagem, exceto nos locais com sinalização semafórica.","nenhuma prioridade.","prioridade sempre, mesmo com semáforo.","prioridade apenas à noite.","prioridade apenas de dia."],"Art. 70, caput.")
q(1,"Nos locais com sinalização semafórica de controle de passagem, será dada preferência aos pedestres que não tenham",["concluído a travessia, mesmo em caso de mudança do semáforo.","começado a travessia.","chegado à faixa.","olhado o semáforo.","visto o agente."],"Art. 70, parágrafo único.")
q(1,"O órgão ou entidade com circunscrição sobre a via manterá obrigatoriamente as faixas e passagens de pedestres em boas condições de visibilidade, higiene, segurança e",["sinalização.","largura.","cor.","iluminação, apenas.","extensão."],"Art. 71.")
q(1,"Todo cidadão ou entidade civil tem o direito de solicitar, por escrito, aos órgãos do Sistema Nacional de Trânsito, sinalização, fiscalização e implantação de",["equipamentos de segurança.","novas ruas.","semáforos privados.","praças.","escolas."],"Art. 72.")
q(1,"Os órgãos do Sistema Nacional de Trânsito têm o dever de analisar as solicitações e responder,",["por escrito, sobre a possibilidade ou não de atendimento.","verbalmente.","por telefone.","por edital.","apenas se a solicitação for atendida."],"Art. 73, caput.")
q(1,"A educação para o trânsito é direito de todos e constitui dever",["prioritário para os componentes do Sistema Nacional de Trânsito.","apenas das escolas.","apenas das famílias.","facultativo dos órgãos.","apenas do Município."],"Art. 74.")
q(1,"É obrigatória a existência de coordenação educacional em cada órgão ou entidade",["componente do Sistema Nacional de Trânsito.","privada.","religiosa.","esportiva.","partidária."],"Art. 74, § 1º.")
q(1,"Os órgãos executivos de trânsito deverão promover, na própria estrutura ou por convênio, o funcionamento de",["Escolas Públicas de Trânsito.","autoescolas privadas.","clubes de motoristas.","oficinas.","seguradoras."],"Art. 74, § 2º.")
q(1,"O Contran estabelecerá, anualmente, os temas e os cronogramas das campanhas de âmbito",["nacional, que deverão ser promovidas por todos os órgãos do sistema.","estadual.","municipal.","local.","regional."],"Art. 75, caput.")
q(1,"As campanhas educativas de trânsito são de caráter",["permanente.","eventual.","anual.","sazonal.","facultativo."],"Art. 75, § 2º.")
q(1,"Os serviços de rádio e difusão de sons e imagens explorados pelo poder público são obrigados a difundir as campanhas de trânsito",["gratuitamente.","mediante pagamento.","por sorteio.","em horário nobre, só.","apenas aos domingos."],"Art. 75, § 2º.")
q(1,"No âmbito da educação para o trânsito, cabe ao Ministério da Saúde estabelecer campanha nacional para esclarecer condutas a serem seguidas nos",["primeiros socorros em caso de sinistros de trânsito.","tratamentos de longo prazo.","exames de habilitação.","seguros de saúde.","prêmios de seguro."],"Art. 77, caput.")
q(1,"No texto da travessia em frente à escola, as crianças atravessavam sobre a faixa, sem semáforo, e tinham",["prioridade de passagem.","nenhuma prioridade.","prioridade apenas se acompanhadas.","prioridade apenas à noite.","prioridade apenas de dia."],"Art. 70, caput.","ctb3a")
q(1,"No texto do pedido da associação, a associação de moradores, como entidade civil, tem o direito de pedir, por escrito, a",["sinalização.","construção de uma escola.","troca do prefeito.","nova lei.","abertura de concurso."],"Art. 72.","ctb3b")
# n=2
q(2,"Onde houver obstrução da calçada ou da passagem para pedestres, o órgão ou entidade com circunscrição sobre a via deverá assegurar",["a devida sinalização e proteção para circulação de pedestres.","a remoção dos pedestres.","a interdição da via.","a retirada das faixas.","a multa aos pedestres."],"Art. 68, § 6º.")
q(2,"Nos trechos urbanos de vias rurais e nas obras de arte a serem construídas, deverá ser previsto",["passeio destinado à circulação dos pedestres, que não deverão usar o acostamento.","apenas acostamento.","apenas ciclovia.","apenas passarela.","apenas semáforo."],"Art. 68, § 5º.")
q(2,"A autoridade competente pode permitir a utilização de parte da calçada para outros fins, desde que não seja prejudicial ao",["fluxo de pedestres.","comércio.","trânsito de veículos.","estacionamento.","lazer."],"Art. 68, caput.")
q(2,"Para cruzar a pista, o pedestre tomará precauções de segurança, levando em conta, principalmente, a visibilidade, a distância e a",["velocidade dos veículos.","cor dos veículos.","marca dos veículos.","idade do condutor.","placa dos veículos."],"Art. 69, caput.")
q(2,"Onde não houver foco de pedestres, o pedestre deve, antes de atravessar a passagem sinalizada, aguardar que o semáforo ou o agente de trânsito",["interrompa o fluxo de veículos.","acelere o fluxo.","libere os pedestres.","sinalize ao motorista.","feche a via."],"Art. 69, II, b.")
q(2,"Nas interseções e em suas proximidades, onde não existam faixas de travessia, os pedestres devem atravessar a via",["na continuação da calçada.","em diagonal.","no meio do quarteirão.","em qualquer ponto.","apenas em esquinas sinalizadas."],"Art. 69, III.")
q(2,"Uma vez iniciada a travessia de uma pista, os pedestres não deverão aumentar o seu percurso, demorar-se ou parar sobre ela",["sem necessidade.","em hipótese alguma.","com semáforo vermelho.","à noite.","com guarda."],"Art. 69, III, b.")
q(2,"Os órgãos do Sistema Nacional de Trânsito têm o dever de responder às solicitações dos cidadãos, esclarecendo ou",["justificando a análise efetuada.","negando sempre.","aceitando sempre.","omitindo.","ignorando."],"Art. 73, caput.")
q(2,"As campanhas de trânsito devem esclarecer quais as atribuições dos órgãos e entidades do Sistema Nacional de Trânsito e como proceder às",["solicitações do cidadão.","multas.","provas.","habilitações.","sinalizações horizontais."],"Art. 73, parágrafo único.")
q(2,"A educação para o trânsito é promovida na pré-escola e nas escolas, por meio de planejamento e ações coordenadas entre os órgãos de trânsito e de",["educação.","saúde.","justiça.","transporte.","cultura."],"Art. 76, caput.")
q(2,"As campanhas de trânsito nacionais devem ser intensificadas, em especial, nos períodos de férias escolares, feriados prolongados e na",["Semana Nacional de Trânsito.","Semana Santa.","Semana do Meio Ambiente.","Semana da Pátria.","Semana do Idoso."],"Art. 75, caput.")
q(2,"Os órgãos e entidades executivos de trânsito poderão firmar convênio com os órgãos de",["educação, para cumprir as obrigações do capítulo.","saúde.","justiça.","transporte.","segurança."],"Art. 79.")
q(2,"Toda peça publicitária da indústria automobilística, nos meios de comunicação social, incluirá obrigatoriamente",["mensagem educativa de trânsito.","preço.","fotografia do fabricante.","mapa de rodovias.","lista de revendedores."],"Art. 77-B, caput.")
q(2,"A publicidade em outdoor à margem de rodovia, de qualquer produto, também deve incluir mensagem educativa quando for de",["qualquer tipo de produto e anunciante, inclusive institucional ou eleitoral.","somente veículos.","somente peças.","somente pneus.","somente combustíveis."],"Art. 77-C.")
q(2,"O descumprimento das regras de publicidade educativa constitui infração punível com advertência por escrito, suspensão de outra propaganda do produto por até 60 dias e",["multa.","prisão.","perda de licença.","cassação de CNH.","perda de veículo."],"Art. 77-E.")
q(2,"No texto da travessia, o motorista que não parou para as crianças na faixa, sem semáforo, desrespeitou a regra da",["prioridade de passagem do pedestre sobre a faixa.","velocidade mínima.","luz alta.","buzina.","ultrapassagem."],"Art. 70, caput.","ctb3a")
q(2,"No texto do pedido da associação, o órgão de trânsito que não respondeu descumpriu o dever de",["responder, por escrito, sobre a possibilidade ou não de atendimento.","construir a faixa.","multar a associação.","aprovar o pedido.","negar o pedido."],"Art. 73, caput.","ctb3b")
q(2,"No texto do pedido da associação, a associação pediu, por escrito, uma faixa de pedestres e placa, o que se enquadra no direito do",["art. 72, que permite solicitar sinalização.","art. 70.","art. 74.","art. 77.","art. 79."],"Art. 72.","ctb3b")
q(2,"O § 2º do art. 75 determina que os serviços de rádio e difusão de sons e imagens explorados pelo poder público difundam as campanhas de trânsito com a frequência recomendada pelos órgãos do sistema, de forma",["gratuita.","onerosa.","opcional.","restrita.","sigilosa."],"Art. 75, § 2º.")
q(2,"Os órgãos executivos de trânsito deverão promover Escolas Públicas de Trânsito nos moldes e padrões estabelecidos pelo",["Contran.","Cetran.","Ministério da Educação.","Município.","Tribunal de Justiça."],"Art. 74, § 2º.")
# n=3
q(3,"Assinale a alternativa correta sobre a circulação de pedestres sem passeio ou acostamento.",["Em via urbana, na pista, pelos bordos, em fila única, com prioridade; em via rural, em sentido contrário ao dos veículos.","Em via urbana, em sentido contrário ao dos veículos.","Em via rural, no mesmo sentido dos veículos.","Em qualquer via, no meio da pista.","Em qualquer via, sem prioridade."],"Art. 68, §§ 2º e 3º.")
q(3,"Considere as afirmações. I. O pedestre na faixa, sem semáforo, tem prioridade. II. O ciclista desmontado empurrando a bicicleta equipara-se ao pedestre. III. O pedestre pode atravessar em qualquer ponto da via, ainda que haja faixa a 20 metros. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"Havendo faixa a até 50 m, o pedestre deve usá-la (art. 69).")
q(3,"Assinale a INCORRETA.",["O pedestre que atravessa fora da faixa, havendo faixa a 30 metros, não tem nenhum dever.","Os órgãos devem responder, por escrito, às solicitações dos cidadãos.","A educação para o trânsito é dever prioritário do sistema.","O ciclista desmontado equipara-se ao pedestre.","A publicidade de veículos deve ter mensagem educativa."],"Art. 69, caput: utilizar sempre as faixas a até 50 m.")
q(3,"A regra do art. 70, parágrafo único, protege o pedestre que",["não concluiu a travessia, mesmo quando o semáforo muda e libera os veículos.","chegou à faixa.","não olhou o semáforo.","atravessou fora da faixa.","parou no meio da pista."],"Art. 70, parágrafo único.")
q(3,"A educação para o trânsito deve ser promovida, segundo o art. 76, por meio de planejamento e ações coordenadas entre os órgãos e entidades do Sistema Nacional de Trânsito e de Educação, da União, dos Estados, do DF e dos",["Municípios.","particulares.","partidos.","sindicatos.","clubes."],"Art. 76, caput.")
q(3,"A publicidade que descumpre as regras de mensagem educativa acarreta a imediata suspensão da veiculação da peça até que cumpridas as exigências, nos termos do",["§ 2º do art. 77-E.","§ 1º do art. 77-E.","art. 77-B.","art. 77-C.","art. 77-D."],"Art. 77-E, § 2º.")
q(3,"A multa pelo descumprimento das regras de publicidade educativa é cobrada do dobro até o quíntuplo em caso de",["reincidência.","dolo.","culpa.","fraude.","revelia."],"Art. 77-E, III.")
q(3,"Os Ministérios da Saúde, da Educação, do Trabalho e Emprego, dos Transportes e da Justiça e Segurança Pública, por intermédio do Contran, desenvolverão programas destinados à",["prevenção de sinistros.","venda de veículos.","cobrança de multas.","fiscalização de velocidade.","abertura de vias."],"Art. 78, caput.")
q(3,"No art. 69, a regra “nas interseções e em suas proximidades, onde não existam faixas de travessia, atravessar na continuação da calçada” tem como cautela a de",["não adentrar na pista sem se certificar de que pode fazê-lo sem obstruir o trânsito de veículos.","correr.","parar.","olhar apenas para a direita.","fazer sinal ao motorista."],"Art. 69, III, a.")
q(3,"O órgão ou entidade com circunscrição sobre a via deve manter as faixas de pedestres em boas condições de",["visibilidade, higiene, segurança e sinalização.","preço.","cor, apenas.","largura, apenas.","extensão, apenas."],"Art. 71.")
q(3,"O Contran estabelece anualmente os temas e cronogramas das campanhas de âmbito nacional que deverão ser promovidas",["por todos os órgãos ou entidades do Sistema Nacional de Trânsito.","apenas pela União.","apenas pelos Estados.","apenas pelos Municípios.","apenas pelas escolas."],"Art. 75, caput.")
q(3,"Os órgãos do sistema poderão promover outras campanhas no âmbito de sua circunscrição e de acordo com as",["peculiaridades locais.","normas do Contran.","ordens do Ministério.","regras do Judiciário.","normas das escolas."],"Art. 75, § 1º.")
q(3,"O parágrafo único do art. 76 prevê que o Ministério da Educação, entre outras ações, promoverá a adoção, em todos os níveis de ensino, de um currículo interdisciplinar com conteúdo programático sobre",["segurança de trânsito.","direito penal.","direito civil.","economia.","geografia."],"Art. 76, parágrafo único, I.")
q(3,"Assinale a alternativa que associa corretamente o artigo ao tema.",["68: pedestre; 72: direito do cidadão; 74: educação para o trânsito; 77-B: publicidade da indústria automobilística.","68: educação; 72: pedestre.","74: cidadão; 77-B: pedestre.","72: publicidade; 77-B: educação.","68: publicidade; 74: pedestre."],"Arts. 68, 72, 74 e 77-B.")
q(3,"A prioridade do pedestre sobre os veículos, nos casos do art. 68, §§ 2º e 3º, é exceção nas situações em que a segurança ficar comprometida e em locais proibidos pela",["sinalização.","legislação municipal.","vontade do pedestre.","presença de agente.","chuva."],"Art. 68, §§ 2º e 3º.")
q(3,"A responsabilidade pelas campanhas educativas de trânsito é compartilhada por",["todos os órgãos ou entidades do Sistema Nacional de Trânsito.","apenas a União.","apenas os Estados.","apenas os Municípios.","apenas as escolas."],"Art. 75, caput.")
q(3,"O art. 77 estabelece que as campanhas de primeiros socorros terão caráter permanente por intermédio do",["Sistema Único de Saúde (SUS).","Contran.","Cetran.","Ministério da Educação.","Ministério da Justiça."],"Art. 77, parágrafo único.")
q(3,"No texto da travessia, a Guarda Municipal que presenciou o fato, ao orientar o motorista, está agindo em conformidade com a prioridade do",["pedestre sobre a faixa delimitada, sem semáforo.","motorista.","ciclista.","motociclista.","ônibus."],"Art. 70, caput.","ctb3a")
q(3,"No texto do pedido da associação, o órgão que não respondeu à solicitação feita por escrito não cumpriu o dever de responder,",["por escrito, dentro de prazos mínimos, sobre a possibilidade ou não de atendimento.","verbalmente.","por telefone.","apenas se atendesse.","apenas se multasse."],"Art. 73, caput.","ctb3b")
q(3,"No texto do pedido da associação, a omissão do órgão pode ser questionada porque o Código atribui ao cidadão e à entidade civil o direito de",["solicitar por escrito e de obter resposta fundamentada.","impor sinalização.","multar o órgão.","demitir o servidor.","votar o orçamento."],"Arts. 72 e 73.","ctb3b")
assert len(Q)==60,len(Q)
code,svg=mapa("Pedestres, cidadão e educação para o trânsito",[
 ("ped","O pedestre",["passeio e acostamento","pista: bordos, fila única","rural: sentido contrário"],"seção 1"),
 ("faixa","Travessia",["faixa a até 50 m: usar","sem faixa: perpendicular","faixa: prioridade, salvo semáforo"],"seção 1"),
 ("cic","Ciclista desmontado",["equipara-se ao pedestre","direitos e deveres","art. 68, § 1º"],"seção 1"),
 ("cid","Direito do cidadão",["pedir por escrito","órgão responde por escrito","justifica a análise"],"seção 2"),
 ("edu","Educação",["direito de todos","dever prioritário do sistema","campanhas permanentes"],"seção 3"),
 ("pub","Publicidade",["mensagem educativa","advertência, suspensão, multa","convênio com educação"],"seção 3")],
 "Na prova: o pedestre tem prioridade na faixa, exceto onde há semáforo")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira caixa trata de quem anda a pé; a segunda e a terceira, dos direitos e da educação de todos.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 68 a 79, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-3","Pedestres, cidadão e educação para o trânsito (CTB, arts. 68 a 79)",Q,list(tx),
 cobertura=["Recorte do edital: direitos, deveres e cidadania. Cobertos: arts. 68 a 79 (os arts. 77-A a 77-F e 78 de forma resumida)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O art. 78, parágrafo único, cita o SPVAT; a destinação de recursos não foi detalhada.","A consolidação mantém no art. 76 a expressão “escolas de 1º, 2º e 3º graus”, anterior à reforma do ensino.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb3a e ctb3b fictícios."],
 fontes_conferidas=["CTB, arts. 68 a 79: texto da Câmara, copiado por programa."])
gravar("ctb-3",aula_html,banco("ctb-3",Q),tx)
