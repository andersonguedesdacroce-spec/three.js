import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='forca1.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Lei 13.060/2014 é curta, mas é a lei do dia a dia do guarda armado: ela manda priorizar os instrumentos de menor potencial ofensivo (spray de pimenta, bastão, arma de condução de energia) e proíbe o uso de arma de fogo em duas situações clássicas: contra pessoa em fuga desarmada e contra veículo que fura bloqueio, salvo risco de morte. A Vunesp cobra os três princípios (legalidade, necessidade, razoabilidade e proporcionalidade), as duas proibições do parágrafo único do art. 2º, o conceito de instrumento de menor potencial ofensivo e a obrigação de socorro."
S={}
S[1]="## 1. Objeto, princípios e vedações\n\n"+L("art. 1º","Art. 1º Esta Lei disciplina","Art. 2º")+"\n\n"+L("art. 2º, caput","Art. 2º Os órgãos de segurança pública","Parágrafo único. Não é legítimo")+"\n\n"+L("art. 2º, parágrafo único","Parágrafo único. Não é legítimo","Art. 3º")+"""

A lei disciplina o uso dos instrumentos de menor potencial ofensivo pelos agentes de segurança pública em todo o território nacional. Os órgãos devem priorizar a utilização desses instrumentos, desde que o uso não coloque em risco a integridade física ou psíquica dos policiais, e obedecer a três princípios: legalidade, necessidade e razoabilidade e proporcionalidade.

Não é legítimo o uso de arma de fogo contra pessoa em fuga que esteja desarmada ou que não represente risco imediato de morte ou lesão aos agentes ou a terceiros, e contra veículo que desrespeite bloqueio policial em via pública, exceto quando o ato represente risco de morte ou lesão aos agentes ou a terceiros.
"""
S[2]="## 2. Formação, conceito e fornecimento\n\n"+L("art. 3º","Art. 3º Os cursos de formação","Art. 4º")+"\n\n"+L("art. 4º","Art. 4º Para os efeitos desta Lei","Art. 5º")+"\n\n"+L("art. 5º","Art. 5º O poder público tem o dever","Art. 6º")+"""

Os cursos de formação e capacitação devem incluir conteúdo programático que habilite ao uso dos instrumentos não letais. Consideram-se instrumentos de menor potencial ofensivo os projetados especificamente para, com baixa probabilidade de causar mortes ou lesões permanentes, conter, debilitar ou incapacitar temporariamente pessoas. O poder público tem o dever de fornecer a todo agente de segurança pública instrumentos de menor potencial ofensivo para o uso racional da força.
"""
S[3]="## 3. Socorro e regulamento\n\n"+L("art. 6º","Art. 6º Sempre que do uso da força","Art. 7º")+"\n\n"+L("art. 7º","Art. 7º O Poder Executivo editará","Art. 8º")+"""

Sempre que do uso da força decorrerem ferimentos em pessoas, deve ser assegurada a imediata prestação de assistência e socorro médico aos feridos, bem como a comunicação do ocorrido à família ou à pessoa por eles indicada. O Poder Executivo edita regulamento classificando e disciplinando a utilização dos instrumentos não letais (o Decreto 12.341/2024 é o regulamento do uso da força).
"""
S[5]="""## 5. Na rotina do guarda

- **Prioridade:** o guarda usa primeiro o instrumento de menor potencial ofensivo (spray, bastão, pistola de choque), desde que isso não coloque em risco a sua integridade.
- **Fuga de desarmado:** não é legítimo atirar em quem foge desarmado e não representa risco imediato.
- **Bloqueio:** não é legítimo atirar em veículo que fura bloqueio, exceto se houver risco de morte ou lesão.
- **Socorro:** se houver ferido, o guarda presta ou providencia socorro imediato e comunica a família ou a pessoa indicada.
- **Capacitação:** só utiliza instrumento quem recebeu formação para tanto.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Princípios do art. 2º | Legalidade, necessidade, razoabilidade e proporcionalidade |
| Prioridade | Instrumentos de menor potencial ofensivo, se não houver risco para o policial |
| Arma de fogo contra fugitivo | Ilegítima se desarmado ou sem risco imediato |
| Veículo em bloqueio | Ilegítimo, exceto risco de morte ou lesão |
| Conceito | Baixa probabilidade de causar mortes ou lesões permanentes |
| Fornecimento | Dever do poder público a todo agente |
| Socorro | Imediato, com comunicação à família ou pessoa indicada |
| Regulamento | Poder Executivo |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Disciplina o uso dos instrumentos de menor potencial ofensivo |
| Art. 2º | Prioridade; legalidade, necessidade, razoabilidade e proporcionalidade |
| Art. 2º, parágrafo único | Vedado fogo contra fugitivo desarmado e veículo em bloqueio, salvo risco |
| Art. 3º | Formação com conteúdo sobre instrumentos não letais |
| Art. 4º | Conceito de instrumento de menor potencial ofensivo |
| Art. 5º | Poder público fornece |
| Art. 6º | Socorro imediato e comunicação |
| Art. 7º | Regulamento do Executivo |
"""
QR=[("Questão 1","Os órgãos de segurança pública deverão priorizar a utilização dos instrumentos de menor potencial ofensivo, desde que o seu uso não coloque em risco a integridade física ou psíquica dos",["policiais.","civis.","presos.","vizinhos.","jornalistas."],0,"Art. 2º."),
("Questão 2","Entre os princípios a serem obedecidos no uso dos instrumentos de menor potencial ofensivo estão a legalidade, a necessidade e a",["razoabilidade e proporcionalidade.","impunidade.","rapidez.","economicidade.","publicidade."],1,"Art. 2º, I a III."),
("Questão 3","Não é legítimo o uso de arma de fogo contra veículo que desrespeite bloqueio policial em via pública, exceto quando o ato represente risco de",["morte ou lesão aos agentes de segurança pública ou a terceiros.","atraso.","multa.","fuga.","dano ao veículo."],2,"Art. 2º, parágrafo único, II."),
("Questão 4","Sempre que do uso da força decorrerem ferimentos em pessoas, deverá ser assegurada a imediata prestação de assistência e socorro médico aos feridos e a comunicação do ocorrido à",["família ou à pessoa por eles indicada.","imprensa.","vizinhança.","empresa.","escola."],3,"Art. 6º.")]
t1="<strong>Fuga a pé</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, perseguiu um homem que fugia a pé, desarmado, após furtar uma loja. O guarda sacou a arma de fogo."
t2="<strong>Bloqueio na avenida</strong><br><br>Um motorista furou uma blitz montada pela guarda numa avenida de Vila Nova e seguiu em baixa velocidade. Ninguém corria risco imediato."
t3="<strong>Uso do spray</strong><br><br>Numa abordagem a um homem agressivo, o guarda de Vila Nova usou spray de pimenta, e o homem passou mal e precisou de atendimento."
tx={"forca1a":t1,"forca1b":t2,"forca1c":t3}
# n=1
q(1,"A Lei 13.060/2014 disciplina o uso dos instrumentos de menor potencial ofensivo pelos agentes de",["segurança pública.","fiscalização tributária.","trânsito, apenas.","defesa civil.","vigilância privada."],"Art. 1º.")
q(1,"A Lei 13.060/2014 aplica-se em todo o território",["nacional.","estadual.","municipal.","urbano.","rural."],"Art. 1º.")
q(1,"Os órgãos de segurança pública deverão priorizar a utilização dos instrumentos de menor potencial",["ofensivo.","lesivo.","letal.","defensivo.","intimidatório."],"Art. 2º.")
q(1,"Um dos princípios do art. 2º é a",["legalidade.","impunidade.","pessoalidade.","oportunidade.","especialidade."],"Art. 2º, I.")
q(1,"Um dos princípios do art. 2º é a necessidade, e o outro é a razoabilidade e a",["proporcionalidade.","moralidade.","publicidade.","eficiência.","impessoalidade."],"Art. 2º, III.")
q(1,"Não é legítimo o uso de arma de fogo contra pessoa em fuga que esteja desarmada ou que não represente risco imediato de morte ou de",["lesão aos agentes de segurança pública ou a terceiros.","furto.","dano ao patrimônio.","atraso.","multa."],"Art. 2º, parágrafo único, I.")
q(1,"Não é legítimo o uso de arma de fogo contra veículo que desrespeite",["bloqueio policial em via pública.","semáforo.","faixa de pedestres.","limite de velocidade.","sinal de pare."],"Art. 2º, parágrafo único, II.")
q(1,"Os cursos de formação e capacitação deverão incluir conteúdo programático que habilite ao uso dos instrumentos",["não letais.","letais.","pesados.","privados.","experimentais."],"Art. 3º.")
q(1,"Instrumentos de menor potencial ofensivo são os projetados para, com baixa probabilidade de causar mortes ou lesões permanentes, conter, debilitar ou incapacitar",["temporariamente pessoas.","definitivamente pessoas.","apenas animais.","apenas veículos.","apenas multidões."],"Art. 4º.")
q(1,"O poder público tem o dever de fornecer a todo agente de segurança pública instrumentos de menor potencial ofensivo para o uso racional da",["força.","arma.","ordem.","informação.","viatura."],"Art. 5º.")
q(1,"Sempre que do uso da força decorrerem ferimentos, deverá ser assegurada a imediata prestação de assistência e socorro",["médico aos feridos.","jurídico.","financeiro.","religioso.","escolar."],"Art. 6º.")
q(1,"O Poder Executivo editará regulamento classificando e disciplinando a utilização dos instrumentos",["não letais.","letais.","privados.","militares.","estrangeiros."],"Art. 7º.")
q(1,"A lei entra em vigor na data de sua",["publicação.","revogação.","aprovação.","regulamentação.","sanção."],"Art. 8º.")
q(1,"O uso dos instrumentos de menor potencial ofensivo deve ser priorizado desde que não coloque em risco a integridade física ou psíquica dos",["policiais.","presos.","jornalistas.","parentes.","testemunhas."],"Art. 2º.")
q(1,"A comunicação do ferimento, no art. 6º, é feita à família ou à pessoa por eles",["indicada.","contratada.","sorteada.","nomeada pelo juiz.","vizinha."],"Art. 6º.")
q(1,"O dever do art. 5º é de fornecer instrumentos a todo",["agente de segurança pública.","agente comunitário.","cidadão.","vigilante privado.","servidor administrativo."],"Art. 5º.")
q(1,"O art. 4º define o conceito de instrumento de menor potencial",["ofensivo.","defensivo.","lesivo.","letal.","brando."],"Art. 4º.")
q(1,"No texto da fuga a pé, o homem desarmado em fuga que não oferece risco imediato é situação em que o uso de arma de fogo",["não é legítimo.","é legítimo.","é obrigatório.","é recomendado.","é regra."],"Art. 2º, parágrafo único, I.","forca1a")
q(1,"No texto do bloqueio na avenida, o motorista que fura o bloqueio sem risco a ninguém não autoriza o uso de",["arma de fogo.","sirene.","comunicação por rádio.","registro de ocorrência.","perseguição."],"Art. 2º, parágrafo único, II.","forca1b")
q(1,"No texto do uso do spray, o homem que passou mal tem direito a imediata prestação de assistência e",["socorro médico.","multa.","julgamento.","liberação.","desculpas."],"Art. 6º.","forca1c")
# n=2
q(2,"A lei obriga os órgãos de segurança pública a obedecer a princípios, entre eles a legalidade, a necessidade e a razoabilidade e proporcionalidade, que somam",["três princípios.","dois princípios.","quatro princípios.","cinco princípios.","seis princípios."],"Art. 2º.")
q(2,"A vedação ao uso de arma de fogo contra fugitivo desarmado está no parágrafo único do art.",["2º.","1º.","3º.","4º.","6º."],"Art. 2º, parágrafo único.")
q(2,"O uso de arma de fogo contra veículo em bloqueio é admitido se o ato representar risco de morte ou lesão aos agentes ou a",["terceiros.","bens.","a imagem.","a viatura.","o trânsito."],"Art. 2º, parágrafo único, II.")
q(2,"O dever de os cursos incluírem conteúdo sobre instrumentos não letais está no art.",["3º.","2º.","4º.","5º.","6º."],"Art. 3º.")
q(2,"Os instrumentos de menor potencial ofensivo têm baixa probabilidade de causar mortes ou lesões",["permanentes.","leves.","temporárias.","psíquicas.","superficiais."],"Art. 4º.")
q(2,"O fornecimento dos instrumentos visa ao uso racional da força, conforme o art.",["5º.","3º.","4º.","6º.","7º."],"Art. 5º.")
q(2,"O art. 6º trata da assistência e do socorro médico, e a comunicação do ocorrido é à família ou à pessoa indicada pelos",["feridos.","agentes.","juízes.","delegados.","comandantes."],"Art. 6º.")
q(2,"O regulamento do art. 7º é editado pelo Poder",["Executivo.","Legislativo.","Judiciário.","Moderador.","Constituinte."],"Art. 7º.")
q(2,"A lei trata dos instrumentos de menor potencial ofensivo, que a doutrina denomina também de instrumentos",["não letais.","letais.","comuns.","pesados.","privados."],"Art. 3º e art. 7º.")
q(2,"A priorização do uso de instrumentos de menor potencial ofensivo cede se o uso colocar em risco a integridade dos",["policiais.","presos.","feridos.","parentes.","jornalistas."],"Art. 2º.")
q(2,"A lei disciplina o uso dos instrumentos pelos agentes de segurança pública, que incluem, para fins da Lei 13.675/2018, as guardas",["municipais.","privadas.","escolares.","florestais.","de condomínio."],"Lei 13.675/2018, art. 9º, § 2º, VII.")
q(2,"A lei prioriza os instrumentos não letais para minimizar o risco de morte e",["lesões permanentes.","gastos.","multas.","atrasos.","burocracia."],"Art. 4º.")
q(2,"O art. 2º se refere à integridade física ou psíquica dos policiais, que é condição para a prioridade do uso de instrumentos de menor potencial",["ofensivo.","legal.","real.","letal.","comum."],"Art. 2º.")
q(2,"A obrigação de socorro do art. 6º vale sempre que do uso da força decorrerem",["ferimentos em pessoas.","multas.","danos a veículos.","atrasos.","protestos."],"Art. 6º.")
q(2,"Os instrumentos podem conter, debilitar ou incapacitar temporariamente",["pessoas.","animais.","veículos.","edifícios.","câmeras."],"Art. 4º.")
q(2,"O uso de arma de fogo contra pessoa em fuga desarmada não é legítimo, exceto se houver risco imediato aos agentes ou a terceiros de morte ou de",["lesão.","multa.","atraso.","perda.","fuga."],"Art. 2º, parágrafo único, I.")
q(2,"No texto da fuga a pé, o guarda deveria priorizar, no lugar da arma de fogo,",["instrumentos de menor potencial ofensivo, se disponíveis.","a viatura.","o rádio.","o apito.","a algema, apenas."],"Art. 2º.","forca1a")
q(2,"No texto do bloqueio na avenida, a exceção que autorizaria o uso da arma seria o risco de morte ou lesão aos agentes ou a",["terceiros.","carros.","ruas.","placas.","prédios."],"Art. 2º, parágrafo único, II.","forca1b")
q(2,"No texto do uso do spray, a comunicação à família do homem atendido é exigida pelo art.",["6º.","2º.","3º.","4º.","5º."],"Art. 6º.","forca1c")
q(2,"O art. 8º da lei dispõe sobre a vigência, que se inicia na data de sua",["publicação.","regulamentação.","sanção.","revogação.","aprovação."],"Art. 8º.")
# n=3
q(3,"Assinale a alternativa correta sobre a Lei 13.060/2014.",["Prioriza os instrumentos de menor potencial ofensivo, veda arma de fogo contra fugitivo desarmado e contra veículo em bloqueio, salvo risco, e exige socorro imediato.","Veda os instrumentos de menor potencial ofensivo.","Autoriza arma de fogo contra qualquer veículo em bloqueio.","Dispensa socorro aos feridos.","Aplica-se apenas à polícia federal."],"Arts. 2º e 6º.")
q(3,"Considere. I. A priorização depende de não colocar em risco a integridade dos policiais. II. É legítimo atirar em fugitivo desarmado. III. O socorro aos feridos deve ser imediato. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Contra fugitivo desarmado, o uso de arma de fogo não é legítimo (art. 2º, parágrafo único).")
q(3,"Assinale a INCORRETA.",["O poder público não tem dever de fornecer os instrumentos.","Os cursos devem incluir conteúdo sobre instrumentos não letais.","O regulamento é editado pelo Poder Executivo.","O socorro aos feridos é imediato.","Os princípios são legalidade, necessidade e razoabilidade e proporcionalidade."],"O poder público tem o dever de fornecer (art. 5º).")
q(3,"O art. 2º impõe aos órgãos de segurança pública, além da priorização, que obedeçam a seguinte lista de princípios:",["legalidade; necessidade; razoabilidade e proporcionalidade.","moralidade; impessoalidade; publicidade.","eficiência; economicidade; celeridade.","urgência; oportunidade; discricionariedade.","especialidade; hierarquia; disciplina."],"Art. 2º, I a III.")
q(3,"A lei admite o uso de arma de fogo contra veículo que fura bloqueio apenas se o ato representar risco de morte ou lesão aos agentes de segurança pública ou a",["terceiros.","bens materiais.","outros motoristas, apenas.","a imagem da corporação.","a viatura, apenas."],"Art. 2º, parágrafo único, II.")
q(3,"A previsão de classificação dos instrumentos não letais por regulamento está no art.",["7º.","3º.","4º.","5º.","6º."],"Art. 7º.")
q(3,"O conceito do art. 4º inclui a ideia de que o instrumento é projetado especificamente para conter, debilitar ou incapacitar temporariamente pessoas, com baixa probabilidade de causar",["mortes ou lesões permanentes.","apenas dores.","apenas medo.","apenas atrasos.","apenas custos."],"Art. 4º.")
q(3,"A lei exige o fornecimento de instrumentos de menor potencial ofensivo para o uso racional da força, tarefa que cabe ao",["poder público.","particular.","sindicato.","cidadão.","condomínio."],"Art. 5º.")
q(3,"A obrigação de imediata assistência aos feridos abrange também a comunicação à família ou à pessoa por eles",["indicada.","contratada.","apontada pelo juiz.","apontada pelo comandante.","escolhida pela imprensa."],"Art. 6º.")
q(3,"O uso de arma de fogo contra fugitivo é ilegítimo quando ele esteja desarmado ou não represente risco imediato de morte ou lesão aos agentes ou a",["terceiros.","propriedades.","carros.","bens públicos.","comércio."],"Art. 2º, parágrafo único, I.")
q(3,"A priorização dos instrumentos de menor potencial ofensivo e os princípios do art. 2º dirigem-se aos",["órgãos de segurança pública.","cidadãos.","empresas.","escolas.","clubes."],"Art. 2º.")
q(3,"A capacitação sobre instrumentos não letais é dever imposto aos cursos de",["formação e capacitação dos agentes de segurança pública.","ensino fundamental.","medicina.","direito.","engenharia."],"Art. 3º.")
q(3,"A Lei 13.060/2014 foi regulamentada, quanto ao uso da força, por decreto de",["2024, no que tange ao Decreto 12.341.","1990.","1964.","1988.","2003."],"Decreto 12.341/2024, art. 1º.")
q(3,"No texto da fuga a pé, o guarda que saca a arma contra o homem desarmado em fuga contraria a vedação do art. 2º, parágrafo único, inciso",["I.","II.","III.","IV.","V."],"Art. 2º, parágrafo único, I.","forca1a")
q(3,"No texto da fuga a pé, a atuação legítima seria contê-lo com instrumento de menor potencial ofensivo ou meios que não ponham em risco a",["integridade de ninguém, respeitada a proporcionalidade.","reputação do guarda.","propriedade da loja.","patrulha.","sirene."],"Art. 2º.","forca1a")
q(3,"No texto do bloqueio na avenida, atirar contra o veículo sem risco imediato contraria o inciso II do",["parágrafo único do art. 2º.","art. 3º.","art. 4º.","art. 5º.","art. 6º."],"Art. 2º, parágrafo único, II.","forca1b")
q(3,"No texto do bloqueio na avenida, o princípio que impede o uso da arma é, em primeiro lugar, o da",["necessidade e proporcionalidade.","impessoalidade.","publicidade.","eficiência.","economicidade."],"Art. 2º.","forca1b")
q(3,"No texto do uso do spray, o spray de pimenta é, em regra, um instrumento de",["menor potencial ofensivo.","uso letal.","arma de fogo.","uso privado.","artilharia."],"Art. 4º.","forca1c")
q(3,"No texto do uso do spray, o socorro prestado ao homem que passou mal cumpre o art. 6º, que exige socorro",["imediato.","facultativo.","tardio.","eventual.","a critério do guarda."],"Art. 6º.","forca1c")
q(3,"No texto do uso do spray, o guarda pode usar instrumento de menor potencial ofensivo porque o poder público tem o dever de fornecê-lo, conforme o art.",["5º.","2º.","3º.","6º.","7º."],"Art. 5º.","forca1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Lei 13.060/2014: instrumentos de menor potencial ofensivo",[
 ("pri","Prioridade",["instrumentos não letais","sem risco ao policial"],"seção 1"),
 ("pci","Princípios",["legalidade","necessidade","razoabilidade e proporcionalidade"],"seção 1"),
 ("ved","Vedações",["fugitivo desarmado","veículo em bloqueio","salvo risco de morte ou lesão"],"seção 1"),
 ("con","Conceito",["baixa probabilidade de morte","conter, debilitar, incapacitar"],"seção 2"),
 ("for","Formação e fornecimento",["cursos com conteúdo","poder público fornece"],"seção 2"),
 ("soc","Socorro",["imediato","comunicar família"],"seção 3")],
 "Na prova: princípios, duas vedações e socorro imediato")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a prioridade, os princípios e as vedações; as demais, o conceito, o fornecimento e o socorro.","Fontes: Edital 02/2026, Anexo I; Lei 13.060/2014, texto de publicação original, Câmara dos Deputados. Exemplos criados para a aula.")
revisao("forca-1","Instrumentos de menor potencial ofensivo (Lei 13.060/2014)",Q,list(tx),
 cobertura=["Todos os artigos da lei (1º a 8º)."],
 pendencias=["Texto-fonte: publicação original da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto se houve alteração posterior.","Duas questões n2 e n3 mencionam o Decreto 12.341/2024 e a Lei 13.675/2018; conferir se cabem no recorte da aula.","Trechos de lei copiados de fontes/forca1.txt por programa.","Casos forca1a, forca1b e forca1c fictícios."],
 fontes_conferidas=["Lei 13.060/2014, arts. 1º a 8º: texto da Câmara, copiado por programa."])
gravar("forca-1",aula_html,banco("forca-1",Q),tx)
