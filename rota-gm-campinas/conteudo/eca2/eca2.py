import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='eca.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Capítulo II do Título II do ECA (arts. 15 a 18-B) trata de três direitos que se confundem na prova: liberdade, respeito e dignidade. Cada um tem conteúdo próprio, e a Vunesp costuma pedir o aspecto certo no direito certo. Os arts. 18-A e 18-B, a chamada Lei Menino Bernardo, proíbem o castigo físico e o tratamento cruel ou degradante e listam as medidas aplicáveis pelo Conselho Tutelar. Para o guarda, é a base para identificar maus-tratos e encaminhar a criança."
S={}
S[1]="## 1. Liberdade, respeito e dignidade\n\n"+L("art. 15","Art. 15. A criança e o adolescente têm direito","Art. 16.")+"\n\n"+L("art. 16","Art. 16. O direito à liberdade compreende","Art. 17.")+"\n\n"+L("art. 17","Art. 17. O direito ao respeito consiste","Art. 18.")+"""

A criança e o adolescente têm direito à liberdade, ao respeito e à dignidade como pessoas em processo de desenvolvimento e sujeitos de direitos civis, humanos e sociais. O direito à liberdade compreende sete aspectos: ir, vir e estar nos logradouros públicos e espaços comunitários, ressalvadas as restrições legais; opinião e expressão; crença e culto religioso; brincar, praticar esportes e divertir-se; participar da vida familiar e comunitária sem discriminação; participar da vida política, na forma da lei; e buscar refúgio, auxílio e orientação.

O direito ao respeito é a inviolabilidade da integridade física, psíquica e moral, abrangendo a preservação da imagem, da identidade, da autonomia, dos valores, ideias e crenças, dos espaços e objetos pessoais.
"""
S[2]="## 2. Dignidade e proibição de castigo físico\n\n"+L("art. 18","Art. 18. É dever de todos","Art. 18-A.")+"\n\n"+L("art. 18-A, caput","Art. 18-A. A criança e o adolescente têm o direito","Parágrafo único. Para os fins")+"\n\n"+L("art. 18-A, parágrafo único","Parágrafo único. Para os fins desta Lei","Art. 18-B.")+"""

É dever de todos velar pela dignidade da criança e do adolescente, pondo-os a salvo de qualquer tratamento desumano, violento, aterrorizante, vexatório ou constrangedor. Ao contrário de outros artigos, o dever aqui é de todos, e não só da família e do Estado.

A criança e o adolescente têm o direito de ser educados e cuidados sem castigo físico ou tratamento cruel ou degradante, como forma de correção, disciplina, educação ou qualquer pretexto, pelos pais, pela família ampliada, pelos responsáveis, pelos agentes públicos executores de medidas socioeducativas ou por qualquer pessoa encarregada de cuidar deles. Castigo físico é a ação disciplinar ou punitiva com uso da força física que resulte em sofrimento físico ou lesão. Tratamento cruel ou degradante é a conduta que humilhe, ameace gravemente ou ridicularize.
"""
S[3]="## 3. Medidas aplicáveis\n\n"+L("art. 18-B, caput e incisos","Art. 18-B. Os pais, os integrantes","Parágrafo único. As medidas previstas")+"\n\n"+L("art. 18-B, parágrafo único","Parágrafo único. As medidas previstas","CAPÍTULO III")+"""

Quem usar castigo físico ou tratamento cruel ou degradante fica sujeito, sem prejuízo de outras sanções, às medidas aplicadas conforme a gravidade do caso: encaminhamento a programa oficial ou comunitário de proteção à família; a tratamento psicológico ou psiquiátrico; a cursos ou programas de orientação; obrigação de encaminhar a criança a tratamento especializado; advertência; e garantia de tratamento de saúde especializado à vítima. As medidas são aplicadas pelo Conselho Tutelar, sem prejuízo de outras providências legais. Atenção: advertência é a mais branda, e a lei não prevê, nesse artigo, multa nem perda do poder familiar.
"""
S[5]="""## 5. Na rotina do guarda

- **Criança na rua:** o direito de ir, vir e estar nos logradouros públicos vale para crianças e adolescentes, salvo as restrições legais; a mera presença não justifica abordagem.
- **Castigo físico ou humilhação:** o guarda que presencia deve intervir, proteger a criança e comunicar o Conselho Tutelar.
- **Imagem:** o respeito inclui a preservação da imagem; o guarda não divulga imagem de criança atendida.
- **Dever de todos:** o art. 18 obriga também o agente público a pôr a criança a salvo de tratamento vexatório.
- **Medidas:** quem aplica as medidas do art. 18-B é o Conselho Tutelar, não o guarda.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Liberdade x respeito x dignidade | Liberdade: sete aspectos; respeito: inviolabilidade e imagem, identidade; dignidade: pôr a salvo de tratamento desumano |
| Dever do art. 18 | De todos |
| Castigo físico | Força física que resulte em sofrimento físico ou lesão |
| Tratamento cruel ou degradante | Humilha, ameaça gravemente ou ridiculariza |
| Quem aplica as medidas | Conselho Tutelar |
| Medidas do art. 18-B | Programa de proteção, tratamento psicológico, cursos, tratamento especializado, advertência, saúde da vítima |
| Participar da vida política | Na forma da lei |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 15 | Liberdade, respeito e dignidade; sujeitos de direitos |
| Art. 16 | Sete aspectos da liberdade |
| Art. 17 | Inviolabilidade física, psíquica e moral; imagem, identidade |
| Art. 18 | Dever de todos de velar pela dignidade |
| Art. 18-A | Proibido castigo físico e tratamento cruel ou degradante |
| Castigo físico | Força física que cause sofrimento ou lesão |
| Cruel ou degradante | Humilhar, ameaçar gravemente, ridicularizar |
| Art. 18-B | Medidas, aplicadas pelo Conselho Tutelar |
"""
QR=[("Questão 1","O direito à liberdade compreende, entre outros aspectos, ir, vir e estar nos logradouros públicos e espaços comunitários, ressalvadas as",["restrições legais.","ordens dos pais.","decisões da escola.","opiniões da comunidade.","regras do bairro."],0,"Art. 16, I."),
("Questão 2","O direito ao respeito consiste na inviolabilidade da integridade física, psíquica e",["moral da criança e do adolescente.","patrimonial.","financeira.","política.","religiosa, apenas."],1,"Art. 17."),
("Questão 3","As medidas do art. 18-B, aplicáveis a quem usar castigo físico, serão aplicadas pelo",["Conselho Tutelar, sem prejuízo de outras providências legais.","delegado de polícia.","diretor da escola.","prefeito.","guarda municipal."],2,"Art. 18-B, parágrafo único."),
("Questão 4","Considera-se tratamento cruel ou degradante a conduta que humilhe, ameace gravemente ou",["ridicularize.","eduque.","oriente.","aconselhe.","corrija verbalmente."],3,"Art. 18-A, parágrafo único, II.")]
t1="<strong>Criança na praça</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, viu um grupo de crianças brincando numa praça pública. Um morador reclamou e pediu que fossem retiradas."
t2="<strong>Castigo no mercado</strong><br><br>Num mercado de Vila Nova, um pai deu um tapa forte no rosto do filho de oito anos, que ficou com o rosto marcado, e o chamou de burro diante de todos."
t3="<strong>Escola de futebol</strong><br><br>Um treinador de uma escolinha mantida pelo Município humilhou diante do grupo um menino de onze anos que errou um passe, dizendo que ele era inútil, e o obrigou a correr até passar mal."
tx={"eca2a":t1,"eca2b":t2,"eca2c":t3}
# n=1
q(1,"A criança e o adolescente têm direito à liberdade, ao respeito e à dignidade como pessoas humanas em",["processo de desenvolvimento.","idade adulta.","fase final.","condição de dependência total.","situação de risco."],"Art. 15.")
q(1,"O direito à liberdade compreende o direito de brincar, praticar esportes e",["divertir-se.","trabalhar.","votar.","dirigir.","contratar."],"Art. 16, IV.")
q(1,"O direito à liberdade compreende a opinião e a",["expressão.","contratação.","tutela.","guarda.","adoção."],"Art. 16, II.")
q(1,"O direito à liberdade compreende a crença e o",["culto religioso.","partido político.","sindicato.","trabalho.","comércio."],"Art. 16, III.")
q(1,"O direito de participar da vida política, para a criança e o adolescente, é exercido",["na forma da lei.","livremente, sem limites.","apenas aos 12 anos.","apenas por voto.","apenas por filiação."],"Art. 16, VI.")
q(1,"A criança e o adolescente têm direito de buscar refúgio, auxílio e",["orientação.","pagamento.","emprego.","contrato.","tutela."],"Art. 16, VII.")
q(1,"O direito ao respeito abrange a preservação da imagem, da identidade, da autonomia, dos valores, ideias e crenças e dos espaços e",["objetos pessoais.","bens da família.","contas bancárias.","terras.","veículos."],"Art. 17.")
q(1,"É dever de todos velar pela dignidade da criança e do adolescente, pondo-os a salvo de qualquer tratamento desumano, violento, aterrorizante, vexatório ou",["constrangedor.","educativo.","disciplinar.","financeiro.","religioso."],"Art. 18.")
q(1,"A criança e o adolescente têm direito de ser educados e cuidados sem o uso de castigo físico ou de tratamento",["cruel ou degradante.","carinhoso.","diligente.","educativo.","afetuoso."],"Art. 18-A.")
q(1,"Castigo físico é a ação de natureza disciplinar ou punitiva aplicada com o uso da",["força física sobre a criança ou o adolescente.","voz.","palavra.","autoridade moral.","riqueza."],"Art. 18-A, parágrafo único, I.")
q(1,"O castigo físico, para os fins do Estatuto, resulta em sofrimento físico ou",["lesão.","aprendizado.","correção.","desinteresse.","ganho."],"Art. 18-A, parágrafo único, I.")
q(1,"As medidas do art. 18-B serão aplicadas de acordo com a",["gravidade do caso.","vontade do infrator.","idade do pai.","renda da família.","opinião do vizinho."],"Art. 18-B.")
q(1,"Entre as medidas do art. 18-B está o encaminhamento a programa oficial ou comunitário de proteção à",["família.","empresa.","escola de futebol.","delegacia.","prisão."],"Art. 18-B, I.")
q(1,"Entre as medidas do art. 18-B está o encaminhamento a tratamento psicológico ou",["psiquiátrico.","esportivo.","religioso.","musical.","turístico."],"Art. 18-B, II.")
q(1,"A advertência é uma das medidas aplicáveis a quem usa castigo físico, aplicada pelo",["Conselho Tutelar.","juiz de paz.","comerciante.","vizinho.","prefeito."],"Art. 18-B, V e parágrafo único.")
q(1,"A garantia de tratamento de saúde especializado é medida em favor da",["vítima.","escola.","comunidade.","imprensa.","empresa."],"Art. 18-B, VI.")
q(1,"O direito à liberdade inclui participar da vida familiar e comunitária, sem",["discriminação.","avaliação.","autorização judicial.","pagamento.","cadastro."],"Art. 16, V.")
q(1,"No texto da criança na praça, o direito de ir, vir e estar nos logradouros públicos decorre do art. 16, inciso",["I.","II.","III.","VI.","VII."],"Art. 16, I.","eca2a")
q(1,"No texto do castigo no mercado, o tapa com marca no rosto configura, em tese,",["castigo físico.","educação regular.","brincadeira.","exercício regular de direito.","direito de correção."],"Art. 18-A, parágrafo único, I.","eca2b")
q(1,"No texto da escola de futebol, humilhar o menino diante do grupo é, em tese,",["tratamento cruel ou degradante.","método pedagógico.","direito do treinador.","exercício regular.","elogio."],"Art. 18-A, parágrafo único, II.","eca2c")
# n=2
q(2,"A criança e o adolescente são, segundo o art. 15, sujeitos de direitos civis, humanos e sociais garantidos na Constituição e nas",["leis.","tradições.","decisões da família.","regras da escola.","portarias."],"Art. 15.")
q(2,"O direito de ir, vir e estar nos logradouros públicos é aspecto do direito à",["liberdade.","dignidade.","convivência.","educação.","saúde."],"Art. 16, I.")
q(2,"A preservação da imagem e da identidade da criança é aspecto do direito ao",["respeito.","lazer.","trabalho.","voto.","esporte."],"Art. 17.")
q(2,"O art. 18, que impõe velar pela dignidade, atribui o dever a",["todos.","apenas à família.","apenas ao Estado.","apenas à escola.","apenas aos pais."],"Art. 18.")
q(2,"O direito de ser educado sem castigo físico vale perante os pais, a família ampliada, os responsáveis, os agentes públicos executores de medidas socioeducativas e",["qualquer pessoa encarregada de cuidar da criança.","somente os pais.","somente o professor.","somente o juiz.","somente o guarda."],"Art. 18-A.")
q(2,"Tratamento cruel ou degradante é a conduta ou forma cruel de tratamento que humilhe, ameace gravemente ou",["ridicularize.","aconselhe.","oriente.","eduque.","compense."],"Art. 18-A, parágrafo único, II.")
q(2,"As medidas do art. 18-B são aplicadas sem prejuízo de outras",["sanções cabíveis.","isenções.","anistias.","liberações.","gratificações."],"Art. 18-B.")
q(2,"Entre as medidas do art. 18-B está o encaminhamento a cursos ou programas de",["orientação.","esporte.","lazer.","turismo.","comércio."],"Art. 18-B, III.")
q(2,"Entre as medidas do art. 18-B está a obrigação de encaminhar a criança a tratamento",["especializado.","religioso.","esportivo.","artístico.","comercial."],"Art. 18-B, IV.")
q(2,"As medidas do art. 18-B são aplicadas pelo Conselho Tutelar, sem prejuízo de outras",["providências legais.","isenções fiscais.","comissões.","disputas.","anistias."],"Art. 18-B, parágrafo único.")
q(2,"O direito à liberdade compreende participar da vida familiar e comunitária, sem",["discriminação.","autorização.","taxa.","limite de idade.","cadastro."],"Art. 16, V.")
q(2,"Na descrição do castigo físico, a ação tem natureza",["disciplinar ou punitiva.","apenas educativa.","apenas médica.","apenas religiosa.","apenas esportiva."],"Art. 18-A, parágrafo único, I.")
q(2,"A criança tem direito de ser cuidada sem castigo físico, como forma de correção, disciplina, educação ou qualquer outro",["pretexto.","meio.","fim.","horário.","local."],"Art. 18-A.")
q(2,"A inviolabilidade da integridade física, psíquica e moral é o conceito legal do direito ao",["respeito.","lazer.","brincar.","voto.","culto."],"Art. 17.")
q(2,"A vedação ao tratamento desumano, violento, aterrorizante, vexatório ou constrangedor está no artigo sobre",["dignidade.","liberdade.","educação.","saúde.","lazer."],"Art. 18.")
q(2,"As medidas do art. 18-B incluem o encaminhamento a programa oficial ou comunitário de proteção à família e a",["advertência.","multa.","prisão.","perda do poder familiar, automática.","demissão."],"Art. 18-B, I e V.")
q(2,"No texto da criança na praça, a restrição à presença das crianças só seria possível se houvesse",["restrição legal.","queixa de um morador.","ordem do síndico.","vontade do guarda.","costume local."],"Art. 16, I.","eca2a")
q(2,"No texto do castigo no mercado, chamar o filho de burro diante de todos configura, em tese, tratamento",["degradante, por humilhar.","educativo.","irrelevante.","autorizado.","permitido."],"Art. 18-A, parágrafo único, II, a.","eca2b")
q(2,"No texto da escola de futebol, o treinador é agente a que se aplica o art. 18-A porque é",["pessoa encarregada de cuidar, educar ou proteger a criança.","parente.","vizinho.","juiz.","fiscal."],"Art. 18-A.","eca2c")
q(2,"O art. 18-A trata do direito de ser educado e cuidado sem uso de castigo físico ou de tratamento",["cruel ou degradante.","afetuoso.","pedagógico.","gentil.","regular."],"Art. 18-A.")
# n=3
q(3,"Assinale a alternativa correta sobre o direito à liberdade.",["Compreende opinião e expressão, crença e culto religioso e brincar e praticar esportes, entre outros aspectos.","Não compreende a opinião.","Compreende o voto sem limites aos 12 anos.","Exclui o direito de brincar.","Compreende só o direito de ir e vir."],"Art. 16.")
q(3,"Considere. I. O dever de velar pela dignidade é de todos. II. O castigo físico é permitido como forma de correção. III. As medidas do art. 18-B são aplicadas pelo Conselho Tutelar. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O castigo físico é vedado (art. 18-A).")
q(3,"Assinale a INCORRETA.",["As medidas do art. 18-B são aplicadas pelo delegado de polícia.","As medidas do art. 18-B incluem a advertência.","O castigo físico resulta em sofrimento físico ou lesão.","O tratamento degradante inclui ameaçar gravemente.","O art. 18 impõe a todos velar pela dignidade."],"As medidas são aplicadas pelo Conselho Tutelar (art. 18-B, parágrafo único).")
q(3,"A lista do art. 16 NÃO inclui, expressamente, o direito de",["exercer atividade remunerada.","buscar refúgio, auxílio e orientação.","opinião e expressão.","brincar e praticar esportes.","crença e culto religioso."],"Art. 16.")
q(3,"A inviolabilidade abrange a preservação da imagem, da identidade, da autonomia, dos valores, ideias e crenças e dos espaços e objetos pessoais, conforme o direito ao",["respeito.","lazer.","convívio.","transporte.","voto."],"Art. 17.")
q(3,"O castigo físico diferencia-se do tratamento cruel ou degradante porque, no primeiro, há uso da",["força física, com sofrimento ou lesão.","voz.","omissão.","privação alimentar, apenas.","ameaça verbal, apenas."],"Art. 18-A, parágrafo único.")
q(3,"A conduta que ameace gravemente a criança é exemplo de tratamento",["cruel ou degradante.","educativo.","lícito.","regular.","pedagógico."],"Art. 18-A, parágrafo único, II, b.")
q(3,"O art. 18-A vale também perante os agentes públicos executores de medidas",["socioeducativas.","de segurança.","tributárias.","ambientais.","sanitárias."],"Art. 18-A.")
q(3,"A medida de garantia de tratamento de saúde especializado à vítima é a de inciso",["VI do art. 18-B.","I do art. 18-B.","III do art. 18-B.","V do art. 18-B.","II do art. 18-B."],"Art. 18-B, VI.")
q(3,"Segundo o art. 18-B, as medidas são aplicadas de acordo com a gravidade do caso e sem prejuízo de",["outras sanções cabíveis.","anistia.","recurso suspensivo.","sigilo absoluto.","extinção da punibilidade."],"Art. 18-B.")
q(3,"A liberdade de participar da vida política vale, para a criança e o adolescente,",["na forma da lei.","sem limites.","apenas após os 16 anos, sempre.","nunca.","apenas em partidos."],"Art. 16, VI.")
q(3,"O direito de ir, vir e estar nos logradouros públicos e espaços comunitários tem as restrições",["legais.","da família, apenas.","da escola, apenas.","do guarda, a critério.","do bairro."],"Art. 16, I.")
q(3,"O dever de pôr a criança a salvo de tratamento vexatório ou constrangedor está no art.",["18.","15.","16.","17.","18-B."],"Art. 18.")
q(3,"O art. 18-A protege a criança contra o castigo físico mesmo quando aplicado como forma de",["correção, disciplina ou educação.","apenas crime.","apenas esporte.","apenas lazer.","apenas trabalho."],"Art. 18-A.")
q(3,"No art. 18-B, a medida de encaminhamento a tratamento psicológico ou psiquiátrico destina-se a quem",["utilizou castigo físico ou tratamento cruel ou degradante.","sofreu apenas.","presenciou apenas.","apenas ao pai.","apenas à escola."],"Art. 18-B, II.")
q(3,"No texto da criança na praça, o pedido do morador para retirar as crianças da praça",["não se sustenta, pois a presença nos logradouros é direito.","é ordem a cumprir.","é lei.","é direito do morador.","deve ser atendido sempre."],"Art. 16, I.","eca2a")
q(3,"No texto do castigo no mercado, o caso deve ser comunicado ao Conselho Tutelar, que pode aplicar medidas como",["encaminhamento a programa de proteção à família e advertência.","multa e prisão.","perda automática do poder familiar.","demissão.","apreensão do filho."],"Art. 18-B.","eca2b")
q(3,"No texto da escola de futebol, obrigar o menino a correr até passar mal, para puni-lo, configura, em tese,",["castigo físico, se resultar em sofrimento físico.","exercício regular.","treino aceito sempre.","brincadeira.","direito do treinador."],"Art. 18-A, parágrafo único, I.","eca2c")
q(3,"No texto da escola de futebol, o dever de velar pela dignidade do menino cabia também ao treinador, pois o art. 18 atribui o dever a",["todos.","apenas à família.","apenas ao Estado.","apenas aos pais.","apenas ao juiz."],"Art. 18.","eca2c")
q(3,"No texto do castigo no mercado, o tapa e a humilhação em público violam o direito ao",["respeito, à integridade física e moral.","lazer.","voto.","esporte.","transporte."],"Art. 17.","eca2b")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("ECA: arts. 15 a 18-B",[
 ("lib","Liberdade",["7 aspectos","ir, vir e estar","opinião, culto, brincar"],"seção 1"),
 ("res","Respeito",["integridade física, psíquica e moral","imagem e identidade","espaços e objetos"],"seção 1"),
 ("dig","Dignidade",["dever de todos","a salvo de tratamento vexatório","art. 18"],"seção 2"),
 ("cas","Castigo físico",["força física","sofrimento ou lesão","vedado"],"seção 2"),
 ("cru","Cruel ou degradante",["humilha","ameaça gravemente","ridiculariza"],"seção 2"),
 ("med","Medidas",["programa de proteção","tratamento, cursos","advertência; Conselho Tutelar"],"seção 3")],
 "Na prova: diferença entre os três direitos e as medidas do art. 18-B")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz liberdade e respeito; as demais, dignidade, castigo físico e medidas.","Fontes: Edital 02/2026, Anexo I; Lei 8.069/1990 (ECA), arts. 15 a 18-B, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("eca-2","ECA: liberdade, respeito e dignidade (arts. 15 a 18-B)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (15 a 18-B)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Trechos de lei copiados de fontes/eca.txt por programa.","Casos eca2a, eca2b e eca2c fictícios."],
 fontes_conferidas=["ECA, arts. 15 a 18-B: texto da Câmara, copiado por programa."])
gravar("eca-2",aula_html,banco("eca-2",Q),tx)
