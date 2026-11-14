import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='eca.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A prevenção é o capítulo do ECA mais próximo da rua. Os arts. 70 a 82 dizem quem deve prevenir, o que a criança pode ver e frequentar e o que é proibido vender ou oferecer. O guarda municipal aparece no texto: o art. 70-A, XI, manda capacitar a Guarda Municipal para identificar violência contra crianças. A Vunesp cobra principalmente os arts. 75 (menores de dez anos), 80 (bilhar e jogos), 81 (produtos proibidos) e 82 (hospedagem)."
S={}
S[1]="## 1. Prevenção geral\n\n"+L("art. 70","Art. 70. É dever de todos","Art. 70-A.")+"\n\n"+L("art. 70-A, caput e inciso I","Art. 70-A. A União, os Estados","II - a integração")+"\n\n"+L("art. 70-A, XI","XI - a capacitação permanente","XII - a promoção")+"\n\n"+L("art. 70-B","Art. 70-B. As entidades, públicas e privadas","Art. 71.")+"\n\n"+L("arts. 71 a 73","Art. 71. A criança e o adolescente têm direito","CAPÍTULO II")+"""

É dever de todos prevenir a ocorrência de ameaça ou violação dos direitos da criança e do adolescente. A União, os Estados, o Distrito Federal e os Municípios atuam de forma articulada para coibir o castigo físico e o tratamento cruel e difundir formas não violentas de educação. Entre as ações está a capacitação permanente das Polícias Civil e Militar, da Guarda Municipal, do Corpo de Bombeiros, dos profissionais das escolas e dos Conselhos Tutelares para identificar situações de violência contra crianças e adolescentes no âmbito familiar ou institucional.

Entidades de saúde e educação devem ter pessoas capacitadas a reconhecer e comunicar ao Conselho Tutelar suspeitas ou casos de crimes contra a criança. A comunicação é dever também de quem cuida, assiste ou guarda crianças por cargo, função, ofício, ministério, profissão ou ocupação, e o retardamento ou omissão injustificados são puníveis. A criança tem direito a informação, cultura, lazer, esportes, diversões, espetáculos e produtos e serviços que respeitem sua condição peculiar. A inobservância das normas de prevenção gera responsabilidade da pessoa física ou jurídica.
"""
S[2]="## 2. Diversões, espetáculos, publicações e jogos\n\n"+L("arts. 74 e 75","Art. 74. O Poder Público","Art. 76.")+"\n\n"+L("art. 76","Art. 76. As emissoras de rádio","Art. 77.")+"\n\n"+L("arts. 78 e 79","Art. 78. As revistas e publicações contendo","Art. 80.")+"\n\n"+L("art. 80","Art. 80. Os responsáveis por estabelecimentos","Seção II")+"""

O Poder Público regula as diversões e espetáculos públicos, informando a natureza, as faixas etárias a que não se recomendam e os locais e horários inadequados; os responsáveis afixam na entrada informação destacada sobre a natureza e a faixa etária do certificado de classificação. Toda criança ou adolescente tem acesso aos espetáculos adequados à sua faixa etária, e crianças menores de dez anos só entram e permanecem acompanhadas dos pais ou responsável.

Emissoras de rádio e televisão exibem, no horário recomendado ao público infanto-juvenil, apenas programas educativos, artísticos, culturais e informativos. Revistas impróprias são vendidas em embalagem lacrada, com advertência; publicações infanto-juvenis não podem trazer anúncios de bebidas alcoólicas, tabaco, armas e munições. Os responsáveis por estabelecimentos de bilhar, sinuca ou congênere e por casas de jogos, que realizem apostas ainda que eventualmente, não permitem a entrada e a permanência de crianças e adolescentes e afixam aviso.
"""
S[3]="## 3. Produtos e serviços proibidos\n\n"+L("art. 81","Art. 81. É proibida a venda","Art. 82.")+"\n\n"+L("art. 82","Art. 82. É proibida a hospedagem","Seção III")+"""

É proibida a venda à criança ou ao adolescente de: armas, munições e explosivos; bebidas alcoólicas; produtos cujos componentes possam causar dependência física ou psíquica, ainda que por utilização indevida; fogos de estampido e de artifício, exceto os de reduzido potencial, incapazes de provocar dano; revistas e publicações impróprias do art. 78; e bilhetes lotéricos e equivalentes. É proibida a hospedagem de criança ou adolescente em hotel, motel, pensão ou estabelecimento congênere, salvo se autorizado ou acompanhado pelos pais ou responsável.
"""
S[5]="""## 5. Na rotina do guarda

- **Venda de bebida alcoólica a adolescente:** a venda é proibida; o guarda registra o fato e comunica o Conselho Tutelar.
- **Bar com sinuca ou casa de jogos:** não pode permitir entrada nem permanência de crianças e adolescentes, e o aviso deve estar afixado.
- **Criança menor de dez anos em espetáculo:** só entra e permanece com os pais ou responsável.
- **Hotel ou motel:** a hospedagem de criança sem autorização ou acompanhamento dos pais é proibida.
- **Violência identificada:** a Guarda Municipal é capacitada para identificar violência contra crianças e comunica a rede de proteção.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Idade para entrar em espetáculo sozinho | Menores de dez anos só com os pais ou responsável |
| Bilhar, sinuca, casas de jogos | Proibida a entrada e a permanência; aviso afixado |
| Produtos proibidos (art. 81) | Armas, bebidas, produtos que causem dependência, fogos, revistas impróprias, bilhetes lotéricos |
| Fogos | Exceto os de reduzido potencial, incapazes de causar dano |
| Hospedagem | Proibida, salvo autorização ou acompanhamento dos pais |
| Quem capacita a Guarda Municipal | Art. 70-A, XI |
| Quem comunica suspeitas ao Conselho Tutelar | Entidades de saúde e educação e quem cuida da criança |
| Publicações infanto-juvenis | Sem anúncio de bebida, tabaco, armas e munições |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 70 | Dever de todos prevenir |
| Art. 70-A | Entes articulados; capacitar a Guarda Municipal |
| Art. 70-B | Comunicar suspeitas ao Conselho Tutelar |
| Art. 74 | Poder Público regula diversões; classificação na entrada |
| Art. 75 | Menores de dez anos: só acompanhados |
| Art. 76 | Rádio e TV: programas educativos no horário infantil |
| Art. 80 | Bilhar e jogos: sem crianças |
| Art. 81 | Seis proibições de venda |
| Art. 82 | Hospedagem só com autorização ou pais |
"""
QR=[("Questão 1","As crianças menores de dez anos somente poderão ingressar e permanecer nos locais de apresentação ou exibição quando acompanhadas dos",["pais ou responsável.","irmãos maiores.","professores.","amigos.","vizinhos."],0,"Art. 75, parágrafo único."),
("Questão 2","É proibida a venda à criança ou ao adolescente de armas, munições e",["explosivos.","brinquedos.","livros.","alimentos.","roupas."],1,"Art. 81, I."),
("Questão 3","A hospedagem de criança ou adolescente em hotel, motel ou pensão é proibida, salvo se autorizado ou acompanhado pelos",["pais ou responsável.","amigos.","irmãos menores.","professores.","vizinhos."],2,"Art. 82."),
("Questão 4","Os responsáveis por estabelecimentos de bilhar, sinuca ou casas de jogos cuidarão para que não seja permitida a entrada e a permanência de",["crianças e adolescentes, afixando aviso.","adultos.","idosos.","turistas.","funcionários."],3,"Art. 80.")]
t1="<strong>Bar com sinuca</strong><br><br>Numa ronda, uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, encontrou dois adolescentes de quinze anos jogando sinuca num bar, sem aviso na porta, e um deles bebendo cerveja vendida pelo dono."
t2="<strong>Show infantil</strong><br><br>Em Vila Nova, um espetáculo público de classificação livre foi anunciado. Uma menina de nove anos tentou entrar sozinha, sem os pais."
t3="<strong>Hospedagem de adolescente</strong><br><br>Um adolescente de dezesseis anos pediu um quarto em uma pensão de Vila Nova, sem autorização nem a presença dos pais ou responsável."
tx={"eca4a":t1,"eca4b":t2,"eca4c":t3}
# n=1
q(1,"É dever de todos prevenir a ocorrência de ameaça ou violação dos direitos da criança e do",["adolescente.","idoso.","adulto.","trabalhador.","consumidor."],"Art. 70.")
q(1,"A inobservância das normas de prevenção importará em responsabilidade da pessoa física ou",["jurídica.","pública.","rural.","militar.","civil, apenas."],"Art. 73.")
q(1,"A criança e o adolescente têm direito a informação, cultura, lazer, esportes, diversões, espetáculos e produtos e serviços que respeitem sua condição peculiar de",["pessoa em desenvolvimento.","pessoa adulta.","consumidor.","trabalhador.","cidadão."],"Art. 71.")
q(1,"O Poder Público regulará as diversões e espetáculos públicos, informando sobre a natureza deles e as faixas",["etárias a que não se recomendem.","salariais.","políticas.","regionais.","religiosas."],"Art. 74.")
q(1,"Os responsáveis pelas diversões e espetáculos públicos deverão afixar, à entrada do local, informação destacada sobre a natureza do espetáculo e a",["faixa etária.","origem do artista.","duração.","localização.","cor do cartaz."],"Art. 74, parágrafo único.")
q(1,"Toda criança ou adolescente terá acesso às diversões e espetáculos públicos classificados como adequados à sua",["faixa etária.","renda.","família.","escola.","residência."],"Art. 75.")
q(1,"As emissoras de rádio e televisão somente exibirão, no horário recomendado ao público infanto-juvenil, programas com finalidades educativas, artísticas, culturais e",["informativas.","comerciais.","políticas.","esportivas, apenas.","religiosas."],"Art. 76.")
q(1,"As revistas e publicações com material impróprio a crianças deverão ser comercializadas em embalagem",["lacrada, com a advertência de seu conteúdo.","aberta.","transparente.","gratuita.","reciclável."],"Art. 78.")
q(1,"As revistas destinadas ao público infanto-juvenil não poderão conter anúncios de bebidas alcoólicas, tabaco, armas e",["munições.","brinquedos.","alimentos.","livros.","roupas."],"Art. 79.")
q(1,"É proibida a venda à criança ou ao adolescente de",["bebidas alcoólicas.","pães.","livros escolares.","brinquedos.","lápis."],"Art. 81, II.")
q(1,"É proibida a venda à criança ou ao adolescente de bilhetes",["lotéricos e equivalentes.","de cinema.","de ônibus.","de teatro infantil.","de museu."],"Art. 81, VI.")
q(1,"É proibida a venda à criança ou ao adolescente de produtos cujos componentes possam causar dependência física ou",["psíquica.","visual.","auditiva.","social.","econômica."],"Art. 81, III.")
q(1,"A hospedagem de criança ou adolescente em hotel, motel ou pensão só é permitida se autorizado ou acompanhado pelos",["pais ou responsável.","amigos.","empregados.","irmãos menores.","vizinhos."],"Art. 82.")
q(1,"Entidades que atuem nas áreas da saúde e da educação devem ter pessoas capacitadas a reconhecer e comunicar ao Conselho Tutelar suspeitas de crimes contra a",["criança e o adolescente.","empresa.","escola.","comunidade.","autoridade."],"Art. 70-B.")
q(1,"As pessoas encarregadas, por razão de cargo, função, ofício ou profissão, do cuidado de crianças também são responsáveis pela",["comunicação ao Conselho Tutelar.","tutela.","guarda judicial.","adoção.","pensão."],"Art. 70-B, parágrafo único.")
q(1,"O art. 70-A prevê a capacitação permanente das Polícias Civil e Militar, do Corpo de Bombeiros e da",["Guarda Municipal.","Guarda Portuária.","Polícia Federal, apenas.","Marinha.","Aeronáutica."],"Art. 70-A, XI.")
q(1,"Os estabelecimentos de bilhar ou sinuca devem afixar aviso para orientação do",["público.","fiscal.","juiz.","Conselho Tutelar.","delegado."],"Art. 80.")
q(1,"No texto do bar com sinuca, os adolescentes jogando sinuca no bar descumprem a regra de que não pode ser permitida a",["entrada e a permanência de crianças e adolescentes.","venda de cerveja a adultos.","música alta.","presença de idosos.","venda de lanches."],"Art. 80.","eca4a")
q(1,"No texto do show infantil, a menina de nove anos só poderia ingressar e permanecer se estivesse acompanhada dos",["pais ou responsável.","amigos.","vizinhos.","irmãos de dez anos.","professores."],"Art. 75, parágrafo único.","eca4b")
q(1,"No texto da hospedagem de adolescente, a hospedagem na pensão sem os pais ou autorização é",["proibida.","livre.","permitida a partir de 16 anos.","permitida em pensão.","dependente do dono."],"Art. 82.","eca4c")
# n=2
q(2,"A União, os Estados, o Distrito Federal e os Municípios atuarão de forma articulada para coibir o uso de castigo físico ou de tratamento",["cruel ou degradante.","amistoso.","cuidadoso.","moderado.","temporário."],"Art. 70-A.")
q(2,"Entre as ações do art. 70-A está a promoção de campanhas educativas",["permanentes.","eventuais.","anuais.","comerciais.","religiosas."],"Art. 70-A, I.")
q(2,"As famílias com crianças e adolescentes com deficiência terão prioridade de atendimento nas ações de prevenção e",["proteção.","comércio.","lazer.","turismo.","consumo."],"Art. 70-A, parágrafo único.")
q(2,"O retardamento ou omissão injustificados da comunicação ao Conselho Tutelar são puníveis, culposos ou",["dolosos.","involuntários.","eventuais.","leves.","tolerados."],"Art. 70-B, parágrafo único.")
q(2,"As obrigações previstas no Estatuto não excluem da prevenção especial outras decorrentes dos",["princípios por ele adotados.","costumes.","contratos.","testamentos.","convênios."],"Art. 72.")
q(2,"Os proprietários de empresas que explorem a venda ou aluguel de fitas de vídeo cuidarão para que não haja venda ou locação em desacordo com a",["classificação atribuída pelo órgão competente.","vontade do cliente.","moda.","renda.","idade do dono."],"Art. 77.")
q(2,"As fitas de vídeo devem exibir, no invólucro, informação sobre a natureza da obra e a",["faixa etária a que se destinam.","duração.","origem.","preço.","cor."],"Art. 77, parágrafo único.")
q(2,"As capas que contenham mensagens pornográficas ou obscenas devem ser protegidas com embalagem",["opaca.","transparente.","aberta.","colorida.","dupla, apenas."],"Art. 78, parágrafo único.")
q(2,"As casas de jogos, para o art. 80, são as que realizem",["apostas, ainda que eventualmente.","apenas bingo.","apenas sinuca.","apenas dominó.","apenas cartas."],"Art. 80.")
q(2,"É proibida a venda a criança ou adolescente de fogos de estampido e de artifício, exceto os de reduzido potencial, incapazes de provocar",["dano físico em caso de utilização indevida.","barulho.","fumaça.","cor.","luz."],"Art. 81, IV.")
q(2,"É proibida a venda a criança ou adolescente das revistas e publicações a que alude o art.",["78.","74.","75.","76.","80."],"Art. 81, V.")
q(2,"A criança menor de dez anos em espetáculo público deve estar acompanhada dos pais ou responsável tanto para ingressar quanto para",["permanecer.","sair.","comer.","comprar.","pagar."],"Art. 75, parágrafo único.")
q(2,"Nenhum espetáculo será apresentado ou anunciado sem aviso de sua classificação, antes de sua transmissão, apresentação ou",["exibição.","venda.","edição.","propaganda.","contratação."],"Art. 76, parágrafo único.")
q(2,"A comunicação de suspeitas de crimes contra a criança, nos termos do art. 70-B, é feita ao",["Conselho Tutelar.","prefeito.","vereador.","síndico.","jornal."],"Art. 70-B.")
q(2,"Entre as ações do art. 70-A está a integração com órgãos de segurança pública, Judiciário, Ministério Público, Defensoria Pública e com o",["Conselho Tutelar.","sindicato.","clube.","mercado.","partido."],"Art. 70-A, II.")
q(2,"A capacitação do art. 70-A, XI, visa a identificar situações em que crianças vivenciam violência e agressões no âmbito familiar ou",["institucional.","esportivo.","político.","comercial.","religioso."],"Art. 70-A, XI.")
q(2,"No texto do bar com sinuca, a venda de cerveja aos adolescentes é proibida pelo art. 81, inciso",["II.","I.","III.","IV.","V."],"Art. 81, II.","eca4a")
q(2,"No texto do show infantil, a classificação livre não afasta a regra de que menores de dez anos entram acompanhados dos",["pais ou responsável.","amigos.","irmãos.","vizinhos.","professores."],"Art. 75, parágrafo único.","eca4b")
q(2,"No texto da hospedagem de adolescente, a pensão está enquadrada no art. 82 como estabelecimento",["congênere.","comercial, apenas.","residencial.","escolar.","religioso."],"Art. 82.","eca4c")
q(2,"Entre as ações do art. 70-A está a celebração de convênios, protocolos e ajustes entre órgãos governamentais ou entre estes e entidades",["não governamentais.","comerciais.","religiosas.","partidárias.","estrangeiras."],"Art. 70-A, X.")
# n=3
q(3,"Assinale a alternativa que traz apenas itens cuja venda a criança ou adolescente é proibida.",["Armas, bebidas alcoólicas e bilhetes lotéricos.","Livros, brinquedos e lápis.","Pão, leite e frutas.","Bicicletas e patins.","Roupas e calçados."],"Art. 81.")
q(3,"Considere. I. Menores de dez anos entram em espetáculo acompanhados. II. A hospedagem de adolescente sem os pais é permitida. III. A venda de bebida alcoólica é proibida. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A hospedagem é proibida, salvo autorização ou acompanhamento (art. 82).")
q(3,"Assinale a INCORRETA.",["É permitida a venda de armas a adolescentes acompanhados.","As publicações infanto-juvenis não podem trazer anúncios de bebidas alcoólicas.","As revistas impróprias são vendidas em embalagem lacrada.","Bilhar e sinuca exigem aviso e proibição de crianças.","A hospedagem exige autorização ou pais."],"A venda de armas a criança ou adolescente é proibida (art. 81, I).")
q(3,"O art. 79 proíbe, nas publicações infanto-juvenis, ilustrações, fotografias, legendas, crônicas ou anúncios de",["bebidas alcoólicas, tabaco, armas e munições.","alimentos.","brinquedos.","remédios.","livros."],"Art. 79.")
q(3,"A obrigação do art. 80 de afixar aviso recai sobre os responsáveis por estabelecimentos que explorem",["bilhar, sinuca ou casas de jogos.","padarias.","farmácias.","escolas.","livrarias."],"Art. 80.")
q(3,"A comunicação ao Conselho Tutelar prevista no art. 70-B é dever, além das entidades de saúde e educação, das pessoas encarregadas do",["cuidado, assistência ou guarda de crianças e adolescentes.","comércio de bebidas.","transporte público.","policiamento de rodovias.","jornalismo."],"Art. 70-B, parágrafo único.")
q(3,"Os produtos cujos componentes possam causar dependência física ou psíquica, ainda que por utilização indevida, têm a venda a criança ou adolescente",["proibida.","livre.","condicionada à renda.","permitida a partir de 16 anos.","permitida com pais."],"Art. 81, III.")
q(3,"A promoção de campanhas educativas e a formação continuada de profissionais constam do art. 70-A, que trata de",["políticas e ações para coibir o castigo físico e o tratamento cruel.","trabalho infantil.","adoção.","medidas socioeducativas.","guarda."],"Art. 70-A.")
q(3,"O art. 70-A, XI, prevê capacitação permanente que inclui profissionais nas escolas e",["Conselhos Tutelares.","tribunais de contas.","empresas de ônibus.","clubes.","sindicatos."],"Art. 70-A, XI.")
q(3,"A responsabilidade pela inobservância das normas de prevenção é da pessoa",["física ou jurídica.","apenas física.","apenas jurídica.","apenas pública.","apenas privada."],"Art. 73.")
q(3,"A informação destacada à entrada do local de exibição deve indicar a natureza do espetáculo e a faixa etária",["especificada no certificado de classificação.","sugerida pelo dono.","escolhida pelos pais.","definida pelo guarda.","livre."],"Art. 74, parágrafo único.")
q(3,"A venda de fogos de artifício a adolescente é proibida, EXCETO a de fogos que, pelo reduzido potencial, sejam",["incapazes de provocar dano físico em caso de utilização indevida.","coloridos.","silenciosos.","pequenos.","baratos."],"Art. 81, IV.")
q(3,"No texto do bar com sinuca, o dono do bar descumpriu, quanto à sinuca, o dever de afixar",["aviso para orientação do público.","cartaz de preços.","alvará.","extintor.","licença sanitária."],"Art. 80.","eca4a")
q(3,"No texto do bar com sinuca, o dono, além do art. 80, descumpriu o art. 81 ao vender",["bebida alcoólica a adolescente.","refrigerante.","salgado.","jornal.","bala."],"Art. 81, II.","eca4a")
q(3,"No texto do show infantil, a menina de nove anos, desacompanhada, não pode ingressar porque a regra do art. 75 vale para menores de",["dez anos.","oito anos.","doze anos.","quatorze anos.","sete anos."],"Art. 75, parágrafo único.","eca4b")
q(3,"No texto do show infantil, a classificação do espetáculo deve ser informada",["à entrada do local de exibição.","apenas na internet.","apenas na bilheteria.","apenas no cartaz externo.","apenas no jornal."],"Art. 74, parágrafo único.","eca4b")
q(3,"No texto da hospedagem de adolescente, a hospedagem só seria possível se o adolescente estivesse",["autorizado ou acompanhado pelos pais ou responsável.","com dinheiro.","com documento escolar.","com carta de amigo.","com identidade."],"Art. 82.","eca4c")
q(3,"No texto da hospedagem de adolescente, a proibição alcança hotel, motel, pensão ou estabelecimento",["congênere.","residencial.","religioso.","escolar.","hospitalar."],"Art. 82.","eca4c")
q(3,"No texto do bar com sinuca, a Guarda Municipal, ao identificar a situação, atua no âmbito do dever de todos de",["prevenir ameaça ou violação dos direitos da criança e do adolescente.","aplicar penas.","lavrar alvarás.","fechar o bar.","tutelar o adolescente."],"Art. 70.","eca4a")
q(3,"A criança e o adolescente têm direito a produtos e serviços que respeitem sua condição peculiar de pessoa em desenvolvimento, direito previsto no art.",["71.","70.","72.","73.","74."],"Art. 71.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("ECA: prevenção (arts. 70 a 82)",[
 ("ger","Prevenção geral",["dever de todos","articulação dos entes","capacitar a Guarda Municipal"],"seção 1"),
 ("com","Comunicação",["saúde e educação","quem cuida da criança","ao Conselho Tutelar"],"seção 1"),
 ("esp","Espetáculos",["classificação etária","menor de 10 anos: acompanhado","rádio e TV"],"seção 2"),
 ("pub","Publicações e jogos",["embalagem lacrada","sem anúncio de bebida","bilhar e sinuca: aviso"],"seção 2"),
 ("ven","Venda proibida",["armas, bebidas","dependência, fogos","revistas, bilhetes"],"seção 3"),
 ("hos","Hospedagem",["hotel, motel, pensão","autorização ou pais"],"seção 3")],
 "Na prova: art. 75, 80, 81 e 82")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a prevenção geral; as demais, diversões, publicações, produtos e hospedagem.","Fontes: Edital 02/2026, Anexo I; Lei 8.069/1990 (ECA), arts. 70 a 82, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("eca-4","ECA: prevenção geral e especial (arts. 70 a 82)",Q,list(tx),
 cobertura=["Cobertos: arts. 70 a 82. Do art. 70-A foram destacados o caput, o inciso I e o inciso XI; demais incisos não detalhados. A autorização para viajar (arts. 83 a 85) está fora do recorte do edital."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Conferir se o edital inclui os arts. 83 a 85 (autorização para viajar).","Trechos de lei copiados de fontes/eca.txt por programa.","Casos eca4a, eca4b e eca4c fictícios."],
 fontes_conferidas=["ECA, arts. 70 a 82: texto da Câmara, copiado por programa."])
gravar("eca-4",aula_html,banco("eca-4",Q),tx)
