import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='eca.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O ato infracional é o assunto do ECA que mais toca o guarda municipal: é ele que muitas vezes encontra o adolescente em flagrante. Os arts. 103 a 111 definem o ato infracional, a inimputabilidade dos menores de dezoito anos e os direitos de quem é apreendido: só se priva da liberdade em flagrante ou por ordem escrita e fundamentada do juiz, a apreensão é comunicada de imediato ao juiz e à família, e a internação antes da sentença dura no máximo 45 dias. A Vunesp cobra esses detalhes com a letra da lei."
S={}
S[1]="## 1. Ato infracional e inimputabilidade\n\n"+L("art. 103","Art. 103. Considera-se ato infracional","Art. 104.")+"\n\n"+L("art. 104","Art. 104. São penalmente inimputáveis","Art. 105.")+"\n\n"+L("art. 105","Art. 105. Ao ato infracional praticado por criança","CAPÍTULO II")+"""

Ato infracional é a conduta descrita como crime ou contravenção penal. Os menores de dezoito anos são penalmente inimputáveis e sujeitos às medidas previstas no Estatuto; vale a idade do adolescente à data do fato. Ao ato infracional praticado por criança (até doze anos incompletos) correspondem as medidas de proteção do art. 101, e não as medidas socioeducativas: a criança não é apreendida nem responde por ato infracional como o adolescente.
"""
S[2]="## 2. Direitos individuais: apreensão e internação provisória\n\n"+L("art. 106","Art. 106. Nenhum adolescente","Art. 107.")+"\n\n"+L("art. 107","Art. 107. A apreensão de qualquer adolescente","Art. 108.")+"\n\n"+L("art. 108","Art. 108. A internação, antes da sentença","Art. 109.")+"\n\n"+L("art. 109","Art. 109. O adolescente civilmente identificado","CAPÍTULO III")+"""

Nenhum adolescente é privado de sua liberdade senão em flagrante de ato infracional ou por ordem escrita e fundamentada da autoridade judiciária competente. O adolescente tem direito à identificação dos responsáveis pela apreensão e a ser informado de seus direitos. A apreensão e o local de recolhimento são comunicados imediatamente à autoridade judiciária e à família ou à pessoa indicada pelo adolescente, e examina-se desde logo, sob pena de responsabilidade, a possibilidade de liberação imediata.

A internação antes da sentença pode durar no máximo quarenta e cinco dias, em decisão fundamentada, baseada em indícios suficientes de autoria e materialidade e na necessidade imperiosa da medida. O adolescente civilmente identificado não passa por identificação compulsória pelos órgãos policiais, de proteção e judiciais, salvo para confrontação, havendo dúvida fundada.
"""
S[3]="## 3. Garantias processuais\n\n"+L("arts. 110 e 111","Art. 110. Nenhum adolescente será privado","CAPÍTULO IV")+"""

Nenhum adolescente é privado da liberdade sem o devido processo legal. São asseguradas, entre outras, seis garantias: pleno e formal conhecimento da atribuição do ato infracional, por citação ou meio equivalente; igualdade na relação processual, podendo confrontar-se com vítimas e testemunhas e produzir provas; defesa técnica por advogado; assistência judiciária gratuita e integral aos necessitados; direito de ser ouvido pessoalmente pela autoridade competente; e direito de solicitar a presença dos pais ou responsável em qualquer fase do procedimento.
"""
S[5]="""## 5. Na rotina do guarda

- **Flagrante de adolescente:** o guarda apreende, informa os direitos, identifica-se e conduz à autoridade policial; a apreensão e o local são comunicados de imediato ao juiz e à família.
- **Criança autora de ato infracional:** não é apreendida; o guarda a encaminha ao Conselho Tutelar, que aplica as medidas do art. 101.
- **Documento:** o adolescente identificado civilmente não passa por identificação compulsória.
- **Algemas e abordagem:** a condução respeita os direitos e a condição peculiar de pessoa em desenvolvimento.
- **Idade:** vale a data do fato; o adolescente que completa 18 depois do ato continua sujeito ao Estatuto quanto àquele ato.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Ato infracional | Conduta descrita como crime ou contravenção penal |
| Inimputabilidade | Menores de dezoito anos |
| Idade considerada | A da data do fato |
| Ato praticado por criança | Medidas do art. 101 (proteção) |
| Privação da liberdade | Só em flagrante ou por ordem escrita e fundamentada do juiz |
| Comunicação da apreensão | Imediata, ao juiz e à família ou pessoa indicada |
| Internação provisória | Máximo de quarenta e cinco dias |
| Identificação compulsória | Vedada, salvo confrontação com dúvida fundada |
| Garantias | Seis: conhecimento, igualdade, defesa técnica, assistência gratuita, oitiva pessoal, presença dos pais |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 103 | Ato infracional = crime ou contravenção |
| Art. 104 | Inimputáveis os menores de 18; idade na data do fato |
| Art. 105 | Criança: medidas do art. 101 |
| Art. 106 | Liberdade: flagrante ou ordem escrita fundamentada |
| Art. 107 | Comunicação imediata ao juiz e à família |
| Art. 108 | Internação provisória: 45 dias |
| Art. 109 | Sem identificação compulsória |
| Art. 110 | Devido processo legal |
| Art. 111 | Seis garantias processuais |
"""
QR=[("Questão 1","Considera-se ato infracional a conduta descrita como",["crime ou contravenção penal.","apenas crime.","apenas contravenção.","infração administrativa.","ilícito civil."],0,"Art. 103."),
("Questão 2","A internação, antes da sentença, pode ser determinada pelo prazo máximo de",["quarenta e cinco dias.","dez dias.","trinta dias.","sessenta dias.","noventa dias."],1,"Art. 108."),
("Questão 3","Nenhum adolescente será privado de sua liberdade senão em flagrante de ato infracional ou por ordem escrita e fundamentada da",["autoridade judiciária competente.","autoridade policial.","autoridade administrativa.","família.","escola."],2,"Art. 106."),
("Questão 4","Ao ato infracional praticado por criança corresponderão as medidas previstas no art.",["101.","112.","98.","104.","90."],3,"Art. 105.")]
t1="<strong>Flagrante na praça</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, surpreendeu um adolescente de dezessete anos furtando uma bicicleta na praça central. Ele foi contido e conduzido."
t2="<strong>Criança com bicicleta</strong><br><br>Em Vila Nova, um menino de onze anos foi flagrado levando uma bicicleta que não era sua e confessou ter pegado de um colega."
t3="<strong>Adolescente que completou dezoito anos</strong><br><br>Um rapaz de Vila Nova praticou um furto quando tinha dezessete anos e onze meses. A apreensão só ocorreu dois meses depois, quando já tinha dezoito anos."
tx={"eca6a":t1,"eca6b":t2,"eca6c":t3}
# n=1
q(1,"São penalmente inimputáveis os menores de",["dezoito anos.","catorze anos.","dezesseis anos.","vinte e um anos.","doze anos."],"Art. 104.")
q(1,"Para os efeitos do Estatuto, deve ser considerada a idade do adolescente à data do",["fato.","julgamento.","apreensão.","cumprimento da medida.","nascimento do filho."],"Art. 104, parágrafo único.")
q(1,"O adolescente tem direito à identificação dos responsáveis pela sua apreensão, devendo ser informado acerca de seus",["direitos.","deveres.","antecedentes.","bens.","custos."],"Art. 106, parágrafo único.")
q(1,"A apreensão de qualquer adolescente e o local onde se encontra recolhido serão comunicados incontinenti à autoridade judiciária e à",["família do apreendido ou à pessoa por ele indicada.","escola.","imprensa.","vizinhança.","empresa."],"Art. 107.")
q(1,"Na apreensão, examinar-se-á desde logo, sob pena de responsabilidade, a possibilidade de",["liberação imediata.","internação.","prisão.","transferência.","julgamento."],"Art. 107, parágrafo único.")
q(1,"A decisão da internação provisória deve basear-se em indícios suficientes de autoria e",["materialidade.","reincidência.","periculosidade.","antecedentes.","confissão."],"Art. 108, parágrafo único.")
q(1,"O adolescente civilmente identificado não será submetido a identificação",["compulsória pelos órgãos policiais, de proteção e judiciais.","civil.","voluntária.","por documento.","por foto, em qualquer caso."],"Art. 109.")
q(1,"Nenhum adolescente será privado de sua liberdade sem o devido",["processo legal.","consentimento.","acordo.","registro.","exame."],"Art. 110.")
q(1,"É garantia do adolescente a defesa técnica por",["advogado.","parente.","amigo.","policial.","escrivão."],"Art. 111, III.")
q(1,"É garantia do adolescente o direito de ser ouvido pessoalmente pela autoridade",["competente.","policial apenas.","administrativa.","escolar.","comunitária."],"Art. 111, V.")
q(1,"É garantia do adolescente solicitar a presença de seus pais ou responsável em qualquer fase do",["procedimento.","contrato.","passeio.","trabalho.","curso."],"Art. 111, VI.")
q(1,"É garantia do adolescente a assistência judiciária gratuita e integral aos",["necessitados, na forma da lei.","ricos.","adultos.","estrangeiros.","empresários."],"Art. 111, IV.")
q(1,"É garantia do adolescente o pleno e formal conhecimento da atribuição de ato infracional, mediante citação ou meio",["equivalente.","oposto.","oral apenas.","informal.","indireto."],"Art. 111, I.")
q(1,"O ato infracional é conduta descrita como",["crime ou contravenção penal.","infração disciplinar.","falta escolar.","infração de trânsito.","ilícito tributário."],"Art. 103.")
q(1,"A criança que pratica ato infracional sujeita-se às medidas",["de proteção do art. 101.","socioeducativas.","de internação.","de semiliberdade.","de liberdade assistida."],"Art. 105.")
q(1,"A privação de liberdade do adolescente só é possível em flagrante ou por ordem escrita e",["fundamentada da autoridade judiciária.","verbal da polícia.","do Conselho Tutelar.","do Ministério Público.","da escola."],"Art. 106.")
q(1,"A igualdade na relação processual permite ao adolescente confrontar-se com vítimas e",["testemunhas.","juízes.","promotores.","jornalistas.","delegados."],"Art. 111, II.")
q(1,"No texto do flagrante na praça, a apreensão do adolescente em flagrante de ato infracional é",["permitida, pois houve flagrante.","proibida.","dependente de mandado sempre.","dependente da escola.","dependente dos pais."],"Art. 106.","eca6a")
q(1,"No texto da criança com bicicleta, o ato infracional praticado por criança implica as medidas do art.",["101.","112.","106.","108.","111."],"Art. 105.","eca6b")
q(1,"No texto do adolescente que completou dezoito anos, vale a idade do rapaz à data do",["fato.","julgamento.","apreensão.","cumprimento.","registro."],"Art. 104, parágrafo único.","eca6c")
# n=2
q(2,"As medidas previstas no Estatuto aplicam-se aos menores de dezoito anos, que são",["penalmente inimputáveis.","imputáveis.","semi-imputáveis.","relativamente imputáveis.","responsáveis civis apenas."],"Art. 104.")
q(2,"A criança que pratica ato infracional é encaminhada, para a aplicação das medidas do art. 101, em regra, ao",["Conselho Tutelar.","Presídio.","Fórum, direto.","Corpo de Bombeiros.","Detran."],"Art. 105 e art. 136.")
q(2,"A comunicação da apreensão à autoridade judiciária deve ser feita",["imediatamente.","em 48 horas.","em 10 dias.","em 30 dias.","a critério do guarda."],"Art. 107.")
q(2,"O local onde o adolescente se encontra recolhido deve ser comunicado à autoridade judiciária competente e à",["família ou pessoa indicada.","imprensa.","Câmara.","escola.","empresa."],"Art. 107.")
q(2,"A internação antes da sentença exige decisão",["fundamentada.","verbal.","sigilosa, sempre.","do Conselho Tutelar.","policial."],"Art. 108, parágrafo único.")
q(2,"A internação provisória exige a demonstração da necessidade",["imperiosa da medida.","eventual da medida.","financeira.","política.","social, apenas."],"Art. 108, parágrafo único.")
q(2,"A identificação compulsória é admitida apenas para efeito de confrontação, havendo dúvida",["fundada.","qualquer.","leve.","imaginária.","apenas dos pais."],"Art. 109.")
q(2,"A igualdade na relação processual inclui produzir todas as provas necessárias à",["defesa.","acusação.","sentença.","execução.","apreensão."],"Art. 111, II.")
q(2,"O art. 111 assegura ao adolescente, entre outras, as garantias",["seguintes (seis incisos).","apenas duas.","apenas três.","apenas quatro.","apenas cinco."],"Art. 111.")
q(2,"A defesa técnica do adolescente é garantida por meio de",["advogado.","guarda.","escrivão.","delegado.","oficial."],"Art. 111, III.")
q(2,"No Estatuto, o ato infracional é conceito aplicado a condutas descritas como crime ou contravenção, e a imputabilidade penal começa aos",["dezoito anos.","dezesseis anos.","quatorze anos.","vinte e um anos.","doze anos."],"Art. 104.")
q(2,"A apreensão do adolescente fora de flagrante exige",["ordem escrita e fundamentada da autoridade judiciária.","ordem verbal do guarda.","autorização dos pais.","pedido da escola.","decisão do Conselho Tutelar."],"Art. 106.")
q(2,"A liberação imediata do adolescente apreendido deve ser examinada desde logo, sob pena de",["responsabilidade.","prisão do adolescente.","multa de trânsito.","exílio.","nenhuma sanção."],"Art. 107, parágrafo único.")
q(2,"O adolescente tem direito a ser informado sobre seus direitos e a identificar os responsáveis pela",["apreensão.","escola.","família.","moradia.","alimentação."],"Art. 106, parágrafo único.")
q(2,"O prazo máximo da internação antes da sentença é de",["quarenta e cinco dias.","trinta dias.","sessenta dias.","noventa dias.","cento e vinte dias."],"Art. 108.")
q(2,"No texto do flagrante na praça, o adolescente apreendido tem direito de identificar os responsáveis pela apreensão e de ser informado de seus",["direitos.","bens.","antecedentes.","gastos.","vizinhos."],"Art. 106, parágrafo único.","eca6a")
q(2,"No texto da criança com bicicleta, o menino de onze anos, por ser criança, não é submetido a",["medida socioeducativa.","medida de proteção.","orientação.","encaminhamento.","acompanhamento."],"Art. 105.","eca6b")
q(2,"No texto do adolescente que completou dezoito anos, a data relevante para a inimputabilidade é a do",["fato.","julgamento.","aniversário.","registro.","processo."],"Art. 104, parágrafo único.","eca6c")
q(2,"O art. 110 veda a privação da liberdade do adolescente sem o devido",["processo legal.","consentimento dos pais.","parecer do Conselho Tutelar.","laudo médico.","pedido da vítima."],"Art. 110.")
q(2,"Ao praticar ato infracional, o menor de dezoito anos sujeita-se às medidas previstas",["no Estatuto da Criança e do Adolescente.","no Código Penal.","no Código de Trânsito.","na Lei de Execução Penal.","no Código Civil."],"Art. 104.")
# n=3
q(3,"Assinale a alternativa correta.",["Nenhum adolescente é privado de liberdade senão em flagrante ou por ordem escrita e fundamentada do juiz; a internação provisória dura no máximo 45 dias.","A internação provisória dura 90 dias.","A apreensão é comunicada ao juiz em dez dias.","A apreensão independe de flagrante ou ordem.","A criança responde por medidas socioeducativas."],"Arts. 106 e 108.")
q(3,"Considere. I. O ato infracional é conduta descrita como crime ou contravenção. II. A internação provisória pode durar até 60 dias. III. A idade considerada é a da data do fato. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A internação provisória dura até 45 dias (art. 108).")
q(3,"Assinale a INCORRETA.",["O adolescente identificado civilmente deve sempre ser identificado compulsoriamente.","A defesa técnica por advogado é garantia.","A apreensão é comunicada ao juiz e à família.","O adolescente pode pedir a presença dos pais.","A criança sujeita-se às medidas do art. 101."],"Não há identificação compulsória, salvo confrontação com dúvida fundada (art. 109).")
q(3,"A comunicação incontinenti da apreensão é feita à autoridade judiciária competente e à família ou à pessoa indicada pelo",["adolescente.","guarda.","delegado.","promotor.","juiz."],"Art. 107.")
q(3,"O Estatuto exige que a decisão de internação provisória seja fundamentada e baseada em indícios suficientes de autoria e materialidade, demonstrada a",["necessidade imperiosa da medida.","vontade da vítima.","pressão popular.","gravidade moral.","reincidência."],"Art. 108, parágrafo único.")
q(3,"A garantia do pleno e formal conhecimento da atribuição de ato infracional é feita por",["citação ou meio equivalente.","comunicação verbal.","notificação eletrônica, apenas.","carta aos pais.","edital, sempre."],"Art. 111, I.")
q(3,"A assistência judiciária ao adolescente é gratuita e integral aos",["necessitados, na forma da lei.","adultos.","maiores de 16.","menores de 14.","reincidentes."],"Art. 111, IV.")
q(3,"O direito de solicitar a presença dos pais ou responsável vale",["em qualquer fase do procedimento.","apenas na audiência.","apenas na apreensão.","apenas na sentença.","apenas na execução."],"Art. 111, VI.")
q(3,"A inimputabilidade penal dos menores de dezoito anos é acompanhada, no Estatuto, da sujeição às",["medidas previstas na própria lei.","penas do Código Penal.","penas de prisão.","penas de multa.","medidas de segurança."],"Art. 104.")
q(3,"A criança que pratica ato infracional não se sujeita a medida socioeducativa, mas a medidas",["de proteção do art. 101.","de internação.","de prisão.","de semiliberdade.","de liberdade assistida."],"Art. 105.")
q(3,"A privação de liberdade do adolescente sem o devido processo legal é vedada pelo art.",["110.","103.","104.","105.","109."],"Art. 110.")
q(3,"A identificação compulsória do adolescente, havendo dúvida fundada, admite-se para efeito de",["confrontação.","registro.","publicidade.","estatística.","divulgação."],"Art. 109.")
q(3,"O art. 106, parágrafo único, assegura ao adolescente identificar os responsáveis pela apreensão, o que protege contra",["abusos na apreensão.","fuga.","reincidência.","testemunhas.","parentes."],"Art. 106, parágrafo único.")
q(3,"A comunicação da apreensão à família pode ser feita também à pessoa",["por ele indicada.","escolhida pelo guarda.","escolhida pelo delegado.","da vizinhança.","da imprensa."],"Art. 107.")
q(3,"A internação provisória, antes da sentença, tem prazo máximo de 45 dias e exige necessidade",["imperiosa.","eventual.","comum.","sugerida.","relativa."],"Art. 108.")
q(3,"No texto do flagrante na praça, a comunicação da apreensão ao juiz e à família deve ser",["imediata.","em 48 horas.","em 5 dias.","opcional.","mensal."],"Art. 107.","eca6a")
q(3,"No texto do flagrante na praça, além de comunicar o juiz e a família, deve-se examinar de imediato a possibilidade de",["liberação imediata.","internação.","julgamento.","transferência para adulto.","prisão preventiva."],"Art. 107, parágrafo único.","eca6a")
q(3,"No texto da criança com bicicleta, o guarda deve encaminhar o menino ao Conselho Tutelar, que poderá aplicar as medidas de",["proteção do art. 101.","internação.","semiliberdade.","liberdade assistida.","prisão."],"Art. 105.","eca6b")
q(3,"No texto do adolescente que completou dezoito anos, o rapaz, pelo fato ocorrido aos dezessete anos e onze meses, é",["inimputável e sujeito às medidas do Estatuto.","imputável, sujeito ao Código Penal.","isento de qualquer medida.","sujeito à pena de prisão.","sujeito apenas a multa."],"Art. 104.","eca6c")
q(3,"No texto do adolescente que completou dezoito anos, a regra aplicada é a de que a idade é considerada à data do",["fato.","aniversário.","julgamento.","processo.","pagamento."],"Art. 104, parágrafo único.","eca6c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("ECA: ato infracional (arts. 103 a 111)",[
 ("ato","Ato infracional",["crime ou contravenção","art. 103"],"seção 1"),
 ("ina","Inimputabilidade",["menores de 18","idade na data do fato","criança: art. 101"],"seção 1"),
 ("lib","Privação de liberdade",["flagrante","ordem escrita e fundamentada","devido processo legal"],"seção 2"),
 ("com","Comunicação",["imediata ao juiz","à família","liberação imediata"],"seção 2"),
 ("int","Internação provisória",["máximo 45 dias","indícios de autoria e materialidade","necessidade imperiosa"],"seção 2"),
 ("gar","Garantias",["advogado","oitiva pessoal","presença dos pais"],"seção 3")],
 "Na prova: flagrante ou ordem; 45 dias; comunicação imediata")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o conceito e a inimputabilidade; as demais, a apreensão, a internação provisória e as garantias.","Fontes: Edital 02/2026, Anexo I; Lei 8.069/1990 (ECA), arts. 103 a 111, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("eca-6","ECA: prática de ato infracional (arts. 103 a 111)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (103 a 111)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Uma questão n2 cita o art. 136 (atribuições do Conselho Tutelar), que não está no recorte; conferir na revisão humana.","Trechos de lei copiados de fontes/eca.txt por programa.","Casos eca6a, eca6b e eca6c fictícios."],
 fontes_conferidas=["ECA, arts. 103 a 111: texto da Câmara, copiado por programa."])
gravar("eca-6",aula_html,banco("eca-6",Q),tx)
