import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEI, LEIS
F='ctb.txt'
C=lambda ref,txt: LEI(ref,txt,F)
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O posto ctb-7 trouxe as infrações de maior incidência (habilitação, álcool, velocidade, estacionamento, sinal vermelho). Este posto completa o Capítulo XV com o que ainda falta e cai bastante em prova de guarda: ultrapassagens e preferências, luzes e buzina, som automotivo, documentos, transporte remunerado irregular, motocicletas, celular ao volante, bloqueio de via e as infrações de pedestres e ciclistas. O foco é a natureza da infração (leve, média, grave ou gravíssima) e a conduta exata descrita no artigo."
S={}
S[1]="## 1. Ultrapassagem, preferência e manobras\n\n"+C("art. 200","Art. 200. Ultrapassar pela direita veículo de transporte coletivo ou de escolares, parado para embarque ou desembarque de passageiros, salvo quando houver refúgio de segurança para o pedestre: Infração - gravíssima; Penalidade - multa.")+"\n\n"+C("art. 201","Art. 201. Deixar de guardar a distância lateral de um metro e cinqüenta centímetros ao passar ou ultrapassar bicicleta: Infração - média; Penalidade - multa.")+"\n\n"+C("art. 202","Art. 202. Ultrapassar outro veículo: I - pelo acostamento; II - em interseções e passagens de nível; Infração - gravíssima;")+"\n\n"+L("art. 206","Art. 206. Executar operação de retorno","Art. 207.")+"\n\n"+C("art. 212","Art. 212. Deixar de parar o veículo antes de transpor linha férrea: Infração - gravíssima; Penalidade - multa.")+"\n\n"+L("art. 214","Art. 214. Deixar de dar preferência de passarem a pedestre","Art. 215.")+"\n\n"+L("art. 215","Art. 215. Deixar de dar preferência de passagem:","Art. 216.")+"""

**O que é, em uma frase:** a lei pune mais forte quem coloca o **pedestre** e o **vulnerável** em risco.

| Conduta | Natureza |
| --- | --- |
| Ultrapassar pela direita (regra) | Média (art. 199) |
| Ultrapassar pela direita **ônibus ou escolar parado** embarcando | **Gravíssima** (art. 200) |
| Não guardar **1,5 m** da bicicleta | Média (art. 201) |
| Ultrapassar pelo **acostamento** ou em interseção | **Gravíssima** (multa × 5) (art. 202) |
| Retorno proibido ou perigoso | Gravíssima (art. 206) |
| Não parar antes da **linha férrea** | Gravíssima (art. 212) |
| Não dar preferência ao pedestre **na faixa**, ao que **não terminou a travessia**, a deficientes, crianças, idosos e gestantes | **Gravíssima** (art. 214, I a III) |
| Pedestre que iniciou travessia sem sinalização; pedestre na via transversal | **Grave** (art. 214, IV e V) |
| Preferência em cruzamento não sinalizado (rotatória, rodovia, quem vem da direita) | Grave (art. 215) |
| Furar fila de veículos parados em sinal ou bloqueio | Grave (art. 211) |

> **Cuidado!** No art. 214, os incisos I a III são **gravíssimos** e os IV e V são **graves**. A banca troca.
"""
S[2]="## 2. Luzes, buzina, som, documentos e condições do veículo\n\n"+C("art. 224","Art. 224. Fazer uso do facho de luz alta dos faróis em vias providas de iluminação pública: Infração - leve; Penalidade - multa.")+"\n\n"+L("art. 227","Art. 227. Usar buzina:","Art. 228.")+"\n\n"+C("art. 228","Art. 228. Usar no veículo equipamento com som em volume ou freqüência que não sejam autorizados pelo CONTRAN: Infração - grave; Penalidade - multa.")+"\n\n"+C("art. 231, VIII","VIII - efetuando transporte remunerado de pessoas ou bens, quando não for licenciado para esse fim, salvo casos de força maior ou com permissão da autoridade competente: Infração - gravíssima;")+"\n\n"+C("art. 232","Art. 232. Conduzir veiculo sem os documentos de porte obrigatório referidos neste Código: Infração - leve; Penalidade - multa; Medida administrativa - retenção do veiculo até a apresentação do documento.")+"\n\n"+C("art. 234","Art. 234. Falsificar ou adulterar documento de habilitação e de identificação do veículo: Infração - gravíssima;")+"\n\n"+C("art. 238","Art. 238. Recusar-se a entregar à autoridade de trânsito ou a seus agentes, mediante recibo, os documentos de habilitação, de registro, de licenciamento de veículo e outros exigidos por lei, para averiguação de sua autenticidade: Infração - gravíssima;")+"\n\n"+C("art. 239","Art. 239. Retirar do local veículo legalmente retido para regularização, sem permissão da autoridade competente ou de seus agentes: Infração - gravíssima;")+"""

| Conduta | Natureza |
| --- | --- |
| Luz alta em via **iluminada** | Leve (art. 224) |
| Buzina prolongada, entre **22h e 6h**, ou fora do toque breve | Leve (art. 227) |
| Som em volume não autorizado | **Grave** + retenção (art. 228) |
| Alarme que perturba o sossego | Média (art. 229) |
| Película, cortina fechada, equipamento obrigatório ineficiente, mau estado | Grave + retenção (art. 230, VII a XIX) |
| Lâmpada queimada | Média (art. 230, XXII) |
| **Transporte remunerado** sem licença | **Gravíssima** + remoção (art. 231, VIII) |
| Lotação excedente | Grave (art. 231, VII) |
| Sem **documento de porte obrigatório** | **Leve** + retenção até apresentar (art. 232) |
| Não registrar veículo em 30 dias | Média (art. 233) |
| **Recusar** entregar documentos ao agente | **Gravíssima** (art. 238) |
| Retirar veículo **retido** sem permissão | Gravíssima (art. 239) |
| Falsa declaração de domicílio | Gravíssima (art. 242) |

> **Cuidado!** Alguns artigos ainda citam "apreensão do veículo" como penalidade, mas o inciso IV do art. 256 (apreensão) foi **revogado**. Em prova, foque na **natureza** e na **medida administrativa** (retenção ou remoção).
"""
S[3]="## 3. Motocicletas, celular, pedestres e ciclistas\n\n"+C("art. 244, I","I - sem usar capacete de segurança ou vestuário de acordo com as normas e as especificações aprovadas pelo Contran;")+"\n\n"+C("art. 244, V","V - transportando criança menor de 10 (dez) anos de idade ou que não tenha, nas circunstâncias, condições de cuidar da própria segurança: Infração - gravíssima; Penalidade - multa e suspensão do direito de dirigir;")+"\n\n"+L("art. 252","Art. 252. Dirigir o veículo:","Art. 253.")+"\n\n"+C("art. 253","Art. 253. Bloquear a via com veículo: Infração - gravíssima;")+"\n\n"+L("art. 254, caput","Art. 254. É proibido ao pedestre:","VII - (VETADO")+"\n\n"+C("art. 255","Art. 255. Conduzir bicicleta em passeios onde não seja permitida a circulação desta, ou de forma agressiva, em desacordo com o disposto no parágrafo único do art. 59: Infração - média; Penalidade - multa; Medida administrativa - remoção da bicicleta, mediante recibo para o pagamento da multa.")+"""

**Moto (art. 244)**
- **Gravíssima + suspensão:** sem capacete; passageiro sem capacete ou fora do assento; malabarismo ou "uma roda"; **criança menor de 10 anos**.
- **Grave:** rebocar outro veículo; sem segurar o guidom com as duas mãos; carga incompatível; transporte remunerado irregular de mercadorias.
- **Média:** capacete sem viseira ou óculos de proteção.

**Celular (art. 252)**
- Dirigir com fone ou **usando** celular: **média**.
- **Segurando ou manuseando** o celular: **gravíssima** (parágrafo único).

**Luzes (art. 250):** luz baixa à noite; de dia em túneis, sob chuva, neblina ou cerração; motos sempre; rodovias de pista simples fora da cidade sem luz diurna: média. Porta aberta de ônibus ou escolar em movimento: **gravíssima**.

**Pedestre (art. 254):** leve, com multa de **50%** do valor da leve. **Bicicleta na calçada proibida ou de forma agressiva (art. 255):** média, com remoção da bicicleta.

> **Macete:** "**segurou, gravíssima**": celular na mão é a pegadinha mais comum do art. 252.
"""
S[5]="""## 5. Na rotina do guarda

Em Campinas, a fiscalização de trânsito é feita pela EMDEC; a guarda municipal autua quando há convênio ou competência delegada (CTB, art. 280, § 4º) e atua sempre na proteção do pedestre e na segurança viária.

- **Moto com criança pequena na garupa:** gravíssima, com suspensão e retenção (art. 244, V).
- **Som alto no carro na praça:** grave, com retenção (art. 228); se perturbar o sossego, também pode haver contravenção penal.
- **Carro de aplicativo pirata:** transporte remunerado sem licença é gravíssimo, com remoção (art. 231, VIII).
- **Condutor recusa entregar a CNH:** gravíssima (art. 238); se só esqueceu o documento, é leve (art. 232).
- **Bloqueio de via em protesto com veículos:** art. 253-A, gravíssima com suspensão por 12 meses; organizadores pagam multa agravada em 60 vezes.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Celular ao volante | Usar ou fone: média; **segurar ou manusear**: gravíssima |
| Esquecer a CNH em casa | Leve (art. 232), não gravíssima |
| Recusar entregar documentos | Gravíssima (art. 238) |
| Criança na garupa da moto | Menor de 10 anos: gravíssima |
| Luz alta na cidade iluminada | Leve |
| Buzina | Proibida das 22h às 6h; leve |
| Pedestre infrator | Leve, com multa de 50% |
| Distância da bicicleta | 1,5 m; média |
| Ultrapassar ônibus escolar parado pela direita | Gravíssima, salvo refúgio para o pedestre |
| Preferência ao pedestre na faixa | Gravíssima |
"""
S[7]="""## 7. Quadro-resumo

| Artigo | Conduta | Natureza |
| --- | --- | --- |
| 200 | Ultrapassar pela direita coletivo ou escolar parado | Gravíssima |
| 201 | 1,5 m da bicicleta | Média |
| 202 | Ultrapassar pelo acostamento ou em interseção | Gravíssima (× 5) |
| 212 | Não parar antes de linha férrea | Gravíssima |
| 214, I a III | Preferência a pedestre na faixa, travessia não concluída, vulneráveis | Gravíssima |
| 224 | Luz alta em via iluminada | Leve |
| 227 | Buzina indevida | Leve |
| 228 | Som não autorizado | Grave |
| 231, VIII | Transporte remunerado sem licença | Gravíssima |
| 232 | Sem documento de porte obrigatório | Leve |
| 238 | Recusar entregar documentos | Gravíssima |
| 244 | Moto sem capacete; criança menor de 10 | Gravíssima |
| 252 | Celular: usar (média); segurar (gravíssima) | Média ou gravíssima |
| 253 | Bloquear a via com veículo | Gravíssima |
| 254 | Pedestre | Leve (50%) |
| 255 | Bicicleta na calçada proibida | Média |
"""
QR=[("Questão 1","Dirigir o veículo segurando ou manuseando telefone celular é infração",["gravíssima.","leve.","média.","grave.","não prevista no CTB."],0,"Art. 252, parágrafo único."),
("Questão 2","Conduzir motocicleta transportando criança menor de 10 anos é infração",["gravíssima, com multa e suspensão do direito de dirigir.","média, com multa.","leve, com advertência.","grave, com multa.","permitida, com capacete."],1,"Art. 244, V."),
("Questão 3","Conduzir veículo sem os documentos de porte obrigatório é infração",["leve, com retenção do veículo até a apresentação do documento.","gravíssima, com remoção.","grave, com multa.","média, com recolhimento da CNH.","não punível."],2,"Art. 232."),
("Questão 4","Deixar de dar preferência ao pedestre que se encontre na faixa a ele destinada é infração",["gravíssima.","leve.","média.","grave.","isenta de multa."],3,"Art. 214, I.")]
t1="<strong>O motoqueiro e o filho</strong><br><br>Na saída de uma escola municipal, um pai passou de motocicleta levando o filho de 7 anos na garupa, os dois de capacete."
t2="<strong>O celular no semáforo</strong><br><br>Uma motorista digitava mensagens no celular, com o aparelho na mão, enquanto conduzia o carro pela avenida."
t3="<strong>O som na praça</strong><br><br>Um carro com o porta-malas aberto tocava música em volume muito alto em frente a uma praça, e o dono, ao ser abordado, recusou-se a entregar a CNH e o documento do veículo."
tx={"ctb11a":t1,"ctb11b":t2,"ctb11c":t3}
# n=1
q(1,"Ultrapassar pela direita veículo de transporte coletivo parado para embarque, sem refúgio para pedestre, é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 200.")
q(1,"Ao ultrapassar bicicleta, o condutor deve guardar distância lateral de",["um metro e cinquenta centímetros.","cinquenta centímetros.","um metro.","dois metros.","três metros."],"Art. 201.")
q(1,"Ultrapassar outro veículo pelo acostamento é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 202, I.")
q(1,"Deixar de parar o veículo antes de transpor linha férrea é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 212.")
q(1,"Usar o facho de luz alta em vias providas de iluminação pública é infração",["leve.","gravíssima.","grave.","média.","isenta."],"Art. 224.")
q(1,"É proibido usar buzina entre as",["vinte e duas e as seis horas.","dezoito e as seis horas.","vinte e as oito horas.","meia-noite e as cinco horas.","vinte e três e as sete horas."],"Art. 227, III.")
q(1,"Usar no veículo som em volume ou frequência não autorizados pelo Contran é infração",["grave.","leve.","média.","gravíssima.","isenta."],"Art. 228.")
q(1,"Efetuar transporte remunerado de pessoas sem licença para esse fim é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 231, VIII.")
q(1,"Conduzir veículo sem os documentos de porte obrigatório é infração",["leve.","gravíssima.","grave.","média.","isenta."],"Art. 232.")
q(1,"Recusar-se a entregar ao agente os documentos de habilitação e do veículo é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 238.")
q(1,"Conduzir motocicleta sem capacete de segurança é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 244, I.")
q(1,"Dirigir com fones nos ouvidos conectados a aparelhagem sonora é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 252, VI.")
q(1,"Dirigir o veículo com o braço do lado de fora é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 252, I.")
q(1,"Bloquear a via com veículo é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 253.")
q(1,"As infrações cometidas por pedestres são de natureza",["leve.","média.","grave.","gravíssima.","penal."],"Art. 254.")
q(1,"Conduzir bicicleta em passeio onde não seja permitida a circulação é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 255.")
q(1,"Retirar do local veículo legalmente retido, sem permissão, é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 239.")
q(1,"No texto do motoqueiro e o filho, o transporte da criança de 7 anos na moto é infração",["gravíssima.","leve.","média.","grave.","permitida, pois ambos usavam capacete."],"Art. 244, V.","ctb11a")
q(1,"No texto do celular no semáforo, a motorista que segura e manuseia o celular comete infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 252, parágrafo único.","ctb11b")
q(1,"No texto do som na praça, o som em volume não autorizado configura infração",["grave.","leve.","média.","gravíssima.","isenta."],"Art. 228.","ctb11c")
# n=2
q(2,"Ultrapassar pela direita, salvo quando o veículo da frente estiver na faixa apropriada e sinalizar que vai entrar à esquerda, é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 199.")
q(2,"Ultrapassar veículos em fila, parados em razão de sinal luminoso ou bloqueio, com exceção dos não motorizados, é infração",["grave.","leve.","média.","gravíssima.","isenta."],"Art. 211.")
q(2,"Deixar de parar quando a marcha for interceptada por agrupamento de pessoas, como passeatas e desfiles, é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 213, I.")
q(2,"Deixar de dar preferência ao pedestre que já iniciou a travessia, mesmo sem sinalização a ele destinada, é infração",["grave.","gravíssima.","leve.","média.","isenta."],"Art. 214, IV.")
q(2,"Em interseção não sinalizada, a preferência é do veículo que circula por rodovia ou rotatória e do que vier da",["direita.","esquerda.","frente.","contramão.","via secundária."],"Art. 215, I.")
q(2,"Deixar de manter ligada, em atendimento de emergência, a iluminação intermitente de ambulâncias e viaturas de polícia, ainda que paradas, é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 222.")
q(2,"Transitar com o farol desregulado, perturbando a visão de outro condutor, é infração grave, com medida administrativa de",["retenção do veículo para regularização.","remoção do veículo.","recolhimento da CNH.","apreensão da placa.","nenhuma medida."],"Art. 223.")
q(2,"Usar indevidamente aparelho de alarme que perturbe o sossego público é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 229.")
q(2,"Conduzir com vidros cobertos por películas não autorizadas é infração",["grave.","leve.","média.","gravíssima.","isenta."],"Art. 230, XVI.")
q(2,"Conduzir com defeito no sistema de iluminação ou com lâmpadas queimadas é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 230, XXII.")
q(2,"Deixar de efetuar o registro do veículo no prazo de trinta dias, nas hipóteses do art. 123, é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 233.")
q(2,"Rebocar outro veículo com cabo flexível ou corda, salvo emergência, é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 236.")
q(2,"Fazer falsa declaração de domicílio para fins de registro, licenciamento ou habilitação é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 242.")
q(2,"Conduzir motocicleta com capacete sem viseira ou óculos de proteção é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 244, X.")
q(2,"Deixar o veículo de transporte coletivo ou escolar de manter a porta fechada, em movimento, é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 250, IV.")
q(2,"Utilizar o pisca-alerta fora de imobilizações ou situações de emergência é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 251, I.")
q(2,"A multa aplicada ao pedestre corresponde a",["50% do valor da infração de natureza leve.","100% do valor da infração média.","o dobro da infração leve.","20% da infração grave.","valor fixo de gravíssima."],"Art. 254.")
q(2,"No texto do motoqueiro e o filho, além da multa, a penalidade inclui",["suspensão do direito de dirigir.","cassação da CNH.","advertência apenas.","curso de reciclagem apenas.","nenhuma outra."],"Art. 244, V.","ctb11a")
q(2,"No texto do celular no semáforo, se a motorista apenas usasse fone conectado ao celular, a infração seria",["média.","gravíssima.","leve.","grave.","isenta."],"Art. 252, VI.","ctb11b")
q(2,"No texto do som na praça, a recusa em entregar a CNH e o documento do veículo é infração",["gravíssima.","leve.","média.","grave.","isenta."],"Art. 238.","ctb11c")
# n=3
q(3,"Assinale a alternativa correta sobre o art. 214 do CTB.",["Deixar de dar preferência a idosos e gestantes é gravíssima; ao pedestre que atravessa a via transversal para onde se dirige o veículo é grave.","Todas as hipóteses são gravíssimas.","Todas as hipóteses são graves.","Não dar preferência ao pedestre na faixa é média.","O artigo não protege veículos não motorizados."],"Art. 214.")
q(3,"Considere. I. Dirigir usando celular sem segurá-lo é infração média. II. Dirigir segurando o celular é gravíssima. III. Dirigir com fone conectado ao celular é leve. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Art. 252, VI e parágrafo único: fone é média.")
q(3,"Assinale a INCORRETA.",["Conduzir sem documento de porte obrigatório é infração gravíssima.","Usar buzina prolongada e sucessivamente é infração leve.","Usar luz alta em via iluminada é infração leve.","Bloquear a via com veículo é gravíssima.","Ultrapassar pelo acostamento é gravíssima."],"Art. 232: leve.")
q(3,"Ultrapassar outro veículo pelo acostamento ou em interseções e passagens de nível é gravíssima, com multa",["multiplicada por cinco.","em dobro.","simples.","multiplicada por dez.","reduzida à metade."],"Art. 202.")
q(3,"No art. 244, as condutas de rebocar outro veículo com a moto, sem segurar o guidom com ambas as mãos e transportando carga incompatível são infrações",["graves.","gravíssimas.","leves.","médias.","isentas."],"Art. 244, VI a IX.")
q(3,"Ao ciclista aplica-se a infração de conduzir passageiro fora da garupa ou do assento especial, sendo infração",["média.","gravíssima.","grave.","leve.","isenta."],"Art. 244, § 1º, a, e § 2º.")
q(3,"Usar veículo para, deliberadamente, interromper a circulação na via sem autorização é infração gravíssima, com multa de vinte vezes e suspensão do direito de dirigir por",["12 meses.","6 meses.","2 meses.","24 meses.","30 dias."],"Art. 253-A.")
q(3,"Aos organizadores da conduta de bloqueio deliberado da via com veículos, a multa é agravada em",["60 vezes.","20 vezes.","10 vezes.","5 vezes.","2 vezes."],"Art. 253-A, § 1º.")
q(3,"Deixar de sinalizar obstáculo à livre circulação no leito da via ou na calçada é infração gravíssima, com multa agravada em até",["cinco vezes, conforme o risco à segurança.","duas vezes.","dez vezes.","vinte vezes.","sessenta vezes."],"Art. 246.")
q(3,"Utilizar a via para depósito de mercadorias, sem autorização, é infração grave, com medida administrativa de",["remoção da mercadoria ou do material.","apreensão do veículo.","recolhimento da CNH.","retenção do veículo.","interdição do estabelecimento."],"Art. 245.")
q(3,"Deixar de manter acesa a luz baixa, de dia, sob chuva, neblina ou cerração, é infração",["média.","leve.","grave.","gravíssima.","isenta."],"Art. 250, I, b.")
q(3,"Conduzir pessoas, animais ou carga nas partes externas do veículo, salvo nos casos autorizados, é infração grave, com",["retenção do veículo para transbordo.","remoção do veículo.","recolhimento da CNH.","apreensão do animal.","advertência apenas."],"Art. 235.")
q(3,"A infração do art. 252, V (dirigir com apenas uma das mãos), torna-se gravíssima quando o condutor estiver",["segurando ou manuseando telefone celular.","fazendo sinais de braço.","mudando a marcha.","acionando o limpador.","ligando o pisca."],"Art. 252, parágrafo único.")
q(3,"Deixar a seguradora de comunicar ao órgão de trânsito a perda total do veículo e de devolver placas e documentos é infração",["grave.","leve.","média.","gravíssima.","isenta."],"Art. 243.")
q(3,"Ultrapassar veículo em movimento que integre cortejo, préstito, desfile ou formação militar, sem autorização, é infração",["leve.","gravíssima.","grave.","média.","isenta."],"Art. 205.")
q(3,"No texto do motoqueiro e o filho, a medida administrativa prevista é a",["retenção do veículo até regularização e o recolhimento do documento de habilitação.","remoção da criança pelo Conselho Tutelar.","apreensão do capacete.","advertência verbal.","interdição da escola."],"Art. 244, V.","ctb11a")
q(3,"No texto do celular no semáforo, a regra aplicada é a do art. 252, que transforma em gravíssima a hipótese de dirigir com",["apenas uma das mãos, segurando ou manuseando o celular.","braço para fora.","calçado inadequado.","fone de ouvido.","incapacidade física temporária."],"Art. 252, V e parágrafo único.","ctb11b")
q(3,"No texto do som na praça, se o condutor apenas tivesse esquecido os documentos em casa, a infração seria",["leve, com retenção até a apresentação do documento.","gravíssima.","grave.","média.","isenta."],"Art. 232.","ctb11c")
q(3,"No texto do som na praça, a medida administrativa prevista para o som em volume não autorizado é a",["retenção do veículo para regularização.","remoção do veículo.","cassação da CNH.","apreensão da placa.","prisão em flagrante."],"Art. 228.","ctb11c")
q(3,"No texto do som na praça, a atuação dos guardas, em Campinas, na autuação de trânsito depende de",["convênio ou competência delegada pelo órgão de trânsito com circunscrição sobre a via.","autorização do juiz.","pedido do motorista.","decisão da Câmara.","nada, pois a guarda é órgão de trânsito por natureza."],"CTB, art. 280, § 4º.","ctb11c")
from collections import Counter; c=Counter(x[0] for x in Q); print(c); assert c=={1:20,2:20,3:20}
code,svg=mapa("CTB: demais infrações",[
 ("ult","Ultrapassagem",["direita: média","ônibus parado: gravíssima","acostamento: gravíssima × 5"],"seção 1"),
 ("pre","Preferência",["pedestre na faixa: gravíssima","vulneráveis: gravíssima","rotatória e quem vem da direita"],"seção 1"),
 ("lb","Luzes e som",["luz alta na cidade: leve","buzina 22h–6h: leve","som alto: grave"],"seção 2"),
 ("doc","Documentos",["esqueceu: leve","recusou entregar: gravíssima","falsificou: gravíssima"],"seção 2"),
 ("mot","Moto e celular",["sem capacete: gravíssima","criança < 10: gravíssima","celular na mão: gravíssima"],"seção 3"),
 ("ped","Pedestre e ciclista",["pedestre: leve 50%","bicicleta na calçada: média","bloquear via: gravíssima"],"seção 3")],
 "Na prova: identifique a natureza da infração e a medida administrativa")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha trata da ultrapassagem e da preferência; a segunda, das luzes, documentos, motos, pedestres e ciclistas.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (CTB), consolidação da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-11","CTB: demais infrações (arts. 179 a 255)",Q,list(tx),
 cobertura=["Complementa o ctb-7: arts. 199 a 206, 211 a 215, 222 a 255 (selecionados). Somados, ctb-7 e ctb-11 cobrem o Capítulo XV."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin); reconferir no Planalto.","Alguns artigos ainda mencionam 'apreensão do veículo' como penalidade, embora o art. 256, IV, tenha sido revogado; as questões não cobram esse ponto.","Casos ctb11a, ctb11b e ctb11c fictícios."],
 fontes_conferidas=["CTB, arts. 199 a 255: texto da Câmara, copiado por programa."])
gravar("ctb-11",aula_html,banco("ctb-11",Q),tx)
