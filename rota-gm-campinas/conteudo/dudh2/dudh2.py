import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS, LEI
F='dudh.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A segunda parte da Declaração Universal dos Direitos Humanos (arts. 22 a 30) trata dos direitos econômicos, sociais e culturais e dos deveres e limites: segurança social, trabalho, repouso e lazer, nível de vida adequado, educação, vida cultural, ordem social e internacional, deveres para com a comunidade e a regra de que as liberdades só se limitam por lei. A Vunesp cobra o texto quase literal. Atenção a três números: o art. 26 (educação gratuita ao menos no ensino elementar e obrigatória), o art. 25 (maternidade e infância) e o art. 29 (deveres e limitações)."
S={}
S[1]="## 1. Arts. 22 a 25: segurança social, trabalho, lazer e nível de vida\n\n"+L("art. 22","Art. 22º ","Art. 23º ")+"\n\n"+L("art. 23","Art. 23º ","Art. 24º ")+"\n\n"+L("arts. 24 e 25","Art. 24º ","Art. 26º ")+"""

Toda pessoa, como membro da sociedade, tem direito à segurança social e pode exigir a satisfação dos direitos econômicos, sociais e culturais indispensáveis, graças ao esforço nacional e à cooperação internacional. Tem direito ao trabalho, à livre escolha do trabalho, a condições equitativas e satisfatórias e à proteção contra o desemprego; a salário igual por trabalho igual, sem discriminação; a remuneração equitativa que permita existência digna; e a fundar sindicatos e filiar-se a eles. Tem direito ao repouso e aos lazeres, a uma limitação razoável da duração do trabalho e a férias periódicas pagas.

Toda pessoa tem direito a um nível de vida suficiente para lhe assegurar e à sua família a saúde e o bem-estar (alimentação, vestuário, alojamento, assistência médica, serviços sociais), e à segurança no desemprego, na doença, na invalidez, na viuvez, na velhice ou em outros casos de perda de meios de subsistência. A maternidade e a infância têm direito a ajuda e assistência especiais, e todas as crianças, nascidas dentro ou fora do matrimônio, gozam da mesma proteção social.
"""
S[2]="## 2. Arts. 26 e 27: educação e vida cultural\n\n"+L("art. 26","Art. 26º ","Art. 27º ")+"\n\n"+L("art. 27","Art. 27º ","Art. 28º ")+"""

Toda pessoa tem direito à educação, que deve ser gratuita, pelo menos a correspondente ao ensino elementar fundamental, sendo o ensino elementar obrigatório. O ensino técnico e profissional deve ser generalizado, e o acesso aos estudos superiores deve estar aberto a todos em plena igualdade, em função do mérito. A educação deve visar à plena expansão da personalidade humana e ao reforço dos direitos humanos e das liberdades fundamentais, favorecendo a compreensão, a tolerância e a amizade entre as nações e os grupos raciais ou religiosos. Aos pais pertence a prioridade do direito de escolher o gênero de educação a dar aos filhos.

Toda pessoa tem o direito de tomar parte livremente na vida cultural da comunidade, de fruir as artes e de participar do progresso científico e de seus benefícios, e à proteção dos interesses morais e materiais ligados a qualquer produção científica, literária ou artística de sua autoria.
"""
S[3]="## 3. Arts. 28 a 30: ordem social, deveres e limites\n\n"+L("art. 28","Art. 28º ","Art. 29º ")+"\n\n"+L("art. 29","Art. 29º ","Art. 30º ")+"\n\n"+LEI("art. 30","Nenhuma disposição da presente Declaração pode ser interpretada de maneira a envolver para qualquer Estado, agrupamento ou indivíduo o direito de se entregar a alguma actividade ou de praticar algum acto destinado a destruir os direitos e liberdades aqui enunciados.",F)+"""

Toda pessoa tem direito a que reine, no plano social e internacional, uma ordem capaz de tornar plenamente efetivos os direitos e liberdades enunciados na Declaração. O indivíduo tem deveres para com a comunidade, fora da qual não é possível o livre e pleno desenvolvimento da sua personalidade. No exercício dos direitos e liberdades, ninguém está sujeito senão às limitações estabelecidas pela lei, com vista exclusivamente a promover o reconhecimento e o respeito dos direitos e liberdades dos outros e a satisfazer as justas exigências da moral, da ordem pública e do bem-estar numa sociedade democrática. Em caso algum esses direitos poderão ser exercidos contrariamente aos fins e princípios da ONU. Nenhuma disposição da Declaração pode ser interpretada de maneira a envolver direito de praticar ato destinado a destruir os direitos e liberdades nela enunciados.
"""
S[5]="""## 5. Na rotina do guarda

- **Limitações por lei (art. 29):** os direitos só são limitados pela lei, em favor dos direitos dos outros, da moral, da ordem pública e do bem-estar; a atuação do guarda se funda nessa limitação.
- **Deveres para com a comunidade (art. 29):** o indivíduo tem deveres, e o guarda orienta sem abandonar o respeito aos direitos.
- **Ordem social e internacional (art. 28):** a segurança pública contribui para uma ordem em que os direitos sejam efetivos.
- **Trabalho do próprio guarda (art. 23 e 24):** o guarda também tem direito a condições equitativas, repouso e lazer.
- **Atendimento a crianças (art. 25):** a infância tem direito a assistência especial; o guarda encaminha crianças em risco à rede de proteção.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Art. 22 | Segurança social e direitos econômicos, sociais e culturais |
| Art. 23 | Trabalho, salário igual, sindicatos |
| Art. 24 | Repouso, lazer, férias periódicas pagas |
| Art. 25 | Nível de vida suficiente; maternidade e infância; todas as crianças com a mesma proteção |
| Art. 26 | Educação gratuita (ao menos a elementar); ensino elementar obrigatório; pais escolhem o gênero de educação |
| Art. 27 | Vida cultural; progresso científico; autoria |
| Art. 28 | Ordem social e internacional |
| Art. 29 | Deveres; limites pela lei; fins da ONU |
| Art. 30 | Vedada a interpretação para destruir direitos |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 22 | Segurança social |
| Art. 23 | Trabalho e sindicatos |
| Art. 24 | Repouso e lazer |
| Art. 25 | Nível de vida; maternidade e infância |
| Art. 26 | Educação |
| Art. 27 | Cultura e autoria |
| Art. 28 | Ordem que efetive os direitos |
| Art. 29 | Deveres e limitações pela lei |
| Art. 30 | Vedada a interpretação destrutiva |
"""
QR=[("Questão 1","Segundo a Declaração Universal dos Direitos Humanos, toda a pessoa tem direito à educação, que deve ser gratuita, pelo menos a correspondente ao ensino",["elementar fundamental.","superior.","técnico.","médio.","pré-escolar."],0,"Art. 26, 1."),
("Questão 2","O ensino elementar é",["obrigatório.","facultativo.","pago.","opcional.","regional."],1,"Art. 26, 1."),
("Questão 3","Todas as crianças, nascidas dentro ou fora do matrimônio, gozam da mesma proteção",["social.","fiscal.","militar.","religiosa.","econômica apenas."],2,"Art. 25, 2."),
("Questão 4","No exercício dos direitos e liberdades, ninguém está sujeito senão às limitações estabelecidas pela",["lei.","tradição.","vontade do Estado.","opinião pública.","moral individual."],3,"Art. 29, 2.")]
t1="<strong>Escola pública</strong><br><br>Um pai de Vila Nova, cidade fictícia, foi informado de que a escola pública cobraria taxa de matrícula do ensino fundamental de seu filho."
t2="<strong>Trabalhadora sem descanso</strong><br><br>Uma funcionária de Vila Nova trabalhava seis dias por semana, sem repouso e sem férias."
t3="<strong>Limite à manifestação</strong><br><br>Uma manifestação em Vila Nova bloqueou uma via e a guarda interveio para desobstruí-la, com base na lei, para proteger o direito de circulação dos demais."
tx={"dudh2a":t1,"dudh2b":t2,"dudh2c":t3}
# n=1
q(1,"Toda a pessoa, como membro da sociedade, tem direito à segurança",["social.","pública.","privada.","nacional.","militar."],"Art. 22.")
q(1,"Toda a pessoa tem direito ao trabalho e à livre escolha do",["trabalho.","patrão.","salário.","sindicato.","local."],"Art. 23, 1.")
q(1,"Todos têm direito, sem discriminação, a salário igual por trabalho",["igual.","extra.","superior.","parcial.","noturno."],"Art. 23, 2.")
q(1,"Toda a pessoa tem o direito de fundar sindicatos e de se filiar em sindicatos para defesa dos seus",["interesses.","lucros.","bens.","cargos.","direitos políticos."],"Art. 23, 4.")
q(1,"Toda a pessoa tem direito ao repouso e aos",["lazeres.","bônus.","empregos.","cargos.","benefícios."],"Art. 24.")
q(1,"Toda a pessoa tem direito a férias periódicas",["pagas.","opcionais.","gratuitas.","eventuais.","anuais, apenas."],"Art. 24.")
q(1,"Toda a pessoa tem direito a um nível de vida suficiente para lhe assegurar e à sua família a saúde e o",["bem-estar.","lucro.","poder.","cargo.","título."],"Art. 25, 1.")
q(1,"A maternidade e a infância têm direito a ajuda e a assistência",["especiais.","comuns.","eventuais.","privadas.","religiosas."],"Art. 25, 2.")
q(1,"Toda a pessoa tem direito à",["educação.","herança.","propriedade rural.","imunidade.","isenção."],"Art. 26, 1.")
q(1,"A educação deve visar à plena expansão da personalidade",["humana.","econômica.","militar.","política.","religiosa."],"Art. 26, 2.")
q(1,"A educação deve favorecer a compreensão, a tolerância e a",["amizade entre todas as nações.","competição.","obediência.","hierarquia.","disputa."],"Art. 26, 2.")
q(1,"Aos pais pertence a prioridade do direito de escolher o gênero de educação a dar aos",["filhos.","alunos.","netos.","vizinhos.","professores."],"Art. 26, 3.")
q(1,"Toda a pessoa tem o direito de tomar parte livremente na vida cultural da",["comunidade.","empresa.","escola.","igreja.","cidade-sede."],"Art. 27, 1.")
q(1,"Todos têm direito à proteção dos interesses morais e materiais ligados a qualquer produção científica, literária ou artística da sua",["autoria.","propriedade.","residência.","origem.","empresa."],"Art. 27, 2.")
q(1,"Toda a pessoa tem direito a que reine, no plano social e no plano internacional, uma",["ordem capaz de tornar efetivos os direitos e liberdades.","vigilância.","hierarquia.","censura.","guerra."],"Art. 28.")
q(1,"O indivíduo tem deveres para com a",["comunidade.","empresa.","Igreja.","família apenas.","escola apenas."],"Art. 29, 1.")
q(1,"Em caso algum os direitos e liberdades poderão ser exercidos contrariamente aos fins e aos princípios das",["Nações Unidas.","empresas.","igrejas.","escolas.","famílias."],"Art. 29, 3.")
q(1,"Nenhuma disposição da Declaração pode ser interpretada de maneira a destruir os direitos e liberdades aqui",["enunciados.","limitados.","comentados.","negados.","ignorados."],"Art. 30.")
q(1,"No texto da escola pública, o direito do filho decorre do art. 26, que prevê educação gratuita, pelo menos a correspondente ao ensino",["elementar fundamental.","superior.","técnico.","pré-escolar.","médio."],"Art. 26, 1.","dudh2a")
q(1,"No texto da trabalhadora sem descanso, a funcionária tem direito ao repouso e aos lazeres, previstos no art.",["24.","22.","23.","25.","26."],"Art. 24.","dudh2b")
# n=2
q(2,"A satisfação dos direitos econômicos, sociais e culturais é possível graças ao esforço nacional e à cooperação",["internacional.","partidária.","privada.","religiosa.","militar."],"Art. 22.")
q(2,"Toda a pessoa tem direito a condições equitativas e satisfatórias de trabalho e à proteção contra o",["desemprego.","descanso.","lazer.","imposto.","emprego público."],"Art. 23, 1.")
q(2,"Quem trabalha tem direito a uma remuneração equitativa e satisfatória que lhe permita, e à sua família, uma existência em conformidade com a",["dignidade humana.","moda.","tradição.","origem.","profissão."],"Art. 23, 3.")
q(2,"Toda a pessoa tem direito a uma limitação razoável da duração do",["trabalho.","descanso.","lazer.","estudo.","passeio."],"Art. 24.")
q(2,"O nível de vida suficiente inclui alimentação, vestuário, alojamento, assistência médica e serviços",["sociais necessários.","de luxo.","privados.","militares.","religiosos."],"Art. 25, 1.")
q(2,"Toda a pessoa tem direito à segurança no desemprego, na doença, na invalidez, na viuvez, na velhice ou noutros casos de perda de meios de",["subsistência.","trabalho.","liberdade.","residência.","documento."],"Art. 25, 1.")
q(2,"O ensino técnico e profissional deve ser",["generalizado.","restrito.","privado.","eventual.","facultativo."],"Art. 26, 1.")
q(2,"O acesso aos estudos superiores deve estar aberto a todos em plena igualdade, em função do seu",["mérito.","patrimônio.","local.","sexo.","cargo."],"Art. 26, 1.")
q(2,"A educação deve favorecer o desenvolvimento das atividades das Nações Unidas para a manutenção da",["paz.","ordem econômica.","hierarquia.","propriedade.","tradição."],"Art. 26, 2.")
q(2,"Toda a pessoa tem o direito de fruir as artes e de participar no progresso científico e nos benefícios que dele",["resultam.","nascem.","derivam apenas ao Estado.","são excluídos.","partem."],"Art. 27, 1.")
q(2,"Os direitos e liberdades enunciados só são plenamente efetivos numa ordem social e",["internacional.","econômica.","militar.","religiosa.","privada."],"Art. 28.")
q(2,"Fora da comunidade não é possível o livre e pleno desenvolvimento da personalidade do",["indivíduo.","Estado.","grupo.","partido.","clero."],"Art. 29, 1.")
q(2,"As limitações legais aos direitos visam a satisfazer as justas exigências da moral, da ordem pública e do bem-estar numa sociedade",["democrática.","militar.","tradicional.","religiosa.","econômica."],"Art. 29, 2.")
q(2,"As limitações legais visam a promover o reconhecimento e o respeito dos direitos e liberdades dos",["outros.","governantes.","empresas.","religiosos.","políticos."],"Art. 29, 2.")
q(2,"O art. 30 impede a interpretação da Declaração que envolva o direito de destruir os direitos e liberdades dela decorrentes por qualquer Estado, agrupamento ou",["indivíduo.","partido.","clube.","empresa.","igreja."],"Art. 30.")
q(2,"A Declaração, no art. 25, dá igual proteção às crianças nascidas dentro ou fora do",["matrimônio.","país.","bairro.","Estado.","hospital."],"Art. 25, 2.")
q(2,"No texto da escola pública, a cobrança de taxa de matrícula do ensino fundamental contraria o princípio da educação",["gratuita, ao menos no ensino elementar.","paga em todos os níveis.","privada.","opcional.","superior."],"Art. 26, 1.","dudh2a")
q(2,"No texto da trabalhadora sem descanso, a ausência de férias periódicas pagas viola o art.",["24.","26.","28.","30.","22."],"Art. 24.","dudh2b")
q(2,"No texto do limite à manifestação, a intervenção só é legítima se fundada em",["lei, para respeitar os direitos dos outros.","vontade do guarda.","ordem verbal.","ordem de um vizinho.","tradição."],"Art. 29, 2.","dudh2c")
q(2,"A educação deve favorecer o desenvolvimento das atividades das Nações Unidas, e o art. 26 também dispõe que o ensino elementar é",["obrigatório.","facultativo.","pago.","opcional.","eventual."],"Art. 26, 1.")
# n=3
q(3,"Assinale a alternativa correta quanto ao art. 26.",["Educação gratuita ao menos no ensino elementar fundamental, que é obrigatório; aos pais cabe prioridade na escolha do gênero de educação.","Educação gratuita apenas no ensino superior.","O ensino elementar é facultativo.","O Estado escolhe a educação dos filhos.","O ensino técnico é vedado."],"Art. 26.")
q(3,"Considere. I. O art. 29 prevê deveres para com a comunidade. II. As limitações aos direitos só podem ser estabelecidas pela lei. III. A Declaração admite o exercício de direitos contrariamente aos fins da ONU. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Os direitos não podem ser exercidos contrariamente aos fins da ONU (art. 29, 3).")
q(3,"Assinale a INCORRETA.",["O ensino elementar é facultativo.","O salário deve ser igual por trabalho igual.","A educação favorece a tolerância e a amizade.","A cultura é direito de todos.","A maternidade e a infância têm assistência especial."],"O ensino elementar é obrigatório (art. 26, 1).")
q(3,"O art. 22 afirma que a satisfação dos direitos econômicos, sociais e culturais deve ser de harmonia com a organização e os recursos de cada",["país.","empresa.","município.","família.","pessoa."],"Art. 22.")
q(3,"O art. 23 estabelece direito de fundar sindicatos e de se filiar a sindicatos, o que está no item",["4.","1.","2.","3.","5."],"Art. 23, 4.")
q(3,"A segurança no desemprego, na doença e na velhice está no art. 25, item",["1.","2.","3.","4.","5."],"Art. 25, 1.")
q(3,"A mesma proteção social às crianças nascidas dentro ou fora do matrimônio está no art. 25, item",["2.","1.","3.","4.","5."],"Art. 25, 2.")
q(3,"A prioridade do direito dos pais de escolher o gênero de educação está no art. 26, item",["3.","1.","2.","4.","5."],"Art. 26, 3.")
q(3,"A proteção dos interesses morais e materiais ligados à produção científica, literária ou artística está no art. 27, item",["2.","1.","3.","4.","5."],"Art. 27, 2.")
q(3,"O art. 29, item 1, trata dos deveres, o item 2, das limitações legais e o item 3, dos fins e princípios das",["Nações Unidas.","empresas.","igrejas.","escolas.","forças armadas."],"Art. 29.")
q(3,"A ressalva do art. 29 de que as limitações visam à moral, à ordem pública e ao bem-estar numa sociedade democrática fundamenta a atuação do",["Estado, nos limites da lei.","indivíduo, a seu critério.","particular, sem lei.","juiz apenas.","mercado."],"Art. 29, 2.")
q(3,"A educação deve visar ao reforço dos direitos do Homem e das",["liberdades fundamentais.","tradições.","culturas.","rendas.","fronteiras."],"Art. 26, 2.")
q(3,"A educação deve favorecer a compreensão, a tolerância e a amizade entre todos os grupos raciais ou",["religiosos.","econômicos.","políticos.","regionais.","profissionais."],"Art. 26, 2.")
q(3,"No texto da escola pública, o pai pode exigir o direito à educação, que é gratuita ao menos no ensino elementar fundamental e",["obrigatório.","facultativo.","pago.","opcional.","superior."],"Art. 26, 1.","dudh2a")
q(3,"No texto da escola pública, o direito aplica-se ao ensino elementar fundamental, que deve ser gratuito e, segundo a Declaração, também",["obrigatório.","facultativo.","privado.","eventual.","opcional."],"Art. 26, 1.","dudh2a")
q(3,"No texto da trabalhadora sem descanso, o art. 24 garante limitação razoável da duração do trabalho e férias periódicas",["pagas.","opcionais.","gratuitas.","eventuais.","anuais, sem remuneração."],"Art. 24.","dudh2b")
q(3,"No texto da trabalhadora sem descanso, a remuneração equitativa e satisfatória, que permita existência digna, está no art.",["23, 3.","24.","25.","26.","22."],"Art. 23, 3.","dudh2b")
q(3,"No texto do limite à manifestação, a intervenção da guarda se justifica pelo art. 29, que admite limitações para respeitar os direitos e liberdades dos",["outros.","governantes.","empresários.","militares.","políticos."],"Art. 29, 2.","dudh2c")
q(3,"No texto do limite à manifestação, a limitação deve ser estabelecida pela lei, com vista a satisfazer as justas exigências da moral, da ordem pública e do",["bem-estar numa sociedade democrática.","lucro.","poder.","partido.","clero."],"Art. 29, 2.","dudh2c")
q(3,"No texto do limite à manifestação, o direito de reunião não pode ser exercido contrariamente aos fins e princípios das",["Nações Unidas.","empresas.","igrejas.","escolas.","famílias."],"Art. 29, 3.","dudh2c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("DUDH: arts. 22 a 30",[
 ("seg","Segurança social",["art. 22","direitos econômicos, sociais, culturais"],"seção 1"),
 ("tra","Trabalho e lazer",["arts. 23 e 24","salário igual","férias pagas"],"seção 1"),
 ("viv","Nível de vida",["art. 25","maternidade e infância","crianças igualmente protegidas"],"seção 1"),
 ("edu","Educação",["art. 26","gratuita e obrigatória (elementar)","pais escolhem o gênero"],"seção 2"),
 ("cul","Cultura",["art. 27","autoria"],"seção 2"),
 ("lim","Deveres e limites",["art. 29","limites pela lei","art. 30"],"seção 3")],
 "Na prova: art. 26 e art. 29")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o trabalho, o lazer e o nível de vida; as demais, a educação, a cultura e os limites dos direitos.","Fontes: Edital 02/2026, Anexo I; Declaração Universal dos Direitos Humanos (ONU, 1948), tradução do Centro de Informação das Nações Unidas, texto da Wikisource. Exemplos criados para a aula.")
revisao("dudh-2","DUDH: arts. 22 a 30",Q,list(tx),
 cobertura=["Todos os artigos do recorte (22 a 30)."],
 pendencias=["Texto-fonte: tradução da Wikisource, com a grafia de Portugal; reconferir na versão oficial em português do Brasil.","Trechos copiados de fontes/dudh.txt por programa.","Casos dudh2a, dudh2b e dudh2c fictícios."],
 fontes_conferidas=["DUDH, arts. 22 a 30: tradução da Wikisource, copiada por programa."])
gravar("dudh-2",aula_html,banco("dudh-2",Q),tx)
