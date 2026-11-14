import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O processo administrativo é o caminho da infração até a multa paga ou o recurso julgado: auto de infração, notificação da autuação, defesa prévia, penalidade, notificação da penalidade, recurso à JARI e depois ao Cetran. Para o guarda municipal, é o capítulo mais próximo do trabalho diário, porque quem lavra o auto é o agente de trânsito. A Vunesp cobra os requisitos do auto, quem pode lavrá-lo, os prazos (30 dias, 180 e 360 dias, 24 meses), os descontos no pagamento e os efeitos do recurso."
S={}
S[1]="## 1. A autuação\n\n"+L("art. 280, caput","Art. 280. Ocorrendo infração","§ 1º (VETADO) § 2º A infração")+"\n\n"+L("art. 280, §§ 2º e 3º","§ 2º A infração deverá ser comprovada","§ 4º O agente")+"\n\n"+L("art. 280, § 4º","§ 4º O agente da autoridade","§ 5º (VETADO na Lei nº 14.599")+"\n\n"+L("art. 280, § 6º","§ 6º Não há infração de circulação","Seção II")+"""

Lavra-se o auto de infração quando ocorre infração prevista na legislação de trânsito. Ele traz a tipificação, o local, a data e a hora, os caracteres da placa, a marca e a espécie do veículo, o prontuário do condutor (sempre que possível), a identificação do órgão e do agente ou equipamento autuador e a assinatura do infrator, que vale como notificação. A infração é comprovada por declaração do agente, aparelho eletrônico, equipamento audiovisual, reações químicas ou outro meio previamente regulamentado pelo Contran. Quem não pode ser autuado em flagrante é relatado no próprio auto, para o procedimento seguinte.

O agente que pode lavrar o auto é o servidor civil, estatutário ou celetista, ou o policial militar designado pela autoridade de trânsito com jurisdição sobre a via. É o caso do guarda municipal designado pelo órgão de trânsito do Município. Não há infração de circulação, parada ou estacionamento relativa a veículos de socorro de incêndio e salvamento, de polícia, de fiscalização e operação de trânsito e a ambulâncias, ainda que não identificados ostensivamente.
"""
S[2]="## 2. Julgamento do auto, defesa prévia e notificação\n\n"+L("art. 281, caput","Art. 281. A autoridade","§ 1º O auto de infração será arquivado")+"\n\n"+L("art. 281, § 1º","I - se considerado inconsistente","§ 2º O prazo para expedição")+"\n\n"+L("arts. 281-A e 282","Art. 281-A. Na notificação","§ 1º A notificação devolvida")+"\n\n"+L("art. 282, § 4º","§ 4º Da notificação","§ 6º O prazo")+"\n\n"+L("art. 282, §§ 6º e 7º","§ 6º O prazo para expedição","§ 6º-A.")+"\n\n"+L("art. 282, § 7º","§ 7º O descumprimento","§ 8º (VETADO")+"""

A autoridade de trânsito julga a consistência do auto e aplica a penalidade. O auto é arquivado, e o registro julgado insubsistente, se for inconsistente ou irregular, ou se a notificação da autuação não for expedida em até 30 dias. A notificação da autuação deve indicar o prazo para a defesa prévia, que não pode ser inferior a 30 dias. Se a defesa prévia for indeferida ou não for apresentada, aplica-se a penalidade e expede-se nova notificação, ao proprietário do veículo ou ao infrator. A notificação devolvida por endereço desatualizado ou por recusa vale para todos os efeitos.

Da notificação da penalidade deve constar o prazo para recurso, que não pode ser inferior a 30 dias. Em multa, essa data é também a do recolhimento. O prazo para expedir a notificação da penalidade é de 180 dias, ou de 360 dias se houve defesa prévia; descumprido, ocorre a decadência do direito de aplicar a penalidade. Quando a multa é imposta ao condutor, a notificação vai ao proprietário, que responde pelo pagamento.
"""
S[3]="## 3. Pagamento da multa e recursos\n\n"+L("art. 284, caput e § 1º","Art. 284. O pagamento da multa","§ 2º O recolhimento")+"\n\n"+L("art. 284, § 2º e § 3º","§ 2º O recolhimento","§ 4º Encerrada")+"\n\n"+L("arts. 285 e 286","Art. 285. O recurso contra","§ 3º [revogado]")+"\n\n"+L("art. 285, § 6º","§ 6º O recurso de que trata","Art. 286.")+"\n\n"+L("arts. 286 a 288","Art. 286. O recurso contra a imposição","Art. 289.")+"""

A multa pode ser paga até o vencimento por 80% do valor. Se o infrator optar, pelo sistema de notificação eletrônica, por não apresentar defesa nem recurso e reconhecer a infração, o desconto é de 40% (paga-se 60%). Pagar a multa não impede questionar o processo, e enquanto não encerrada a instância administrativa não incide cobrança moratória nem restrição ao licenciamento ou à transferência.

O recurso contra a penalidade é interposto perante a autoridade que a impôs e tem efeito suspensivo; o intempestivo ou de parte ilegítima não tem efeito suspensivo e é arquivado. A autoridade remete o recurso à JARI em dez dias, e a JARI julga no prazo de 24 meses. O recurso contra multa pode ser interposto sem o recolhimento do valor; se o infrator pagar e o recurso vencer, a quantia é devolvida, corrigida. Das decisões da JARI cabe novo recurso, em trinta dias, ao Cetran (penalidade estadual ou municipal) ou ao Contrandife (Distrito Federal), ou a colegiado especial (União).
"""
S[4]="## 4. Segunda instância e encerramento\n\n"+L("art. 289, caput e incisos","Art. 289. O recurso de que trata","Parágrafo único. No caso")+"\n\n"+L("arts. 289-A e 290","Art. 289-A. O não julgamento","Art. 290-A.")+"""

O recurso à segunda instância é julgado em 24 meses. Se isso não ocorre, em qualquer das duas instâncias, ocorre a prescrição da pretensão punitiva. Encerram a instância administrativa o julgamento do recurso, a não interposição no prazo legal e o pagamento da multa com reconhecimento da infração e requerimento de encerramento do processo, sem defesa ou recurso. Esgotados os recursos, as penalidades são cadastradas no Renach. Os prazos processuais não se suspendem, salvo força maior comprovada.
"""
S[5]="""## 5. Na rotina do guarda

- **Preencher o auto:** tipificação, local, data e hora, placa, marca e espécie, identificação do agente, e assinatura do infrator quando possível; sem ela, o auto segue por notificação.
- **Autuar em flagrante:** quando não for possível, o agente relata o fato no auto e informa os dados do veículo.
- **Veículos de emergência:** não há infração de circulação, parada ou estacionamento por viatura de socorro, de polícia, de fiscalização ou ambulância.
- **Prova:** declaração do agente, aparelho eletrônico, imagem; o auto deve ser consistente para não ser arquivado.
- **Prazos:** o auto é arquivado se a notificação da autuação não sair em 30 dias.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Prazo da notificação da autuação | 30 dias; senão o auto é arquivado |
| Defesa prévia | Prazo não inferior a 30 dias |
| Prazo para recurso | Não inferior a 30 dias da notificação da penalidade |
| Notificação da penalidade | 180 dias, ou 360 com defesa prévia; senão decadência |
| Desconto no pagamento | 80% até o vencimento; 60% se optar pelo sistema eletrônico sem defesa nem recurso |
| Efeito do recurso | Suspensivo, se tempestivo e de parte legítima |
| Remessa à JARI | 10 dias |
| Julgamento | 24 meses; senão prescrição da pretensão punitiva |
| Recurso das decisões da JARI | 30 dias, ao Cetran ou Contrandife |
| Quem lava o auto | Servidor civil (estatutário ou celetista) ou policial militar designado |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Auto de infração | Tipificação, local, data, hora, placa, agente, assinatura |
| Quem lava | Servidor civil ou policial militar designado |
| Veículos de emergência | Sem infração de circulação, parada ou estacionamento |
| Notificação da autuação | 30 dias; senão, arquivamento |
| Defesa prévia | Mínimo 30 dias |
| Notificação da penalidade | 180 dias; 360 com defesa |
| Recurso | Mínimo 30 dias; efeito suspensivo |
| Pagamento | 80% até o vencimento; 60% sem defesa nem recurso |
| JARI | Remessa em 10 dias; 24 meses |
| Cetran / Contrandife | Recurso em 30 dias; 24 meses |
| Encerramento | Julgamento, prazo ou pagamento com reconhecimento |
"""
QR=[("Questão 1","O auto de infração será arquivado, e seu registro julgado insubsistente, se não for expedida a notificação da autuação no prazo máximo de",["trinta dias.","dez dias.","sessenta dias.","noventa dias.","cento e oitenta dias."],0,"Art. 281, § 1º, II."),
("Questão 2","O prazo para apresentação de defesa prévia, na notificação de autuação, não será inferior a",["trinta dias, contado da data de expedição da notificação.","cinco dias.","dez dias.","quinze dias.","sessenta dias."],1,"Art. 281-A."),
("Questão 3","O recurso contra a penalidade será interposto perante a autoridade que imputou a penalidade e terá efeito",["suspensivo.","devolutivo apenas.","nenhum.","meramente declaratório.","retroativo."],2,"Art. 285."),
("Questão 4","O pagamento da multa pode ser efetuado até a data do vencimento expressa na notificação, por",["oitenta por cento do seu valor.","metade do valor.","cem por cento, sem desconto.","setenta por cento.","noventa por cento."],3,"Art. 284.")]
t1="<strong>Autuação de uma Guarda Municipal</strong><br><br>Um guarda municipal designado pelo órgão de trânsito de Vila Nova, cidade fictícia, lavrou auto de infração por estacionamento irregular, sem a assinatura do condutor, que não foi localizado."
t2="<strong>Notificação da penalidade</strong><br><br>Um proprietário recebeu a notificação da autuação em 20 dias, apresentou defesa prévia, que foi indeferida, e recebeu a notificação da penalidade. Ele pretende recorrer sem pagar a multa."
t3="<strong>Recurso à JARI</strong><br><br>Um condutor recorreu da penalidade de multa. O recurso foi tempestivo e a autoridade o remeteu à Jari. O recurso foi julgado improcedente, e o condutor pretende recorrer ao Cetran."
tx={"ctb9a":t1,"ctb9b":t2,"ctb9c":t3}
# n=1
q(1,"Ocorrendo infração prevista na legislação de trânsito, lavrar-se-á",["auto de infração.","termo de ajuste.","alvará.","edital.","contrato."],"Art. 280.")
q(1,"Do auto de infração constará a tipificação da infração e o local, a data e a hora do",["cometimento da infração.","nascimento do condutor.","licenciamento anterior.","pagamento.","recurso."],"Art. 280, II.")
q(1,"A assinatura do infrator no auto de infração, sempre que possível, vale como",["notificação do cometimento da infração.","confissão.","pagamento.","procuração.","renúncia."],"Art. 280, VI.")
q(1,"O agente da autoridade de trânsito competente para lavrar o auto de infração poderá ser servidor civil, estatutário ou celetista, ou policial militar designado pela",["autoridade de trânsito com jurisdição sobre a via.","empresa privada.","associação de moradores.","Câmara de Vereadores.","imprensa."],"Art. 280, § 4º.")
q(1,"A infração poderá ser comprovada por declaração da autoridade ou do agente, aparelho eletrônico, equipamento audiovisual ou outro meio previamente regulamentado pelo",["Contran.","Congresso.","Detran, sozinho.","Município, sozinho.","STF."],"Art. 280, § 2º.")
q(1,"Não há infração de circulação, parada ou estacionamento relativa aos veículos de socorro de incêndio e salvamento, aos de polícia, aos de fiscalização e operação de trânsito e às",["ambulâncias.","motocicletas.","bicicletas.","vans.","carroças."],"Art. 280, § 6º.")
q(1,"A autoridade de trânsito julgará a consistência do auto de infração e aplicará a",["penalidade cabível.","medida política.","lei.","isenção.","anistia."],"Art. 281.")
q(1,"A notificação da autuação deve constar o prazo para apresentação de",["defesa prévia.","indenização.","contraprova de embriaguez.","perícia.","doação."],"Art. 281-A.")
q(1,"Caso a defesa prévia seja indeferida ou não seja apresentada, será",["aplicada a penalidade e expedida a notificação.","arquivado o auto.","extinta a infração.","perdoada a multa.","aplicada a prescrição."],"Art. 282.")
q(1,"Da notificação da penalidade deve constar a data do término do prazo para apresentação de",["recurso.","comissão.","reajuste.","transferência.","isenção."],"Art. 282, § 4º.")
q(1,"O prazo para recurso, na notificação da penalidade, não será inferior a",["trinta dias.","cinco dias.","dez dias.","quinze dias.","sessenta dias."],"Art. 282, § 4º.")
q(1,"O descumprimento dos prazos para expedição das notificações das penalidades implicará a",["decadência do direito de aplicar a respectiva penalidade.","prescrição da multa.","anistia.","prisão.","suspensão do processo."],"Art. 282, § 7º.")
q(1,"O pagamento da multa não implica renúncia ao",["questionamento administrativo.","pagamento.","prazo.","processo penal.","licenciamento."],"Art. 284, § 2º.")
q(1,"O recurso contra a imposição de multa poderá ser interposto no prazo legal, sem o recolhimento do seu",["valor.","prazo.","endereço.","processo.","comprovante."],"Art. 286.")
q(1,"A autoridade que receber o recurso tempestivo o remeterá à Jari no prazo de",["dez dias, contado da data de sua interposição.","três dias.","cinco dias.","trinta dias.","sessenta dias."],"Art. 285, § 2º.")
q(1,"Das decisões da JARI cabe recurso no prazo de",["trinta dias, contado da publicação ou da notificação da decisão.","cinco dias.","dez dias.","quinze dias.","sessenta dias."],"Art. 288.")
q(1,"Os recursos contra as decisões da JARI, em penalidades estaduais e municipais, são julgados pelos",["Cetran.","Municípios.","Procons.","tribunais de contas.","sindicatos."],"Art. 289, II.")
q(1,"No texto da autuação da guarda municipal, o agente designado pelo órgão de trânsito pode lavrar o auto porque o art. 280, § 4º, admite como autuador o",["servidor civil, estatutário ou celetista, designado pela autoridade de trânsito.","guarda aposentado.","vizinho.","fiscal da prefeitura sem designação.","oficial de justiça."],"Art. 280, § 4º.","ctb9a")
q(1,"No texto do recurso à JARI, o recurso tempestivo, interposto perante a autoridade que impôs a penalidade, tem efeito",["suspensivo.","nenhum.","devolutivo apenas.","meramente informativo.","retroativo."],"Art. 285.","ctb9c")
q(1,"No texto da notificação da penalidade, o proprietário pretende recorrer sem recolher o valor da multa, o que é",["permitido, pois o recurso pode ser interposto sem o recolhimento.","proibido.","permitido apenas com depósito.","permitido apenas para infração leve.","dependente de fiador."],"Art. 286.","ctb9b")
# n=2
q(2,"Constam do auto de infração os caracteres da placa de identificação do veículo, sua marca e espécie e outros elementos julgados necessários à sua",["identificação.","venda.","avaliação.","pintura.","seguradora."],"Art. 280, III.")
q(2,"Não sendo possível a autuação em flagrante, o agente de trânsito relatará o fato à autoridade no próprio auto de infração, informando os dados a respeito do",["veículo, além dos incisos I, II e III.","condutor, apenas.","vizinho.","estacionamento.","semáforo."],"Art. 280, § 3º.")
q(2,"O auto de infração será arquivado se considerado inconsistente ou",["irregular.","claro.","assinado.","pago.","digital."],"Art. 281, § 1º, I.")
q(2,"O prazo para expedição da notificação da autuação referente às penalidades de suspensão e de cassação é contado a partir da data da",["instauração do processo destinado à aplicação dessas penalidades.","infração.","licença.","prisão.","compra."],"Art. 281, § 2º.")
q(2,"A notificação devolvida por desatualização do endereço do proprietário ou por recusa em recebê-la será considerada",["válida para todos os efeitos.","nula.","suspensa.","inexistente.","provisória."],"Art. 282, § 1º.")
q(2,"Sempre que a multa for imposta a condutor, a notificação será encaminhada ao proprietário do veículo, responsável pelo seu",["pagamento.","cadastro.","reparo.","seguro.","depósito."],"Art. 282, § 3º.")
q(2,"O prazo para expedição das notificações das penalidades é de 180 dias ou, se houver interposição de defesa prévia, de",["360 dias.","240 dias.","270 dias.","540 dias.","720 dias."],"Art. 282, § 6º.")
q(2,"A notificação por meio eletrônico considera notificado o proprietário ou o condutor autuado em",["30 dias após a inclusão da informação no sistema e o envio da mensagem.","imediatamente.","10 dias.","60 dias.","90 dias."],"Art. 282-A, § 2º.")
q(2,"Quem opta, pelo sistema eletrônico, por não apresentar defesa prévia nem recurso, reconhecendo a infração, pode pagar a multa por",["60% do valor.","80% do valor.","40% do valor.","50% do valor.","30% do valor."],"Art. 284, § 1º.")
q(2,"Enquanto não encerrada a instância administrativa, não incidirá cobrança moratória nem restrição, inclusive para fins de licenciamento e",["transferência.","pintura.","reboque.","emplacamento do vizinho.","lavagem."],"Art. 284, § 3º.")
q(2,"O recurso intempestivo ou interposto por parte ilegítima",["não terá efeito suspensivo.","terá efeito suspensivo.","será julgado por unanimidade.","será pago em dobro.","será convertido em defesa."],"Art. 285, § 1º.")
q(2,"O recurso à JARI deve ser julgado no prazo de",["24 meses, contado do recebimento do recurso pelo órgão julgador.","6 meses.","12 meses.","36 meses.","60 meses."],"Art. 285, § 6º.")
q(2,"Se o infrator recolher o valor da multa e apresentar recurso, e o recurso for provido, será devolvida a importância paga, atualizada por",["índice legal de correção.","metade do valor.","nada.","apenas 50%.","apenas o principal."],"Art. 286, § 2º.")
q(2,"Se a infração for cometida em localidade diversa da do licenciamento, o recurso poderá ser apresentado ao órgão de trânsito da residência ou",["domicílio do infrator.","local do trabalho.","família.","banco.","cartório."],"Art. 287.")
q(2,"O não julgamento dos recursos nos prazos legais ensejará a",["prescrição da pretensão punitiva.","decadência do imposto.","prisão.","anistia automática.","perempção."],"Art. 289-A.")
q(2,"Implica encerramento da instância administrativa a não interposição do recurso no",["prazo legal.","bairro.","cartório.","consulado.","semestre."],"Art. 290, II.")
q(2,"Esgotados os recursos, as penalidades aplicadas serão cadastradas no",["RENACH.","RENAVAM.","SINESP.","Cadúnico.","CAGED."],"Art. 290, parágrafo único.")
q(2,"No texto da autuação da guarda municipal, a ausência de assinatura do condutor, que não foi localizado, é admitida porque a assinatura é exigida",["sempre que possível.","em todos os casos.","apenas para infração leve.","apenas para habilitados.","apenas em rodovias."],"Art. 280, VI.","ctb9a")
q(2,"No texto da notificação da penalidade, a notificação da autuação em 20 dias foi expedida dentro do prazo de",["30 dias.","10 dias.","15 dias.","5 dias.","60 dias."],"Art. 281, § 1º, II.","ctb9b")
q(2,"No texto do recurso à JARI, o condutor poderá recorrer ao Cetran no prazo de",["30 dias, da notificação da decisão.","5 dias.","10 dias.","15 dias.","60 dias."],"Art. 288.","ctb9c")
# n=3
q(3,"Assinale a alternativa correta sobre os prazos do processo administrativo.",["Defesa prévia: no mínimo 30 dias; notificação da penalidade: 180 dias, ou 360 com defesa; recurso: no mínimo 30 dias.","Defesa prévia: 5 dias.","Notificação da penalidade: 30 dias.","Recurso: 10 dias.","Notificação da autuação: 180 dias."],"Arts. 281-A e 282.")
q(3,"Considere. I. O auto de infração será arquivado se a notificação da autuação não sair em 30 dias. II. O recurso intempestivo tem efeito suspensivo. III. A defesa prévia tem prazo mínimo de 30 dias. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O recurso intempestivo não tem efeito suspensivo (art. 285, § 1º).")
q(3,"Assinale a INCORRETA.",["O pagamento da multa implica renúncia ao questionamento administrativo.","O recurso pode ser interposto sem o recolhimento da multa.","A multa pode ser paga por 80% até o vencimento.","A multa paga com desconto de 60% depende da opção pelo sistema eletrônico.","A notificação devolvida por endereço desatualizado é válida."],"O pagamento não implica renúncia (art. 284, § 2º).")
q(3,"Após encerrada a instância administrativa, a multa não paga até o vencimento será acrescida de juros de mora equivalentes à taxa Selic e de",["1% relativamente ao mês em que o pagamento estiver sendo efetuado.","10% ao mês.","5% ao ano.","50% do valor.","dobro do valor."],"Art. 284, § 4º.")
q(3,"A notificação no sistema eletrônico exige que o proprietário e o condutor autuado mantenham seu cadastro atualizado no órgão executivo de trânsito",["do Estado ou do Distrito Federal.","do Município, apenas.","da União, apenas.","do consulado.","do cartório."],"Art. 282-A, § 1º.")
q(3,"A coordenação do sistema de notificação eletrônica é de responsabilidade do",["órgão máximo executivo de trânsito da União.","Município.","Estado.","Cetran.","Jari."],"Art. 282-A, § 4º.")
q(3,"Na apresentação de defesa ou recurso, para efeitos de admissibilidade, não serão exigidos documentos emitidos pelo",["órgão responsável pela autuação.","infrator.","tabelião.","juiz.","banco."],"Art. 285, § 4º.")
q(3,"No caso de pessoal de missões diplomáticas, a notificação é remetida ao",["Ministério das Relações Exteriores.","Ministério da Justiça.","Município.","Estado.","Cetran."],"Art. 282, § 2º.")
q(3,"O recurso das decisões da JARI, quando se tratar de penalidade da União, é julgado por colegiado especial integrado, entre outros, pelo",["Coordenador-Geral da Jari.","Prefeito.","Governador.","Presidente do Cetran.","delegado."],"Art. 289, I.")
q(3,"Da decisão de provimento da JARI, o recurso será interposto pela",["autoridade que impôs a penalidade.","vítima.","testemunha.","imprensa.","seguradora."],"Art. 288, § 1º.")
q(3,"Da decisão de não provimento da JARI, o recurso será interposto pelo",["responsável pela infração.","juiz.","Detran.","Município.","Cetran."],"Art. 288, § 1º.")
q(3,"Implica encerramento da instância administrativa o pagamento da multa com reconhecimento da infração e requerimento de encerramento, sem apresentação de",["defesa ou recurso.","documentos.","testemunhas.","fotos.","comprovantes."],"Art. 290, III.")
q(3,"Os prazos processuais de que trata o Código não se suspendem, salvo por motivo de",["força maior devidamente comprovado.","férias.","feriado.","vontade do infrator.","greve."],"Art. 290-A.")
q(3,"No caso de infração cometida em localidade diversa, a autoridade que receber o recurso o remeterá de pronto à autoridade que impôs a penalidade, acompanhado das cópias dos",["prontuários necessários ao julgamento.","contratos.","laudos médicos.","recibos.","cartas."],"Art. 287, parágrafo único.")
q(3,"A notificação a pessoa jurídica proprietária, após prazo sem identificação do infrator, resulta em multa de valor igual a duas vezes a originária, conforme o art. 257, § 8º, e é lavrada com direito de",["defesa prévia e recursos.","isenção.","anistia.","redução automática.","nenhum recurso."],"Art. 257, § 8º.")
q(3,"No texto da autuação da guarda municipal, se a notificação da autuação não for expedida em 30 dias, o auto será",["arquivado, com registro julgado insubsistente.","mantido por 1 ano.","convertido em advertência.","julgado procedente.","enviado ao juiz."],"Art. 281, § 1º, II.","ctb9a")
q(3,"No texto da notificação da penalidade, a defesa prévia indeferida leva à aplicação da penalidade e à",["expedição de notificação, ao proprietário ou ao infrator.","extinção do processo.","prisão.","prescrição imediata.","anistia."],"Art. 282.","ctb9b")
q(3,"No texto da notificação da penalidade, o prazo para expedir a notificação da penalidade, havendo defesa prévia, é de",["360 dias.","180 dias.","30 dias.","90 dias.","720 dias."],"Art. 282, § 6º.","ctb9b")
q(3,"No texto do recurso à JARI, a autoridade remeteu o recurso à Jari dentro do prazo de",["dez dias.","cinco dias.","trinta dias.","sessenta dias.","um ano."],"Art. 285, § 2º.","ctb9c")
q(3,"No texto do recurso à JARI, se o recurso ao Cetran não for julgado em 24 meses, ocorre",["a prescrição da pretensão punitiva.","a aplicação da multa em dobro.","a prisão.","a decadência do recurso.","a conversão em advertência."],"Art. 289-A.","ctb9c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Processo administrativo de trânsito",[
 ("aut","Autuação",["auto de infração","quem lava: servidor ou PM designado","comprovação"],"seção 1"),
 ("not","Notificação da autuação",["30 dias, senão arquivamento","defesa prévia: mínimo 30 dias","consistência"],"seção 2"),
 ("pen","Penalidade",["notificação: 180 ou 360 dias","decadência","recurso: mínimo 30 dias"],"seção 2"),
 ("pag","Pagamento",["80% até o vencimento","60% sem defesa nem recurso","sem renúncia ao recurso"],"seção 3"),
 ("jar","JARI",["remessa em 10 dias","24 meses","efeito suspensivo"],"seção 3"),
 ("cet","Cetran",["recurso em 30 dias","24 meses","prescrição"],"seção 4")],
 "Na prova: prazo e quem decide; lembre dos 30, 180, 360 e 24")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7],QR,4,svg,"A primeira linha traz a autuação e a notificação; as demais, penalidade, pagamento, recursos e encerramento.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 280 a 290, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-9","Processo administrativo (CTB, arts. 280 a 290-A)",Q,list(tx),
 cobertura=["Cobertos: arts. 280 a 290 (com 281-A, 282-A e 289-A). Não detalhados: art. 282, §§ 5º e 6º-A, art. 284, §§ 5º e 6º, art. 289, parágrafo único, art. 290-A."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","No texto da aula, a explicação do desconto de 60% (art. 284, § 1º) deve ser relida com a redação mais recente da Lei 14.599/2023.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb9a, ctb9b e ctb9c fictícios."],
 fontes_conferidas=["CTB, arts. 280 a 290: texto da Câmara, copiado por programa."])
gravar("ctb-9",aula_html,banco("ctb-9",Q),tx)
