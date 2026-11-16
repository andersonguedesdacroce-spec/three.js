import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='ctb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A habilitação é o assunto do Código que mais mistura números: idades, anos de experiência, prazos de validade, categorias A a E. A Vunesp cobra os arts. 140 a 160 pelos requisitos para habilitar-se, pelas categorias (qual veículo cada uma permite conduzir), pelos exames, pela Permissão para Dirigir de um ano, pelo exame toxicológico para categorias C, D e E, e pelo porte e validade da Carteira. Para o guarda, é a base da fiscalização da CNH. A aula segue o texto consolidado, com a lei citada e a explicação logo abaixo."
S={}
S[1]="## 1. Requisitos e categorias\n\n"+L("art. 140","Art. 140. A habilitação para conduzir","Parágrafo único. As informações do candidato")+"\n\n"+L("art. 143, caput e § 1º","Art. 143. Os candidatos poderão habilitar-se","§ 2º São os condutores da categoria B")+"\n\n"+L("art. 145","Art. 145. Para habilitar-se nas categorias D e E","§ 1º A participação em curso")+"""

Para habilitar-se, o candidato deve ser penalmente imputável, saber ler e escrever e possuir carteira de identidade ou equivalente, e os exames são feitos no órgão executivo do Estado ou do DF do domicílio ou residência. As categorias seguem uma gradação. A categoria A é para veículo motorizado de duas ou três rodas, com ou sem carro lateral. A B é para veículo motorizado não abrangido pela A, de peso bruto total até 3.500 kg e lotação de até 8 lugares, excluído o motorista. A C amplia para veículos de carga com peso bruto total acima de 3.500 kg. A D, para transporte de passageiros com lotação acima de 8 lugares. E a E, para combinação de veículos em que a unidade tratora se enquadre em B, C ou D e a unidade acoplada tenha 6.000 kg ou mais de peso bruto total, ou lotação acima de 8 lugares.

Para a categoria C, o condutor deve estar habilitado há ao menos um ano na categoria B e não ter cometido mais de uma infração gravíssima nos últimos 12 meses. Para as categorias D e E, ou para conduzir veículo de transporte coletivo de passageiros, de escolares, de emergência ou de produto perigoso, o candidato deve ser maior de 21 anos, estar habilitado há pelo menos dois anos na B (ou um ano na C) para a D, ou um ano na C para a E, não ter mais de uma infração gravíssima nos últimos 12 meses e ser aprovado em curso especializado e em curso de treinamento de prática veicular em situação de risco.
"""
S[2]="## 2. Exames, Permissão para Dirigir e exame toxicológico\n\n"+L("art. 147, caput","Art. 147. O candidato à habilitação deverá","§ 1º Os resultados dos exames")+"\n\n"+L("art. 147, § 2º","§ 2º O exame de aptidão física e mental, a ser realizado","§ 3º O exame previsto no § 2º incluirá")+"\n\n"+L("art. 148, caput e §§ 1º a 4º","Art. 148. Os exames de habilitação","§ 5º O Conselho Nacional")+"""

O candidato se submete aos exames na ordem: aptidão física e mental, escrito sobre legislação de trânsito, noções de primeiros socorros e direção veicular, este realizado na via pública, em veículo da categoria pretendida. O exame de aptidão física e mental, preliminar, é renovável a cada 10 anos para quem tem menos de 50 anos; a cada 5 anos para quem tem 50 anos ou mais e menos de 70; e a cada 3 anos para quem tem 70 anos ou mais. A formação inclui curso de direção defensiva e de conceitos básicos de proteção ao meio ambiente.

O candidato aprovado recebe a Permissão para Dirigir, com validade de um ano. A Carteira Nacional de Habilitação é conferida ao condutor no término de um ano, desde que não tenha cometido nenhuma infração de natureza grave ou gravíssima ou seja reincidente em infração média. Se não obtém a CNH por esse motivo, reinicia todo o processo de habilitação.

"""+L("art. 148-A, caput, §§ 1º e 2º","Art. 148-A. Os condutores das categorias C, D e E","§ 3º [revogado]")+"\n\n"+L("art. 148-A, § 5º","§ 5º O resultado positivo no exame previsto no § 2º","§ 6º O resultado do exame somente")+"""

Os condutores das categorias C, D e E devem comprovar resultado negativo em exame toxicológico para obter e renovar a CNH. O exame busca aferir o consumo de substâncias psicoativas que comprometam a capacidade de direção e tem janela de detecção mínima de 90 dias. Além disso, os condutores C, D e E com menos de 70 anos são submetidos a novo exame a cada 2 anos e 6 meses. O resultado positivo no exame periódico leva à suspensão do direito de dirigir por 3 meses, condicionado o levantamento à inclusão de resultado negativo em novo exame.
"""
S[3]="## 3. Formação, porte e validade da CNH\n\n"+L("art. 154, caput e § 2º","Art. 154. Os veículos destinados à formação","§ 1º No veículo eventualmente utilizado")+"\n\n"+L("art. 154, § 2º","§ 2º As idades máximas","§ 3º (VETADO")+"\n\n"+L("art. 158","Art. 158. A aprendizagem só poderá realizar-se:","§ 2º [revogado]")+"\n\n"+L("art. 159, caput e §§ 1º e 1º-A","Art. 159. A Carteira Nacional de Habilitação:","§ 2º (VETADO)")+"\n\n"+L("art. 159, § 5º","§ 5º A Carteira Nacional de Habilitação e a Permissão","§ 6º A identificação")+"\n\n"+L("art. 160","Art. 160. O condutor condenado","§ 1º Em caso de sinistro grave")+"""

Os veículos de formação de condutores são identificados por faixa amarela de vinte centímetros de largura, à meia altura, com a inscrição AUTO-ESCOLA em preto. As idades máximas desses veículos, sem computar o ano de fabricação, são de 8 anos para a categoria A, 12 para a B e 20 para as categorias C, D e E. A aprendizagem só se realiza nos termos, horários e locais do órgão de trânsito, acompanhado o aprendiz por instrutor autorizado, e o veículo pode levar, além deles, apenas mais um acompanhante.

A CNH pode ser emitida em meio físico ou digital, tem fé pública e equivale a documento de identidade no território nacional. É obrigatório o porte da Permissão para Dirigir ou da CNH quando o condutor estiver à direção do veículo, dispensado o porte quando, na fiscalização, for possível acessar o sistema informatizado para verificar se o condutor está habilitado. A CNH e a Permissão só têm validade para a condução quando apresentadas em original. E o condutor condenado por delito de trânsito deve ser submetido a novos exames para voltar a dirigir, independentemente do reconhecimento da prescrição.
"""
S[5]="""## 5. Na rotina do guarda

- **Abordagem:** o agente confere a categoria da CNH em relação ao veículo (A para duas ou três rodas, B para automóveis, C para carga acima de 3.500 kg, D para passageiros com mais de 8 lugares).
- **Documento digital:** a CNH em meio digital vale, e o agente pode consultar o sistema se o documento não for apresentado.
- **Permissão para Dirigir:** o condutor recém-habilitado tem a Permissão, válida por um ano, e infrações graves ou gravíssimas nesse período impedem a CNH definitiva.
- **Categorias profissionais:** quem dirige ônibus, escolar, ambulância ou carga pesada precisa da categoria correspondente, de ser maior de 21 anos nos casos do art. 145 e do exame toxicológico.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Peso e lotação da categoria B | Até 3.500 kg e até 8 lugares, excluído o motorista |
| Idade para as categorias D e E | Maior de 21 anos |
| Experiência para a categoria C | Um ano na B |
| Experiência para a categoria D | Dois anos na B ou um ano na C |
| Validade da Permissão para Dirigir | Um ano |
| Exame de aptidão física e mental | 10 anos (menos de 50), 5 anos (50 a 69), 3 anos (70 ou mais) |
| Exame toxicológico | Categorias C, D e E; a cada 2 anos e 6 meses para quem tem menos de 70 anos |
| Porte da CNH | Obrigatório, dispensado se o sistema permitir a consulta |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Requisitos | Imputável, saber ler e escrever, identidade |
| A | Duas ou três rodas |
| B | Até 3.500 kg e 8 lugares |
| C | Carga acima de 3.500 kg; 1 ano na B |
| D | Passageiros acima de 8 lugares |
| E | Combinação com unidade acoplada de 6.000 kg ou mais |
| D e E | Maior de 21 anos; curso especializado |
| Permissão para Dirigir | 1 ano; sem infração grave ou gravíssima para obter a CNH |
| Aptidão física e mental | 10, 5 ou 3 anos conforme a idade |
| Exame toxicológico | C, D e E; janela de 90 dias |
| Faixa AUTO-ESCOLA | Amarela, 20 cm, letras pretas |
"""
QR=[("Questão 1","A categoria B de habilitação é para condutor de veículo motorizado, não abrangido pela categoria A, cujo peso bruto total não exceda",["três mil e quinhentos quilogramas e cuja lotação não exceda oito lugares, excluído o do motorista.","dois mil quilogramas e seis lugares.","quatro mil e quinhentos quilogramas e dez lugares.","cinco mil quilogramas e doze lugares.","três mil quilogramas e cinco lugares."],0,"Art. 143, II."),
("Questão 2","Ao candidato aprovado nos exames de habilitação será conferida a Permissão para Dirigir, com validade de",["um ano.","seis meses.","dois anos.","três anos.","cinco anos."],2,"Art. 148, § 2º."),
("Questão 3","Para habilitar-se nas categorias D e E, o candidato deverá ser maior de",["vinte e um anos.","dezoito anos.","dezenove anos.","vinte anos.","vinte e cinco anos."],1,"Art. 145, I."),
("Questão 4","O exame de aptidão física e mental é renovável a cada 10 anos para condutores com idade inferior a",["cinquenta anos.","quarenta anos.","sessenta anos.","trinta anos.","setenta anos."],4,"Art. 147, § 2º, I.")]
t1="<strong>Abordagem de um ônibus</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, abordou um micro-ônibus escolar de 20 lugares dirigido por um homem de 23 anos, que apresentou a CNH digital na categoria B, obtida há dois anos e seis meses."
t2="<strong>Condutor recém-habilitado</strong><br><br>Um jovem recebeu a Permissão para Dirigir em março. Em outubro, foi autuado por infração gravíssima. Pergunta-se sobre a emissão da CNH definitiva."
tx={"ctb6a":t1,"ctb6b":t2}
# n=1
q(1,"Para conduzir veículo automotor, o candidato deve ser penalmente imputável, saber ler e escrever e possuir",["Carteira de Identidade ou equivalente.","título de eleitor.","comprovante de renda.","carteira de trabalho.","certificado de reservista."],"Art. 140.")
q(1,"As informações do candidato à habilitação serão cadastradas no",["RENACH.","RENAVAM.","SINESP.","CAGED.","SIAFI."],"Art. 140, parágrafo único.")
q(1,"A autorização para conduzir veículos de propulsão humana e de tração animal fica a cargo dos",["Municípios.","Estados.","Contran.","União.","Cetran."],"Art. 141, § 1º.")
q(1,"A categoria A de habilitação é para condutor de veículo motorizado de",["duas ou três rodas, com ou sem carro lateral.","quatro rodas.","carga.","passageiros.","tração."],"Art. 143, I.")
q(1,"A categoria C é para condutor de veículo de carga com peso bruto total superior a",["3.500 kg.","2.000 kg.","5.000 kg.","6.000 kg.","1.000 kg."],"Art. 143, III.")
q(1,"A categoria D é para condutor de veículo de transporte de passageiros com lotação superior a",["8 lugares, excluído o do motorista.","4 lugares.","6 lugares.","10 lugares.","12 lugares."],"Art. 143, IV.")
q(1,"A categoria E é para condutor de combinação de veículos em que a unidade tratora se enquadre nas categorias B, C ou D e a unidade acoplada tenha",["6.000 kg ou mais de peso bruto total, ou lotação superior a 8 lugares.","menos de 3.500 kg.","4.000 kg.","5.000 kg.","3.000 kg."],"Art. 143, V.")
q(1,"Para habilitar-se na categoria C, o condutor deverá estar habilitado no mínimo há",["1 ano na categoria B.","2 anos na categoria B.","3 anos na categoria B.","6 meses na categoria B.","5 anos na categoria B."],"Art. 143, § 1º.")
q(1,"Para habilitar-se nas categorias D e E, o candidato deverá ser maior de",["vinte e um anos.","dezoito anos.","dezenove anos.","vinte anos.","vinte e cinco anos."],"Art. 145, I.")
q(1,"Para habilitar-se na categoria D, o candidato deve estar habilitado no mínimo há dois anos na categoria B ou há um ano na categoria",["C.","A.","D.","E.","B."],"Art. 145, II, a.")
q(1,"Para habilitar-se na categoria E, o candidato deve estar habilitado no mínimo há um ano na categoria",["C.","A.","B.","D.","E."],"Art. 145, II, b.")
q(1,"O exame de direção veicular é realizado na via pública, em veículo da categoria para a qual o candidato estiver",["habilitando-se.","habilitado.","testando.","vendendo.","comprando."],"Art. 147, V.")
q(1,"O exame de aptidão física e mental é renovável a cada 5 anos para condutores com idade igual ou superior a 50 e inferior a",["70 anos.","60 anos.","65 anos.","55 anos.","80 anos."],"Art. 147, § 2º, II.")
q(1,"O exame de aptidão física e mental é renovável a cada 3 anos para condutores com idade igual ou superior a",["70 anos.","60 anos.","65 anos.","55 anos.","80 anos."],"Art. 147, § 2º, III.")
q(1,"Ao candidato aprovado nos exames será conferida a Permissão para Dirigir, com validade de",["um ano.","seis meses.","dois anos.","três anos.","cinco anos."],"Art. 148, § 2º.")
q(1,"A formação de condutores deverá incluir, obrigatoriamente, curso de direção defensiva e de conceitos básicos de proteção ao",["meio ambiente relacionados com o trânsito.","patrimônio.","consumidor.","trabalhador.","idoso."],"Art. 148, § 1º.")
q(1,"Os condutores das categorias C, D e E deverão comprovar resultado negativo em exame",["toxicológico, para a obtenção e a renovação da CNH.","de sangue.","de visão, apenas.","de audição.","de urina, apenas."],"Art. 148-A, caput.")
q(1,"Os veículos destinados à formação de condutores são identificados por faixa",["amarela, com a inscrição AUTO-ESCOLA em preto.","branca, com inscrição preta.","vermelha.","azul.","verde."],"Art. 154, caput.")
q(1,"É obrigatório o porte da Permissão para Dirigir ou da CNH quando o condutor estiver",["à direção do veículo.","em casa.","no trabalho.","em viagem de ônibus.","como passageiro."],"Art. 159, § 1º.")
q(1,"No texto do condutor recém-habilitado, a CNH definitiva só será conferida se o condutor, no término de um ano, não tiver cometido",["nenhuma infração de natureza grave ou gravíssima, ou reincidência em média.","nenhuma infração leve.","nenhuma infração.","mais de duas infrações.","mais de três infrações."],"Art. 148, § 3º.","ctb6b")
# n=2
q(2,"Os exames de habilitação serão realizados no órgão ou entidade executivos do Estado ou do DF, do",["domicílio ou residência do candidato.","local de nascimento.","local de trabalho.","local do veículo.","local de estudo."],"Art. 140, caput.")
q(2,"O processo de habilitação e as normas relativas à aprendizagem serão regulamentados pelo",["Contran.","Cetran.","Município.","Estado.","Ministério da Educação."],"Art. 141, caput.")
q(2,"O reconhecimento de habilitação obtida em outro país está subordinado às condições estabelecidas em",["convenções e acordos internacionais e às normas do Contran.","leis municipais.","decretos estaduais.","portarias do juiz.","normas das escolas."],"Art. 142.")
q(2,"Os condutores da categoria B são autorizados a conduzir veículo da espécie motor-casa, cujo peso não exceda 6.000 kg ou cuja lotação não exceda",["8 lugares, excluído o do motorista.","4 lugares.","10 lugares.","12 lugares.","20 lugares."],"Art. 143, § 2º.")
q(2,"Os condutores da categoria B são autorizados a conduzir veículo a motor de propulsão elétrica ou híbrida, com tração predominantemente elétrica, com peso bruto total de até",["4.250 kg.","3.500 kg.","5.000 kg.","6.000 kg.","2.000 kg."],"Art. 143, § 2º-A.")
q(2,"O trator de roda e os equipamentos automotores destinados a trabalhos agrícolas poderão ser conduzidos em via pública também por condutor habilitado na categoria",["B.","A.","D, apenas.","E, apenas.","nenhuma."],"Art. 144, parágrafo único.")
q(2,"O trator de roda, de esteira, misto ou o equipamento automotor para trabalho de terraplenagem só podem ser conduzidos por habilitado nas categorias",["C, D ou E.","A ou B.","A, apenas.","B, apenas.","qualquer categoria."],"Art. 144, caput.")
q(2,"Para conduzir ambulâncias, o candidato deverá comprovar treinamento especializado e reciclagem em cursos específicos a cada",["5 anos.","2 anos.","3 anos.","10 anos.","1 ano."],"Art. 145-A.")
q(2,"Para conduzir veículos de outra categoria, o condutor deverá realizar",["exames complementares exigidos para habilitação na categoria pretendida.","nenhum exame.","apenas curso.","apenas pagamento de taxa.","apenas cadastro."],"Art. 146.")
q(2,"Os exames de aptidão física e mental e a avaliação psicológica devem ser realizados por médicos e psicólogos peritos examinadores com titulação de especialista em",["medicina do tráfego e em psicologia do trânsito.","cardiologia e psiquiatria.","clínica geral e psicopedagogia.","medicina do trabalho e psicologia social.","neurologia e psicologia clínica."],"Art. 147, caput.")
q(2,"O exame de aptidão física e mental incluirá avaliação psicológica preliminar e complementar sempre que a ele se submeter o condutor que",["exerce atividade remunerada ao veículo.","for idoso.","for jovem.","for estrangeiro.","tenha multas."],"Art. 147, § 3º.")
q(2,"Ao candidato com deficiência auditiva é assegurada, em todas as etapas do processo de habilitação,",["acessibilidade de comunicação, por tecnologias assistivas ou ajudas técnicas.","dispensa dos exames.","isenção de taxas.","prioridade nas filas.","categoria especial."],"Art. 147-A.")
q(2,"Os exames de habilitação, exceto os de direção veicular, poderão ser aplicados por entidades públicas ou privadas",["credenciadas pelo órgão executivo de trânsito dos Estados e do DF.","do exterior.","sem credenciamento.","religiosas.","partidárias."],"Art. 148, caput.")
q(2,"Se o condutor não obtém a CNH no término do ano da Permissão por ter cometido infração grave ou gravíssima, ele",["reinicia todo o processo de habilitação.","recebe a CNH.","recebe nova Permissão.","paga multa.","é preso."],"Art. 148, § 4º.")
q(2,"O exame toxicológico dos condutores C, D e E tem janela de detecção mínima de",["90 dias.","30 dias.","60 dias.","120 dias.","180 dias."],"Art. 148-A, § 1º.")
q(2,"Os condutores C, D e E com idade inferior a 70 anos fazem novo exame toxicológico a cada período de",["2 anos e 6 meses.","1 ano.","2 anos.","3 anos.","5 anos."],"Art. 148-A, § 2º.")
q(2,"O resultado positivo no exame toxicológico periódico do § 2º acarreta a suspensão do direito de dirigir pelo período de",["3 meses.","1 mês.","6 meses.","1 ano.","2 anos."],"Art. 148-A, § 5º, II.")
q(2,"No texto do ônibus, o condutor de micro-ônibus escolar com lotação de 20 lugares precisaria, para a condução, da categoria",["D.","B.","A.","C.","E."],"Art. 143, IV: passageiros com mais de 8 lugares.","ctb6a")
q(2,"No texto do ônibus, para conduzir transporte escolar, o condutor deveria ser maior de 21 anos e ter",["curso especializado, entre outros requisitos do art. 145.","apenas a CNH B.","apenas 18 anos.","apenas o exame de visão.","apenas o seguro."],"Art. 145.","ctb6a")
q(2,"No texto do condutor recém-habilitado, a infração gravíssima no período da Permissão impede a CNH porque o art. 148, § 3º, exige que o condutor não tenha cometido infração",["de natureza grave ou gravíssima, nem seja reincidente em média.","apenas gravíssima.","apenas leve.","apenas média.","nenhuma, de qualquer natureza."],"Art. 148, § 3º.","ctb6b")
# n=3
q(3,"Assinale a alternativa que traz apenas categorias e requisitos corretos.",["B: até 3.500 kg e 8 lugares; C: carga acima de 3.500 kg; D: passageiros acima de 8 lugares.","B: até 5.000 kg e 10 lugares; C: carga acima de 5.000 kg.","C: passageiros; D: carga.","A: quatro rodas; B: duas rodas.","E: veículos de uma só unidade."],"Art. 143, II a IV.")
q(3,"Considere as afirmações. I. A categoria D exige ser maior de 21 anos. II. A Permissão para Dirigir vale por um ano. III. O exame de aptidão física e mental é renovado a cada 10 anos para quem tem 55 anos. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II e III, apenas.","I e III, apenas.","I, II e III."],"Aos 55 anos, o exame é renovado a cada 5 anos (art. 147, § 2º, II).")
q(3,"Assinale a INCORRETA.",["A categoria C exige 2 anos de habilitação na B.","A categoria D exige ser maior de 21 anos.","A categoria E exige um ano na C.","A categoria C exige não ter cometido mais de uma infração gravíssima em 12 meses.","A Permissão para Dirigir vale um ano."],"A categoria C exige um ano na B (art. 143, § 1º).")
q(3,"Os condutores das categorias B, C e D podem conduzir combinação de veículos cuja unidade acoplada tenha peso bruto total inferior a",["6.000 kg e lotação não superior a 8 lugares.","3.500 kg.","4.000 kg.","5.000 kg.","8.000 kg."],"Art. 143, § 4º.")
q(3,"A CNH, nos termos do art. 159, tem fé pública e equivale a",["documento de identidade em todo o território nacional.","passaporte.","título de eleitor.","carteira de trabalho.","certidão de nascimento."],"Art. 159, III.")
q(3,"O porte do documento de habilitação será dispensado quando, no momento da fiscalização, for possível",["ter acesso ao sistema informatizado para verificar se o condutor está habilitado.","consultar o vizinho.","ligar para a família.","pedir a testemunha.","ver o veículo."],"Art. 159, § 1º-A.")
q(3,"A CNH e a Permissão para Dirigir somente terão validade para a condução de veículo quando apresentadas em",["original.","cópia autenticada.","cópia simples.","fotografia.","declaração."],"Art. 159, § 5º.")
q(3,"A renovação da CNH ou a emissão de nova via somente será realizada após quitação dos",["débitos constantes do prontuário do condutor.","débitos do veículo.","débitos de IPTU.","débitos de IPVA.","débitos de aluguel."],"Art. 159, § 8º.")
q(3,"A validade da CNH está condicionada ao prazo de vigência do",["exame de aptidão física e mental.","exame toxicológico.","seguro do veículo.","licenciamento do veículo.","registro do veículo."],"Art. 159, § 10.")
q(3,"O condutor condenado por delito de trânsito deverá ser submetido a novos exames para que possa voltar a dirigir, independentemente do reconhecimento da",["prescrição, em face da pena concretizada na sentença.","reincidência.","menoridade.","primariedade.","culpa."],"Art. 160, caput.")
q(3,"As idades máximas dos veículos destinados à formação de condutores, para a categoria B, são de",["12 anos, não computado o ano de fabricação.","8 anos.","20 anos.","5 anos.","15 anos."],"Art. 154, § 2º, II.")
q(3,"A aprendizagem só poderá realizar-se acompanhado o aprendiz por",["instrutor autorizado.","qualquer habilitado.","um parente.","um amigo.","um policial."],"Art. 158, II.")
q(3,"Além do aprendiz e do instrutor, o veículo utilizado na aprendizagem poderá conduzir apenas mais",["um acompanhante.","dois acompanhantes.","três acompanhantes.","nenhum acompanhante.","quatro acompanhantes."],"Art. 158, § 1º.")
q(3,"O exame de direção veicular será realizado perante comissão integrada por",["3 membros designados pelo dirigente do órgão executivo local de trânsito.","2 membros.","5 membros.","um membro.","7 membros."],"Art. 152, caput.")
q(3,"A exigência de exame toxicológico para obtenção da primeira habilitação por condutores das categorias A e B, no § 10 do art. 148-A, aparece no texto consolidado como",["vetada, sem vigência.","vigente.","revogada.","inconstitucional.","suspensa."],"Art. 148-A, § 10: marca de vetado.")
q(3,"No texto do ônibus, o condutor, com CNH B obtida há 2 anos e 6 meses, para habilitar-se na categoria D, atenderia ao tempo exigido no art. 145, II, a, que é de",["dois anos na B, entre outros requisitos.","três anos na B.","um ano na B.","cinco anos na B.","seis meses na B."],"Art. 145, II, a.","ctb6a")
q(3,"No texto do ônibus, além do tempo de B, para a categoria D seriam exigidos, entre outros, a idade e",["curso especializado e curso de treinamento de prática veicular em situação de risco.","apenas exame de visão.","apenas seguro.","apenas licenciamento.","apenas inspeção."],"Art. 145, III e IV.","ctb6a")
q(3,"No texto do condutor recém-habilitado, o prazo da Permissão para Dirigir é de",["um ano, contado da emissão.","seis meses.","dois anos.","três anos.","cinco anos."],"Art. 148, § 2º.","ctb6b")
q(3,"A habilitação para conduzir veículo de transporte coletivo de passageiros, de escolares, de emergência ou de produto perigoso exige, entre outros requisitos, que o condutor",["não tenha cometido mais de uma infração gravíssima nos últimos 12 meses.","tenha menos de 21 anos.","não tenha curso algum.","seja habilitado há apenas 6 meses.","seja estrangeiro."],"Art. 145, III.")
q(3,"Considere. I. A CNH pode ser física ou digital. II. A CNH em cópia simples vale para a condução. III. O porte pode ser dispensado se a fiscalização acessar o sistema. Está correto o que se afirma em",["I e III, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Art. 159, § 5º: só vale em original; a cópia simples não serve.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Habilitação: requisitos, categorias e exames",[
 ("req","Requisitos",["imputável","saber ler e escrever","identidade"],"seção 1"),
 ("cat","Categorias",["A: duas ou três rodas","B: até 3.500 kg e 8 lugares","C, D, E"],"seção 1"),
 ("idade","Idade e experiência",["D e E: maior de 21 anos","C: 1 ano na B","D: 2 anos na B ou 1 na C"],"seção 1"),
 ("exa","Exames",["aptidão física e mental","escrito, primeiros socorros, direção","10, 5 ou 3 anos"],"seção 2"),
 ("perm","Permissão para Dirigir",["1 ano","sem infração grave ou gravíssima","senão recomeça"],"seção 2"),
 ("cnh","CNH",["física ou digital","fé pública, vale como identidade","porte obrigatório"],"seção 3")],
 "Na prova: confira idade, experiência e peso e lotação de cada categoria")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira caixa traz os requisitos e as categorias; as demais, o caminho até a CNH e as regras de porte e validade.","Fontes: Edital 02/2026, Anexo I; Lei 9.503/1997 (Código de Trânsito Brasileiro), arts. 140 a 160, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("ctb-6","Habilitação (CTB, arts. 140 a 160)",Q,list(tx),
 cobertura=["Recorte do edital: categorias, permissão para dirigir e exames. Cobertos: arts. 140 a 148-A, 152, 154, 155, 158, 159 e 160. Não detalhados: arts. 149 a 151, 153, 156 e 157."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026. O Planalto estava inacessível; reconferir no Planalto.","O art. 148-A, §§ 10 e 11, aparece vetado na consolidação; foram omitidos.","Trechos de lei copiados de fontes/ctb.txt por programa.","Casos ctb6a e ctb6b fictícios."],
 fontes_conferidas=["CTB, arts. 140 a 160: texto da Câmara, copiado por programa."])
gravar("ctb-6",aula_html,banco("ctb-6",Q),tx)
