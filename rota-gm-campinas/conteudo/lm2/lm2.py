import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='lm_dec.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Decreto Municipal 21.019/2020 regulamenta o Programa de Avaliação Probatória dos servidores de Campinas e é a parte do edital que mais atinge o guarda recém-empossado: o estágio dura três anos, tem seis avaliações semestrais e exige nota mínima de 70%. O decreto até cita o Guarda Municipal (art. 4º, § 2º): a avaliação é feita pelo superior hierárquico em conjunto com a comissão interna nomeada pelo Secretário da Pasta. A Vunesp cobra números (três anos, seis semestres, 70 pontos, 12 faltas, 15 dias, quatro anos de mandato da comissão) e os critérios de avaliação."
S={}
S[1]="## 1. Programa, estágio e critérios\n\n"+L("art. 1º","Art. 1º Fica instituído","Art. 2º")+"\n\n"+L("art. 2º","Art. 2º A avaliação probatória","Art. 3º")+"\n\n"+L("art. 3º","Art. 3º Os critérios","Art. 4º")+"\n\n"+L("art. 4º","Art. 4º Será de responsabilidade","Art. 5º")+"\n\n"+L("art. 6º","Art. 6º As avaliações semestrais","Art. 7º")+"""

O Programa de Avaliação Probatória visa a aferir a aptidão do servidor admitido por concurso, com o objetivo final de aquisição de estabilidade (art. 41, § 4º, da Constituição). O estágio probatório dura os três anos iniciais de efetivo exercício, ressalvadas as suspensões, e é composto por seis avaliações semestrais, cada uma com planejamento, acompanhamento e avaliação, dando-se ciência ao servidor. Os critérios são: avaliação de desempenho no cargo, eficiência, disciplina, subordinação, dedicação ao serviço, ética e boa conduta, liderança, proatividade, assiduidade e pontualidade e aptidão física e/ou mental.

O superior hierárquico planeja, acompanha e avalia o servidor. Para os servidores do cargo de Guarda Municipal, a avaliação é feita pelo superior hierárquico em conjunto com a comissão interna nomeada pelo Secretário da Pasta. Os seis períodos avaliativos encerram-se no último dia do 6º, 12º, 18º, 24º, 30º e 36º meses de efetivo exercício.
"""
S[2]="## 2. Instrumento, nota e autoavaliação\n\n"+L("art. 7º","Art. 7º O servidor estagiário será avaliado","Art. 8º")+"\n\n"+L("art. 9º","Art. 9º No tópico","Art. 10.")+"\n\n"+L("art. 10","Art. 10. O servidor estagiário deverá acessar","Art. 11.")+"\n\n"+L("art. 11","Art. 11. Havendo discordância","Art. 12.")+"\n\n"+L("art. 12","Art. 12. A avaliação do servidor","Art. 13.")+"""

O instrumento de avaliação é elaborado pela Secretaria Municipal de Recursos Humanos e eletrônico, composto dos formulários de planejamento e de avaliação, com os tópicos Desempenho no Cargo, Competências, Assiduidade e Pontualidade e Aptidão Física e/ou Mental. Os pesos somam 100 pontos, e a nota de cada atividade e competência, de 0 a 100, é convertida em pontos pelo peso. Se a nota do período ficar abaixo de 70 pontos, o superior deve justificá-la. É obrigatório apontar no mínimo quatro competências no período, e a Liderança é obrigatória para cargos com responsabilidade técnica sobre outros servidores.

O servidor registra no sistema ciência e concordância ou discordância em cinco dias corridos, sob pena de concordância tácita. Havendo discordância, pode fazer autoavaliação em quinze dias corridos, analisada apenas se a nota estiver abaixo de 70 pontos com discordância expressa ou se a avaliação não seguir a legislação. Para ser aprovado e adquirir a estabilidade, o servidor deve alcançar aproveitamento de 70% do total de pontos na média final.
"""
S[3]="## 3. Exoneração, faltas, avaliação ocupacional e comissão\n\n"+L("art. 18","Art. 18. O servidor estagiário poderá ter","§ 1º A recomendação")+"\n\n"+L("art. 19","Art. 19. O servidor estagiário que, durante o período avaliativo","§ 1º O disposto no caput")+"\n\n"+L("art. 23, caput e § 1º","Art. 23. O servidor estagiário poderá ser encaminhado","§ 2º O encaminhamento")+"\n\n"+L("art. 25","Art. 25. O servidor que não obtiver","Art. 26.")+"\n\n"+L("art. 29","Art. 29. Será suspenso","Art. 30.")+"\n\n"+L("art. 35","Art. 35. Fica instituída","Art. 36.")+"""

A exoneração do estagiário pode ser recomendada por insuficiência de desempenho, por mais de 12 faltas injustificadas, consecutivas ou não (jornada de 36 horas semanais, proporcionalizada nas demais), ou por incompatibilidade de aptidão física ou mental. A recomendação depende da avaliação da Comissão Permanente de Avaliação Probatória, com ampla defesa e contraditório. Quem se ausentar injustificadamente por mais de dois dias no período avaliativo perde a pontuação do respectivo período, pelo critério de assiduidade. O estagiário que ultrapassar 120 dias de afastamento para tratamento de saúde é encaminhado para avaliação ocupacional probatória, feita por equipe multiprofissional de no mínimo três membros, um deles médico.

Quem não obtiver conceito favorável pode apresentar defesa escrita em 15 dias, e o recurso fora do prazo é intempestivo. O ato de exoneração é fundamentado e dado pelo Chefe do Poder Executivo, por portaria no Diário Oficial. Suspendem o estágio o exercício de funções estranhas ao cargo, as licenças, faltas e afastamentos legais, as suspensões disciplinares e a nomeação para cargo em comissão ou função de confiança sem compatibilidade. A Comissão Permanente é nomeada pelo Prefeito, com mandato de quatro anos, e composta por cinco servidores efetivos estáveis (três titulares e dois suplentes).
"""
S[5]="""## 5. Na rotina do guarda

- **Estágio de três anos:** o guarda recém-empossado é avaliado em seis semestres; só adquire estabilidade com média de 70%.
- **Avaliação do guarda:** feita pelo superior hierárquico com a comissão interna nomeada pelo Secretário da Pasta.
- **Ciência em cinco dias:** o guarda registra no sistema ciência e concordância ou discordância em cinco dias corridos; calado, a concordância é tácita.
- **Faltas:** mais de doze faltas injustificadas podem levar à recomendação de exoneração; mais de dois dias de ausência injustificada fazem perder a pontuação do período.
- **Proibições no estágio:** não há alteração de lotação, licença para estudo e cessão funcional, salvo relevante interesse público.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Duração do estágio | Três anos de efetivo exercício |
| Avaliações | Seis, semestrais |
| Nota mínima | 70 pontos por período; média final de 70% |
| Competências obrigatórias | Mínimo de quatro; Liderança para cargos com responsabilidade técnica |
| Ciência do servidor | Cinco dias corridos; concordância tácita |
| Autoavaliação | Quinze dias corridos |
| Faltas para exoneração | Mais de doze injustificadas |
| Perda da pontuação | Mais de dois dias de ausência injustificada no período |
| Avaliação ocupacional | Após 120 dias de afastamento para saúde |
| Defesa escrita | Quinze dias |
| Mandato da comissão | Quatro anos; cinco servidores efetivos estáveis |
| Guarda Municipal | Superior hierárquico e comissão interna do Secretário |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Programa de Avaliação Probatória |
| Art. 2º | Três anos; seis avaliações semestrais |
| Art. 3º | Dez critérios |
| Art. 4º | Superior hierárquico; Guarda: com comissão interna |
| Art. 6º | Períodos: 6º, 12º, 18º, 24º, 30º e 36º mês |
| Art. 7º | Instrumento eletrônico; pesos somam 100; mínimo de 70 |
| Art. 10 | Ciência em 5 dias |
| Art. 11 | Autoavaliação em 15 dias |
| Art. 12 | Aprovação com 70% |
| Art. 18 | Exoneração: desempenho, mais de 12 faltas, inaptidão |
| Art. 25 | Defesa em 15 dias |
| Art. 35 | Comissão: 4 anos, 5 servidores |
"""
QR=[("Questão 1","O estágio probatório ocorrerá durante os três anos iniciais de efetivo exercício e será composto de avaliações",["semestrais, em número de seis.","anuais, em número de três.","trimestrais, em número de doze.","mensais.","bianuais."],0,"Art. 2º, §§ 1º e 3º."),
("Questão 2","Para ser aprovado e adquirir a estabilidade, o servidor deve alcançar aproveitamento, na média final, de",["setenta por cento do total de pontos.","cinquenta por cento.","sessenta por cento.","oitenta por cento.","noventa por cento."],1,"Art. 12."),
("Questão 3","A avaliação probatória dos servidores do cargo de Guarda Municipal será realizada pelo superior hierárquico em conjunto com a comissão interna nomeada pelo",["Secretário da Pasta.","Prefeito.","Vereador.","Corregedor.","Comandante da PM."],2,"Art. 4º, § 2º."),
("Questão 4","A Comissão Permanente de Avaliação Probatória tem mandato de",["quatro anos.","dois anos.","um ano.","três anos.","cinco anos."],3,"Art. 35.")]
t1="<strong>Guarda em estágio</strong><br><br>Um guarda municipal de Campinas, no segundo semestre do estágio, recebeu nota 65 na avaliação do período e discorda da avaliação."
t2="<strong>Faltas do estagiário</strong><br><br>Um guarda em estágio, com jornada de 36 horas semanais, acumulou 13 faltas injustificadas ao longo do estágio."
t3="<strong>Afastamento prolongado</strong><br><br>Um servidor em estágio probatório ficou afastado por tratamento de saúde, de forma intercalada, por 130 dias."
tx={"lm2a":t1,"lm2b":t2,"lm2c":t3}
# n=1
q(1,"O Programa de Avaliação Probatória visa a aferir a aptidão do servidor admitido por concurso público, tendo como objetivo final a aquisição de",["estabilidade no cargo ocupado.","aposentadoria.","promoção.","licença.","gratificação."],"Art. 1º.")
q(1,"A avaliação probatória tem como finalidade a eficiência nos serviços prestados pela Prefeitura Municipal de",["Campinas.","Valinhos.","Sumaré.","Hortolândia.","Paulínia."],"Art. 2º.")
q(1,"O estágio probatório ocorrerá durante os iniciais",["três anos de efetivo exercício.","dois anos.","um ano.","quatro anos.","cinco anos."],"Art. 2º, § 1º.")
q(1,"O estágio probatório será composto de avaliações semestrais em número de",["seis.","três.","quatro.","oito.","doze."],"Art. 2º, § 3º.")
q(1,"Cada semestre avaliativo terá as etapas de planejamento, acompanhamento e",["avaliação.","julgamento.","punição.","promoção.","registro."],"Art. 2º, § 4º.")
q(1,"Entre os critérios de avaliação está a eficiência e a",["disciplina.","fama.","renda.","simpatia.","origem."],"Art. 3º, III.")
q(1,"Entre os critérios de avaliação está a ética e boa",["conduta.","aparência.","origem.","fama.","sorte."],"Art. 3º, VI.")
q(1,"Entre os critérios de avaliação está a aptidão física e/ou",["mental.","financeira.","social.","política.","legal."],"Art. 3º, X.")
q(1,"A avaliação do servidor estagiário é de responsabilidade do superior",["hierárquico.","imediato apenas.","remoto.","sindical.","político."],"Art. 4º.")
q(1,"O 1º período avaliativo vai até o último dia do",["6º mês de efetivo exercício.","12º mês.","3º mês.","18º mês.","24º mês."],"Art. 6º, I.")
q(1,"O 6º período avaliativo vai até o último dia do",["36º mês de efetivo exercício.","30º mês.","24º mês.","18º mês.","12º mês."],"Art. 6º, VI.")
q(1,"O instrumento de avaliação probatória é elaborado pela Secretaria Municipal de",["Recursos Humanos.","Saúde.","Educação.","Segurança.","Finanças."],"Art. 7º.")
q(1,"Na avaliação, as notas de cada atividade e competência variam de zero a",["cem.","dez.","cinquenta.","mil.","setenta."],"Art. 7º, § 5º, I.")
q(1,"Caso o desempenho não alcance a nota mínima de setenta pontos no período, o superior deverá",["justificá-la em campo específico.","anulá-la.","promover o servidor.","ignorá-la.","exonerar o servidor."],"Art. 7º, § 6º.")
q(1,"No tópico Competências será obrigatório o apontamento de, no mínimo,",["quatro competências.","duas competências.","três competências.","cinco competências.","dez competências."],"Art. 9º, § 1º.")
q(1,"A ciência do servidor sobre o instrumento é registrada no prazo máximo de",["cinco dias corridos.","dez dias corridos.","quinze dias corridos.","trinta dias corridos.","dois dias úteis."],"Art. 10.")
q(1,"A autoavaliação deve ser preenchida no prazo máximo de",["quinze dias corridos.","cinco dias.","dez dias.","trinta dias.","dois dias."],"Art. 11, § 2º.")
q(1,"No texto do guarda em estágio, a nota de 65 pontos é inferior à mínima de",["setenta pontos.","sessenta pontos.","oitenta pontos.","cinquenta pontos.","noventa pontos."],"Art. 7º, § 6º.","lm2a")
q(1,"No texto das faltas do estagiário, o limite de faltas injustificadas para a jornada de 36 horas é de",["doze.","cinco.","dez.","quinze.","vinte."],"Art. 18, II.","lm2b")
q(1,"No texto do afastamento prolongado, o servidor que ultrapassar cento e vinte dias de afastamento é encaminhado para avaliação",["ocupacional probatória.","especial de desempenho.","disciplinar.","fiscal.","psicológica."],"Art. 23, § 1º.","lm2c")
# n=2
q(2,"O estágio probatório é regulado nos termos do § 4º do art. 41 da",["Constituição Federal.","Constituição Estadual.","Lei Orgânica.","Lei 1.399/1955, apenas.","Lei de Licitações."],"Art. 1º.")
q(2,"Durante o estágio probatório apurar-se-ão a aptidão, a conduta e o comportamento do servidor para determinar a sua permanência ou não no serviço",["público.","privado.","militar.","rural.","comercial."],"Art. 2º, § 2º.")
q(2,"O critério da subordinação refere-se ao respeito à hierarquia e ao acatamento das requisições de",["tarefas.","dinheiro.","viagens.","horários.","cargos."],"Art. 3º, IV.")
q(2,"O critério da liderança consiste em motivar e influenciar os liderados, de forma ética e positiva, para os objetivos da equipe e da",["organização.","imprensa.","família.","igreja.","praça."],"Art. 3º, VII.")
q(2,"O superior hierárquico é o responsável pela gestão da unidade de trabalho a que o servidor estagiário estiver",["vinculado.","contrário.","isolado.","exonerado.","indicado."],"Art. 4º, § 1º.")
q(2,"O servidor que trabalhou sob mais de um superior será avaliado por aquele que por último assumiu a gestão da",["unidade.","carreira.","escola.","cidade.","secretaria."],"Art. 4º, § 4º.")
q(2,"O instrumento de avaliação será composto dos formulários de planejamento e de avaliação",["probatória.","pessoal.","disciplinar.","fiscal.","médica."],"Art. 7º, § 1º.")
q(2,"O superior hierárquico poderá incluir equipe de até quatro membros no ato do",["planejamento das atividades e competências.","julgamento.","concurso.","recurso.","sorteio."],"Art. 7º, § 3º.")
q(2,"Os pesos, no planejamento, devem ser pontuados de 0 a 100 pontos, e a soma dos pesos deverá ser igual a",["cem pontos.","dez pontos.","setenta pontos.","cinquenta pontos.","mil pontos."],"Art. 7º, § 4º.")
q(2,"A Liderança é obrigatória nos cargos que demandem grau de responsabilidade técnica sobre outros",["servidores.","processos.","bens.","contratos.","veículos."],"Art. 9º, § 2º.")
q(2,"O servidor que não registrar sua ciência terá sua concordância",["tácita registrada.","negada.","dispensada.","adiada.","suspensa."],"Art. 10, parágrafo único.")
q(2,"A autoavaliação somente será analisada quando a nota do período estiver abaixo de",["setenta pontos, com discordância expressa.","sessenta pontos.","oitenta pontos.","cinquenta pontos.","noventa pontos."],"Art. 11, § 4º, I.")
q(2,"O superior hierárquico preenche e disponibiliza o instrumento ao servidor em até dez dias",["corridos.","úteis.","decorridos de um ano.","por sorteio.","no mês seguinte."],"Art. 13, § 1º.")
q(2,"A exoneração pode ser recomendada por insuficiência de desempenho, por mais de doze faltas injustificadas ou por incompatibilidade de aptidão física ou",["mental.","financeira.","social.","política.","etária."],"Art. 18, III.")
q(2,"O estagiário que se ausentar injustificadamente por mais de dois dias perde a pontuação do respectivo período em razão do critério de assiduidade e",["pontualidade.","simpatia.","fama.","origem.","renda."],"Art. 19.")
q(2,"A equipe multiprofissional da avaliação ocupacional é composta por no mínimo três membros, sendo um deles",["médico.","advogado.","psicólogo.","engenheiro.","administrador."],"Art. 23, § 4º.")
q(2,"Quem não obtiver conceito favorável poderá protocolizar defesa escrita no prazo de",["quinze dias.","cinco dias.","dez dias.","trinta dias.","dois dias."],"Art. 25.")
q(2,"No texto do guarda em estágio, a autoavaliação só será analisada se a nota for inferior a setenta pontos e houver ciência e discordância",["expressa do servidor.","tácita.","do superior.","do prefeito.","da imprensa."],"Art. 11, § 4º, I.","lm2a")
q(2,"No texto das faltas do estagiário, a exoneração só se dá após avaliação da",["Comissão Permanente de Avaliação Probatória.","Câmara.","imprensa.","vizinhança.","empresa."],"Art. 18, § 1º.","lm2b")
q(2,"No texto do afastamento prolongado, a avaliação ocupacional ocorrerá ainda que o servidor esteja afastado para",["tratamento de saúde.","férias.","estudo.","viagem.","lazer."],"Art. 23, § 6º.","lm2c")
# n=3
q(3,"Assinale a alternativa correta sobre o estágio probatório regulado pelo Decreto 21.019/2020.",["Três anos, seis avaliações semestrais, média final de 70% para a estabilidade.","Um ano, duas avaliações anuais.","Dois anos, quatro avaliações.","Três anos, três avaliações.","Quatro anos, oito avaliações."],"Arts. 2º e 12.")
q(3,"Considere. I. O guarda é avaliado pelo superior hierárquico com a comissão interna nomeada pelo Secretário. II. A ciência é registrada em dez dias. III. A comissão permanente tem mandato de quatro anos. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A ciência é em cinco dias corridos (art. 10).")
q(3,"Assinale a INCORRETA.",["A Comissão Permanente é composta por dez servidores.","A Comissão é nomeada pelo Prefeito.","O mandato é de quatro anos.","São três titulares e dois suplentes.","Os integrantes são servidores efetivos estáveis."],"São cinco servidores: três titulares e dois suplentes (art. 35).")
q(3,"A exoneração do servidor em estágio, com base na decisão que concluir pela sua desaprovação, dá-se pelo Chefe do Poder Executivo, através de portaria publicada no",["Diário Oficial do Município.","jornal local.","mural da secretaria.","sítio da escola.","rádio."],"Art. 26.")
q(3,"O servidor que não comparecer para ciência do parecer será convocado por publicação no Diário Oficial por três dias úteis",["consecutivos.","alternados.","semanais.","mensais.","eventuais."],"Art. 27.")
q(3,"A nomeação para cargo em comissão ou função de confiança leva à suspensão automática do cômputo do estágio, que será retomado se as atividades forem compatíveis com as do cargo de provimento",["efetivo.","temporário.","comissionado.","político.","eventual."],"Art. 28, VII.")
q(3,"Não será permitido ao servidor em estágio probatório a alteração de lotação, a licença para estudo ou missão e a cessão",["funcional.","particular.","parcial.","temporária.","interna."],"Art. 30.")
q(3,"A exoneração a pedido do servidor em processo de avaliação especial não obsta a conversão em exoneração pela Comissão, se a análise concluir pela sua",["inaptidão.","aptidão.","aposentadoria.","promoção.","licença."],"Art. 32.")
q(3,"Ao término do período probatório, com a aprovação, a Comissão publica a homologação no",["Diário Oficial do Município.","mural.","jornal.","rádio.","sítio privado."],"Art. 34.")
q(3,"A suspensão do estágio probatório resulta, entre outros casos, de suspensões",["disciplinares.","de lazer.","sindicais.","voluntárias.","ocasionais."],"Art. 29, III.")
q(3,"No caso de suspensão do estágio, a contagem será retomada quando do retorno ao efetivo exercício, aproveitando-se o período que",["antecedeu o fato que motivou a suspensão.","sucedeu.","foi perdido.","for escolhido.","for compensado."],"Art. 29, § 1º.")
q(3,"O prazo da defesa escrita do art. 25 conta-se a partir da ciência oficial, excluindo-se o dia do começo e incluindo-se o do",["vencimento.","início.","feriado.","domingo.","registro."],"Art. 25, § 1º.")
q(3,"O prazo da defesa escrita do art. 25 conta-se de modo",["contínuo.","descontínuo.","suspenso.","parcial.","mensal."],"Art. 25, § 3º.")
q(3,"A Comissão Permanente deve encaminhar à Junta Médica Oficial os recursos referentes a processos de inaptidão física e/ou",["mental.","financeira.","social.","política.","legal."],"Art. 17, IV.")
q(3,"No texto do guarda em estágio, a nota de 65 exige que o superior hierárquico justifique a nota em campo específico, anexando documentos, quando for o",["caso.","dever.","pedido.","prazo.","laudo."],"Art. 7º, § 6º.","lm2a")
q(3,"No texto do guarda em estágio, a avaliação do guarda é realizada pelo superior hierárquico e pela comissão interna nomeada pelo(a)",["Secretário(a) da Pasta.","Prefeito(a).","Vereador(a).","Comandante.","Juiz(a)."],"Art. 4º, § 2º.","lm2a")
q(3,"No texto das faltas do estagiário, as 13 faltas excedem o limite de doze, e a recomendação de exoneração exige ampla defesa e",["contraditório.","sigilo.","silêncio.","anistia.","prescrição."],"Art. 18, § 1º.","lm2b")
q(3,"No texto das faltas do estagiário, o limite de doze faltas é proporcionalizado nas jornadas",["diferenciadas.","iguais.","maiores apenas.","noturnas apenas.","festivas."],"Art. 18, § 2º.","lm2b")
q(3,"No texto do afastamento prolongado, o afastamento de 130 dias, consecutivos ou não, supera o limite de",["cento e vinte dias.","noventa dias.","trinta dias.","sessenta dias.","cento e oitenta dias."],"Art. 23, § 1º.","lm2c")
q(3,"No texto do afastamento prolongado, o encaminhamento à avaliação ocupacional é feito pela",["Comissão Permanente de Avaliação Probatória.","própria chefia.","Câmara.","imprensa.","vizinhança."],"Art. 23, § 2º.","lm2c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Decreto 21.019/2020: avaliação probatória",[
 ("est","Estágio",["3 anos","6 avaliações semestrais","70% para a estabilidade"],"seção 1"),
 ("cri","Critérios",["dez critérios","eficiência, disciplina, ética","assiduidade, aptidão"],"seção 1"),
 ("sup","Superior hierárquico",["planeja e avalia","Guarda: com comissão interna","do Secretário da Pasta"],"seção 1"),
 ("ins","Instrumento",["pesos somam 100","nota mínima: 70","ciência: 5 dias"],"seção 2"),
 ("exo","Exoneração",["mais de 12 faltas","insuficiência de desempenho","inaptidão"],"seção 3"),
 ("com","Comissão",["mandato de 4 anos","5 servidores","homologação"],"seção 3")],
 "Na prova: 3 anos, 6 avaliações, 70%, 12 faltas, 5 e 15 dias")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o estágio e os critérios; as demais, o instrumento de avaliação, a exoneração e a comissão.","Fontes: Edital 02/2026, Anexo I; Decreto Municipal 21.019/2020 (Campinas), texto de consulta da Câmara Municipal de Campinas (SAPL). Exemplos criados para a aula.")
revisao("lm-2","Programa de Avaliação Probatória (Decreto 21.019/2020)",Q,list(tx),
 cobertura=["Arts. 1º a 4º, 6º, 7º, 9º a 12, 17 a 19, 23, 25 a 30, 32, 34, 35. Não detalhados: arts. 5º, 8º, 13 a 16, 20 a 22, 24, 31, 33, 36 em diante e os anexos."],
 pendencias=["Texto-fonte: texto de consulta da Câmara Municipal de Campinas (SAPL), baixado em 14/11/2026; reconferir no Diário Oficial do Município.","Decretos posteriores podem ter alterado o texto; conferir no portal oficial.","Casos lm2a, lm2b e lm2c fictícios."],
 fontes_conferidas=["Decreto 21.019/2020: texto do SAPL, copiado por programa."])
gravar("lm-2",aula_html,banco("lm-2",Q),tx)
