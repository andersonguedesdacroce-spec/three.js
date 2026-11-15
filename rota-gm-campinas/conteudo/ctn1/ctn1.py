import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctn.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os arts. 77 a 79 do Código Tributário Nacional tratam das taxas e do poder de polícia. O assunto aparece na prova da Guarda Municipal porque o guarda é, em essência, um agente do poder de polícia do Município: a taxa de fiscalização, o alvará e a multa decorrem dele. A Vunesp cobra o fato gerador das taxas (poder de polícia ou serviço público específico e divisível), o conceito legal de poder de polícia, o que significa regular o exercício e a definição de serviço utilizado, específico e divisível."
S={}
S[1]="## 1. Taxas e fato gerador\n\n"+L("art. 77","Art. 77. As taxas cobradas","Art. 78.")+"""

As taxas podem ser cobradas pela União, pelos Estados, pelo Distrito Federal e pelos Municípios, no âmbito de suas atribuições. O fato gerador é o exercício regular do poder de polícia ou a utilização, efetiva ou potencial, de serviço público específico e divisível, prestado ao contribuinte ou posto à sua disposição. A taxa não pode ter base de cálculo ou fato gerador idênticos aos de imposto, nem ser calculada em função do capital das empresas.
"""
S[2]="## 2. Poder de polícia\n\n"+L("art. 78","Art. 78. Considera-se poder de polícia","Art. 79.")+"""

Poder de polícia é a atividade da administração pública que, limitando ou disciplinando direito, interesse ou liberdade, regula a prática de ato ou abstenção de fato, em razão de interesse público concernente à segurança, à higiene, à ordem, aos costumes, à disciplina da produção e do mercado, ao exercício de atividades econômicas dependentes de concessão ou autorização, à tranquilidade pública ou ao respeito à propriedade e aos direitos individuais ou coletivos. O exercício é regular quando feito pelo órgão competente, nos limites da lei, com observância do processo legal e, na atividade discricionária, sem abuso ou desvio de poder.
"""
S[3]="## 3. Serviços públicos que geram taxa\n\n"+L("art. 79","Art. 79. Os serviços públicos","Art. 80.")+"""

Os serviços públicos que podem gerar taxa são considerados utilizados pelo contribuinte efetivamente, quando por ele usufruídos a qualquer título, ou potencialmente, quando de utilização compulsória e postos à sua disposição mediante atividade administrativa em efetivo funcionamento. São específicos quando possam ser destacados em unidades autônomas de intervenção, de utilidade ou de necessidade públicas, e divisíveis quando suscetíveis de utilização separadamente por cada usuário.
"""
S[5]="""## 5. Na rotina do guarda

- **Fiscalização:** o guarda exerce o poder de polícia administrativo do Município ao fiscalizar posturas, comércio e uso do espaço público.
- **Limites:** o poder de polícia só é regular se exercido pelo órgão competente, nos limites da lei, com processo legal e sem abuso ou desvio de poder.
- **Taxa de polícia:** a taxa de fiscalização (alvará) tem como fato gerador o exercício regular do poder de polícia.
- **Abuso:** a abordagem ou autuação fora da competência ou com desvio de finalidade não é exercício regular.
- **Interesse público:** segurança, ordem, tranquilidade e respeito aos direitos individuais ou coletivos fundamentam a limitação de direitos.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Fato gerador da taxa | Poder de polícia ou serviço público específico e divisível |
| Quem pode cobrar | União, Estados, DF e Municípios, no âmbito de suas atribuições |
| Base de cálculo | Não pode ser idêntica à de imposto |
| Capital das empresas | A taxa não é calculada em função dele |
| Poder de polícia | Atividade que limita ou disciplina direito, interesse ou liberdade |
| Exercício regular | Órgão competente, limites da lei, processo legal, sem abuso ou desvio |
| Serviço utilizado | Efetivamente ou potencialmente |
| Serviço específico | Destacável em unidades autônomas |
| Serviço divisível | Utilizável separadamente por cada usuário |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 77 | Taxas: poder de polícia ou serviço específico e divisível |
| Parágrafo único | Sem base idêntica à de imposto; sem capital das empresas |
| Art. 78 | Conceito de poder de polícia |
| Parágrafo único | Regular: competente, lei, processo legal, sem desvio |
| Art. 79 | Serviço utilizado, específico e divisível |
| Utilização potencial | Compulsória e posta à disposição |
"""
QR=[("Questão 1","As taxas têm como fato gerador o exercício regular do poder de polícia ou a utilização, efetiva ou potencial, de serviço público",["específico e divisível, prestado ao contribuinte ou posto à sua disposição.","geral e indivisível.","privado e divisível.","genérico e indivisível.","comercial e específico."],0,"Art. 77."),
("Questão 2","A taxa não pode ter base de cálculo ou fato gerador idênticos aos que correspondam a",["imposto.","contribuição de melhoria.","tarifa.","multa.","empréstimo compulsório."],1,"Art. 77, parágrafo único."),
("Questão 3","Considera-se regular o exercício do poder de polícia quando desempenhado pelo órgão competente nos limites da lei aplicável, com observância do",["processo legal.","interesse do agente.","costume.","regulamento interno apenas.","consentimento do particular."],2,"Art. 78, parágrafo único."),
("Questão 4","Os serviços públicos considerados específicos são aqueles que possam ser destacados em",["unidades autônomas de intervenção, de utilidade ou de necessidade públicas.","grupos de contribuintes.","regiões inteiras.","áreas rurais.","bairros."],3,"Art. 79, II.")]
t1="<strong>Fiscalização de um bar</strong><br><br>A Guarda Municipal de Vila Nova, cidade fictícia, fiscaliza um bar que funciona sem alvará e com som alto após o horário permitido, e o Município cobra a taxa de fiscalização."
t2="<strong>Taxa de iluminação</strong><br><br>Um município de Vila Nova instituiu taxa para custear a iluminação de todas as ruas, calculada sobre o valor do imóvel de cada contribuinte."
t3="<strong>Abordagem fora da competência</strong><br><br>Um guarda de Vila Nova, sem designação do órgão competente, passou a fiscalizar atividade econômica em outro município e aplicou multa por conta própria."
tx={"ctn1a":t1,"ctn1b":t2,"ctn1c":t3}
# n=1
q(1,"As taxas podem ser cobradas pela União, pelos Estados, pelo Distrito Federal e pelos",["Municípios, no âmbito de suas atribuições.","particulares.","consórcios privados.","associações.","bancos."],"Art. 77.")
q(1,"O exercício regular do poder de polícia é um dos fatos geradores da",["taxa.","contribuição de melhoria.","tarifa.","multa.","anuidade."],"Art. 77.")
q(1,"A taxa não pode ser calculada em função do capital das",["empresas.","pessoas físicas.","fundações.","igrejas.","escolas."],"Art. 77, parágrafo único.")
q(1,"Poder de polícia é atividade da administração pública que, limitando ou disciplinando direito, interesse ou liberdade, regula a prática de ato ou abstenção de",["fato.","norma.","valor.","pena.","imposto."],"Art. 78.")
q(1,"O poder de polícia é exercido em razão de interesse público concernente à segurança, à higiene, à ordem, aos costumes e à",["tranquilidade pública, entre outros.","renda.","propriedade privada apenas.","religião.","política partidária."],"Art. 78.")
q(1,"O poder de polícia visa também ao respeito à propriedade e aos direitos individuais ou",["coletivos.","empresariais.","políticos.","partidários.","religiosos."],"Art. 78.")
q(1,"Considera-se regular o exercício do poder de polícia quando desempenhado pelo órgão",["competente.","vizinho.","privado.","estrangeiro.","incompetente."],"Art. 78, parágrafo único.")
q(1,"No exercício discricionário do poder de polícia, não pode haver abuso ou desvio de",["poder.","finalidade apenas.","prazo.","valor.","tempo."],"Art. 78, parágrafo único.")
q(1,"Os serviços públicos utilizados efetivamente são aqueles usufruídos pelo contribuinte a qualquer",["título.","preço.","horário.","tempo.","valor."],"Art. 79, I, a.")
q(1,"Os serviços utilizados potencialmente são os de utilização",["compulsória postos à disposição do contribuinte.","facultativa.","eventual.","paga.","noturna."],"Art. 79, I, b.")
q(1,"Os serviços divisíveis são os suscetíveis de utilização separadamente por parte de cada um dos seus",["usuários.","vizinhos.","funcionários.","contribuintes inadimplentes.","agentes."],"Art. 79, III.")
q(1,"A utilização potencial exige que o serviço seja posto à disposição mediante atividade administrativa em efetivo",["funcionamento.","estudo.","planejamento.","projeto.","debate."],"Art. 79, I, b.")
q(1,"A taxa tem como fato gerador também a utilização de serviço público específico e",["divisível.","indivisível.","geral.","privado.","comercial."],"Art. 77.")
q(1,"O poder de polícia limita ou disciplina direito, interesse ou",["liberdade.","dever.","imposto.","tributo.","salário."],"Art. 78.")
q(1,"A base de cálculo da taxa não pode ser idêntica à de",["imposto.","tarifa.","multa.","preço público.","contribuição social."],"Art. 77, parágrafo único.")
q(1,"A taxa de fiscalização que o Município cobra pelo alvará funda-se no exercício do",["poder de polícia.","poder legislativo.","poder constituinte.","poder moderador.","poder econômico."],"Art. 77.")
q(1,"No texto da fiscalização do bar, a taxa de fiscalização do Município tem como fato gerador o exercício regular do",["poder de polícia.","poder econômico.","poder privado.","poder familiar.","poder militar."],"Art. 77.","ctn1a")
q(1,"No texto da taxa de iluminação, a taxa não pode ter base de cálculo idêntica à de",["imposto, como o valor do imóvel.","tarifa.","multa.","preço.","anuidade."],"Art. 77, parágrafo único.","ctn1b")
q(1,"No texto da abordagem fora da competência, a atuação sem competência não configura exercício",["regular do poder de polícia.","do poder legislativo.","do dever de agir.","do direito de petição.","da cidadania."],"Art. 78, parágrafo único.","ctn1c")
q(1,"A taxa de polícia incide sobre o exercício regular do poder de polícia, que é atividade da administração",["pública.","privada.","religiosa.","partidária.","sindical."],"Art. 78.")
# n=2
q(2,"A taxa cobrada pelo Município é devida no âmbito de suas respectivas",["atribuições.","vontades.","dívidas.","receitas.","áreas rurais."],"Art. 77.")
q(2,"O poder de polícia regula atos em razão de interesse público concernente ao exercício de atividades econômicas dependentes de",["concessão ou autorização do Poder Público.","registro civil.","mandato eletivo.","contrato privado.","herança."],"Art. 78.")
q(2,"O poder de polícia pode disciplinar a produção e o",["mercado.","lazer.","voto.","culto.","ensino."],"Art. 78.")
q(2,"O poder de polícia visa à tranquilidade pública, à segurança, à ordem e aos",["costumes.","tributos.","lucros.","juros.","contratos."],"Art. 78.")
q(2,"O exercício do poder de polícia exige observância do processo legal e, quanto à atividade discricionária, ausência de abuso ou desvio de",["poder.","prazo.","valor.","lugar.","pessoa."],"Art. 78, parágrafo único.")
q(2,"Quanto ao serviço, o art. 79 trata da utilização efetiva ou",["potencial.","eventual.","ocasional.","indireta.","acessória."],"Art. 79, I.")
q(2,"Serviço específico é o que pode ser destacado em unidades autônomas de intervenção, de utilidade ou de necessidade",["públicas.","privadas.","comerciais.","eventuais.","pessoais."],"Art. 79, II.")
q(2,"A utilização potencial do serviço depende de a utilização ser",["compulsória.","facultativa.","eventual.","mediante contrato.","temporária."],"Art. 79, I, b.")
q(2,"A taxa pode ter por fato gerador serviço prestado ao contribuinte ou posto à sua",["disposição.","vista.","escolha.","venda.","guarda."],"Art. 77.")
q(2,"A atuação do poder de polícia, para ser regular, deve estar nos limites da lei",["aplicável.","local, apenas.","pessoal.","costumeira.","interna."],"Art. 78, parágrafo único.")
q(2,"A taxa que usa a mesma base de cálculo de um imposto é",["vedada.","permitida.","incentivada.","obrigatória.","suspensa."],"Art. 77, parágrafo único.")
q(2,"Considera-se divisível o serviço suscetível de utilização, separadamente, por parte de cada um dos seus",["usuários.","fornecedores.","agentes.","gestores.","fiscais."],"Art. 79, III.")
q(2,"O art. 78 dispõe sobre o conceito de",["poder de polícia.","imposto.","contribuição.","tarifa.","empréstimo."],"Art. 78.")
q(2,"O art. 79 define, para o art. 77, quando os serviços públicos são utilizados, específicos e",["divisíveis.","gerais.","indivisíveis.","privados.","comerciais."],"Art. 79.")
q(2,"A limitação a direito, interesse ou liberdade, no poder de polícia, é feita em razão do interesse",["público.","privado.","do agente.","do vizinho.","do mercado."],"Art. 78.")
q(2,"No texto da fiscalização do bar, o funcionamento sem alvará e o som alto envolvem interesses de segurança, ordem e",["tranquilidade pública.","lucros.","moda.","turismo.","comércio exterior."],"Art. 78.","ctn1a")
q(2,"No texto da taxa de iluminação, a iluminação de todas as ruas é serviço de natureza",["geral e indivisível, não específico.","específica e divisível.","privada.","comercial.","particular."],"Art. 79, II e III.","ctn1b")
q(2,"No texto da abordagem fora da competência, o desvio decorre do fato de o guarda não ser o órgão",["competente.","fiscal da lei.","da câmara.","do Judiciário.","da União."],"Art. 78, parágrafo único.","ctn1c")
q(2,"A utilização efetiva do serviço público ocorre quando ele é usufruído pelo contribuinte a qualquer",["título.","tempo.","preço.","horário.","valor."],"Art. 79, I, a.")
q(2,"A taxa do art. 77 é um tributo que pode ser cobrado pelos Municípios no âmbito de suas atribuições; o seu fato gerador é o poder de polícia ou o serviço",["público específico e divisível.","privado.","geral.","indivisível.","eventual."],"Art. 77.")
# n=3
q(3,"Assinale a alternativa correta sobre o poder de polícia, nos termos do CTN.",["É atividade da administração que limita ou disciplina direito, interesse ou liberdade; é regular quando exercido pelo órgão competente, nos limites da lei, com processo legal e sem desvio.","É atividade privada.","Exerce-se sem processo legal.","Dispensa competência.","Aplica-se apenas à União."],"Art. 78.")
q(3,"Considere. I. As taxas podem ter fato gerador o poder de polícia. II. A taxa pode ser calculada sobre o capital das empresas. III. A base de cálculo da taxa não pode ser a mesma de um imposto. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A taxa não é calculada em função do capital das empresas (art. 77, parágrafo único).")
q(3,"Assinale a INCORRETA.",["O serviço indivisível pode gerar taxa.","O serviço divisível pode gerar taxa.","O serviço específico pode gerar taxa.","O poder de polícia pode gerar taxa.","A utilização potencial pode gerar taxa."],"A taxa exige serviço específico e divisível (art. 77).")
q(3,"A utilização potencial de serviço exige que ele seja compulsório e posto à disposição mediante atividade administrativa em efetivo",["funcionamento.","projeto.","debate.","estudo.","contrato."],"Art. 79, I, b.")
q(3,"Considera-se regular o exercício do poder de polícia quando desempenhado nos limites da lei, com observância do processo legal e, tratando-se de atividade discricionária, sem abuso ou",["desvio de poder.","consentimento.","anuência do particular.","recurso.","aprovação do Legislativo."],"Art. 78, parágrafo único.")
q(3,"A competência para cobrar taxas é da União, dos Estados, do Distrito Federal e dos Municípios, cada um no âmbito de suas",["respectivas atribuições.","vontades.","dívidas.","receitas.","decisões."],"Art. 77.")
q(3,"A taxa de serviço exige que o serviço seja prestado ao contribuinte ou posto à sua disposição, sendo específico e",["divisível.","geral.","indivisível.","privado.","facultativo."],"Art. 77.")
q(3,"No exercício do poder de polícia, o desvio de poder ocorre quando o agente se afasta do",["interesse público que justifica a atividade.","horário.","local.","regimento da guarda.","uniforme."],"Art. 78, parágrafo único.")
q(3,"O poder de polícia pode ser exercido em razão do interesse público relativo à higiene, que se refere à proteção da",["saúde coletiva.","propriedade industrial.","imagem.","renda.","moda."],"Art. 78.")
q(3,"A taxa de polícia é cobrada do contribuinte quando o poder de polícia é exercido de forma",["regular.","irregular.","abusiva.","incompetente.","ilegal."],"Art. 77.")
q(3,"Para o CTN, o serviço específico é aquele que pode ser destacado em unidades autônomas, o que o distingue do serviço",["geral.","divisível.","específico.","utilizado.","efetivo."],"Art. 79, II.")
q(3,"A utilização efetiva ocorre quando o serviço é usufruído a qualquer título, enquanto a potencial depende de utilização compulsória e de serviço posto à disposição, ambas no inciso I do art.",["79.","77.","78.","80.","81."],"Art. 79, I.")
q(3,"A taxa não pode ser calculada em função do capital das empresas, o que a distingue de tributos sobre o",["patrimônio ou a renda.","serviço.","poder de polícia.","uso de bem.","contrato."],"Art. 77, parágrafo único.")
q(3,"A cobrança de taxa depende de o poder de polícia ser regularmente exercido, o que inclui a observância do",["processo legal.","interesse do agente.","consentimento do contribuinte.","costume local.","regimento da câmara."],"Art. 78, parágrafo único.")
q(3,"Entre os interesses que justificam o poder de polícia está o respeito à propriedade e aos direitos individuais ou",["coletivos.","empresariais.","comerciais.","partidários.","religiosos."],"Art. 78.")
q(3,"No texto da fiscalização do bar, a atuação da guarda ao fiscalizar alvará e som é exemplo de exercício do poder de polícia em razão da ordem e da",["tranquilidade pública.","moda.","renda.","religião.","política."],"Art. 78.","ctn1a")
q(3,"No texto da fiscalização do bar, a taxa só é devida se o poder de polícia for exercido de forma",["regular, pelo órgão competente.","abusiva.","privada.","paralela.","informal."],"Art. 77 e art. 78, parágrafo único.","ctn1a")
q(3,"No texto da taxa de iluminação, a taxa é inválida porque, entre outros motivos, o serviço é",["geral e indivisível, e a base de cálculo é a do imposto.","específico.","divisível.","utilizado efetivamente.","prestado ao contribuinte."],"Arts. 77 e 79.","ctn1b")
q(3,"No texto da taxa de iluminação, calcular a taxa sobre o valor do imóvel ofende o parágrafo único do art.",["77.","78.","79.","80.","81."],"Art. 77, parágrafo único.","ctn1b")
q(3,"No texto da abordagem fora da competência, a multa aplicada pelo guarda sem designação",["não é exercício regular do poder de polícia.","é regular.","é facultativa.","é obrigatória.","é inexigível apenas a posteriori."],"Art. 78, parágrafo único.","ctn1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("CTN: taxas e poder de polícia (arts. 77 a 79)",[
 ("taxa","Taxa",["quem cobra: União, Estados, DF, Municípios","fato gerador"],"seção 1"),
 ("lim","Limites da taxa",["base distinta de imposto","sem capital das empresas"],"seção 1"),
 ("pp","Poder de polícia",["limita direito, interesse ou liberdade","interesse público"],"seção 2"),
 ("reg","Exercício regular",["órgão competente","limites da lei","processo legal, sem desvio"],"seção 2"),
 ("uti","Serviço utilizado",["efetivamente","potencialmente: compulsório"],"seção 3"),
 ("esp","Específico e divisível",["destacável em unidades autônomas","utilizável por cada usuário"],"seção 3")],
 "Na prova: fato gerador da taxa e requisitos do exercício regular")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz as taxas; as demais, o poder de polícia e os serviços utilizados, específicos e divisíveis.","Fontes: Edital 02/2026, Anexo I; Lei 5.172/1966 (Código Tributário Nacional), arts. 77 a 79, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctn-1","CTN: taxas e poder de polícia (arts. 77 a 79)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (77 a 79)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Material curto (3 artigos): 60 questões exploram o mesmo conteúdo com ângulos variados; conferir repetições na revisão humana.","Trechos de lei copiados de fontes/ctn.txt por programa.","Casos ctn1a, ctn1b e ctn1c fictícios."],
 fontes_conferidas=["CTN, arts. 77 a 79: texto da Câmara, copiado por programa."])
gravar("ctn-1",aula_html,banco("ctn-1",Q),tx)
