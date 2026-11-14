import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='mp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Lei Maria da Penha (Lei 11.340/2006) cria mecanismos para coibir e prevenir a violência doméstica e familiar contra a mulher. Os arts. 1º a 7º trazem o conceito: o que é violência doméstica e familiar (ação ou omissão baseada no gênero), onde ela ocorre (unidade doméstica, família, relação íntima de afeto) e as formas que assume (física, psicológica, sexual, patrimonial, moral e, na redação atual, vicária). Para o guarda, é a base do primeiro atendimento: reconhecer a violência e saber que ela independe de coabitação e de orientação sexual."
S={}
S[1]="## 1. Objeto, direitos e interpretação\n\n"+L("art. 1º","Art. 1º Esta Lei cria mecanismos","Art. 2º")+"\n\n"+L("art. 2º","Art. 2º Toda mulher","Art. 3º")+"\n\n"+L("art. 3º","Art. 3º Serão asseguradas","Art. 4º")+"\n\n"+L("art. 4º","Art. 4º Na interpretação","TÍTULO II")+"""

A lei cria mecanismos para coibir e prevenir a violência doméstica e familiar contra a mulher, com base no art. 226, § 8º, da Constituição e em tratados internacionais, dispõe sobre os Juizados de Violência Doméstica e Familiar contra a Mulher e estabelece medidas de assistência e proteção. Toda mulher, independentemente de classe, raça, etnia, orientação sexual, renda, cultura, nível educacional, idade e religião, goza dos direitos fundamentais da pessoa humana e tem asseguradas as oportunidades para viver sem violência.

Cabe à família, à sociedade e ao poder público criar as condições para o efetivo exercício dos direitos. Na interpretação da lei consideram-se os fins sociais a que se destina e as condições peculiares das mulheres em situação de violência doméstica e familiar.
"""
S[2]="## 2. Conceito de violência doméstica e familiar\n\n"+L("art. 5º","Art. 5º Para os efeitos desta Lei","Art. 6º")+"\n\n"+L("art. 6º","Art. 6º A violência doméstica","CAPÍTULO II")+"""

Configura violência doméstica e familiar contra a mulher qualquer ação ou omissão baseada no gênero que lhe cause morte, lesão, sofrimento físico, sexual ou psicológico e dano moral ou patrimonial. A violência se dá em três âmbitos: da unidade doméstica (espaço de convívio permanente de pessoas, com ou sem vínculo familiar, inclusive as esporadicamente agregadas); da família (comunidade de indivíduos que são ou se consideram aparentados, por laços naturais, afinidade ou vontade expressa); e de qualquer relação íntima de afeto, em que o agressor conviva ou tenha convivido com a ofendida, independentemente de coabitação. As relações independem de orientação sexual. A violência doméstica e familiar é forma de violação dos direitos humanos.
"""
S[3]="## 3. Formas de violência\n\n"+L("art. 7º, I e II","Art. 7º São formas de violência doméstica","III - a violência sexual")+"\n\n"+L("art. 7º, III","III - a violência sexual","IV - a violência patrimonial")+"\n\n"+L("art. 7º, IV a VI","IV - a violência patrimonial","TÍTULO III")+"""

São formas de violência doméstica e familiar, entre outras: a violência física (conduta que ofenda a integridade ou saúde corporal); a psicológica (conduta que cause dano emocional e diminuição da autoestima, ou vise degradar ou controlar ações, comportamentos, crenças e decisões, mediante ameaça, constrangimento, humilhação, manipulação, isolamento, vigilância constante, perseguição contumaz, insulto, chantagem, violação da intimidade, ridicularização, exploração e limitação do direito de ir e vir); a sexual (constranger a presenciar, manter ou participar de relação sexual não desejada, ou impedir o uso de contraceptivo, forçar ao matrimônio, gravidez, aborto ou prostituição); a patrimonial (retenção, subtração ou destruição de objetos, instrumentos de trabalho, documentos pessoais, bens, valores e recursos econômicos); a moral (calúnia, difamação ou injúria); e a vicária (violência contra descendente, ascendente, dependente, enteado, parente ou pessoa de sua rede de apoio, com vistas a atingi-la).
"""
S[5]="""## 5. Na rotina do guarda

- **Chamado por violência doméstica:** a violência independe de coabitação, de casamento e de orientação sexual; basta relação íntima de afeto, atual ou passada.
- **Reconhecer as formas:** além da agressão física, o guarda registra ameaças, perseguição, retenção de documentos e destruição de objetos.
- **Rede de apoio:** a violência vicária contra filhos ou parentes para atingir a mulher também é violência doméstica.
- **Primeiro atendimento:** o guarda garante a segurança da mulher, encaminha à delegacia e à rede de proteção e não minimiza a ocorrência.
- **Direitos humanos:** a violência doméstica é violação de direitos humanos, e a mulher tem direito a viver sem violência.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Base do conceito | Ação ou omissão baseada no gênero |
| Resultados possíveis | Morte, lesão, sofrimento físico, sexual ou psicológico, dano moral ou patrimonial |
| Três âmbitos | Unidade doméstica, família e relação íntima de afeto |
| Coabitação | Não é exigida; vale quem convive ou conviveu |
| Orientação sexual | As relações independem dela |
| Formas de violência | Física, psicológica, sexual, patrimonial, moral e vicária |
| Violência moral | Calúnia, difamação ou injúria |
| Violência patrimonial | Retenção, subtração ou destruição de objetos, documentos, bens, valores |
| Violência psicológica | Ameaça, humilhação, isolamento, vigilância, perseguição |
| Natureza | Violação dos direitos humanos |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Mecanismos para coibir e prevenir; Juizados |
| Art. 2º | Todos os direitos, sem distinção |
| Art. 3º | Condições para exercer direitos; dever da família, sociedade e poder público |
| Art. 4º | Interpretação: fins sociais e condições peculiares |
| Art. 5º | Ação ou omissão baseada no gênero |
| Âmbitos | Unidade doméstica, família, relação íntima de afeto |
| Art. 6º | Violação dos direitos humanos |
| Art. 7º, I | Física |
| Art. 7º, II | Psicológica |
| Art. 7º, III | Sexual |
| Art. 7º, IV | Patrimonial |
| Art. 7º, V | Moral |
| Art. 7º, VI | Vicária |
"""
QR=[("Questão 1","Configura violência doméstica e familiar contra a mulher qualquer ação ou omissão baseada no",["gênero que lhe cause morte, lesão, sofrimento ou dano.","status econômico.","grau de instrução.","estado civil.","local de moradia."],0,"Art. 5º."),
("Questão 2","A violência patrimonial é entendida como qualquer conduta que configure retenção, subtração, destruição parcial ou total de seus objetos, instrumentos de trabalho, documentos pessoais, bens, valores e",["direitos ou recursos econômicos.","amizades.","estudos.","viagens.","emprego."],1,"Art. 7º, IV."),
("Questão 3","A violência moral é entendida como qualquer conduta que configure",["calúnia, difamação ou injúria.","lesão corporal.","constrangimento sexual.","retenção de documentos.","ameaça física."],2,"Art. 7º, V."),
("Questão 4","As relações pessoais que configuram violência doméstica e familiar independem de",["orientação sexual.","gênero.","convivência passada.","parentesco.","afeto."],3,"Art. 5º, parágrafo único.")]
t1="<strong>Briga de ex-namorados</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, atendeu uma mulher que dizia ser perseguida pelo ex-namorado, com quem nunca morou, que a seguia diariamente e a ameaçava por mensagens."
t2="<strong>Documentos retidos</strong><br><br>Um homem de Vila Nova retinha os documentos pessoais e o cartão da conta da companheira e destruiu seus instrumentos de trabalho depois de uma discussão."
t3="<strong>Ameaça a parente</strong><br><br>Após a separação, um homem de Vila Nova passou a ameaçar a mãe e o filho da ex-companheira, dizendo que os machucaria para atingi-la."
tx={"mp1a":t1,"mp1b":t2,"mp1c":t3}
# n=1
q(1,"A Lei Maria da Penha cria mecanismos para coibir e prevenir a violência doméstica e familiar contra a",["mulher.","criança.","pessoa idosa.","pessoa com deficiência.","comunidade."],"Art. 1º.")
q(1,"A lei dispõe sobre a criação dos Juizados de Violência Doméstica e Familiar contra a",["Mulher.","Criança.","Família.","Pessoa Idosa.","Comunidade."],"Art. 1º.")
q(1,"Toda mulher, independentemente de classe, raça, etnia, orientação sexual, renda, cultura, nível educacional, idade e religião, goza dos direitos fundamentais inerentes à",["pessoa humana.","classe média.","família.","comunidade.","empresa."],"Art. 2º.")
q(1,"Cabe à família, à sociedade e ao poder público criar as condições necessárias para o efetivo exercício dos",["direitos enunciados no caput.","deveres da mulher.","deveres do agressor.","direitos do agressor.","contratos."],"Art. 3º, § 2º.")
q(1,"Na interpretação da lei serão considerados os fins sociais a que ela se destina e as condições peculiares das mulheres em situação de",["violência doméstica e familiar.","trabalho.","estudo.","viagem.","lazer."],"Art. 4º.")
q(1,"A violência doméstica e familiar contra a mulher constitui uma das formas de violação dos direitos",["humanos.","civis apenas.","tributários.","políticos apenas.","comerciais."],"Art. 6º.")
q(1,"A violência física é entendida como qualquer conduta que ofenda a integridade ou a saúde",["corporal.","mental.","financeira.","social.","moral."],"Art. 7º, I.")
q(1,"A violência psicológica inclui conduta que cause dano emocional e diminuição da",["autoestima.","renda.","saúde física.","moradia.","escolaridade."],"Art. 7º, II.")
q(1,"A violência sexual inclui a conduta que impeça a mulher de usar qualquer método",["contraceptivo.","de pagamento.","de transporte.","de estudo.","de trabalho."],"Art. 7º, III.")
q(1,"A violência patrimonial inclui a retenção de documentos",["pessoais.","do agressor.","da escola.","do vizinho.","da empresa."],"Art. 7º, IV.")
q(1,"A violência moral é a conduta que configure calúnia, difamação ou",["injúria.","lesão.","ameaça.","omissão.","retenção."],"Art. 7º, V.")
q(1,"A violência vicária é praticada contra descendente, ascendente, dependente, enteado, parente ou pessoa de sua rede de apoio, com vistas a",["atingir a mulher.","atingir o agressor.","atingir a justiça.","proteger a mulher.","beneficiar a família."],"Art. 7º, VI.")
q(1,"A violência doméstica pode ocorrer no âmbito da unidade doméstica, da família ou de qualquer relação íntima de",["afeto.","trabalho.","amizade.","vizinhança.","estudo."],"Art. 5º, III.")
q(1,"Na relação íntima de afeto, a violência se configura independentemente de",["coabitação.","gênero.","agressão.","ameaça.","denúncia."],"Art. 5º, III.")
q(1,"A unidade doméstica é compreendida como o espaço de convívio permanente de pessoas, com ou sem vínculo familiar, inclusive as esporadicamente",["agregadas.","visitantes.","contratadas.","vizinhas.","hospedadas em hotel."],"Art. 5º, I.")
q(1,"A família é compreendida como a comunidade formada por indivíduos que são ou se consideram",["aparentados.","amigos.","colegas.","vizinhos.","sócios."],"Art. 5º, II.")
q(1,"No texto da briga de ex-namorados, a perseguição e a ameaça por mensagens configuram violência",["psicológica.","patrimonial.","apenas física.","apenas moral.","apenas sexual."],"Art. 7º, II.","mp1a")
q(1,"No texto dos documentos retidos, a retenção dos documentos da companheira configura violência",["patrimonial.","moral.","vicária.","sexual.","psicológica, apenas."],"Art. 7º, IV.","mp1b")
q(1,"No texto da ameaça a parente, a ameaça ao filho para atingir a mulher configura violência",["vicária.","moral.","patrimonial.","sexual.","física."],"Art. 7º, VI.","mp1c")
q(1,"O art. 6º da Lei Maria da Penha define a violência doméstica e familiar contra a mulher como forma de violação dos direitos",["humanos.","tributários.","comerciais.","processuais.","contratuais."],"Art. 6º.")
# n=2
q(2,"A lei estabelece medidas de assistência e proteção às mulheres em situação de violência doméstica e",["familiar.","urbana.","rural.","comunitária.","pública."],"Art. 1º.")
q(2,"O poder público desenvolverá políticas que visem garantir os direitos humanos das mulheres no âmbito das relações domésticas e",["familiares.","comerciais.","trabalhistas.","escolares.","esportivas."],"Art. 3º, § 1º.")
q(2,"Entre as condições asseguradas às mulheres no art. 3º estão a vida, a segurança, a saúde, a alimentação, a educação, a cultura, a moradia e o acesso à",["justiça.","propriedade.","herança.","política partidária.","carreira militar."],"Art. 3º.")
q(2,"A ação ou omissão que configura violência doméstica pode causar dano moral ou",["patrimonial.","social.","político.","tributário.","trabalhista."],"Art. 5º.")
q(2,"As relações pessoais do art. 5º independem de orientação",["sexual.","política.","religiosa.","econômica.","escolar."],"Art. 5º, parágrafo único.")
q(2,"A violência psicológica inclui a limitação do direito de",["ir e vir.","estudar.","votar.","trabalhar apenas.","dormir."],"Art. 7º, II.")
q(2,"A violência psicológica inclui a vigilância constante e a perseguição",["contumaz.","eventual.","autorizada.","legal.","casual."],"Art. 7º, II.")
q(2,"A violência sexual inclui forçar a mulher ao matrimônio, à gravidez, ao aborto ou à",["prostituição.","viagem.","festa.","escola.","reunião."],"Art. 7º, III.")
q(2,"A violência sexual pode ocorrer mediante intimidação, ameaça, coação ou uso da",["força.","palavra.","carta.","lei.","amizade."],"Art. 7º, III.")
q(2,"A violência patrimonial inclui a destruição de instrumentos de",["trabalho.","lazer.","festa.","viagem.","transporte público."],"Art. 7º, IV.")
q(2,"A violência patrimonial inclui a retenção dos recursos econômicos, inclusive os destinados a satisfazer as necessidades da",["mulher.","empresa.","escola.","vizinhança.","família do agressor."],"Art. 7º, IV.")
q(2,"As formas de violência do art. 7º são enumeradas",["entre outras (rol exemplificativo).","de forma taxativa.","apenas em lei estadual.","apenas por decreto.","apenas pelo juiz."],"Art. 7º, caput.")
q(2,"A violência psicológica pode se dar mediante ameaça, constrangimento, humilhação, manipulação, isolamento, insulto, chantagem e",["ridicularização.","elogio.","aviso.","conselho.","orientação."],"Art. 7º, II.")
q(2,"A lei foi editada nos termos do art. 226, § 8º, da",["Constituição Federal.","Constituição Estadual.","Lei Orgânica Municipal.","Código Civil.","Código Penal."],"Art. 1º.")
q(2,"No texto da briga de ex-namorados, a ausência de convivência com o ex-namorado",["não afasta a configuração, pois a lei exige relação íntima de afeto, independentemente de coabitação.","afasta a violência doméstica.","impede a aplicação da lei.","exige casamento.","exige filhos."],"Art. 5º, III.","mp1a")
q(2,"No texto dos documentos retidos, a destruição de instrumentos de trabalho também configura violência",["patrimonial.","vicária.","moral.","sexual.","apenas psicológica."],"Art. 7º, IV.","mp1b")
q(2,"No texto da ameaça a parente, a mãe e o filho da ex-companheira são atingidos como pessoas da",["rede de apoio ou descendente da mulher.","empresa.","vizinhança.","escola.","clientela."],"Art. 7º, VI.","mp1c")
q(2,"A violência psicológica pode se configurar por meio de insulto, chantagem e violação de sua",["intimidade.","carteira de trabalho.","conta bancária.","propriedade.","escola."],"Art. 7º, II.")
q(2,"A violência doméstica e familiar abrange também a esporadicamente agregada à unidade doméstica, pois a unidade doméstica inclui as pessoas",["esporadicamente agregadas.","ausentes.","desconhecidas.","vizinhas.","contratadas por hora."],"Art. 5º, I.")
q(2,"A violência patrimonial pode atingir os objetos e instrumentos de trabalho, documentos pessoais, bens, valores e direitos ou recursos",["econômicos.","políticos.","religiosos.","esportivos.","culturais."],"Art. 7º, IV.")
# n=3
q(3,"Assinale a alternativa que traz apenas formas de violência previstas no art. 7º.",["Física, psicológica, sexual, patrimonial, moral e vicária.","Física, social e esportiva.","Psicológica, política e religiosa.","Sexual, comercial e tributária.","Moral, civil e penal."],"Art. 7º.")
q(3,"Considere. I. A violência doméstica independe de coabitação. II. A violência moral é calúnia, difamação ou injúria. III. As relações do art. 5º dependem da orientação sexual. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"As relações independem de orientação sexual (art. 5º, parágrafo único).")
q(3,"Assinale a INCORRETA.",["A violência doméstica exige coabitação.","A violência pode ocorrer na unidade doméstica.","A violência pode ocorrer em relação íntima de afeto.","A violência é violação dos direitos humanos.","A violência vicária é forma prevista no art. 7º."],"Não se exige coabitação (art. 5º, III).")
q(3,"Entre as formas de violência psicológica NÃO consta expressamente",["a lesão corporal.","a humilhação.","o isolamento.","a chantagem.","a ridicularização."],"A lesão corporal é violência física (art. 7º, I).")
q(3,"A violência sexual inclui conduta que limite ou anule o exercício dos direitos sexuais e",["reprodutivos.","políticos.","civis.","trabalhistas.","tributários."],"Art. 7º, III.")
q(3,"A violência psicológica pode vir da exploração e da violação da",["intimidade.","empresa.","herança.","renda.","dívida."],"Art. 7º, II.")
q(3,"A violência patrimonial abrange a retenção, subtração ou destruição de documentos pessoais, bens, valores e",["direitos ou recursos econômicos.","amizades.","opiniões.","crenças.","idades."],"Art. 7º, IV.")
q(3,"A violência vicária foi incluída no art. 7º como inciso",["VI.","V.","IV.","III.","VII."],"Art. 7º, VI.")
q(3,"O art. 5º, I, trata da unidade doméstica; o II, da família; o III,",["da relação íntima de afeto.","do trabalho.","da escola.","da vizinhança.","da comunidade."],"Art. 5º.")
q(3,"A mulher goza dos direitos fundamentais da pessoa humana, e lhe são asseguradas oportunidades para viver sem violência, preservar a saúde física e mental e seu aperfeiçoamento moral, intelectual e",["social.","financeiro.","político.","religioso.","militar."],"Art. 2º.")
q(3,"O art. 3º impõe ao poder público a tarefa de resguardar as mulheres de toda forma de negligência, discriminação, exploração, violência, crueldade e",["opressão.","adoção.","educação.","tutela.","guarda."],"Art. 3º, § 1º.")
q(3,"A violência moral, no art. 7º, V, corresponde, em termos penais, aos crimes contra a",["honra.","vida.","liberdade sexual.","fé pública.","administração."],"Art. 7º, V.")
q(3,"A violência baseada no gênero é elemento do conceito do",["art. 5º.","art. 2º.","art. 3º.","art. 4º.","art. 1º."],"Art. 5º.")
q(3,"No texto da briga de ex-namorados, o caso enquadra-se no âmbito de",["relação íntima de afeto, independentemente de coabitação.","unidade doméstica.","família.","trabalho.","escola."],"Art. 5º, III.","mp1a")
q(3,"No texto da briga de ex-namorados, além da violência psicológica, a perseguição contumaz está expressamente descrita no art. 7º, inciso",["II.","I.","III.","IV.","V."],"Art. 7º, II.","mp1a")
q(3,"No texto dos documentos retidos, as condutas do homem configuram violência",["patrimonial.","moral.","vicária.","sexual.","apenas psicológica."],"Art. 7º, IV.","mp1b")
q(3,"No texto dos documentos retidos, a conduta ocorreu no âmbito da relação íntima de afeto, o que está previsto no art. 5º, inciso",["III.","I.","II.","IV.","V."],"Art. 5º, III.","mp1b")
q(3,"No texto da ameaça a parente, a conduta enquadra-se como violência",["vicária, prevista no art. 7º, VI.","moral, apenas.","patrimonial, apenas.","sexual.","física, apenas."],"Art. 7º, VI.","mp1c")
q(3,"No texto da ameaça a parente, a violência vicária tem por objetivo",["atingir a mulher por meio de pessoas de sua rede de apoio.","beneficiar a família.","proteger a mulher.","atingir o agressor.","aumentar a renda."],"Art. 7º, VI.","mp1c")
q(3,"No texto da ameaça a parente, a ameaça à mãe da ex-companheira configura violência contra",["ascendente ou parente da mulher.","empregado.","vizinho.","sócio.","cliente."],"Art. 7º, VI.","mp1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Lei Maria da Penha: arts. 1º a 7º",[
 ("obj","Objeto",["coibir e prevenir","Juizados","direitos sem distinção"],"seção 1"),
 ("int","Interpretação",["fins sociais","condições peculiares"],"seção 1"),
 ("con","Conceito",["ação ou omissão baseada no gênero","morte, lesão, sofrimento, dano"],"seção 2"),
 ("amb","Âmbitos",["unidade doméstica","família","relação íntima de afeto"],"seção 2"),
 ("for","Formas",["física, psicológica","sexual, patrimonial","moral, vicária"],"seção 3"),
 ("dh","Direitos humanos",["art. 6º","sem exigência de coabitação","independe de orientação sexual"],"seção 2")],
 "Na prova: três âmbitos e as seis formas de violência")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o objeto e a interpretação; as demais, o conceito, os âmbitos e as formas de violência.","Fontes: Edital 02/2026, Anexo I; Lei 11.340/2006 (Lei Maria da Penha), arts. 1º a 7º, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("mp-1","Lei Maria da Penha: disposições gerais e formas de violência (arts. 1º a 7º)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (1º a 7º)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","O inciso VI do art. 7º (violência vicária) consta da consolidação; conferir no Planalto.","Trechos de lei copiados de fontes/mp.txt por programa.","Casos mp1a, mp1b e mp1c fictícios."],
 fontes_conferidas=["Lei 11.340/2006, arts. 1º a 7º: texto da Câmara, copiado por programa."])
gravar("mp-1",aula_html,banco("mp-1",Q),tx)
