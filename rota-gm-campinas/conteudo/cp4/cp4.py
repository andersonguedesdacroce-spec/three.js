import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='cp.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os crimes contra a honra são três, e a prova pede sempre que se distinga um do outro: a calúnia atribui falsamente um crime, a difamação atribui um fato ofensivo à reputação e a injúria ofende a dignidade ou o decoro. A Vunesp cobra os arts. 138 a 145 pela definição de cada crime, pela exceção da verdade, pelas causas de aumento, pela retratação e pela ação penal, que é de regra privada. Na rotina do guarda, o assunto aparece nas ofensas em via pública e nas redes sociais."
S={}
S[1]="## 1. Calúnia\n\n"+L("art. 138, caput e §§ 1º e 2º","Art. 138. Caluniar alguém","Exceção da verdade")+"\n\n"+L("art. 138, § 3º","§ 3º Admite-se a prova da verdade, salvo:","Difamação")+"""

Na calúnia, o agente imputa falsamente a alguém fato definido como crime. Duas palavras decidem: “falsamente” (a imputação é mentira, e o autor sabe) e “fato definido como crime” (não basta chamar de ladrão: é preciso dizer que a pessoa praticou um furto determinado). A pena é de detenção de seis meses a dois anos e multa. Responde igualmente quem, sabendo falsa a imputação, a propala ou a divulga, e a calúnia contra os mortos é punível, porque a lei protege a memória do falecido.

A exceção da verdade permite ao acusado provar que a imputação é verdadeira, o que afasta o crime. Mas há três limites: se o fato imputado é crime de ação privada e o ofendido não foi condenado por sentença irrecorrível, se o fato é imputado ao Presidente da República ou a chefe de governo estrangeiro, e se, apesar de o crime ser de ação pública, o ofendido foi absolvido por sentença irrecorrível.
"""
S[2]="## 2. Difamação e injúria\n\n"+L("art. 139","Art. 139. Difamar alguém","Injúria")+"\n\n"+L("art. 140, caput e §§ 1º e 2º","Art. 140. Injuriar alguém","§ 3º Se a injúria")+"\n\n"+L("art. 140, § 3º","§ 3º Se a injúria consiste","Disposições comuns")+"""

Na difamação, o agente imputa fato ofensivo à reputação, que pode ser verdadeiro, e a pena é de detenção de três meses a um ano e multa. A exceção da verdade só se admite quando o ofendido é funcionário público e a ofensa é relativa ao exercício de suas funções, porque o interesse público em saber se o servidor trabalha bem prevalece sobre a reputação dele.

Na injúria, o agente ofende a dignidade ou o decoro, sem imputar fato: é o xingamento. A pena é de detenção de um a seis meses ou multa. O juiz pode deixar de aplicar a pena se o ofendido provocou diretamente a injúria de forma reprovável ou no caso de retorsão imediata. Se a injúria consiste em violência ou vias de fato aviltantes, a pena é de detenção de três meses a um ano e multa, além da pena da violência. E, se consiste na utilização de elementos referentes a religião ou à condição de pessoa idosa ou com deficiência, é a injúria preconceituosa, com reclusão de um a três anos e multa.

[[NOTA: A calúnia atinge a honra objetiva e exige fato definido como crime; a difamação também atinge a honra objetiva e exige fato ofensivo; a injúria atinge a honra subjetiva (o que a pessoa pensa de si). A prova costuma dar a frase e pedir o nome do crime.]]
"""
S[3]="## 3. Causas de aumento e exclusão do crime\n\n"+L("art. 141, caput e incisos","Art. 141. As penas cominadas","§ 1º Se o crime é cometido mediante paga")+"\n\n"+L("art. 141, § 1º","§ 1º Se o crime é cometido mediante paga","§ 2º Se o crime é cometido ou divulgado")+" "+L("art. 141, § 3º","§ 3º Se o crime é cometido contra a mulher","Exclusão do crime")+"""

As penas dos crimes contra a honra aumentam de um terço se o crime é cometido contra o Presidente da República ou chefe de governo estrangeiro, contra funcionário público em razão de suas funções (ou contra os Presidentes do Senado, da Câmara e do STF), na presença de várias pessoas ou por meio que facilite a divulgação, ou contra criança, adolescente, maior de 60 anos ou pessoa com deficiência, exceto na injúria preconceituosa. A pena é aplicada em dobro se o crime é cometido mediante paga ou promessa de recompensa e também se é cometido contra a mulher por razões da condição do sexo feminino.

[[NOTA: O § 2º do art. 141, que triplicava a pena quando o crime fosse cometido ou divulgado nas redes sociais, aparece na compilação com a marca de vetado: não está em vigor.]]

"""+L("art. 142","Art. 142. Não constituem injúria ou difamação punível:","Retratação")+"""

Não são puníveis a ofensa irrogada em juízo na discussão da causa, a opinião desfavorável da crítica literária, artística ou científica e o conceito desfavorável de funcionário público no cumprimento do dever de ofício. A imunidade vale só para a injúria e a difamação: a calúnia não está nesse artigo. E, nos casos de ofensa em juízo e de funcionário público, responde quem dá publicidade.
"""
S[4]="## 4. Retratação e ação penal\n\n"+L("art. 143","Art. 143. O querelado que","Art. 144.")+"\n\n"+L("art. 144","Art. 144. Se, de referências","Art. 145.")+"\n\n"+L("art. 145","Art. 145. Nos crimes previstos neste capítulo","CAPÍTULO VI")+"""

A retratação cabal, antes da sentença, isenta de pena o querelado, mas só vale para a calúnia e a difamação: na injúria, a lei não prevê. O art. 144 cuida do pedido de explicações em juízo, quando a ofensa vem por alusões, e quem se recusa a explicar, ou explica de modo insatisfatório, responde pela ofensa.

Nos crimes contra a honra, a regra é a ação penal privada, que depende de queixa do ofendido. As exceções estão no art. 145: procede-se por ação pública condicionada à requisição do Ministro da Justiça quando o crime é contra o Presidente da República ou chefe de governo estrangeiro, por ação pública condicionada à representação do ofendido quando é contra funcionário público em razão de suas funções e na injúria preconceituosa do § 3º do art. 140, e por ação pública quando a injúria consiste em violência da qual resulta lesão corporal.
"""
S[6]="""## 6. Na rotina do guarda

- **Ofensa em via pública:** o xingamento é injúria, de regra de ação privada; o guarda orienta a vítima a registrar e a procurar a queixa, e lavra o termo quando o caso permite.
- **Ofensa contra o próprio guarda:** é o caso do art. 141, II, aumento de um terço, e a ação depende de representação do ofendido (art. 145, parágrafo único).
- **Redes sociais:** a ofensa pública na internet atrai o aumento do art. 141, III, por facilitar a divulgação.
- **Injúria preconceituosa:** a injúria com elementos de religião ou da condição de idoso ou de pessoa com deficiência tem reclusão de um a três anos, com ação pública condicionada a representação.
"""
S[7]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Calúnia: imputar fato ofensivo | Calúnia é imputar falsamente fato definido como crime |
| Difamação: imputar crime | Difamação imputa fato ofensivo à reputação, não crime |
| Injúria: imputar fato | Injúria ofende a dignidade ou o decoro, sem fato |
| Pena da calúnia | Detenção de seis meses a dois anos e multa |
| Pena da injúria | Detenção de um a seis meses ou multa |
| Retratação da injúria | A retratação isenta só a calúnia e a difamação |
| Ação penal | Regra: queixa. Exceções: requisição do Ministro; representação |
| Exceção da verdade na difamação | Só se o ofendido é funcionário público e a ofensa se relaciona ao cargo |
"""
S[8]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Calúnia | Imputar falsamente fato definido como crime: detenção, 6 meses a 2 anos, e multa |
| Difamação | Imputar fato ofensivo à reputação: detenção, 3 meses a 1 ano, e multa |
| Injúria | Ofender dignidade ou decoro: detenção, 1 a 6 meses, ou multa |
| Injúria preconceituosa | Reclusão, 1 a 3 anos, e multa |
| Aumento | 1/3 (Presidente, funcionário, várias pessoas, criança, idoso, deficiente) |
| Dobro | Mediante paga; contra a mulher por razões do sexo feminino |
| Retratação | Isenta de pena na calúnia e na difamação |
| Ação penal | Queixa; requisição do Ministro da Justiça; representação |
"""
QR=[("Questão 1","Imputar falsamente a alguém fato definido como crime é",["calúnia.","difamação.","injúria.","denunciação caluniosa.","falso testemunho."],0,"Art. 138."),
("Questão 2","Imputar a alguém fato ofensivo à sua reputação é",["difamação.","calúnia.","injúria.","injúria real.","constrangimento ilegal."],2,"Art. 139."),
("Questão 3","Ofender a dignidade ou o decoro de alguém, sem imputar fato, é",["injúria.","calúnia.","difamação.","ameaça.","rixa."],4,"Art. 140."),
("Questão 4","Nos crimes contra a honra, a retratação cabal antes da sentença isenta de pena",["o querelado que calunia ou difama.","o querelado que injuria.","qualquer dos três crimes.","somente o que injuria.","nenhum dos três crimes."],1,"Art. 143.")]
t1="<strong>Xingamento em frente à escola</strong><br><br>Em Vila Nova, cidade fictícia, um motorista discutiu com um guarda municipal que o abordou por estacionar em local proibido e o xingou de “incompetente” e “vagabundo”, em voz alta, diante de várias pessoas. O guarda estava no exercício da função."
t2="<strong>Mensagem falsa sobre um vizinho</strong><br><br>Um morador espalhou entre os vizinhos, sabendo ser falso, que outro morador havia furtado o relógio de um comerciante. O ofendido soube e quis responsabilizar o autor. Na delegacia, o autor disse que poderia provar que o fato era verdade, mas não apresentou prova."
tx={"cp4a":t1,"cp4b":t2}
# n=1
q(1,"Imputar falsamente a alguém fato definido como crime configura",["calúnia.","difamação.","injúria.","ameaça.","constrangimento ilegal."],"Art. 138.")
q(1,"A pena da calúnia é de",["detenção, de seis meses a dois anos, e multa.","detenção, de três meses a um ano, e multa.","detenção, de um a seis meses, ou multa.","reclusão, de um a três anos, e multa.","reclusão, de seis meses a dois anos."],"Art. 138, caput.")
q(1,"Imputar a alguém fato ofensivo à sua reputação configura",["difamação.","calúnia.","injúria.","ameaça.","perigo de contágio."],"Art. 139.")
q(1,"A pena da difamação é de",["detenção, de três meses a um ano, e multa.","detenção, de seis meses a dois anos, e multa.","detenção, de um a seis meses, ou multa.","reclusão, de um a três anos.","multa, apenas."],"Art. 139, caput.")
q(1,"Ofender a dignidade ou o decoro de alguém configura",["injúria.","calúnia.","difamação.","lesão corporal.","rixa."],"Art. 140, caput.")
q(1,"A pena da injúria simples é de",["detenção, de um a seis meses, ou multa.","detenção, de três meses a um ano, e multa.","detenção, de seis meses a dois anos, e multa.","reclusão, de um a três anos.","multa, apenas."],"Art. 140, caput.")
q(1,"Na calúnia, o fato imputado é",["definido como crime.","ofensivo à reputação, mas não crime.","apenas um xingamento.","uma contravenção.","verdadeiro."],"Art. 138.")
q(1,"É punível a calúnia contra",["os mortos.","somente os vivos.","somente funcionários públicos.","somente pessoas jurídicas.","ninguém, depois da morte."],"Art. 138, § 2º.")
q(1,"Na calúnia, também responde quem, sabendo falsa a imputação,",["a propala ou divulga.","a ignora.","a nega.","a corrige.","a desmente."],"Art. 138, § 1º.")
q(1,"Na difamação, a exceção da verdade somente se admite se o ofendido é",["funcionário público e a ofensa é relativa ao exercício de suas funções.","qualquer pessoa.","menor de idade.","pessoa jurídica.","o Presidente da República."],"Art. 139, parágrafo único.")
q(1,"A injúria consistente em violência ou vias de fato aviltantes tem pena de",["detenção, de três meses a um ano, e multa, além da pena da violência.","detenção, de um a seis meses.","reclusão, de um a três anos.","multa.","detenção, de seis meses a dois anos."],"Art. 140, § 2º.")
q(1,"A injúria com elementos referentes a religião, ou à condição de pessoa idosa ou com deficiência, tem pena de",["reclusão, de um a três anos, e multa.","detenção, de um a seis meses.","detenção, de três meses a um ano.","multa.","reclusão, de dois a cinco anos."],"Art. 140, § 3º.")
q(1,"As penas dos crimes contra a honra aumentam de um terço se o crime é cometido contra",["o Presidente da República.","qualquer pessoa.","um parente.","um vizinho.","um estudante."],"Art. 141, I.")
q(1,"As penas dos crimes contra a honra aumentam de um terço se o crime é cometido",["na presença de várias pessoas, ou por meio que facilite a divulgação.","de dia.","por reincidente.","por funcionário público.","em ambiente fechado."],"Art. 141, III.")
q(1,"Se o crime contra a honra é cometido mediante paga ou promessa de recompensa, a pena é aplicada",["em dobro.","em triplo.","com aumento de um terço.","com aumento da metade.","com aumento de um sexto."],"Art. 141, § 1º.")
q(1,"Não constitui injúria ou difamação punível",["a ofensa irrogada em juízo, na discussão da causa, pela parte ou por seu procurador.","qualquer ofensa em público.","qualquer ofensa a funcionário público.","toda crítica a político.","qualquer xingamento."],"Art. 142, I.")
q(1,"O querelado que, antes da sentença, se retrata cabalmente da calúnia ou da difamação",["fica isento de pena.","tem a pena reduzida.","tem a pena aumentada.","é absolvido da injúria.","responde por falso testemunho."],"Art. 143.")
q(1,"Nos crimes contra a honra, procede-se, em regra, mediante",["queixa.","denúncia do Ministério Público, de ofício.","requisição do juiz.","auto de prisão em flagrante.","portaria do delegado."],"Art. 145, caput.")
q(1,"No texto do xingamento, as palavras “incompetente” e “vagabundo” configuram, em tese,",["injúria.","calúnia.","difamação.","ameaça.","desacato apenas."],"Ofensas à dignidade ou ao decoro, sem fato: art. 140.","cp4a")
q(1,"No texto da mensagem falsa, o morador que espalhou que o outro havia furtado o relógio cometeu, em tese,",["calúnia.","injúria.","difamação.","ameaça.","furto."],"Imputou falsamente fato definido como crime: art. 138.","cp4b")
# n=2
q(2,"Na calúnia, admite-se a prova da verdade, salvo se o fato imputado é",["crime de ação privada e o ofendido não foi condenado por sentença irrecorrível.","qualquer crime.","contravenção.","crime de ação pública.","crime culposo."],"Art. 138, § 3º, I.")
q(2,"Na calúnia, a prova da verdade não se admite se o fato é imputado",["ao Presidente da República ou a chefe de governo estrangeiro.","a qualquer cidadão.","a um servidor público municipal.","a um desconhecido.","a um menor."],"Art. 138, § 3º, II, com remissão ao art. 141, I.")
q(2,"Na calúnia, a prova da verdade não se admite se, embora o crime seja de ação pública, o ofendido",["foi absolvido por sentença irrecorrível.","foi condenado por sentença irrecorrível.","está foragido.","foi preso em flagrante.","é reincidente."],"Art. 138, § 3º, III.")
q(2,"O juiz pode deixar de aplicar a pena na injúria quando",["o ofendido, de forma reprovável, provocou diretamente a injúria.","a vítima é idosa.","o autor é reincidente.","há várias testemunhas.","a injúria é pública."],"Art. 140, § 1º, I.")
q(2,"O juiz pode deixar de aplicar a pena na injúria",["no caso de retorsão imediata que consista em outra injúria.","quando a vítima é funcionário público.","quando há paga.","quando é praticada na internet.","quando é preconceituosa."],"Art. 140, § 1º, II.")
q(2,"A pena dos crimes contra a honra aumenta de um terço se o crime é cometido contra funcionário público",["em razão de suas funções.","fora do serviço.","em qualquer circunstância.","apenas se for federal.","apenas se for policial."],"Art. 141, II.")
q(2,"A pena dos crimes contra a honra aumenta de um terço se o crime é cometido contra",["criança, adolescente, pessoa maior de 60 anos ou pessoa com deficiência, exceto na hipótese do § 3º do art. 140.","qualquer adulto.","apenas pessoa com deficiência.","apenas idoso.","apenas criança."],"Art. 141, IV.")
q(2,"A pena dos crimes contra a honra é aplicada em dobro se o crime é cometido contra",["a mulher, por razões da condição do sexo feminino.","qualquer idoso.","qualquer funcionário.","qualquer criança.","pessoa com deficiência."],"Art. 141, § 3º.")
q(2,"O § 2º do art. 141, que previa triplicar a pena quando o crime é divulgado em redes sociais,",["aparece no texto consolidado como vetado e não está em vigor.","está em vigor.","foi revogado em 2020.","foi declarado inconstitucional.","foi incorporado ao art. 140."],"A consolidação marca o dispositivo como vetado.")
q(2,"Não constitui injúria ou difamação punível a opinião desfavorável da crítica literária, artística ou científica, salvo quando",["inequívoca a intenção de injuriar ou difamar.","for em público.","for assinada.","for impressa.","for contra mulher."],"Art. 142, II.")
q(2,"Não constitui injúria ou difamação punível o conceito desfavorável emitido por funcionário público",["em apreciação ou informação que preste no cumprimento de dever do ofício.","em qualquer ocasião.","em ambiente privado.","a título pessoal.","em redes sociais."],"Art. 142, III.")
q(2,"Nos casos de ofensa em juízo e de conceito de funcionário público, responde pela injúria ou difamação",["quem dá publicidade.","o juiz.","o advogado.","o funcionário.","ninguém."],"Art. 142, parágrafo único.")
q(2,"Quando o querelado praticou a calúnia ou a difamação por meios de comunicação, a retratação dar-se-á, se o ofendido desejar,",["pelos mesmos meios em que se praticou a ofensa.","por carta.","por e-mail.","em juízo.","em cartório."],"Art. 143, parágrafo único.")
q(2,"Se, de referências, alusões ou frases, se infere calúnia, difamação ou injúria, quem se julga ofendido pode",["pedir explicações em juízo.","exigir prisão do ofensor.","exigir indenização imediata.","registrar boletim, apenas.","pedir retratação extrajudicial, apenas."],"Art. 144.")
q(2,"Nos crimes contra a honra, procede-se mediante queixa, salvo quando, na injúria real do art. 140, § 2º,",["da violência resulta lesão corporal.","a vítima é idosa.","há paga.","há várias pessoas.","há reincidência."],"Art. 145, caput.")
q(2,"A ação penal, no crime contra a honra do Presidente da República, depende de",["requisição do Ministro da Justiça.","queixa do ofendido.","representação do ofendido.","denúncia sem condição.","requisição do juiz."],"Art. 145, parágrafo único.")
q(2,"A ação penal, no crime contra a honra de funcionário público em razão de suas funções, depende de",["representação do ofendido.","queixa do ofendido.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 145, parágrafo único.")
q(2,"No texto do xingamento, o aumento de um terço do art. 141 incide, em tese, porque a ofensa foi dirigida a funcionário público em razão de suas funções e",["praticada na presença de várias pessoas.","praticada de dia.","feita em voz baixa.","praticada em ambiente fechado.","praticada sem testemunhas."],"Art. 141, II e III.","cp4a")
q(2,"No texto do xingamento, a ação penal, por se tratar de ofensa a funcionário público em razão da função, depende de",["representação do ofendido.","queixa-crime apenas.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 145, parágrafo único.","cp4a")
q(2,"No texto da mensagem falsa, o fato de o autor dizer que poderia provar a verdade da imputação",["permite a exceção da verdade, que, se provada, afasta o crime de calúnia.","afasta o crime automaticamente.","agrava a pena.","configura injúria.","dispensa a prova."],"Art. 138, § 3º: admite-se a prova da verdade; sem prova, o crime subsiste.","cp4b")
# n=3
q(3,"Assinale a alternativa que associa corretamente o crime à sua definição.",["Calúnia: imputar falsamente fato definido como crime; difamação: imputar fato ofensivo à reputação; injúria: ofender dignidade ou decoro.","Calúnia: ofender dignidade; difamação: imputar crime; injúria: imputar fato.","Calúnia: imputar fato ofensivo; difamação: ofender dignidade; injúria: imputar crime.","Calúnia, difamação e injúria: imputar crime.","Calúnia: imputar crime verdadeiro."],"Arts. 138 a 140.")
q(3,"Considere as afirmações. I. A retratação cabal isenta de pena na calúnia e na difamação. II. A retratação cabal isenta de pena na injúria. III. A retratação deve ocorrer antes da sentença. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II e III, apenas.","I e II, apenas.","I, II e III."],"Art. 143: só calúnia e difamação.")
q(3,"Assinale a INCORRETA.",["A calúnia contra os mortos não é punível.","A difamação admite exceção da verdade, em regra, apenas se o ofendido é funcionário público.","A injúria preconceituosa tem pena de reclusão de um a três anos, e multa.","As penas aumentam de um terço se o crime é contra o Presidente da República.","Nos crimes contra a honra, procede-se, em regra, mediante queixa."],"A calúnia contra os mortos é punível (art. 138, § 2º).")
q(3,"Assinale a INCORRETA sobre o art. 142 do Código Penal.",["Aplica-se à calúnia.","Aplica-se à injúria e à difamação.","Protege a ofensa irrogada em juízo na discussão da causa.","Protege a opinião desfavorável da crítica literária, artística ou científica.","Protege o conceito desfavorável emitido por funcionário público no cumprimento do dever do ofício."],"Art. 142: só injúria e difamação.")
q(3,"Se, na injúria, o ofendido provocou diretamente o ofensor de forma reprovável, o juiz",["pode deixar de aplicar a pena.","deve aumentar a pena.","deve aplicar pena em dobro.","deve absolver.","deve converter em reclusão."],"Art. 140, § 1º, I.")
q(3,"A injúria real, em que a injúria consiste em violência ou vias de fato aviltantes, tem pena de detenção de três meses a um ano e multa",["além da pena correspondente à violência.","em lugar da pena da violência.","sem prejuízo da pena de multa maior.","apenas se houver lesão grave.","apenas se houver reincidência."],"Art. 140, § 2º.")
q(3,"A ação penal na injúria preconceituosa do § 3º do art. 140 depende de",["representação do ofendido.","queixa.","requisição do Ministro da Justiça.","denúncia incondicionada.","requisição do juiz."],"Art. 145, parágrafo único, parte final.")
q(3,"A injúria consistente em violência da qual resulta lesão corporal, segundo o art. 145, caput, procede-se",["por ação pública, sem queixa.","somente mediante queixa.","somente mediante requisição do Ministro da Justiça.","somente por representação.","somente por requisição do juiz."],"Art. 145, caput, exceção.")
q(3,"A exceção da verdade, na difamação, existe porque, quando o ofendido é funcionário público,",["há interesse público em apurar se a ofensa relativa ao exercício das funções é verdadeira.","a reputação do servidor não merece proteção.","o servidor é sempre culpado.","a lei protege o ofensor.","a verdade é irrelevante."],"Art. 139, parágrafo único.")
q(3,"No art. 141, a circunstância “na presença de várias pessoas, ou por meio que facilite a divulgação da calúnia, da difamação ou da injúria” aumenta a pena de",["um terço.","metade.","dois terços.","um sexto.","o dobro."],"Art. 141, III.")
q(3,"O aumento do art. 141, IV (criança, adolescente, maior de 60 anos ou pessoa com deficiência) NÃO se aplica",["à injúria preconceituosa do § 3º do art. 140.","à calúnia.","à difamação.","à injúria simples.","à injúria real."],"Art. 141, IV.")
q(3,"Sobre a ação penal nos crimes contra a honra, assinale a alternativa correta.",["Regra: queixa; exceções: requisição do Ministro da Justiça, representação do ofendido e injúria real com lesão corporal.","Regra: denúncia sem condição; exceção: queixa.","Regra: requisição do Ministro da Justiça.","Sempre representação.","Sempre ação pública incondicionada."],"Art. 145.")
q(3,"A calúnia exige, como elemento do tipo, imputar falsamente fato",["definido como crime.","definido como contravenção.","ofensivo à reputação.","vexatório.","imoral."],"Art. 138, caput.")
q(3,"A diferença essencial entre difamação e calúnia está em que, na difamação, o fato imputado",["é ofensivo à reputação, não precisa ser crime e pode até ser verdadeiro.","é sempre falso e é crime.","é uma ordem.","é uma ameaça.","é um xingamento."],"Arts. 138 e 139.")
q(3,"A retratação, nos crimes contra a honra, é cabível",["antes da sentença, na calúnia e na difamação.","depois do trânsito em julgado.","na injúria.","em qualquer fase.","nunca."],"Art. 143.")
q(3,"O pedido de explicações em juízo (art. 144) é cabível quando",["de referências, alusões ou frases se infere calúnia, difamação ou injúria.","há ofensa direta.","há ameaça.","há lesão corporal.","há furto."],"Art. 144.")
q(3,"O § 3º do art. 141, aplicável aos crimes contra a honra, aplica a pena em dobro se o crime é cometido",["contra a mulher por razões da condição do sexo feminino.","contra idoso.","na internet.","contra funcionário público.","contra criança."],"Art. 141, § 3º.")
q(3,"A pena de reclusão de um a três anos, e multa, é prevista para",["a injúria que consiste na utilização de elementos referentes a religião ou à condição de pessoa idosa ou com deficiência.","a calúnia simples.","a difamação simples.","a injúria simples.","a injúria real."],"Art. 140, § 3º.")
q(3,"No texto do xingamento, a ofensa foi dirigida ao guarda no exercício da função, o que, segundo o art. 141, II,",["aumenta as penas em um terço.","diminui as penas.","dobra as penas.","extingue a punibilidade.","muda o crime para calúnia."],"Art. 141, II.","cp4a")
q(3,"No texto da mensagem falsa, se o autor se retratar cabalmente antes da sentença, ele",["fica isento de pena, por ser calúnia.","responde, pois a retratação não se aplica à calúnia.","tem a pena aumentada.","responde por injúria.","responde por difamação."],"Art. 143.","cp4b")
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes contra a honra",[
 ("cal","Calúnia",["falsamente fato definido como crime","6 meses a 2 anos, e multa","punível contra os mortos"],"seção 1"),
 ("dif","Difamação",["fato ofensivo à reputação","3 meses a 1 ano, e multa","verdade só se servidor"],"seção 2"),
 ("inj","Injúria",["ofende dignidade ou decoro","1 a 6 meses, ou multa","preconceituosa: 1 a 3 anos"],"seção 2"),
 ("aum","Aumentos",["1/3: Presidente, funcionário, vários","em dobro: paga; mulher","§ 2º vetado"],"seção 3"),
 ("exc","Exclusão",["ofensa em juízo","crítica literária e científica","dever de ofício"],"seção 3"),
 ("acao","Retratação e ação penal",["retratação: calúnia e difamação","regra: queixa","exceções: requisição e representação"],"seção 4")],
 "Na prova: leia o que foi imputado (crime, fato ou nada) para nomear o crime")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',6,7,8],QR,5,svg,"As três primeiras caixas diferenciam os crimes; as demais cuidam do que aumenta a pena, do que exclui o crime e da ação penal.","Fontes: Edital 02/2026, Anexo I; Decreto-Lei 2.848/1940 (Código Penal), arts. 138 a 145, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("cp-4","Crimes contra a honra (CP, arts. 138 a 145)",Q,list(tx),
 cobertura=["Recorte do edital: arts. 138 a 145. Cobertos todos, incluindo o art. 141 (com o § 2º vetado) e as regras de ação penal do art. 145."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O § 2º do art. 141 aparece vetado na consolidação; confirmar no Planalto.","Trechos de lei copiados de fontes/cp.txt por programa.","Casos cp4a e cp4b fictícios."],
 fontes_conferidas=["CP, arts. 138 a 145: texto da Câmara, copiado por programa."])
gravar("cp-4",aula_html,banco("cp-4",Q),tx)
