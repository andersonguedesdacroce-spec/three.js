import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='lm_lei.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Estatuto dos Funcionários Públicos do Município de Campinas (Lei 1.399/1955) é o texto que o edital pede em dois recortes: o art. 15 (estágio probatório) e os arts. 184 a 204 (deveres, proibições, responsabilidade, penalidades e prescrição). A Vunesp cobra a letra da lei: a lista de deveres e de proibições, as seis penas disciplinares, os casos de demissão, o prazo de 30 dias para o abandono de cargo e os prazos de prescrição. Atenção: o art. 15 do Estatuto fala em estágio de um ano, mas o Decreto 21.019/2020, com base no art. 41 da Constituição, fixa três anos; a aula do posto seguinte trata do decreto."
S={}
S[1]="## 1. Estágio probatório (art. 15)\n\n"+L("art. 15, caput e § 1º","Art. 15.","§ 2º Os Diretores")+"\n\n"+L("art. 15, §§ 3º a 6º","§ 3º O órgão do Pessoal","§ 7º A apuração")+"\n\n"+L("art. 15, §§ 7º e 8º","§ 7º A apuração","Seção II")+"""

O estágio probatório, nos termos do art. 15 do Estatuto, é o período de um ano de efetivo exercício do funcionário nomeado em virtude de concurso (hoje, três anos, pelo art. 41 da Constituição e pelo Decreto 21.019/2020). No estágio, apuram-se idoneidade moral, assiduidade, disciplina e eficiência. Trinta dias antes de terminado o prazo, o órgão de pessoal informa ao Prefeito sobre a conveniência de confirmar a nomeação; da informação contrária, dá-se vista ao estagiário por cinco dias. Se o Prefeito julgar aconselhável a exoneração, determina a lavratura do decreto; se for favorável à permanência, a confirmação não depende de novo ato. A conclusão do estágio importa na efetivação automática.
"""
S[2]="## 2. Deveres e proibições (arts. 184 e 185)\n\n"+L("art. 184","Art. 184.","CAPÍTULO III")+"\n\n"+L("art. 185","Art.185.","CAPÍTULO IV")+"""

São deveres do funcionário: assiduidade; pontualidade; discrição; urbanidade; lealdade às instituições constitucionais e administrativas; observância das normas legais e regulamentares; obediência às ordens superiores, exceto quando manifestamente ilegais; levar ao conhecimento da autoridade superior irregularidade de que tiver ciência em razão do cargo; zelar pela economia e conservação do material; manter em ordem o assentamento individual; e atender prontamente às requisições para defesa da Fazenda Pública e à expedição de certidões.

É proibido ao funcionário, entre outras condutas: referir-se de modo depreciativo, em informação, parecer ou despacho, às autoridades e atos da administração; retirar documento ou objeto da repartição sem autorização; promover manifestação de apreço ou desapreço ou circular lista de donativos no recinto; valer-se do cargo para proveito pessoal; coagir ou aliciar subordinados para fins partidários; participar da gerência ou administração de empresa industrial ou comercial (salvo licença para interesses particulares ou disponibilidade); praticar usura; pleitear como procurador ou intermediário junto às repartições municipais (salvo vantagens de parente até 2º grau); receber propinas, comissões e presentes em razão das atribuições; e cometer a pessoa estranha à repartição o desempenho de cargo que lhe competir.
"""
S[3]="## 3. Responsabilidade, penas, demissão e prescrição (arts. 186 a 204)\n\n"+L("arts. 186 a 190","Art. 186.","CAPÍTULO V")+"\n\n"+L("arts. 191 a 194","Art. 191.","Art. 195.")+"\n\n"+L("arts. 195 a 197","Art. 195.","Art. 198.")+"\n\n"+L("art. 198, caput","Art. 198.","§ 1º Considera-se abandono")+"\n\n"+L("art. 198, § 1º","§ 1º Considera-se abandono","§ 2º Será ainda")+"\n\n"+L("arts. 199 a 201","Art. 199.","Art. 202.")+"\n\n"+L("arts. 202 a 204","Art. 202.","CAPÍTULO VI")+"""

Pelo exercício irregular das atribuições, o funcionário responde civil, penal e administrativamente, e as cominações podem acumular-se, sendo independentes entre si. As penas disciplinares são seis: advertência, repreensão, multas, suspensão, demissão e cassação de aposentadoria e disponibilidade. A advertência é verbal, para casos leves de desobediência ou falta de cumprimento dos deveres, e consta somente do assentamento; a repreensão é por escrito; a suspensão não excede 90 dias, aplicada em falta grave ou reincidência, e pode ser convertida em multa de até 50% do vencimento por dia, permanecendo o funcionário em serviço.

A demissão é aplicada em nove hipóteses, entre elas crime contra a administração pública, abandono do cargo, incontinência pública e escandalosa, embriaguez habitual, insubordinação grave em serviço, ofensa física em serviço (salvo legítima defesa), aplicação irregular dos dinheiros públicos, lesão aos cofres públicos, corrupção passiva e transgressão de itens IV a X do art. 185. Considera-se abandono a ausência sem justa causa por mais de 30 dias consecutivos, e o edital de chamamento tem prazo de 20 dias. Competente para demissão, multa, cassação e suspensão por mais de 30 dias é o Prefeito; nos demais casos, o Diretor do Departamento e o Inspetor Fiscal. A prescrição é de 2 anos para a falta sujeita a repreensão, multa ou suspensão e de 4 anos para as sujeitas a demissão (no caso do § 2º do art. 198) e a cassação de aposentadoria e disponibilidade.
"""
S[5]="""## 5. Na rotina do guarda

- **Deveres do art. 184:** assiduidade, pontualidade, urbanidade e obediência às ordens superiores, exceto as manifestamente ilegais, orientam a rotina do guarda.
- **Irregularidade conhecida:** o guarda leva ao conhecimento da autoridade superior a irregularidade de que tiver ciência em razão do cargo.
- **Proibições do art. 185:** não se aceitam propinas, presentes ou vantagens em razão do cargo, nem se retira documento da repartição sem autorização.
- **Advertência e repreensão:** a advertência é verbal e a repreensão é escrita; a suspensão chega a 90 dias.
- **Abandono:** mais de 30 dias consecutivos de ausência sem justa causa autoriza a demissão.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Estágio probatório no Estatuto | Um ano (art. 15), mas hoje são três anos pela Constituição e pelo Decreto 21.019/2020 |
| Requisitos do estágio | Idoneidade moral, assiduidade, disciplina e eficiência |
| Informação do órgão de pessoal | 30 dias antes do fim do prazo |
| Vista ao estagiário | 5 dias |
| Obediência às ordens | Exceto as manifestamente ilegais |
| Penas disciplinares | Seis: advertência, repreensão, multas, suspensão, demissão, cassação |
| Advertência | Verbal |
| Repreensão | Por escrito |
| Suspensão | Até 90 dias; conversível em multa de até 50% do vencimento por dia |
| Abandono de cargo | Mais de 30 dias consecutivos; edital de 20 dias |
| Competência para demissão | Prefeito |
| Prescrição | 2 anos (repreensão, multa, suspensão); 4 anos (demissão do § 2º do art. 198 e cassação) |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 15 | Estágio: 1 ano no texto; requisitos; efetivação automática |
| Art. 184 | Deveres do funcionário |
| Art. 185 | Proibições |
| Art. 186 | Responsabilidade civil, penal e administrativa |
| Art. 190 | Cominações cumuláveis e independentes |
| Art. 191 | Seis penas disciplinares |
| Art. 194 | Advertência verbal |
| Art. 196 | Repreensão escrita |
| Art. 197 | Suspensão até 90 dias |
| Art. 198 | Demissão; abandono: mais de 30 dias |
| Art. 201 | Competência: Prefeito, Diretor de Departamento, Inspetor Fiscal |
| Art. 204 | Prescrição: 2 e 4 anos |
"""
QR=[("Questão 1","A pena de advertência será aplicada",["verbalmente, em casos de natureza leve, e constará somente do assentamento pessoal.","por escrito.","em audiência pública.","por publicação no Diário Oficial.","por decreto."],0,"Art. 194."),
("Questão 2","A pena de suspensão não excederá de",["noventa dias.","trinta dias.","sessenta dias.","cento e vinte dias.","um ano."],1,"Art. 197."),
("Questão 3","Considera-se abandono de cargo a ausência em serviço, sem justa causa, por mais de",["trinta dias consecutivos.","dez dias.","quinze dias.","sessenta dias.","noventa dias."],2,"Art. 198, § 1º."),
("Questão 4","Prescreverá em dois anos a falta sujeita a repreensão, multa ou",["suspensão.","demissão.","cassação.","disponibilidade.","aposentadoria."],3,"Art. 204, I.")]
t1="<strong>Recebimento de presente</strong><br><br>Um guarda municipal de Campinas aceitou um relógio de um comerciante como agradecimento por não autuá-lo, em razão de suas atribuições."
t2="<strong>Ausência prolongada</strong><br><br>Um servidor municipal faltou ao serviço por 45 dias consecutivos, sem justa causa."
t3="<strong>Ordem manifestamente ilegal</strong><br><br>Um superior determinou a um funcionário que ocultasse documentos de uma investigação, ordem manifestamente ilegal."
tx={"lm1a":t1,"lm1b":t2,"lm1c":t3}
# n=1
q(1,"São deveres do funcionário a assiduidade e a",["pontualidade.","simpatia.","pressa.","fama.","rapidez."],"Art. 184, II.")
q(1,"É dever do funcionário a urbanidade e a",["discrição.","pressa.","ironia.","fama.","aposta."],"Art. 184, III e IV.")
q(1,"É dever do funcionário a lealdade às instituições constitucionais e",["administrativas a que servir.","partidárias.","particulares.","religiosas.","sindicais."],"Art. 184, V.")
q(1,"O funcionário deve obedecer às ordens superiores, exceto quando",["manifestamente ilegais.","simples.","verbais.","tardias.","longas."],"Art. 184, VII.")
q(1,"É dever do funcionário atender prontamente às requisições para defesa da Fazenda",["Pública.","Federal.","Privada.","Particular.","Estadual."],"Art. 184, XI, a.")
q(1,"É proibido ao funcionário valer-se do cargo para lograr proveito",["pessoal.","coletivo.","público.","social.","comum."],"Art. 185, IV.")
q(1,"É proibido ao funcionário coagir ou aliciar subordinados com objetivos de natureza",["partidária.","funcional.","esportiva.","cultural.","religiosa."],"Art. 185, V.")
q(1,"É proibido ao funcionário praticar a usura em qualquer das suas",["formas.","datas.","horas.","regiões.","épocas."],"Art. 185, VII.")
q(1,"É proibido ao funcionário receber propinas, comissões, presentes e vantagens de qualquer espécie em razão das",["atribuições.","férias.","viagens.","festas.","contas."],"Art. 185, IX.")
q(1,"Pelo exercício irregular de suas atribuições, o funcionário responde civil, penal e",["administrativamente.","politicamente.","religiosamente.","tributariamente.","eleitoralmente."],"Art. 186.")
q(1,"As penas disciplinares do Estatuto incluem a advertência, a repreensão, as multas, a suspensão, a demissão e a cassação de",["aposentadoria e disponibilidade.","férias.","licença.","vencimento.","promoção."],"Art. 191.")
q(1,"A pena de repreensão será aplicada",["por escrito.","verbalmente.","por telefone.","por edital.","por mensagem."],"Art. 196.")
q(1,"No caso de abandono de cargo, o edital de chamamento tem prazo de",["vinte dias.","dez dias.","trinta dias.","quinze dias.","sessenta dias."],"Art. 195.")
q(1,"Uma das hipóteses de demissão é o crime contra a administração",["pública.","privada.","religiosa.","familiar.","tributária."],"Art. 198, I.")
q(1,"A pena de demissão pode ser aplicada por corrupção passiva, nos termos da",["Lei Penal.","Lei Civil.","Lei de Trânsito.","Lei Eleitoral.","Lei do Inquilinato."],"Art. 198, VIII.")
q(1,"O ato de demissão mencionará sempre a causa da",["penalidade.","remuneração.","vaga.","antiguidade.","viagem."],"Art. 199.")
q(1,"Para demissão, multa, cassação e suspensão por mais de 30 dias, é competente o",["Prefeito Municipal.","Diretor de Departamento.","Inspetor Fiscal.","Chefe de seção.","Vereador."],"Art. 201, I.")
q(1,"No texto do recebimento de presente, a conduta do guarda enquadra-se na proibição de receber presentes e vantagens em razão das",["atribuições.","férias.","folgas.","festas.","contas."],"Art. 185, IX.","lm1a")
q(1,"No texto da ausência prolongada, a ausência por 45 dias consecutivos é abandono, que se considera a ausência por mais de",["trinta dias consecutivos.","dez dias.","quinze dias.","sessenta dias.","noventa dias."],"Art. 198, § 1º.","lm1b")
q(1,"No texto da ordem manifestamente ilegal, o funcionário deve obedecer às ordens superiores, exceto quando",["manifestamente ilegais.","pouco claras.","verbais.","incômodas.","tardias."],"Art. 184, VII.","lm1c")
# n=2
q(2,"No estágio probatório, no texto do art. 15, apuram-se a idoneidade moral, a assiduidade, a disciplina e a",["eficiência.","simpatia.","fama.","renda.","antiguidade."],"Art. 15, § 1º.")
q(2,"O órgão de pessoal informa ao Prefeito sobre a conveniência da confirmação da nomeação trinta dias antes de decorrido o prazo do",["estágio.","concurso.","cargo.","mandato.","contrato."],"Art. 15, § 3º.")
q(2,"Da informação contrária à confirmação será dada vista ao estagiário, pelo prazo de",["cinco dias.","dez dias.","trinta dias.","quarenta e oito horas.","um mês."],"Art. 15, § 4º.")
q(2,"Se a decisão do Prefeito for favorável à permanência do funcionário, a confirmação",["não dependerá de qualquer novo ato.","depende de decreto.","depende de concurso.","depende de portaria.","depende da Câmara."],"Art. 15, § 6º.")
q(2,"A conclusão do estágio importará na efetivação",["automática do funcionário.","condicionada.","eventual.","diferida.","por sorteio."],"Art. 15, § 8º.")
q(2,"É proibido ao funcionário retirar, sem prévia autorização da autoridade competente, qualquer documento ou objeto da",["repartição.","cidade.","escola.","rua.","praça."],"Art. 185, II.")
q(2,"É proibido ao funcionário participar da gerência ou administração de empresas industrial ou comercial, salvo quando estiver de licença para tratar de interesses",["particulares ou em disponibilidade.","públicos.","eleitorais.","sindicais.","familiares apenas."],"Art. 185, VI.")
q(2,"É proibido ao funcionário pleitear como procurador, ou intermediário, junto às repartições públicas municipais, salvo vantagens de parente até",["2º grau.","1º grau.","3º grau.","4º grau.","5º grau."],"Art. 185, VIII.")
q(2,"A responsabilidade civil decorre de procedimento doloso ou culposo que importe em prejuízo para a Fazenda Municipal ou de",["terceiros.","parentes.","colegas.","superiores.","partidos."],"Art. 187.")
q(2,"A indenização de prejuízos pode ser descontada em prestações mensais não excedentes à décima parte do vencimento ou",["remuneração.","gratificação.","adicional.","pensão.","bônus."],"Art. 187, § 1º.")
q(2,"A responsabilidade penal abrange os crimes e contravenções imputados ao funcionário nessa",["qualidade.","data.","cidade.","viagem.","reunião."],"Art. 188.")
q(2,"As cominações civis, penais e disciplinares poderão acumular-se, sendo umas e outras independentes entre si, bem assim as instâncias civil, penal e",["administrativa.","política.","tributária.","religiosa.","eleitoral."],"Art. 190.")
q(2,"Na aplicação das penas disciplinares serão consideradas a natureza e a gravidade da infração e os danos que dela provierem para o serviço",["público.","privado.","comum.","social.","familiar."],"Art. 192.")
q(2,"A suspensão poderá ser convertida em multa de até cinquenta por cento por dia do vencimento, obrigado o funcionário a permanecer em",["serviço.","casa.","férias.","licença.","disponibilidade."],"Art. 197, parágrafo único.")
q(2,"A demissão poderá ser aplicada com a nota 'A bem do serviço",["público.","privado.","coletivo.","social.","comum."],"Art. 200.")
q(2,"A pena de cassação de aposentadoria e disponibilidade será aplicada se ficar provado que o inativo praticou falta grave no exercício do",["cargo.","trânsito.","comércio.","lazer.","voto."],"Art. 202, I.")
q(2,"A pena de disponibilidade é aplicada ao funcionário em gozo de estabilidade quando a conveniência do serviço público aconselhar o seu",["afastamento.","retorno.","aumento.","descanso.","estudo."],"Art. 203.")
q(2,"No texto do recebimento de presente, a infração do guarda pode levar à penalidade de demissão pela transgressão de itens do art. 185, entre os incisos",["IV a X.","I a III.","X a XII.","II e III.","I apenas."],"Art. 198, IX.","lm1a")
q(2,"No texto da ausência prolongada, o chefe da repartição promoverá a publicação de edital de chamamento por vinte dias, conforme o art.",["195.","194.","196.","197.","198."],"Art. 195.","lm1b")
q(2,"No texto da ordem manifestamente ilegal, o funcionário deve levar ao conhecimento da autoridade superior a irregularidade de que tiver ciência em razão do",["cargo.","bairro.","lazer.","contrato.","salário."],"Art. 184, VIII.","lm1c")
# n=3
q(3,"Assinale a alternativa correta sobre as penas disciplinares do Estatuto.",["A advertência é verbal; a repreensão é escrita; a suspensão não excede 90 dias.","A advertência é escrita.","A repreensão é verbal.","A suspensão chega a 180 dias.","A multa é a pena mais leve."],"Arts. 194, 196 e 197.")
q(3,"Considere. I. As penas disciplinares são seis. II. A advertência é por escrito. III. O Prefeito é competente para a demissão. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A advertência é verbal (art. 194).")
q(3,"Assinale a INCORRETA.",["O funcionário deve obedecer sempre, mesmo às ordens manifestamente ilegais.","O funcionário deve zelar pela economia do material.","O funcionário deve ser pontual.","O funcionário deve ser leal às instituições.","O funcionário deve levar ao superior a irregularidade que conhecer."],"A obediência exclui as ordens manifestamente ilegais (art. 184, VII).")
q(3,"Considera-se abandono de cargo a ausência sem justa causa por mais de trinta dias consecutivos ou entradas atrasadas ou saídas antecipadas em número superior a noventa, ocorridas",["consecutivamente.","interpoladamente.","anualmente.","semestralmente.","mensalmente."],"Art. 198, § 1º.")
q(3,"Será ainda demitido o servidor que, durante o ano, faltar ao serviço sessenta dias",["interpoladamente, sem causa justificada.","consecutivamente.","com atestado.","por licença.","por greve."],"Art. 198, § 2º.")
q(3,"A prescrição de quatro anos aplica-se às faltas sujeitas à pena de demissão no caso do § 2º do art. 198 e à cassação de aposentadoria e",["disponibilidade.","vencimento.","férias.","promoção.","licença."],"Art. 204, II.")
q(3,"A falta também prevista na Lei Penal como crime prescreverá juntamente com",["estes.","a lei civil.","a pena de multa apenas.","a sentença.","a licença."],"Art. 204, parágrafo único.")
q(3,"Para a imposição de suspensão por mais de 30 dias é competente o",["Prefeito Municipal.","Diretor do Departamento.","Inspetor Fiscal.","Chefe de seção.","Vereador."],"Art. 201, I.")
q(3,"Nos demais casos de pena disciplinar, são competentes o Diretor do Departamento e o",["Inspetor Fiscal.","Vereador.","Prefeito.","Secretário Geral da Câmara.","Juiz."],"Art. 201, II.")
q(3,"A demissão por ofensa física em serviço contra funcionário ou particular não se aplica em caso de",["legítima defesa.","estado de necessidade.","dever legal.","exercício regular.","provocação."],"Art. 198, V.")
q(3,"Será punido o funcionário que, sem justa causa, deixar de submeter-se à inspeção",["médica determinada por autoridade competente.","policial.","fiscal.","eleitoral.","tributária."],"Art. 193.")
q(3,"A suspensão será aplicada em casos de falta grave ou",["reincidência.","atraso.","licença.","promoção.","viagem."],"Art. 197.")
q(3,"A pena de demissão aplica-se a quem transgredir quaisquer dos itens IV a X do",["art. 185.","art. 184.","art. 186.","art. 191.","art. 204."],"Art. 198, IX.")
q(3,"Se a decisão for desfavorável, o estagiário recebe vista da informação contrária por cinco dias e o Prefeito, julgando aconselhável a exoneração, determina a lavratura dos respectivos",["decretos.","contratos.","editais.","avisos.","pareceres."],"Art. 15, § 5º.")
q(3,"No texto do recebimento de presente, a conduta pode também ser a hipótese de demissão por corrupção passiva, nos termos da",["Lei Penal.","Lei Civil.","Lei de Trânsito.","Lei Eleitoral.","Lei do Inquilinato."],"Art. 198, VIII.","lm1a")
q(3,"No texto do recebimento de presente, as responsabilidades civil, penal e administrativa do guarda podem",["acumular-se, sendo independentes entre si.","ser somente penais.","ser somente civis.","ser alternativas.","ser dispensadas."],"Art. 190.","lm1a")
q(3,"No texto da ausência prolongada, ausente justa causa, o chefe proporá a expedição de decreto de demissão após o fim do prazo do edital se não for provada",["força maior.","doença leve.","viagem.","festa.","licença-prêmio."],"Art. 195, parágrafo único.","lm1b")
q(3,"No texto da ausência prolongada, a ausência de 45 dias consecutivos configura a hipótese de demissão por",["abandono do cargo.","insubordinação.","embriaguez.","corrupção.","ofensa física."],"Art. 198, II.","lm1b")
q(3,"No texto da ordem manifestamente ilegal, o funcionário, ao recusar a ordem, age em conformidade com o dever de obedecer, exceto às ordens",["manifestamente ilegais.","legais.","verbais.","rotineiras.","simples."],"Art. 184, VII.","lm1c")
q(3,"No texto da ordem manifestamente ilegal, o funcionário também deve levar ao conhecimento da autoridade superior, conforme o art. 184, inciso",["VIII.","I.","VII.","X.","XI."],"Art. 184, VIII.","lm1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Estatuto dos Funcionários de Campinas (Lei 1.399/1955)",[
 ("est","Estágio probatório",["art. 15","1 ano no texto; hoje 3 anos","idoneidade, assiduidade, disciplina, eficiência"],"seção 1"),
 ("dev","Deveres",["art. 184","obediência, exceto ilegais","comunicar irregularidades"],"seção 2"),
 ("pro","Proibições",["art. 185","propinas e presentes","usura, partido, empresa"],"seção 2"),
 ("res","Responsabilidade",["civil, penal, administrativa","cumuláveis e independentes"],"seção 3"),
 ("pen","Penas",["seis penas","suspensão até 90 dias","demissão: nove hipóteses"],"seção 3"),
 ("pre","Prescrição",["2 anos","4 anos","crime prescreve junto"],"seção 3")],
 "Na prova: penas, 90 dias, 30 dias de abandono e prescrição de 2 e 4 anos")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o estágio probatório; as demais, os deveres, as proibições, as penas e a prescrição.","Fontes: Edital 02/2026, Anexo I; Lei Municipal 1.399/1955 (Estatuto dos Funcionários Públicos do Município de Campinas), art. 15 e arts. 184 a 204, texto de consulta da Câmara Municipal de Campinas (SAPL). Exemplos criados para a aula.")
revisao("lm-1","Estatuto do Servidor Público de Campinas (Lei 1.399/1955)",Q,list(tx),
 cobertura=["Art. 15 e arts. 184 a 204, integralmente (exceto o art. 198, § 2º, apenas citado)."],
 pendencias=["Texto-fonte: texto de consulta da Câmara Municipal de Campinas (SAPL), sem valor legal, baixado em 14/11/2026; reconferir a redação vigente no portal oficial de legislação de Campinas.","Contradição aparente: o art. 15 fala em estágio de 1 ano; o Decreto 21.019/2020 fixa 3 anos (art. 41 da CF). Conferir como o gabarito oficial tratará a questão.","Notas remissivas '(ver ...)' foram removidas do texto citado.","Casos lm1a, lm1b e lm1c fictícios."],
 fontes_conferidas=["Lei 1.399/1955, art. 15 e arts. 184 a 204: texto do SAPL, copiado por programa."])
gravar("lm-1",aula_html,banco("lm-1",Q),tx)
