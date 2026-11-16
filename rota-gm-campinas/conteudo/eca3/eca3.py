import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='eca.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O direito à educação, à cultura, ao esporte e ao lazer (arts. 53 a 59-A) mistura direitos do aluno, deveres do Estado e deveres da escola. A Vunesp cobra os números (creche de zero a cinco anos), os sujeitos de cada dever (Estado, pais, dirigentes de escola, Municípios) e a lista de situações que a escola deve comunicar ao Conselho Tutelar. Para o guarda municipal, importa saber que a evasão escolar e os maus-tratos na escola são sinais de risco que chegam à rede de proteção."
S={}
S[1]="## 1. Direito à educação\n\n"+L("art. 53","Art. 53. A criança e o adolescente têm direito","Art. 53-A.")+"\n\n"+L("art. 53-A","Art. 53-A. É dever da instituição","Art. 54.")+"""

A criança e o adolescente têm direito à educação, visando ao pleno desenvolvimento da pessoa, ao preparo para a cidadania e à qualificação para o trabalho, assegurando-se: igualdade de condições para o acesso e permanência na escola; direito de ser respeitado por seus educadores; direito de contestar critérios avaliativos, podendo recorrer às instâncias escolares superiores; direito de organização e participação em entidades estudantis; e acesso à escola pública e gratuita, próxima de sua residência, com vagas no mesmo estabelecimento para irmãos na mesma etapa. Os pais têm direito de ter ciência do processo pedagógico e de participar da definição das propostas educacionais.

É dever da instituição de ensino, de clubes, agremiações recreativas e estabelecimentos congêneres assegurar medidas de conscientização, prevenção e enfrentamento ao uso ou dependência de drogas ilícitas.
"""
S[2]="## 2. Deveres do Estado e dos pais\n\n"+L("art. 54","Art. 54. É dever do Estado","Art. 55.")+"\n\n"+L("art. 55","Art. 55. Os pais ou responsável","Art. 56.")+"""

É dever do Estado assegurar ensino fundamental obrigatório e gratuito (inclusive aos que não tiveram acesso na idade própria); progressiva extensão da obrigatoriedade e gratuidade ao ensino médio; atendimento educacional especializado aos portadores de deficiência, preferencialmente na rede regular; atendimento em creche e pré-escola às crianças de zero a cinco anos; acesso aos níveis mais elevados do ensino, da pesquisa e da criação artística, segundo a capacidade; ensino noturno regular, adequado ao adolescente trabalhador; e programas suplementares de material didático-escolar, transporte, alimentação e assistência à saúde no ensino fundamental.

O acesso ao ensino obrigatório e gratuito é direito público subjetivo. O não oferecimento ou a oferta irregular importa responsabilidade da autoridade competente. Compete ao Poder Público recensear os educandos, fazer a chamada e zelar, junto aos pais, pela frequência. Os pais ou responsável têm a obrigação de matricular os filhos ou pupilos na rede regular de ensino.
"""
S[3]="## 3. Comunicação ao Conselho Tutelar, cultura e lazer\n\n"+L("art. 56","Art. 56. Os dirigentes","Art. 57.")+"\n\n"+L("arts. 58 e 59","Art. 58. No processo educacional","Art. 59-A.")+"\n\n"+L("art. 59-A","Art. 59-A. As instituições sociais","CAPÍTULO V")+"""

Os dirigentes de estabelecimentos de ensino fundamental comunicam ao Conselho Tutelar os casos de maus-tratos, reiteração de faltas injustificadas e evasão escolar (esgotados os recursos escolares), elevados níveis de repetência, e negligência, abuso ou abandono. No processo educacional respeitam-se os valores culturais, morais, éticos, artísticos e históricos do contexto social da criança, com liberdade de criação e acesso às fontes de cultura. Os Municípios, com apoio dos Estados e da União, estimulam a destinação de recursos e espaços para programações culturais, esportivas e de lazer.

As instituições sociais que desenvolvam atividades com crianças e recebam recursos públicos devem exigir e manter certidões de antecedentes criminais de todos os colaboradores, atualizadas a cada seis meses. Os estabelecimentos educacionais, mesmo sem recursos públicos, devem manter fichas cadastrais e certidões atualizadas.
"""
S[5]="""## 5. Na rotina do guarda

- **Criança fora da escola em horário de aula:** é sinal de evasão; a guarda orienta e encaminha, comunicando o Conselho Tutelar se for o caso.
- **Maus-tratos na escola:** o dirigente deve comunicar ao Conselho Tutelar; o guarda que presencia também comunica.
- **Eventos esportivos e culturais:** o Município deve destinar espaços e recursos; a guarda acompanha a segurança.
- **Drogas no entorno da escola:** as medidas de prevenção e enfrentamento são dever da instituição de ensino.
- **Cadastro de colaboradores:** escolas e entidades devem manter certidões de antecedentes; o guarda pode ser acionado em denúncia.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Creche e pré-escola | Zero a cinco anos |
| Ensino médio | Progressiva extensão da obrigatoriedade e gratuidade |
| Direito público subjetivo | Acesso ao ensino obrigatório e gratuito |
| Matrícula | Obrigação dos pais ou responsável |
| Recensear e chamada | Poder Público |
| Quem comunica ao Conselho Tutelar | Dirigentes de ensino fundamental |
| O que se comunica | Maus-tratos, faltas e evasão, repetência, negligência, abuso e abandono |
| Certidões de antecedentes | Atualizadas a cada 6 meses (instituições com recursos públicos) |
| Recursos para cultura e lazer | Municípios, com apoio dos Estados e da União |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 53 | Educação para pleno desenvolvimento, cidadania e trabalho |
| Escola | Pública, gratuita e próxima da residência |
| Art. 53-A | Prevenção às drogas: instituições de ensino, clubes |
| Art. 54 | Deveres do Estado: ensino, creche, deficiência, noturno |
| Creche | Zero a cinco anos |
| Art. 55 | Pais matriculam |
| Art. 56 | Dirigentes comunicam ao Conselho Tutelar |
| Art. 58 | Valores culturais e liberdade de criação |
| Art. 59 | Municípios: espaços de cultura, esporte e lazer |
| Art. 59-A | Certidões de antecedentes a cada 6 meses |
"""
QR=[("Questão 1","É dever do Estado assegurar atendimento em creche e pré-escola às crianças de",["zero a cinco anos de idade.","dois a seis anos.","três a sete anos.","zero a três anos.","quatro a seis anos."],0,"Art. 54, IV."),
("Questão 2","Os pais ou responsável têm a obrigação de matricular seus filhos ou pupilos na",["rede regular de ensino.","escola particular.","escola religiosa.","escola técnica.","escola militar."],1,"Art. 55."),
("Questão 3","Os dirigentes de estabelecimentos de ensino fundamental comunicarão ao Conselho Tutelar os casos de maus-tratos, reiteração de faltas injustificadas, elevados níveis de repetência e",["negligência, abuso ou abandono.","aprovação.","mudança de escola.","festas.","doações."],2,"Art. 56."),
("Questão 4","O acesso ao ensino obrigatório e gratuito é direito",["público subjetivo.","facultativo.","condicionado.","eventual.","limitado."],3,"Art. 54, § 1º.")]
t1="<strong>Faltas na escola</strong><br><br>O diretor de uma escola de ensino fundamental de Vila Nova, cidade fictícia, percebeu que um aluno faltou vinte dias seguidos sem justificativa, esgotados os recursos da escola para trazê-lo de volta."
t2="<strong>Vagas para irmãos</strong><br><br>Uma mãe de Vila Nova pediu vaga para os dois filhos, que cursam a mesma etapa do ensino fundamental, na escola mais próxima de casa."
t3="<strong>Escolinha de esportes</strong><br><br>Uma associação de Vila Nova, que recebe recursos públicos, mantém atividades esportivas com crianças. A direção contratou um monitor sem pedir antecedentes criminais."
tx={"eca3a":t1,"eca3b":t2,"eca3c":t3}
# n=1
q(1,"A criança e o adolescente têm direito à educação, visando ao pleno desenvolvimento da pessoa, ao preparo para o exercício da cidadania e à",["qualificação para o trabalho.","aposentadoria.","vida política.","propriedade.","diplomação."],"Art. 53.")
q(1,"É direito do estudante contestar critérios avaliativos, podendo recorrer às instâncias escolares",["superiores.","inferiores.","particulares.","religiosas.","políticas."],"Art. 53, III.")
q(1,"É direito do estudante a organização e a participação em entidades",["estudantis.","sindicais.","partidárias.","religiosas.","comerciais."],"Art. 53, IV.")
q(1,"É direito da criança o acesso à escola pública e gratuita, próxima de sua",["residência.","escola anterior.","igreja.","delegacia.","família ampliada."],"Art. 53, V.")
q(1,"O dever de assegurar medidas de prevenção ao uso de drogas ilícitas cabe à instituição de ensino, a clubes e a",["agremiações recreativas e estabelecimentos congêneres.","apenas a hospitais.","apenas à polícia.","apenas ao juiz.","apenas aos pais."],"Art. 53-A.")
q(1,"É dever do Estado assegurar ensino fundamental, obrigatório e",["gratuito.","pago.","facultativo.","privado.","militar."],"Art. 54, I.")
q(1,"É dever do Estado a oferta de ensino noturno regular, adequado às condições do adolescente",["trabalhador.","rico.","militar.","estrangeiro.","aposentado."],"Art. 54, VI.")
q(1,"O atendimento educacional especializado aos portadores de deficiência é ofertado, preferencialmente, na",["rede regular de ensino.","rede particular.","rede religiosa.","em casa.","em hospital."],"Art. 54, III.")
q(1,"Compete ao Poder Público recensear os educandos no ensino fundamental e fazer-lhes a",["chamada.","avaliação.","matrícula forçada.","inscrição partidária.","cobrança."],"Art. 54, § 3º.")
q(1,"O não oferecimento do ensino obrigatório pelo Poder Público importa responsabilidade da",["autoridade competente.","família.","criança.","comunidade.","imprensa."],"Art. 54, § 2º.")
q(1,"Os pais ou responsável têm a obrigação de matricular seus filhos na rede",["regular de ensino.","militar.","religiosa.","privada.","técnica."],"Art. 55.")
q(1,"Os dirigentes de ensino fundamental comunicarão ao Conselho Tutelar os casos de maus-tratos envolvendo seus",["alunos.","professores.","vizinhos.","pais.","fornecedores."],"Art. 56, I.")
q(1,"Os dirigentes comunicam ao Conselho Tutelar os elevados níveis de",["repetência.","aprovação.","matrículas.","bolsas.","merenda."],"Art. 56, III.")
q(1,"No processo educacional respeitam-se os valores culturais, morais, éticos, artísticos e históricos próprios do contexto",["social da criança e do adolescente.","do professor.","da cidade vizinha.","do Estado.","da União."],"Art. 58.")
q(1,"Os Municípios, com apoio dos Estados e da União, estimularão a destinação de recursos e espaços para programações culturais, esportivas e de",["lazer.","comércio.","política.","indústria.","pesca."],"Art. 59.")
q(1,"As instituições sociais que recebam recursos públicos devem exigir e manter certidões de antecedentes",["criminais de todos os colaboradores.","médicos.","tributários.","escolares.","bancários."],"Art. 59-A.")
q(1,"As certidões de antecedentes criminais do art. 59-A devem ser atualizadas a cada",["seis meses.","um mês.","três meses.","um ano.","dois anos."],"Art. 59-A.")
q(1,"No texto das faltas na escola, o diretor deve comunicar a reiteração de faltas injustificadas e a evasão ao",["Conselho Tutelar.","delegado.","prefeito.","vereador.","síndico."],"Art. 56, II.","eca3a")
q(1,"No texto das vagas para irmãos, a escola mais próxima da residência é direito, garantindo-se vagas no mesmo estabelecimento a irmãos que frequentem a mesma",["etapa ou ciclo de ensino da educação básica.","série apenas.","turma apenas.","idade.","escola particular."],"Art. 53, V.","eca3b")
q(1,"No texto da escolinha de esportes, a associação que recebe recursos públicos deve exigir certidões de antecedentes criminais de todos os",["colaboradores.","visitantes.","pais.","alunos.","vizinhos."],"Art. 59-A.","eca3c")
# n=2
q(2,"Entre os direitos assegurados no art. 53 está a igualdade de condições para o acesso e a permanência na",["escola.","rua.","cidade.","empresa.","feira."],"Art. 53, I.")
q(2,"O direito de ser respeitado por seus educadores está previsto como direito da",["criança e do adolescente.","escola.","mantenedora.","comunidade.","imprensa."],"Art. 53, II.")
q(2,"Os pais ou responsáveis têm direito de participar da definição das propostas",["educacionais.","comerciais.","políticas.","sanitárias.","religiosas."],"Art. 53, parágrafo único.")
q(2,"A progressiva extensão da obrigatoriedade e gratuidade, no art. 54, refere-se ao ensino",["médio.","superior.","técnico.","de idiomas.","religioso."],"Art. 54, II.")
q(2,"O ensino fundamental, obrigatório e gratuito, deve ser assegurado inclusive aos que a ele não tiveram acesso na idade",["própria.","adulta.","avançada.","mínima.","escolar."],"Art. 54, I.")
q(2,"O acesso aos níveis mais elevados do ensino, da pesquisa e da criação artística é segundo a capacidade de",["cada um.","pagamento.","família.","origem.","sorte."],"Art. 54, V.")
q(2,"No ensino fundamental, o Estado deve atender por programas suplementares de material didático-escolar, transporte, alimentação e",["assistência à saúde.","moradia.","lazer, apenas.","emprego.","seguro."],"Art. 54, VII.")
q(2,"Compete ao Poder Público zelar, junto aos pais ou responsável, pela",["frequência à escola.","renda familiar.","residência.","religião.","profissão."],"Art. 54, § 3º.")
q(2,"A comunicação ao Conselho Tutelar da reiteração de faltas deve ocorrer depois de esgotados os recursos",["escolares.","familiares.","policiais.","judiciais.","médicos."],"Art. 56, II.")
q(2,"A negligência, o abuso ou o abandono na forma dos arts. 4º e 5º devem ser comunicados pelos dirigentes ao",["Conselho Tutelar.","Ministério da Educação.","Prefeito.","Delegado.","Síndico."],"Art. 56, IV.")
q(2,"O Poder Público estimulará pesquisas e experiências relativas a calendário, seriação, currículo, metodologia, didática e",["avaliação.","moradia.","salário.","tributo.","lazer."],"Art. 57.")
q(2,"No processo educacional garante-se aos estudantes a liberdade da criação e o acesso às fontes de",["cultura.","renda.","emprego.","crédito.","moradia."],"Art. 58.")
q(2,"Aos Municípios cabe, com apoio dos Estados e da União, facilitar a destinação de recursos e espaços para programações voltadas para a",["infância e a juventude.","indústria.","agricultura.","mineração.","construção."],"Art. 59.")
q(2,"Os estabelecimentos educacionais, mesmo sem recursos públicos, devem manter fichas cadastrais e certidões de antecedentes criminais",["atualizadas de todos os colaboradores.","dos alunos.","dos pais.","dos vizinhos.","do prefeito."],"Art. 59-A, parágrafo único.")
q(2,"A instituição de ensino, os clubes e as agremiações recreativas devem assegurar medidas de enfrentamento ao uso ou dependência de",["drogas ilícitas.","jogos.","álcool, apenas.","tabaco, apenas.","redes sociais."],"Art. 53-A.")
q(2,"O direito de atendimento em creche e pré-escola é, nos termos do art. 54, dever do",["Estado.","comércio.","clero.","sindicato.","condomínio."],"Art. 54, IV.")
q(2,"No texto das faltas na escola, a situação do aluno com vinte dias de faltas enquadra-se no inciso",["II do art. 56.","I do art. 56.","III do art. 56.","IV do art. 56.","V do art. 56."],"Art. 56, II.","eca3a")
q(2,"No texto das vagas para irmãos, o direito de ter os irmãos no mesmo estabelecimento está no art.",["53, V.","54, I.","55.","56.","58."],"Art. 53, V.","eca3b")
q(2,"No texto da escolinha de esportes, a certidão de antecedentes deve ser atualizada a cada",["seis meses.","um mês.","dois anos.","cinco anos.","dez anos."],"Art. 59-A.","eca3c")
q(2,"O art. 53-A atribui às instituições de ensino, clubes e agremiações recreativas o dever de assegurar medidas de conscientização, prevenção e enfrentamento ao uso ou dependência de",["drogas ilícitas.","jogos eletrônicos.","apostas.","álcool, apenas.","redes sociais."],"Art. 53-A.")
# n=3
q(3,"Assinale a alternativa correta sobre os deveres previstos nos arts. 54 e 56.",["O Estado assegura creche de zero a cinco anos; os dirigentes de ensino fundamental comunicam ao Conselho Tutelar os maus-tratos.","Os pais comunicam ao Conselho Tutelar a repetência.","O Estado assegura creche de zero a três anos.","Os dirigentes de ensino superior comunicam os casos.","O Conselho Tutelar comunica à escola."],"Arts. 54, IV e 56.")
q(3,"Considere. I. O acesso ao ensino obrigatório é direito público subjetivo. II. A matrícula é dever do Estado. III. Os Municípios estimulam o lazer. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A matrícula é obrigação dos pais (art. 55).")
q(3,"Assinale a INCORRETA.",["Os dirigentes de ensino médio comunicam ao Conselho Tutelar os casos do art. 56.","O ensino fundamental é obrigatório e gratuito.","A creche atende crianças de zero a cinco anos.","A frequência é zelada junto aos pais pelo Poder Público.","As certidões do art. 59-A são atualizadas a cada seis meses."],"O art. 56 fala em dirigentes de estabelecimentos de ensino fundamental.")
q(3,"No art. 53, V, a garantia de vagas no mesmo estabelecimento a irmãos exige que frequentem a mesma",["etapa ou ciclo de ensino da educação básica.","turma.","série e turno.","idade.","sala."],"Art. 53, V.")
q(3,"A oferta irregular do ensino obrigatório, segundo o art. 54, § 2º, importa responsabilidade da",["autoridade competente.","criança.","família.","comunidade.","escola particular."],"Art. 54, § 2º.")
q(3,"A liberdade da criação e o acesso às fontes de cultura são garantidos no",["processo educacional.","processo penal.","processo tributário.","processo eleitoral.","processo civil."],"Art. 58.")
q(3,"A comunicação de elevados níveis de repetência ao Conselho Tutelar compete ao dirigente de estabelecimento de",["ensino fundamental.","ensino superior.","ensino técnico.","curso livre.","creche."],"Art. 56, III.")
q(3,"O art. 59-A impõe a manutenção de certidões de antecedentes criminais de colaboradores às instituições sociais que",["desenvolvam atividades com crianças e recebam recursos públicos.","não tenham fins.","recebam doações.","atuem em outro Estado.","sejam comerciais."],"Art. 59-A.")
q(3,"O direito do estudante de contestar critérios avaliativos pode ser exercido recorrendo às instâncias",["escolares superiores.","judiciais apenas.","policiais.","tributárias.","eleitorais."],"Art. 53, III.")
q(3,"A destinação de recursos e espaços para programações culturais, esportivas e de lazer é estimulada pelos",["Municípios, com apoio dos Estados e da União.","particulares apenas.","clubes apenas.","sindicatos.","empresas apenas."],"Art. 59.")
q(3,"A assistência à saúde, o transporte e a alimentação no ensino fundamental são previstos por programas",["suplementares.","principais.","particulares.","religiosos.","temporários."],"Art. 54, VII.")
q(3,"O Poder Público estimulará pesquisas para inserir crianças e adolescentes excluídos do ensino fundamental",["obrigatório.","facultativo.","superior.","técnico.","religioso."],"Art. 57.")
q(3,"A prevenção ao uso de drogas ilícitas, no art. 53-A, é dever também de",["clubes e agremiações recreativas.","empresas de ônibus.","apenas hospitais.","apenas juízes.","apenas partidos."],"Art. 53-A.")
q(3,"A atualização das certidões do art. 59-A é de seis meses para as instituições",["que recebem recursos públicos.","que não recebem.","apenas esportivas.","apenas religiosas.","apenas culturais."],"Art. 59-A.")
q(3,"No texto das faltas na escola, o diretor age conforme o art. 56 ao comunicar o caso ao Conselho Tutelar, porque já se esgotaram os",["recursos escolares.","recursos judiciais.","recursos policiais.","prazos de matrícula.","anos letivos."],"Art. 56, II.","eca3a")
q(3,"No texto das vagas para irmãos, o direito invocado pela mãe é de acesso à escola",["pública e gratuita, próxima da residência.","particular.","militar.","religiosa.","técnica."],"Art. 53, V.","eca3b")
q(3,"No texto da escolinha de esportes, a contratação sem antecedentes criminais descumpre a regra do art.",["59-A.","53-A.","55.","56.","58."],"Art. 59-A.","eca3c")
q(3,"No texto da escolinha de esportes, a exigência de certidões vale porque a associação",["recebe recursos públicos e atua com crianças.","é de outro Estado.","é pequena.","é nova.","tem fins lucrativos."],"Art. 59-A.","eca3c")
q(3,"No texto das vagas para irmãos, a escolha por escola próxima de casa é direito do art. 53, que trata do direito à",["educação.","saúde.","moradia.","liberdade.","convivência."],"Art. 53.","eca3b")
q(3,"É direito dos pais ou responsáveis, no art. 53, parágrafo único, ter ciência do processo pedagógico e participar da definição das",["propostas educacionais.","notas dos colegas.","contratações de professores.","verbas da escola.","regras do bairro."],"Art. 53, parágrafo único.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("ECA: educação, cultura e lazer (arts. 53 a 59-A)",[
 ("dir","Direitos do aluno",["igualdade de acesso","respeito dos educadores","contestar critérios, entidades"],"seção 1"),
 ("esc","Escola próxima",["pública e gratuita","vagas para irmãos","ciência dos pais"],"seção 1"),
 ("est","Deveres do Estado",["ensino fundamental","creche: 0 a 5 anos","deficiência, noturno"],"seção 2"),
 ("pai","Pais",["matricular","frequência","recenseamento"],"seção 2"),
 ("con","Comunicação",["Conselho Tutelar","maus-tratos, evasão","repetência, negligência"],"seção 3"),
 ("mun","Municípios e certidões",["cultura e lazer","antecedentes criminais","a cada 6 meses"],"seção 3")],
 "Na prova: creche 0 a 5 anos e as comunicações ao Conselho Tutelar")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz os direitos do aluno; as demais, os deveres do Estado e dos pais, as comunicações e a cultura e lazer.","Fontes: Edital 02/2026, Anexo I; Lei 8.069/1990 (ECA), arts. 53 a 59-A, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("eca-3","ECA: educação, cultura, esporte e lazer (arts. 53 a 59-A)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (53 a 59-A)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Trechos de lei copiados de fontes/eca.txt por programa.","Casos eca3a, eca3b e eca3c fictícios."],
 fontes_conferidas=["ECA, arts. 53 a 59-A: texto da Câmara, copiado por programa."])
gravar("eca-3",aula_html,banco("eca-3",Q),tx)
