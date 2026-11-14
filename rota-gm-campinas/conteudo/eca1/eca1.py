import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='eca.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Estatuto da Criança e do Adolescente (Lei 8.069/1990) começa pelos princípios que sustentam todo o resto: proteção integral, prioridade absoluta e condição peculiar de pessoa em desenvolvimento. Os arts. 1º a 6º são curtos, mas a Vunesp cobra os detalhes: a idade que separa criança de adolescente, os quatro itens da garantia de prioridade, quem tem o dever de assegurar os direitos e a forma de interpretar a lei. Para o guarda municipal, é a base de qualquer atendimento a criança ou adolescente em situação de risco, de rua ou de violência."
S={}
S[1]="## 1. Proteção integral, conceito de criança e de adolescente\n\n"+L("art. 1º","Art. 1º Esta Lei dispõe","Art. 2º")+"\n\n"+L("art. 2º","Art. 2º Considera-se criança","Art. 3º")+"\n\n"+L("art. 3º","Art. 3º A criança e o adolescente gozam","Parágrafo único. Os direitos enunciados")+"\n\n"+L("art. 3º, parágrafo único","Parágrafo único. Os direitos enunciados","Art. 4º")+"""

A lei trata da proteção integral à criança e ao adolescente. A idade é a regra de ouro: criança é a pessoa até doze anos incompletos; adolescente, a que tem de doze a dezoito anos. Quem tem doze anos completos já é adolescente. Excepcionalmente, nos casos expressos em lei, o Estatuto aplica-se a pessoas entre dezoito e vinte e um anos.

A criança e o adolescente gozam de todos os direitos fundamentais da pessoa humana, e a lei assegura todas as oportunidades e facilidades para o desenvolvimento físico, mental, moral, espiritual e social, em condições de liberdade e dignidade. Esses direitos valem para todos, sem discriminação de nascimento, situação familiar, idade, sexo, raça, etnia, cor, religião, deficiência, condição econômica, ambiente social ou local de moradia.
"""
S[2]="## 2. Prioridade absoluta e assistência afetiva\n\n"+L("art. 4º, caput","Art. 4º É dever da família","§ 1º A garantia")+"\n\n"+L("art. 4º, § 1º, alíneas","a) primazia de receber","§ 2º Compete aos pais")+"\n\n"+L("art. 4º, §§ 2º e 3º","§ 2º Compete aos pais","Art. 5º")+"""

É dever da família, da comunidade, da sociedade em geral e do poder público assegurar, com absoluta prioridade, a efetivação dos direitos referentes à vida, à saúde, à alimentação, à educação, ao esporte, ao lazer, à profissionalização, à cultura, à dignidade, ao respeito, à liberdade, à natureza e à convivência familiar e comunitária. Gravar: quatro sujeitos (família, comunidade, sociedade, poder público).

A garantia de prioridade compreende quatro itens: primazia de receber proteção e socorro em quaisquer circunstâncias (a); precedência de atendimento nos serviços públicos ou de relevância pública (b); preferência na formulação e execução das políticas sociais públicas (c); e destinação privilegiada de recursos públicos nas áreas de proteção à infância e juventude (d). Aos pais cabe, além de zelar pelos direitos, prestar assistência afetiva, por convívio ou visitação periódica, o que inclui orientação sobre escolhas, apoio em momentos de sofrimento e presença física quando solicitada e possível.
"""
S[3]="## 3. Proibição de violação e interpretação\n\n"+L("art. 5º","Art. 5º Nenhuma criança","Art. 6º")+"\n\n"+L("art. 6º","Art. 6º Na interpretação","TÍTULO II")+"""

Nenhuma criança ou adolescente será objeto de negligência, discriminação, exploração, violência, crueldade e opressão, e qualquer atentado, por ação ou omissão, aos seus direitos fundamentais é punido na forma da lei. É conduta ilícita, sujeita a reparação de danos, a ação ou omissão que ofenda direito fundamental previsto no Estatuto, incluídos os casos de abandono afetivo.

Na interpretação da lei, levam-se em conta os fins sociais a que ela se dirige, as exigências do bem comum, os direitos e deveres individuais e coletivos e a condição peculiar da criança e do adolescente como pessoas em desenvolvimento.
"""
S[5]="""## 5. Na rotina do guarda

- **Idade:** o guarda que atende um jovem de 12 anos completos trata-o como adolescente, não como criança.
- **Prioridade:** em fila, atendimento ou socorro, crianças e adolescentes têm precedência nos serviços públicos.
- **Violência e negligência:** qualquer atentado por ação ou omissão contra os direitos da criança deve ser comunicado ao Conselho Tutelar.
- **Rua e risco:** a abordagem respeita a condição peculiar de pessoa em desenvolvimento; a criança não é tratada como suspeita.
- **Sem discriminação:** os direitos valem para todos, qualquer que seja a condição econômica ou o local de moradia.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Idade da criança | Até 12 anos incompletos; 12 anos completos já é adolescente |
| Idade do adolescente | De 12 a 18 anos |
| Aplicação a 18 a 21 anos | Excepcional, nos casos expressos em lei |
| Quem tem o dever | Família, comunidade, sociedade e poder público |
| Itens da prioridade | Primazia, precedência, preferência, destinação privilegiada de recursos |
| Abandono afetivo | Conduta ilícita sujeita a reparação de danos |
| Interpretação | Fins sociais, bem comum, direitos e deveres, condição peculiar |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Objeto | Proteção integral à criança e ao adolescente |
| Criança | Até 12 anos incompletos |
| Adolescente | De 12 a 18 anos |
| Exceção | 18 a 21 anos, nos casos expressos em lei |
| Dever | Família, comunidade, sociedade e poder público |
| Prioridade | Primazia de socorro, precedência, preferência em políticas, recursos |
| Assistência afetiva | Orientação, apoio nos sofrimentos, presença |
| Art. 5º | Nenhuma forma de negligência, discriminação, exploração, violência, crueldade e opressão |
| Reparação | Abandono afetivo é conduta ilícita |
| Interpretação | Fins sociais, bem comum, condição peculiar |
"""
QR=[("Questão 1","Considera-se criança, para os efeitos do Estatuto, a pessoa até",["doze anos de idade incompletos.","dez anos completos.","catorze anos completos.","dezesseis anos incompletos.","dezoito anos incompletos."],0,"Art. 2º."),
("Questão 2","A garantia de prioridade compreende a primazia de receber proteção e socorro em",["quaisquer circunstâncias.","horário comercial.","dias úteis.","rodovias.","hospitais."],1,"Art. 4º, § 1º, a."),
("Questão 3","É dever da família, da comunidade, da sociedade em geral e do poder público assegurar, com absoluta prioridade, a efetivação dos direitos referentes à",["vida, à saúde, à alimentação, à educação, ao esporte e ao lazer, entre outros.","propriedade, apenas.","renda, apenas.","política partidária.","religião, apenas."],2,"Art. 4º."),
("Questão 4","Na interpretação do Estatuto, leva-se em conta a condição peculiar da criança e do adolescente como",["pessoas em desenvolvimento.","adultos pequenos.","incapazes absolutos.","trabalhadores.","consumidores."],3,"Art. 6º.")]
t1="<strong>Atendimento de um menino</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, atendeu um menino que dizia ter doze anos, completados na semana anterior, perdido na praça central."
t2="<strong>Fila de atendimento</strong><br><br>Num posto de saúde de Vila Nova, havia grande fila. Uma mãe chegou com o filho de sete anos com febre alta, e o guarda que organizava a fila a encaminhou ao atendimento antes de outras pessoas."
t3="<strong>Pai ausente</strong><br><br>Um pai de Vila Nova nunca visitou nem acompanhou o filho de dez anos, sem justificativa. A mãe procurou orientação sobre o direito do filho."
tx={"eca1a":t1,"eca1b":t2,"eca1c":t3}
# n=1
q(1,"O Estatuto da Criança e do Adolescente dispõe sobre a",["proteção integral à criança e ao adolescente.","proteção apenas do adolescente infrator.","aplicação de penas a adolescentes.","tutela do idoso.","disciplina do trabalho infantil, apenas."],"Art. 1º.")
q(1,"Considera-se adolescente a pessoa entre",["doze e dezoito anos de idade.","dez e catorze anos.","catorze e dezesseis anos.","dezesseis e vinte anos.","dezoito e vinte e um anos."],"Art. 2º.")
q(1,"Nos casos expressos em lei, aplica-se excepcionalmente o Estatuto às pessoas entre dezoito e",["vinte e um anos de idade.","vinte anos.","vinte e dois anos.","vinte e cinco anos.","trinta anos."],"Art. 2º, parágrafo único.")
q(1,"A criança e o adolescente gozam de todos os direitos fundamentais inerentes à",["pessoa humana.","pessoa maior.","família, apenas.","escola, apenas.","religião."],"Art. 3º.")
q(1,"Os direitos do Estatuto aplicam-se a todas as crianças e adolescentes, sem",["discriminação.","exceção de nenhum tipo, sempre.","cadastro.","residência fixa.","autorização."],"Art. 3º, parágrafo único.")
q(1,"É dever do poder público, da família, da comunidade e da sociedade em geral assegurar os direitos da criança com absoluta",["prioridade.","reserva.","opção.","condição.","liberdade de escolha."],"Art. 4º.")
q(1,"A garantia de prioridade compreende a precedência de atendimento nos serviços",["públicos ou de relevância pública.","particulares, apenas.","de turismo.","de transporte, apenas.","religiosos."],"Art. 4º, § 1º, b.")
q(1,"A garantia de prioridade compreende a preferência na formulação e na execução das políticas sociais",["públicas.","privadas.","partidárias.","religiosas.","comerciais."],"Art. 4º, § 1º, c.")
q(1,"A garantia de prioridade compreende a destinação privilegiada de recursos públicos nas áreas relacionadas com a proteção à",["infância e à juventude.","indústria.","agricultura.","política.","segurança de eventos."],"Art. 4º, § 1º, d.")
q(1,"Compete aos pais prestar aos filhos assistência",["afetiva, por meio de convívio ou de visitação periódica.","apenas financeira.","apenas jurídica.","apenas religiosa.","apenas esportiva."],"Art. 4º, § 2º.")
q(1,"Nenhuma criança ou adolescente será objeto de qualquer forma de negligência, discriminação, exploração, violência, crueldade e",["opressão.","adoção.","educação.","assistência.","proteção."],"Art. 5º.")
q(1,"A ação ou omissão que ofenda direito fundamental de criança ou adolescente é conduta ilícita sujeita a",["reparação de danos.","anistia.","prescrição imediata.","isenção.","perdão."],"Art. 5º, parágrafo único.")
q(1,"Na interpretação do Estatuto levam-se em conta os fins sociais a que ele se dirige e as exigências do",["bem comum.","mercado.","poder privado.","lucro.","partido."],"Art. 6º.")
q(1,"Considera-se assistência afetiva a presença física espontaneamente solicitada pela criança ou adolescente, quando possível de ser",["atendida.","ignorada.","negada.","adiada.","paga."],"Art. 4º, § 3º, III.")
q(1,"A orientação quanto às principais escolhas e oportunidades profissionais, educacionais e culturais é um exemplo de assistência",["afetiva.","financeira.","política.","militar.","tributária."],"Art. 4º, § 3º, I.")
q(1,"O abandono afetivo, no Estatuto, é incluído entre as condutas",["ilícitas, sujeitas a reparação de danos.","lícitas.","irrelevantes.","anistiadas.","apenas morais."],"Art. 5º, parágrafo único.")
q(1,"A proteção integral prevista no Estatuto abrange as crianças e os adolescentes",["sem discriminação de raça, etnia ou cor.","apenas de uma etnia.","apenas de uma região.","apenas da capital.","apenas os matriculados."],"Art. 3º, parágrafo único.")
q(1,"No texto do atendimento do menino, aos doze anos completos, a pessoa é considerada",["adolescente.","criança.","adulto.","jovem adulto.","idoso."],"Art. 2º.","eca1a")
q(1,"No texto da fila de atendimento, a precedência da criança no posto de saúde decorre da garantia de",["prioridade absoluta.","preferência econômica.","isonomia formal.","prioridade relativa.","sorteio."],"Art. 4º, § 1º, b.","eca1b")
q(1,"No texto do pai ausente, a omissão do pai, sem justificativa, pode ser considerada",["abandono afetivo, conduta ilícita sujeita a reparação.","exercício regular do direito.","direito do pai.","fato lícito.","mera liberalidade."],"Art. 5º, parágrafo único.","eca1c")
# n=2
q(2,"No Estatuto, o adolescente é a pessoa com idade",["entre doze e dezoito anos.","entre dez e doze anos.","entre doze e quinze anos.","entre quinze e dezoito anos.","a partir de quatorze anos."],"Art. 2º.")
q(2,"A criança e o adolescente gozam de oportunidades e facilidades que lhes facultem o desenvolvimento físico, mental, moral, espiritual e",["social, em condições de liberdade e dignidade.","financeiro, apenas.","militar.","esportivo, apenas.","político."],"Art. 3º.")
q(2,"Os direitos do Estatuto aplicam-se sem discriminação de nascimento, situação familiar, idade, sexo, raça, etnia ou cor, religião, deficiência e",["condição econômica, ambiente social ou local de moradia.","apenas moradia.","apenas religião.","apenas deficiência.","apenas idade."],"Art. 3º, parágrafo único.")
q(2,"Entre os que têm o dever de assegurar, com absoluta prioridade, os direitos da criança está o(a)",["comunidade.","empresa privada, apenas.","partido político.","sindicato.","imprensa."],"Art. 4º.")
q(2,"A preferência na formulação das políticas públicas é um dos itens da garantia de",["prioridade.","autonomia.","isonomia.","tutela.","guarda."],"Art. 4º, § 1º.")
q(2,"Na garantia de prioridade, a primazia de receber proteção e socorro vale em",["quaisquer circunstâncias.","apenas em dias de semana.","apenas nas cidades.","apenas em hospitais.","apenas nas escolas."],"Art. 4º, § 1º, a.")
q(2,"A assistência afetiva do art. 4º, § 2º, pode ocorrer por meio de convívio ou de",["visitação periódica.","pagamento de pensão.","viagem anual.","envio de cartas, apenas.","tutela."],"Art. 4º, § 2º.")
q(2,"O art. 5º do Estatuto proíbe a criança ser objeto de negligência, discriminação, exploração, violência, crueldade e",["opressão.","adoção.","tutela.","apadrinhamento.","guarda."],"Art. 5º.")
q(2,"Qualquer atentado, por ação ou omissão, aos direitos fundamentais da criança é punido",["na forma da lei.","a critério da família.","a critério da escola.","na forma da tradição.","sem pena."],"Art. 5º.")
q(2,"Na interpretação do Estatuto levam-se em conta os direitos e deveres",["individuais e coletivos.","apenas individuais.","apenas coletivos.","apenas dos pais.","apenas do Estado."],"Art. 6º.")
q(2,"Os direitos do Estatuto valem para todas as crianças, sem discriminação de",["deficiência.","apenas peso.","altura.","grau de escolaridade, apenas.","profissão dos pais, apenas."],"Art. 3º, parágrafo único.")
q(2,"A proteção integral, segundo o art. 1º, é objeto da",["lei.","tradição.","jurisprudência, apenas.","portaria.","recomendação."],"Art. 1º.")
q(2,"Na aplicação excepcional do Estatuto às pessoas entre 18 e 21 anos, a regra se aplica nos casos",["expressos em lei.","a critério do juiz sempre.","a critério da família.","a critério do guarda.","em qualquer caso."],"Art. 2º, parágrafo único.")
q(2,"A destinação privilegiada de recursos públicos é prioridade nas áreas de proteção à",["infância e à juventude.","indústria.","agricultura.","mineração.","pesca."],"Art. 4º, § 1º, d.")
q(2,"Considera-se assistência afetiva a solidariedade e o apoio nos momentos de intenso sofrimento ou de",["dificuldade.","festa.","competição.","viagem.","compra."],"Art. 4º, § 3º, II.")
q(2,"A assistência afetiva do Estatuto inclui a orientação quanto às principais escolhas e oportunidades profissionais, educacionais e",["culturais.","tributárias.","militares.","policiais.","partidárias."],"Art. 4º, § 3º, I.")
q(2,"No texto do atendimento do menino, a idade de 12 anos completos enquadra-se na definição do art.",["2º do Estatuto.","1º do Estatuto.","4º do Estatuto.","6º do Estatuto.","5º do Estatuto."],"Art. 2º.","eca1a")
q(2,"No texto da fila de atendimento, o guarda aplicou a prioridade do art. 4º, § 1º, alínea",["b: precedência de atendimento.","a: primazia de proteção.","c: preferência em políticas.","d: recursos.","e: nenhuma."],"Art. 4º, § 1º, b.","eca1b")
q(2,"No texto do pai ausente, o dever do pai de acompanhar a formação do filho decorre do art. 4º, § 2º, que fala em",["assistência afetiva.","pagamento apenas.","educação formal, apenas.","guarda compartilhada.","tutela."],"Art. 4º, § 2º.","eca1c")
q(2,"A garantia de prioridade, quanto às políticas sociais públicas, compreende a preferência na sua formulação e na sua",["execução.","revogação.","suspensão.","privatização.","divulgação."],"Art. 4º, § 1º, c.")
# n=3
q(3,"Assinale a alternativa correta.",["Criança é a pessoa até doze anos incompletos; adolescente é a que tem de doze a dezoito anos.","Criança é a pessoa até quatorze anos.","Adolescente é a pessoa de dez a dezoito anos.","Criança é a pessoa até doze anos completos.","Adolescente é a pessoa de doze a vinte e um anos."],"Art. 2º.")
q(3,"Considere. I. A garantia de prioridade inclui a precedência de atendimento. II. O Estatuto nunca se aplica a pessoas com mais de dezoito anos. III. Os direitos valem sem discriminação. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Aplica-se excepcionalmente a 18 a 21 anos (art. 2º, parágrafo único).")
q(3,"Assinale a INCORRETA.",["O dever de assegurar os direitos é só da família.","O dever cabe também à comunidade e ao poder público.","A prioridade é absoluta.","A assistência afetiva compete aos pais.","O abandono afetivo é conduta ilícita."],"O dever é da família, da comunidade, da sociedade em geral e do poder público (art. 4º).")
q(3,"Assinale a alternativa que traz os itens da garantia de prioridade.",["Primazia de proteção e socorro, precedência de atendimento, preferência nas políticas, destinação privilegiada de recursos.","Primazia, equidade, recursos e isonomia.","Precedência, prioridade, igualdade e tutela.","Preferência, pensão, recursos e guarda.","Socorro, saúde, lazer e esporte."],"Art. 4º, § 1º.")
q(3,"No art. 4º, entre os direitos que se assegura com absoluta prioridade, NÃO se inclui expressamente o direito",["à propriedade privada.","à vida.","à saúde.","à educação.","à convivência familiar e comunitária."],"A propriedade não consta do rol do art. 4º.")
q(3,"A condição peculiar da criança e do adolescente como pessoas em desenvolvimento é considerada, pelo Estatuto, na",["interpretação da lei.","definição de penas.","fixação de tributos.","definição de competências.","eleição de conselheiros."],"Art. 6º.")
q(3,"Segundo o art. 5º, parágrafo único, a ação ou omissão que ofenda direito fundamental, incluídos os casos de abandono afetivo, sujeita-se a reparação de danos, sem prejuízo de",["outras sanções cabíveis.","anistia.","prescrição imediata.","perdão judicial obrigatório.","prisão sempre."],"Art. 5º, parágrafo único.")
q(3,"A assistência afetiva do art. 4º, § 3º, abrange as hipóteses de",["orientação, solidariedade e presença física quando possível.","apenas pensão.","apenas educação formal.","apenas moradia.","apenas tutela."],"Art. 4º, § 3º.")
q(3,"A destinação privilegiada de recursos públicos para a infância é uma forma de efetivação da",["prioridade absoluta.","isonomia formal.","reserva do possível.","tutela patrimonial.","guarda."],"Art. 4º, § 1º, d.")
q(3,"A aplicação excepcional do Estatuto a pessoas entre 18 e 21 anos exige que o caso seja",["expresso em lei.","indicado pelo guarda.","indicado pelo pai.","indicado pelo diretor.","qualquer um."],"Art. 2º, parágrafo único.")
q(3,"O art. 3º assegura, por lei ou por outros meios, todas as oportunidades e facilidades para o desenvolvimento físico, mental, moral, espiritual e social, em condições de",["liberdade e dignidade.","trabalho.","riqueza.","isolamento.","competição."],"Art. 3º.")
q(3,"No art. 4º, o dever de assegurar os direitos com absoluta prioridade cabe à família, à comunidade, à sociedade em geral e ao",["poder público.","setor privado, apenas.","clero.","sindicato.","mercado."],"Art. 4º.")
q(3,"Os direitos fundamentais da criança aplicam-se independentemente de sua condição econômica e do",["ambiente social, região e local de moradia.","apenas local de nascimento.","apenas sexo.","apenas idade.","apenas escolaridade."],"Art. 3º, parágrafo único.")
q(3,"O Estatuto considera ilícita a ação ou omissão que ofenda direito fundamental de criança ou adolescente previsto na própria",["lei, incluídos os casos de abandono afetivo.","Constituição, apenas.","portaria.","sentença.","súmula."],"Art. 5º, parágrafo único.")
q(3,"A proteção e o socorro, na garantia de prioridade, devem ser prestados à criança em",["quaisquer circunstâncias.","horário comercial.","sábados.","cidades grandes.","rodovias."],"Art. 4º, § 1º, a.")
q(3,"No texto do atendimento do menino, a idade de doze anos completos na semana anterior indica que o menino é",["adolescente.","criança.","adulto.","jovem de 18 a 21 anos.","incapaz."],"Art. 2º.","eca1a")
q(3,"No texto da fila de atendimento, o encaminhamento da criança de sete anos antes de outras pessoas decorre da",["precedência de atendimento nos serviços públicos.","fila preferencial de idosos.","ordem alfabética.","ordem de chegada.","escolha do guarda."],"Art. 4º, § 1º, b.","eca1b")
q(3,"No texto do pai ausente, a mãe pode pleitear a reparação de danos, porque o abandono afetivo é, segundo o Estatuto,",["conduta ilícita.","direito do pai.","fato natural.","fato irrelevante.","apenas dever moral."],"Art. 5º, parágrafo único.","eca1c")
q(3,"No texto do pai ausente, a assistência afetiva compreende a orientação, o apoio em momentos de sofrimento e a",["presença física, quando solicitada e possível.","entrega de bens.","pensão alimentícia, apenas.","moradia.","tutela."],"Art. 4º, § 3º.","eca1c")
q(3,"No texto da fila de atendimento, a precedência vale para o atendimento nos serviços",["públicos ou de relevância pública.","apenas particulares.","apenas privados.","apenas de transporte.","apenas religiosos."],"Art. 4º, § 1º, b.","eca1b")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("ECA: arts. 1º a 6º",[
 ("int","Proteção integral",["art. 1º","direitos fundamentais"],"seção 1"),
 ("ida","Idades",["criança: até 12 incompletos","adolescente: 12 a 18","exceção: 18 a 21"],"seção 1"),
 ("dev","Dever",["família, comunidade","sociedade, poder público","prioridade absoluta"],"seção 2"),
 ("pri","Itens da prioridade",["primazia","precedência","preferência e recursos"],"seção 2"),
 ("pro","Proibições",["negligência, violência","crueldade, opressão","abandono afetivo"],"seção 3"),
 ("int2","Interpretação",["fins sociais","bem comum","pessoas em desenvolvimento"],"seção 3")],
 "Na prova: idades, quatro itens da prioridade e quem tem o dever")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a proteção integral e as idades; as demais, os deveres, a prioridade e a interpretação.","Fontes: Edital 02/2026, Anexo I; Lei 8.069/1990 (ECA), arts. 1º a 6º, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("eca-1","ECA: disposições preliminares (arts. 1º a 6º)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (1º a 6º)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","A consolidação mostra a redação dada pela Lei 15.240/2025 aos arts. 4º e 5º (assistência afetiva e abandono afetivo); conferir no Planalto.","Trechos de lei copiados de fontes/eca.txt por programa.","Casos eca1a, eca1b e eca1c fictícios."],
 fontes_conferidas=["ECA, arts. 1º a 6º: texto da Câmara, copiado por programa."])
gravar("eca-1",aula_html,banco("eca-1",Q),tx)
