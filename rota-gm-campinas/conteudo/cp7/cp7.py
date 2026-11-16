import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O furto é o crime contra o patrimônio mais frequente e, por isso, o mais cobrado. A Vunesp cobra o art. 155 pelo conceito (subtrair coisa alheia móvel, sem violência), pelo repouso noturno, pelo furto privilegiado, pelas qualificadoras e pelas modalidades novas, de pena maior, como o furto de celular, de cabos e de combustíveis. O art. 156, do furto de coisa comum, completa o tema. A aula segue o texto consolidado, que tem muitos parágrafos, e organiza o que a prova costuma trocar: pena, qualificadora e aumento."
S={}
S[1]="## 1. O furto simples e seus ajustes\n\n"+L("art. 155, caput","Art. 155. Subtrair, para si ou para outrem","§ 1º A pena aumenta-se de metade")+"""

Furtar é subtrair, para si ou para outrem, coisa alheia móvel, e a pena é de reclusão de um a seis anos e multa. Cada palavra decide: “subtrair” é tirar sem violência ou ameaça (com violência já é roubo); “coisa alheia” é a que pertence a outra pessoa; “móvel” é a que pode ser transportada, o que exclui o imóvel, mas inclui o que, por natureza, é removível, e o § 3º equipara a coisa móvel a energia elétrica ou qualquer outra que tenha valor econômico. O dolo inclui a intenção de ter a coisa para si ou para outrem.

"""+L("art. 155, § 1º","§ 1º A pena aumenta-se de metade","§ 2º Se o criminoso")+"\n\n"+L("art. 155, § 2º","§ 2º Se o criminoso é primário","§ 3º Equipara-se")+"""

O repouso noturno aumenta a pena de metade, porque a vigilância é menor e o crime é mais fácil de praticar à noite. Já o furto privilegiado (§ 2º) premia o criminoso primário que subtrai coisa de pequeno valor: o juiz pode substituir a reclusão pela detenção, diminuir a pena de um a dois terços ou aplicar somente a multa. Os dois requisitos são cumulativos: primário e pequeno valor da coisa.
"""
S[2]="## 2. Furto qualificado\n\n"+L("art. 155, § 4º","§ 4º A pena é de reclusão, de 2 (dois) a 8 (oito) anos","§ 4º-A.")+"""

O furto qualificado tem reclusão de dois a oito anos e multa. Qualificam o furto o rompimento ou a destruição de obstáculo à subtração, o abuso de confiança ou a fraude, a escalada ou a destreza, a chave falsa, o concurso de duas ou mais pessoas e a subtração de bens que comprometam o funcionamento de órgãos públicos ou de estabelecimentos que prestem serviços essenciais.

"""+L("art. 155, § 4º-A","§ 4º-A. A pena é de reclusão de 4","§ 4º-B.")+"\n\n"+L("art. 155, §§ 4º-B e 4º-C","§ 4º-B. A pena é de reclusão","§ 5º A pena é de reclusão")+"""

Há figuras qualificadas de pena maior. O emprego de explosivo ou artefato análogo que cause perigo comum leva a reclusão de quatro a dez anos e multa. O furto mediante fraude por dispositivo eletrônico ou informático, o chamado furto eletrônico, tem a mesma pena de quatro a dez anos, com aumento se o crime usa servidor fora do território nacional ou se é contra idoso ou vulnerável.
"""
S[3]="## 3. Subtrações de pena maior e a energia, os fios e os combustíveis\n\n"+L("art. 155, §§ 5º a 7º","§ 5º A pena é de reclusão","§ 8º A pena é de reclusão")+"\n\n"+L("art. 155, §§ 8º e 9º","§ 8º A pena é de reclusão","§ 10.")+"""

A pena é de reclusão de quatro a dez anos e multa se o veículo automotor subtraído é transportado para outro Estado ou para o exterior, se a subtração é de semovente domesticável de produção ou de animal doméstico, de aparelho de telefonia celular, de computador ou dispositivo eletrônico semelhante, de substâncias explosivas ou de arma de fogo. A subtração de fios, cabos ou equipamentos de fornecimento de energia elétrica, telefonia ou transferência de dados, e de materiais ferroviários ou metroviários, tem reclusão de dois a oito anos e multa, e aplica-se a eles o privilégio do § 2º. Se o furto é cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, a pena é de quatro a dez anos.

"""+L("art. 155, § 10","§ 10. A pena é de reclusão","Furto de coisa comum")+"""

Os §§ 10 a 12 tratam do furto de combustíveis: reclusão de quatro a dez anos e multa, aumentada de um terço se há destruição, concurso, abuso de confiança ou vínculo com o ente lesado, ou se praticado por ocupante de cargo, emprego ou função pública, e de dois terços se resulta suspensão das atividades, desabastecimento, incêndio, poluição, lesão grave ou morte.
"""
S[4]="## 4. Furto de coisa comum\n\n"+L("art. 156","Art. 156. Subtrair o condômino","CAPÍTULO II")+"""

O art. 156 trata do condômino, co-herdeiro ou sócio que subtrai coisa comum de quem legitimamente a detém. A pena é de detenção de seis meses a dois anos, ou multa, e só se procede mediante representação. Não é punível a subtração de coisa comum fungível cujo valor não exceda a quota a que o agente tem direito. Isso mostra que a lei trata de modo diferente quem toma o que, em parte, já é seu.
"""
S[6]="""## 6. Na rotina do guarda

- **Flagrante de furto:** a pessoa encontrada subtraindo coisa alheia está em flagrante, e o guarda a conduz ao delegado com o objeto e as testemunhas.
- **Furto de fios e cabos:** a subtração de fios e cabos de energia e telefonia, comum nas cidades, tem pena de dois a oito anos e afeta serviços essenciais.
- **Furto de celular:** pena de quatro a dez anos, e merece registro cuidadoso do aparelho e do local.
- **Furto de bicicleta ou objeto de pequeno valor por primário:** pode caber o privilégio do § 2º; o guarda não decide, mas relata os fatos que o juiz considerará.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do furto simples | Reclusão de um a seis anos, e multa |
| Pena do furto qualificado | Reclusão de dois a oito anos, e multa |
| Repouso noturno | Aumenta a pena de metade, no furto simples (§ 1º) |
| Privilégio: pequeno valor ou primário | Os dois requisitos juntos |
| Celular e arma de fogo | Reclusão de quatro a dez anos, e multa (§ 6º e § 7º) |
| Fios e cabos | Reclusão de dois a oito anos, com possibilidade de privilégio |
| Furto de coisa comum | Detenção de seis meses a dois anos, ou multa; representação |
| Furto com violência | Não é furto: é roubo |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Furto simples | Reclusão, 1 a 6 anos, e multa |
| Repouso noturno | Aumento de metade |
| Privilegiado | Primário e pequeno valor: detenção, redução de 1/3 a 2/3, ou só multa |
| Qualificado | Reclusão, 2 a 8 anos, e multa |
| Explosivo | Reclusão, 4 a 10 anos, e multa |
| Furto eletrônico | Reclusão, 4 a 10 anos, e multa |
| Veículo para outro Estado; celular; arma | Reclusão, 4 a 10 anos, e multa |
| Fios e cabos | Reclusão, 2 a 8 anos, e multa |
| Coisa comum | Detenção, 6 meses a 2 anos, ou multa; representação |
"""
QR=[("Questão 1","A pena do furto simples é de",["reclusão, de um a seis anos, e multa.","reclusão, de dois a oito anos, e multa.","detenção, de um a seis anos.","reclusão, de quatro a dez anos.","detenção, de seis meses a dois anos."],0,"Art. 155, caput."),
("Questão 2","Se o furto é praticado durante o repouso noturno, a pena é",["aumentada de metade.","aumentada de um terço.","dobrada.","aumentada de um sexto.","mantida."],2,"Art. 155, § 1º."),
("Questão 3","O furto cometido mediante concurso de duas ou mais pessoas tem pena de",["reclusão, de dois a oito anos, e multa.","reclusão, de um a seis anos, e multa.","reclusão, de quatro a dez anos, e multa.","detenção, de seis meses a dois anos.","reclusão, de seis a dez anos."],1,"Art. 155, § 4º, IV."),
("Questão 4","A subtração de aparelho de telefonia celular tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos, e multa.","reclusão, de dois a oito anos, e multa.","detenção, de um a três anos.","reclusão, de seis a dez anos."],4,"Art. 155, § 6º, II.")]
t1="<strong>Fios furtados na avenida</strong><br><br>Em Vila Nova, cidade fictícia, dois homens foram flagrados cortando e levando fios de cobre de postes de iluminação pública, de madrugada. A Guarda Municipal os deteve e apreendeu os fios e as ferramentas. Um deles era primário, e o valor dos fios, baixo."
t2="<strong>Celular levado da mesa</strong><br><br>Um homem, em uma lanchonete, subtraiu o celular que um cliente deixou sobre a mesa, e saiu sem usar violência ou ameaça. Foi visto por uma funcionária e perseguido por uma equipe da Guarda Municipal, que o deteve."
tx={"cp7a":t1,"cp7b":t2}
# n=1
q(1,"A pena do furto simples (art. 155, caput) é de",["reclusão, de um a seis anos, e multa.","reclusão, de dois a oito anos, e multa.","detenção, de um a seis anos.","reclusão, de quatro a dez anos.","detenção, de seis meses a dois anos."],"Art. 155, caput.")
q(1,"Furtar é subtrair, para si ou para outrem,",["coisa alheia móvel.","coisa alheia imóvel.","coisa própria móvel.","qualquer coisa, com violência.","qualquer coisa própria."],"Art. 155, caput.")
q(1,"No furto praticado durante o repouso noturno, a pena aumenta-se de",["metade.","um terço.","dois terços.","um sexto.","o dobro."],"Art. 155, § 1º.")
q(1,"Equipara-se à coisa móvel, para o furto,",["a energia elétrica ou qualquer outra que tenha valor econômico.","o terreno.","a casa.","o imóvel rural.","o título de propriedade de imóvel."],"Art. 155, § 3º.")
q(1,"A pena do furto qualificado do § 4º é de",["reclusão, de dois a oito anos, e multa.","reclusão, de um a seis anos, e multa.","reclusão, de quatro a dez anos, e multa.","detenção, de dois a oito anos.","reclusão, de seis a dez anos."],"Art. 155, § 4º.")
q(1,"Qualifica o furto o crime cometido com",["destruição ou rompimento de obstáculo à subtração da coisa.","valor baixo.","autor primário.","coisa comum.","autorização do dono."],"Art. 155, § 4º, I.")
q(1,"Qualifica o furto o crime cometido com",["abuso de confiança, fraude, escalada ou destreza.","repouso noturno.","pequeno valor.","agente primário.","confissão."],"Art. 155, § 4º, II.")
q(1,"Qualifica o furto o emprego de",["chave falsa.","chave verdadeira.","violência.","ameaça.","arma branca."],"Art. 155, § 4º, III.")
q(1,"Qualifica o furto o crime cometido mediante",["concurso de duas ou mais pessoas.","um agente.","um menor.","um parente.","uma testemunha."],"Art. 155, § 4º, IV.")
q(1,"O furto com emprego de explosivo ou de artefato análogo que cause perigo comum tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de dois a oito anos.","reclusão, de um a seis anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 4º-A.")
q(1,"O furto mediante fraude, cometido por dispositivo eletrônico ou informático, tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 4º-B.")
q(1,"A subtração de veículo automotor que venha a ser transportado para outro Estado ou para o exterior tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 5º.")
q(1,"A subtração de aparelho de telefonia celular tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 6º, II.")
q(1,"A subtração de arma de fogo tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 7º, II.")
q(1,"A subtração de fios, cabos ou equipamentos de fornecimento de energia ou de telefonia tem pena de",["reclusão, de dois a oito anos, e multa.","reclusão, de quatro a dez anos.","reclusão, de um a seis anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 8º.")
q(1,"O furto de coisa comum (art. 156) é praticado por",["condômino, co-herdeiro ou sócio.","qualquer pessoa.","apenas funcionário público.","apenas herdeiro.","apenas parente."],"Art. 156, caput.")
q(1,"A pena do furto de coisa comum é de",["detenção, de seis meses a dois anos, ou multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a três anos.","multa, apenas."],"Art. 156, caput.")
q(1,"No texto dos fios, a subtração dos fios de iluminação pública configura, em tese, furto com pena de",["reclusão, de dois a oito anos, e multa.","reclusão, de quatro a dez anos.","reclusão, de um a seis anos.","detenção, de seis meses a dois anos.","reclusão, de seis a dez anos."],"Art. 155, § 8º.","cp7a")
q(1,"No texto do celular, o crime foi cometido sem violência ou ameaça, portanto trata-se de",["furto.","roubo.","extorsão.","estelionato.","apropriação indébita."],"Art. 155 e art. 157.","cp7b")
q(1,"Subtrair coisa móvel alheia, mediante grave ameaça ou violência a pessoa, é",["roubo.","furto.","extorsão.","estelionato.","apropriação indébita."],"Art. 157, caput.")
# n=2
q(2,"O furto privilegiado (§ 2º) exige que o criminoso seja primário e que a coisa furtada seja de",["pequeno valor.","valor médio.","valor elevado.","valor desconhecido.","valor histórico."],"Art. 155, § 2º.")
q(2,"No furto privilegiado, o juiz pode, entre outras medidas,",["substituir a reclusão pela detenção, diminuí-la de um a dois terços ou aplicar somente a multa.","absolver o réu.","aumentar a pena.","converter em reclusão maior.","extinguir a punibilidade."],"Art. 155, § 2º.")
q(2,"O furto qualificado pelo rompimento de obstáculo exige que o obstáculo seja rompido para",["a subtração da coisa.","o acesso à casa de terceiro.","a fuga.","a entrada de visitantes.","o ingresso de familiares."],"Art. 155, § 4º, I.")
q(2,"No furto, o abuso de confiança qualifica o crime porque",["o agente aproveita a relação de confiança com a vítima.","a vítima é idosa.","o valor é alto.","há violência.","há ameaça."],"Art. 155, § 4º, II.")
q(2,"O furto praticado mediante a subtração de bens que comprometam o funcionamento de órgãos públicos ou de estabelecimentos que prestem serviços essenciais é",["qualificado.","simples.","privilegiado.","atenuado.","atípico."],"Art. 155, § 4º, V.")
q(2,"O § 4º-C do art. 155 aumenta a pena do furto eletrônico de um terço ao dobro se o crime é praticado contra",["idoso ou vulnerável.","qualquer pessoa.","empresa.","servidor.","menor de 18 anos, apenas."],"Art. 155, § 4º-C, II.")
q(2,"O § 4º-C do art. 155 aumenta a pena do furto eletrônico de 1/3 a 2/3 se o crime é praticado mediante utilização de",["servidor mantido fora do território nacional.","computador de uso pessoal.","celular.","rede pública.","provedor local."],"Art. 155, § 4º-C, I.")
q(2,"A subtração de semovente domesticável de produção, ainda que abatido ou dividido em partes no local da subtração, tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 6º, I.")
q(2,"A subtração de substâncias explosivas ou de acessórios que possibilitem sua fabricação tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos.","reclusão, de dois a oito anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 7º, I.")
q(2,"Na subtração de fios, cabos ou equipamentos de energia ou telefonia, o § 8º ressalva a aplicação",["do § 2º do art. 155, o privilégio.","do § 1º, o repouso noturno.","do § 4º, as qualificadoras.","do art. 157.","do art. 159."],"Art. 155, § 8º.")
q(2,"O furto de combustíveis do § 10 tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de dois a oito anos.","reclusão, de um a seis anos.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 10.")
q(2,"A pena do furto de combustíveis é aumentada de um terço, entre outras hipóteses, se o crime é praticado",["por ocupante de cargo, de emprego ou de função pública.","de dia.","por um só agente.","sem destruição.","com autorização."],"Art. 155, § 11, IV.")
q(2,"A pena do furto de combustíveis é aumentada de dois terços se do crime resulta",["desabastecimento.","atraso.","demora.","inconveniência.","nenhum resultado."],"Art. 155, § 12, II.")
q(2,"No furto de coisa comum, procede-se mediante",["representação.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 156, § 1º.")
q(2,"Não é punível a subtração de coisa comum fungível cujo valor",["não exceda a quota a que tem direito o agente.","seja alto.","seja superior.","seja desconhecido.","seja histórico."],"Art. 156, § 2º.")
q(2,"Aplica-se o repouso noturno do § 1º ao furto",["simples.","apenas ao qualificado.","apenas ao privilegiado.","apenas à coisa comum.","apenas ao eletrônico."],"Art. 155, § 1º (a doutrina e a jurisprudência discutem sua aplicação ao furto qualificado).")
q(2,"No texto dos fios, o fato de um dos agentes ser primário e o valor ser baixo permite, nos termos do § 8º,",["a aplicação do privilégio do § 2º do art. 155.","a absolvição.","o aumento da pena.","a prisão preventiva obrigatória.","a extinção da punibilidade."],"Art. 155, § 8º.","cp7a")
q(2,"No texto dos fios, a subtração por dois agentes sugere ainda a incidência do",["concurso de duas ou mais pessoas, qualificadora do § 4º, IV.","repouso noturno, apenas.","privilégio, apenas.","art. 156.","art. 157."],"Art. 155, § 4º, IV.","cp7a")
q(2,"No texto do celular, a subtração do aparelho, sem violência, tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de um a seis anos, e multa.","reclusão, de dois a oito anos, e multa.","detenção, de um a quatro anos.","reclusão, de seis a doze anos."],"Art. 155, § 6º, II.","cp7b")
q(2,"A pena do furto de combustíveis, prevista no § 10, é aumentada de um terço se o crime é praticado mediante o concurso de",["duas ou mais pessoas.","uma pessoa.","três pessoas, apenas.","cinco pessoas, apenas.","qualquer número, sem aumento."],"Art. 155, § 11, II.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Furto simples: reclusão de um a seis anos e multa; qualificado: reclusão de dois a oito anos e multa; celular: reclusão de quatro a dez anos e multa.","Furto simples: reclusão de dois a oito anos; qualificado: reclusão de um a seis anos.","Furto simples: detenção de um a seis anos; celular: reclusão de dois a oito anos.","Furto simples: reclusão de quatro a dez anos; celular: detenção.","Furto simples: multa; qualificado: detenção."],"Art. 155, caput e §§ 4º e 6º.")
q(3,"Considere as afirmações. I. O repouso noturno aumenta a pena de metade, no furto simples. II. O furto privilegiado exige agente primário e coisa de pequeno valor. III. O furto de fios e cabos tem pena de quatro a dez anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"Fios e cabos: reclusão de dois a oito anos (§ 8º).")
q(3,"Assinale a INCORRETA.",["O furto de coisa comum tem pena de reclusão de um a seis anos.","O furto de arma de fogo tem pena de reclusão de quatro a dez anos, e multa.","O furto de veículo levado a outro Estado tem pena de reclusão de quatro a dez anos, e multa.","O furto qualificado tem pena de reclusão de dois a oito anos, e multa.","O furto privilegiado permite aplicar somente a pena de multa."],"O furto de coisa comum tem detenção de seis meses a dois anos, ou multa (art. 156).")
q(3,"No furto, “destreza” é a",["habilidade do agente para subtrair sem que a vítima perceba.","violência.","ameaça.","fraude.","escalada."],"Art. 155, § 4º, II.")
q(3,"No art. 155, a “escalada” qualifica o furto quando o agente",["vence obstáculo subindo ou trepando para entrar no local.","entra pela porta.","usa chave verdadeira.","entra com permissão.","entra de dia."],"Art. 155, § 4º, II.")
q(3,"O furto eletrônico do § 4º-B se caracteriza pela subtração mediante fraude cometida por",["dispositivo eletrônico ou informático, conectado ou não à rede, com ou sem a violação de mecanismo de segurança.","qualquer subtração de computador.","apenas invasão de sistemas bancários.","apenas uso de arma.","apenas uso de violência."],"Art. 155, § 4º-B.")
q(3,"No art. 155, § 12, a pena do furto de combustíveis é aumentada de dois terços se do crime resulta, entre outros,",["lesão corporal grave ou morte.","dano moral.","atraso.","inconveniência.","desprazer."],"Art. 155, § 12, V e VI.")
q(3,"No furto qualificado do § 4º, a pena mínima é de",["dois anos.","um ano.","quatro anos.","seis anos.","três anos."],"Art. 155, § 4º.")
q(3,"No furto simples, a pena máxima de reclusão é de",["seis anos.","oito anos.","dez anos.","quatro anos.","dois anos."],"Art. 155, caput.")
q(3,"A diferença entre o furto e o roubo é que, no roubo,",["há grave ameaça ou violência contra a pessoa.","a coisa é imóvel.","a coisa é comum.","a vítima é idosa.","há mais de um agente."],"Art. 157, caput.")
q(3,"No furto, o elemento subjetivo exigido é o de subtrair a coisa",["para si ou para outrem.","por brincadeira.","por culpa.","por esquecimento.","sem dolo."],"Art. 155, caput.")
q(3,"O furto de energia elétrica (o chamado “gato”) é crime porque o § 3º do art. 155",["equipara a coisa móvel a energia elétrica.","exclui a energia do crime.","trata como imóvel.","só pune se houver violência.","só pune se houver arma."],"Art. 155, § 3º.")
q(3,"No § 5º do art. 155, a subtração de veículo automotor tem pena de quatro a dez anos se o veículo",["venha a ser transportado para outro Estado ou para o exterior.","seja de luxo.","esteja estacionado.","pertença a idoso.","seja de carga."],"Art. 155, § 5º.")
q(3,"A subtração de fios, cabos ou equipamentos de energia ou telefonia, no § 8º, pode receber o privilégio porque o texto",["manda aplicar, em qualquer caso, o disposto no § 2º.","exclui o privilégio.","não trata do assunto.","manda aplicar o repouso noturno.","manda aplicar o § 4º."],"Art. 155, § 8º.")
q(3,"A pena do furto de fios, cabos ou equipamentos, no § 8º, é de reclusão de",["dois a oito anos, e multa.","quatro a dez anos, e multa.","um a seis anos, e multa.","seis a doze anos.","seis meses a dois anos."],"Art. 155, § 8º.")
q(3,"O furto cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada tem pena de",["reclusão, de quatro a dez anos, e multa.","reclusão, de dois a oito anos.","reclusão, de um a seis anos.","reclusão, de seis a doze anos.","detenção, de um a quatro anos."],"Art. 155, § 9º.")
q(3,"No furto mediante fraude por dispositivo eletrônico, a pena do § 4º-B é aumentada de um terço ao dobro se o crime é praticado contra",["idoso ou vulnerável.","qualquer adulto.","empresa.","servidor público.","estrangeiro."],"Art. 155, § 4º-C, II.")
q(3,"No § 6º do art. 155, a subtração de semovente domesticável de produção é equiparada, quanto à pena, à de",["animal doméstico e à de celular, computador ou dispositivo eletrônico semelhante.","imóvel rural.","energia elétrica.","fios e cabos.","combustíveis."],"Art. 155, § 6º, I e II.")
q(3,"No texto dos fios, a pena máxima aplicável em tese, antes de eventuais aumentos ou reduções, é de",["oito anos de reclusão.","seis anos de reclusão.","dez anos de reclusão.","dois anos de detenção.","quatro anos de reclusão."],"Art. 155, § 8º.","cp7a")
q(3,"No texto do celular, a pena é maior que a do furto simples porque o objeto é aparelho de telefonia celular, hipótese do",["§ 6º, II, do art. 155.","§ 4º, I, do art. 155.","§ 1º do art. 155.","art. 156.","art. 157."],"Art. 155, § 6º, II.","cp7b")
assert len(Q)==60,len(Q)
code,svg=mapa("Furto: do simples ao qualificado",[
 ("simples","Furto simples",["reclusão, 1 a 6 anos, e multa","coisa alheia móvel","sem violência"],"seção 1"),
 ("ajustes","Aumento e privilégio",["repouso noturno: + metade","primário e pequeno valor","detenção, redução ou multa"],"seção 1"),
 ("qual","Qualificado",["reclusão, 2 a 8 anos, e multa","obstáculo, confiança, fraude","chave falsa, concurso"],"seção 2"),
 ("maior","Pena de 4 a 10 anos",["explosivo","furto eletrônico","celular, arma, veículo"],"seções 2 e 3"),
 ("fios","Fios, cabos e combustíveis",["fios e cabos: 2 a 8 anos","privilégio aplica","combustíveis: 4 a 10 anos"],"seção 3"),
 ("comum","Coisa comum",["detenção, 6 meses a 2 anos","representação","fungível: não punível"],"seção 4")],
 "Na prova: confira a pena de cada hipótese e se há violência (roubo) ou não (furto)")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As duas primeiras caixas têm o furto e seus ajustes; as demais, as figuras de pena maior e a coisa comum.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 155 e 156, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-7","Furto (CP, arts. 155 e 156)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 155 e 156. Cobertos: art. 155 (caput e §§ 1º a 12) e art. 156."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; o art. 155 teve muitas alterações (2018 a 2026) e deve ser reconferido no Planalto.","A questão sobre a aplicação do repouso noturno ao furto qualificado é controvertida na jurisprudência; a aula não a trata.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp7a e cp7b fictícios."],
 fontes_conferidas=["CP, arts. 155 e 156: texto da Câmara, copiado por programa."])
gravar("cp-7",aula_html,banco("cp-7",Q),tx)
