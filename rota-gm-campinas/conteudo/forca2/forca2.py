import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='forca2.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="O Decreto 12.341/2024 regulamenta o uso da força pelos profissionais de segurança pública. Ele traz os sete princípios gerais (legalidade, precaução, necessidade, proporcionalidade, razoabilidade, responsabilização e não discriminação), as diretrizes do uso diferenciado da força, a regra de que a arma de fogo é medida de último recurso, a capacitação anual obrigatória e as regras de registro e de controle. A Vunesp cobra o texto do decreto com rigor: os sete princípios, o relatório circunstanciado quando há ferimento ou morte e o mínimo de dois instrumentos de menor potencial ofensivo por profissional em serviço."
S={}
S[1]="## 1. Objeto e princípios\n\n"+L("art. 1º","Art. 1º Este Decreto disciplina","Art. 2º")+"\n\n"+L("art. 2º, caput","Art. 2º São princípios gerais","Parágrafo único. O uso da força")+"\n\n"+L("art. 2º, parágrafo único","Parágrafo único. O uso da força em segurança pública deverá","CAPÍTULO II")+"""

O decreto disciplina o uso da força e dos instrumentos de menor potencial ofensivo pelos profissionais de segurança pública, com vistas à eficiência, à transparência, à valorização dos profissionais e ao respeito aos direitos humanos. São sete os princípios gerais: legalidade, precaução, necessidade, proporcionalidade, razoabilidade, responsabilização e não discriminação.

As diretrizes gerais determinam que a força só pode ocorrer para um objetivo legal e nos estritos limites da lei; que as operações devem ser planejadas para prevenir ou minimizar o uso da força; que um recurso de força só é empregado quando outros de menor intensidade não bastam; que o nível da força é compatível com a gravidade da ameaça; que a força é empregada com bom senso, prudência e equilíbrio; que órgãos e profissionais assumem a responsabilidade pelo uso inadequado, após processo com devido processo legal, ampla defesa e contraditório; e que a atuação é não discriminatória.
"""
S[2]="## 2. Uso diferenciado da força e capacitação\n\n"+L("art. 3º","Art. 3º A força deverá ser utilizada","CAPÍTULO III")+"\n\n"+L("art. 4º","Art. 4º Na capacitação de profissionais","CAPÍTULO IV")+"""

A força é utilizada de forma diferenciada, com a seleção apropriada do nível a ser empregado, em resposta a uma ameaça real ou potencial, minimizando o uso de meios que possam causar ofensas, ferimentos ou mortes. Os profissionais priorizam a comunicação, a negociação e as técnicas que impeçam uma escalada da violência. O emprego de arma de fogo é medida de último recurso, e não é legítimo contra pessoa em fuga desarmada ou sem risco imediato, nem contra veículo que desrespeite bloqueio, exceto risco de morte ou lesão. O emprego de arma de fogo ou instrumento de menor potencial ofensivo é restrito aos profissionais habilitados. Sempre que o uso da força resultar em ferimento ou morte, deve ser elaborado relatório circunstanciado.

Na capacitação, os órgãos observam a obrigatoriedade e a periodicidade anual, a realização no horário de serviço e a adoção de conteúdo sobre o emprego adequado de armas de fogo e de instrumentos de menor potencial ofensivo.
"""
S[3]="## 3. Implementação, controle e monitoramento\n\n"+L("art. 6º","Art. 6º Para implementação do disposto","CAPÍTULO V")+"\n\n"+L("art. 7º","Art. 7º São diretrizes para atuação","Art. 8º")+"\n\n"+L("art. 8º, caput","Art. 8º Ato do Ministro","§ 1º O ato de que trata")+"\n\n"+L("arts. 9º e 10","Art. 9º O repasse de recursos","Art. 11.")+"""

Os órgãos de segurança pública devem elaborar atos normativos sobre o uso diferenciado da força; registrar e publicar dados sobre o uso da força; disponibilizar equipamento de proteção individual e, no mínimo, dois instrumentos de menor potencial ofensivo a todo profissional em serviço; instituir programas de atenção à saúde mental dos profissionais em ocorrências de alto risco; reduzir a vitimização dos profissionais e a letalidade policial; normatizar a identificação dos profissionais, para individualizar suas ações; e normatizar a atuação em gerenciamento de crises, busca pessoal e domiciliar, uso de algemas e providências nos casos de lesão ou morte.

Os mecanismos de controle garantem transparência e acesso a dados, canais de denúncia, processamento eficaz das reclamações e fortalecimento das corregedorias e ouvidorias. As ocorrências são registradas quando resultarem em lesão corporal ou morte ou envolverem o emprego de armas ou instrumentos em ambientes prisionais. O Comitê Nacional de Monitoramento do Uso da Força (CNMUDF) é instituído por ato do Ministro da Justiça e Segurança Pública. O repasse de recursos do Fundo Nacional de Segurança Pública e do Funpen às polícias estaduais e municipais depende da observância da Lei 13.060/2014 e do decreto.
"""
S[5]="""## 5. Na rotina do guarda

- **Comunicação antes da força:** o guarda prioriza a comunicação e a negociação, para impedir a escalada da violência.
- **Último recurso:** a arma de fogo só é usada como medida de último recurso.
- **Relatório:** se o uso da força causar ferimento ou morte, o guarda elabora relatório circunstanciado.
- **Capacitação anual:** a capacitação sobre uso da força é obrigatória, anual e feita no horário de serviço.
- **Equipamento:** todo guarda em serviço deve ter equipamento de proteção individual e, no mínimo, dois instrumentos de menor potencial ofensivo.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Princípios gerais | Sete: legalidade, precaução, necessidade, proporcionalidade, razoabilidade, responsabilização, não discriminação |
| Arma de fogo | Medida de último recurso |
| Priorizar | Comunicação, negociação, técnicas que impeçam escalada |
| Relatório circunstanciado | Sempre que o uso da força resultar em ferimento ou morte |
| Capacitação | Obrigatória, anual, no horário de serviço |
| Instrumentos por profissional | No mínimo dois instrumentos de menor potencial ofensivo |
| Identificação | Normatização e fiscalização para individualizar ações |
| Comitê Nacional | CNMUDF, por ato do Ministro da Justiça e Segurança Pública |
| Registro de ocorrências | Lesão corporal ou morte; armas ou instrumentos em ambientes prisionais |
| Repasse de recursos | Condicionado à Lei 13.060/2014 e ao decreto |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 1º | Eficiência, transparência, valorização, direitos humanos |
| Art. 2º | Sete princípios e sete diretrizes |
| Art. 3º | Uso diferenciado; arma de fogo é último recurso |
| Art. 4º | Capacitação anual no horário de serviço |
| Art. 5º | Competências do Ministério da Justiça |
| Art. 6º | Diretrizes aos órgãos; dois instrumentos por profissional |
| Art. 7º | Controle, ouvidorias e registro |
| Art. 8º | Comitê Nacional (CNMUDF) |
| Art. 9º | Repasse condicionado |
| Art. 10 | Normas complementares do Ministro |
"""
QR=[("Questão 1","Entre os princípios gerais de uso da força em segurança pública estão a legalidade, a precaução, a necessidade, a proporcionalidade, a razoabilidade, a responsabilização e a",["não discriminação.","impunidade.","celeridade.","economicidade.","eficiência."],0,"Art. 2º."),
("Questão 2","O emprego de arma de fogo será medida de",["último recurso.","primeiro recurso.","rotina.","opção livre.","regra."],1,"Art. 3º, § 2º."),
("Questão 3","Sempre que o uso da força resultar em ferimento ou morte, deverá ser elaborado",["relatório circunstanciado.","boletim simples.","aviso verbal.","recibo.","edital."],2,"Art. 3º, § 5º."),
("Questão 4","Na capacitação sobre o uso da força, a periodicidade é",["anual.","mensal.","semestral.","bienal.","eventual."],3,"Art. 4º, I.")]
t1="<strong>Negociação na praça</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, abordou um homem alterado que ameaçava as pessoas com uma garrafa quebrada. O guarda conversou, pediu calma e evitou o confronto."
t2="<strong>Ferimento na ocorrência</strong><br><br>Durante a contenção de um agressor, o guarda de Vila Nova usou um instrumento de menor potencial ofensivo, e o homem sofreu uma lesão."
t3="<strong>Equipamento do guarda</strong><br><br>A administração da Guarda de Vila Nova entregou a cada guarda uma arma de fogo, mas nenhum instrumento de menor potencial ofensivo."
tx={"forca2a":t1,"forca2b":t2,"forca2c":t3}
# n=1
q(1,"O Decreto 12.341/2024 disciplina o uso da força e dos instrumentos de menor potencial ofensivo pelos profissionais de segurança",["pública.","privada.","penitenciária.","escolar.","comunitária."],"Art. 1º.")
q(1,"O decreto busca promover eficiência, transparência, valorização dos profissionais e respeito aos direitos",["humanos.","civis.","empresariais.","tributários.","comerciais."],"Art. 1º.")
q(1,"Um dos princípios gerais de uso da força é a",["precaução.","pessoalidade.","oportunidade.","discricionariedade.","prescrição."],"Art. 2º, II.")
q(1,"Um dos princípios gerais de uso da força é a responsabilização, e outro é a não",["discriminação.","comunicação.","investigação.","penalização.","aplicação."],"Art. 2º, VII.")
q(1,"A força somente poderá ocorrer para a consecução de um objetivo legal e nos estritos limites da",["lei.","vontade do agente.","ordem verbal.","urgência.","opinião pública."],"Art. 2º, parágrafo único, I.")
q(1,"Um recurso de força somente poderá ser empregado quando outros recursos de menor intensidade não forem",["suficientes.","disponíveis.","baratos.","rápidos.","novos."],"Art. 2º, parágrafo único, III.")
q(1,"A força deve ser empregada com bom senso, prudência e",["equilíbrio.","rigor.","pressa.","sigilo.","ordem."],"Art. 2º, parágrafo único, V.")
q(1,"A força deverá ser utilizada de forma",["diferenciada.","padronizada.","constante.","máxima.","imprevisível."],"Art. 3º.")
q(1,"Os profissionais deverão priorizar a comunicação, a negociação e o emprego de técnicas que impeçam uma escalada da",["violência.","dívida.","investigação.","crise econômica.","pena."],"Art. 3º, § 1º.")
q(1,"O emprego de arma de fogo ou de instrumento de menor potencial ofensivo deverá ser restrito aos profissionais devidamente",["habilitados.","contratados.","nomeados.","indicados.","registrados."],"Art. 3º, § 4º.")
q(1,"A capacitação sobre uso da força deve ser realizada no horário de",["serviço.","folga.","férias.","almoço.","descanso."],"Art. 4º, II.")
q(1,"As diretrizes da implementação incluem o registro e a publicação de dados sobre o uso da",["força.","verba.","viatura.","arma.","escala."],"Art. 6º, II.")
q(1,"Os órgãos devem disponibilizar, a todo profissional em serviço, equipamento de proteção individual e, no mínimo, dois instrumentos de menor potencial",["ofensivo.","lesivo.","letal.","defensivo.","pesado."],"Art. 6º, III.")
q(1,"Entre as diretrizes está a instituição de programas continuados de atenção à saúde mental dos profissionais que se envolvam em ocorrências de alto",["risco.","custo.","tempo.","valor.","volume."],"Art. 6º, IV.")
q(1,"As ocorrências do uso da força são registradas quando resultarem em lesão corporal ou",["morte.","atraso.","multa.","protesto.","prisão."],"Art. 7º, parágrafo único, I.")
q(1,"O Comitê Nacional de Monitoramento do Uso da Força é instituído por ato do Ministro de Estado da Justiça e Segurança",["Pública.","Privada.","Social.","Civil.","Militar."],"Art. 8º.")
q(1,"O repasse de recursos do Fundo Nacional de Segurança Pública está condicionado à observância da Lei 13.060/2014 e deste",["Decreto.","contrato.","convênio.","manual.","regimento."],"Art. 9º.")
q(1,"No texto da negociação na praça, a conversa para evitar o confronto cumpre a diretriz de priorizar a",["comunicação e a negociação.","força máxima.","fuga.","omissão.","vingança."],"Art. 3º, § 1º.","forca2a")
q(1,"No texto do ferimento na ocorrência, o guarda deve elaborar",["relatório circunstanciado.","edital.","aviso.","contrato.","recibo."],"Art. 3º, § 5º.","forca2b")
q(1,"No texto do equipamento do guarda, falta ao guarda o mínimo de",["dois instrumentos de menor potencial ofensivo.","uma arma.","um colete.","um rádio.","uma viatura."],"Art. 6º, III.","forca2c")
# n=2
q(2,"A classificação dos instrumentos de menor potencial ofensivo obedece ao art. 23 da Lei 10.826/2003, aos arts. 4º e 7º da Lei 13.060/2014 e ao Decreto",["10.030/2019.","11.615/2023.","12.002/2024.","9.846/2019.","11.203/2022."],"Art. 1º, parágrafo único.")
q(2,"Entre as diretrizes gerais, o nível da força deve ser compatível com a gravidade da ameaça apresentada pela conduta das pessoas e os objetivos legítimos da ação do",["profissional de segurança pública.","cidadão.","juiz.","jornalista.","vizinho."],"Art. 2º, parágrafo único, IV.")
q(2,"Entre as diretrizes, os órgãos e profissionais devem assumir a responsabilidade pelo uso inadequado da força após a conclusão de processo de investigação, respeitado o devido processo legal, a ampla defesa e o",["contraditório.","sigilo.","arquivamento.","recurso ao chefe.","silêncio."],"Art. 2º, parágrafo único, VI.")
q(2,"A não discriminação impede preconceitos de raça, etnia, cor, gênero, orientação sexual, idioma, religião, nacionalidade, origem social, deficiência, situação econômica, opinião política ou de outra",["natureza.","cidade.","idade apenas.","família.","profissão."],"Art. 2º, parágrafo único, VII.")
q(2,"A força deve ser selecionada em resposta a uma ameaça real ou",["potencial.","hipotética.","passada.","futura.","eventual."],"Art. 3º.")
q(2,"Não é legítimo o uso de arma de fogo contra pessoa em fuga que esteja desarmada ou que não represente risco imediato de morte ou de lesão aos profissionais ou a",["terceiros.","carros.","bens.","viaturas.","edifícios."],"Art. 3º, § 3º, I.")
q(2,"A capacitação deve adotar conteúdo que aborde o emprego adequado de diferentes tipos de armas de fogo e de instrumentos de menor potencial",["ofensivo.","lesivo.","letal.","defensivo.","brando."],"Art. 4º, III.")
q(2,"A matriz curricular nacional da Lei 13.675/2018 deverá ser atualizada para adequação à Lei 13.060/2014 e a este",["Decreto.","contrato.","convênio.","manual.","portal."],"Art. 4º, parágrafo único.")
q(2,"Compete ao Ministério da Justiça e Segurança Pública financiar, conforme a disponibilidade orçamentária, ações para implementar a Lei 13.060/2014 e este",["Decreto.","convênio.","tratado.","estatuto.","regimento."],"Art. 5º, I.")
q(2,"O Ministério deve desenvolver materiais de referência, especialmente quanto ao uso de algemas, à busca pessoal e domiciliar e à atuação em ambientes",["prisionais.","escolares.","esportivos.","comerciais.","rurais."],"Art. 5º, IV.")
q(2,"O Ministério deve disponibilizar atas de registro de preços para aquisição de armas de fogo, de instrumentos de menor potencial ofensivo e de equipamentos de proteção",["individual.","coletiva.","externa.","pública.","militar."],"Art. 5º, V.")
q(2,"As diretrizes de implementação incluem a normatização e fiscalização da identificação dos profissionais, de forma a possibilitar a individualização de suas ações durante o",["serviço.","almoço.","descanso.","treinamento.","plantão apenas."],"Art. 6º, IX.")
q(2,"Os mecanismos de controle devem garantir a transparência e o acesso público a dados e informações sobre o uso da",["força.","verba.","arma.","viatura.","escala."],"Art. 7º, I.")
q(2,"A atuação dos mecanismos de controle inclui o fortalecimento das corregedorias e",["ouvidorias.","empresas.","clubes.","sindicatos.","bancos."],"Art. 7º, IV.")
q(2,"O Comitê terá a participação da sociedade civil na composição do",["colegiado.","juízo.","tribunal.","cartório.","balcão."],"Art. 8º, § 1º, I, a.")
q(2,"Os Estados, o Distrito Federal e os Municípios, quando instituírem comitês de monitoramento, observarão as mesmas finalidades, garantida a participação de representantes da sociedade",["civil.","militar.","privada.","religiosa.","partidária."],"Art. 8º, § 2º.")
q(2,"O Ministro de Estado da Justiça e Segurança Pública editará normas complementares necessárias à execução do",["Decreto.","contrato.","convênio.","tratado.","edital."],"Art. 10.")
q(2,"No texto da negociação na praça, a diretriz aplicada decorre do art. 3º, § 1º, que fala em priorizar a comunicação e a",["negociação.","contenção.","perseguição.","restrição.","omissão."],"Art. 3º, § 1º.","forca2a")
q(2,"No texto do ferimento na ocorrência, o relatório é exigido sempre que o uso da força resultar em ferimento ou",["morte.","atraso.","multa.","protesto.","prisão."],"Art. 3º, § 5º.","forca2b")
q(2,"No texto do equipamento do guarda, o Município deve disponibilizar a todo profissional em serviço equipamento de proteção individual e instrumentos de menor potencial ofensivo, no",["mínimo dois.","máximo um.","mínimo cinco.","máximo três.","mínimo dez."],"Art. 6º, III.","forca2c")
# n=3
q(3,"Assinale a alternativa correta sobre o Decreto 12.341/2024.",["Os princípios gerais são sete; a arma de fogo é último recurso; a capacitação é anual e no horário de serviço.","Os princípios gerais são cinco; a arma de fogo é o primeiro recurso.","A capacitação é bienal e fora do horário de serviço.","O relatório é dispensado em caso de morte.","Cada profissional recebe um instrumento de menor potencial ofensivo."],"Arts. 2º, 3º e 4º.")
q(3,"Considere. I. A comunicação e a negociação devem ser priorizadas. II. A arma de fogo é medida de último recurso. III. O relatório circunstanciado é facultativo. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O relatório é obrigatório quando há ferimento ou morte (art. 3º, § 5º).")
q(3,"Assinale a INCORRETA.",["A capacitação sobre uso da força é facultativa.","A capacitação é anual.","A capacitação é feita no horário de serviço.","A capacitação aborda armas de fogo e instrumentos de menor potencial ofensivo.","A matriz curricular nacional será atualizada."],"A capacitação é obrigatória (art. 4º, I).")
q(3,"As ocorrências do uso da força serão registradas também quando envolverem o emprego de armas de fogo ou de instrumentos de menor potencial ofensivo em ambientes",["prisionais.","escolares.","domésticos.","comerciais.","rurais."],"Art. 7º, parágrafo único, II.")
q(3,"O registro formal das ocorrências segue parâmetros estabelecidos em ato do Ministro de Estado da",["Justiça e Segurança Pública.","Defesa.","Fazenda.","Saúde.","Educação."],"Art. 7º, parágrafo único.")
q(3,"O Comitê Nacional de Monitoramento do Uso da Força observará, para a sua organização, o Capítulo VI do Decreto",["12.002/2024.","12.341/2024.","10.030/2019.","9.846/2019.","11.615/2023."],"Art. 8º, § 1º, II.")
q(3,"Entre as finalidades do Comitê está o acompanhamento da implementação do Plano Nacional de Segurança Pública, em relação à redução da letalidade policial e da vitimização de",["profissionais de segurança pública.","empresários.","estudantes.","motoristas.","moradores."],"Art. 8º, § 1º, III, b.")
q(3,"Entre as finalidades do Comitê está a articulação com os comitês estaduais e distrital sobre o uso da",["força.","verba.","viatura.","arma.","escala."],"Art. 8º, § 1º, III, f.")
q(3,"O art. 6º, X, trata da normatização da atuação em gerenciamento de crises, busca pessoal, busca domiciliar, uso de algemas e providências nos casos em que o uso da força resultar em lesão corporal ou",["morte.","atraso.","protesto.","multa.","prisão."],"Art. 6º, X.")
q(3,"Entre as competências do Ministério da Justiça está estabelecer ações para a redução da vitimização dos profissionais de segurança pública e da",["letalidade policial.","carga horária.","verba.","jornada.","remuneração."],"Art. 5º, X.")
q(3,"Entre as competências do Ministério está desenvolver medidas para informar a população sobre as políticas de uso da força e como reportar condutas inadequadas na ação dos",["profissionais de segurança pública.","empresários.","estudantes.","motoristas.","moradores."],"Art. 5º, XII.")
q(3,"A responsabilização pelo uso inadequado da força é apurada com respeito ao devido processo legal, à ampla defesa e ao",["contraditório.","sigilo.","arquivamento.","silêncio do chefe.","ordem verbal."],"Art. 2º, parágrafo único, VI.")
q(3,"Os princípios do art. 2º e as vedações do art. 3º, § 3º, aplicam-se aos",["profissionais de segurança pública.","cidadãos.","vigilantes privados.","bombeiros civis.","agentes de saúde."],"Art. 1º e art. 3º.")
q(3,"No texto da negociação na praça, o homem com garrafa representa ameaça, e a resposta deve ser diferenciada, com seleção apropriada do",["nível da força.","tipo de viatura.","horário.","local.","uniforme."],"Art. 3º.","forca2a")
q(3,"No texto da negociação na praça, o objetivo é minimizar o uso de meios que possam causar ofensas, ferimentos ou",["mortes.","gastos.","multas.","atrasos.","protestos."],"Art. 3º.","forca2a")
q(3,"No texto do ferimento na ocorrência, o relatório segue parâmetros estabelecidos em ato do Ministro de Estado da",["Justiça e Segurança Pública.","Defesa.","Fazenda.","Saúde.","Educação."],"Art. 3º, § 5º.","forca2b")
q(3,"No texto do ferimento na ocorrência, o registro formal da ocorrência decorre de ela ter resultado em",["lesão corporal.","protesto.","atraso.","multa.","reclamação."],"Art. 7º, parágrafo único, I.","forca2b")
q(3,"No texto do equipamento do guarda, a conduta da administração descumpre a diretriz do art. 6º, inciso",["III.","I.","II.","IV.","IX."],"Art. 6º, III.","forca2c")
q(3,"No texto do equipamento do guarda, a diretriz exige também equipamento de proteção",["individual.","coletiva.","externa.","pública.","militar."],"Art. 6º, III.","forca2c")
q(3,"No texto do equipamento do guarda, entregar apenas arma de fogo leva o guarda a depender da arma como recurso, o que contraria a lógica de a arma ser medida de",["último recurso.","primeiro recurso.","rotina.","opção livre.","regra."],"Art. 3º, § 2º.","forca2c")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Decreto 12.341/2024: uso da força",[
 ("pri","Sete princípios",["legalidade, precaução","necessidade, proporcionalidade","razoabilidade, responsabilização, não discriminação"],"seção 1"),
 ("dir","Diretrizes",["objetivo legal","recurso de menor intensidade","bom senso"],"seção 1"),
 ("dif","Uso diferenciado",["comunicação e negociação","arma de fogo: último recurso","relatório se há ferimento ou morte"],"seção 2"),
 ("cap","Capacitação",["obrigatória","anual","no horário de serviço"],"seção 2"),
 ("equ","Equipamento",["EPI","dois instrumentos no mínimo"],"seção 3"),
 ("con","Controle",["ouvidorias e corregedorias","registro de ocorrências","Comitê Nacional"],"seção 3")],
 "Na prova: sete princípios, capacitação anual e dois instrumentos")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz os princípios; as demais, o uso diferenciado, a capacitação, o equipamento e o controle.","Fontes: Edital 02/2026, Anexo I; Decreto 12.341/2024, publicação original, Câmara dos Deputados. Exemplos criados para a aula.")
revisao("forca-2","Regulamentação do uso da força (Decreto 12.341/2024)",Q,list(tx),
 cobertura=["Cobertos os arts. 1º a 4º, 6º a 10. O art. 5º (competências do Ministério) aparece só em questões."],
 pendencias=["Texto-fonte: publicação original da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto se houve alteração posterior.","Trechos de lei copiados de fontes/forca2.txt por programa.","Casos forca2a, forca2b e forca2c fictícios."],
 fontes_conferidas=["Decreto 12.341/2024: texto da Câmara, copiado por programa."])
gravar("forca-2",aula_html,banco("forca-2",Q),tx)
