import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='eca.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="As entidades de atendimento (arts. 90 a 97) são os programas e as instituições que executam as medidas de proteção e socioeducativas: acolhimento, semiliberdade, internação. O texto é cheio de listas e prazos que a Vunesp adora: os oito regimes de atendimento, os motivos para negar o registro, os princípios do acolhimento, o prazo de 24 horas para comunicar ao juiz, o prazo máximo do registro (quatro anos) e as medidas contra entidades que descumprem. Para o guarda, interessa saber quem fiscaliza (Judiciário, Ministério Público, Conselhos Tutelares) e que as entidades que abrigam crianças devem reportar maus-tratos ao Conselho Tutelar."
S={}
S[1]="## 1. Programas e regimes de atendimento\n\n"+L("art. 90, caput","Art. 90. As entidades de atendimento","§ 1º As entidades governamentais")+"\n\n"+L("art. 90, § 1º","§ 1º As entidades governamentais","§ 1º pela Lei nº 12.010")+"\n\n"+L("art. 90, § 3º","§ 3º Os programas em execução","Art. 91.")+"""

As entidades de atendimento mantêm as próprias unidades e planejam e executam programas de proteção e socioeducativos em oito regimes: orientação e apoio sociofamiliar; apoio socioeducativo em meio aberto; colocação familiar; acolhimento institucional; prestação de serviços à comunidade; liberdade assistida; semiliberdade; e internação. As entidades governamentais e não governamentais inscrevem seus programas no Conselho Municipal dos Direitos da Criança e do Adolescente, que mantém o registro e comunica ao Conselho Tutelar e à autoridade judiciária. Os programas são reavaliados pelo Conselho Municipal, no máximo, a cada dois anos.
"""
S[2]="## 2. Registro das entidades não governamentais\n\n"+L("art. 91, caput","Art. 91. As entidades não-governamentais","§ 1º Será negado")+"\n\n"+L("art. 91, § 1º","§ 1º Será negado o registro à entidade que:")+"\n\n"+L("art. 91, § 1º, alíneas","a) não ofereça instalações","§ 2º O registro terá")+"\n\n"+L("art. 91, § 2º","§ 2º O registro terá validade","Art. 92.")+"""

As entidades não governamentais só funcionam depois de registradas no Conselho Municipal dos Direitos da Criança e do Adolescente, que comunica o registro ao Conselho Tutelar e à autoridade judiciária. O registro é negado à entidade que não ofereça instalações adequadas de habitabilidade, higiene, salubridade e segurança; não apresente plano de trabalho compatível com a lei; esteja irregularmente constituída; tenha em seus quadros pessoas inidôneas; ou não cumpra as resoluções dos Conselhos de Direitos. O registro vale no máximo quatro anos e é reavaliado periodicamente.
"""
S[3]="## 3. Acolhimento familiar e institucional\n\n"+L("art. 92, caput","Art. 92. As entidades que desenvolvam programas","§ 1º O dirigente")+"\n\n"+L("art. 92, § 1º","§ 1º O dirigente de entidade","§ 1º com nova redação")+"\n\n"+L("art. 92, § 2º","§ 2º Os dirigentes de entidades","§ 3º Os entes")+"\n\n"+L("art. 93","Art. 93. As entidades que mantenham","Parágrafo único. Recebida")+"""

As entidades de acolhimento familiar ou institucional seguem nove princípios, entre eles a preservação dos vínculos familiares, a integração em família substituta quando esgotados os recursos na família natural ou extensa, o atendimento personalizado em pequenos grupos, o não desmembramento de irmãos e a preparação gradativa para o desligamento. O dirigente da entidade de acolhimento institucional é equiparado ao guardião para todos os efeitos de direito. Os dirigentes remetem à autoridade judiciária, no máximo a cada seis meses, relatório circunstanciado sobre cada criança acolhida e sua família.

As entidades de acolhimento institucional podem, em caráter excepcional e de urgência, acolher crianças e adolescentes sem prévia determinação da autoridade competente, comunicando o fato em até 24 horas ao Juiz da Infância e da Juventude, sob pena de responsabilidade.
"""
S[4]="## 4. Internação, fiscalização e medidas\n\n"+L("art. 94, I a XII","Art. 94. As entidades que desenvolvem programas de internação","XIII - proceder")+"\n\n"+L("art. 94, XIV","XIV - reavaliar periodicamente","XV - informar")+"\n\n"+L("art. 94-A","Art. 94-A. As entidades, públicas ou privadas","Seção II")+"\n\n"+L("arts. 95 e 96","Art. 95. As entidades governamentais","Art. 97.")+"\n\n"+L("art. 97, caput e incisos","Art. 97. São medidas aplicáveis","§ 1º Em caso de reiteradas")+"""

As entidades que executam internação devem, entre outras obrigações, observar os direitos dos adolescentes; não restringir direito que a decisão de internação não restringiu; oferecer atendimento personalizado em pequenas unidades; preservar a identidade; diligenciar pelos vínculos familiares; oferecer instalações, vestuário, alimentação, cuidados médicos, psicológicos, odontológicos e farmacêuticos; propiciar escolarização, profissionalização, atividades culturais, esportivas e de lazer e assistência religiosa; e reavaliar cada caso com intervalo máximo de seis meses. As entidades que abriguem crianças devem ter profissionais capacitados a reconhecer e reportar ao Conselho Tutelar suspeitas de maus-tratos.

As entidades são fiscalizadas pelo Judiciário, pelo Ministério Público e pelos Conselhos Tutelares. Os planos de aplicação e as prestações de contas são apresentados ao Estado ou ao Município, conforme a origem das dotações. Para as entidades governamentais, as medidas por descumprimento são advertência, afastamento provisório ou definitivo dos dirigentes e fechamento de unidade ou interdição de programa; para as não governamentais, advertência, suspensão do repasse de verbas públicas, interdição de unidades ou suspensão de programa e cassação do registro.
"""
S[5]="""## 5. Na rotina do guarda

- **Fiscalização:** quem fiscaliza as entidades é o Judiciário, o Ministério Público e o Conselho Tutelar; o guarda comunica irregularidades que presencie.
- **Acolhimento de urgência:** a entidade pode receber a criança sem ordem prévia e comunica o juiz em até 24 horas.
- **Maus-tratos em abrigo:** as entidades devem reportar ao Conselho Tutelar; o guarda que testemunha também comunica.
- **Entidade sem registro:** a entidade não governamental só funciona após registro no Conselho Municipal; funcionamento sem registro é irregularidade a ser comunicada.
- **Adolescente internado:** os direitos não restringidos pela decisão são preservados.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Regimes de atendimento | Oito (orientação, meio aberto, colocação familiar, acolhimento, PSC, LA, semiliberdade, internação) |
| Onde se inscrevem os programas | Conselho Municipal dos Direitos da Criança e do Adolescente |
| Reavaliação dos programas | No máximo a cada dois anos |
| Validade do registro | Máximo de quatro anos |
| Relatório do acolhimento | No máximo a cada seis meses, à autoridade judiciária |
| Acolhimento de urgência | Comunicação ao juiz em até 24 horas |
| Reavaliação na internação | Intervalo máximo de seis meses |
| Quem fiscaliza | Judiciário, Ministério Público e Conselhos Tutelares |
| Medidas | Entidade governamental: afastamento de dirigentes; não governamental: cassação do registro |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 90 | Oito regimes; inscrição no Conselho Municipal; reavaliação em 2 anos |
| Art. 91 | Registro obrigatório; validade de 4 anos |
| Negativa de registro | Instalações, plano, constituição, inidoneidade, resoluções |
| Art. 92 | Princípios do acolhimento; dirigente equiparado a guardião |
| Relatório | A cada 6 meses |
| Art. 93 | Acolhimento de urgência; 24 horas |
| Art. 94 | Obrigações da internação; reavaliação em 6 meses |
| Art. 94-A | Capacitação para reportar maus-tratos |
| Art. 95 | Fiscalização: Judiciário, MP e Conselhos Tutelares |
| Art. 97 | Medidas por descumprimento |
"""
QR=[("Questão 1","As entidades não governamentais somente poderão funcionar depois de registradas no",["Conselho Municipal dos Direitos da Criança e do Adolescente.","Conselho Tutelar.","Ministério Público.","Juizado de Paz.","Cartório de Registro Civil."],0,"Art. 91."),
("Questão 2","O registro das entidades não governamentais terá validade máxima de",["quatro anos.","um ano.","dois anos.","seis anos.","dez anos."],1,"Art. 91, § 2º."),
("Questão 3","As entidades de acolhimento institucional podem acolher crianças sem prévia determinação da autoridade competente, comunicando o fato ao Juiz da Infância e da Juventude em até",["vinte e quatro horas.","quarenta e oito horas.","sete dias.","dez dias.","trinta dias."],2,"Art. 93."),
("Questão 4","As entidades governamentais e não governamentais serão fiscalizadas pelo Judiciário, pelo Ministério Público e pelos",["Conselhos Tutelares.","prefeitos.","vereadores.","sindicatos.","clubes."],3,"Art. 95.")]
t1="<strong>Abrigo sem registro</strong><br><br>Uma associação de Vila Nova, cidade fictícia, passou a abrigar crianças em uma casa sem ter registro no Conselho Municipal. A guarda municipal tomou conhecimento durante uma ronda."
t2="<strong>Acolhimento de urgência</strong><br><br>Uma criança de seis anos foi encontrada sozinha à noite, e o abrigo da cidade a acolheu sem ordem prévia do juiz, comunicando o fato 10 horas depois."
t3="<strong>Unidade de internação</strong><br><br>Uma entidade de Vila Nova que executa internação de adolescentes não reavaliava os casos havia oito meses e proibia visitas dos pais sem decisão que as restringisse."
tx={"eca5a":t1,"eca5b":t2,"eca5c":t3}
# n=1
q(1,"As entidades de atendimento são responsáveis pela manutenção das próprias unidades e pelo planejamento e execução de programas de proteção e",["socioeducativos.","comerciais.","tributários.","militares.","partidários."],"Art. 90.")
q(1,"Entre os regimes de atendimento do art. 90 está a prestação de serviços à",["comunidade.","empresa.","prefeitura, apenas.","escola, apenas.","igreja, apenas."],"Art. 90, V.")
q(1,"Entre os regimes de atendimento está a liberdade",["assistida.","vigiada.","condicional.","provisória.","plena."],"Art. 90, VI.")
q(1,"Entre os regimes de atendimento do art. 90 estão a semiliberdade e a",["internação.","prisão.","detenção.","reclusão.","expulsão."],"Art. 90, VII e VIII.")
q(1,"As entidades inscrevem seus programas no Conselho Municipal dos Direitos da Criança e do",["Adolescente.","Idoso.","Trabalhador.","Consumidor.","Cidadão."],"Art. 90, § 1º.")
q(1,"Os programas em execução serão reavaliados pelo Conselho Municipal, no máximo, a cada",["dois anos.","um ano.","três anos.","quatro anos.","cinco anos."],"Art. 90, § 3º.")
q(1,"Será negado o registro à entidade que não ofereça instalações físicas em condições adequadas de habitabilidade, higiene, salubridade e",["segurança.","luxo.","decoração.","tecnologia.","jardins."],"Art. 91, § 1º, a.")
q(1,"Será negado o registro à entidade que tenha em seus quadros pessoas",["inidôneas.","jovens.","idosas.","voluntárias.","estrangeiras."],"Art. 91, § 1º, d.")
q(1,"As entidades de acolhimento devem adotar o princípio da preservação dos vínculos familiares e promoção da",["reintegração familiar.","adoção imediata.","institucionalização.","guarda.","tutela."],"Art. 92, I.")
q(1,"Entre os princípios do acolhimento está o não desmembramento de grupos de",["irmãos.","amigos.","colegas.","vizinhos.","funcionários."],"Art. 92, V.")
q(1,"O dirigente de entidade de acolhimento institucional é equiparado ao",["guardião, para todos os efeitos de direito.","tutor.","juiz.","delegado.","curador."],"Art. 92, § 1º.")
q(1,"Os dirigentes das entidades de acolhimento remetem à autoridade judiciária relatório circunstanciado, no máximo a cada",["seis meses.","um mês.","três meses.","um ano.","dois anos."],"Art. 92, § 2º.")
q(1,"As entidades de acolhimento institucional podem acolher sem prévia ordem, comunicando ao juiz em até 24 horas, apenas em caráter excepcional e de",["urgência.","rotina.","lazer.","conveniência.","festa."],"Art. 93.")
q(1,"As entidades que desenvolvem programas de internação devem observar os direitos e garantias de que são titulares os",["adolescentes.","funcionários.","pais.","vizinhos.","diretores."],"Art. 94, I.")
q(1,"Na internação, a reavaliação periódica de cada caso tem intervalo máximo de",["seis meses.","um mês.","três meses.","um ano.","dois anos."],"Art. 94, XIV.")
q(1,"As entidades que abriguem crianças devem ter profissionais capacitados a reconhecer e reportar ao Conselho Tutelar suspeitas de",["maus-tratos.","furtos.","fugas.","aniversários.","viagens."],"Art. 94-A.")
q(1,"Os planos de aplicação e as prestações de contas das entidades serão apresentados ao Estado ou ao Município, conforme a origem das",["dotações orçamentárias.","doações privadas.","vendas.","heranças.","multas."],"Art. 96.")
q(1,"No texto do abrigo sem registro, a entidade não governamental só poderia funcionar após registrar-se no",["Conselho Municipal dos Direitos da Criança e do Adolescente.","Cartório.","Fórum.","Detran.","Corpo de Bombeiros."],"Art. 91.","eca5a")
q(1,"No texto do acolhimento de urgência, o acolhimento sem ordem prévia é admitido em caráter excepcional e de",["urgência.","rotina.","lazer.","conveniência.","festa."],"Art. 93.","eca5b")
q(1,"No texto da unidade de internação, a reavaliação dos casos deve ocorrer em intervalo máximo de",["seis meses.","oito meses.","um ano.","dois anos.","três meses."],"Art. 94, XIV.","eca5c")
# n=2
q(2,"Entre os regimes de atendimento do art. 90 está a colocação",["familiar.","empresarial.","partidária.","religiosa.","sindical."],"Art. 90, III.")
q(2,"Os recursos destinados aos programas serão previstos nas dotações dos órgãos de Educação, Saúde e",["Assistência Social, entre outros.","Defesa, apenas.","Turismo, apenas.","Esporte, apenas.","Transporte, apenas."],"Art. 90, § 2º.")
q(2,"Para renovar a autorização de funcionamento dos programas, considera-se a qualidade e eficiência do trabalho, atestadas pelo Conselho Tutelar, pelo Ministério Público e pela",["Justiça da Infância e da Juventude.","imprensa.","Câmara.","Prefeitura, apenas.","escola."],"Art. 90, § 3º, II.")
q(2,"O Conselho Municipal comunicará o registro da entidade ao Conselho Tutelar e à",["autoridade judiciária da respectiva localidade.","Polícia Federal.","Receita.","Delegacia, apenas.","Assembleia."],"Art. 91.")
q(2,"Será negado o registro à entidade que esteja",["irregularmente constituída.","em prédio novo.","em bairro distante.","sem fins lucrativos.","com muitos funcionários."],"Art. 91, § 1º, c.")
q(2,"Será negado o registro à entidade que não apresente plano de trabalho compatível com os princípios da",["lei.","tradição.","igreja.","empresa.","imprensa."],"Art. 91, § 1º, b.")
q(2,"O Conselho Municipal, periodicamente, reavalia o cabimento da renovação do",["registro.","alvará.","contrato.","imóvel.","convênio."],"Art. 91, § 2º.")
q(2,"As entidades de acolhimento devem prezar pelo atendimento personalizado e em pequenos",["grupos.","prédios.","bairros.","contratos.","turnos."],"Art. 92, III.")
q(2,"A integração em família substituta ocorre quando esgotados os recursos de manutenção na família natural ou",["extensa.","vizinha.","escolar.","institucional.","comunitária."],"Art. 92, II.")
q(2,"As entidades de acolhimento devem evitar, sempre que possível, a transferência para outras entidades de crianças e adolescentes",["abrigados.","visitantes.","funcionários.","vizinhos.","doadores."],"Art. 92, VI.")
q(2,"As entidades de acolhimento só poderão receber recursos públicos se comprovado o atendimento dos princípios, exigências e finalidades da",["lei.","tradição.","igreja.","empresa.","imprensa."],"Art. 92, § 5º.")
q(2,"O descumprimento da lei pelo dirigente de entidade de acolhimento é causa de sua",["destituição.","promoção.","aposentadoria.","transferência.","licença."],"Art. 92, § 6º.")
q(2,"Recebida a comunicação do acolhimento de urgência, a autoridade judiciária ouve o",["Ministério Público.","prefeito.","delegado.","reitor.","síndico."],"Art. 93, parágrafo único.")
q(2,"Na internação, a entidade deve propiciar escolarização e",["profissionalização.","aposentadoria.","casamento.","emprego público.","viagem."],"Art. 94, X.")
q(2,"Na internação, a entidade deve oferecer atendimento personalizado em pequenas unidades e grupos",["reduzidos.","grandes.","fechados.","mistos, apenas.","anônimos."],"Art. 94, III.")
q(2,"Para as entidades governamentais, uma das medidas por descumprimento é o afastamento provisório de seus",["dirigentes.","funcionários.","alunos.","clientes.","vizinhos."],"Art. 97, I, b.")
q(2,"No texto do abrigo sem registro, a entidade que tenha irregularidade na constituição tem o registro",["negado.","aprovado.","dispensado.","adiado.","automático."],"Art. 91, § 1º, c.","eca5a")
q(2,"No texto do acolhimento de urgência, a comunicação ao juiz feita 10 horas depois está",["dentro do prazo de 24 horas.","fora do prazo.","dispensada.","antecipada demais.","irregular."],"Art. 93.","eca5b")
q(2,"No texto da unidade de internação, a entidade deve preservar os direitos que a decisão não tenha",["restringido.","previsto.","comentado.","julgado.","citado."],"Art. 94, II.","eca5c")
q(2,"As entidades de acolhimento devem promover a participação na vida da comunidade local e a preparação gradativa para o",["desligamento.","casamento.","emprego.","comércio.","exílio."],"Art. 92, VII e VIII.")
# n=3
q(3,"Assinale a alternativa correta sobre prazos e validades das entidades de atendimento.",["Registro: até quatro anos; reavaliação dos programas: até dois anos; relatório do acolhimento: até seis meses.","Registro: dois anos; reavaliação: um ano.","Registro: dez anos; relatório: um ano.","Registro: um ano; reavaliação: seis meses.","Registro: seis anos; relatório: dois anos."],"Arts. 90, § 3º, 91, § 2º, 92, § 2º.")
q(3,"Considere. I. A internação tem reavaliação a cada seis meses. II. O acolhimento de urgência é comunicado ao juiz em 24 horas. III. O registro vale por dez anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O registro vale no máximo quatro anos (art. 91, § 2º).")
q(3,"Assinale a INCORRETA.",["As entidades governamentais não precisam de inscrição dos programas.","As entidades não governamentais precisam de registro.","A fiscalização é do Judiciário, do MP e dos Conselhos Tutelares.","O dirigente do acolhimento é equiparado ao guardião.","A reavaliação dos programas é de no máximo dois anos."],"As entidades governamentais e não governamentais inscrevem os programas (art. 90, § 1º).")
q(3,"A medida de cassação do registro aplica-se às entidades",["não governamentais.","governamentais.","apenas às religiosas.","apenas às estrangeiras.","apenas às de pequeno porte."],"Art. 97, II, d.")
q(3,"O afastamento definitivo de dirigentes é medida aplicável às entidades",["governamentais.","não governamentais.","privadas.","religiosas.","estrangeiras."],"Art. 97, I, c.")
q(3,"A suspensão total ou parcial do repasse de verbas públicas é medida aplicável às entidades",["não governamentais.","governamentais.","públicas.","federais.","municipais."],"Art. 97, II, b.")
q(3,"Em caso de reiteradas infrações das entidades, o fato será comunicado ao Ministério Público ou representado perante autoridade judiciária, inclusive para suspensão das atividades ou",["dissolução da entidade.","promoção.","prêmio.","isenção.","licença."],"Art. 97, § 1º.")
q(3,"As pessoas jurídicas de direito público e as organizações não governamentais responderão pelos danos que seus agentes causarem às crianças, caracterizado o descumprimento dos",["princípios norteadores das atividades de proteção específica.","contratos.","orçamentos.","editais.","regimentos."],"Art. 97, § 2º.")
q(3,"No acolhimento de crianças de zero a três anos, dar-se-á especial atenção à atuação de educadores de referência",["estáveis e qualitativamente significativos.","rotativos.","voluntários.","temporários.","terceirizados."],"Art. 92, § 7º.")
q(3,"Os entes federados promoverão a permanente qualificação dos profissionais que atuam em programas de acolhimento, incluindo membros do Poder Judiciário, Ministério Público e",["Conselho Tutelar.","clubes.","sindicatos.","imprensa.","partidos."],"Art. 92, § 3º.")
q(3,"As entidades de acolhimento estimulam o contato da criança com seus pais e parentes, salvo determinação em contrário da autoridade",["judiciária competente.","policial.","tributária.","religiosa.","esportiva."],"Art. 92, § 4º.")
q(3,"A comunicação do acolhimento de urgência ao juiz é feita sob pena de",["responsabilidade.","prisão automática.","multa de trânsito.","perda do cargo, sempre.","demissão."],"Art. 93.")
q(3,"Na internação, a entidade deve oferecer assistência religiosa àqueles que desejarem, de acordo com suas",["crenças.","condições.","origens.","finanças.","profissões."],"Art. 94, XII.")
q(3,"Os dirigentes de entidade que desenvolve programa de acolhimento remetem relatório à autoridade para fins da reavaliação prevista no art. 19, § 1º, que trata do",["acolhimento.","trabalho.","esporte.","lazer.","comércio."],"Art. 92, § 2º.")
q(3,"No texto do abrigo sem registro, a conduta da associação é irregular porque o art. 91 exige o registro antes do",["funcionamento.","contrato.","aluguel.","nome.","cadastro."],"Art. 91.","eca5a")
q(3,"No texto do abrigo sem registro, a fiscalização cabe ao Judiciário, ao Ministério Público e aos",["Conselhos Tutelares.","prefeitos.","vereadores.","sindicatos.","bombeiros."],"Art. 95.","eca5a")
q(3,"No texto do acolhimento de urgência, após a comunicação ao juiz, a autoridade, ouvido o Ministério Público, promove a reintegração familiar ou o encaminhamento a programa de acolhimento ou a",["família substituta.","orfanato particular.","abrigo de rua.","escola.","delegacia."],"Art. 93, parágrafo único.","eca5b")
q(3,"No texto da unidade de internação, a restrição das visitas dos pais sem decisão violaria o dever de não restringir direito que não tenha sido objeto da decisão de",["internação.","adoção.","guarda.","tutela.","matrícula."],"Art. 94, II.","eca5c")
q(3,"No texto da unidade de internação, o prazo de oito meses sem reavaliação",["excede o máximo de seis meses.","é permitido.","é regra.","é recomendado.","é irrelevante."],"Art. 94, XIV.","eca5c")
q(3,"No texto do acolhimento de urgência, o abrigo, além de comunicar o juiz, acolhe a criança sem ordem prévia, o que é admitido pelo art.",["93.","91.","94.","95.","97."],"Art. 93.","eca5b")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("ECA: entidades de atendimento (arts. 90 a 97)",[
 ("reg","Regimes e programas",["oito regimes","inscrição no Conselho Municipal","reavaliação em 2 anos"],"seção 1"),
 ("rgs","Registro",["só após registro","negado por 5 motivos","validade: 4 anos"],"seção 2"),
 ("aco","Acolhimento",["princípios","dirigente = guardião","relatório a cada 6 meses"],"seção 3"),
 ("urg","Urgência",["sem ordem prévia","excepcional","juiz em 24 horas"],"seção 3"),
 ("int","Internação",["obrigações","reavaliação em 6 meses","capacitar para maus-tratos"],"seção 4"),
 ("fis","Fiscalização e medidas",["Judiciário, MP, Conselho Tutelar","governamentais: afastamento","não governamentais: cassação"],"seção 4")],
 "Na prova: prazos (24 horas, 6 meses, 2 e 4 anos) e quem fiscaliza")
aula_html=aula(LEAD,S,[1,2,3,4,5,6,7],QR,4,svg,"A primeira linha traz os programas e o registro; as demais, o acolhimento, a internação e as medidas.","Fontes: Edital 02/2026, Anexo I; Lei 8.069/1990 (ECA), arts. 90 a 97, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("eca-5","ECA: entidades de atendimento (arts. 90 a 97)",Q,list(tx),
 cobertura=["Cobertos os arts. 90 a 97. Do art. 90, § 2º e do art. 94, incisos XIII a XX não foram citados literalmente."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Trechos de lei copiados de fontes/eca.txt por programa.","Casos eca5a, eca5b e eca5c fictícios."],
 fontes_conferidas=["ECA, arts. 90 a 97: texto da Câmara, copiado por programa."])
gravar("eca-5",aula_html,banco("eca-5",Q),tx)
