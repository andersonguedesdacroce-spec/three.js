import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='idoso.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Os arts. 43 a 68 do Estatuto da Pessoa Idosa tratam do que acontece quando os direitos são ameaçados (medidas de proteção), de como o Estado organiza o atendimento (política de atendimento e entidades) e de como as entidades são fiscalizadas e punidas. A Vunesp cobra as hipóteses do art. 43, as medidas do art. 45, as linhas de ação do art. 47, os requisitos e princípios das entidades de longa permanência, as penalidades do art. 55, as multas administrativas e os prazos do procedimento (10 dias para a defesa, 24 horas para o auto)."
S={}
S[1]="## 1. Medidas de proteção\n\n"+L("art. 43","Art. 43. As medidas de proteção","CAPÍTULO II")+"\n\n"+L("arts. 44 e 45","Art. 44. As medidas de proteção","TÍTULO IV")+"""

As medidas de proteção são aplicáveis sempre que os direitos forem ameaçados ou violados por ação ou omissão da sociedade ou do Estado; por falta, omissão ou abuso da família, do curador ou da entidade de atendimento; ou em razão da condição pessoal da pessoa idosa. Podem ser aplicadas isolada ou cumulativamente, levando em conta os fins sociais e o fortalecimento dos vínculos familiares e comunitários.

O Ministério Público, ou o Judiciário a seu requerimento, pode determinar, entre outras, estas seis medidas: encaminhamento à família ou ao curador, mediante termo de responsabilidade; orientação, apoio e acompanhamento temporários; requisição para tratamento de saúde, em regime ambulatorial, hospitalar ou domiciliar; inclusão em programa de auxílio a usuários de drogas, da própria pessoa idosa ou de quem lhe cause perturbação; abrigo em entidade; e abrigo temporário.
"""
S[2]="## 2. Política de atendimento e entidades\n\n"+L("arts. 46 e 47","Art. 46. A política de atendimento","CAPÍTULO II DAS ENTIDADES")+"\n\n"+L("art. 48, caput","Art. 48. As entidades de atendimento são responsáveis","(“caput” do artigo")+"\n\n"+L("art. 48, parágrafo único","Parágrafo único. As entidades governamentais e não governamentais de assistência","Art. 49.")+"\n\n"+L("art. 49","Art. 49. As entidades que desenvolvam programas","Art. 50.")+"\n\n"+L("art. 50, I a XII","Art. 50. Constituem obrigações","XIII - providenciar")+"\n\n"+L("art. 51","Art. 51. As instituições filantrópicas","CAPÍTULO III")+"""

A política de atendimento é feita por ações governamentais e não governamentais articuladas da União, dos Estados, do Distrito Federal e dos Municípios. As linhas de ação são seis: políticas sociais básicas; assistência social em caráter supletivo; serviços especiais de prevenção e atendimento às vítimas de negligência, maus-tratos, exploração, abuso, crueldade e opressão; serviço de identificação e localização de parentes de pessoas idosas abandonadas em hospitais e instituições; proteção jurídico-social por entidades de defesa; e mobilização da opinião pública.

As entidades de atendimento inscrevem seus programas perante a Vigilância Sanitária e o Conselho Municipal da Pessoa Idosa (ou, na falta, o Estadual ou o Nacional), observados quatro requisitos: instalações adequadas, objetivos estatutários e plano de trabalho compatíveis, regular constituição e idoneidade dos dirigentes. As entidades de longa permanência seguem seis princípios, e o dirigente responde civil e criminalmente pelos atos em detrimento da pessoa idosa. Entre as obrigações das entidades estão o contrato escrito, o vestuário adequado (se pública), a alimentação suficiente e a comunicação ao Ministério Público da situação de abandono moral ou material. As instituições filantrópicas ou sem fins lucrativos têm direito à assistência judiciária gratuita.
"""
S[3]="## 3. Fiscalização, penalidades e infrações administrativas\n\n"+L("arts. 52 e 54","Art. 52. As entidades governamentais e não governamentais de atendimento","Art. 53.")+"\n\n"+L("art. 55, caput","Art. 55. As entidades de atendimento que descumprirem","§ 1º Havendo danos")+"\n\n"+L("arts. 56 a 58","Art. 56. Deixar a entidade de atendimento","CAPÍTULO V")+"""

As entidades são fiscalizadas pelos Conselhos da Pessoa Idosa, pelo Ministério Público, pela Vigilância Sanitária e por outros previstos em lei, e dão publicidade às prestações de contas. Para as entidades governamentais, as penalidades são advertência, afastamento provisório ou definitivo dos dirigentes e fechamento de unidade ou interdição de programa; para as não governamentais, advertência, multa, suspensão parcial ou total do repasse de verbas públicas, interdição de unidade ou suspensão de programa e proibição de atendimento a pessoas idosas.

As infrações administrativas têm multa: descumprir as obrigações do art. 50, de R$ 500,00 a R$ 3.000,00, com possível interdição; o profissional de saúde ou o responsável por estabelecimento que deixar de comunicar à autoridade os crimes contra a pessoa idosa, de R$ 500,00 a R$ 3.000,00, em dobro na reincidência; e descumprir a prioridade de atendimento, de R$ 500,00 a R$ 1.000,00, mais multa civil estipulada pelo juiz. Os valores são atualizados anualmente.
"""
S[4]="## 4. Apuração das infrações\n\n"+L("arts. 59 e 60","Art. 59. Os valores monetários","§ 1º No procedimento iniciado")+"\n\n"+L("arts. 61 a 63","Art. 61. O autuado terá prazo","CAPÍTULO VI")+"\n\n"+L("arts. 65 a 67","Art. 65. O procedimento de apuração","Art. 68.")+"\n\n"+L("art. 68, §§ 1º e 2º","§ 1º Salvo manifestação em audiência","§ 3º Antes de aplicar")+"""

O procedimento administrativo começa com requisição do Ministério Público ou com auto de infração elaborado por servidor efetivo e assinado, se possível, por duas testemunhas. O autuado tem dez dias para a defesa, contados da intimação, feita pelo autuante, no próprio auto se lavrado na presença do infrator, ou por via postal com aviso de recebimento. Havendo risco para a vida ou a saúde da pessoa idosa, a autoridade aplica as sanções regulamentares, sem prejuízo das providências do Ministério Público.

A apuração judicial começa por petição fundamentada de pessoa interessada ou por iniciativa do Ministério Público. Havendo motivo grave, o juiz, ouvido o Ministério Público, pode decretar liminarmente o afastamento provisório do dirigente. O dirigente é citado para responder por escrito em dez dias; depois da defesa, o juiz decide ou designa audiência, e as partes têm cinco dias para as alegações finais, decidindo o juiz em igual prazo. No afastamento de dirigente de entidade governamental, a autoridade superior tem 24 horas para a substituição.
"""
S[5]="""## 6. Na rotina do guarda

- **Pessoa idosa em risco:** o guarda comunica o Ministério Público e a rede de proteção; as medidas do art. 45 são do Ministério Público ou do Judiciário.
- **Entidade de longa permanência:** o guarda comunica irregularidades à Vigilância Sanitária, ao Conselho da Pessoa Idosa ou ao Ministério Público.
- **Abandono em hospital:** o serviço de identificação e localização de parentes é linha de ação da política de atendimento.
- **Violência:** a omissão do profissional de saúde em comunicar crime contra a pessoa idosa é infração administrativa.
- **Prioridade:** o descumprimento da prioridade no atendimento gera multa.
"""
S[6]="""## 7. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Hipóteses do art. 43 | Sociedade ou Estado; família, curador ou entidade; condição pessoal |
| Quem aplica as medidas do art. 45 | Ministério Público ou Judiciário a requerimento dele |
| Medidas do art. 45 | Seis: família, orientação, tratamento, drogas, abrigo em entidade, abrigo temporário |
| Linhas de ação | Seis |
| Requisitos de inscrição | Quatro |
| Princípios das entidades de longa permanência | Seis |
| Penalidades governamentais x não governamentais | Governamentais: afastamento; não governamentais: multa, suspensão do repasse, proibição |
| Multas | R$ 500 a R$ 3.000 (arts. 56 e 57); R$ 500 a R$ 1.000 (art. 58) |
| Prazo da defesa | Dez dias |
| Auto de infração | Servidor efetivo; duas testemunhas se possível; 24 horas |
"""
S[7]="""## 8. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 43 | Hipóteses de aplicação das medidas |
| Art. 45 | Seis medidas pelo MP ou Judiciário |
| Art. 47 | Seis linhas de ação |
| Art. 48 | Inscrição no Conselho e na Vigilância Sanitária; quatro requisitos |
| Art. 49 | Seis princípios; dirigente responde civil e criminalmente |
| Art. 50 | Obrigações, com contrato escrito |
| Art. 52 | Fiscalização: Conselhos, MP, Vigilância Sanitária |
| Art. 55 | Penalidades distintas para governamentais e não governamentais |
| Arts. 56 a 58 | Multas administrativas |
| Art. 61 | Defesa em dez dias |
| Art. 68 | Alegações finais em cinco dias |
"""
QR=[("Questão 1","As medidas de proteção à pessoa idosa são aplicáveis sempre que os direitos reconhecidos no Estatuto forem ameaçados ou violados por ação ou omissão da sociedade ou do",["Estado.","comércio.","clube.","vizinho.","sindicato."],0,"Art. 43, I."),
("Questão 2","O autuado terá prazo para a apresentação da defesa de",["dez dias, contado da data da intimação.","cinco dias.","vinte dias.","trinta dias.","quarenta e oito horas."],1,"Art. 61."),
("Questão 3","Deixar de cumprir as determinações do Estatuto sobre a prioridade no atendimento à pessoa idosa sujeita à multa de R$ 500,00 a",["R$ 1.000,00, e multa civil a ser estipulada pelo juiz.","R$ 3.000,00.","R$ 5.000,00.","R$ 10.000,00.","R$ 700,00."],2,"Art. 58."),
("Questão 4","As entidades de atendimento celebrarão contrato escrito de prestação de serviço com a pessoa idosa, especificando o tipo de atendimento, as obrigações da entidade e os respectivos",["preços, se for o caso.","nomes dos funcionários.","horários de visita.","fornecedores.","padrões de uniforme."],3,"Art. 50, I.")]
t1="<strong>Abandono no hospital</strong><br><br>Uma senhora de 78 anos foi deixada num hospital de Vila Nova, cidade fictícia, sem documentos, e ninguém a procurou. A assistente social pediu ajuda à guarda."
t2="<strong>Casa de repouso</strong><br><br>A Guarda Municipal recebeu denúncia de que numa casa de repouso de Vila Nova a comida era insuficiente e não havia contrato escrito com os residentes."
t3="<strong>Hospital que não comunicou</strong><br><br>O responsável por um hospital privado de Vila Nova soube que um paciente idoso sofria maus-tratos e nada comunicou à autoridade competente."
tx={"idoso2a":t1,"idoso2b":t2,"idoso2c":t3}
# n=1
q(1,"As medidas de proteção à pessoa idosa são aplicáveis sempre que os direitos reconhecidos no Estatuto forem",["ameaçados ou violados.","ignorados pela vítima.","debatidos.","citados.","votados."],"Art. 43.")
q(1,"As medidas de proteção podem ser aplicadas isolada ou",["cumulativamente.","alternadamente.","retroativamente.","eventualmente.","anualmente."],"Art. 44.")
q(1,"Verificada a hipótese do art. 43, o Ministério Público poderá determinar o encaminhamento à família ou ao curador, mediante termo de",["responsabilidade.","adoção.","guarda.","tutela.","quitação."],"Art. 45, I.")
q(1,"Entre as medidas do art. 45 está o abrigo",["em entidade.","em hotel.","em escola.","em quartel.","em presídio."],"Art. 45, V.")
q(1,"A política de atendimento à pessoa idosa far-se-á por meio do conjunto articulado de ações governamentais e",["não governamentais.","particulares apenas.","militares.","judiciais apenas.","partidárias."],"Art. 46.")
q(1,"É linha de ação da política de atendimento o serviço de identificação e localização de parentes ou responsáveis por pessoas idosas abandonadas em hospitais e instituições de",["longa permanência.","ensino.","lazer.","comércio.","turismo."],"Art. 47, IV.")
q(1,"As entidades de atendimento inscrevem os programas perante a Vigilância Sanitária e o Conselho Municipal da",["Pessoa Idosa.","Criança.","Saúde.","Educação.","Cultura."],"Art. 48, parágrafo único.")
q(1,"Entre os requisitos de inscrição das entidades está estar regularmente",["constituída.","fechada.","isenta.","registrada na polícia.","aposentada."],"Art. 48, parágrafo único, III.")
q(1,"As entidades de longa permanência adotam o princípio da preservação dos vínculos",["familiares.","comerciais.","políticos.","religiosos.","partidários."],"Art. 49, I.")
q(1,"O dirigente de instituição de atendimento à pessoa idosa responderá civil e criminalmente pelos atos que praticar em detrimento da",["pessoa idosa.","entidade.","comunidade.","prefeitura.","imprensa."],"Art. 49, parágrafo único.")
q(1,"As instituições filantrópicas ou sem fins lucrativos prestadoras de serviço às pessoas idosas terão direito à assistência",["judiciária gratuita.","tributária.","médica.","bancária.","imobiliária."],"Art. 51.")
q(1,"As entidades de atendimento serão fiscalizadas pelos Conselhos da Pessoa Idosa, Ministério Público, Vigilância Sanitária e outros previstos em",["lei.","costume.","contrato.","convênio.","sentença."],"Art. 52.")
q(1,"Será dada publicidade das prestações de contas dos recursos públicos e privados recebidos pelas",["entidades de atendimento.","famílias.","prefeituras.","escolas.","empresas."],"Art. 54.")
q(1,"Para as entidades governamentais, uma das penalidades é a advertência e o afastamento provisório de seus",["dirigentes.","funcionários.","usuários.","fornecedores.","vizinhos."],"Art. 55, I.")
q(1,"A multa é penalidade aplicável às entidades",["não governamentais.","governamentais.","apenas às federais.","apenas às municipais.","nenhuma delas."],"Art. 55, II, b.")
q(1,"O procedimento administrativo de imposição de penalidade tem início com requisição do Ministério Público ou auto de infração elaborado por servidor",["efetivo.","comissionado.","terceirizado.","voluntário.","estagiário."],"Art. 60.")
q(1,"O dirigente da entidade será citado para, no prazo de dez dias, oferecer resposta",["escrita.","oral.","gravada.","telefônica.","tácita."],"Art. 67.")
q(1,"No texto do abandono no hospital, o serviço de identificação e localização de parentes é linha de ação da política de",["atendimento.","trânsito.","tributos.","educação, apenas.","defesa."],"Art. 47, IV.","idoso2a")
q(1,"No texto da casa de repouso, a ausência de contrato escrito descumpre o art. 50, inciso",["I.","II.","III.","V.","XV."],"Art. 50, I.","idoso2b")
q(1,"No texto do hospital que não comunicou, a omissão é infração administrativa sujeita a multa de R$ 500,00 a",["R$ 3.000,00.","R$ 1.000,00.","R$ 5.000,00.","R$ 700,00.","R$ 10.000,00."],"Art. 57.","idoso2c")
# n=2
q(2,"As medidas de proteção levam em conta os fins sociais e o fortalecimento dos vínculos familiares e",["comunitários.","políticos.","comerciais.","religiosos.","sindicais."],"Art. 44.")
q(2,"A inclusão em programa de auxílio a usuários de drogas pode ser da própria pessoa idosa ou da pessoa de sua convivência que lhe cause",["perturbação.","alegria.","renda.","visita.","aprendizado."],"Art. 45, IV.")
q(2,"Entre as medidas do art. 45 está a requisição para tratamento de saúde em regime ambulatorial, hospitalar ou",["domiciliar.","prisional.","escolar.","comercial.","militar."],"Art. 45, III.")
q(2,"A assistência social, entre as linhas de ação do art. 47, é prestada em caráter",["supletivo, para aqueles que necessitarem.","principal.","exclusivo.","obrigatório para todos.","eventual."],"Art. 47, II.")
q(2,"As políticas sociais básicas citadas no art. 47 estão previstas na Lei",["8.842, de 1994.","8.069, de 1990.","11.340, de 2006.","9.503, de 1997.","13.675, de 2018."],"Art. 47, I.")
q(2,"As entidades de longa permanência adotam o princípio da manutenção da pessoa idosa na mesma instituição, salvo em caso de",["força maior.","vontade do dirigente.","falta de vaga.","férias.","moda."],"Art. 49, III.")
q(2,"As entidades devem fornecer vestuário adequado, se for pública, e alimentação",["suficiente.","luxuosa.","vegetariana.","opcional.","eventual."],"Art. 50, III.")
q(2,"As entidades comunicam ao Ministério Público a situação de abandono moral ou material por parte dos",["familiares.","vizinhos.","funcionários.","clientes.","políticos."],"Art. 50, XVI.")
q(2,"As entidades devem manter no quadro de pessoal profissionais com formação",["específica.","genérica.","superior apenas.","militar.","religiosa."],"Art. 50, XVII.")
q(2,"Havendo danos às pessoas idosas abrigadas ou fraude, caberá o afastamento provisório dos dirigentes ou a interdição da unidade e a suspensão do",["programa.","contrato.","aluguel.","imposto.","convênio."],"Art. 55, § 1º.")
q(2,"A suspensão do repasse de verbas públicas ocorrerá quando verificada má aplicação ou desvio de finalidade dos",["recursos.","imóveis.","funcionários.","contratos.","veículos."],"Art. 55, § 2º.")
q(2,"Na aplicação das penalidades são consideradas a natureza e a gravidade da infração, os danos, as circunstâncias agravantes ou atenuantes e os antecedentes da",["entidade.","pessoa idosa.","vizinhança.","prefeitura.","imprensa."],"Art. 55, § 4º.")
q(2,"No caso de interdição de estabelecimento de longa permanência, as pessoas idosas serão transferidas para outra instituição, a expensas do estabelecimento",["interditado.","vizinho.","público.","federal.","privado."],"Art. 56, parágrafo único.")
q(2,"A multa do art. 57 é aplicada em dobro no caso de",["reincidência.","dolo.","culpa.","ação coletiva.","pedido."],"Art. 57.")
q(2,"Os valores monetários expressos no Capítulo IV serão atualizados",["anualmente.","semestralmente.","a cada dois anos.","a cada cinco anos.","nunca."],"Art. 59.")
q(2,"O auto de infração, sempre que possível, é assinado por duas",["testemunhas.","autoridades.","empresas.","famílias.","advogados."],"Art. 60.")
q(2,"No texto do abandono no hospital, a pessoa idosa abandonada pode ser objeto de medida como o encaminhamento à família ou ao curador, ou o",["abrigo temporário.","abrigo permanente apenas.","internação psiquiátrica.","prisão.","exílio."],"Art. 45, VI.","idoso2a")
q(2,"No texto da casa de repouso, a comida insuficiente descumpre o art. 50, que exige alimentação",["suficiente.","regional.","vegetariana.","opcional.","diária apenas."],"Art. 50, III.","idoso2b")
q(2,"No texto do hospital que não comunicou, a conduta do responsável configura a infração do art.",["57.","56.","58.","55.","54."],"Art. 57.","idoso2c")
q(2,"O art. 52 atribui a fiscalização das entidades de atendimento, entre outros, ao Ministério Público e à",["Vigilância Sanitária.","Receita Federal.","Polícia Rodoviária.","Junta Comercial.","Capitania dos Portos."],"Art. 52.")
# n=3
q(3,"Assinale a alternativa correta sobre as multas administrativas.",["Art. 56: R$ 500 a R$ 3.000; art. 57: R$ 500 a R$ 3.000, em dobro na reincidência; art. 58: R$ 500 a R$ 1.000 mais multa civil.","Art. 56: R$ 100 a R$ 500.","Art. 57: R$ 1.000 a R$ 10.000.","Art. 58: R$ 3.000 a R$ 5.000.","Art. 58 não prevê multa civil."],"Arts. 56 a 58.")
q(3,"Considere. I. As medidas do art. 45 são determinadas pelo Ministério Público ou pelo Judiciário. II. O autuado tem 10 dias para a defesa. III. As penalidades das entidades governamentais incluem multa. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"A multa é penalidade das entidades não governamentais (art. 55, II).")
q(3,"Assinale a INCORRETA.",["O dirigente de entidade não responde civil e criminalmente por atos contra a pessoa idosa.","O art. 45 prevê seis medidas.","O auto pode ser lavrado em 24 horas por motivo justificado.","A defesa é apresentada em dez dias.","O afastamento liminar do dirigente exige motivo grave."],"O dirigente responde civil e criminalmente (art. 49, parágrafo único).")
q(3,"Havendo motivo grave, a autoridade judiciária, ouvido o Ministério Público, poderá decretar liminarmente o afastamento provisório do dirigente da entidade, mediante decisão",["fundamentada.","verbal.","sigilosa.","do Conselho.","da Vigilância."],"Art. 66.")
q(3,"Após a defesa, as partes e o Ministério Público têm, salvo manifestação em audiência, para as alegações finais, o prazo de",["cinco dias.","dez dias.","vinte e quatro horas.","quinze dias.","trinta dias."],"Art. 68, § 1º.")
q(3,"No afastamento de dirigente de entidade governamental, a autoridade administrativa imediatamente superior tem para proceder à substituição o prazo de",["vinte e quatro horas.","cinco dias.","dez dias.","quarenta e oito horas.","trinta dias."],"Art. 68, § 2º.")
q(3,"A multa e a advertência serão impostas ao dirigente da entidade ou ao responsável pelo programa de",["atendimento.","trânsito.","educação.","lazer.","saúde."],"Art. 68, § 4º.")
q(3,"Antes de aplicar qualquer das medidas, a autoridade judiciária poderá fixar prazo para a remoção das irregularidades; satisfeitas as exigências, o processo será extinto sem julgamento do",["mérito.","réu.","prazo.","juiz.","recurso."],"Art. 68, § 3º.")
q(3,"A intimação do autuado é feita pelo autuante no instrumento de autuação, quando lavrado na presença do infrator, ou por via",["postal, com aviso de recebimento.","telefônica.","verbal.","de edital apenas.","de jornal."],"Art. 61.")
q(3,"Havendo risco para a vida ou a saúde da pessoa idosa, a autoridade competente aplicará à entidade as",["sanções regulamentares.","medidas de proteção do art. 45.","penas do Código Penal.","multas do Código de Trânsito.","medidas socioeducativas."],"Art. 62.")
q(3,"O procedimento de apuração judicial começa por petição fundamentada de pessoa interessada ou iniciativa do",["Ministério Público.","Detran.","Prefeito.","Conselho de Classe.","Sindicato."],"Art. 65.")
q(3,"Aplicam-se subsidiariamente ao procedimento administrativo as Leis 6.437/1977 e",["9.784/1999.","8.069/1990.","11.340/2006.","10.406/2002.","13.869/2019."],"Art. 64.")
q(3,"A proibição de atendimento a pessoas idosas a bem do interesse público é penalidade aplicável às entidades",["não governamentais.","governamentais.","apenas às federais.","apenas às estaduais.","nenhuma."],"Art. 55, II, e.")
q(3,"Havendo infração por entidade que coloque em risco os direitos assegurados, o fato será comunicado ao Ministério Público, que poderá promover a suspensão das atividades ou a",["dissolução da entidade.","promoção do dirigente.","isenção de tributos.","anistia.","fusão."],"Art. 55, § 3º.")
q(3,"No texto da casa de repouso, a ausência de contrato escrito e a comida insuficiente podem levar à multa de",["R$ 500,00 a R$ 3.000,00, com possível interdição.","R$ 100,00.","R$ 10.000,00.","R$ 700,00.","advertência apenas."],"Art. 56.","idoso2b")
q(3,"No texto da casa de repouso, a denúncia à guarda deve ser encaminhada, entre outros, ao",["Ministério Público e à Vigilância Sanitária.","Detran.","Sindicato.","Clube.","Banco."],"Art. 52.","idoso2b")
q(3,"No texto do hospital que não comunicou, a multa é aplicada em dobro no caso de",["reincidência.","dolo.","culpa.","dano maior.","pedido da vítima."],"Art. 57.","idoso2c")
q(3,"No texto do hospital que não comunicou, o dever de comunicar recai sobre o profissional de saúde ou o responsável por estabelecimento de",["saúde ou instituição de longa permanência.","apenas hospital público.","apenas clínica.","apenas escola.","apenas asilo."],"Art. 57.","idoso2c")
q(3,"No texto do abandono no hospital, o abrigo temporário é uma das medidas do art.",["45.","43.","44.","47.","50."],"Art. 45, VI.","idoso2a")
q(3,"No texto do abandono no hospital, a medida aplicável é determinada pelo Ministério Público ou pelo",["Poder Judiciário, a requerimento daquele.","delegado.","prefeito.","guarda.","hospital."],"Art. 45.","idoso2a")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Estatuto da Pessoa Idosa: proteção e atendimento (arts. 43 a 68)",[
 ("med","Medidas de proteção",["art. 43: hipóteses","art. 45: seis medidas","MP ou Judiciário"],"seção 1"),
 ("pol","Política de atendimento",["ações articuladas","seis linhas de ação","busca de parentes"],"seção 2"),
 ("ent","Entidades",["inscrição e requisitos","princípios","obrigações e contrato"],"seção 2"),
 ("fis","Fiscalização",["Conselhos, MP, Vigilância","penalidades","governamentais x não"],"seção 3"),
 ("inf","Infrações",["R$ 500 a 3.000","R$ 500 a 1.000","prioridade"],"seção 3"),
 ("apu","Apuração",["defesa: 10 dias","auto em 24 horas","alegações em 5 dias"],"seção 4")],
 "Na prova: números das multas e prazos; diferença entre entidade governamental e não governamental")
aula_html=aula(LEAD,S,[1,2,3,4,'QR',5,6,7],QR,5,svg,"A primeira linha traz as medidas de proteção e a política; as demais, a fiscalização, as infrações e a apuração.","Fontes: Edital 02/2026, Anexo I; Lei 10.741/2003 (Estatuto da Pessoa Idosa), arts. 43 a 68, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("idoso-2","Estatuto da Pessoa Idosa: medidas de proteção e política de atendimento (arts. 43 a 68)",Q,list(tx),
 cobertura=["Cobertos: arts. 43 a 68, exceto o art. 53 (altera a Lei 8.842/1994), o art. 60, §§ 1º e 2º, o art. 63 e o art. 68, § 3º (apenas citado)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","Os valores das multas são atualizados anualmente (art. 59); conferir no Planalto.","Trechos de lei copiados de fontes/idoso.txt por programa.","Casos idoso2a, idoso2b e idoso2c fictícios."],
 fontes_conferidas=["Estatuto da Pessoa Idosa, arts. 43 a 68: texto da Câmara, copiado por programa."])
gravar("idoso-2",aula_html,banco("idoso-2",Q),tx)
