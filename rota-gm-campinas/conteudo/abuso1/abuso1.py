import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='abuso.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Lei de Abuso de Autoridade (Lei 13.869/2019) define os crimes cometidos por agente público que, no exercício de suas funções ou a pretexto de exercê-las, abusa do poder. O guarda municipal é agente público e, portanto, sujeito ativo desses crimes. Os arts. 1º a 8º trazem o conceito, o dolo específico (finalidade de prejudicar outrem, beneficiar a si ou a terceiro, ou capricho), os sujeitos, a ação penal, os efeitos da condenação e a independência das esferas. A Vunesp cobra a finalidade específica, a regra de que divergência na interpretação não é abuso e o prazo de um a cinco anos de inabilitação."
S={}
S[1]="## 1. Conceito, finalidade específica, sujeitos e ação penal\n\n"+L("art. 1º, caput","Art. 1º Esta Lei define","§ 1º As condutas descritas")+"\n\n"+L("art. 1º, § 1º","§ 1º As condutas descritas","§ 2º A divergência")+"\n\n"+L("art. 1º, § 2º","§ 2º A divergência","CAPÍTULO II")+"\n\n"+L("art. 2º, caput","Art. 2º É sujeito ativo","Parágrafo único. Reputa-se")+"\n\n"+L("art. 2º, parágrafo único","Parágrafo único. Reputa-se agente público","CAPÍTULO III")+"\n\n"+L("art. 3º, caput","Art. 3º Os crimes previstos nesta Lei","§ 1º Será admitida")+"""

A lei define os crimes de abuso de autoridade cometidos por agente público, servidor ou não, que, no exercício de suas funções ou a pretexto de exercê-las, abuse do poder que lhe tenha sido atribuído. As condutas só são crime quando praticadas com a finalidade específica de prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou ainda por mero capricho ou satisfação pessoal. A divergência na interpretação de lei ou na avaliação de fatos e provas não configura abuso.

É sujeito ativo qualquer agente público, servidor ou não, da administração direta, indireta ou fundacional de qualquer dos Poderes da União, dos Estados, do DF, dos Municípios e de Território, incluindo servidores públicos e militares, membros do Legislativo, do Executivo, do Judiciário, do Ministério Público e dos tribunais ou conselhos de contas. Reputa-se agente público quem exerce, ainda que transitoriamente ou sem remuneração, mandato, cargo, emprego ou função. Os crimes são de ação penal pública incondicionada, admitida a ação privada se a pública não for intentada no prazo legal.
"""
S[2]="## 2. Efeitos da condenação e penas restritivas\n\n"+L("art. 4º","Art. 4º São efeitos da condenação","Parágrafo único. Os efeitos previstos")+"\n\n"+L("art. 4º, parágrafo único","Parágrafo único. Os efeitos previstos nos incisos II e III","Seção II")+"\n\n"+L("art. 5º","Art. 5º As penas restritivas de direitos","III - (VETADO)")+"\n\n"+L("art. 5º, parágrafo único","Parágrafo único. As penas restritivas","CAPÍTULO V")+"""

São efeitos da condenação tornar certa a obrigação de indenizar o dano causado pelo crime, devendo o juiz fixar na sentença o valor mínimo para reparação dos danos; a inabilitação para o exercício de cargo, mandato ou função pública pelo período de um a cinco anos; e a perda do cargo, do mandato ou da função pública. Os dois últimos efeitos são condicionados à reincidência em crime de abuso de autoridade e não são automáticos, devendo ser declarados motivadamente na sentença.

As penas restritivas de direitos substitutivas das privativas de liberdade são a prestação de serviços à comunidade ou a entidades públicas e a suspensão do exercício do cargo, da função ou do mandato, de um a seis meses, com perda dos vencimentos e das vantagens. Podem ser aplicadas autônoma ou cumulativamente.
"""
S[3]="## 3. Sanções civis e administrativas\n\n"+L("art. 6º","Art. 6º As penas previstas","Art. 7º")+"\n\n"+L("art. 7º","Art. 7º As responsabilidades civil","Art. 8º")+"\n\n"+L("art. 8º","Art. 8º Faz coisa julgada","CAPÍTULO VI")+"""

As penas da lei são aplicadas independentemente das sanções civis ou administrativas cabíveis, e as notícias de crime que descreverem falta funcional são informadas à autoridade competente para apuração. As responsabilidades civil e administrativa são independentes da criminal, não se podendo mais questionar a existência ou a autoria do fato quando decididas no juízo criminal. Faz coisa julgada nas esferas cível e administrativo-disciplinar a sentença penal que reconhecer o ato praticado em estado de necessidade, legítima defesa, estrito cumprimento de dever legal ou exercício regular de direito.
"""
S[5]="""## 5. Na rotina do guarda

- **Agente público:** o guarda municipal é agente público e pode ser sujeito ativo de abuso de autoridade.
- **Dolo específico:** o crime exige finalidade de prejudicar, beneficiar a si ou a terceiro, ou capricho; o erro de interpretação não é crime.
- **Estrito cumprimento do dever legal:** quando reconhecido pelo juízo penal, faz coisa julgada nas esferas civil e administrativa.
- **Independência:** o mesmo fato pode gerar responsabilidade penal, civil e administrativa.
- **Efeitos:** a condenação pode levar à inabilitação de um a cinco anos e à perda do cargo, em caso de reincidência, de forma motivada.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Elemento subjetivo | Finalidade específica de prejudicar outrem, beneficiar a si ou a terceiro, ou capricho ou satisfação pessoal |
| Divergência de interpretação | Não configura abuso |
| Sujeito ativo | Qualquer agente público, servidor ou não |
| Ação penal | Pública incondicionada |
| Inabilitação | 1 a 5 anos |
| Perda do cargo | Condicionada à reincidência; não é automática |
| Suspensão do cargo | 1 a 6 meses, com perda dos vencimentos |
| Esferas | Independentes; coisa julgada se reconhecido estado de necessidade, legítima defesa, dever legal ou exercício regular de direito |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Dolo específico; divergência não é abuso |
| Art. 2º | Qualquer agente público |
| Art. 3º | Ação penal pública incondicionada |
| Art. 4º | Indenização, inabilitação (1 a 5 anos), perda do cargo (reincidência) |
| Art. 5º | Serviços à comunidade; suspensão do cargo (1 a 6 meses) |
| Art. 6º | Penas independem das sanções civis e administrativas |
| Art. 7º | Responsabilidades independentes |
| Art. 8º | Coisa julgada em excludentes |
"""
QR=[("Questão 1","As condutas descritas na Lei de Abuso de Autoridade constituem crime quando praticadas com a finalidade específica de prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou ainda por mero",["capricho ou satisfação pessoal.","erro.","engano.","azar.","descuido."],0,"Art. 1º, § 1º."),
("Questão 2","A divergência na interpretação de lei ou na avaliação de fatos e provas",["não configura abuso de autoridade.","configura abuso.","é sempre crime.","gera prisão.","gera demissão."],1,"Art. 1º, § 2º."),
("Questão 3","A inabilitação para o exercício de cargo, mandato ou função pública, como efeito da condenação, é pelo período de",["um a cinco anos.","seis meses a um ano.","dois a oito anos.","dez anos.","vitalícia."],2,"Art. 4º, II."),
("Questão 4","Os crimes de abuso de autoridade são de ação penal",["pública incondicionada.","privada.","condicionada à representação.","subsidiária.","mista."],3,"Art. 3º.")]
t1="<strong>Capricho do agente</strong><br><br>Um guarda municipal de Vila Nova, cidade fictícia, deteve um comerciante por irritação pessoal, sem qualquer motivo legal, apenas para humilhá-lo."
t2="<strong>Divergência de interpretação</strong><br><br>Um guarda de Vila Nova interpretou uma norma municipal de forma diferente do chefe e autuou um comerciante, e o superior considerou a interpretação equivocada."
t3="<strong>Condenação por abuso</strong><br><br>Um agente público, reincidente em crime de abuso de autoridade, foi condenado, e o juiz declarou na sentença, motivadamente, a perda do cargo."
tx={"abuso1a":t1,"abuso1b":t2,"abuso1c":t3}
# n=1
q(1,"A Lei 13.869/2019 define os crimes de abuso de autoridade cometidos por agente",["público, servidor ou não.","privado.","apenas servidor.","apenas militar.","apenas magistrado."],"Art. 1º.")
q(1,"O crime ocorre quando o agente, no exercício de suas funções ou a pretexto de exercê-las, abuse do poder que lhe tenha sido",["atribuído.","negado.","delegado a terceiros.","retirado.","emprestado."],"Art. 1º.")
q(1,"A finalidade específica pode ser prejudicar outrem ou beneficiar a si mesmo ou a",["terceiro.","empresa.","comunidade.","Estado.","juiz."],"Art. 1º, § 1º.")
q(1,"Também configura o crime a conduta praticada por mero capricho ou satisfação",["pessoal.","coletiva.","pública.","profissional.","institucional."],"Art. 1º, § 1º.")
q(1,"A divergência na avaliação de fatos e provas não configura abuso de",["autoridade.","direito.","liberdade.","poder familiar.","profissão."],"Art. 1º, § 2º.")
q(1,"É sujeito ativo do crime de abuso de autoridade qualquer agente público, servidor ou",["não.","apenas concursado.","apenas militar.","apenas juiz.","apenas policial."],"Art. 2º.")
q(1,"Os membros do Ministério Público são sujeitos ativos do crime de abuso de",["autoridade.","poder econômico.","direito.","omissão.","tutela."],"Art. 2º, V.")
q(1,"Reputa-se agente público quem exerce função ainda que transitoriamente ou sem",["remuneração.","concurso.","gratificação.","posse.","carteira."],"Art. 2º, parágrafo único.")
q(1,"Os crimes da lei são de ação penal",["pública incondicionada.","privada.","condicionada.","eventual.","subsidiária apenas."],"Art. 3º.")
q(1,"São efeitos da condenação tornar certa a obrigação de",["indenizar o dano causado pelo crime.","prender.","absolver.","reintegrar.","promover."],"Art. 4º, I.")
q(1,"A inabilitação para cargo, mandato ou função pública como efeito da condenação é por um a",["cinco anos.","dois anos.","três anos.","dez anos.","seis meses."],"Art. 4º, II.")
q(1,"É efeito da condenação a perda do cargo, do mandato ou da função",["pública.","privada.","religiosa.","sindical.","partidária."],"Art. 4º, III.")
q(1,"Os efeitos de inabilitação e de perda são condicionados à reincidência e não são",["automáticos.","motivados.","fundamentados.","declarados.","públicos."],"Art. 4º, parágrafo único.")
q(1,"Uma das penas restritivas de direitos é a prestação de serviços à",["comunidade ou a entidades públicas.","empresa.","igreja.","família.","escola."],"Art. 5º, I.")
q(1,"A suspensão do exercício do cargo, como pena restritiva, é de um a seis",["meses.","anos.","dias.","semanas.","décadas."],"Art. 5º, II.")
q(1,"As penas restritivas de direitos podem ser aplicadas autônoma ou",["cumulativamente.","alternadamente.","eventualmente.","retroativamente.","provisoriamente."],"Art. 5º, parágrafo único.")
q(1,"As penas da lei serão aplicadas independentemente das sanções civis ou",["administrativas cabíveis.","penais.","tributárias.","eleitorais.","trabalhistas."],"Art. 6º.")
q(1,"No texto do capricho do agente, a detenção por irritação pessoal enquadra-se na finalidade de",["mero capricho ou satisfação pessoal.","divergência de interpretação.","estrito cumprimento de dever legal.","legítima defesa.","estado de necessidade."],"Art. 1º, § 1º.","abuso1a")
q(1,"No texto da divergência de interpretação, a interpretação diversa da norma pelo guarda",["não configura abuso de autoridade.","configura abuso.","é sempre crime.","gera prisão.","gera demissão."],"Art. 1º, § 2º.","abuso1b")
q(1,"No texto da condenação por abuso, a perda do cargo depende de reincidência e de decisão",["motivada na sentença.","automática.","verbal.","do chefe.","do corregedor."],"Art. 4º, parágrafo único.","abuso1c")
# n=2
q(2,"O art. 2º inclui, entre os sujeitos ativos, os membros dos tribunais ou conselhos de",["contas.","classe.","consumidores.","moradores.","empresas."],"Art. 2º, VI.")
q(2,"O art. 2º abrange a administração direta, indireta ou",["fundacional.","privada.","comercial.","religiosa.","partidária."],"Art. 2º.")
q(2,"Admite-se ação privada se a ação penal pública não for intentada no",["prazo legal.","mês seguinte.","ano seguinte.","prazo do chefe.","prazo de prescrição."],"Art. 3º, § 1º.")
q(2,"Na ação privada subsidiária, o Ministério Público pode aditar a queixa, repudiá-la e oferecer denúncia",["substitutiva.","aditiva.","complementar.","paralela.","opcional."],"Art. 3º, § 1º.")
q(2,"O juiz fixará na sentença o valor mínimo para reparação dos danos, a requerimento do",["ofendido.","ofensor.","juiz.","delegado.","promotor."],"Art. 4º, I.")
q(2,"Os efeitos de inabilitação e de perda do cargo devem ser declarados motivadamente na",["sentença.","denúncia.","queixa.","portaria.","súmula."],"Art. 4º, parágrafo único.")
q(2,"A suspensão do cargo como pena restritiva implica perda dos vencimentos e das",["vantagens.","dívidas.","funções.","férias.","licenças."],"Art. 5º, II.")
q(2,"As notícias de crimes da lei que descreverem falta funcional serão informadas à autoridade competente com vistas à",["apuração.","absolvição.","prescrição.","anistia.","extinção."],"Art. 6º, parágrafo único.")
q(2,"As responsabilidades civil e administrativa são independentes da",["criminal.","tributária.","eleitoral.","trabalhista.","ambiental."],"Art. 7º.")
q(2,"Não se pode mais questionar sobre a existência ou a autoria do fato quando essas questões tenham sido decididas no juízo",["criminal.","cível.","eleitoral.","trabalhista.","administrativo."],"Art. 7º.")
q(2,"Faz coisa julgada no âmbito cível e administrativo-disciplinar a sentença penal que reconhecer estado de necessidade, legítima defesa, estrito cumprimento de dever legal ou exercício regular de",["direito.","poder.","cargo.","dever.","mandato."],"Art. 8º.")
q(2,"O art. 8º trata da coisa julgada em âmbito",["cível e administrativo-disciplinar.","apenas penal.","apenas eleitoral.","apenas tributário.","apenas trabalhista."],"Art. 8º.")
q(2,"A lei trata como agentes públicos os militares e as pessoas a eles",["equiparadas.","contrárias.","aposentadas.","estrangeiras.","privadas."],"Art. 2º, I.")
q(2,"Os crimes dependem de dolo específico, o que significa que o agente deve ter a finalidade de prejudicar outrem ou beneficiar a si ou a",["terceiro, ou agir por capricho.","a empresa.","a comunidade.","o Estado.","o juiz."],"Art. 1º, § 1º.")
q(2,"O sujeito ativo pode ser membro do Poder Executivo, do Legislativo e do",["Judiciário.","clero.","comércio.","sindicato.","condomínio."],"Art. 2º, II a IV.")
q(2,"Quanto à inabilitação, o período é de um a cinco anos e o efeito é condicionado à",["reincidência.","confissão.","prisão.","multa.","absolvição."],"Art. 4º, parágrafo único.")
q(2,"No texto do capricho do agente, o guarda é sujeito ativo porque é",["agente público.","particular.","vigilante.","estagiário.","voluntário."],"Art. 2º.","abuso1a")
q(2,"No texto da divergência de interpretação, o erro de interpretação da norma municipal pelo guarda decorre da divergência na interpretação de",["lei.","preço.","contrato.","impostos.","horário."],"Art. 1º, § 2º.","abuso1b")
q(2,"No texto da condenação por abuso, a inabilitação acompanharia a perda do cargo pelo período de um a",["cinco anos.","dois anos.","três anos.","dez anos.","seis meses."],"Art. 4º, II.","abuso1c")
q(2,"O crime de abuso de autoridade exige que o agente atue no exercício de suas funções ou a pretexto de",["exercê-las.","abandoná-las.","delegá-las.","renunciá-las.","omiti-las."],"Art. 1º.")
# n=3
q(3,"Assinale a alternativa correta sobre a Lei 13.869/2019 (arts. 1º a 8º).",["O crime exige finalidade específica; a divergência de interpretação não é abuso; a ação é pública incondicionada.","O crime dispensa finalidade específica.","A divergência de interpretação é abuso.","A ação é privada.","Somente policiais respondem."],"Arts. 1º a 3º.")
q(3,"Considere. I. A inabilitação dura de 1 a 5 anos. II. A perda do cargo é automática. III. A suspensão do cargo é de 1 a 6 meses. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Os efeitos não são automáticos (art. 4º, parágrafo único).")
q(3,"Assinale a INCORRETA.",["A responsabilidade civil depende da criminal.","As responsabilidades civil e administrativa são independentes da criminal.","As penas se aplicam independentemente de sanções civis e administrativas.","A sentença que reconhece legítima defesa faz coisa julgada.","As notícias de falta funcional vão à autoridade competente."],"Art. 7º: independentes.")
q(3,"A prestação de serviços e a suspensão do cargo são penas restritivas de direitos substitutivas das",["privativas de liberdade previstas na lei.","multas.","penas pecuniárias.","medidas cautelares.","sanções civis."],"Art. 5º.")
q(3,"A finalidade específica do art. 1º, § 1º, abrange prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou ainda agir por",["mero capricho ou satisfação pessoal.","erro de fato.","erro de direito.","ordem superior.","dever legal."],"Art. 1º, § 1º.")
q(3,"A ação penal privada é admitida se a pública não for intentada no prazo legal, cabendo ao Ministério Público, entre outras coisas, retomar a ação a todo tempo no caso de negligência do",["querelante.","querelado.","juiz.","delegado.","testemunha."],"Art. 3º, § 1º.")
q(3,"A reparação de danos tem valor mínimo fixado pelo juiz na",["sentença.","denúncia.","queixa.","portaria.","súmula."],"Art. 4º, I.")
q(3,"Nos termos do art. 8º, a sentença penal que reconhecer o estado de necessidade faz coisa julgada no âmbito",["cível e administrativo-disciplinar.","somente criminal.","somente eleitoral.","somente tributário.","somente trabalhista."],"Art. 8º.")
q(3,"A suspensão do exercício do cargo como pena restritiva tem o prazo de",["um a seis meses, com perda dos vencimentos.","um a cinco anos.","seis a doze meses, sem perda.","dois a oito anos.","dez dias."],"Art. 5º, II.")
q(3,"O sujeito ativo abrange agente público de qualquer dos Poderes da União, dos Estados, do Distrito Federal, dos Municípios e de",["Território.","Condomínio.","Associação.","Sindicato.","Empresa privada."],"Art. 2º.")
q(3,"Os efeitos do art. 4º, incisos II e III, são condicionados à reincidência e dependem de declaração motivada na",["sentença.","denúncia.","portaria.","súmula.","queixa."],"Art. 4º, parágrafo único.")
q(3,"O art. 6º dispõe que as penas serão aplicadas independentemente das sanções de natureza",["civil ou administrativa cabíveis.","penal.","militar.","tributária.","eleitoral."],"Art. 6º.")
q(3,"A coisa julgada do art. 8º ocorre quando o ato foi praticado em estrito cumprimento de dever legal, em legítima defesa, estado de necessidade ou exercício regular de",["direito.","cargo.","poder.","mandato.","emprego."],"Art. 8º.")
q(3,"No texto do capricho do agente, o ato do guarda configura crime porque há a finalidade de",["humilhar por capricho, sem motivo legal.","cumprir ordem legítima.","aplicar a lei.","proteger terceiros.","salvar uma vida."],"Art. 1º, § 1º.","abuso1a")
q(3,"No texto do capricho do agente, o guarda, além da esfera penal, pode responder nas esferas civil e",["administrativa.","tributária.","eleitoral.","trabalhista.","militar."],"Art. 6º.","abuso1a")
q(3,"No texto da divergência de interpretação, a conduta do guarda não é crime porque não há",["finalidade específica de prejudicar ou capricho.","lei.","vítima.","Município.","autuação."],"Art. 1º, §§ 1º e 2º.","abuso1b")
q(3,"No texto da divergência de interpretação, o superior considerou a interpretação equivocada, o que indica a hipótese de divergência na interpretação de",["lei.","contrato.","preço.","horário.","salário."],"Art. 1º, § 2º.","abuso1b")
q(3,"No texto da condenação por abuso, a perda do cargo foi decretada porque o agente era",["reincidente em crime de abuso de autoridade.","primário.","absolvido.","aposentado.","estrangeiro."],"Art. 4º, parágrafo único.","abuso1c")
q(3,"No texto da condenação por abuso, a decisão do juiz sobre a perda do cargo exige que seja",["declarada motivadamente na sentença.","verbal.","tácita.","automática.","genérica."],"Art. 4º, parágrafo único.","abuso1c")
q(3,"No texto da condenação por abuso, além da perda do cargo, o juiz pode fixar a inabilitação por um a",["cinco anos.","dois anos.","três anos.","dez anos.","seis meses."],"Art. 4º, II.","abuso1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Abuso de autoridade: arts. 1º a 8º",[
 ("con","Conceito",["agente público","abuso do poder","pretexto de exercer função"],"seção 1"),
 ("dol","Dolo específico",["prejudicar outrem","beneficiar a si ou a terceiro","capricho"],"seção 1"),
 ("suj","Sujeitos",["qualquer agente público","todos os Poderes","ainda sem remuneração"],"seção 1"),
 ("efe","Efeitos da condenação",["indenização","inabilitação: 1 a 5 anos","perda do cargo: reincidência"],"seção 2"),
 ("pen","Penas restritivas",["serviços à comunidade","suspensão: 1 a 6 meses"],"seção 2"),
 ("ind","Independência",["civil e administrativa","coisa julgada nas excludentes"],"seção 3")],
 "Na prova: dolo específico, divergência não é abuso, 1 a 5 anos")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o conceito e os sujeitos; as demais, os efeitos da condenação, as penas restritivas e a independência das esferas.","Fontes: Edital 02/2026, Anexo I; Lei 13.869/2019 (Abuso de Autoridade), arts. 1º a 8º, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("abuso-1","Abuso de autoridade: disposições gerais, efeitos e sanções (arts. 1º a 8º)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (1º a 8º). O art. 3º, § 2º e o art. 5º, III aparecem vetados ou fora da citação."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Trechos de lei copiados de fontes/abuso.txt por programa.","Casos abuso1a, abuso1b e abuso1c fictícios."],
 fontes_conferidas=["Lei 13.869/2019, arts. 1º a 8º: texto da Câmara, copiado por programa."])
gravar("abuso-1",aula_html,banco("abuso-1",Q),tx)
