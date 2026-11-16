import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='armas.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Antes de falar de registro e porte, a prova cobra vocabulário: o que é arma de porte, portátil, curta, longa, semiautomática, automática e de repetição, e o que separa o uso permitido do restrito e do proibido. Em seguida vêm os requisitos para comprar uma arma de uso permitido (art. 15): 25 anos, efetiva necessidade, idoneidade, ocupação lícita e residência certa, capacidade técnica, aptidão psicológica e cofre em casa. Para o guarda, isso aparece na rua: saber se a arma apreendida é de uso restrito ou se um simulacro é proibido muda o enquadramento da ocorrência."
S={}
S[1]="## 1. Definições que mais caem (art. 2º)\n\n"+L("art. 2º, III e IV","III - arma de fogo de porte","V - arma de fogo não portátil")+"\n\n"+L("art. 2º, VII a XI","VII - arma de fogo longa","XII - arma de fogo raiada")+"\n\n"+L("art. 2º, XIII","XIII - arma de fogo institucional","XIV - arma de fogo histórica")+"\n\n"+L("art. 2º, XXIV","XXIV - Certificado de Registro de Arma de Fogo","XXV - colecionador")+"\n\n"+L("art. 2º, XXXII","XXXII - porte de arma de fogo para defesa pessoal","XXXIII - porte de arma de fogo funcional")+"""

**O que é, em uma frase:** o art. 2º é o dicionário do decreto; a banca troca uma definição pela outra.

| Tipo | Como reconhecer |
| --- | --- |
| De porte | Disparada com **uma** mão: pistola, revólver, garrucha |
| Portátil | Uma pessoa transporta, mas não cabe no coldre; exige **ambas** as mãos |
| Longa | Ambas as mãos **com apoio no ombro** |
| Semiautomática | Faz tudo sozinha, mas **cada disparo exige novo acionamento** do gatilho |
| Automática | Dispara **continuamente** enquanto o gatilho estiver acionado |
| De repetição | O atirador usa **força física** no mecanismo entre um disparo e outro |
| Desmuniciada | Revólver: sem munição no tambor. Pistola: sem carregador e sem munição na câmara |
| Institucional | Do órgão público, **gravada com brasão** |

> **Cuidado!** CRAF é o registro **da arma** (PF ou Exército); CR é do Exército para CAC; CRPF e CRPJ são da PF para a pessoa.
"""
S[2]="## 2. Uso permitido, restrito e proibido (arts. 11 a 14)\n\n"+L("art. 11","Art. 11. São de uso permitido","Armas e munições de uso restrito")+"\n\n"+L("art. 12","Art. 12. São de uso restrito","Art. 13.")+"\n\n"+L("art. 13","Art. 13. É vedada a comercialização","Armas e munições de uso proibido")+"\n\n"+L("art. 14","Art. 14. São de uso proibido","Seção II Da aquisição")+"""

**Regra principal:** a linha divisória é a **energia na saída do cano**.

| | Permitido | Restrito |
| --- | --- | --- |
| Arma de porte | até 300 libras-pé (407 joules) | acima disso |
| Longa raiada | até 1.200 libras-pé (1.620 joules), de repetição | acima disso |
| Longa de alma lisa | calibre 12 ou inferior, de repetição | calibre acima de 12 ou **semiautomática** de qualquer calibre |
| Automática | nunca | **sempre**, qualquer calibre |
| Pressão (gás ou mola) | até 6 mm | acima de 6 mm (exceto paintball) |

> **Cai muito:** **toda arma automática é de uso restrito**, independentemente do calibre. **Simulacro que possa ser confundido com arma de fogo é de uso proibido** (salvo armas de pressão e réplicas para instrução ou coleção autorizada).
"""
S[3]="## 3. Aquisição de arma de uso permitido (arts. 15 a 19)\n\n"+L("art. 15, caput","Art. 15. A aquisição de arma de fogo de uso permitido","§ 1º O disposto no caput e no § 3º")+"\n\n"+L("art. 15, § 2º","§ 2º O interessado poderá adquirir até duas armas","§ 3º A comprovação da efetiva necessidade")+"\n\n"+L("art. 15, § 3º","§ 3º A comprovação da efetiva necessidade","§ 4º Para comprovação da idoneidade")+"\n\n"+L("art. 15, § 8º","§ 8º A autorização para aquisição","§ 9º Fica dispensado")+"\n\n"+L("art. 15, § 10","§ 10. Após a aquisição","Art. 16.")+"\n\n"+L("art. 17, § 4º","§ 4º É proibida a venda de armas de fogo adulteradas","§ 5º A concessão do CRPJ")+"\n\n"+L("art. 19, caput","Art. 19. As empresas de segurança privada","§ 1º A aquisição de armas de fogo nos termos")+"""

**Macete dos requisitos (art. 15): "25, NIO-CAP-Cofre"**
- **25** anos de idade, no mínimo;
- **N**ecessidade efetiva (não é presumida: precisa de fatos concretos);
- **I**doneidade (certidões das Justiças Federal, Estadual, Militar e Eleitoral; últimos 5 anos);
- **O**cupação lícita e residência certa;
- **CA**pacidade técnica (instrutor credenciado na PF);
- **P**sicológica (laudo de psicólogo da PF ou credenciado);
- **Cofre** ou lugar seguro com tranca, longe de menores de 18 e incapazes.

> **Cuidado!** Para defesa pessoal: **até duas armas** e **até 50 munições por arma, por ano**. A autorização para aquisição é **intransferível**, e sem **CRAF** a arma **não é entregue** ao comprador.
"""
S[5]="""## 5. Na rotina do guarda

- **Apreensão de arma automática:** é sempre de uso restrito, o que pesa no enquadramento penal (Lei 10.826/2003, art. 16).
- **Simulacro ou réplica:** se pode ser confundido com arma de fogo, é de uso proibido (art. 14, II); registre e apresente à autoridade.
- **Pistola de vigilante:** empresas de segurança privada só compram pistola de uso permitido para vigilantes em serviço (art. 19).
- **Numeração raspada:** a venda é proibida (art. 17, § 4º); a arma vai para a delegacia com o portador.
- **Arma desmuniciada:** saber a definição ajuda a descrever o estado em que a arma foi encontrada no boletim.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| "Automática de pequeno calibre é de uso permitido" | Falso: automática é restrita em qualquer calibre |
| Espingarda calibre 12 semiautomática | Restrita (alma lisa semiautomática é restrita em qualquer calibre) |
| Idade mínima para comprar arma | 25 anos, não 21 nem 18 |
| Efetiva necessidade | Não é presumida: fatos e circunstâncias concretas |
| Quantas armas para defesa pessoal | Até duas, com 50 munições por arma por ano |
| Quem autoriza a compra | Polícia Federal (autorização prévia) |
| Quem autoriza o comércio | Comando do Exército (CR) |
| Arma de pressão até 6 mm | Uso permitido |
| Simulacro confundível com arma | Uso proibido |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 2º | Definições: porte (uma mão), portátil, longa (ombro), semiautomática, automática, repetição |
| Art. 11 | Permitido: porte até 300 lb-pé; longa raiada até 1.200 lb-pé; alma lisa calibre 12 ou menos, de repetição |
| Art. 12 | Restrito: automáticas; acima dos limites; alma lisa semiautomática; não portáteis |
| Art. 13 | Comércio de restrito vedado, salvo instituições públicas, seus integrantes, atirador nível 3, caçador excepcional |
| Art. 14 | Proibido: tratados, simulacros confundíveis, armas dissimuladas, munições incendiárias ou químicas |
| Art. 15 | 25 anos, necessidade, idoneidade, ocupação e residência, capacidade técnica, aptidão psicológica, cofre |
| Art. 15, § 2º | Até 2 armas, 50 munições por arma por ano |
| Art. 17 | Comércio depende de CR do Exército; venda de arma com numeração raspada é proibida |
| Art. 19 | Segurança privada: pistola de uso permitido |
"""
QR=[("Questão 1","Nos termos do Decreto 11.615/2023, a arma de fogo automática é de uso",["restrito, independentemente do tipo ou calibre.","permitido, se de calibre reduzido.","proibido em qualquer caso.","permitido para defesa pessoal.","livre para colecionadores."],0,"Art. 12, I."),
("Questão 2","Para adquirir arma de fogo de uso permitido, o interessado deverá ter, no mínimo,",["vinte e cinco anos de idade.","dezoito anos de idade.","vinte e um anos de idade.","trinta anos de idade.","dezesseis anos de idade, se emancipado."],1,"Art. 15, I."),
("Questão 3","Arma de fogo que realiza automaticamente todas as operações de funcionamento, exceto os disparos, que dependem de novo acionamento do gatilho, é a arma",["semiautomática.","automática.","de repetição.","obsoleta.","não portátil."],2,"Art. 2º, IX."),
("Questão 4","São de uso proibido os simulacros de armas de fogo que com estas possam se confundir, exceto",["as armas de pressão e as réplicas destinadas à instrução, ao adestramento ou à coleção de usuário autorizado.","os brinquedos infantis de qualquer tipo.","os simulacros de metal.","os simulacros vendidos em lojas.","as réplicas pintadas de preto."],3,"Art. 14, II.")]
t1="<strong>O pedido de compra</strong><br><br>Um comerciante de 23 anos, sem antecedentes, procurou a Polícia Federal para comprar uma pistola de uso permitido para defesa pessoal, alegando apenas que o bairro é perigoso."
t2="<strong>A réplica na mochila</strong><br><br>Em uma abordagem, guardas municipais encontraram na mochila de um jovem uma réplica de pistola, sem marcação colorida, que podia ser confundida com uma arma verdadeira."
t3="<strong>O fuzil no porta-malas</strong><br><br>Em operação integrada, foi localizado em um veículo um fuzil que dispara continuamente enquanto o gatilho permanece acionado."
tx={"armas2a":t1,"armas2b":t2,"armas2c":t3}
# n=1
q(1,"Arma de fogo de porte é a que pode ser disparada pelo atirador com apenas uma de suas mãos, como",["pistola, revólver e garrucha.","fuzil, carabina e espingarda.","metralhadora e canhão.","espingarda e garrucha.","fuzil e revólver."],"Art. 2º, III.")
q(1,"A arma de fogo longa exige, para o disparo eficiente, ambas as mãos com apoio no",["ombro.","joelho.","chão.","coldre.","cotovelo."],"Art. 2º, VII.")
q(1,"A arma de fogo cujo disparo ocorre continuamente enquanto o gatilho estiver acionado é a",["automática.","semiautomática.","de repetição.","obsoleta.","de porte."],"Art. 2º, X.")
q(1,"A arma de fogo institucional é de propriedade, responsabilidade e guarda das instituições e dos órgãos públicos, gravada com",["brasão.","número de série apenas.","nome do servidor.","cor oficial.","código de barras."],"Art. 2º, XIII.")
q(1,"O documento comprobatório do cadastro da arma de fogo, vinculado ao proprietário e à finalidade, é o",["CRAF.","CRPJ.","CNH.","CR.","RG."],"Art. 2º, XXIV.")
q(1,"O porte de arma de fogo para defesa pessoal permite a circulação com a arma de maneira",["velada.","ostensiva.","coletiva.","livre.","escancarada."],"Art. 2º, XXXII.")
q(1,"As armas de fogo automáticas são de uso",["restrito.","permitido.","proibido.","livre.","recreativo."],"Art. 12, I.")
q(1,"É permitido o uso de armas de pressão por gás comprimido ou mola com calibre igual ou inferior a",["seis milímetros.","doze milímetros.","nove milímetros.","três milímetros.","vinte milímetros."],"Art. 11, parágrafo único.")
q(1,"As armas de fogo portáteis, longas, de alma lisa, de repetição, de calibre doze ou inferior são de uso",["permitido.","restrito.","proibido.","exclusivo das Forças Armadas.","exclusivo de colecionadores."],"Art. 11, III.")
q(1,"As armas de fogo dissimuladas, com aparência de objetos inofensivos, são de uso",["proibido.","permitido.","restrito.","livre.","esportivo."],"Art. 14, III.")
q(1,"As munições incendiárias ou químicas são de uso",["proibido.","permitido.","restrito.","livre.","esportivo."],"Art. 14, IV, b.")
q(1,"A aquisição de arma de fogo de uso permitido depende de autorização prévia da",["Polícia Federal.","Polícia Militar.","Guarda Municipal.","Polícia Civil.","Prefeitura."],"Art. 15.")
q(1,"Um dos requisitos para adquirir arma de uso permitido é comprovar a efetiva necessidade da posse ou do",["porte.","uso esportivo.","comércio.","transporte.","colecionamento."],"Art. 15, III.")
q(1,"A aptidão psicológica é atestada em laudo conclusivo fornecido por psicólogo do quadro da Polícia Federal ou por esta",["credenciado.","indicado pelo interessado.","contratado pelo Município.","eleito.","nomeado pelo juiz."],"Art. 15, VII.")
q(1,"O interessado declara que a residência possui cofre ou lugar seguro, com",["tranca.","alarme.","câmera.","cachorro.","vigia."],"Art. 15, VIII.")
q(1,"A autorização para aquisição de arma de fogo é",["intransferível.","transferível a parentes.","transferível a terceiros.","vitalícia.","negociável."],"Art. 15, § 8º.")
q(1,"É proibida a venda de armas de fogo adulteradas, sem numeração ou com numeração",["raspada.","pintada.","nova.","dupla.","estrangeira."],"Art. 17, § 4º.")
q(1,"No texto do pedido de compra, o comerciante não cumpre o requisito de idade mínima de",["vinte e cinco anos.","dezoito anos.","vinte e um anos.","trinta anos.","quarenta anos."],"Art. 15, I.","armas2a")
q(1,"No texto da réplica na mochila, a réplica que pode ser confundida com arma verdadeira é de uso",["proibido.","permitido.","restrito.","livre.","esportivo."],"Art. 14, II.","armas2b")
q(1,"No texto do fuzil no porta-malas, a arma descrita é",["automática.","semiautomática.","de repetição.","de pressão.","obsoleta."],"Art. 2º, X.","armas2c")
# n=2
q(2,"A arma de fogo portátil é a que pode ser transportada por um indivíduo, mas não conduzida em um coldre, e exige, em situações normais,",["ambas as mãos para o disparo eficiente.","apenas uma das mãos.","um suporte fixo.","um veículo.","duas pessoas."],"Art. 2º, IV.")
q(2,"A arma semiautomática difere da automática porque, na semiautomática, cada disparo depende de novo",["acionamento do gatilho.","carregamento manual do cartucho.","engatilhamento do cão.","municiamento do tambor.","apoio no ombro."],"Art. 2º, IX e X.")
q(2,"Na arma de repetição, após cada disparo, o atirador emprega sua",["força física sobre um componente do mecanismo.","energia de gás comprimido.","mola automática.","alavanca elétrica.","trava de segurança."],"Art. 2º, XI.")
q(2,"O revólver é considerado desmuniciado quando estiver sem munição no",["tambor.","carregador.","cano.","coldre.","gatilho."],"Art. 2º, VIII.")
q(2,"A arma semiautomática ou automática é considerada desmuniciada quando estiver sem carregador e sem munição na",["câmara de explosão.","coronha.","bandoleira.","maleta.","mira."],"Art. 2º, VIII.")
q(2,"É de uso permitido a arma de fogo de porte cuja munição comum tenha, na saída do cano de prova, energia de até",["trezentas libras-pé ou quatrocentos e sete joules.","mil e duzentas libras-pé.","quinhentas libras-pé.","cem libras-pé.","dois mil joules."],"Art. 11, I.")
q(2,"As armas de fogo portáteis, longas, de alma raiada, de repetição, são de uso permitido se a energia não superar",["mil e duzentas libras-pé ou mil seiscentos e vinte joules.","trezentas libras-pé.","quatrocentos e sete joules.","duas mil libras-pé.","cem joules."],"Art. 11, II.")
q(2,"As armas portáteis, longas, de alma lisa, semiautomáticas, são de uso",["restrito, de qualquer calibre.","permitido, se calibre 12.","permitido em qualquer calibre.","proibido.","livre para caçadores."],"Art. 12, V, b.")
q(2,"As armas de fogo não portáteis são de uso",["restrito.","permitido.","proibido.","livre.","doméstico."],"Art. 12, VI.")
q(2,"A comercialização de armas de uso restrito é vedada, ressalvadas as aquisições por instituições públicas, no interesse da segurança pública ou da",["defesa nacional.","economia.","cultura.","saúde.","educação."],"Art. 13, I.")
q(2,"São de uso proibido as armas assim classificadas em acordos ou tratados internacionais dos quais o Brasil seja",["signatário.","observador.","adversário.","credor.","devedor."],"Art. 14, I.")
q(2,"A idoneidade é comprovada por certidões de antecedentes das Justiças Federal, Estadual ou Distrital, Militar e",["Eleitoral.","do Trabalho.","Desportiva.","Arbitral.","Agrária."],"Art. 15, IV.")
q(2,"As certidões negativas para comprovar idoneidade referem-se aos locais de domicílio dos últimos",["cinco anos.","dois anos.","dez anos.","três anos.","doze meses."],"Art. 15, § 4º.")
q(2,"Para defesa pessoal, o interessado poderá adquirir até",["duas armas de fogo e até cinquenta munições por arma, por ano.","cinco armas e cem munições por ano.","uma arma e vinte munições.","quatro armas e duzentas munições.","três armas e mil munições."],"Art. 15, § 2º.")
q(2,"Após a aquisição, sem o CRAF a arma de fogo",["não poderá ser entregue ao adquirente.","pode ser entregue por 30 dias.","pode ser portada.","é entregue provisoriamente.","é registrada pelo vendedor."],"Art. 15, § 10.")
q(2,"A comercialização de armas de fogo por estabelecimento empresarial depende de autorização prévia do",["Comando do Exército.","Município.","Ministério da Saúde.","Banco Central.","Detran."],"Art. 17.")
q(2,"As empresas de segurança privada podem adquirir, para uso dos vigilantes em serviço, armas da espécie",["pistola, de uso permitido.","fuzil.","metralhadora.","espingarda semiautomática.","arma automática."],"Art. 19.")
q(2,"No texto do pedido de compra, além da idade, a alegação genérica de que o bairro é perigoso não atende à efetiva necessidade, pois ela",["não é presumida e exige fatos e circunstâncias concretas.","é presumida para comerciantes.","é dispensada para defesa pessoal.","é provada por boletim de outra pessoa.","é presumida em bairros perigosos."],"Art. 15, § 3º.","armas2a")
q(2,"No texto da réplica na mochila, a réplica seria permitida se fosse destinada à instrução, ao adestramento ou à",["coleção de usuário autorizado.","brincadeira infantil.","decoração.","venda.","defesa pessoal."],"Art. 14, II.","armas2b")
q(2,"No texto do fuzil no porta-malas, a arma é de uso restrito porque toda arma automática é restrita",["independentemente do tipo ou calibre.","só se calibre acima de 12.","só se longa.","só se importada.","só se não portátil."],"Art. 12, I.","armas2c")
# n=3
q(3,"Assinale a alternativa correta quanto à classificação de armas.",["Arma de pressão por mola de calibre superior a seis milímetros é de uso restrito, salvo lançadores de paintball.","Arma automática de calibre reduzido é de uso permitido.","Espingarda calibre 12 semiautomática é de uso permitido.","Simulacro confundível com arma de fogo é de uso permitido.","Arma não portátil é de uso permitido."],"Arts. 11 e 12.")
q(3,"Considere. I. Pistola com munição de até 407 joules é de uso permitido. II. Arma automática é restrita qualquer que seja o calibre. III. Munição química é de uso restrito. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"Munição química é de uso proibido (art. 14, IV, b).")
q(3,"Assinale a INCORRETA sobre a aquisição de arma de uso permitido.",["A efetiva necessidade é presumida quando o interessado reside em área de risco.","Exige idade mínima de vinte e cinco anos.","Exige comprovação de capacidade técnica.","Exige laudo de aptidão psicológica.","Exige declaração de cofre ou lugar seguro com tranca."],"Art. 15, § 3º: não é presumida.")
q(3,"O comprovante de capacidade técnica é expedido por instrutor de armamento credenciado na Polícia Federal e atesta, entre outros, o conhecimento básico dos",["componentes e das partes da arma de fogo.","tratados internacionais.","códigos de trânsito.","processos judiciais.","direitos humanos."],"Art. 15, § 5º, II.")
q(3,"Fica dispensado de comprovar capacidade técnica e aptidão psicológica o interessado que tenha porte válido de mesmo calibre e se tenha submetido a avaliação psicológica em período não superior a",["um ano.","cinco anos.","três anos.","dois anos.","seis meses."],"Art. 15, § 9º.")
q(3,"O indeferimento do pedido de aquisição pode fundamentar-se, exemplificativamente, na manutenção de vínculo do interessado com",["grupos criminosos.","partidos políticos.","sindicatos.","associações de bairro.","clubes esportivos."],"Art. 15, § 7º, III.")
q(3,"A aquisição e o registro de arma de fogo dos integrantes das Forças Armadas competem a cada órgão, e o cadastro é feito no",["Sigma.","Sinarm.","Detran.","Infoseg.","Sisbin."],"Art. 16.")
q(3,"As empresas autorizadas a comercializar armas informam ao Exército e à PF as vendas no prazo de",["quarenta e oito horas, contado da venda.","sete dias úteis.","trinta dias.","quinze dias.","um ano."],"Art. 17, § 1º.")
q(3,"Os adquirentes comunicam a aquisição à Polícia Federal e ao Comando do Exército no prazo de",["sete dias úteis, contado da aquisição.","quarenta e oito horas.","trinta dias.","noventa dias.","um ano."],"Art. 17, § 2º.")
q(3,"A aquisição de arma para caça excepcional, tiro desportivo ou colecionamento depende da apresentação de",["CR pelo interessado.","CNH.","carteira de vigilante.","CRPJ.","título de eleitor."],"Art. 18.")
q(3,"Os estabelecimentos comerciais mantêm à disposição do Exército e da PF a relação dos estoques e das vendas mensais dos últimos",["cinco anos.","dois anos.","dez anos.","doze meses.","três anos."],"Art. 17, § 7º.")
q(3,"A comercialização de arma de uso restrito é ressalvada, entre outras hipóteses, aos atiradores de nível",["3.","1.","2.","4.","5."],"Art. 13, III.")
q(3,"O caçador excepcional é pessoa física registrada pelo Comando do Exército por meio do CR, vinculada à caça para manejo de fauna",["exógena invasora.","nativa ameaçada.","doméstica.","marinha.","silvestre protegida."],"Art. 2º, XVIII.")
q(3,"O Certificado de Registro de Pessoa Física (CRPF) é concedido pela",["Polícia Federal.","Polícia Militar.","Guarda Municipal.","Receita Federal.","Prefeitura."],"Art. 2º, XXII.")
q(3,"A guia de tráfego confere autorização para o tráfego de armas",["desmuniciadas, suas munições e acessórios.","municiadas.","portadas ostensivamente.","automáticas sem registro.","de terceiros sem autorização."],"Art. 2º, XXVII.")
q(3,"No texto do pedido de compra, além de cumprir os requisitos, o comerciante, se autorizado, poderia comprar até",["duas armas para defesa pessoal.","cinco armas.","uma arma de uso restrito.","quatro armas.","dez armas."],"Art. 15, § 2º.","armas2a")
q(3,"No texto do pedido de compra, a autorização seria expedida pela",["Polícia Federal.","Guarda Municipal.","Polícia Militar.","Prefeitura.","Câmara Municipal."],"Art. 15, § 6º.","armas2a")
q(3,"No texto da réplica na mochila, a conduta adequada dos guardas é",["recolher o objeto, registrar e apresentar o caso à autoridade competente.","devolver a réplica ao jovem.","destruir a réplica no local.","liberar sem registro.","vender a réplica."],"Art. 14, II: uso proibido.","armas2b")
q(3,"No texto do fuzil no porta-malas, a comercialização desse tipo de arma é vedada, salvo, entre outras, para",["instituições públicas, no interesse da segurança pública ou da defesa nacional.","qualquer cidadão maior de 25 anos.","colecionadores de qualquer nível.","empresas de segurança privada.","clubes de futebol."],"Art. 13, I.","armas2c")
q(3,"No texto do fuzil no porta-malas, ainda que o calibre fosse pequeno, a classificação seria de uso",["restrito.","permitido.","livre.","esportivo.","recreativo."],"Art. 12, I.","armas2c")
from collections import Counter; c=Counter(x[0] for x in Q); print(c); assert c=={1:20,2:20,3:20}
code,svg=mapa("Decreto 11.615/2023: classificação e aquisição",[
 ("def","Definições (art. 2º)",["porte: uma mão","longa: apoio no ombro","semiautomática x automática"],"seção 1"),
 ("per","Uso permitido (art. 11)",["porte até 407 J","longa raiada até 1.620 J","calibre 12 de repetição"],"seção 2"),
 ("res","Uso restrito (art. 12)",["automáticas, qualquer calibre","alma lisa semiautomática","não portáteis"],"seção 2"),
 ("pro","Uso proibido (art. 14)",["simulacros confundíveis","armas dissimuladas","munição incendiária ou química"],"seção 2"),
 ("aq","Aquisição (art. 15)",["25 anos","necessidade concreta","técnica, psicológica, cofre"],"seção 3"),
 ("com","Comércio (arts. 17 e 19)",["CR do Exército","sem numeração raspada","segurança privada: pistola"],"seção 3")],
 "Na prova: automática é sempre restrita; simulacro é proibido; 25 anos")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz o vocabulário e a classificação; a segunda, a aquisição e o comércio.","Fontes: Edital 02/2026, Anexo I; Decreto 11.615/2023, texto da publicação original, Câmara dos Deputados. Exemplos criados para a aula.")
revisao("armas-2","Decreto 11.615/2023: classificação e aquisição de armas",Q,list(tx),
 cobertura=["Arts. 2º (definições selecionadas), 11 a 15, 17 a 19. Caça, tiro desportivo e colecionamento (arts. 30 a 45) cobertos só pelas definições."],
 pendencias=["Texto da publicação original (Câmara dos Deputados); conferir alterações posteriores no Planalto.","Casos armas2a, armas2b e armas2c fictícios."],
 fontes_conferidas=["Decreto 11.615/2023, arts. 2º, 11 a 15, 17 e 19: copiados por programa de fontes/armas.txt."])
gravar("armas-2",aula_html,banco("armas-2",Q),tx)
