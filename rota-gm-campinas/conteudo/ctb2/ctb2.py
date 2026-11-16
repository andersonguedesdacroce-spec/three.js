import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="As normas gerais de circulação e conduta são o coração do Código de Trânsito: quem tem a preferência, como se ultrapassa, como se converte, quando se usam luzes e buzina, quais são os limites de velocidade e como se para e se estaciona. A Vunesp cobra os arts. 26 a 65 pela letra da lei, e as perguntas giram em torno de números (velocidades, idades, distâncias) e de proibições (onde não se pode ultrapassar). Para o guarda, são as regras que ele fiscaliza todos os dias. A aula segue o texto consolidado, com a lei citada e a explicação logo abaixo."
S={}
S[1]="## 1. Dever geral, preferência e veículos de emergência\n\n"+L("art. 26","Art. 26. Os usuários das vias terrestres devem:","Art. 27.")+"\n\n"+L("art. 28","Art. 28. O condutor deverá, a todo momento","Art. 29.")+"\n\n"+L("art. 29, caput e I a III","Art. 29. O trânsito de veículos nas vias terrestres","IV - quando uma pista")+"""

Todo usuário da via deve abster-se de atos que possam constituir perigo ou obstáculo, e todo condutor deve ter, a todo momento, domínio do veículo e dirigir com atenção e cuidados indispensáveis à segurança. A circulação se faz pelo lado direito da via. A preferência em cruzamento não sinalizado segue uma escada: quem circula em rodovia, quando só um dos fluxos vem de rodovia; quem circula na rotatória; e, nos demais casos, quem vier pela direita do condutor. É regra que cai todo ano.

"""+L("art. 29, VII","VII - os veículos destinados a socorro de incêndio","a) quando os dispositivos regulamentares")+"\n\n"+L("art. 29, VII, a","a) quando os dispositivos regulamentares de alarme","b) os pedestres, ao ouvirem")+"""

Os veículos de socorro de incêndio e salvamento, os de polícia, os de fiscalização e operação de trânsito e as ambulâncias têm prioridade no trânsito e livre circulação, estacionamento e parada, quando em serviço de urgência, de policiamento ostensivo ou de preservação da ordem pública, e só se estiverem com alarme sonoro e luz intermitente acionados. Os demais condutores devem deixar livre a passagem pela faixa da esquerda, indo para a direita e parando, se necessário. O uso do alarme e da luz somente pode ocorrer na efetiva prestação de serviço de urgência.

"""+L("art. 29, § 2º","§ 2º Respeitadas as normas de circulação e conduta","§ 3º Compete ao Contran regulamentar")+"""

A regra do § 2º, de responsabilidade em ordem decrescente, é uma síntese: os veículos de maior porte são responsáveis pela segurança dos menores, os motorizados pelos não motorizados e, juntos, pela incolumidade dos pedestres.
"""
S[2]="## 2. Ultrapassagem e manobras\n\n"+L("art. 29, IX","IX - a ultrapassagem de outro veículo em movimento","X - todo condutor deverá, antes")+"\n\n"+L("art. 32","Art. 32. O condutor não poderá ultrapassar","Art. 34.")+"\n\n"+L("art. 35, caput","Art. 35. Antes de iniciar qualquer manobra","Parágrafo único. Entende-se por deslocamento lateral")+"\n\n"+L("art. 39","Art. 39. Nas vias urbanas, a operação de retorno","Art. 40.")+"""

A ultrapassagem é pela esquerda, obedecida a sinalização, exceto quando o veículo a ser ultrapassado estiver sinalizando que vai entrar à esquerda. Não se pode ultrapassar, nas vias de duplo sentido e pista única, nos trechos em curvas e em aclives sem visibilidade suficiente, nas passagens de nível, nas pontes e viadutos e nas travessias de pedestres, salvo sinalização permitindo; e, nas interseções e suas proximidades, a ultrapassagem é proibida (art. 33). Antes de qualquer manobra com deslocamento lateral, o condutor indica o propósito com a luz de direção ou gesto, com antecedência. Deslocamento lateral é a transposição de faixas, a conversão à direita ou à esquerda e os retornos. E nas vias urbanas o retorno só pode ser feito nos locais determinados por sinalização ou nos que ofereçam condições de segurança.
"""
S[3]="## 3. Luzes, buzina, velocidade e cruzamentos\n\n"+L("art. 40, I","Art. 40. O uso de luzes em veículo","II - nas vias não iluminadas")+"\n\n"+L("art. 40, V","V - O condutor utilizará o pisca-alerta","VI - durante a noite")+"\n\n"+L("art. 41","Art. 41. O condutor de veículo só poderá fazer uso de buzina","Art. 42.")+"\n\n"+L("art. 44-A","Art. 44-A. É livre o movimento de conversão à direita","Art. 45.")+"\n\n"+L("art. 45","Art. 45. Mesmo que a indicação luminosa","Art. 46.")+"""

O condutor mantém acesos os faróis, na luz baixa, à noite e, mesmo de dia, em túneis e sob chuva, neblina ou cerração. O pisca-alerta é usado em imobilizações ou situações de emergência, ou quando a regulamentação da via assim determinar. A buzina só pode ser usada em toque breve, para advertências necessárias a evitar sinistros ou, fora das áreas urbanas, para advertir que se vai ultrapassar. É livre a conversão à direita diante de sinal vermelho onde houver sinalização que permita, observados os arts. 44, 45 e 70. E, mesmo com sinal verde, não se pode entrar em interseção se há possibilidade de ficar parado na área do cruzamento, obstruindo a passagem do trânsito transversal.

"""+L("art. 60","Art. 60. As vias abertas à circulação","Art. 61.")+"\n\n"+L("art. 61, caput e § 1º, I","Art. 61. A velocidade máxima permitida","II - nas vias rurais:")+"\n\n"+L("art. 61, § 1º, II","II - nas vias rurais:","§ 2º O órgão ou entidade")+"\n\n"+L("art. 62","Art. 62. A velocidade mínima","Art. 63.")+"""

As vias urbanas se classificam em via de trânsito rápido, arterial, coletora e local; as rurais, em rodovias e estradas. Onde não existir sinalização regulamentadora, a velocidade máxima nas vias urbanas é de 80 km/h na de trânsito rápido, 60 km/h na arterial, 40 km/h na coletora e 30 km/h na local. Nas rurais, é de 110 km/h para automóveis, camionetas, caminhonetes e motocicletas e 90 km/h para os demais veículos nas rodovias de pista dupla; 100 km/h e 90 km/h, respectivamente, nas de pista simples; e 60 km/h nas estradas. A velocidade mínima não pode ser inferior à metade da máxima.
"""
S[4]="## 4. Parada, estacionamento, motos, bicicletas, crianças e cinto\n\n"+L("art. 47","Art. 47. Quando proibido o estacionamento","Art. 48.")+"\n\n"+L("art. 48, caput e § 2º","Art. 48. Nas paradas, operações de carga","§ 1º Nas vias providas de acostamento")+" "+L("art. 48, § 2º","§ 2º O estacionamento dos veículos motorizados de duas rodas","§ 3º O estacionamento dos veículos sem abandono")+"\n\n"+L("art. 54","Art. 54. Os condutores de motocicletas","Art. 55.")+"\n\n"+L("art. 58","Art. 58. Nas vias urbanas e nas rurais","Parágrafo único. A autoridade de trânsito")+"\n\n"+L("art. 64","Art. 64. As crianças com idade inferior","Parágrafo único. O Contran disciplinará")+"\n\n"+L("art. 65","Art. 65. É obrigatório o uso do cinto","Art. 66.")+"""

Quando é proibido estacionar, a parada se restringe ao tempo indispensável para embarque ou desembarque de passageiros, sem perturbar o fluxo. A carga e a descarga são regulamentadas pelo órgão com circunscrição sobre a via e são consideradas estacionamento. O veículo deve ser posicionado no sentido do fluxo, paralelo ao bordo da pista e junto ao meio-fio, e o das motos de duas rodas é estacionado em posição perpendicular à guia e junto a ela, salvo sinalização diversa.

O condutor de moto, motoneta ou ciclomotor só circula com capacete de segurança, com viseira ou óculos protetores, segurando o guidom com as duas mãos e usando vestuário de proteção. As bicicletas circulam, quando não há ciclovia, ciclofaixa ou acostamento, nos bordos da pista, no mesmo sentido do fluxo, com preferência sobre os veículos automotores. As crianças com menos de 10 anos que não tenham atingido 1,45 m de altura são transportadas nos bancos traseiros, em dispositivo de retenção adequado. E o cinto de segurança é obrigatório para condutor e passageiros em todas as vias do território nacional, salvo situações regulamentadas pelo Contran.
"""
S[6]="""## 6. Na rotina do guarda

- **Veículos de emergência:** o guarda, ao usar viatura com alarme e luz acionados em serviço de urgência, tem prioridade e livre circulação, mas só quando em serviço de urgência, de policiamento ostensivo ou de preservação da ordem pública.
- **Preferência no cruzamento:** em cruzamento não sinalizado, a regra da preferência (rodovia, rotatória, direita) orienta o agente que lida com sinistros.
- **Velocidades:** a velocidade máxima, sem sinalização, depende do tipo de via: 30, 40, 60 ou 80 km/h nas urbanas.
- **Crianças e cinto:** o agente verifica o uso de cinto e a retenção das crianças com menos de 10 anos e menos de 1,45 m.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Preferência em cruzamento sem sinal | Rodovia, depois rotatória, depois quem vem pela direita |
| Ultrapassagem pela direita | A regra é pela esquerda, salvo quem sinaliza entrada à esquerda |
| Ultrapassar em interseção | É proibido nas interseções e proximidades |
| Velocidade em via local | 30 km/h sem sinalização; coletora 40; arterial 60; trânsito rápido 80 |
| Velocidade em rodovia de pista dupla | 110 km/h para automóveis e motos; 90 km/h para os demais |
| Velocidade mínima | Metade da máxima |
| Crianças no banco | Menores de 10 anos com menos de 1,45 m: banco traseiro, com retenção |
| Estacionamento de motos | Perpendicular à guia, salvo sinalização diferente |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Circulação | Pela direita |
| Preferência sem sinal | Rodovia; rotatória; quem vem pela direita |
| Emergência | Prioridade e livre circulação, com alarme e luz, em serviço de urgência |
| Ultrapassagem | Pela esquerda; proibida em curvas, pontes, interseções |
| Luz baixa | À noite e, de dia, em túneis e sob chuva |
| Buzina | Toque breve, só para evitar sinistro ou advertir ultrapassagem fora da cidade |
| Velocidade urbana | 80, 60, 40 e 30 km/h |
| Velocidade rural | Pista dupla: 110 e 90; simples: 100 e 90; estradas: 60 |
| Mínima | Metade da máxima |
| Cinto | Obrigatório para todos |
"""
QR=[("Questão 1","Em um cruzamento não sinalizado, quando apenas um dos fluxos é proveniente de rodovia, a preferência é de quem",["estiver circulando pela rodovia.","vier pela esquerda.","estiver na via menor.","vier pela direita.","estiver na rotatória."],0,"Art. 29, III, a."),
("Questão 2","Onde não existir sinalização regulamentadora, a velocidade máxima nas vias urbanas locais é de",["30 km/h.","40 km/h.","60 km/h.","80 km/h.","50 km/h."],2,"Art. 61, § 1º, I, d."),
("Questão 3","As crianças com idade inferior a 10 anos que não tenham atingido 1,45 m de altura devem ser transportadas",["nos bancos traseiros, em dispositivo de retenção adequado.","no banco dianteiro, com cinto.","no colo do passageiro.","em qualquer banco.","apenas em carro lateral."],1,"Art. 64."),
("Questão 4","A ultrapassagem de outro veículo em movimento deverá ser feita",["pela esquerda, obedecida a sinalização regulamentar.","pela direita, sempre.","por qualquer lado.","pelo acostamento.","pelo meio-fio."],4,"Art. 29, IX.")]
t1="<strong>Viatura em atendimento</strong><br><br>Uma viatura da Guarda Municipal de Vila Nova, cidade fictícia, seguia com sirene e luz intermitente acionadas, para atender a uma ocorrência de ameaça em andamento. Em um cruzamento, os demais condutores se detiveram."
t2="<strong>Via de rodagem</strong><br><br>Em uma via arterial de Vila Nova, sem placa de velocidade, um motorista dirigia a 70 km/h. Em uma estrada rural próxima, outro condutor, de automóvel, dirigia a 70 km/h, também sem sinalização."
tx={"ctb2a":t1,"ctb2b":t2}
# n=1
q(1,"Segundo o art. 29, I, a circulação far-se-á pelo lado",["direito da via, admitindo-se as exceções devidamente sinalizadas.","esquerdo da via.","do meio da via.","do acostamento.","que o condutor preferir."],"Art. 29, I.")
q(1,"Em cruzamento não sinalizado, no caso de rotatória, a preferência é de quem",["estiver circulando por ela.","vier pela direita.","vier pela esquerda.","for de transporte coletivo.","for mais veloz."],"Art. 29, III, b.")
q(1,"Em cruzamento não sinalizado, nos demais casos, a preferência é do condutor que vier",["pela direita do outro condutor.","pela esquerda do outro.","em maior velocidade.","em veículo maior.","em veículo menor."],"Art. 29, III, c.")
q(1,"Os veículos de polícia, quando em serviço de urgência, gozam de prioridade no trânsito e de livre circulação, estacionamento e parada, desde que",["estejam com alarme sonoro e iluminação intermitente acionados.","tenham pressa.","estejam sem luz.","estejam sem sirene.","estejam com a sirene desligada."],"Art. 29, VII, a, e e f.")
q(1,"O uso de dispositivos de alarme sonoro e de iluminação intermitente somente poderá ocorrer por ocasião da efetiva",["prestação de serviço de urgência.","patrulha de rotina.","saída do quartel.","mudança de turno.","manobra."],"Art. 29, VII, c.")
q(1,"A ultrapassagem de outro veículo em movimento deverá ser feita pela",["esquerda.","direita.","calçada.","qualquer lado.","faixa de pedestres."],"Art. 29, IX.")
q(1,"O condutor não poderá ultrapassar veículos em vias com duplo sentido de direção e pista única, entre outros trechos,",["em curvas e em aclives sem visibilidade suficiente.","em retas.","em declives.","em vias largas.","em pistas duplas."],"Art. 32.")
q(1,"Nas interseções e suas proximidades, o condutor",["não poderá efetuar ultrapassagem.","poderá ultrapassar.","poderá ultrapassar pela direita.","poderá ultrapassar com buzina.","poderá ultrapassar com pisca."],"Art. 33.")
q(1,"Antes de iniciar qualquer manobra que implique deslocamento lateral, o condutor deverá indicar seu propósito por meio da",["luz indicadora de direção ou de gesto convencional de braço.","buzina.","luz alta.","luz de freio.","sirene."],"Art. 35, caput.")
q(1,"Nas vias urbanas, a operação de retorno deverá ser feita",["nos locais determinados por sinalização ou em outros locais que ofereçam condições de segurança e fluidez.","em qualquer lugar.","apenas em cruzamentos.","apenas em rotatórias.","apenas em pontes."],"Art. 39.")
q(1,"O condutor manterá acesos os faróis do veículo, na luz baixa, à noite e, mesmo durante o dia,",["em túneis e sob chuva, neblina ou cerração.","em rodovias.","em ruas estreitas.","em ruas com tráfego intenso.","em qualquer via."],"Art. 40, I.")
q(1,"O condutor utilizará o pisca-alerta em imobilizações ou situações de emergência, ou quando a regulamentação da via",["assim o determinar.","for rural.","for urbana.","for estreita.","for larga."],"Art. 40, V.")
q(1,"O condutor só poderá fazer uso de buzina, em toque breve, para fazer as advertências necessárias a fim de evitar sinistros ou, fora das áreas urbanas, para",["advertir a um condutor que se tem o propósito de ultrapassá-lo.","chamar passageiros.","cumprimentar conhecidos.","pedir passagem na cidade.","avisar que vai estacionar."],"Art. 41.")
q(1,"É livre o movimento de conversão à direita diante de sinal vermelho do semáforo onde houver",["sinalização indicativa que permita essa conversão.","tráfego livre.","guarda de trânsito.","passagem de pedestres.","buzina."],"Art. 44-A.")
q(1,"Mesmo que o semáforo lhe seja favorável, nenhum condutor pode entrar em uma interseção se houver possibilidade de ser obrigado a",["imobilizar o veículo na área do cruzamento, obstruindo a passagem do trânsito transversal.","acelerar.","frear.","buzinar.","acender o farol."],"Art. 45.")
q(1,"Quando proibido o estacionamento, a parada deverá restringir-se ao tempo indispensável para",["embarque ou desembarque de passageiros.","carga de mercadorias, sem limite.","descanso.","refeição.","compras."],"Art. 47.")
q(1,"Os condutores de motocicletas só poderão circular nas vias utilizando capacete de segurança, com viseira ou óculos protetores, segurando o guidom com as duas mãos e",["usando vestuário de proteção, de acordo com as especificações do Contran.","com um passageiro, sempre.","sem retrovisor.","sem luz.","em velocidade máxima."],"Art. 54.")
q(1,"A velocidade máxima, sem sinalização, em via urbana de trânsito rápido, é de",["80 km/h.","60 km/h.","40 km/h.","30 km/h.","100 km/h."],"Art. 61, § 1º, I, a.")
q(1,"No texto da viatura em atendimento, os demais condutores devem, ao perceber a sirene e a luz, deixar livre a passagem pela faixa da",["esquerda, indo para a direita da via e parando, se necessário.","direita, indo para a esquerda.","esquerda, sem parar.","direita, sem parar.","esquerda, acelerando."],"Art. 29, VII, a.","ctb2a")
q(1,"No texto da via de rodagem, em via arterial sem sinalização, a velocidade máxima é de",["60 km/h.","80 km/h.","40 km/h.","30 km/h.","50 km/h."],"Art. 61, § 1º, I, b.","ctb2b")
# n=2
q(2,"O condutor deve guardar distância de segurança lateral e frontal entre o seu e os demais veículos, considerando, no momento, a velocidade e",["as condições do local, da circulação, do veículo e as condições climáticas.","apenas o horário.","apenas o tipo de via.","apenas o modelo do veículo.","apenas o cansaço."],"Art. 29, II.")
q(2,"Quando uma pista comportar várias faixas no mesmo sentido, as da direita são destinadas ao deslocamento dos veículos",["mais lentos e de maior porte, quando não houver faixa especial.","mais velozes.","apenas de passeio.","apenas de motocicletas.","apenas de ambulâncias."],"Art. 29, IV.")
q(2,"O trânsito de veículos sobre passeios, calçadas e acostamentos só poderá ocorrer para",["que se adentre ou se saia dos imóveis ou áreas especiais de estacionamento.","qualquer fim.","descanso.","ultrapassagem.","retorno."],"Art. 29, V.")
q(2,"Os veículos que se deslocam sobre trilhos têm",["preferência de passagem sobre os demais, respeitadas as normas de circulação.","preferência nula.","preferência apenas em rodovias.","preferência apenas à noite.","preferência apenas em cruzamentos."],"Art. 29, XII.")
q(2,"Quanto ao dever do maior porte, os veículos de maior porte são responsáveis pela segurança dos menores, os motorizados pelos não motorizados e, juntos, pela incolumidade dos",["pedestres.","passageiros.","animais.","ciclistas apenas.","motociclistas apenas."],"Art. 29, § 2º.")
q(2,"O condutor que tenha o propósito de ultrapassar um veículo de transporte coletivo que esteja parado, efetuando embarque ou desembarque, deverá",["reduzir a velocidade, dirigindo com atenção redobrada, ou parar o veículo, com vistas à segurança dos pedestres.","acelerar.","buzinar.","ultrapassar pela direita.","manter velocidade."],"Art. 31.")
q(2,"Todo condutor, ao perceber que outro que o segue tem o propósito de ultrapassá-lo, estando na faixa da esquerda, deverá",["deslocar-se para a faixa da direita, sem acelerar a marcha.","acelerar.","frear.","manter-se.","buzinar."],"Art. 30, I.")
q(2,"Entende-se por deslocamento lateral a transposição de faixas, movimentos de conversão à direita, à esquerda e",["retornos.","partidas.","freadas.","buzinadas.","paradas."],"Art. 35, parágrafo único.")
q(2,"O condutor que for ingressar numa via, procedente de lote lindeiro, deverá dar preferência aos",["veículos e pedestres que por ela estejam transitando.","veículos parados.","pedestres apenas.","ciclistas apenas.","veículos oficiais apenas."],"Art. 36.")
q(2,"Nenhum condutor deverá frear bruscamente seu veículo, salvo por razões de",["segurança.","pressa.","economia.","conforto.","hábito."],"Art. 42.")
q(2,"Ao aproximar-se de qualquer tipo de cruzamento, o condutor deve demonstrar",["prudência especial, transitando em velocidade moderada, de forma que possa deter o veículo com segurança.","pressa.","impaciência.","indiferença.","velocidade máxima."],"Art. 44.")
q(2,"No transporte de crianças, o limite que combina idade e altura, para uso dos bancos traseiros em dispositivo de retenção, é menos de 10 anos e menos de",["1,45 m.","1,30 m.","1,50 m.","1,60 m.","1,20 m."],"Art. 64.")
q(2,"É obrigatório o uso do cinto de segurança para condutor e passageiros em",["todas as vias do território nacional, salvo situações regulamentadas pelo Contran.","apenas rodovias.","apenas vias urbanas.","apenas à noite.","apenas em viagens longas."],"Art. 65.")
q(2,"As vias urbanas classificam-se em via de trânsito rápido, arterial, coletora e",["local.","rural.","estrada.","rodovia.","particular."],"Art. 60, I.")
q(2,"As vias rurais classificam-se em rodovias e",["estradas.","ruas.","avenidas.","vias locais.","vias arteriais."],"Art. 60, II.")
q(2,"A velocidade mínima não poderá ser inferior à",["metade da velocidade máxima estabelecida.","terça parte da máxima.","quarta parte da máxima.","máxima menos 10 km/h.","máxima menos 20 km/h."],"Art. 62.")
q(2,"No texto da viatura em atendimento, o uso de sirene e luz intermitente só se justifica por ser",["serviço de urgência, em efetiva prestação.","trânsito intenso.","rotina de patrulha.","saída do quartel.","entrega de documento."],"Art. 29, VII, c.","ctb2a")
q(2,"No texto da via de rodagem, a velocidade de 70 km/h na via arterial, sem sinalização,",["excede a velocidade máxima de 60 km/h.","está dentro do limite.","é a velocidade mínima.","é permitida em qualquer caso.","é exigida pelo Código."],"Art. 61, § 1º, I, b.","ctb2b")
q(2,"No texto da via de rodagem, na estrada rural, sem sinalização, a velocidade máxima é de",["60 km/h.","80 km/h.","90 km/h.","100 km/h.","110 km/h."],"Art. 61, § 1º, II, c.","ctb2b")
q(2,"O condutor e os passageiros não deverão abrir a porta do veículo, deixá-la aberta ou descer sem antes se certificarem de que isso não constitui perigo para eles e para outros usuários da via. O embarque e o desembarque devem ocorrer sempre do lado da calçada, exceto para",["o condutor.","o passageiro.","a criança.","o idoso.","a pessoa com deficiência."],"Art. 49, caput e parágrafo único.")
# n=3
q(3,"Assinale a alternativa que traz apenas velocidades máximas corretas para vias urbanas sem sinalização.",["Trânsito rápido, 80 km/h; arterial, 60 km/h; coletora, 40 km/h; local, 30 km/h.","Trânsito rápido, 100 km/h; arterial, 80 km/h; coletora, 60 km/h; local, 40 km/h.","Trânsito rápido, 80 km/h; arterial, 70 km/h; coletora, 50 km/h; local, 30 km/h.","Trânsito rápido, 60 km/h; arterial, 40 km/h; coletora, 30 km/h; local, 20 km/h.","Trânsito rápido, 90 km/h; arterial, 60 km/h; coletora, 40 km/h; local, 30 km/h."],"Art. 61, § 1º, I.")
q(3,"Assinale a alternativa que traz apenas velocidades máximas corretas para vias rurais sem sinalização.",["Rodovias de pista dupla, 110 km/h (automóveis e motos) e 90 km/h (demais); pista simples, 100 e 90 km/h; estradas, 60 km/h.","Rodovias de pista dupla, 120 e 100; pista simples, 110 e 90; estradas, 80.","Rodovias de pista dupla, 110 e 90; pista simples, 90 e 80; estradas, 60.","Rodovias de pista dupla, 100 e 80; pista simples, 90 e 70; estradas, 50.","Rodovias de pista dupla, 120 e 90; pista simples, 100 e 80; estradas, 60."],"Art. 61, § 1º, II.")
q(3,"Considere as afirmações. I. A ultrapassagem é pela esquerda. II. A ultrapassagem é permitida em interseções. III. A ultrapassagem é proibida nas pontes e viadutos, salvo sinalização que a permita. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II e III, apenas.","I e II, apenas.","I, II e III."],"Art. 33 proíbe a ultrapassagem nas interseções.")
q(3,"Assinale a INCORRETA sobre o art. 29, VII.",["Os veículos de emergência têm prioridade mesmo sem alarme e iluminação acionados.","A prioridade se aplica em serviço de urgência, policiamento ostensivo ou preservação da ordem pública.","O uso do alarme só pode ocorrer na efetiva prestação de serviço de urgência.","A prioridade de passagem na via e no cruzamento deve se dar com velocidade reduzida e cuidados de segurança.","A livre estacionamento aplica-se quando os veículos estiverem identificados por iluminação intermitente."],"Art. 29, VII, e: livre circulação e parada só com alarme e iluminação.")
q(3,"A prioridade dos veículos de emergência, na via e no cruzamento, deve ser exercida com",["velocidade reduzida e os devidos cuidados de segurança.","velocidade máxima.","qualquer velocidade.","sem cuidados.","sem sinalização."],"Art. 29, VII, d.")
q(3,"Em cruzamento não sinalizado, a escada de preferência é: rodovia, rotatória e",["quem vier pela direita do condutor.","quem vier pela esquerda do condutor.","quem estiver em veículo maior.","quem estiver em veículo menor.","quem chegar primeiro."],"Art. 29, III.")
q(3,"A regra de que as faixas da direita se destinam aos veículos mais lentos e as da esquerda à ultrapassagem e aos veículos mais velozes aplica-se, em princípio, quando",["não houver faixa especial destinada a eles.","houver faixa especial.","a via for rural.","a via for urbana.","houver semáforo."],"Art. 29, IV.")
q(3,"A buzina, nas áreas urbanas, só pode ser usada para",["fazer advertências necessárias a fim de evitar sinistros.","advertir ultrapassagem.","cumprimentar.","chamar passageiros.","pedir passagem."],"Art. 41, I.")
q(3,"A troca de luz baixa e alta, de forma intermitente e por curto período, só pode ser utilizada para indicar a intenção de ultrapassar ou para indicar a existência de",["risco à segurança para os veículos que circulam no sentido contrário.","trânsito intenso.","buraco na via.","pedestre distante.","semáforo fechado."],"Art. 40, III.")
q(3,"O estacionamento dos veículos motorizados de duas rodas será feito, salvo sinalização diversa, em posição",["perpendicular à guia da calçada e junto a ela.","paralela à guia.","oblíqua.","sobre a calçada.","no meio da pista."],"Art. 48, § 2º.")
q(3,"As bicicletas, quando não houver ciclovia, ciclofaixa ou acostamento, circulam",["nos bordos da pista de rolamento, no mesmo sentido do fluxo, com preferência sobre os veículos automotores.","no meio da pista.","na calçada.","em sentido contrário.","apenas à noite."],"Art. 58, caput.")
q(3,"A circulação de bicicletas no sentido contrário ao fluxo dos veículos automotores só pode ser autorizada pela autoridade de trânsito, desde que dotado o trecho com",["ciclofaixa.","semáforo.","radar.","faixa de pedestres.","lombada."],"Art. 58, parágrafo único.")
q(3,"Os veículos de tração animal serão conduzidos",["pela direita da pista, junto à guia ou acostamento, sempre que não houver faixa especial.","pela esquerda.","no meio da pista.","pela calçada.","em qualquer lugar."],"Art. 52.")
q(3,"Os animais isolados ou em grupos só podem circular nas vias quando conduzidos por",["um guia.","qualquer pessoa.","um veterinário.","um policial.","um agente de trânsito."],"Art. 53.")
q(3,"Ao regular a velocidade, o condutor deverá observar constantemente as condições físicas da via, do veículo e da carga, as condições meteorológicas e a intensidade do trânsito, obedecendo aos limites máximos de velocidade estabelecidos para a via, além de, entre outras regras,",["não obstruir a marcha normal dos demais veículos, transitando a velocidade anormalmente reduzida, sem causa justificada.","aumentar sempre a velocidade.","manter velocidade constante.","acompanhar o veículo à frente.","buzinar ao frear."],"Art. 43, I.")
q(3,"As normas de ultrapassagem das alíneas a e b do inciso X e a e b do inciso XI do art. 29 aplicam-se à transposição de faixas, que pode ser realizada",["tanto pela faixa da esquerda como pela da direita.","apenas pela esquerda.","apenas pela direita.","apenas pelo acostamento.","apenas pela calçada."],"Art. 29, § 1º.")
q(3,"Nas vias providas de acostamento, os veículos parados, estacionados ou em operação de carga ou descarga deverão estar situados",["fora da pista de rolamento.","na pista de rolamento.","na calçada.","em qualquer local.","em fila dupla."],"Art. 48, § 1º.")
q(3,"No texto da viatura em atendimento, a viatura, ao passar no cruzamento com sirene, deve fazê-lo com",["velocidade reduzida e os devidos cuidados de segurança.","velocidade máxima.","sem reduzir.","sem sinal.","sem cuidados."],"Art. 29, VII, d.","ctb2a")
q(3,"No texto da via de rodagem, entre os dois condutores, o que excede o limite da via é",["o da via arterial (70 km/h, com limite de 60) e também o da estrada (70 km/h, com limite de 60).","apenas o da via arterial.","apenas o da estrada.","nenhum.","ambos estão abaixo."],"Art. 61, § 1º, I, b, e II, c.","ctb2b")
q(3,"No texto da via de rodagem, a velocidade mínima na via arterial, onde a máxima é 60 km/h, não poderá ser inferior a",["30 km/h.","20 km/h.","40 km/h.","50 km/h.","10 km/h."],"Art. 62: metade da máxima.","ctb2b")
assert len(Q)==60,len(Q)
code,svg=mapa("Circulação e conduta",[
 ("pref","Preferência",["rodovia, rotatória, direita","trilhos têm preferência","emergência: alarme e luz"],"seção 1"),
 ("ult","Ultrapassagem",["pela esquerda","proibida em curvas, pontes, interseções","indicar a manobra"],"seção 2"),
 ("luz","Luzes e buzina",["luz baixa à noite e sob chuva","pisca-alerta em emergência","buzina: toque breve"],"seção 3"),
 ("vel","Velocidades",["urbanas: 80, 60, 40, 30","rurais: 110/90, 100/90, 60","mínima: metade da máxima"],"seção 3"),
 ("par","Parada e estacionamento",["parada: embarque e desembarque","carga e descarga é estacionamento","moto: perpendicular"],"seção 4"),
 ("cint","Motos, crianças e cinto",["capacete e vestuário","menores de 10 anos e 1,45 m: atrás","cinto para todos"],"seção 4")],
 "Na prova: decore as velocidades, a escada de preferência e as proibições de ultrapassagem")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As quatro primeiras caixas seguem a sequência do próprio Código; a última reúne as regras de proteção do usuário.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 26 a 65, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-2","Normas gerais de circulação e conduta (CTB, arts. 26 a 65)",Q,list(tx),
 cobertura=["Recorte do edital: preferências, ultrapassagem, velocidades e conversões. Cobertos: arts. 26, 28, 29, 30, 31, 32, 33, 35, 36, 39, 40, 41, 42, 44, 44-A, 45, 47, 48, 52, 53, 54, 58, 60, 61, 62, 64 e 65. Não detalhados: arts. 27, 34, 37, 38, 43, 46, 49 a 51, 55, 57, 59, 67 e o Capítulo III-A (motoristas profissionais)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O Capítulo III-A (tempo de direção dos motoristas profissionais) não foi tratado e tem trecho declarado inconstitucional pela ADI 5.322 (citada na consolidação); fica para revisão.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb2a e ctb2b fictícios."],
 fontes_conferidas=["CTB, arts. 26 a 65: texto da Câmara, copiado por programa."])
gravar("ctb-2",aula_html,banco("ctb-2",Q),tx)
