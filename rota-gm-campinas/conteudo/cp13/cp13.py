import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes funcionais são os praticados por quem exerce função pública, e o guarda municipal é, para efeitos penais, funcionário público. O peculato, aberto pelo art. 312, é o crime de quem se apropria de bem de que tem a posse em razão do cargo. A Vunesp cobra os arts. 312 a 315 pelo conceito de cada crime, pelo peculato culposo e a reparação do dano, pelo peculato mediante erro, pela inserção de dados falsos em sistemas e pelas figuras do extravio de documento e do emprego irregular de verbas. A aula segue o texto consolidado."
S={}
S[1]="## 1. Peculato\n\n"+L("art. 312, caput e § 1º","Art. 312. Apropriar-se o funcionário público","Peculato culposo")+"""

O peculato é o crime de quem, sendo funcionário público, se apropria de dinheiro, valor ou outro bem móvel, público ou particular, de que tem a posse em razão do cargo, ou o desvia, em proveito próprio ou alheio. A pena é de reclusão de dois a doze anos e multa. O que o distingue da apropriação indébita é a qualidade do agente (funcionário) e a razão da posse (o cargo). O bem pode ser público ou particular: o guarda que se apropria de bem de particular apreendido por ele em razão do cargo também comete peculato.

O § 1º é o peculato-furto: o funcionário, embora sem a posse do bem, o subtrai ou concorre para que seja subtraído, valendo-se da facilidade que lhe dá a qualidade de funcionário. A pena é a mesma.

"""+L("art. 312, §§ 2º e 3º","Peculato culposo","Peculato mediante erro de outrem")+"""

No peculato culposo, o funcionário concorre culposamente para o crime de outrem, com detenção de três meses a um ano. A reparação do dano, se precede a sentença irrecorrível, extingue a punibilidade; se é posterior, reduz de metade a pena imposta. Esta é uma das raras regras do Código em que a reparação tem esse efeito, e só vale para o peculato culposo.
"""
S[2]="## 2. Peculato mediante erro e crimes com sistemas de informação\n\n"+L("art. 313","Art. 313. Apropriar-se de dinheiro","Inserção de dados falsos")+"\n\n"+L("art. 313-A","Art. 313-A. Inserir ou facilitar","Modificação ou alteração não autorizada")+"\n\n"+L("art. 313-B","Art. 313-B. Modificar ou alterar","Extravio, sonegação")+"""

No peculato mediante erro de outrem (art. 313), o funcionário se apropria de dinheiro ou utilidade que, no exercício do cargo, recebeu por erro de outrem, com reclusão de um a quatro anos e multa. A inserção de dados falsos em sistema de informações (art. 313-A) é inserir ou facilitar a inserção de dados falsos, alterar ou excluir indevidamente dados corretos nos sistemas da Administração Pública, com o fim de obter vantagem indevida ou causar dano, com reclusão de dois a doze anos e multa. O art. 313-B pune o funcionário que modifica ou altera sistema ou programa sem autorização, com detenção de três meses a dois anos e multa, e aumento de um terço até a metade se resulta dano.
"""
S[3]="## 3. Extravio de documento e emprego irregular de verbas\n\n"+L("art. 314","Art. 314. Extraviar livro oficial","Emprego irregular de verbas")+"\n\n"+L("art. 315","Art. 315. Dar às verbas ou rendas públicas","Concussão")+"""

O art. 314 pune o funcionário que extravia livro oficial ou documento de que tem a guarda em razão do cargo, ou o sonega ou inutiliza, total ou parcialmente. A pena é de reclusão de um a quatro anos, se o fato não constitui crime mais grave: é um crime subsidiário. Já o emprego irregular de verbas ou rendas públicas (art. 315) é dar a elas aplicação diversa da estabelecida em lei, com detenção de um a três meses, ou multa. Repare que o gestor pode usar a verba em finalidade pública, mas diferente da prevista na lei, e ainda assim comete o crime.
"""
S[5]="""## 5. Na rotina do guarda

- **Bens apreendidos:** o guarda que se apropria ou desvia bens que recebeu em razão do cargo comete peculato, de pena de dois a doze anos.
- **Documentos e livros oficiais:** extraviar boletim de ocorrência ou livro de registro da Guarda é crime do art. 314.
- **Sistemas de informação:** inserir dado falso ou alterar registro indevidamente no sistema da Guarda ou da Prefeitura é crime do art. 313-A, com reclusão de dois a doze anos.
- **Valores recebidos por erro:** o servidor que recebe valor por engano de um cidadão e o retém comete peculato mediante erro.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Pena do peculato | Reclusão de dois a doze anos, e multa |
| Peculato-furto | Funcionário sem a posse, que se vale da facilidade do cargo (§ 1º) |
| Pena do peculato culposo | Detenção de três meses a um ano |
| Reparação do dano | Antes da sentença, extingue a punibilidade; depois, reduz a pena de metade |
| Peculato mediante erro | Reclusão de um a quatro anos, e multa |
| Inserção de dados falsos | Reclusão de dois a doze anos, e multa |
| Pena do art. 314 | Reclusão de um a quatro anos, se não é crime mais grave |
| Pena do art. 315 | Detenção de um a três meses, ou multa |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Peculato | Reclusão, 2 a 12 anos, e multa; posse em razão do cargo |
| Peculato culposo | Detenção, 3 meses a 1 ano; reparação extingue ou reduz |
| Peculato mediante erro | Reclusão, 1 a 4 anos, e multa |
| Dados falsos em sistema | Reclusão, 2 a 12 anos, e multa |
| Alteração não autorizada de sistema | Detenção, 3 meses a 2 anos, e multa |
| Extravio de documento | Reclusão, 1 a 4 anos, se não é crime mais grave |
| Emprego irregular de verbas | Detenção, 1 a 3 meses, ou multa |
"""
QR=[("Questão 1","A pena do peculato (art. 312, caput) é de",["reclusão, de dois a doze anos, e multa.","reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","reclusão, de quatro a oito anos.","detenção, de um a três meses."],0,"Art. 312, caput."),
("Questão 2","No peculato culposo, a reparação do dano, se precede a sentença irrecorrível,",["extingue a punibilidade.","reduz a pena de metade.","aumenta a pena.","não tem efeito.","converte em multa."],2,"Art. 312, § 3º."),
("Questão 3","O funcionário que se apropria de dinheiro que recebeu, no exercício do cargo, por erro de outrem pratica",["peculato mediante erro, de reclusão de um a quatro anos, e multa.","peculato, de reclusão de dois a doze anos.","furto.","estelionato.","extorsão."],1,"Art. 313."),
("Questão 4","O art. 315 (emprego irregular de verbas ou rendas públicas) é crime com pena de",["detenção, de um a três meses, ou multa.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","multa, apenas."],4,"Art. 315.")]
t1="<strong>Bens apreendidos desaparecem do depósito</strong><br><br>Um guarda municipal de Vila Nova, cidade fictícia, responsável pelo depósito de bens apreendidos, vendeu parte do material e ficou com o dinheiro. O material pertencia a particulares e fora apreendido por ele em razão do cargo."
t2="<strong>Dados alterados no sistema</strong><br><br>Um servidor municipal, com acesso autorizado, alterou no sistema informatizado da Prefeitura o registro de multas de trânsito de um conhecido, apagando as multas, para beneficiá-lo."
tx={"cp13a":t1,"cp13b":t2}
# n=1
q(1,"A pena do peculato é de",["reclusão, de dois a doze anos, e multa.","reclusão, de um a quatro anos, e multa.","detenção, de três meses a um ano.","reclusão, de quatro a oito anos.","detenção, de um a três meses."],"Art. 312, caput.")
q(1,"O peculato é crime praticado por",["funcionário público.","qualquer pessoa.","apenas particular.","apenas juiz.","apenas policial."],"Art. 312, caput.")
q(1,"No peculato, o funcionário público se apropria de dinheiro, valor ou outro bem móvel de que tem a posse",["em razão do cargo.","por empréstimo.","por herança.","por compra.","por doação."],"Art. 312, caput.")
q(1,"O bem objeto do peculato pode ser",["público ou particular.","apenas público.","apenas particular.","apenas imóvel.","apenas de valor elevado."],"Art. 312, caput.")
q(1,"Aplica-se a mesma pena do peculato ao funcionário que, sem ter a posse do bem, o subtrai valendo-se da",["facilidade que lhe proporciona a qualidade de funcionário.","violência.","ameaça.","fraude.","escalada."],"Art. 312, § 1º.")
q(1,"A pena do peculato culposo é de",["detenção, de três meses a um ano.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de um a três meses.","multa."],"Art. 312, § 2º.")
q(1,"No peculato culposo, a reparação do dano posterior à sentença irrecorrível",["reduz de metade a pena imposta.","extingue a punibilidade.","aumenta a pena.","não tem efeito.","absolve."],"Art. 312, § 3º.")
q(1,"A pena do peculato mediante erro de outrem (art. 313) é de",["reclusão, de um a quatro anos, e multa.","reclusão, de dois a doze anos.","detenção, de três meses a um ano.","detenção, de um a três meses.","multa."],"Art. 313.")
q(1,"Inserir dados falsos nos sistemas informatizados da Administração Pública, com o fim de obter vantagem indevida, tem pena de",["reclusão, de dois a doze anos, e multa.","reclusão, de um a quatro anos.","detenção, de três meses a dois anos.","detenção, de um a três meses.","multa."],"Art. 313-A.")
q(1,"A modificação ou alteração, pelo funcionário, de sistema de informações ou programa de informática sem autorização tem pena de",["detenção, de três meses a dois anos, e multa.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de um a três meses.","multa."],"Art. 313-B.")
q(1,"A pena do art. 313-B aumenta-se de um terço até a metade se da modificação resulta",["dano para a Administração Pública ou para o administrado.","lucro.","prazer.","benefício.","nenhum efeito."],"Art. 313-B, parágrafo único.")
q(1,"Extraviar livro oficial ou documento de que se tem a guarda em razão do cargo tem pena de",["reclusão, de um a quatro anos, se o fato não constitui crime mais grave.","detenção, de três meses a um ano.","reclusão, de dois a doze anos.","multa.","detenção, de um a três meses."],"Art. 314.")
q(1,"Dar às verbas ou rendas públicas aplicação diversa da estabelecida em lei tem pena de",["detenção, de um a três meses, ou multa.","reclusão, de dois a doze anos.","reclusão, de um a quatro anos.","detenção, de seis meses a dois anos.","multa, apenas."],"Art. 315.")
q(1,"O peculato é crime contra",["a Administração Pública.","a vida.","a honra.","o patrimônio, apenas.","a liberdade."],"Art. 312 (Título XI do Código Penal).")
q(1,"No peculato, o desvio do bem, em proveito próprio ou alheio, equivale à",["apropriação.","omissão.","negligência.","dívida.","culpa."],"Art. 312, caput.")
q(1,"A inserção de dados falsos em sistemas informatizados é crime praticado por",["funcionário autorizado.","qualquer pessoa.","apenas particular.","apenas estagiário.","apenas servidor aposentado."],"Art. 313-A.")
q(1,"A pena do art. 314 (extravio de livro ou documento) é subsidiária porque aplicável",["se o fato não constitui crime mais grave.","em qualquer caso.","se há violência.","se há fraude.","se há dano."],"Art. 314.")
q(1,"No texto do depósito, o guarda que vende bens de particulares apreendidos por ele em razão do cargo e fica com o dinheiro comete",["peculato.","furto.","roubo.","estelionato.","extorsão."],"Art. 312, caput.","cp13a")
q(1,"No texto dos dados alterados, o servidor que apaga multas no sistema, para beneficiar um conhecido, comete",["inserção de dados falsos ou alteração indevida, do art. 313-A.","peculato.","corrupção passiva.","concussão.","prevaricação."],"Art. 313-A.","cp13b")
q(1,"Para efeitos penais, o guarda municipal, que exerce cargo, emprego ou função pública, é considerado",["funcionário público.","particular.","autônomo.","voluntário.","terceirizado, apenas."],"Art. 327, caput.")
# n=2
q(2,"O peculato-furto do § 1º se distingue do peculato do caput porque, no § 1º, o funcionário",["não tem a posse do bem e se vale da facilidade do cargo para subtraí-lo.","tem a posse.","usa violência.","usa fraude.","é aposentado."],"Art. 312, § 1º.")
q(2,"No peculato culposo, o funcionário",["concorre culposamente para o crime de outrem.","age com dolo.","se apropria do bem.","desvia o bem.","subtrai o bem."],"Art. 312, § 2º.")
q(2,"A reparação do dano antes da sentença irrecorrível extingue a punibilidade no",["peculato culposo.","peculato doloso.","peculato-furto.","peculato mediante erro.","art. 313-A."],"Art. 312, § 3º.")
q(2,"No peculato mediante erro de outrem, o funcionário recebe o bem, no exercício do cargo, por",["erro de outrem.","violência.","fraude.","ameaça.","doação."],"Art. 313.")
q(2,"A inserção de dados falsos nos sistemas da Administração Pública tem como fim obter vantagem indevida para si ou para outrem, ou",["causar dano.","produzir benefício.","dar publicidade.","prestar contas.","corrigir erro."],"Art. 313-A.")
q(2,"A conduta de “facilitar a inserção de dados falsos” é típica do art.",["313-A.","313-B.","314.","315.","312."],"Art. 313-A.")
q(2,"Alterar ou excluir indevidamente dados corretos nos sistemas da Administração Pública, com fim de obter vantagem, é crime do art.",["313-A.","313-B.","314.","315.","312."],"Art. 313-A.")
q(2,"O art. 313-B pune o funcionário que modifica ou altera sistema ou programa de informática sem autorização ou solicitação de",["autoridade competente.","particular.","imprensa.","vizinho.","parente."],"Art. 313-B.")
q(2,"No art. 314, o funcionário tem a guarda do livro ou documento em razão do",["cargo.","parentesco.","empréstimo.","contrato.","compra."],"Art. 314.")
q(2,"No art. 314, as condutas típicas são extraviar, sonegar ou",["inutilizar, total ou parcialmente.","copiar.","ler.","guardar.","fotografar."],"Art. 314.")
q(2,"O emprego irregular de verbas públicas (art. 315) ocorre quando se dá a verba aplicação",["diversa da estabelecida em lei.","igual à estabelecida.","parcelada.","antecipada.","tardia."],"Art. 315.")
q(2,"No peculato, “apropriar-se” significa",["passar a agir como dono do bem de que tem posse.","entregar o bem.","guardar o bem.","consertar o bem.","devolver o bem."],"Art. 312, caput.")
q(2,"A pena do peculato é mais alta que a da apropriação indébita porque o peculato atinge",["a Administração Pública e o dever do funcionário.","apenas o patrimônio do particular.","apenas a honra.","a vida.","a liberdade."],"Arts. 168 e 312.")
q(2,"No peculato culposo, a pena é de",["detenção, de três meses a um ano.","reclusão, de um a quatro anos.","reclusão, de dois a doze anos.","multa.","detenção, de um a três meses."],"Art. 312, § 2º.")
q(2,"O art. 313-A fala em funcionário",["autorizado.","qualquer.","estagiário apenas.","aposentado.","terceirizado apenas."],"Art. 313-A.")
q(2,"No texto do depósito, o fato de o bem pertencer a particular",["não afasta o peculato, pois o bem pode ser público ou particular.","afasta o peculato.","transforma em furto.","transforma em roubo.","transforma em estelionato."],"Art. 312, caput.","cp13a")
q(2,"No texto do depósito, a pena do crime é de",["reclusão, de dois a doze anos, e multa.","reclusão, de um a quatro anos.","detenção, de três meses a um ano.","detenção, de um a três meses.","multa."],"Art. 312, caput.","cp13a")
q(2,"No texto dos dados alterados, a pena do crime é de",["reclusão, de dois a doze anos, e multa.","detenção, de três meses a dois anos.","reclusão, de um a quatro anos.","detenção, de um a três meses.","multa."],"Art. 313-A.","cp13b")
q(2,"A pena mínima do peculato culposo é de",["três meses de detenção.","um ano de reclusão.","dois anos de reclusão.","um mês de detenção.","seis meses de reclusão."],"Art. 312, § 2º.")
q(2,"Na inserção de dados falsos do art. 313-A, a pena de reclusão máxima é de",["doze anos.","quatro anos.","dois anos.","oito anos.","seis anos."],"Art. 313-A.")
# n=3
q(3,"Assinale a alternativa que traz apenas penas corretas.",["Peculato: reclusão de dois a doze anos e multa; peculato culposo: detenção de três meses a um ano; peculato mediante erro: reclusão de um a quatro anos e multa.","Peculato: detenção; culposo: reclusão.","Peculato: reclusão de um a quatro anos; mediante erro: reclusão de dois a doze.","Culposo: reclusão de dois a doze anos.","Mediante erro: detenção de três meses a um ano."],"Arts. 312 e 313.")
q(3,"Considere as afirmações. I. O peculato pode ter por objeto bem particular. II. A reparação do dano antes da sentença irrecorrível extingue a punibilidade no peculato culposo. III. O peculato mediante erro tem pena de detenção. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"O peculato mediante erro tem reclusão (art. 313).")
q(3,"Assinale a INCORRETA.",["A reparação do dano, depois da sentença irrecorrível, extingue a punibilidade no peculato culposo.","O peculato-furto não exige que o funcionário tenha a posse do bem.","O art. 314 é crime subsidiário.","O art. 315 tem pena de detenção de um a três meses, ou multa.","O art. 313-A tem pena de reclusão de dois a doze anos e multa."],"Depois da sentença, a reparação apenas reduz a pena de metade (art. 312, § 3º).")
q(3,"A diferença entre peculato e apropriação indébita está",["na qualidade de funcionário público do agente e na posse em razão do cargo.","no valor do bem.","no local do crime.","no horário.","na idade da vítima."],"Arts. 168 e 312.")
q(3,"A diferença entre o peculato do caput e o do art. 313 está em que, neste último, o funcionário recebeu o bem",["por erro de outrem.","em razão do cargo, sem erro.","por violência.","por fraude.","por doação."],"Art. 313.")
q(3,"No art. 313-A, a conduta de “inserir ou facilitar a inserção” é cometida pelo funcionário",["autorizado.","qualquer pessoa.","apenas estagiário.","apenas aposentado.","apenas terceirizado."],"Art. 313-A.")
q(3,"No art. 313-B, a pena é aumentada de um terço até a metade se da modificação ou alteração resulta dano para",["a Administração Pública ou para o administrado.","apenas o servidor.","apenas o chefe.","apenas o agente.","ninguém."],"Art. 313-B, parágrafo único.")
q(3,"O art. 314 tem pena de reclusão de um a quatro anos",["se o fato não constitui crime mais grave.","em qualquer caso.","apenas se houver dano.","apenas se houver dolo.","apenas se houver lucro."],"Art. 314.")
q(3,"No peculato, a conduta de “desviar” o bem consiste em",["dar ao bem destino diverso do que deveria ter, em proveito próprio ou alheio.","entregar o bem.","guardar o bem.","consertar o bem.","vender o bem lícito."],"Art. 312, caput.")
q(3,"A razão de o peculato-furto (§ 1º) ter a mesma pena do peculato do caput é que, em ambos,",["o funcionário se vale do cargo para lesar o patrimônio.","há violência.","há ameaça.","há fraude.","há arma."],"Art. 312, § 1º.")
q(3,"O emprego irregular de verbas (art. 315) é crime ainda que a verba seja usada em",["finalidade pública, desde que diversa da estabelecida em lei.","finalidade pessoal apenas.","finalidade ilícita apenas.","compra de bens pessoais apenas.","pagamento de dívida pessoal apenas."],"Art. 315.")
q(3,"A reparação do dano, no peculato culposo, depois da sentença irrecorrível, tem como efeito",["reduzir de metade a pena imposta.","extinguir a punibilidade.","aumentar a pena.","converter em multa.","absolver."],"Art. 312, § 3º.")
q(3,"O art. 313-A fala em “sistemas informatizados ou bancos de dados da Administração Pública”, o que mostra que o objeto do crime é",["dado da Administração Pública, e não de empresa privada.","dado de qualquer pessoa.","dado de empresa privada.","dado de parente.","dado de vizinho."],"Art. 313-A.")
q(3,"Assinale a alternativa correta sobre o art. 313-A.",["O funcionário autorizado que insere dados falsos ou altera dados corretos nos sistemas da Administração Pública, com fim de vantagem indevida ou dano, tem pena de reclusão de dois a doze anos e multa.","O crime é de detenção.","O crime é praticado por qualquer pessoa.","O crime exige violência.","O crime exige ameaça."],"Art. 313-A.")
q(3,"Assinale a alternativa que associa corretamente o artigo à conduta.",["312: apropriação ou desvio; 313: bem recebido por erro; 314: extravio de documento; 315: aplicação diversa de verba.","312: erro; 313: apropriação; 314: verba; 315: extravio.","312: documento; 313: verba.","313: dados; 314: peculato.","315: peculato; 312: verba."],"Arts. 312 a 315.")
q(3,"A pena do peculato mediante erro (art. 313) é menor que a do peculato do caput porque, no art. 313,",["o bem veio ao funcionário por erro de outrem, e não por posse em razão do cargo.","o funcionário é primário.","há menos dano.","há menos dolo.","há mais testemunhas."],"Arts. 312 e 313.")
q(3,"No texto do depósito, o “bem apreendido” pertencia a particulares. O peculato é, nesse caso, crime contra",["a Administração Pública, que tem a guarda do bem, e também contra o particular.","apenas o particular.","apenas o juiz.","apenas o Município.","ninguém."],"Art. 312, caput.","cp13a")
q(3,"No texto do depósito, a pena mínima do crime é de",["dois anos de reclusão.","um ano de reclusão.","três meses de detenção.","um mês de detenção.","quatro anos de reclusão."],"Art. 312, caput.","cp13a")
q(3,"No texto dos dados alterados, o fato de o servidor ter acesso autorizado ao sistema",["não exclui o crime do art. 313-A, que se refere ao funcionário autorizado.","exclui o crime.","transforma em furto.","transforma em estelionato.","reduz a pena."],"Art. 313-A.","cp13b")
q(3,"No texto dos dados alterados, a pena máxima do crime é de",["doze anos de reclusão.","quatro anos de reclusão.","dois anos de detenção.","três meses de detenção.","oito anos de reclusão."],"Art. 313-A.","cp13b")
assert len(Q)==60,len(Q)
code,svg=mapa("Peculato e crimes afins",[
 ("pec","Peculato",["reclusão, 2 a 12 anos, e multa","apropria ou desvia","posse em razão do cargo"],"seção 1"),
 ("furto","Peculato-furto",["§ 1º","sem posse","facilidade do cargo"],"seção 1"),
 ("culp","Peculato culposo",["detenção, 3 meses a 1 ano","reparação antes da sentença: extingue","depois: reduz de metade"],"seção 1"),
 ("erro","Mediante erro",["art. 313","reclusão, 1 a 4 anos","recebeu por erro de outrem"],"seção 2"),
 ("dados","Sistemas de informação",["313-A: reclusão, 2 a 12 anos","313-B: detenção, 3 meses a 2 anos","dano: aumento de 1/3 a 1/2"],"seção 2"),
 ("doc","Documento e verbas",["314: reclusão, 1 a 4 anos","315: detenção, 1 a 3 meses","verba com aplicação diversa"],"seção 3")],
 "Na prova: o peculato exige funcionário e posse em razão do cargo; a reparação só importa no culposo")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira caixa trata do peculato e de suas formas; as demais, de figuras com a mesma ideia de infidelidade ao cargo.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 312 a 315, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-13","Peculato e crimes afins (CP, arts. 312 a 315)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 312 a 315. Cobertos: 312, 313, 313-A, 313-B, 314 e 315."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","A expressão peculato-furto é doutrinária.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp13a e cp13b fictícios."],
 fontes_conferidas=["CP, arts. 312 a 315: texto da Câmara, copiado por programa."])
gravar("cp-13",aula_html,banco("cp-13",Q),tx)
