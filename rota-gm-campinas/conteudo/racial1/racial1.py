import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='racial.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Lei Estadual (SP) 14.187/2010 pune administrativamente os atos de discriminação por motivo de raça ou cor praticados no Estado de São Paulo. É a lei local que o edital cobra em Direitos Humanos. A Vunesp pergunta o rol de atos discriminatórios do art. 2º (dez incisos), o aviso obrigatório do art. 2º-A, o processo administrativo, a denúncia à Secretaria da Justiça e da Defesa da Cidadania e as sanções do art. 6º (advertência, multa de até 1.000 UFESPs, até 3.000 na reincidência, suspensão e cassação da licença). Atenção: a sanção é administrativa, não penal."
S={}
S[1]="## 1. Atos discriminatórios e aviso obrigatório\n\n"+L("art. 1º","Artigo 1° -","Artigo 2° -")+"\n\n"+L("art. 2º","Artigo 2° - Consideram-se","Artigo 2°-A")+"\n\n"+L("art. 2º-A, caput","Artigo 2°-A - É obrigatória","§ 1° - Os avisos")+"\n\n"+L("art. 2º-A, §§ 1º e 3º","§ 1° - Os avisos","§ 2° - Para os fins")+"\n\n"+L("art. 2º-A, § 3º","§ 3° - O descumprimento","- Artigo 2°-A acrescentado")+"""

Será punido todo ato discriminatório por motivo de raça ou cor praticado no Estado por qualquer pessoa, jurídica ou física, inclusive a que exerça função pública. São atos discriminatórios: a ação violenta, constrangedora, intimidatória ou vexatória; a proibição ou constrangimento ao ingresso ou permanência em ambiente aberto ao público; embaraços ao acesso às dependências comuns de edifícios; a recusa, retardamento ou impedimento da utilização de serviços, transportes, comunicação, consumo, hospedagem, espetáculos, estabelecimentos comerciais ou bancários; a recusa de locação, compra ou empréstimo de bens; a coação do empregador sobre o empregado; a negativa de emprego, demissão ou obstáculo à ascensão ou ao acesso a cargo público ou licitação; a prática, indução ou incitação ao preconceito, inclusive por meios eletrônicos; a criação ou veiculação de símbolos e propagandas que incitem a discriminação; e a recusa da prestação de serviço de saúde, público ou privado.

É obrigatória a afixação de avisos nos ambientes de uso coletivo, públicos ou privados, em pontos de ampla visibilidade, com os dizeres da lei e a palavra DENUNCIE; o descumprimento acarreta ao proprietário ou responsável multa de 100 UFESPs. O conceito de ambientes de uso coletivo é amplo, abrangendo trabalho, estudo, lazer, comércio, repartições públicas, transporte coletivo, viaturas oficiais e táxis.
"""
S[2]="## 2. Processo administrativo e denúncia\n\n"+L("art. 3º","Artigo 3° - A prática dos atos","Artigo 4° -")+"\n\n"+L("art. 4º, caput","Artigo 4° - Aquele que for vítima","§ 1° - O relato")+"\n\n"+L("art. 4º, § 3º","§ 3° - Recebida a denúncia","Artigo 5°")+"\n\n"+L("art. 5º","Artigo 5° - A Secretaria","Artigo 6° -")+"""

A prática dos atos é apurada em processo administrativo, iniciado por reclamação do ofendido, de seu representante legal ou de qualquer pessoa que tenha ciência do ato, ou por ato ou ofício de autoridade competente. A vítima, seu representante legal ou quem tenha presenciado os atos pode relatá-los à Secretaria da Justiça e da Defesa da Cidadania, inclusive por meio eletrônico. Recebida a denúncia, a Secretaria promove a instauração do processo administrativo para apuração e imposição das sanções e transmite notícia à autoridade policial quando o fato caracterizar infração penal. Para fiscalizar, a Secretaria pode firmar convênios com Municípios, com a Assembleia Legislativa e com Câmaras Municipais.
"""
S[3]="## 3. Sanções\n\n"+L("art. 6º, caput","Artigo 6° - As sanções aplicáveis","§ 1° - Quando a infração")+"\n\n"+L("art. 6º, § 1º","§ 1° - Quando a infração","§ 2° - O valor")+"\n\n"+L("art. 6º, §§ 2º e 3º","§ 2° - O valor da multa","§ 4°")+"\n\n"+L("art. 7º","Artigo 7° - Na apuração","Artigo 8°")+"""

As sanções são a advertência; multa de até 1.000 UFESPs; multa de até 3.000 UFESPs, em caso de reincidência; suspensão da licença estadual para funcionamento por 30 dias; e cassação da licença estadual para funcionamento. Quando a infração for cometida por agente público, servidor ou militar, no exercício de suas funções, aplicam-se também as penalidades disciplinares, sem prejuízo das sanções dos incisos I a III. O valor da multa considera as condições pessoais e econômicas do infrator e não pode ser inferior a 500 UFESPs, podendo ser elevada até o triplo quando a quantia inferior seria ineficaz. Na apuração observa-se a Lei 10.177/1998, que regula o processo administrativo no âmbito da Administração Pública Estadual.
"""
S[5]="""## 5. Na rotina do guarda

- **Discriminação no atendimento:** o guarda que presencia recusa de entrada, de serviço ou constrangimento por raça ou cor orienta a vítima a denunciar e pode registrar a ocorrência.
- **Infração penal:** quando o fato caracterizar crime (por exemplo, racismo ou injúria racial), a Secretaria transmite notícia à autoridade policial.
- **Aviso afixado:** em ambientes de uso coletivo, o cartaz da lei deve estar em ponto de ampla visibilidade.
- **Agente público:** o guarda que discriminar responde também disciplinarmente, além das multas.
- **Relato:** qualquer pessoa que presenciou pode relatar à Secretaria da Justiça, inclusive por meio eletrônico.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Natureza da punição | Administrativa, com processo administrativo |
| Quem pratica | Pessoa física ou jurídica, inclusive quem exerce função pública |
| Atos discriminatórios | Dez incisos do art. 2º |
| Aviso | Obrigatório em ambientes de uso coletivo; multa de 100 UFESPs |
| Quem pode relatar | Vítima, representante legal ou quem presenciou |
| Para quem se relata | Secretaria da Justiça e da Defesa da Cidadania |
| Multa | Até 1.000 UFESPs; até 3.000 na reincidência; mínimo de 500 |
| Elevação | Até o triplo, se a multa for ineficaz |
| Sanções gravosas | Suspensão de 30 dias e cassação da licença estadual |
| Agente público | Também penalidades disciplinares |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Todo ato discriminatório por raça ou cor, no Estado |
| Art. 2º | Dez atos discriminatórios |
| Art. 2º-A | Aviso obrigatório; multa de 100 UFESPs |
| Art. 3º | Processo administrativo: reclamação ou ato de ofício |
| Art. 4º | Relato à Secretaria da Justiça |
| Art. 5º | Convênios |
| Art. 6º | Advertência, multas, suspensão e cassação |
| Art. 7º | Lei 10.177/1998 |
"""
QR=[("Questão 1","Segundo a Lei Estadual (SP) 14.187/2010, será punido todo ato discriminatório por motivo de raça ou cor praticado no Estado por qualquer pessoa, jurídica ou física, inclusive a que exerça",["função pública.","atividade esportiva.","atividade rural.","atividade de lazer.","profissão liberal."],0,"Art. 1º."),
("Questão 2","A multa por descumprimento da obrigação de afixação de avisos é de",["100 UFESPs.","10 UFESPs.","500 UFESPs.","1.000 UFESPs.","3.000 UFESPs."],1,"Art. 2º-A, § 3º."),
("Questão 3","O relato da discriminação pode ser feito à Secretaria da Justiça e da Defesa da",["Cidadania.","Educação.","Saúde.","Fazenda.","Segurança."],2,"Art. 4º."),
("Questão 4","Em caso de reincidência, a multa pode chegar a",["3.000 UFESPs.","500 UFESPs.","1.000 UFESPs.","100 UFESPs.","5.000 UFESPs."],3,"Art. 6º, III.")]
t1="<strong>Recusa de entrada</strong><br><br>Em Vila Nova, cidade fictícia, um bar impediu a entrada de um cliente por causa de sua cor, e uma testemunha acionou a guarda municipal."
t2="<strong>Aviso ausente</strong><br><br>Um supermercado de Vila Nova não tinha afixado, em local visível, o aviso exigido pela lei estadual contra a discriminação racial."
t3="<strong>Servidor que discriminou</strong><br><br>Um servidor público estadual recusou atendimento a um cidadão por motivo de raça, no exercício de suas funções, e a Secretaria instaurou processo administrativo."
tx={"racial1a":t1,"racial1b":t2,"racial1c":t3}
# n=1
q(1,"A Lei Estadual 14.187/2010 pune os atos discriminatórios por motivo de raça ou",["cor.","religião.","idade.","renda.","classe."],"Art. 1º.")
q(1,"A lei alcança atos praticados no",["Estado de São Paulo.","território nacional.","exterior.","Município de São Paulo, apenas.","Distrito Federal."],"Art. 1º.")
q(1,"É ato discriminatório praticar qualquer tipo de ação violenta, constrangedora, intimidatória ou",["vexatória.","legal.","comum.","educativa.","comercial."],"Art. 2º, I.")
q(1,"É ato discriminatório proibir ou impor constrangimento ao ingresso ou permanência em ambiente ou estabelecimento aberto ao",["público.","domicílio.","empregador.","condomínio.","sócio."],"Art. 2º, II.")
q(1,"É ato discriminatório recusar, retardar, impedir ou onerar a locação, compra ou empréstimo de bens móveis ou",["imóveis.","intangíveis.","públicos.","estrangeiros.","rurais."],"Art. 2º, V.")
q(1,"É ato discriminatório negar emprego, demitir ou dificultar a ascensão em empresa pública ou",["privada.","estrangeira.","filantrópica.","religiosa.","familiar."],"Art. 2º, VII.")
q(1,"É ato discriminatório recusar, retardar ou impedir a prestação de serviço de saúde, público ou",["privado.","filantrópico.","militar.","rural.","estrangeiro."],"Art. 2º, X.")
q(1,"É obrigatória a afixação de avisos nos ambientes de uso coletivo, públicos ou privados, em pontos de ampla",["visibilidade.","altura.","privacidade.","luminosidade.","distância."],"Art. 2º-A.")
q(1,"Os avisos devem ter os dizeres da lei e a palavra",["DENUNCIE.","ATENÇÃO.","PROIBIDO.","CUIDADO.","SILÊNCIO."],"Art. 2º-A, § 1º.")
q(1,"O descumprimento do art. 2º-A acarreta multa de 100",["UFESPs.","reais.","salários mínimos.","dólares.","dias-multa."],"Art. 2º-A, § 3º.")
q(1,"A prática dos atos discriminatórios será apurada em processo",["administrativo.","penal.","civil.","eleitoral.","trabalhista."],"Art. 3º.")
q(1,"O processo pode ter início por reclamação do ofendido ou por ato ou ofício de autoridade",["competente.","vizinha.","privada.","estrangeira.","religiosa."],"Art. 3º, II.")
q(1,"A vítima ou quem tenha presenciado os atos poderá relatá-los à Secretaria da Justiça e da Defesa da",["Cidadania.","Segurança.","Educação.","Fazenda.","Saúde."],"Art. 4º.")
q(1,"O relato poderá ser apresentado por meio eletrônico, no sítio da",["internet.","imprensa.","rádio.","televisão.","fax."],"Art. 4º, § 2º.")
q(1,"A Secretaria poderá firmar convênios com Municípios, com a Assembleia Legislativa e com",["Câmaras Municipais.","empresas.","clubes.","sindicatos.","partidos."],"Art. 5º.")
q(1,"A primeira das sanções do art. 6º é a",["advertência.","multa.","suspensão.","cassação.","prisão."],"Art. 6º, I.")
q(1,"A cassação da licença estadual para funcionamento é a",["última sanção da lista.","primeira sanção da lista.","sanção penal.","sanção civil.","sanção eleitoral."],"Art. 6º, V.")
q(1,"No texto da recusa de entrada, o impedimento de entrada por cor é ato do art. 2º, inciso",["II.","I.","V.","VII.","X."],"Art. 2º, II.","racial1a")
q(1,"No texto do aviso ausente, a falta do aviso acarreta ao responsável multa de",["100 UFESPs.","500 UFESPs.","1.000 UFESPs.","3.000 UFESPs.","10 UFESPs."],"Art. 2º-A, § 3º.","racial1b")
q(1,"No texto do servidor que discriminou, a punição da lei, além da multa, inclui penalidades",["disciplinares.","eleitorais.","tributárias.","militares apenas.","civis apenas."],"Art. 6º, § 1º.","racial1c")
# n=2
q(2,"É ato discriminatório criar embaraços ao acesso e à utilização das dependências comuns e áreas não privativas de",["edifícios.","carros.","empresas.","clubes.","escolas."],"Art. 2º, III.")
q(2,"É ato discriminatório praticar, induzir ou incitar o preconceito, inclusive pelos meios de comunicação, inclusive",["eletrônicos.","manuscritos.","orais apenas.","impressos apenas.","pessoais."],"Art. 2º, VIII.")
q(2,"É ato discriminatório criar, comercializar ou veicular símbolos, emblemas e propagandas que incitem à",["discriminação.","saúde.","venda.","educação.","união."],"Art. 2º, IX.")
q(2,"É ato discriminatório o empregador praticar atos de coação direta ou indireta sobre o",["empregado.","cliente.","vizinho.","fornecedor.","sócio."],"Art. 2º, VI.")
q(2,"A expressão ambientes de uso coletivo compreende, entre outros, os veículos públicos ou privados de transporte coletivo, as viaturas oficiais e os",["táxis.","carros particulares.","caminhões.","aviões particulares.","barcos de lazer."],"Art. 2º-A, § 2º.")
q(2,"O processo administrativo pode iniciar-se por reclamação de qualquer pessoa que tenha ciência do ato",["discriminatório.","legal.","comercial.","esportivo.","religioso."],"Art. 3º, I.")
q(2,"O relato deve conter a exposição do fato e suas circunstâncias e a identificação do",["autor.","juiz.","delegado.","promotor.","vizinho."],"Art. 4º, § 1º.")
q(2,"Recebida a denúncia, compete à Secretaria promover a instauração do processo administrativo para apuração e imposição das",["sanções cabíveis.","penas privativas.","medidas socioeducativas.","multas de trânsito.","intimações."],"Art. 4º, § 3º, I.")
q(2,"Se o fato caracterizar infração penal, a Secretaria transmite notícia à autoridade",["policial competente.","eleitoral.","tributária.","sanitária.","ambiental."],"Art. 4º, § 3º, II.")
q(2,"A multa de até 1.000 UFESPs é a sanção do inciso",["II do art. 6º.","I do art. 6º.","III do art. 6º.","IV do art. 6º.","V do art. 6º."],"Art. 6º, II.")
q(2,"A suspensão da licença estadual para funcionamento é por",["30 dias.","10 dias.","60 dias.","90 dias.","1 ano."],"Art. 6º, IV.")
q(2,"O valor da multa não poderá ser inferior a",["500 UFESPs.","100 UFESPs.","1.000 UFESPs.","3.000 UFESPs.","50 UFESPs."],"Art. 6º, § 2º.")
q(2,"A multa poderá ser elevada até o triplo quando sua fixação em quantia inferior seria",["ineficaz.","injusta.","ilegal.","imoral.","indevida."],"Art. 6º, § 3º.")
q(2,"A pena de cassação da licença será comunicada à autoridade responsável pela outorga da",["licença.","multa.","pensão.","guarda.","sentença."],"Art. 6º, § 4º.")
q(2,"Na apuração dos atos discriminatórios devem ser observados os procedimentos da Lei 10.177/1998, que regula o processo administrativo no âmbito da Administração Pública",["Estadual.","Municipal.","Federal.","Distrital.","Militar."],"Art. 7º.")
q(2,"A lei entra em vigor na data de sua",["publicação.","regulamentação.","sanção.","aprovação.","revogação."],"Art. 8º.")
q(2,"No texto da recusa de entrada, o relato pode ser feito por quem presenciou, à Secretaria da Justiça, por meio",["eletrônico, inclusive.","apenas verbal.","apenas por advogado.","apenas por carta.","apenas por fax."],"Art. 4º, § 2º.","racial1a")
q(2,"No texto do aviso ausente, o aviso deve ser exibido na forma de cartaz, placa ou",["plaqueta.","painel.","luminoso.","cartão.","adesivo de carro."],"Art. 2º-A, § 1º.","racial1b")
q(2,"No texto do servidor que discriminou, o processo administrativo foi instaurado pela",["Secretaria da Justiça e da Defesa da Cidadania.","delegacia.","imprensa.","comarca.","prefeitura."],"Art. 4º, § 3º, I.","racial1c")
q(2,"A sanção do inciso III do art. 6º, multa de até 3.000 UFESPs, tem como pressuposto a",["reincidência.","denúncia anônima.","existência de crime.","condenação penal.","prescrição."],"Art. 6º, III.")
# n=3
q(3,"Assinale a alternativa correta sobre as sanções da Lei 14.187/2010.",["Advertência; multa de até 1.000 UFESPs; até 3.000 na reincidência; suspensão por 30 dias; cassação da licença.","Prisão de 1 a 3 anos.","Multa de 100 reais.","Perda do cargo imediata.","Apenas advertência."],"Art. 6º.")
q(3,"Considere. I. A lei pune administrativamente os atos de discriminação racial. II. A multa mínima é de 500 UFESPs. III. A lei estabelece pena de reclusão. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A lei não prevê reclusão: as sanções são administrativas (art. 6º).")
q(3,"Assinale a INCORRETA.",["A lei só alcança pessoas jurídicas.","A lei alcança pessoa física ou jurídica.","A lei alcança quem exerce função pública.","O processo é administrativo.","A multa tem limites em UFESPs."],"A lei alcança pessoa física ou jurídica (art. 1º).")
q(3,"A multa de até 3.000 UFESPs é aplicada em caso de",["reincidência.","dolo.","culpa.","mero capricho.","denúncia anônima."],"Art. 6º, III.")
q(3,"Quando a infração for cometida por agente público, servidor ou militar, serão aplicadas, sem prejuízo das sanções dos incisos I a III, as penalidades",["disciplinares cominadas na legislação pertinente.","penais.","eleitorais.","tributárias.","trabalhistas."],"Art. 6º, § 1º.")
q(3,"O descumprimento do art. 2º-A é punido com multa a quem for proprietário ou responsável pelo estabelecimento ou meio de",["transporte coletivo.","carga.","comunicação.","lazer.","lavoura."],"Art. 2º-A, § 3º.")
q(3,"O art. 2º-A foi acrescentado pela Lei estadual",["16.762/2018.","14.187/2010.","10.177/1998.","8.069/1990.","11.340/2006."],"Art. 2º-A, nota de alteração.")
q(3,"A multa mínima de 500 UFESPs vale para a multa do art. 6º, e o valor leva em conta as condições pessoais e",["econômicas do infrator.","raciais.","religiosas.","políticas.","familiares."],"Art. 6º, § 2º.")
q(3,"A comunicação da cassação da licença, além da autoridade outorgante, é feita à autoridade federal ou municipal para eventuais providências no âmbito de sua",["competência.","vontade.","conveniência.","residência.","região."],"Art. 6º, § 4º.")
q(3,"O relato que ao ser recebido pela Secretaria pode levar à instauração do processo deve conter a identificação do autor com nome, prenome, número da cédula de identidade, endereço e",["assinatura.","profissão.","foto.","renda.","filiação."],"Art. 4º, § 1º, 2.")
q(3,"A lei mantém o foco em condutas de recusa ou impedimento de serviços e acesso, entre elas as de recusa de serviços de saúde, tema do inciso",["X do art. 2º.","I do art. 2º.","V do art. 2º.","VIII do art. 2º.","IX do art. 2º."],"Art. 2º, X.")
q(3,"A negativa de acesso a cargo ou função pública ou a certame licitatório é discriminação prevista no art. 2º, inciso",["VII.","I.","II.","V.","X."],"Art. 2º, VII.")
q(3,"A lei classifica a recusa de transporte, comunicação, hospedagem e espetáculos no art. 2º, inciso",["IV.","I.","II.","V.","VII."],"Art. 2º, IV.")
q(3,"No texto da recusa de entrada, o ato configura discriminação e, além da sanção administrativa, o fato pode caracterizar",["infração penal, devendo ser comunicado à autoridade policial.","apenas infração civil.","nenhuma infração.","infração eleitoral.","infração tributária."],"Art. 4º, § 3º, II.","racial1a")
q(3,"No texto da recusa de entrada, a testemunha que acionou a guarda pode também relatar o fato à Secretaria, pois a lei permite o relato por quem",["tenha presenciado os atos.","seja apenas parente da vítima.","tenha a mesma cor.","seja advogado.","seja comerciante."],"Art. 4º.","racial1a")
q(3,"No texto do aviso ausente, o aviso deve conter a frase de que a lei pune administrativamente os atos de discriminação racial no Estado de São Paulo e a palavra",["DENUNCIE.","CUIDADO.","SILÊNCIO.","PROIBIDO.","ATENÇÃO."],"Art. 2º-A, § 1º.","racial1b")
q(3,"No texto do aviso ausente, supermercados enquadram-se na expressão ambientes de uso coletivo, que inclui",["supermercados.","apenas escolas.","apenas hospitais.","apenas praças.","apenas teatros."],"Art. 2º-A, § 2º.","racial1b")
q(3,"No texto do servidor que discriminou, as sanções do art. 6º, incisos I a III, aplicam-se sem prejuízo das penalidades",["disciplinares.","eleitorais.","tributárias.","militares apenas.","civis apenas."],"Art. 6º, § 1º.","racial1c")
q(3,"No texto do servidor que discriminou, o servidor responde porque a lei alcança quem exerce função",["pública.","privada.","religiosa.","esportiva.","artística."],"Art. 1º.","racial1c")
q(3,"No texto do servidor que discriminou, a recusa de atendimento a cidadão por motivo de raça é ato discriminatório previsto no art. 2º, entre outros, no inciso",["IV.","VI.","VIII.","IX.","III."],"Art. 2º, IV.","racial1c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Lei Estadual (SP) 14.187/2010: discriminação racial",[
 ("alc","Alcance",["raça ou cor","pessoa física ou jurídica","inclusive função pública"],"seção 1"),
 ("ato","Atos discriminatórios",["dez incisos","acesso, serviços, emprego","propaganda e saúde"],"seção 1"),
 ("avi","Aviso obrigatório",["ambientes de uso coletivo","DENUNCIE","multa de 100 UFESPs"],"seção 1"),
 ("pro","Processo",["administrativo","reclamação ou ofício","Secretaria da Justiça"],"seção 2"),
 ("san","Sanções",["advertência","multa 1.000 / 3.000 UFESPs","suspensão e cassação"],"seção 3"),
 ("age","Agente público",["também disciplinar","sem prejuízo das multas"],"seção 3")],
 "Na prova: rol de atos, aviso e sanções em UFESPs")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o alcance, os atos discriminatórios e o aviso; as demais, o processo e as sanções.","Fontes: Edital 02/2026, Anexo I; Lei Estadual (SP) 14.187/2010, texto consolidado da Assembleia Legislativa de São Paulo. Exemplos criados para a aula.")
revisao("racial-1","Lei Estadual (SP) 14.187/2010: discriminação racial",Q,list(tx),
 cobertura=["Todos os artigos (1º a 8º). Do art. 2º-A, o § 2º (rol de ambientes de uso coletivo) foi apenas resumido."],
 pendencias=["Texto-fonte: página da Assembleia Legislativa de São Paulo, baixada em 14/11/2026; reconferir a versão atualizada no sítio da ALESP.","O valor da UFESP varia por ano; a aula usa os números de UFESPs, não valores em reais.","Trechos de lei copiados de fontes/racial.txt por programa.","Casos racial1a, racial1b e racial1c fictícios."],
 fontes_conferidas=["Lei Estadual (SP) 14.187/2010, arts. 1º a 7º: texto copiado por programa."])
gravar("racial-1",aula_html,banco("racial-1",Q),tx)
