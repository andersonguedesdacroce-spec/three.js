import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEI
F='ctb.txt'
C=lambda ref,txt: LEI(ref,txt,F)
A=lambda txt: C("Anexo I",txt)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Anexo I do CTB é o glossário do Código: diz o que é via arterial, o que é parada e o que é estacionamento, a diferença entre ultrapassagem e passagem, entre ciclovia e ciclofaixa, entre motocicleta e motoneta. A Vunesp adora cobrar essas definições ao pé da letra, trocando uma pela outra. Como o edital cobra o CTB inteiro, este posto reúne os conceitos mais cobrados, organizados em três blocos: vias, manobras e imobilizações, e veículos e agentes."
S={}
S[1]="## 1. Vias e suas partes\n\n"+A("VIA DE TRÂNSITO RÁPIDO - aquela caracterizada por acessos especiais com trânsito livre, sem interseções em nível, sem acessibilidade direta aos lotes lindeiros e sem travessia de pedestres em nível.")+"\n\n"+A("VIA ARTERIAL - aquela caracterizada por interseções em nível, geralmente controlada por semáforo, com acessibilidade aos lotes lindeiros e às vias secundárias e locais, possibilitando o trânsito entre as regiões da cidade.")+"\n\n"+A("VIA COLETORA - aquela destinada a coletar e distribuir o trânsito que tenha necessidade de entrar ou sair das vias de trânsito rápido ou arteriais, possibilitando o trânsito dentro das regiões da cidade.")+"\n\n"+A("VIA LOCAL - aquela caracterizada por interseções em nível não semaforizadas, destinada apenas ao acesso local ou a áreas restritas.")+"\n\n"+A("VIA RURAL - estradas e rodovias.")+" "+A("ESTRADA - via rural não pavimentada.")+" "+A("RODOVIA - via rural pavimentada.")+"\n\n"+A("CICLOVIA - pista própria destinada à circulação de ciclos, separada fisicamente do tráfego comum.")+"\n\n"+A("CICLOFAIXA - parte da pista de rolamento destinada à circulação exclusiva de ciclos, delimitada por sinalização específica.")+"\n\n"+A("ACOSTAMENTO - parte da via diferenciada da pista de rolamento destinada à parada ou estacionamento de veículos, em caso de emergência, e à circulação de pedestres e bicicletas, quando não houver local apropriado para esse fim.")+"""

**Escada das vias urbanas (da mais rápida para a mais lenta)**

| Via | Marca registrada | Velocidade máxima sem sinalização (art. 61) |
| --- | --- | --- |
| Trânsito rápido | **Sem** interseção em nível, **sem** acesso aos lotes, **sem** travessia de pedestre em nível | 80 km/h |
| Arterial | Interseção em nível, **semáforo**, trânsito **entre** regiões | 60 km/h |
| Coletora | **Coleta e distribui**; trânsito **dentro** das regiões | 40 km/h |
| Local | Interseções **sem semáforo**; acesso local | 30 km/h |

> **Macete:** **E**strada é de t**E**rra (não pavimentada); **R**odovia é **R**evestida (pavimentada).

> **Cuidado!** **Ciclovia** é **separada fisicamente**; **ciclofaixa** é parte da pista, **só pintada** (sinalização).

| Parte da via | Para que serve |
| --- | --- |
| Calçada | Não é para veículos; pedestres e mobiliário urbano |
| Passeio | Parte da calçada (ou da pista, separada) só para pedestres e, excepcionalmente, ciclistas |
| Refúgio | Parte sinalizada e protegida para o pedestre durante a travessia |
| Ilha | Obstáculo físico na pista para ordenar fluxos em interseção |
| Canteiro central | Separa as pistas |
"""
S[2]="## 2. Manobras e imobilizações\n\n"+A("ULTRAPASSAGEM - movimento de passar à frente de outro veículo que se desloca no mesmo sentido, em menor velocidade e na mesma faixa de tráfego, necessitando sair e retornar à faixa de origem.")+"\n\n"+A("PASSAGEM POR OUTRO VEÍCULO - movimento de passagem à frente de outro veículo que se desloca no mesmo sentido, em menor velocidade, mas em faixas distintas da via.")+"\n\n"+A("TRANSPOSIÇÃO DE FAIXAS - passagem de um veículo de uma faixa demarcada para outra.")+"\n\n"+A("CONVERSÃO - movimento em ângulo, à esquerda ou à direita, de mudança da direção original do veículo.")+"\n\n"+A("PARADA - imobilização do veículo com a finalidade e pelo tempo estritamente necessário para efetuar embarque ou desembarque de passageiros.")+"\n\n"+A("ESTACIONAMENTO - imobilização de veículos por tempo superior ao necessário para embarque ou desembarque de passageiros.")+"\n\n"+A("INTERRUPÇÃO DE MARCHA - imobilização do veículo para atender circunstância momentânea do trânsito.")+"\n\n"+A("NOITE - período do dia compreendido entre o pôr-do-sol e o nascer do sol.")+"""

| Movimento | Mesma faixa? | Sai e volta? |
| --- | --- | --- |
| **Ultrapassagem** | **Sim** | **Sim** |
| **Passagem** por outro veículo | **Não** (faixas distintas) | Não |
| **Transposição** de faixas | Muda de uma faixa para outra | Não precisa voltar |

| Imobilização | Por quê | Por quanto tempo |
| --- | --- | --- |
| **Interrupção de marcha** | Circunstância **momentânea** do trânsito (semáforo, congestionamento) | O necessário |
| **Parada** | **Embarque ou desembarque** de passageiros | **Estritamente** necessário |
| **Estacionamento** | Qualquer outro motivo | **Superior** ao do embarque e desembarque |

> **Cai muito:** parar o carro para **descarregar mercadorias** por mais tempo do que o necessário para o embarque ou desembarque de **pessoas** é **estacionamento**, não parada.
"""
S[3]="## 3. Veículos, trânsito e agentes\n\n"+A("TRÂNSITO - movimentação e imobilização de veículos, pessoas e animais nas vias terrestres.")+"\n\n"+A("AUTOMÓVEL - veículo automotor destinado ao transporte de passageiros, com capacidade para até oito pessoas, exclusive o condutor.")+"\n\n"+A("MOTOCICLETA - veículo automotor de duas rodas, com ou sem \"side-car\", dirigido por condutor em posição montada.")+"\n\n"+A("MOTONETA - veículo automotor de duas rodas, dirigido por condutor em posição sentada.")+"\n\n"+A("BICICLETA - veículo de propulsão humana, dotado de duas rodas, não sendo, para efeito deste Código, similar à motocicleta, motoneta e ciclomotor.")+"\n\n"+A("AUTORIDADE DE TRÂNSITO - dirigente máximo de órgão ou entidade executivo integrante do Sistema Nacional de Trânsito ou pessoa por ele expressamente credenciada.")+"\n\n"+A("INFRAÇÃO - inobservância a qualquer preceito da legislação de trânsito, às normas emanadas do Código de Trânsito, do Conselho Nacional de Trânsito e a regulamentação estabelecida pelo órgão ou entidade executiva do trânsito.")+"\n\n"+A("SINISTRO DE TRÂNSITO - evento que resulta em dano ao veículo ou à sua carga e/ou em lesões a pessoas ou animais e que pode trazer dano material ou prejuízo ao trânsito, à via ou ao meio ambiente, em que pelo menos uma das partes está em movimento nas vias terrestres ou em áreas abertas ao público.")+"""

| Veículo | Como reconhecer |
| --- | --- |
| Automóvel | Passageiros, **até 8 pessoas além do condutor** |
| Motocicleta | Duas rodas, condutor **montado** |
| Motoneta | Duas rodas, condutor **sentado** (tipo "scooter") |
| Ciclomotor | 2 ou 3 rodas, até **50 cm³** ou elétrico até **4 kW**, máximo **50 km/h** |
| Bicicleta | Propulsão **humana**, duas rodas; **não** é similar à moto |
| Caminhonete | **Carga**, peso bruto total até **3.500 kg** |
| Camioneta | **Misto**: passageiros e carga no **mesmo compartimento** |
| Utilitário | Misto, versátil, inclusive fora de estrada |

> **Cuidado!** O CTB hoje usa **"sinistro de trânsito"** (Lei 14.599/2023) no lugar de "acidente". **Autoridade** de trânsito é o **dirigente máximo** do órgão; o **agente** é quem fiscaliza e lavra o auto.

> **Macete:** caminhone**T**e = **T**ransporte de carga; camione**T**a = **T**udo junto (misto).
"""
S[5]="""## 5. Na rotina do guarda

- **Boletim de ocorrência:** use os termos do Anexo I: "sinistro de trânsito", "via arterial", "estacionado" ou "parado". A descrição correta evita nulidade no auto.
- **Carro de entrega na faixa:** se fica além do tempo de embarque e desembarque, é **estacionamento**.
- **Ciclista na ciclofaixa:** a faixa é exclusiva de ciclos; o carro que a invade pode cometer infração de trânsito.
- **Veículo abandonado:** o Anexo I define veículo em estado de abandono como o que não se locomove por meios próprios e oferece risco à saúde, à segurança ou ao meio ambiente, ainda que em local permitido.
- **Policiamento ostensivo de trânsito:** é função das **Polícias Militares**; a guarda atua na fiscalização quando houver convênio (CTB, art. 25-A e art. 280, § 4º).
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Estrada x rodovia | Estrada: não pavimentada. Rodovia: pavimentada |
| Ciclovia x ciclofaixa | Ciclovia: separada fisicamente. Ciclofaixa: sinalização na pista |
| Parada x estacionamento | Parada: só o tempo do embarque ou desembarque |
| Ultrapassagem x passagem | Ultrapassagem: mesma faixa, sai e volta. Passagem: faixas distintas |
| Via arterial x coletora | Arterial: entre regiões, semáforo. Coletora: dentro das regiões |
| Via de trânsito rápido | Sem interseção em nível e sem travessia de pedestre em nível |
| Motocicleta x motoneta | Montado x sentado |
| Automóvel | Até 8 pessoas, sem contar o condutor |
| Caminhonete x camioneta | Carga (3.500 kg) x misto |
| Noite | Do pôr do sol ao nascer do sol |
"""
S[7]="""## 7. Quadro-resumo

| Conceito | Definição em poucas palavras |
| --- | --- |
| Trânsito | Movimentação e imobilização de veículos, pessoas e animais nas vias terrestres |
| Trânsito rápido | Sem interseção em nível, sem acesso a lotes, sem travessia em nível |
| Arterial | Semáforo; entre regiões da cidade |
| Coletora | Coleta e distribui; dentro das regiões |
| Local | Sem semáforo; acesso local |
| Estrada / Rodovia | Rural não pavimentada / pavimentada |
| Ciclovia / Ciclofaixa | Separada fisicamente / delimitada por sinalização |
| Ultrapassagem | Mesma faixa, sai e retorna |
| Passagem | Faixas distintas |
| Parada | Embarque ou desembarque, tempo estritamente necessário |
| Estacionamento | Tempo superior ao da parada |
| Automóvel | Até 8 pessoas além do condutor |
| Motocicleta / Motoneta | Montado / sentado |
| Ciclomotor | Até 50 cm³ ou 4 kW; até 50 km/h |
| Autoridade de trânsito | Dirigente máximo do órgão executivo ou pessoa credenciada |
| Sinistro de trânsito | Evento com dano ou lesão, ao menos uma parte em movimento |
"""
QR=[("Questão 1","Segundo o Anexo I do CTB, a via caracterizada por interseções em nível, geralmente controlada por semáforo, que possibilita o trânsito entre as regiões da cidade, é a via",["arterial.","coletora.","local.","de trânsito rápido.","rural."],0,"Anexo I, via arterial."),
("Questão 2","A imobilização do veículo pelo tempo estritamente necessário para efetuar embarque ou desembarque de passageiros denomina-se",["parada.","estacionamento.","interrupção de marcha.","retenção.","remoção."],1,"Anexo I, parada."),
("Questão 3","Rodovia é a via rural",["pavimentada.","não pavimentada.","urbana.","sem sinalização.","de trânsito rápido."],2,"Anexo I, rodovia."),
("Questão 4","A parte da pista de rolamento destinada à circulação exclusiva de ciclos, delimitada por sinalização específica, é a",["ciclofaixa.","ciclovia.","calçada.","passeio.","acostamento."],3,"Anexo I, ciclofaixa.")]
t1="<strong>A van de entregas</strong><br><br>Uma van parou junto ao meio-fio de uma avenida com semáforos que liga o Centro a outras regiões de Campinas e ficou vinte minutos descarregando caixas."
t2="<strong>A motoneta e a ciclofaixa</strong><br><br>Um condutor de motoneta trafegava sobre a faixa pintada na pista, destinada aos ciclistas, para fugir do congestionamento."
t3="<strong>O sinistro na rodovia</strong><br><br>Dois carros colidiram em uma via rural pavimentada próxima ao limite do município, ferindo um motorista; a guarda municipal apoiou a sinalização do local."
tx={"ctb12a":t1,"ctb12b":t2,"ctb12c":t3}
# n=1
q(1,"Estrada, segundo o Anexo I do CTB, é a via rural",["não pavimentada.","pavimentada.","urbana.","de trânsito rápido.","arterial."],"Anexo I.")
q(1,"A via rural pavimentada denomina-se",["rodovia.","estrada.","via local.","via coletora.","ciclovia."],"Anexo I.")
q(1,"A via caracterizada por interseções em nível não semaforizadas, destinada apenas ao acesso local, é a via",["local.","arterial.","coletora.","de trânsito rápido.","rural."],"Anexo I.")
q(1,"A via sem interseções em nível, sem acessibilidade direta aos lotes lindeiros e sem travessia de pedestres em nível é a via",["de trânsito rápido.","arterial.","coletora.","local.","rural."],"Anexo I.")
q(1,"A pista própria destinada à circulação de ciclos, separada fisicamente do tráfego comum, é a",["ciclovia.","ciclofaixa.","calçada.","faixa de pedestres.","ilha."],"Anexo I.")
q(1,"A imobilização de veículos por tempo superior ao necessário para embarque ou desembarque de passageiros é o",["estacionamento.","parada.","retorno.","bloqueio.","sinistro."],"Anexo I.")
q(1,"A imobilização do veículo para atender circunstância momentânea do trânsito é a",["interrupção de marcha.","parada.","estacionamento.","conversão.","retenção."],"Anexo I.")
q(1,"O movimento em ângulo, à esquerda ou à direita, de mudança da direção original do veículo, é a",["conversão.","ultrapassagem.","transposição.","passagem.","parada."],"Anexo I.")
q(1,"Noite, para o CTB, é o período compreendido entre o",["pôr do sol e o nascer do sol.","meio-dia e a meia-noite.","18h e as 6h.","22h e as 6h.","anoitecer e a meia-noite."],"Anexo I.")
q(1,"Trânsito é a movimentação e a imobilização de veículos, pessoas e",["animais nas vias terrestres.","cargas no mar.","aeronaves.","trens nos trilhos.","embarcações."],"Anexo I.")
q(1,"Automóvel é o veículo automotor de passageiros com capacidade para até",["oito pessoas, exclusive o condutor.","cinco pessoas, incluído o condutor.","dez pessoas.","doze pessoas.","vinte pessoas."],"Anexo I.")
q(1,"A motocicleta é dirigida por condutor em posição",["montada.","sentada.","em pé.","deitada.","ajoelhada."],"Anexo I.")
q(1,"A motoneta é dirigida por condutor em posição",["sentada.","montada.","em pé.","deitada.","lateral."],"Anexo I.")
q(1,"A bicicleta é veículo de propulsão",["humana.","elétrica.","a combustão.","animal.","híbrida."],"Anexo I.")
q(1,"A caminhonete é veículo destinado ao transporte de",["carga, com peso bruto total de até 3.500 kg.","passageiros, até oito pessoas.","passageiros e carga no mesmo compartimento.","pessoas com deficiência.","animais."],"Anexo I.")
q(1,"A parte da via, sinalizada e protegida, destinada ao uso de pedestres durante a travessia, é o",["refúgio.","acostamento.","canteiro.","lote lindeiro.","bordo."],"Anexo I.")
q(1,"A inobservância a qualquer preceito da legislação de trânsito denomina-se",["infração.","sinistro.","crime.","fiscalização.","operação."],"Anexo I.")
q(1,"No texto da van de entregas, a via descrita, com semáforos e ligando regiões da cidade, é",["arterial.","local.","coletora.","de trânsito rápido.","rural."],"Anexo I.","ctb12a")
q(1,"No texto da motoneta e a ciclofaixa, a faixa pintada na pista para ciclistas é a",["ciclofaixa.","ciclovia.","calçada.","faixa de pedestres.","acostamento."],"Anexo I.","ctb12b")
q(1,"No texto do sinistro na rodovia, a via rural pavimentada é uma",["rodovia.","estrada.","via local.","via arterial.","ciclovia."],"Anexo I.","ctb12c")
# n=2
q(2,"A via destinada a coletar e distribuir o trânsito que entra ou sai das vias de trânsito rápido ou arteriais, possibilitando o trânsito dentro das regiões da cidade, é a via",["coletora.","arterial.","local.","rural.","de trânsito rápido."],"Anexo I.")
q(2,"Via urbana compreende ruas, avenidas, vielas ou caminhos abertos à circulação pública, situados na área urbana, caracterizados principalmente por possuírem",["imóveis edificados ao longo de sua extensão.","pavimentação asfáltica.","semáforos.","ciclovias.","canteiros centrais."],"Anexo I.")
q(2,"O acostamento destina-se à parada ou estacionamento em emergência e à circulação de pedestres e bicicletas",["quando não houver local apropriado para esse fim.","sempre.","apenas à noite.","apenas aos domingos.","apenas em rodovias federais."],"Anexo I.")
q(2,"A ultrapassagem é o movimento de passar à frente de veículo que se desloca no mesmo sentido, em menor velocidade, na mesma faixa,",["necessitando sair e retornar à faixa de origem.","sem sair da faixa.","em faixas distintas.","pela contramão obrigatoriamente.","pelo acostamento."],"Anexo I.")
q(2,"A passagem por outro veículo ocorre quando o veículo passa à frente de outro que se desloca no mesmo sentido, em menor velocidade, mas em",["faixas distintas da via.","mesma faixa.","sentido oposto.","acostamento.","contramão."],"Anexo I.")
q(2,"A passagem de um veículo de uma faixa demarcada para outra denomina-se",["transposição de faixas.","conversão.","ultrapassagem.","retorno.","interseção."],"Anexo I.")
q(2,"Interseção é todo cruzamento em nível, entroncamento ou",["bifurcação.","viaduto.","túnel.","ponte.","passarela."],"Anexo I.")
q(2,"Cruzamento é a interseção de duas vias",["em nível.","em desnível.","rurais.","de trânsito rápido.","paralelas."],"Anexo I.")
q(2,"A ilha é obstáculo físico, colocado na pista de rolamento, destinado à",["ordenação dos fluxos de trânsito em uma interseção.","travessia de pedestres.","parada de ônibus.","circulação de bicicletas.","estacionamento."],"Anexo I.")
q(2,"A calçada é parte da via, normalmente segregada e em nível diferente,",["não destinada à circulação de veículos, reservada ao trânsito de pedestres.","destinada à circulação de motos.","destinada ao estacionamento.","destinada a ciclistas exclusivamente.","destinada a carga e descarga."],"Anexo I.")
q(2,"Camioneta é o veículo",["misto destinado ao transporte de passageiros e carga no mesmo compartimento.","de carga até 3.500 kg.","de passageiros até oito pessoas.","de duas rodas.","de tração animal."],"Anexo I.")
q(2,"O ciclomotor com motor de combustão tem cilindrada que não exceda a",["50 cm³.","125 cm³.","250 cm³.","100 cm³.","30 cm³."],"Anexo I.")
q(2,"A velocidade máxima de fabricação do ciclomotor não pode exceder",["50 km/h.","80 km/h.","30 km/h.","60 km/h.","100 km/h."],"Anexo I.")
q(2,"Autoridade de trânsito é o dirigente máximo de órgão ou entidade executivo integrante do SNT ou",["pessoa por ele expressamente credenciada.","qualquer servidor público.","qualquer policial.","qualquer guarda municipal.","o prefeito necessariamente."],"Anexo I.")
q(2,"O etilômetro é o aparelho destinado à medição do teor alcoólico no",["ar alveolar.","sangue.","suor.","urina.","cabelo."],"Anexo I.")
q(2,"O perímetro urbano é o limite entre",["área urbana e área rural.","dois Municípios.","dois Estados.","duas vias.","calçada e pista."],"Anexo I.")
q(2,"Lote lindeiro é aquele situado ao longo das vias urbanas ou rurais e que com elas",["se limita.","se cruza.","se sobrepõe.","se separa por rio.","não tem contato."],"Anexo I.")
q(2,"No texto da van de entregas, os vinte minutos descarregando caixas configuram",["estacionamento.","parada.","interrupção de marcha.","conversão.","transposição de faixas."],"Anexo I.","ctb12a")
q(2,"No texto da motoneta e a ciclofaixa, o condutor está em posição",["sentada, pois se trata de motoneta.","montada, pois se trata de motoneta.","em pé.","deitada.","de bicicleta."],"Anexo I.","ctb12b")
q(2,"No texto do sinistro na rodovia, o CTB chama o evento de",["sinistro de trânsito.","acidente aéreo.","infração.","crime ambiental.","interrupção de marcha."],"Anexo I.","ctb12c")
# n=3
q(3,"Assinale a alternativa correta.",["Ciclovia é separada fisicamente do tráfego comum; ciclofaixa é parte da pista delimitada por sinalização.","Ciclofaixa é separada fisicamente; ciclovia é só sinalizada.","Ciclovia e ciclofaixa são sinônimos no CTB.","Ciclofaixa é parte da calçada.","Ciclovia é parte do acostamento."],"Anexo I.")
q(3,"Considere. I. Estrada é via rural pavimentada. II. Rodovia é via rural pavimentada. III. Via rural compreende estradas e rodovias. Está correto o que se afirma em",["II e III, apenas.","I, apenas.","I e II, apenas.","III, apenas.","I, II e III."],"Anexo I.")
q(3,"Assinale a INCORRETA.",["Passagem por outro veículo exige sair e retornar à faixa de origem.","Ultrapassagem ocorre na mesma faixa de tráfego.","Transposição de faixas é a passagem de uma faixa demarcada para outra.","Conversão é movimento em ângulo de mudança de direção.","Parada é para embarque ou desembarque de passageiros."],"Passagem ocorre em faixas distintas.")
q(3,"O passeio é parte da calçada ou da pista, separada por pintura ou elemento físico, destinada à circulação exclusiva de pedestres e, excepcionalmente, de",["ciclistas.","motociclistas.","carros de mão.","veículos de emergência.","animais."],"Anexo I.")
q(3,"Logradouro público é o espaço livre destinado pela municipalidade à circulação, parada ou estacionamento de veículos, ou à circulação de pedestres, tais como",["calçada, parques, áreas de lazer e calçadões.","lotes particulares.","garagens privadas.","pátios de empresas.","condomínios fechados."],"Anexo I.")
q(3,"Agente da autoridade de trânsito inclui o agente de trânsito e o policial rodoviário federal e, quando designados mediante convênio, também o",["policial militar ou os agentes do art. 25-A.","vigilante privado.","fiscal sanitário.","oficial de justiça.","bombeiro civil."],"Anexo I.")
q(3,"O policiamento ostensivo de trânsito, segundo o Anexo I, é função exercida pelas",["Polícias Militares.","Guardas Municipais.","Polícias Civis.","Forças Armadas.","empresas de engenharia de tráfego."],"Anexo I.")
q(3,"A fiscalização de trânsito é o ato de controlar o cumprimento das normas por meio do poder de polícia",["administrativa de trânsito.","judiciária.","militar.","fiscal tributária.","sanitária."],"Anexo I.")
q(3,"No sinistro de trânsito, conforme o Anexo I, ao menos uma das partes está",["em movimento nas vias terrestres ou em áreas abertas ao público.","parada em garagem particular.","em via aérea.","em embarcação.","sem condutor habilitado."],"Anexo I.")
q(3,"O veículo em estado de abandono é o estacionado na via, sem capacidade de locomoção por meios próprios, que ofereça risco à saúde, à segurança ou ao meio ambiente,",["independentemente de encontrar-se em local permitido.","apenas se em local proibido.","apenas se sem placa.","apenas se há mais de um ano.","apenas se incendiado."],"Anexo I.")
q(3,"O veículo automotor inclui, por expressa previsão, os veículos conectados a uma linha elétrica que não circulam sobre trilhos, como o",["ônibus elétrico.","bonde.","trem.","metrô.","teleférico."],"Anexo I.")
q(3,"A bicicleta, para efeito do CTB,",["não é similar à motocicleta, motoneta e ciclomotor.","é similar ao ciclomotor.","é veículo automotor.","é equiparada à motocicleta.","não é veículo."],"Anexo I.")
q(3,"O ciclomotor elétrico tem potência máxima de",["4 kW.","10 kW.","1 kW.","50 kW.","20 kW."],"Anexo I.")
q(3,"A operação de trânsito é o monitoramento técnico, baseado em engenharia de tráfego, das condições de fluidez, de estacionamento e de",["parada na via.","arrecadação.","licenciamento.","habilitação.","pesagem de carga."],"Anexo I.")
q(3,"Utilitário é o veículo",["misto caracterizado pela versatilidade do seu uso, inclusive fora de estrada.","de carga com mais de 3.500 kg.","de duas rodas.","de propulsão humana.","de tração animal."],"Anexo I.")
q(3,"No texto da van de entregas, a velocidade máxima, onde não houver sinalização, nessa via é de",["60 km/h.","80 km/h.","40 km/h.","30 km/h.","110 km/h."],"Art. 61, § 1º, I, b.","ctb12a")
q(3,"No texto da van de entregas, se a van ficasse apenas o tempo para um passageiro descer, haveria",["parada.","estacionamento.","interrupção de marcha.","abandono.","bloqueio."],"Anexo I.","ctb12a")
q(3,"No texto da motoneta e a ciclofaixa, se a faixa fosse separada fisicamente da pista, seria uma",["ciclovia.","ciclofaixa.","calçada.","ilha.","faixa de rolamento."],"Anexo I.","ctb12b")
q(3,"No texto do sinistro na rodovia, se a via rural não fosse pavimentada, seria uma",["estrada.","rodovia.","via arterial.","via coletora.","via local."],"Anexo I.","ctb12c")
q(3,"No texto do sinistro na rodovia, o termo usado pelo CTB, após a Lei 14.599/2023, é sinistro de trânsito, que abrange dano ao veículo ou à carga e lesões a",["pessoas ou animais.","apenas pessoas.","apenas veículos.","apenas animais.","apenas o patrimônio público."],"Anexo I.","ctb12c")
from collections import Counter; c=Counter(x[0] for x in Q); print(c); assert c=={1:20,2:20,3:20}
code,svg=mapa("CTB, Anexo I: conceitos e definições",[
 ("via","Vias urbanas",["trânsito rápido: sem interseção","arterial: semáforo, entre regiões","coletora e local"],"seção 1"),
 ("rur","Vias rurais",["estrada: não pavimentada","rodovia: pavimentada"],"seção 1"),
 ("cic","Ciclos e pedestres",["ciclovia: separada","ciclofaixa: sinalizada","refúgio, passeio, calçada"],"seção 1"),
 ("man","Manobras",["ultrapassagem: mesma faixa","passagem: faixas distintas","conversão e transposição"],"seção 2"),
 ("imo","Imobilizações",["interrupção de marcha","parada: embarque","estacionamento: mais que isso"],"seção 2"),
 ("vei","Veículos e agentes",["automóvel: até 8 + condutor","moto montada x motoneta sentada","autoridade x agente"],"seção 3")],
 "Na prova: as definições são cobradas ao pé da letra")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"Os blocos seguem as três seções: vias, manobras e imobilizações, veículos e agentes.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (CTB), Anexo I, consolidação da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-12","CTB: conceitos e definições (Anexo I)",Q,list(tx),
 cobertura=["Anexo I do CTB: cerca de 50 conceitos selecionados (vias, partes da via, manobras, imobilizações, veículos, agentes). Não incluídos: conceitos técnicos de freios, luzes, pesos e reboques."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin); reconferir no Planalto.","Velocidades por tipo de via conferidas com o art. 61 (ctb-2).","Casos ctb12a, ctb12b e ctb12c fictícios."],
 fontes_conferidas=["CTB, Anexo I: texto da Câmara, copiado por programa."])
gravar("ctb-12",aula_html,banco("ctb-12",Q),tx)
