import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='dudh.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Declaração Universal dos Direitos Humanos (ONU, 1948) é o documento-base dos direitos humanos e aparece na prova da Guarda Municipal pelo seu conteúdo: vida, liberdade e segurança, proibição da tortura e da escravidão, igualdade, presunção de inocência, vedação de prisão arbitrária, privacidade, liberdade de circulação, asilo, nacionalidade, família, propriedade, pensamento, expressão, reunião e participação política. Este primeiro posto cobre o Preâmbulo e os arts. 1º a 21 (direitos civis e políticos). A Vunesp cobra o texto quase literal: preste atenção às palavras exatas de cada artigo."
S={}
S[1]="## 1. Preâmbulo e arts. 1º a 8º\n\n"+L("Preâmbulo","Considerando que o reconhecimento","Art. 1º ")+"\n\n"+L("arts. 1º e 2º","Art. 1º Todos","Art. 3º ")+"\n\n"+L("arts. 3º a 6º","Art. 3º ","Art. 7º ")+"\n\n"+L("arts. 7º e 8º","Art. 7º ","Art. 9º ")+"""

O Preâmbulo reconhece a dignidade inerente a todos os membros da família humana e seus direitos iguais e inalienáveis como fundamento da liberdade, da justiça e da paz, e proclama a Declaração como ideal comum a atingir por todos os povos e nações. Todos os seres humanos nascem livres e iguais em dignidade e em direitos, dotados de razão e de consciência, e devem agir em espírito de fraternidade. Podem invocar os direitos sem distinção alguma, nomeadamente de raça, cor, sexo, língua, religião, opinião política, origem nacional ou social, fortuna, nascimento ou outra situação.

Todo indivíduo tem direito à vida, à liberdade e à segurança pessoal. Ninguém será mantido em escravatura ou servidão. Ninguém será submetido a tortura nem a penas ou tratamentos cruéis, desumanos ou degradantes. Todos têm direito ao reconhecimento da personalidade jurídica, são iguais perante a lei e têm direito a igual proteção contra qualquer discriminação, e a recurso efetivo contra atos que violem os direitos fundamentais.
"""
S[2]="## 2. Arts. 9º a 15: prisão, julgamento, presunção de inocência, privacidade, circulação e asilo\n\n"+L("arts. 9º e 10","Art. 9º ","Art. 11º ")+"\n\n"+L("art. 11","Art. 11º ","Art. 12º ")+"\n\n"+L("arts. 12 e 13","Art. 12º ","Art. 14º ")+"\n\n"+L("arts. 14 e 15","Art. 14º ","Art. 16º ")+"""

Ninguém pode ser arbitrariamente preso, detido ou exilado. Toda pessoa tem direito, em plena igualdade, a uma causa equitativa e publicamente julgada por tribunal independente e imparcial. Toda pessoa acusada de ato delituoso presume-se inocente até que sua culpabilidade fique legalmente provada em processo público com todas as garantias de defesa. Ninguém será condenado por ações ou omissões que, no momento, não constituíam delito, e não se infligirá pena mais grave do que a aplicável no momento do ato (legalidade e irretroatividade).

Ninguém sofrerá intromissões arbitrárias na vida privada, na família, no domicílio ou na correspondência, nem ataques à honra e reputação. Toda pessoa tem direito de circular livremente e escolher sua residência no interior de um Estado, de abandonar qualquer país, inclusive o seu, e de regressar ao seu país. Toda pessoa perseguida tem direito de procurar e beneficiar-se de asilo, mas não em caso de crime de direito comum ou atividades contrárias aos fins e princípios da ONU. Toda pessoa tem direito a uma nacionalidade e ninguém pode ser arbitrariamente privado dela.
"""
S[3]="## 3. Arts. 16 a 21: família, propriedade, pensamento, expressão, reunião e participação política\n\n"+L("arts. 16 e 17","Art. 16º ","Art. 18º ")+"\n\n"+L("arts. 18 e 19","Art. 18º ","Art. 20º ")+"\n\n"+L("arts. 20 e 21","Art. 20º ","Art. 22º ")+"""

A partir da idade núbil, homem e mulher têm direito de casar e constituir família, sem restrição de raça, nacionalidade ou religião; o casamento exige o livre e pleno consentimento dos futuros esposos, e a família é o elemento natural e fundamental da sociedade, com direito à proteção da sociedade e do Estado. Toda pessoa, individual ou coletiva, tem direito à propriedade e ninguém pode ser arbitrariamente privado dela.

Toda pessoa tem direito à liberdade de pensamento, consciência e religião, o que inclui mudar de religião e manifestá-la pelo ensino, prática, culto e ritos. Tem direito à liberdade de opinião e expressão, inclusive de procurar, receber e difundir informações sem consideração de fronteiras. Tem direito à liberdade de reunião e associação pacíficas, e ninguém pode ser obrigado a fazer parte de uma associação. Toda pessoa tem o direito de tomar parte na direção dos negócios públicos do seu país, direta ou por representantes livremente escolhidos, e acesso, em condições de igualdade, às funções públicas; a vontade do povo é o fundamento da autoridade dos poderes públicos e exprime-se por eleições honestas, periódicas, por sufrágio universal e igual, com voto secreto.
"""
S[5]="""## 5. Na rotina do guarda

- **Prisão arbitrária (art. 9º):** o guarda só detém dentro das hipóteses legais; a detenção arbitrária viola a Declaração.
- **Tortura e tratamento degradante (art. 5º):** proibidos sempre, em qualquer circunstância.
- **Presunção de inocência (art. 11):** o preso é tratado como inocente até a prova legal da culpa.
- **Privacidade e domicílio (art. 12):** não há intromissão arbitrária no domicílio nem na correspondência.
- **Reunião pacífica (art. 20):** a liberdade de reunião e associação pacíficas é direito, e o guarda a respeita e protege.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Art. 1º | Nascem livres e iguais em dignidade e em direitos |
| Art. 3º | Vida, liberdade e segurança pessoal |
| Art. 4º | Escravatura e servidão proibidas |
| Art. 5º | Tortura, penas e tratamentos cruéis, desumanos ou degradantes |
| Art. 9º | Ninguém pode ser arbitrariamente preso, detido ou exilado |
| Art. 11 | Presunção de inocência; irretroatividade |
| Art. 12 | Vida privada, família, domicílio, correspondência, honra |
| Art. 13 | Circular, escolher residência, sair e voltar ao país |
| Art. 14 | Asilo, salvo crime comum |
| Art. 17 | Propriedade; ninguém privado arbitrariamente |
| Art. 20 | Reunião e associação pacíficas; ninguém é obrigado a associar-se |
| Art. 21 | Participação política; sufrágio universal; voto secreto |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Arts. 1º e 2º | Igualdade em dignidade e direitos, sem distinção |
| Art. 3º | Vida, liberdade, segurança |
| Arts. 4º e 5º | Sem escravidão nem tortura |
| Arts. 6º a 8º | Personalidade jurídica, igualdade perante a lei, recurso efetivo |
| Arts. 9º a 11 | Sem prisão arbitrária; julgamento justo; presunção de inocência |
| Art. 12 | Privacidade |
| Arts. 13 a 15 | Circulação, asilo, nacionalidade |
| Arts. 16 e 17 | Família, propriedade |
| Arts. 18 a 20 | Pensamento, expressão, reunião |
| Art. 21 | Participação política |
"""
QR=[("Questão 1","Segundo a Declaração Universal dos Direitos Humanos, ninguém pode ser arbitrariamente",["preso, detido ou exilado.","fiscalizado.","aposentado.","transferido de cidade.","avaliado."],0,"Art. 9º."),
("Questão 2","Toda pessoa acusada de um ato delituoso presume-se inocente até que a sua culpabilidade fique legalmente provada em processo",["público em que todas as garantias de defesa lhe sejam asseguradas.","sigiloso.","administrativo, apenas.","policial.","verbal."],1,"Art. 11, 1."),
("Questão 3","Ninguém sofrerá intromissões arbitrárias na sua vida privada, na sua família, no seu domicílio ou na sua",["correspondência, nem ataques à sua honra e reputação.","profissão.","propriedade.","escola.","vizinhança."],2,"Art. 12."),
("Questão 4","A família é o elemento natural e fundamental da sociedade e tem direito à proteção desta e do",["Estado.","mercado.","vizinho.","partido.","clero."],3,"Art. 16, 3.")]
t1="<strong>Detenção sem motivo</strong><br><br>Um guarda municipal de Vila Nova, cidade fictícia, deteve um jovem durante uma noite inteira sem qualquer motivo legal, apenas porque ele estava na praça."
t2="<strong>Passeata pacífica</strong><br><br>Um grupo de moradores de Vila Nova organizou uma passeata pacífica por melhorias no bairro, e a guarda foi acionada para acompanhar."
t3="<strong>Pedido de asilo</strong><br><br>Um estrangeiro perseguido em seu país procurou abrigo em Vila Nova e disse que pretendia pedir asilo."
tx={"dudh1a":t1,"dudh1b":t2,"dudh1c":t3}
# n=1
q(1,"Todos os seres humanos nascem livres e iguais em",["dignidade e em direitos.","renda e em cargo.","raça e em cor.","idade e em sexo.","poder e em fortuna."],"Art. 1º.")
q(1,"Dotados de razão e de consciência, os seres humanos devem agir uns para com os outros em espírito de",["fraternidade.","competição.","hierarquia.","obediência.","neutralidade."],"Art. 1º.")
q(1,"Todo o indivíduo tem direito à vida, à liberdade e à segurança",["pessoal.","coletiva.","nacional.","pública.","internacional."],"Art. 3º.")
q(1,"Ninguém será mantido em escravatura ou em",["servidão.","guarda.","tutela.","custódia.","moradia."],"Art. 4º.")
q(1,"Ninguém será submetido a tortura nem a penas ou tratamentos cruéis, desumanos ou",["degradantes.","legais.","rápidos.","disciplinares.","públicos."],"Art. 5º.")
q(1,"Todos os indivíduos têm direito ao reconhecimento da sua personalidade",["jurídica.","fiscal.","política.","religiosa.","comercial."],"Art. 6º.")
q(1,"Todos são iguais perante a",["lei.","polícia.","empresa.","escola.","igreja."],"Art. 7º.")
q(1,"Toda a pessoa tem direito a recurso efetivo para as jurisdições nacionais competentes contra os atos que violem os direitos",["fundamentais reconhecidos pela Constituição ou pela lei.","privados.","comerciais.","tributários.","trabalhistas."],"Art. 8º.")
q(1,"Ninguém pode ser arbitrariamente preso, detido ou",["exilado.","julgado.","fiscalizado.","investigado.","transferido."],"Art. 9º.")
q(1,"A causa de toda pessoa deve ser julgada por tribunal independente e",["imparcial.","militar.","político.","sigiloso.","municipal."],"Art. 10.")
q(1,"Toda pessoa acusada de ato delituoso presume-se",["inocente.","culpada.","suspeita.","condenada.","vigiada."],"Art. 11, 1.")
q(1,"Ninguém sofrerá ataques à sua honra e",["reputação.","fortuna.","moradia.","posição.","idade."],"Art. 12.")
q(1,"Toda a pessoa tem o direito de livremente circular e escolher a sua",["residência no interior de um Estado.","profissão.","religião.","língua.","escola."],"Art. 13, 1.")
q(1,"Toda a pessoa tem o direito de abandonar o país em que se encontra, incluindo o seu, e o direito de",["regressar ao seu país.","mudar de nome.","perder a nacionalidade.","ocupar cargo público.","pedir exílio."],"Art. 13, 2.")
q(1,"Toda a pessoa sujeita a perseguição tem o direito de procurar e de beneficiar de",["asilo em outros países.","anistia.","tutela.","imunidade.","residência fixa."],"Art. 14, 1.")
q(1,"Todo o indivíduo tem direito a ter uma",["nacionalidade.","propriedade.","arma.","profissão.","herança."],"Art. 15, 1.")
q(1,"Toda a pessoa, individual ou coletiva, tem direito à",["propriedade.","herança apenas.","tutela.","anistia.","isenção."],"Art. 17, 1.")
q(1,"Toda a pessoa tem direito à liberdade de pensamento, de consciência e de",["religião.","comércio.","ocupação.","moradia.","herança."],"Art. 18.")
q(1,"Toda a pessoa tem direito à liberdade de reunião e de associação",["pacíficas.","armadas.","secretas.","partidárias apenas.","sindicais apenas."],"Art. 20, 1.")
q(1,"No texto da detenção sem motivo, a detenção do jovem sem motivo legal viola o art. 9º, que veda a prisão ou detenção",["arbitrária.","necessária.","legal.","pública.","cautelar."],"Art. 9º.","dudh1a")
# n=2
q(2,"A Declaração foi adotada e proclamada pela resolução 217 A (III) da Assembleia Geral da ONU, de 10 de dezembro de",["1948.","1964.","1988.","1990.","1945."],"Preâmbulo.")
q(2,"O art. 2º diz que a distinção de direitos não pode ser fundada no estatuto político, jurídico ou internacional do país ou do território da",["naturalidade da pessoa.","residência da pessoa.","profissão da pessoa.","religião da pessoa.","renda da pessoa."],"Art. 2º.")
q(2,"Todos têm direito a proteção igual contra qualquer discriminação que viole a Declaração e contra qualquer incitamento a tal",["discriminação.","punição.","reunião.","associação.","revisão."],"Art. 7º.")
q(2,"Ninguém será condenado por ações ou omissões que, no momento da sua prática, não constituíssem ato delituoso à face do direito interno ou",["internacional.","costumeiro.","privado.","religioso.","militar."],"Art. 11, 2.")
q(2,"Não será infligida pena mais grave do que a que era aplicável no momento em que o ato delituoso foi",["cometido.","julgado.","denunciado.","notificado.","apreciado."],"Art. 11, 2.")
q(2,"O direito de asilo não pode ser invocado no caso de processo realmente existente por crime de direito",["comum.","civil.","tributário.","eleitoral.","trabalhista."],"Art. 14, 2.")
q(2,"Ninguém pode ser arbitrariamente privado da sua nacionalidade nem do direito de mudar de",["nacionalidade.","nome.","religião.","residência.","partido."],"Art. 15, 2.")
q(2,"O casamento não pode ser celebrado sem o livre e pleno consentimento dos futuros",["esposos.","pais.","padrinhos.","juízes.","parentes."],"Art. 16, 2.")
q(2,"A partir da idade núbil, homem e mulher têm direito de casar e constituir família, sem restrição de raça, nacionalidade ou",["religião.","renda.","idade.","profissão.","bairro."],"Art. 16, 1.")
q(2,"Ninguém pode ser arbitrariamente privado da sua",["propriedade.","profissão.","língua.","religião.","opinião."],"Art. 17, 2.")
q(2,"A liberdade de religião implica a liberdade de mudar de religião ou de",["convicção.","nome.","residência.","Estado.","língua."],"Art. 18.")
q(2,"A liberdade de opinião e expressão inclui procurar, receber e difundir informações e ideias sem consideração de",["fronteiras.","partidos.","idades.","rendas.","cargos."],"Art. 19.")
q(2,"Ninguém pode ser obrigado a fazer parte de uma",["associação.","reunião.","escola.","família.","religião."],"Art. 20, 2.")
q(2,"Toda a pessoa tem direito de acesso, em condições de igualdade, às funções",["públicas do seu país.","privadas.","religiosas.","militares apenas.","estrangeiras."],"Art. 21, 2.")
q(2,"A vontade do povo é o fundamento da autoridade dos poderes",["públicos.","privados.","militares.","religiosos.","econômicos."],"Art. 21, 3.")
q(2,"As eleições honestas devem ser realizadas periodicamente por sufrágio universal e igual, com voto",["secreto ou processo equivalente.","aberto.","censitário.","facultativo.","por aclamação."],"Art. 21, 3.")
q(2,"Toda pessoa tem direito, em plena igualdade, a que a sua causa seja equitativa e publicamente julgada, o que se refere ao art.",["10.","9º.","11.","12.","13."],"Art. 10.")
q(2,"No texto da passeata pacífica, o direito dos moradores se funda no art. 20, que garante a liberdade de reunião e de associação",["pacíficas.","armadas.","secretas.","partidárias.","obrigatórias."],"Art. 20, 1.","dudh1b")
q(2,"No texto do pedido de asilo, o estrangeiro perseguido tem o direito de procurar e beneficiar de asilo, previsto no art.",["14.","13.","15.","16.","12."],"Art. 14, 1.","dudh1c")
q(2,"No texto da detenção sem motivo, além do art. 9º, a conduta pode violar o direito à liberdade e à segurança, do art.",["3º.","1º.","7º.","11.","20."],"Art. 3º.","dudh1a")
# n=3
q(3,"Assinale a alternativa correta, nos termos da Declaração.",["Ninguém pode ser arbitrariamente preso, detido ou exilado, e todo acusado presume-se inocente até a prova legal da culpa.","Todo acusado presume-se culpado até prova em contrário.","A prisão arbitrária é admitida em emergência.","A tortura é admitida em casos graves.","O asilo vale em qualquer crime."],"Arts. 5º, 9º e 11.")
q(3,"Considere. I. Ninguém será mantido em escravatura ou servidão. II. O asilo vale para qualquer crime. III. Todos são iguais perante a lei. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O asilo não pode ser invocado em crime de direito comum (art. 14, 2).")
q(3,"Assinale a INCORRETA.",["A Declaração admite a pena mais grave do que a aplicável ao tempo do ato.","A Declaração proíbe a tortura.","A Declaração protege a privacidade e o domicílio.","A Declaração garante a liberdade de reunião pacífica.","A Declaração protege o direito à nacionalidade."],"Não se infligirá pena mais grave do que a aplicável ao tempo do ato (art. 11, 2).")
q(3,"Segundo o art. 12, toda pessoa tem direito a proteção da lei contra intromissões ou",["ataques.","críticas.","reuniões.","visitas.","consultas."],"Art. 12.")
q(3,"O art. 13 trata de dois direitos: circular e escolher residência no interior de um Estado (item 1) e abandonar qualquer país e regressar ao seu (item",["2).","3).","4).","5).","6)."],"Art. 13, 2.")
q(3,"O art. 18 inclui, entre as formas de manifestar a religião ou convicção, o ensino, a prática, o culto e os",["ritos.","costumes.","decretos.","livros.","símbolos."],"Art. 18.")
q(3,"O art. 19 protege o direito de não ser inquietado pelas suas",["opiniões.","dívidas.","origens.","viagens.","amizades."],"Art. 19.")
q(3,"O art. 21 trata do direito de tomar parte na direção dos negócios públicos do seu país, quer diretamente, quer por intermédio de representantes",["livremente escolhidos.","indicados.","nomeados.","hereditários.","militares."],"Art. 21, 1.")
q(3,"A Declaração, no art. 16, prevê que, durante o casamento e na altura da sua dissolução, ambos têm direitos",["iguais.","diversos.","limitados.","reduzidos.","hierarquizados."],"Art. 16, 1.")
q(3,"O art. 8º assegura recurso efetivo contra atos que violem direitos fundamentais reconhecidos pela Constituição ou pela",["lei.","religião.","tradição.","jurisprudência.","moral."],"Art. 8º.")
q(3,"O art. 2º diz que todos podem invocar os direitos, sem distinção alguma, nomeadamente de raça, cor, sexo, língua, religião, opinião política ou outra, origem nacional ou social, fortuna, nascimento ou qualquer outra",["situação.","profissão.","idade.","religião.","cidade."],"Art. 2º.")
q(3,"A presunção de inocência é prevista no art. 11, item",["1.","2.","3.","4.","5."],"Art. 11, 1.")
q(3,"A irretroatividade da lei penal mais grave está no art. 11, item",["2.","1.","3.","4.","5."],"Art. 11, 2.")
q(3,"A proibição de ser obrigado a fazer parte de uma associação está no art. 20, item",["2.","1.","3.","4.","5."],"Art. 20, 2.")
q(3,"No texto da detenção sem motivo, o jovem também tem direito a recurso efetivo, previsto no art. 8º, contra atos que violem os direitos",["fundamentais.","comerciais.","privados.","tributários.","trabalhistas."],"Art. 8º.","dudh1a")
q(3,"No texto da detenção sem motivo, a Declaração impede que o jovem seja arbitrariamente",["preso, detido ou exilado.","fiscalizado.","orientado.","aconselhado.","transferido de turno."],"Art. 9º.","dudh1a")
q(3,"No texto da passeata pacífica, além da reunião, o exercício de opinião e expressão é protegido pelo art.",["19.","20.","18.","21.","17."],"Art. 19.","dudh1b")
q(3,"No texto da passeata pacífica, a participação na direção dos negócios públicos, por meio das reivindicações, relaciona-se ao art.",["21.","16.","17.","12.","14."],"Art. 21.","dudh1b")
q(3,"No texto do pedido de asilo, o asilo não pode ser invocado em caso de processo realmente existente por crime de direito comum ou por atividades contrárias aos fins e princípios das",["Nações Unidas.","Forças Armadas.","empresas.","igrejas.","escolas."],"Art. 14, 2.","dudh1c")
q(3,"No texto do pedido de asilo, o estrangeiro perseguido tem direito de procurar asilo em",["outros países.","apenas no seu país.","apenas na capital.","apenas em embaixadas.","apenas no litoral."],"Art. 14, 1.","dudh1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("DUDH: Preâmbulo e arts. 1º a 21",[
 ("ig","Igualdade e dignidade",["arts. 1º e 2º","sem distinção alguma"],"seção 1"),
 ("vid","Vida e integridade",["art. 3º","sem escravidão","sem tortura"],"seção 1"),
 ("pri","Prisão e julgamento",["sem prisão arbitrária","julgamento equitativo","presunção de inocência"],"seção 2"),
 ("pv","Privacidade e circulação",["art. 12","art. 13","asilo e nacionalidade"],"seção 2"),
 ("fam","Família e propriedade",["art. 16","art. 17"],"seção 3"),
 ("liv","Liberdades e participação",["pensamento, expressão","reunião e associação","voto secreto"],"seção 3")],
 "Na prova: palavras exatas de cada artigo")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a igualdade, a vida e a integridade; as demais, a prisão e o julgamento, a privacidade, a família e as liberdades.","Fontes: Edital 02/2026, Anexo I; Declaração Universal dos Direitos Humanos (ONU, 1948), tradução do Centro de Informação das Nações Unidas, texto da Wikisource. Exemplos criados para a aula.")
revisao("dudh-1","DUDH: Preâmbulo e arts. 1º a 21",Q,list(tx),
 cobertura=["Preâmbulo (partes) e arts. 1º a 21."],
 pendencias=["Texto-fonte: tradução da Wikisource, que usa a grafia de Portugal; reconferir na versão oficial em português do Brasil e ajustar a grafia e a redação (por exemplo, 'tratamentos cruéis, desumanos ou degradantes').","Em algumas questões, a pergunta e a alternativa seguem a redação portuguesa literal.","Trechos copiados de fontes/dudh.txt por programa.","Casos dudh1a, dudh1b e dudh1c fictícios."],
 fontes_conferidas=["DUDH, Preâmbulo e arts. 1º a 21: tradução da Wikisource, copiada por programa."])
gravar("dudh-1",aula_html,banco("dudh-1",Q),tx)
