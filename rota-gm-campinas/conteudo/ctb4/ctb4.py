import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A sinalização é a linguagem do trânsito: placas, pinturas, semáforos, apitos e gestos. O Código determina como ela deve ser colocada, quais são os tipos de sinal, quem prevalece quando há conflito e em que situação a multa deixa de valer porque a sinalização falhou. A Vunesp cobra os arts. 80 a 95 pela classificação dos sinais, pela ordem de prevalência (a mais cobrada), pela proibição de qualquer sinalização não prevista e pelas obras e eventos que exigem permissão prévia. O guarda é, ele mesmo, parte da sinalização, porque seus gestos prevalecem sobre tudo. A aula segue o texto consolidado."
S={}
S[1]="## 1. Como deve ser a sinalização\n\n"+L("art. 80, caput e § 1º","Art. 80. Sempre que necessário","§ 2º O órgão máximo executivo")+"\n\n"+L("art. 80, § 3º","§ 3º A responsabilidade pela instalação da sinalização","Art. 81.")+"\n\n"+L("art. 81","Art. 81. Nas vias públicas e nos imóveis","Art. 82.")+"\n\n"+L("art. 82","Art. 82. É proibido afixar sobre a sinalização","Art. 83.")+"\n\n"+L("art. 84","Art. 84. O órgão ou entidade de trânsito com circunscrição","Art. 85.")+"""

A sinalização é colocada ao longo da via, destinada a condutores e pedestres, vedada a utilização de qualquer outra além da prevista no Código e na legislação complementar. Deve ser colocada de modo perfeitamente visível e legível, de dia e de noite, em distância compatível com a segurança, conforme normas do Contran. A responsabilidade pela sinalização nas vias internas de condomínios e nos estacionamentos privados de uso coletivo é do proprietário. É proibido colocar, nas vias e nos imóveis, luzes, publicidade, inscrições, vegetação e mobiliário que possam gerar confusão ou interferir na visibilidade da sinalização, e é proibido afixar sobre a sinalização e seus suportes publicidade ou qualquer símbolo que não se relacione com a mensagem. O órgão de trânsito pode retirar ou determinar a imediata retirada do elemento que prejudique a visibilidade, com ônus para quem o colocou.
"""
S[2]="## 2. Tipos de sinais e ordem de prevalência\n\n"+L("art. 87","Art. 87. Os sinais de trânsito classificam-se em:","Art. 88.")+"\n\n"+L("art. 88","Art. 88. Nenhuma via pavimentada","Art. 89.")+"\n\n"+L("art. 89","Art. 89. A sinalização terá a seguinte ordem","Art. 90.")+"\n\n"+L("art. 90, caput e § 1º","Art. 90. Não serão aplicadas as sanções","§ 2º O CONTRAN editará")+"""

Os sinais classificam-se em verticais, horizontais, dispositivos de sinalização auxiliar, luminosos, sonoros e gestos do agente de trânsito e do condutor. Nenhuma via pavimentada pode ser entregue após a construção, ou reaberta após obras ou manutenção, enquanto não estiver devidamente sinalizada, vertical e horizontalmente.

A ordem de prevalência é a regra mais cobrada: primeiro as ordens do agente de trânsito, que prevalecem sobre as normas de circulação e sobre os demais sinais; depois as indicações do semáforo, sobre os demais sinais; e, por fim, as indicações dos sinais, sobre as demais normas de trânsito. Em outras palavras, o gesto do agente vence o semáforo, e o semáforo vence a placa. E, se a sinalização é insuficiente ou incorreta, não se aplicam as sanções por sua inobservância, e o órgão de trânsito responde pela falta, insuficiência ou incorreta colocação.
"""
S[3]="## 3. Engenharia de tráfego, obras e eventos\n\n"+L("art. 91","Art. 91. O CONTRAN estabelecerá","Art. 92.")+"\n\n"+L("art. 93","Art. 93. Nenhum projeto de edificação","Art. 94.")+"\n\n"+L("art. 94","Art. 94. Qualquer obstáculo","Art. 95.")+"\n\n"+L("art. 95, caput","Art. 95. Nenhuma obra ou evento","§ 1º A obrigação de sinalizar")+"\n\n"+L("art. 95, §§ 1º e 2º","§ 1º A obrigação de sinalizar","§ 3º O descumprimento")+"\n\n"+L("art. 95, §§ 3º e 4º","§ 3º O descumprimento do disposto neste artigo","CAPÍTULO IX")+"""

O Contran estabelece as normas a serem adotadas em todo o território nacional na engenharia de tráfego. Nenhum projeto de edificação que possa se tornar polo atrativo de trânsito pode ser aprovado sem anuência prévia do órgão com circunscrição sobre a via e sem área de estacionamento e indicação de vias de acesso adequadas. Todo obstáculo à livre circulação, que não possa ser retirado, deve ser imediatamente sinalizado, e é proibida a utilização de ondulações transversais e sonorizadores como redutores de velocidade, salvo casos especiais definidos pelo órgão competente nos padrões do Contran.

Nenhuma obra ou evento que possa perturbar ou interromper a circulação de veículos e pedestres, ou colocar em risco sua segurança, será iniciada sem permissão prévia do órgão de trânsito. A obrigação de sinalizar é do responsável pela obra ou evento. Salvo em emergência, a autoridade avisará a comunidade com quarenta e oito horas de antecedência, indicando caminhos alternativos. O descumprimento é punido com multa de R$ 81,35 a R$ 488,10, além de multa diária, e o servidor público responsável pela inobservância sofre multa diária equivalente a cinquenta por cento de um dia de vencimento.
"""
S[5]="""## 5. Na rotina do guarda

- **Gestos do agente:** a ordem do guarda de trânsito prevalece sobre o semáforo e sobre a placa. O condutor deve obedecer ao gesto, ainda que o semáforo esteja verde.
- **Sinalização falha:** se a placa é insuficiente ou incorreta, a infração não pode ser aplicada, e o agente deve registrar o problema ao órgão de trânsito.
- **Obras e eventos:** o evento ou obra que interrompa a circulação precisa de permissão prévia do órgão de trânsito, e o guarda confere a sinalização do desvio.
- **Obstáculos:** a presença de obstáculo não removido exige sinalização imediata.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Ordem de prevalência | Agente de trânsito, depois semáforo, depois sinais |
| Gesto do agente contra o semáforo | O gesto do agente prevalece |
| Tipos de sinais | Verticais, horizontais, auxiliares, luminosos, sonoros, gestos |
| Multa com sinalização falha | Não se aplicam sanções quando a sinalização é insuficiente ou incorreta |
| Quem responde pela falta de sinalização | O órgão ou entidade de trânsito com circunscrição sobre a via |
| Aviso de interdição de via | Quarenta e oito horas de antecedência, salvo emergência |
| Obra ou evento sem permissão | Multa de R$ 81,35 a R$ 488,10 e multa diária |
| Quem sinaliza a obra | O responsável pela execução ou manutenção |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Sinais | Verticais, horizontais, auxiliares, luminosos, sonoros, gestos |
| Prevalência | Agente de trânsito, semáforo, sinais |
| Sinalização falha | Sem sanção por inobservância; órgão responde |
| Vedação | Qualquer sinalização que não a prevista no Código |
| Obstáculo | Sinalizar imediatamente |
| Ondulações e sonorizadores | Proibidos como redutores, salvo casos especiais |
| Obras e eventos | Permissão prévia; responsável sinaliza |
| Interdição | Aviso com 48 horas, salvo emergência |
"""
QR=[("Questão 1","Segundo o Código de Trânsito, a sinalização terá a seguinte ordem de prevalência:",["as ordens do agente de trânsito, as indicações do semáforo e as indicações dos sinais.","as indicações dos sinais, do semáforo e do agente.","o semáforo, o agente e os sinais.","os sinais, o agente e o semáforo.","o agente e os sinais, sem o semáforo."],0,"Art. 89."),
("Questão 2","Não serão aplicadas as sanções previstas no Código por inobservância à sinalização quando esta for",["insuficiente ou incorreta.","antiga.","de cor desbotada, apenas.","vertical.","horizontal."],2,"Art. 90, caput."),
("Questão 3","Os sinais de trânsito classificam-se em verticais, horizontais, dispositivos de sinalização auxiliar, luminosos, sonoros e",["gestos do agente de trânsito e do condutor.","sinais de fumaça.","sinais postais.","sinais de bandeira.","sinais de rádio."],1,"Art. 87."),
("Questão 4","A obrigação de sinalizar obra ou evento que possa perturbar a circulação é do",["responsável pela execução ou manutenção da obra ou do evento.","Contran.","Cetran.","motorista.","pedestre."],4,"Art. 95, § 1º.")]
t1="<strong>Gesto contra o semáforo</strong><br><br>Em um cruzamento de Vila Nova, cidade fictícia, o semáforo estava verde, mas um guarda de trânsito, em razão de um acidente à frente, fez sinal de parada. O motorista, vendo o verde, avançou."
t2="<strong>Placa que não existia</strong><br><br>Um motorista foi autuado por estacionar em local onde, depois se comprovou, a placa de proibição havia sido arrancada e não havia sinalização horizontal. O motorista recorreu."
tx={"ctb4a":t1,"ctb4b":t2}
# n=1
q(1,"Sempre que necessário, será colocada ao longo da via a sinalização prevista no Código e na legislação complementar, destinada a condutores e pedestres, vedada a utilização de",["qualquer outra.","placas verticais.","sinais luminosos.","sinais horizontais.","sinais auxiliares."],"Art. 80, caput.")
q(1,"A sinalização será colocada em posição e condições que a tornem perfeitamente visível e legível durante",["o dia e a noite.","o dia, apenas.","a noite, apenas.","a chuva, apenas.","o verão, apenas."],"Art. 80, § 1º.")
q(1,"A responsabilidade pela instalação da sinalização nas vias internas de condomínios é de",["seu proprietário.","do Município.","do Estado.","do Contran.","do Cetran."],"Art. 80, § 3º.")
q(1,"Nas vias públicas e nos imóveis é proibido colocar luzes, publicidade, inscrições, vegetação e mobiliário que possam gerar confusão ou interferir na visibilidade da",["sinalização.","paisagem.","calçada.","iluminação pública.","arborização."],"Art. 81.")
q(1,"É proibido afixar sobre a sinalização de trânsito e seus suportes qualquer tipo de publicidade, inscrições, legendas e símbolos que",["não se relacionem com a mensagem da sinalização.","se relacionem com a mensagem.","sejam pequenos.","sejam coloridos.","sejam temporários."],"Art. 82.")
q(1,"A afixação de publicidade ao longo das vias condiciona-se à prévia aprovação do",["órgão ou entidade com circunscrição sobre a via.","Contran.","Cetran.","Ministério Público.","juiz."],"Art. 83.")
q(1,"O órgão de trânsito com circunscrição sobre a via poderá retirar elemento que prejudique a visibilidade da sinalização, com ônus para",["quem o tenha colocado.","o Município.","o Estado.","o pedestre.","o motorista."],"Art. 84.")
q(1,"Os locais destinados à travessia de pedestres deverão ser sinalizados com",["faixas pintadas ou demarcadas no leito da via.","placas apenas.","semáforos apenas.","lombadas.","cones."],"Art. 85.")
q(1,"Os sinais de trânsito classificam-se, entre outros, em verticais, horizontais e",["luminosos.","térmicos.","olfativos.","táteis.","magnéticos."],"Art. 87.")
q(1,"Nenhuma via pavimentada poderá ser entregue após sua construção enquanto não estiver devidamente sinalizada, vertical e",["horizontalmente.","provisoriamente.","parcialmente.","apenas em parte.","em período diurno."],"Art. 88.")
q(1,"Na ordem de prevalência da sinalização, o primeiro lugar é das ordens do",["agente de trânsito.","semáforo.","sinais verticais.","sinais horizontais.","Contran."],"Art. 89, I.")
q(1,"Na ordem de prevalência da sinalização, as indicações do semáforo prevalecem sobre",["os demais sinais.","as ordens do agente.","as normas de circulação do agente.","todas as normas.","as ordens do juiz."],"Art. 89, II.")
q(1,"Na ordem de prevalência da sinalização, as indicações dos sinais prevalecem sobre",["as demais normas de trânsito.","o agente.","o semáforo.","o Contran.","a lei."],"Art. 89, III.")
q(1,"Quem responde pela falta, insuficiência ou incorreta colocação da sinalização é o órgão ou entidade de trânsito com",["circunscrição sobre a via.","sede na capital.","poder de polícia federal.","atuação nacional.","apenas competência rodoviária."],"Art. 90, § 1º.")
q(1,"O Contran estabelecerá as normas e regulamentos a serem adotados em todo o território nacional na implementação das soluções da",["Engenharia de Tráfego.","Engenharia Civil.","Engenharia Elétrica.","Engenharia Naval.","Engenharia Mecânica."],"Art. 91.")
q(1,"Nenhum projeto de edificação que possa transformar-se em polo atrativo de trânsito poderá ser aprovado sem prévia anuência do",["órgão ou entidade com circunscrição sobre a via.","Contran.","Ministério Público.","juiz.","vizinho."],"Art. 93.")
q(1,"Qualquer obstáculo à livre circulação e à segurança de veículos e pedestres, na via ou na calçada, caso não possa ser retirado, deve ser devida e imediatamente",["sinalizado.","removido.","coberto.","ignorado.","aterrado."],"Art. 94, caput.")
q(1,"É proibida a utilização das ondulações transversais e de sonorizadores como redutores de velocidade, salvo em",["casos especiais definidos pelo órgão ou entidade competente, nos padrões do Contran.","qualquer caso.","vias urbanas.","vias rurais.","escolas."],"Art. 94, parágrafo único.")
q(1,"No texto do gesto contra o semáforo, o motorista deveria ter obedecido ao",["gesto do agente de trânsito, que prevalece sobre o semáforo.","semáforo verde.","vizinho.","passageiro.","carro à frente."],"Art. 89, I.","ctb4a")
q(1,"No texto da placa que não existia, o motorista autuado onde não havia sinalização",["não pode ser sancionado, pois a sinalização era insuficiente ou incorreta.","deve ser multado.","deve perder a CNH.","deve ser preso.","deve ser notificado novamente."],"Art. 90, caput.","ctb4b")
# n=2
q(2,"O órgão máximo executivo de trânsito da União poderá autorizar, em caráter experimental e por período prefixado, a utilização de",["sinalização e equipamentos não previstos no Código.","ordens verbais.","gestos de cidadãos.","placas particulares.","semáforos de empresas."],"Art. 80, § 2º.")
q(2,"A sinalização das vias internas de condomínios constituídos por unidades autônomas será implantada e mantida às expensas do condomínio, após aprovação dos projetos pelo órgão com circunscrição sobre a via, nos termos do",["art. 51.","art. 1º.","art. 68.","art. 80.","art. 95."],"Art. 51.")
q(2,"Os locais destinados a postos de gasolina, oficinas, estacionamentos ou garagens de uso coletivo deverão ter suas entradas e saídas devidamente",["identificadas, na forma regulamentada pelo Contran.","pintadas de vermelho.","iluminadas à noite, apenas.","fechadas à noite.","cercadas."],"Art. 86.")
q(2,"As vagas de estacionamento regulamentado a que se refere o art. 86-A devem ser sinalizadas com placas indicativas de destinação e com placas informando dados sobre a infração por",["estacionamento indevido.","excesso de velocidade.","embriaguez.","falta de cinto.","falta de CNH."],"Art. 86-A.")
q(2,"O Contran editará normas complementares sobre a interpretação, a colocação e o uso da",["sinalização.","legislação penal.","legislação civil.","legislação tributária.","legislação trabalhista."],"Art. 90, § 2º.")
q(2,"Nas vias ou trechos de vias em obras deverá ser afixada sinalização",["específica e adequada.","genérica.","apenas verbal.","apenas luminosa.","apenas horizontal."],"Art. 88, parágrafo único.")
q(2,"Nenhuma obra ou evento que possa perturbar ou interromper a livre circulação será iniciada sem",["permissão prévia do órgão ou entidade de trânsito com circunscrição sobre a via.","comunicação ao vizinho.","autorização do juiz.","pagamento de taxa.","aviso por carta."],"Art. 95, caput.")
q(2,"A obrigação de sinalizar a obra ou o evento é do",["responsável pela execução ou manutenção da obra ou do evento.","pedestre.","motorista.","Contran.","Município, em qualquer caso."],"Art. 95, § 1º.")
q(2,"Salvo em emergência, a autoridade de trânsito avisará a comunidade, por meio de comunicação social, com antecedência de",["quarenta e oito horas, de qualquer interdição da via.","vinte e quatro horas.","setenta e duas horas.","cinco dias.","dez dias."],"Art. 95, § 2º.")
q(2,"No aviso de interdição de via, a autoridade deve indicar também",["os caminhos alternativos a serem utilizados.","o responsável pelo erro.","o valor das multas.","os feriados.","o horário do comércio."],"Art. 95, § 2º.")
q(2,"O descumprimento do art. 95 será punido com multa de R$ 81,35 a R$ 488,10, independentemente das cominações cíveis e penais, além de",["multa diária no mesmo valor até a regularização.","prisão.","perda de licença.","cassação da CNH.","suspensão do direito de dirigir."],"Art. 95, § 3º.")
q(2,"Ao servidor público responsável pela inobservância das normas dos arts. 93, 94 e 95, a autoridade de trânsito aplicará multa diária de",["cinquenta por cento do dia de vencimento ou remuneração.","um salário mínimo.","dez por cento do salário.","um dia de salário.","dois dias de salário."],"Art. 95, § 4º.")
q(2,"Os veículos de tração animal, bicicletas e pedestres também são destinatários da sinalização, uma vez que a sinalização se destina a",["condutores e pedestres.","motoristas apenas.","pedestres apenas.","ciclistas apenas.","motociclistas apenas."],"Art. 80, caput.")
q(2,"O art. 90 isenta de sanção quem inobserva a sinalização quando esta for insuficiente ou incorreta porque a responsabilidade pela implantação é do",["órgão ou entidade de trânsito com circunscrição sobre a via.","motorista.","pedestre.","agente de trânsito.","Contran."],"Art. 90, § 1º.")
q(2,"No texto do gesto contra o semáforo, o fundamento legal da prevalência do gesto do agente é o art.",["89, I.","81.","87.","93.","95."],"Art. 89, I.","ctb4a")
q(2,"No texto do gesto contra o semáforo, o gesto do agente é espécie de sinal classificado como",["gesto do agente de trânsito.","sinal luminoso.","sinal vertical.","sinal horizontal.","dispositivo auxiliar."],"Art. 87, VI.","ctb4a")
q(2,"No texto da placa que não existia, quem responde pela falta da sinalização é o",["órgão ou entidade de trânsito com circunscrição sobre a via.","motorista.","pedestre.","vizinho.","fabricante da placa."],"Art. 90, § 1º.","ctb4b")
q(2,"O Contran estabelecerá as normas e regulamentos a serem adotados em todo o território nacional na implementação das soluções da Engenharia de Tráfego, bem como os",["padrões a serem praticados por todos os órgãos e entidades do Sistema Nacional de Trânsito.","preços dos serviços.","salários dos agentes.","horários das escolas.","tarifas de ônibus."],"Art. 91.")
q(2,"A afixação de publicidade ao longo das vias, nos termos do art. 83, condiciona-se à prévia aprovação do órgão ou entidade",["com circunscrição sobre a via.","com sede na capital.","com competência federal.","com atuação nacional.","privado."],"Art. 83.")
q(2,"A proibição de colocar vegetação e mobiliário que possam gerar confusão com a sinalização está no art.",["81.","80.","82.","83.","84."],"Art. 81.")
# n=3
q(3,"Assinale a alternativa que traz a ordem correta de prevalência da sinalização.",["Agente de trânsito, semáforo, sinais.","Semáforo, agente, sinais.","Sinais, semáforo, agente.","Agente, sinais, semáforo.","Semáforo, sinais, agente."],"Art. 89.")
q(3,"Considere as afirmações. I. O gesto do agente de trânsito prevalece sobre o semáforo. II. A sinalização incorreta afasta as sanções por inobservância. III. É permitida qualquer sinalização que o órgão queira colocar. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"É vedada a utilização de sinalização não prevista (art. 80, caput).")
q(3,"Assinale a INCORRETA.",["O semáforo prevalece sobre as ordens do agente de trânsito.","A sinalização incorreta afasta as sanções por inobservância.","É proibido afixar publicidade sobre a sinalização.","As obras e eventos que perturbem a circulação dependem de permissão prévia.","O responsável pela obra deve sinalizá-la."],"As ordens do agente prevalecem sobre o semáforo (art. 89, I e II).")
q(3,"O art. 87 inclui, entre os sinais de trânsito, os gestos do agente de trânsito e",["do condutor.","do pedestre.","do passageiro.","do ciclista apenas.","do vizinho."],"Art. 87, VI.")
q(3,"A sanção de multa diária ao servidor público responsável pela inobservância dos arts. 93, 94 e 95 é equivalente a",["cinquenta por cento do dia de vencimento ou remuneração devida, enquanto permanecer a irregularidade.","um dia de salário.","um salário mínimo.","dez por cento do salário.","dois dias de salário."],"Art. 95, § 4º.")
q(3,"A obra ou evento sem permissão prévia sujeita-se a multa de R$ 81,35 a R$ 488,10, independentemente das cominações",["cíveis e penais cabíveis.","apenas administrativas.","apenas tributárias.","apenas trabalhistas.","apenas eleitorais."],"Art. 95, § 3º.")
q(3,"A multa diária, na hipótese do § 3º do art. 95, é cobrada a partir do prazo final concedido pela autoridade de trânsito, levando-se em consideração a",["dimensão da obra ou do evento e o prejuízo causado ao trânsito.","idade do responsável.","natureza do contrato.","cor da placa.","velocidade do tráfego."],"Art. 95, § 3º.")
q(3,"O art. 93 exige, para aprovar projeto de edificação que possa se tornar polo atrativo de trânsito, que dele conste área para estacionamento e",["indicação das vias de acesso adequadas.","projeto de decoração.","contrato de segurança.","alvará de lazer.","seguro de vida."],"Art. 93.")
q(3,"Segundo o art. 94, parágrafo único, ondulações transversais e sonorizadores como redutores de velocidade são",["proibidos, salvo casos especiais definidos pelo órgão competente.","permitidos em qualquer caso.","obrigatórios em escolas.","obrigatórios em hospitais.","permitidos apenas em estradas."],"Art. 94, parágrafo único.")
q(3,"A sinalização das vias e áreas de estacionamento de estabelecimentos privados de uso coletivo é de responsabilidade de seu",["proprietário.","Município.","Estado.","Contran.","JARI."],"Art. 80, § 3º.")
q(3,"A diferença entre as sinalizações vertical e horizontal está em que a vertical é composta por placas e a horizontal por",["marcas pintadas no leito da via (como faixas).","semáforos.","cones.","gestos.","apitos."],"Art. 87, I e II; art. 85.")
q(3,"A sinalização sonora do art. 87 inclui, por exemplo,",["o apito do agente de trânsito.","a buzina do motorista.","a música de rua.","o grito do pedestre.","o alarme residencial."],"Art. 87, V (sinais sonoros).")
q(3,"A ordem de prevalência da sinalização, como regra de conflito, vale quando houver",["divergência entre o agente, o semáforo e os sinais.","qualquer dúvida do motorista.","pedido do passageiro.","ausência de sinalização.","sinalização uniforme."],"Art. 89.")
q(3,"Assinale a alternativa correta sobre a retirada de elementos que prejudiquem a sinalização.",["O órgão de trânsito pode retirar ou determinar a imediata retirada, com ônus para quem tenha colocado o elemento.","O órgão deve pedir autorização ao juiz.","O ônus é do órgão de trânsito.","A retirada depende do Contran.","A retirada só pode ocorrer após 48 horas."],"Art. 84.")
q(3,"A multa diária prevista no § 3º do art. 95 é do mesmo valor da multa principal e é aplicada",["até a regularização da situação, a partir do prazo final concedido pela autoridade.","por uma única vez.","por três dias.","por trinta dias.","por um ano."],"Art. 95, § 3º.")
q(3,"Assinale a alternativa que associa corretamente o artigo ao tema.",["Art. 87: tipos de sinais; art. 89: prevalência; art. 90: sinalização insuficiente; art. 95: obras e eventos.","Art. 87: prevalência; art. 89: tipos de sinais.","Art. 90: obras; art. 95: prevalência.","Art. 89: obras; art. 87: sinalização insuficiente.","Art. 95: tipos de sinais; art. 90: prevalência."],"Arts. 87, 89, 90 e 95.")
q(3,"Assinale a INCORRETA sobre obras e eventos na via.",["A obrigação de sinalizar é do órgão de trânsito, em qualquer caso.","Dependem de permissão prévia do órgão de trânsito.","O descumprimento gera multa e multa diária.","A autoridade avisa a comunidade com quarenta e oito horas, salvo emergência.","O servidor responsável pela inobservância sofre multa diária."],"Art. 95, § 1º: a obrigação de sinalizar é do responsável pela obra ou evento.")
q(3,"No texto do gesto contra o semáforo, o motorista que desobedeceu ao gesto do agente praticou infração porque a ordem do agente prevalece sobre",["as normas de circulação e outros sinais, inclusive o semáforo.","a lei.","a Constituição.","a sentença.","a ordem do juiz."],"Art. 89, I.","ctb4a")
q(3,"No texto da placa que não existia, o recurso do motorista deve ser acolhido porque o art. 90 afasta as sanções quando a sinalização é",["insuficiente ou incorreta.","correta.","presente.","completa.","visível."],"Art. 90, caput.","ctb4b")
q(3,"No texto da placa que não existia, a ausência de placa e de sinalização horizontal acarreta, para o órgão de trânsito, a responsabilidade pela",["falta, insuficiência ou incorreta colocação da sinalização.","multa do motorista.","retirada do carro.","cassação da CNH.","lavratura de boletim."],"Art. 90, § 1º.","ctb4b")
assert len(Q)==60,len(Q)
code,svg=mapa("Sinalização e engenharia de tráfego",[
 ("como","Como é a sinalização",["visível e legível, de dia e à noite","só a prevista no Código","proibida publicidade sobre ela"],"seção 1"),
 ("tipos","Tipos de sinais",["verticais e horizontais","luminosos e sonoros","gestos e auxiliares"],"seção 2"),
 ("prev","Prevalência",["1º agente de trânsito","2º semáforo","3º sinais"],"seção 2"),
 ("falha","Sinalização falha",["sem sanção por inobservância","órgão responde","art. 90"],"seção 2"),
 ("obra","Obras e eventos",["permissão prévia","responsável sinaliza","aviso de 48 horas"],"seção 3"),
 ("obst","Obstáculos",["sinalizar imediatamente","ondulações: proibidas, em regra","art. 94"],"seção 3")],
 "Na prova: o gesto do agente prevalece sobre o semáforo, e o semáforo sobre a placa")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"As duas primeiras caixas dizem como deve ser a sinalização e quem prevalece; as demais, o que se exige de obras e obstáculos.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 80 a 95, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-4","Sinalização, engenharia, operação e fiscalização (CTB, arts. 80 a 95)",Q,list(tx),
 cobertura=["Recorte do edital: tipos de sinais e ordem de prevalência. Cobertos: arts. 80 a 95 (os arts. 83, 85, 86, 86-A e 92 de forma resumida)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O Anexo II do CTB (sinalização), que detalha placas, marcas e cores, não foi consultado.","Os valores das multas do art. 95 são os do texto consolidado e podem ter sido atualizados.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb4a e ctb4b fictícios."],
 fontes_conferidas=["CTB, arts. 80 a 95: texto da Câmara, copiado por programa."])
gravar("ctb-4",aula_html,banco("ctb-4",Q),tx)
