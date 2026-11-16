import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='idoso.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Estatuto da Pessoa Idosa (Lei 10.741/2003) regula os direitos de quem tem 60 anos ou mais. Os arts. 8º a 42 são os direitos fundamentais: vida, liberdade, respeito, dignidade, alimentos, saúde, educação, trabalho, previdência, assistência, habitação e transporte. A Vunesp cobra principalmente os números: os 65 anos da gratuidade no transporte e do benefício assistencial, os 10% dos assentos, os 5% das vagas de estacionamento, os 3% das unidades habitacionais, os 50% de desconto em ingressos, a preferência especial dos maiores de 80 anos e os 70% do limite de participação em entidade de longa permanência."
S={}
S[1]="## 1. Envelhecimento, liberdade, respeito, dignidade e alimentos\n\n"+L("arts. 8º e 9º","Art. 8º O envelhecimento","CAPÍTULO II")+"\n\n"+L("art. 10","Art. 10. É obrigação do Estado e da sociedade","CAPÍTULO III")+"\n\n"+L("arts. 11 a 14","Art. 11. Os alimentos serão prestados","CAPÍTULO IV")+"""

O envelhecimento é um direito personalíssimo e sua proteção, um direito social. É obrigação do Estado garantir a proteção à vida e à saúde, mediante políticas públicas que permitam um envelhecimento saudável e digno. É obrigação do Estado e da sociedade assegurar a liberdade, o respeito e a dignidade. A liberdade tem sete aspectos (ir, vir e estar; opinião e expressão; crença e culto; esportes e diversões; vida familiar e comunitária; vida política; refúgio, auxílio e orientação); o respeito é a inviolabilidade física, psíquica e moral, com imagem, identidade e autonomia; e é dever de todos zelar pela dignidade, colocando a pessoa idosa a salvo de tratamento desumano, violento, aterrorizante, vexatório ou constrangedor.

A obrigação alimentar é solidária, e a pessoa idosa pode optar entre os prestadores. As transações sobre alimentos podem ser feitas perante o Promotor de Justiça ou o Defensor Público, e têm efeito de título executivo extrajudicial. Se a pessoa idosa ou seus familiares não tiverem condições, o poder público provê o sustento, no âmbito da assistência social.
"""
S[2]="## 2. Saúde\n\n"+L("art. 15, caput","Art. 15. É assegurada a atenção integral","§ 1º A prevenção")+"\n\n"+L("art. 15, §§ 2º a 4º","§ 2º Incumbe ao poder público","§ 5º É vedado exigir")+"\n\n"+L("art. 15, §§ 5º a 7º","§ 5º É vedado exigir","Art. 16.")+"\n\n"+L("arts. 16 e 17","Art. 16. À pessoa idosa internada","Art. 18.")+"\n\n"+L("art. 19","Art. 19. Os casos de suspeita","§ 2º Aplica-se")+"""

A atenção integral à saúde é assegurada pelo SUS, com acesso universal e igualitário. O poder público fornece gratuitamente medicamentos, especialmente os de uso continuado, próteses e órteses. É vedada a discriminação nos planos de saúde pela cobrança de valores diferenciados em razão da idade. É vedado exigir o comparecimento da pessoa idosa enferma perante órgãos públicos: o agente vai à residência, ou a pessoa se faz representar por procurador. Em todo atendimento de saúde, os maiores de 80 anos têm preferência especial sobre as demais pessoas idosas, exceto em emergência.

A pessoa idosa internada ou em observação tem direito a acompanhante em tempo integral, segundo o critério médico. A pessoa que esteja no domínio de suas faculdades mentais pode optar pelo tratamento que julgar mais favorável. Os casos de suspeita ou confirmação de violência contra pessoas idosas são de notificação compulsória pelos serviços de saúde à autoridade sanitária e de comunicação obrigatória à autoridade policial, ao Ministério Público e aos Conselhos Municipal, Estadual e Nacional da Pessoa Idosa. Violência é qualquer ação ou omissão, em local público ou privado, que cause morte, dano ou sofrimento físico ou psicológico.
"""
S[3]="## 3. Educação, trabalho, previdência e assistência\n\n"+L("art. 20","Art. 20. A pessoa idosa tem direito","Art. 21.")+"\n\n"+L("art. 23","Art. 23. A participação das pessoas idosas","Art. 24.")+"\n\n"+L("arts. 26 e 27","Art. 26. A pessoa idosa tem direito ao exercício","Art. 28.")+"\n\n"+L("art. 34","Art. 34. Às pessoas idosas, a partir de 65","Art. 35.")+"\n\n"+L("arts. 35 e 36","Art. 35. Todas as entidades de longa permanência","CAPÍTULO IX")+"""

A participação em atividades culturais e de lazer é proporcionada mediante descontos de pelo menos 50% nos ingressos para eventos artísticos, culturais, esportivos e de lazer, com acesso preferencial aos locais. A pessoa idosa tem direito ao exercício de atividade profissional, respeitadas suas condições; na admissão em qualquer trabalho são vedadas a discriminação e a fixação de limite máximo de idade, inclusive em concursos, ressalvada a natureza do cargo. O primeiro critério de desempate em concurso público é a idade, com preferência ao mais idoso.

A partir de 65 anos, a pessoa idosa sem meios de prover a subsistência, nem de tê-la provida pela família, tem direito ao benefício mensal de um salário mínimo, nos termos da Loas. Todas as entidades de longa permanência são obrigadas a firmar contrato de prestação de serviços com a pessoa idosa abrigada; nas filantrópicas, a participação no custeio não pode exceder 70% de qualquer benefício previdenciário ou assistencial recebido.
"""
S[4]="## 4. Habitação e transporte\n\n"+L("art. 37","Art. 37. A pessoa idosa tem direito a moradia digna","Art. 38.")+"\n\n"+L("art. 38","Art. 38. Nos programas habitacionais","CAPÍTULO X")+"\n\n"+L("art. 39","Art. 39. Aos maiores de 65","Art. 40.")+"\n\n"+L("arts. 40 a 42","Art. 40. No sistema de transporte coletivo interestadual","TÍTULO III")+"""

A pessoa idosa tem direito a moradia digna, no seio da família natural ou substituta, desacompanhada se assim o desejar, ou em instituição pública ou privada. Toda instituição de atendimento deve manter identificação externa visível, sob pena de interdição. Nos programas habitacionais públicos ou subsidiados, a pessoa idosa tem prioridade e há reserva de pelo menos 3% das unidades, preferencialmente no pavimento térreo.

Aos maiores de 65 anos é assegurada a gratuidade dos transportes coletivos públicos urbanos e semiurbanos, exceto nos serviços seletivos e especiais; basta qualquer documento pessoal que prove a idade. São reservados 10% dos assentos, identificados com placa. Entre 60 e 65 anos, a legislação local dispõe sobre a gratuidade. No transporte interestadual são duas vagas gratuitas por veículo para pessoas com renda até dois salários mínimos e desconto de 50%, no mínimo, para as que excederem as vagas. Reserva-se 5% das vagas nos estacionamentos públicos e privados, e são asseguradas a prioridade e a segurança no embarque e desembarque.
"""
S[5]="""## 6. Na rotina do guarda

- **Vagas de estacionamento:** 5% das vagas, posicionadas para melhor comodidade; o guarda fiscaliza o uso indevido nos termos da legislação.
- **Transporte coletivo:** gratuidade a partir de 65 anos com qualquer documento que prove a idade; 10% dos assentos reservados.
- **Violência contra a pessoa idosa:** a ocorrência é comunicada à autoridade policial e ao Ministério Público, e o guarda registra a ação ou a omissão.
- **Prioridade:** os maiores de 80 anos têm preferência especial no atendimento de saúde, exceto em emergência.
- **Dignidade:** é dever de todos pôr a pessoa idosa a salvo de tratamento vexatório ou constrangedor.
"""
S[6]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Gratuidade no transporte coletivo | Maiores de 65 anos; entre 60 e 65 a lei local dispõe |
| Benefício assistencial | A partir de 65 anos, um salário mínimo |
| Assentos reservados | 10% |
| Vagas de estacionamento | 5% |
| Unidades habitacionais | 3%, preferencialmente no térreo |
| Desconto em ingressos | Pelo menos 50% |
| Preferência especial | Maiores de 80 anos |
| Limite do custeio em entidade filantrópica | 70% do benefício |
| Transporte interestadual | Duas vagas gratuitas; desconto de 50%; renda até 2 salários mínimos |
| Idade no concurso público | Não há limite máximo; desempate pela maior idade |
"""
S[7]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Arts. 8º e 9º | Envelhecimento: direito personalíssimo; Estado protege vida e saúde |
| Art. 10 | Liberdade, respeito e dignidade |
| Art. 12 | Obrigação alimentar solidária |
| Art. 15 | SUS; medicamentos gratuitos; preferência aos maiores de 80 |
| Art. 16 | Acompanhante em tempo integral |
| Art. 19 | Notificação compulsória de violência |
| Art. 23 | Desconto de 50% em ingressos |
| Art. 27 | Sem limite máximo de idade; desempate pela idade |
| Art. 34 | 65 anos; um salário mínimo |
| Art. 38 | 3% das unidades |
| Art. 39 | 65 anos; 10% dos assentos |
| Art. 41 | 5% das vagas |
"""
QR=[("Questão 1","Aos maiores de 65 anos fica assegurada a gratuidade dos transportes coletivos públicos",["urbanos e semiurbanos, exceto nos serviços seletivos e especiais.","apenas urbanos.","apenas interestaduais.","apenas rodoviários.","apenas ferroviários."],0,"Art. 39."),
("Questão 2","Nos veículos de transporte coletivo, serão reservados às pessoas idosas, devidamente identificados, assentos na proporção de",["dez por cento.","cinco por cento.","vinte por cento.","trinta por cento.","três por cento."],1,"Art. 39, § 2º."),
("Questão 3","É assegurada a reserva para as pessoas idosas, nos termos da lei local, de cinco por cento das vagas nos estacionamentos",["públicos e privados.","públicos apenas.","privados apenas.","de shoppings apenas.","de hospitais apenas."],2,"Art. 41."),
("Questão 4","Em todo atendimento de saúde, os maiores de oitenta anos terão preferência especial sobre as demais pessoas idosas, exceto em caso de",["emergência.","consulta.","exame.","vacinação.","retorno."],3,"Art. 15, § 7º.")]
t1="<strong>Ônibus urbano</strong><br><br>Uma senhora de 66 anos entrou num ônibus urbano de Vila Nova, cidade fictícia, e mostrou o RG ao cobrador para ter a gratuidade. O cobrador exigiu um cartão especial."
t2="<strong>Estacionamento do mercado</strong><br><br>O mercado municipal de Vila Nova tem cem vagas e reservou três para pessoas idosas, deixando-as longe da entrada. Um idoso de 72 anos reclamou à guarda."
t3="<strong>Violência no asilo</strong><br><br>Uma auxiliar de enfermagem de uma instituição de Vila Nova percebeu que um residente de 85 anos tinha hematomas e relatava que era empurrado pelo cuidador."
tx={"idoso1a":t1,"idoso1b":t2,"idoso1c":t3}
# n=1
q(1,"O envelhecimento é um direito personalíssimo e a sua proteção um direito",["social.","empresarial.","político.","penal.","tributário."],"Art. 8º.")
q(1,"É obrigação do Estado garantir à pessoa idosa a proteção à vida e à",["saúde.","propriedade.","renda.","carreira.","moradia."],"Art. 9º.")
q(1,"O direito à liberdade da pessoa idosa compreende a faculdade de ir, vir e estar nos logradouros públicos e espaços comunitários, ressalvadas as",["restrições legais.","ordens da família.","regras do bairro.","vontades do síndico.","decisões do juiz."],"Art. 10, § 1º, I.")
q(1,"É dever de todos zelar pela dignidade da pessoa idosa, colocando-a a salvo de qualquer tratamento desumano, violento, aterrorizante, vexatório ou",["constrangedor.","educativo.","disciplinar.","amistoso.","cuidadoso."],"Art. 10, § 3º.")
q(1,"A obrigação alimentar à pessoa idosa é",["solidária.","subsidiária.","única.","facultativa.","extinta."],"Art. 12.")
q(1,"As transações relativas a alimentos poderão ser celebradas perante o Promotor de Justiça ou o",["Defensor Público.","Delegado.","Prefeito.","Juiz de Paz.","Escrivão."],"Art. 13.")
q(1,"É assegurada à pessoa idosa a atenção integral à saúde por intermédio do",["Sistema Único de Saúde (SUS).","INSS.","Ministério Público.","Conselho Tutelar.","Detran."],"Art. 15.")
q(1,"Incumbe ao poder público fornecer às pessoas idosas, gratuitamente, medicamentos, especialmente os de uso",["continuado.","eventual.","raro.","comum.","estético."],"Art. 15, § 2º.")
q(1,"É vedada a discriminação da pessoa idosa nos planos de saúde pela cobrança de valores diferenciados em razão da",["idade.","renda.","moradia.","profissão.","origem."],"Art. 15, § 3º.")
q(1,"À pessoa idosa internada ou em observação é assegurado o direito a",["acompanhante.","indenização.","transferência.","advogado.","visita de imprensa."],"Art. 16.")
q(1,"Os casos de suspeita ou confirmação de violência contra pessoas idosas são objeto de notificação",["compulsória pelos serviços de saúde.","facultativa.","eventual.","verbal.","anônima apenas."],"Art. 19.")
q(1,"A pessoa idosa tem direito a descontos de pelo menos 50% nos ingressos para eventos artísticos, culturais, esportivos e de",["lazer.","comércio.","política.","indústria.","pesca."],"Art. 23.")
q(1,"Na admissão da pessoa idosa em qualquer trabalho são vedadas a discriminação e a fixação de limite máximo de",["idade.","altura.","peso.","salário.","distância."],"Art. 27.")
q(1,"O primeiro critério de desempate em concurso público será a",["idade, com preferência ao de idade mais elevada.","nota em português.","altura.","sorteio.","ordem de inscrição."],"Art. 27, parágrafo único.")
q(1,"A partir de 65 anos, a pessoa idosa sem meios de prover a subsistência tem direito ao benefício mensal de",["um salário mínimo.","dois salários mínimos.","meio salário mínimo.","três salários mínimos.","cinco salários mínimos."],"Art. 34.")
q(1,"Nos programas habitacionais públicos, há reserva de pelo menos três por cento das unidades para as pessoas",["idosas.","jovens.","trabalhadoras rurais.","com deficiência, apenas.","militares."],"Art. 38, I.")
q(1,"As unidades residenciais reservadas a pessoas idosas devem situar-se, preferencialmente, no pavimento",["térreo.","superior.","intermediário.","subsolo.","cobertura."],"Art. 38, parágrafo único.")
q(1,"No texto do ônibus urbano, a gratuidade aos 66 anos pode ser comprovada com",["qualquer documento pessoal que faça prova da idade.","apenas cartão especial.","apenas CNH.","apenas CPF.","apenas título de eleitor."],"Art. 39, § 1º.","idoso1a")
q(1,"No texto do estacionamento do mercado, a reserva legal de vagas para pessoas idosas é de",["cinco por cento.","três por cento.","dez por cento.","dois por cento.","vinte por cento."],"Art. 41.","idoso1b")
q(1,"No texto da violência no asilo, a notificação da suspeita de violência pelos serviços de saúde é",["compulsória.","facultativa.","sigilosa.","eventual.","vedada."],"Art. 19.","idoso1c")
# n=2
q(2,"A liberdade da pessoa idosa compreende a participação na vida política, na forma da",["lei.","tradição.","família.","comunidade.","vontade."],"Art. 10, § 1º, VI.")
q(2,"O direito ao respeito consiste na inviolabilidade da integridade física, psíquica e",["moral.","financeira.","jurídica.","comercial.","política."],"Art. 10, § 2º.")
q(2,"A pessoa idosa pode optar entre os prestadores da obrigação",["alimentar.","tributária.","trabalhista.","penal.","eleitoral."],"Art. 12.")
q(2,"Se a pessoa idosa ou seus familiares não possuírem condições de prover o seu sustento, impõe-se esse provimento ao",["poder público, no âmbito da assistência social.","comércio.","vizinho.","empregador.","banco."],"Art. 14.")
q(2,"É vedado exigir o comparecimento da pessoa idosa enferma perante os órgãos públicos; no interesse do poder público, o agente promoverá o contato em sua",["residência.","sede do órgão.","clínica.","escola.","igreja."],"Art. 15, § 5º, I.")
q(2,"A pessoa idosa enferma tem atendimento domiciliar pela perícia médica do",["INSS.","Detran.","Poder Judiciário.","Conselho Tutelar.","Ministério Público."],"Art. 15, § 6º.")
q(2,"À pessoa idosa no domínio de suas faculdades mentais é assegurado o direito de optar pelo tratamento de saúde que lhe for reputado mais",["favorável.","barato.","rápido.","comum.","moderno."],"Art. 17.")
q(2,"Não estando a pessoa idosa em condições de optar pelo tratamento, a opção será feita pelo curador, quando ela for",["interditada.","jovem.","estrangeira.","residente.","comerciante."],"Art. 17, parágrafo único, I.")
q(2,"Os casos de violência são comunicados, entre outros órgãos, à autoridade policial, ao Ministério Público e ao",["Conselho Municipal da Pessoa Idosa.","Detran.","Corpo de Bombeiros.","Banco Central.","Sindicato."],"Art. 19.")
q(2,"Considera-se violência contra a pessoa idosa qualquer ação ou omissão praticada em local público ou privado que lhe cause morte, dano ou sofrimento físico ou",["psicológico.","financeiro.","social.","moral, apenas.","político."],"Art. 19, § 1º.")
q(2,"A pessoa idosa tem direito a educação, cultura, esporte, lazer, diversões, espetáculos, produtos e serviços que respeitem sua peculiar condição de",["idade.","renda.","moradia.","profissão.","origem."],"Art. 20.")
q(2,"O Poder Público criará programas de preparação dos trabalhadores para a aposentadoria, com antecedência mínima de",["um ano.","seis meses.","dois anos.","três meses.","cinco anos."],"Art. 28, II.")
q(2,"Todas as entidades de longa permanência são obrigadas a firmar contrato de prestação de serviços com a pessoa idosa",["abrigada.","visitante.","funcionária.","vizinha.","parente."],"Art. 35.")
q(2,"A participação no custeio da entidade filantrópica não pode exceder a seguinte parte de qualquer benefício da pessoa idosa:",["setenta por cento.","cinquenta por cento.","trinta por cento.","noventa por cento.","cem por cento."],"Art. 35, § 2º.")
q(2,"Toda instituição de atendimento à pessoa idosa deve manter identificação externa visível, sob pena de",["interdição.","fechamento imediato.","multa de trânsito.","demissão.","advertência apenas."],"Art. 37, § 2º.")
q(2,"A gratuidade nos transportes coletivos não alcança os serviços seletivos e especiais, quando prestados paralelamente aos serviços",["regulares.","noturnos.","escolares.","turísticos.","de carga."],"Art. 39.")
q(2,"No transporte interestadual, são reservadas duas vagas gratuitas por veículo para pessoas idosas com renda igual ou inferior a",["dois salários mínimos.","um salário mínimo.","três salários mínimos.","cinco salários mínimos.","meio salário mínimo."],"Art. 40, I.")
q(2,"No texto do ônibus urbano, a exigência de cartão especial aos 66 anos contraria o art. 39, § 1º, que basta qualquer documento pessoal que faça prova da",["idade.","renda.","residência.","profissão.","origem."],"Art. 39, § 1º.","idoso1a")
q(2,"No texto do estacionamento do mercado, a reserva de 3 vagas em 100 é",["inferior a cinco por cento exigidos.","superior ao exigido.","exatamente a exigida.","irrelevante.","desnecessária."],"Art. 41.","idoso1b")
q(2,"No texto da violência no asilo, o caso deve ser comunicado, entre outros, à",["autoridade policial e ao Ministério Público.","imprensa.","Câmara.","escola.","empresa."],"Art. 19.","idoso1c")
# n=3
q(3,"Assinale a alternativa correta sobre os números do Estatuto.",["Gratuidade no transporte: 65 anos; assentos reservados: 10%; vagas de estacionamento: 5%.","Gratuidade: 60 anos; assentos: 5%; vagas: 10%.","Gratuidade: 70 anos; assentos: 20%; vagas: 3%.","Gratuidade: 65 anos; assentos: 5%; vagas: 20%.","Gratuidade: 60 anos; assentos: 10%; vagas: 2%."],"Arts. 39, 41.")
q(3,"Considere. I. Os maiores de 80 anos têm preferência especial no atendimento de saúde. II. A gratuidade no transporte vale a partir dos 60 anos em todos os casos. III. A idade é o primeiro critério de desempate em concurso. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A gratuidade é a partir de 65 anos; de 60 a 65, a lei local (art. 39, § 3º).")
q(3,"Assinale a INCORRETA.",["O limite máximo de idade em concurso é sempre vedado, sem exceção.","A obrigação alimentar é solidária.","O desconto em ingressos é de pelo menos 50%.","O benefício assistencial é de um salário mínimo a partir de 65 anos.","A reserva de 3% das unidades habitacionais é para pessoas idosas."],"O limite é vedado, ressalvados os casos em que a natureza do cargo o exigir (art. 27).")
q(3,"Para a gratuidade nos transportes, na faixa de 60 a 65 anos, a legislação local dispõe sobre as",["condições para o exercício da gratuidade.","datas de aniversário.","tarifas máximas.","linhas de ônibus.","empresas."],"Art. 39, § 3º.")
q(3,"O benefício já concedido a qualquer membro da família nos termos do art. 34 não será computado para o cálculo da",["renda familiar per capita a que se refere a Loas.","pensão alimentícia.","herança.","aposentadoria.","contribuição."],"Art. 34, parágrafo único.")
q(3,"O acolhimento de pessoas idosas em situação de risco social, por adulto ou núcleo familiar, caracteriza",["a dependência econômica, para os efeitos legais.","a adoção.","a guarda.","a tutela.","a curatela."],"Art. 36.")
q(3,"A assistência integral na modalidade de entidade de longa permanência é prestada quando verificada a inexistência de grupo familiar, casa-lar, abandono ou",["carência de recursos financeiros próprios ou da família.","desejo de viajar.","aposentadoria.","doença leve.","mudança de cidade."],"Art. 37, § 1º.")
q(3,"Nos programas habitacionais, a pessoa idosa goza de prioridade na aquisição de imóvel, com implantação de equipamentos urbanos comunitários e eliminação de",["barreiras arquitetônicas e urbanísticas.","taxas.","juros.","impostos.","prazos."],"Art. 38, III.")
q(3,"A pessoa idosa tem direito a moradia digna, inclusive desacompanhada de seus familiares, quando",["assim o desejar.","o juiz determinar.","o filho autorizar.","o Estado impuser.","a entidade permitir."],"Art. 37.")
q(3,"No sistema interestadual, o desconto de 50%, no mínimo, aplica-se às pessoas idosas que excederem as vagas gratuitas e tiverem renda de até",["dois salários mínimos.","um salário mínimo.","três salários mínimos.","cinco salários mínimos.","dez salários mínimos."],"Art. 40, II.")
q(3,"As instituições de saúde devem promover o treinamento e a capacitação dos profissionais e orientação a cuidadores familiares e grupos de",["autoajuda.","vendas.","esporte.","política.","caridade."],"Art. 18.")
q(3,"Na proporção do art. 39, os assentos reservados devem estar identificados com placa de",["reservado preferencialmente para pessoas idosas.","uso exclusivo.","atenção.","proibido sentar.","gratuito."],"Art. 39, § 2º.")
q(3,"O Dia Mundial do Trabalho, 1º de maio, é, segundo o Estatuto, a database dos",["aposentados e pensionistas.","comerciantes.","estudantes.","servidores.","empresários."],"Art. 32.")
q(3,"A perda da condição de segurado não será considerada para a concessão da aposentadoria por idade, desde que haja, no mínimo, o tempo de contribuição correspondente à",["carência na data do requerimento do benefício.","idade de 80 anos.","renda mínima.","residência.","filiação sindical."],"Art. 30.")
q(3,"No texto do ônibus urbano, a gratuidade da passageira de 66 anos decorre do art. 39, que a assegura aos maiores de",["65 anos.","60 anos.","70 anos.","75 anos.","80 anos."],"Art. 39.","idoso1a")
q(3,"No texto do ônibus urbano, a cobrança de cartão especial, em vez de qualquer documento, pode ser considerada, em tese,",["descumprimento do art. 39, § 1º.","cumprimento regular.","isenção.","faculdade do cobrador.","exigência da guarda."],"Art. 39, § 1º.","idoso1a")
q(3,"No texto do estacionamento do mercado, a lei exige reserva de 5% das vagas, e o posicionamento deve garantir a melhor",["comodidade à pessoa idosa.","visibilidade do mercado.","renda.","distância.","segurança do veículo."],"Art. 41.","idoso1b")
q(3,"No texto do estacionamento do mercado, 5% de 100 vagas são",["cinco vagas.","três vagas.","dez vagas.","vinte vagas.","uma vaga."],"Art. 41.","idoso1b")
q(3,"No texto da violência no asilo, a ação do cuidador de empurrar o residente configura violência, que é qualquer ação ou omissão que cause dano ou sofrimento",["físico ou psicológico.","apenas financeiro.","apenas moral.","apenas social.","apenas político."],"Art. 19, § 1º.","idoso1c")
q(3,"No texto da violência no asilo, além da autoridade policial, a comunicação obrigatória deve ser feita ao",["Ministério Público.","Detran.","Banco.","Sindicato.","Clube."],"Art. 19, II.","idoso1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Estatuto da Pessoa Idosa: direitos fundamentais (arts. 8º a 42)",[
 ("vid","Vida, liberdade, dignidade",["direito personalíssimo","7 aspectos da liberdade","dever de todos zelar"],"seção 1"),
 ("ali","Alimentos",["obrigação solidária","transação: MP ou Defensoria","poder público provê"],"seção 1"),
 ("sau","Saúde",["SUS","maiores de 80: preferência","violência: notificação"],"seção 2"),
 ("edu","Educação e trabalho",["50% em ingressos","sem limite de idade","desempate pela idade"],"seção 3"),
 ("ass","Assistência",["65 anos: 1 salário mínimo","contrato nas entidades","70% do benefício"],"seção 3"),
 ("tra","Habitação e transporte",["3% das unidades","65 anos: gratuidade","10% assentos; 5% vagas"],"seção 4")],
 "Na prova: os números (65, 10%, 5%, 3%, 50%, 70%, 80 anos)")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',5,6,7],QR,5,svg,"A primeira linha traz vida, dignidade e alimentos; as demais, saúde, trabalho, assistência, habitação e transporte.","Fontes: Edital 02/2026, Anexo I; Lei 10.741/2003 (Estatuto da Pessoa Idosa), arts. 8º a 42, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("idoso-1","Estatuto da Pessoa Idosa: direitos fundamentais (arts. 8º a 42)",Q,list(tx),
 cobertura=["Cobertos: arts. 8º a 20, 23, 26, 27, 30, 32, 34 a 42. Não detalhados: arts. 21, 22, 24, 25, 28, 29, 31, 33 e incisos do art. 15, § 1º."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","As questões numéricas devem ser reconferidas no Planalto, pois os percentuais podem ser alterados por lei.","Trechos de lei copiados de fontes/idoso.txt por programa.","Casos idoso1a, idoso1b e idoso1c fictícios."],
 fontes_conferidas=["Estatuto da Pessoa Idosa, arts. 8º a 42: texto da Câmara, copiado por programa."])
gravar("idoso-1",aula_html,banco("idoso-1",Q),tx)
