import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='armas.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="Posse e porte são coisas diferentes, e a banca vive trocando uma pela outra. Posse é manter a arma registrada (CRAF) dentro de casa ou do próprio local de trabalho. Porte é poder circular com ela, e para o cidadão comum é excepcional, pessoal, intransferível e sempre velado. Esta aula reúne o registro (CRAF: validade, renovação, cassação e falecimento do dono), a guia de tráfego e o porte para defesa pessoal, incluindo os locais onde o portador não pode entrar armado e a suspensão cautelar por perda da aptidão psicológica."
S={}
S[1]="## 1. Registro e posse: o CRAF (arts. 20 a 24)\n\n"+L("art. 23, caput","Art. 23. O CRAF tem validade no território nacional","Parágrafo único. Para fins do disposto no caput, considera-se")+"\n\n"+L("art. 24, caput","Art. 24. O CRAF terá o seguinte prazo","§ 1º Para fins de manutenção do CRAF")+"\n\n"+L("art. 21, parágrafo único","Parágrafo único. A guia de tráfego não autoriza","Transferência da propriedade de armas")+"\n\n"+L("art. 20, caput","Art. 20. O titular de CR, CRPF ou CRPJ","Parágrafo único. Independentemente da obrigação")+"""

**O que é, em uma frase:** posse é ter a arma registrada **dentro** de casa ou do próprio trabalho; não autoriza sair com ela.

| Quem | Validade do CRAF |
| --- | --- |
| Colecionador, atirador, caçador excepcional (CAC) | **3 anos** |
| Posse (defesa) ou caça de subsistência | **5 anos** |
| Empresa de segurança privada | **5 anos** |
| Integrantes da ativa de instituições do art. 7º, § 1º, IV | **Prazo indeterminado** |

> **Cuidado!** "Local de trabalho" só vale se a pessoa for **titular ou responsável legal** pelo estabelecimento. Empregado comum não pode manter a arma no trabalho.

> **Cai muito:** a **guia de tráfego não é porte**: só autoriza o transporte da arma **desmuniciada**, acondicionada e no percurso autorizado.
"""
S[2]="## 2. Renovação, cassação e falecimento (arts. 25 a 29)\n\n"+L("art. 26, caput","Art. 26. Na hipótese de o CRAF não ser renovado","§ 1º Em caso de inércia do proprietário")+"\n\n"+L("art. 28, caput","Art. 28. O procedimento de cassação do CRAF","§ 1º Instaurado o procedimento de cassação")+"\n\n"+L("art. 28, § 2º","§ 2º São elementos que demonstram a perda","§ 3º O disposto no § 2º")+"\n\n"+L("art. 28, § 5º","§ 5º Nos casos de ação penal ou de inquérito policial","§ 6º Na hipótese de cassação do CRAF")+"\n\n"+L("art. 29, § 1º","§ 1º O administrador da herança ou o curador comunicará","§ 2º Na hipótese prevista no inciso I do caput, a arma")+"""

**Linha do tempo dos prazos**

| Situação | Prazo |
| --- | --- |
| Informar alteração de dados cadastrais | **15 dias** |
| Notificado por CRAF vencido: entregar, transferir ou renovar | **60 dias** |
| Notificado da cassação: escolher entregar ou transferir | **15 dias** |
| Comunicar morte ou interdição do dono | **90 dias** |

> **Cai muito:** perde a idoneidade quem tem **mandado de prisão**, é **indiciado** em inquérito por crime ou tem **denúncia ou queixa recebida**. Em **violência doméstica contra a mulher**, a arma é **apreendida imediatamente**.
"""
S[3]="## 3. Porte para defesa pessoal (arts. 46 a 52 e 62)\n\n"+L("art. 46, caput","Art. 46. O porte de arma de fogo de uso permitido","Parágrafo único. Caberá ao Diretor-Geral")+"\n\n"+L("art. 48","Art. 48. O porte de arma de fogo é pessoal","Expedição do porte de arma")+"\n\n"+L("art. 50","Art. 50. O titular do porte","Art. 51.")+"\n\n"+L("art. 51","Art. 51. O titular de porte de arma de fogo para defesa pessoal","Porte de arma para integrantes de missões")+"\n\n"+L("art. 62, caput","Art. 62. O CRAF e a autorização para porte","§ 1º Na hipótese prevista no caput, haverá")+"""

**Regra principal:** o porte do cidadão é **excepcional**, expedido pela **Polícia Federal**, **pessoal, intransferível e revogável a qualquer tempo**, e vale só para a arma nele especificada, com documento de identidade.

**Exceções e pegadinhas**
- **Proibido** portar **ostensivamente** e entrar ou permanecer armado em igrejas, escolas, estádios, clubes, agências bancárias e locais com aglomeração. Consequência: **cassação** do porte e **apreensão** da arma.
- A mesma consequência vale para quem porta a arma **embriagado** ou sob efeito de drogas ou de medicamentos que alterem o desempenho.
- Extravio, furto ou roubo: comunicar **imediatamente** à unidade policial mais próxima **e** à Polícia Federal; não comunicar gera **suspensão** do porte.
- **Diplomatas** e seguranças de dignitários estrangeiros: porte pela PF, por **reciprocidade**, sem os requisitos do decreto.
"""
S[5]="""## 5. Na rotina do guarda

- **Cidadão armado na rua:** peça o **porte** e o documento de identidade; o CRAF sozinho só autoriza a posse em casa ou no próprio estabelecimento.
- **Armado em estádio, escola, igreja ou banco:** o portador civil perde o porte (cassação) e a arma é apreendida (art. 51).
- **Portador embriagado:** mesma consequência (art. 51, § 2º).
- **Transporte com guia de tráfego:** a arma precisa estar desmuniciada e no percurso autorizado; fora disso, não há porte.
- **Violência doméstica:** a arma do agressor é apreendida imediatamente (art. 28, § 5º; Lei Maria da Penha, art. 18, IV).
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| "O CRAF autoriza levar a arma no carro" | Falso: posse só dentro de casa ou do próprio trabalho |
| Guia de tráfego = porte | Falso: só transporte desmuniciado no percurso |
| Validade do CRAF para posse | 5 anos (CAC: 3 anos) |
| Porte de defesa pessoal | Excepcional, pessoal, intransferível e revogável |
| Portar arma ostensivamente | Proibido ao porte de defesa pessoal |
| Arma em clube ou estádio | Cassação do porte e apreensão |
| Comunicação de furto da arma | Imediata, à polícia local e à PF |
| Falecimento do dono | Comunicar em 90 dias |
| Suspensão cautelar por sinais de perda da aptidão psicológica | Apreensão imediata, mesmo com laudo válido |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 20 | Alteração cadastral: 15 dias |
| Art. 21 | Guia de tráfego: transporte desmuniciado, não porte |
| Art. 23 | CRAF: nacional; arma só em casa ou no próprio trabalho |
| Art. 24 | Validade: CAC 3 anos; posse e segurança privada 5 anos |
| Art. 26 | CRAF vencido: 60 dias para entregar, transferir ou renovar |
| Art. 28 | Cassação; idoneidade perdida; violência doméstica: apreensão imediata |
| Art. 29 | Morte ou interdição: comunicar em 90 dias |
| Arts. 46 a 48 | Porte pela PF, excepcional, pessoal, intransferível, revogável |
| Art. 50 | Comunicar mudança de domicílio e extravio, furto ou roubo |
| Art. 51 | Nada de porte ostensivo nem em locais de aglomeração; embriaguez |
| Art. 62 | Suspensão cautelar por sinais de perda da aptidão psicológica |
"""
QR=[("Questão 1","Nos termos do Decreto 11.615/2023, o CRAF autoriza o proprietário a manter a arma de fogo",["exclusivamente no interior de sua residência ou dependências, ou de seu local de trabalho, se for o titular ou responsável legal.","em qualquer lugar do território nacional.","no veículo, desde que desmuniciada.","em local público, de forma velada.","em qualquer local de trabalho, mesmo como empregado."],0,"Art. 23."),
("Questão 2","O CRAF concedido para fins de posse de arma de fogo tem validade de",["cinco anos.","três anos.","dez anos.","um ano.","prazo indeterminado."],1,"Art. 24, II."),
("Questão 3","A guia de tráfego",["não autoriza o porte, apenas o transporte da arma desmuniciada, no percurso autorizado.","autoriza o porte por 30 dias.","autoriza o porte em todo o território nacional.","substitui o CRAF.","autoriza o transporte da arma municiada."],2,"Art. 21, parágrafo único."),
("Questão 4","O titular de porte para defesa pessoal que adentra estádio desportivo armado sujeita-se à",["cassação do porte e à apreensão da arma.","advertência verbal.","multa de trânsito.","suspensão por 15 dias, sem apreensão.","renovação obrigatória do CRAF."],3,"Art. 51, § 1º.")]
t1="<strong>A arma no carro</strong><br><br>Em uma blitz, um motorista apresentou, para a pistola que levava no console, apenas o CRAF em seu nome, dizendo que o registro bastava."
t2="<strong>O torcedor armado</strong><br><br>Um homem com porte de arma para defesa pessoal tentou entrar armado em um estádio em dia de jogo e foi barrado na revista."
t3="<strong>A herança</strong><br><br>Após a morte do pai, que tinha uma espingarda registrada, a filha, administradora da herança, ficou em dúvida sobre o que fazer com a arma."
tx={"armas3a":t1,"armas3b":t2,"armas3c":t3}
# n=1
q(1,"O CRAF tem validade no território",["nacional.","estadual.","municipal.","distrital.","regional."],"Art. 23.")
q(1,"O CRAF autoriza manter a arma no interior da residência ou",["dependências desta.","do veículo.","da via pública.","do clube.","do shopping."],"Art. 23.")
q(1,"O CRAF concedido a colecionador, atirador desportivo ou caçador excepcional tem validade de",["três anos.","cinco anos.","dez anos.","um ano.","dois anos."],"Art. 24, I.")
q(1,"O CRAF concedido a empresa de segurança privada tem validade de",["cinco anos.","três anos.","um ano.","dez anos.","prazo indeterminado."],"Art. 24, III.")
q(1,"A guia de tráfego autoriza apenas o",["transporte da arma.","porte da arma.","uso da arma.","disparo da arma.","comércio da arma."],"Art. 21, parágrafo único.")
q(1,"O titular de CR, CRPF ou CRPJ deve informar alteração em seus dados cadastrais no prazo de",["quinze dias.","sete dias.","trinta dias.","sessenta dias.","noventa dias."],"Art. 20.")
q(1,"É proibida a renovação do CRAF de armas adulteradas, sem numeração ou com numeração",["raspada.","nova.","dupla.","pintada.","estrangeira."],"Art. 25, § 3º.")
q(1,"Se o CRAF não for renovado no prazo, o proprietário será notificado, por meio eletrônico, para agir no prazo de",["sessenta dias.","quinze dias.","trinta dias.","noventa dias.","dez dias."],"Art. 26.")
q(1,"Nos casos de violência doméstica e familiar contra a mulher, a arma será apreendida",["imediatamente.","em 30 dias.","após o trânsito em julgado.","apenas se o agressor concordar.","somente se houver disparo."],"Art. 28, § 5º.")
q(1,"O administrador da herança comunica a morte do proprietário da arma no prazo de",["noventa dias.","quinze dias.","trinta dias.","sessenta dias.","um ano."],"Art. 29, § 1º.")
q(1,"O porte de arma de fogo de uso permitido para defesa pessoal é expedido pela",["Polícia Federal.","Polícia Militar.","Guarda Municipal.","Polícia Civil.","Prefeitura."],"Art. 46.")
q(1,"O porte para defesa pessoal é expedido em caráter",["excepcional.","geral.","automático.","obrigatório.","hereditário."],"Art. 46.")
q(1,"O porte de arma de fogo é pessoal, intransferível e",["revogável a qualquer tempo.","vitalício.","hereditário.","irrevogável.","negociável."],"Art. 48.")
q(1,"O porte é válido apenas em relação à arma nele especificada, mediante apresentação do documento de",["identificação do portador.","propriedade do veículo.","residência.","quitação eleitoral.","trabalho."],"Art. 48.")
q(1,"O titular de porte para defesa pessoal não poderá conduzir a arma",["ostensivamente.","de forma velada.","em sua residência.","desmuniciada.","no coldre."],"Art. 51.")
q(1,"O titular do porte deve comunicar imediatamente o furto da arma à unidade policial mais próxima e à",["Polícia Federal.","Prefeitura.","Receita Federal.","Câmara Municipal.","Defensoria."],"Art. 50, II.")
q(1,"O porte a diplomatas estrangeiros pode ser autorizado pela PF com base no princípio da",["reciprocidade.","territorialidade.","anterioridade.","legalidade tributária.","insignificância."],"Art. 52.")
q(1,"No texto da arma no carro, o CRAF apresentado autoriza apenas a",["posse dentro de casa ou do próprio local de trabalho.","condução da arma em veículo.","circulação velada.","circulação ostensiva.","entrega a terceiros."],"Art. 23.","armas3a")
q(1,"No texto do torcedor armado, o local onde ele tentou entrar armado é",["vedado ao portador de defesa pessoal.","permitido se a arma estiver velada.","permitido em dia de jogo.","permitido com o CRAF.","permitido com guia de tráfego."],"Art. 51.","armas3b")
q(1,"No texto da herança, a filha deve comunicar a morte do pai à autoridade competente no prazo de",["noventa dias.","quinze dias.","sessenta dias.","trinta dias.","um ano."],"Art. 29, § 1º.","armas3c")
# n=2
q(2,"Considera-se interior da residência toda a extensão da área particular registrada do imóvel, edificada ou não, em que resida o titular,",["inclusive quando se tratar de imóvel rural.","exceto se rural.","apenas a área construída.","apenas o quarto do titular.","apenas a garagem."],"Art. 23, parágrafo único, I.")
q(2,"O CRAF autoriza manter a arma no local de trabalho desde que o proprietário seja",["o titular ou responsável legal pelo estabelecimento ou pela empresa.","qualquer empregado.","estagiário.","cliente habitual.","vizinho do estabelecimento."],"Art. 23.")
q(2,"O CRAF concedido para caça de subsistência tem validade de",["cinco anos.","três anos.","dez anos.","um ano.","prazo indeterminado."],"Art. 24, II.")
q(2,"Para manutenção do CRAF, as empresas de segurança privada submetem seus funcionários à avaliação psicológica a cada",["três anos.","cinco anos.","um ano.","dez anos.","seis meses."],"Art. 24, § 1º, I.")
q(2,"A guia de tráfego autoriza o transporte da arma desmuniciada e acondicionada de maneira a não ser feito uso, e somente",["no percurso nela autorizado.","no Estado.","no Município.","em todo o território nacional.","durante o dia."],"Art. 21, parágrafo único.")
q(2,"Na mudança de domicílio, o proprietário solicita à Polícia Federal ou ao Comando do Exército a",["guia de tráfego.","renovação do porte.","certidão de óbito.","CNH.","transferência de propriedade."],"Art. 21.")
q(2,"A transferência de propriedade de arma de uso permitido cadastrada no Sinarm depende de autorização prévia da",["Polícia Federal.","Guarda Municipal.","Polícia Militar.","Prefeitura.","Câmara."],"Art. 22.")
q(2,"Notificado do CRAF vencido, o proprietário pode, no prazo legal, entregar a arma à PF mediante indenização, transferi-la a terceiro ou",["renovar o registro.","vendê-la livremente.","doá-la a menor.","guardá-la sem registro.","levá-la ao exterior."],"Art. 26.")
q(2,"Em caso de inércia após a notificação, instaura-se cassação do CRAF e o proprietário não poderá, entre outros, obter a emissão ou a renovação de",["passaporte.","CNH.","título de eleitor.","RG.","CPF."],"Art. 26, § 2º, II.")
q(2,"O procedimento de cassação do CRAF é instaurado de ofício ou mediante",["denúncia.","sorteio.","pagamento.","plebiscito.","eleição."],"Art. 28.")
q(2,"Demonstra a perda do requisito de idoneidade, entre outros, o",["indiciamento em inquérito policial pela prática de crime.","recebimento de multa de trânsito.","atraso no IPTU.","divórcio.","desemprego."],"Art. 28, § 2º.")
q(2,"Cassado o CRAF, o proprietário é notificado para, em quinze dias, manifestar interesse na entrega da arma à PF ou na",["transferência a terceiro.","renovação automática.","destruição pessoal.","doação ao Município.","guarda em casa."],"Art. 28, § 6º.")
q(2,"O porte de arma de fogo é documento obrigatório para a condução da arma e contém, entre outros dados, a abrangência territorial e a",["eficácia temporal.","renda do portador.","religião do portador.","profissão do vendedor.","cor do veículo."],"Art. 47.")
q(2,"A falta de comunicação da mudança de domicílio ou do furto da arma implica",["suspensão do porte pelo prazo estabelecido pela autoridade.","advertência verbal.","multa de trânsito.","prisão em flagrante.","nada."],"Art. 50, parágrafo único.")
q(2,"O titular de porte para defesa pessoal não pode entrar ou permanecer armado em",["igrejas, escolas, estádios, clubes e agências bancárias.","sua residência.","seu veículo.","lojas de conveniência isoladas.","ruas residenciais."],"Art. 51.")
q(2,"A cassação do porte e a apreensão da arma aplicam-se também ao titular que porta o armamento",["em estado de embriaguez.","desmuniciado.","em casa.","com o documento.","de forma velada."],"Art. 51, § 2º.")
q(2,"O CRAF e o porte podem ser suspensos cautelarmente, a qualquer tempo, em razão de sinais exteriores da perda da aptidão",["psicológica.","financeira.","técnica.","física.","eleitoral."],"Art. 62.")
q(2,"No texto da arma no carro, para conduzir a pistola o motorista precisaria do",["porte de arma de fogo.","CRAF apenas.","certificado de propriedade do veículo.","título de eleitor.","comprovante de residência."],"Arts. 23 e 47.","armas3a")
q(2,"No texto do torcedor armado, a consequência prevista é",["a cassação do porte e a apreensão da arma.","apenas advertência.","suspensão por 30 dias, sem apreensão.","multa administrativa.","renovação do CRAF."],"Art. 51, § 1º.","armas3b")
q(2,"No texto da herança, a filha pode providenciar a transferência da arma, por alvará judicial ou autorização dos herdeiros maiores e capazes, ou",["entregá-la à Polícia Federal, mediante indenização.","ficar com ela sem registro.","vendê-la a qualquer pessoa.","jogá-la fora.","enterrá-la com o pai."],"Art. 29.","armas3c")
# n=3
q(3,"Assinale a alternativa correta.",["O CRAF dos integrantes da ativa das instituições do art. 7º, § 1º, IV, tem prazo indeterminado.","O CRAF de colecionador vale cinco anos.","O CRAF de posse vale três anos.","O CRAF de empresa de segurança privada vale dez anos.","O CRAF vale apenas no Estado."],"Art. 24.")
q(3,"Considere. I. A guia de tráfego autoriza o porte no percurso. II. O CRAF tem validade nacional. III. O porte de defesa pessoal é revogável a qualquer tempo. Está correto o que se afirma em",["II e III, apenas.","I, apenas.","I e II, apenas.","III, apenas.","I, II e III."],"Arts. 21, 23 e 48.")
q(3,"Assinale a INCORRETA.",["A comunicação do furto da arma pode ser feita em até 90 dias.","O porte é pessoal e intransferível.","O porte é revogável a qualquer tempo.","O porte vale só para a arma nele especificada.","O porte é expedido pela Polícia Federal."],"Art. 50: comunicação imediata.")
q(3,"No procedimento de renovação do CRAF, o interessado cumpre os requisitos dos incisos III a VII do art. 15, e a inobservância do prazo de renovação",["poderá acarretar a cassação do CRAF.","gera renovação automática.","dispensa os requisitos.","gera multa de trânsito.","não tem consequência."],"Art. 25.")
q(3,"A apreensão da arma, quando a perda de idoneidade decorre de indiciamento ou denúncia, é de responsabilidade da",["polícia judiciária competente para investigar o crime motivador da cassação.","Guarda Municipal.","Receita Federal.","Prefeitura.","empresa de segurança."],"Art. 28, § 4º.")
q(3,"As hipóteses de perda de idoneidade do art. 28, § 2º, alcançam",["todas as armas de propriedade do indiciado ou acusado.","apenas a arma usada no crime.","apenas armas de uso restrito.","apenas a primeira arma registrada.","nenhuma arma."],"Art. 28, § 3º.")
q(3,"Instaurado o procedimento de cassação, a autoridade pode suspender cautelarmente o CRPF ou CRPJ, os CRAF e o porte, com",["imediata apreensão administrativa da arma, dos acessórios e das munições.","apreensão apenas após o trânsito em julgado.","aviso de 60 dias.","multa apenas.","manutenção da arma com o titular."],"Art. 28, § 1º.")
q(3,"Na transferência por herança, a arma permanece sob guarda do administrador da herança ou curador, em local seguro, até a",["expedição do CRAF e a entrega ao novo proprietário.","partilha dos bens.","missa de sétimo dia.","venda do imóvel.","decisão do Município."],"Art. 29, § 2º.")
q(3,"Na suspensão cautelar por sinais de perda da aptidão psicológica, a apreensão da arma ocorre",["independentemente de laudo de aptidão psicológica válido.","apenas se o laudo estiver vencido.","após recurso.","apenas com ordem judicial.","só após 60 dias."],"Art. 62, § 1º.")
q(3,"Para recorrer da suspensão cautelar por perda da aptidão psicológica, o interessado submete-se previamente, às suas expensas, a exame perante junta de",["três psicólogos credenciados pela PF.","um médico do SUS.","dois policiais.","cinco juízes.","um psiquiatra particular."],"Art. 62, § 1º.")
q(3,"As regras de suspensão cautelar do art. 62, §§ 1º a 3º, não se aplicam aos agentes públicos e políticos com",["porte por prerrogativa de função.","CRAF de colecionador.","guia de tráfego.","porte para defesa pessoal.","CR de atirador."],"Art. 62, § 4º.")
q(3,"Compete às instituições públicas com armas recolher cautelarmente as armas do servidor com sinais de falta de condição psicológica e submetê-lo a",["junta médica oficial.","exame de vista.","prova de tiro.","curso de reciclagem.","julgamento popular."],"Art. 63.")
q(3,"O porte para defesa pessoal é vinculado à prévia expedição de CRAF e ao cadastro no",["Sinarm.","Sigma.","Detran.","Renach.","Infoseg."],"Art. 46.")
q(3,"Entre os dados do documento de porte estão o número do cadastro da arma no Sinarm e a assinatura, o cargo e a função da",["autoridade concedente.","testemunha.","pessoa vendedora.","empresa fabricante.","loja."],"Art. 47, IV e VI.")
q(3,"A falta de renovação do CRAF e a inércia após notificação podem levar o proprietário a incorrer nos crimes da Lei 10.826/2003, arts.",["12 e 14.","16 e 17.","18 e 19.","1º e 2º.","30 e 31."],"Art. 26, § 1º.")
q(3,"No texto da arma no carro, o motorista que transporta arma de uso permitido fora de casa, só com CRAF, pode responder por",["porte ilegal de arma de fogo de uso permitido (Lei 10.826/2003, art. 14).","nenhum crime, pois tem CRAF.","contravenção de vadiagem.","crime de trânsito.","infração ambiental."],"Arts. 23 do decreto e 14 da Lei.","armas3a")
q(3,"No texto da arma no carro, se o motorista estivesse se mudando, o documento adequado para o transporte seria a",["guia de tráfego, com a arma desmuniciada e no percurso autorizado.","CNH.","nota fiscal da arma.","declaração de vizinhos.","certidão de casamento."],"Art. 21.","armas3a")
q(3,"No texto do torcedor armado, ainda que a arma estivesse oculta, a entrada seria vedada porque o art. 51 proíbe",["adentrar ou permanecer armado em locais com aglomeração de pessoas, como estádios.","apenas o porte ostensivo.","apenas o porte noturno.","apenas armas automáticas.","apenas a entrada sem ingresso."],"Art. 51.","armas3b")
q(3,"No texto da herança, se a filha deixar de comunicar a morte no prazo e de guardar a arma em local seguro, haverá",["apreensão da arma, sem prejuízo das sanções penais.","renovação automática do CRAF.","transferência automática.","perda da herança.","nada."],"Art. 29, § 3º.","armas3c")
q(3,"No texto da herança, a transferência da arma a um herdeiro exige que ele",["atenda aos requisitos do art. 15 para aquisição.","seja maior de 18 anos apenas.","more na mesma casa.","seja policial.","pague imposto especial."],"Art. 29, I.","armas3c")
from collections import Counter; c=Counter(x[0] for x in Q); print(c); assert c=={1:20,2:20,3:20}
code,svg=mapa("Decreto 11.615/2023: registro, posse e porte",[
 ("craf","CRAF (posse)",["validade nacional","só em casa ou no próprio trabalho","CAC 3 anos; posse 5 anos"],"seção 1"),
 ("gt","Guia de tráfego",["não é porte","arma desmuniciada","só no percurso"],"seção 1"),
 ("cas","Cassação",["perda de requisito","indiciamento ou denúncia","violência doméstica: apreensão"],"seção 2"),
 ("pra","Prazos",["15 dias: dados","60 dias: CRAF vencido","90 dias: morte do dono"],"seção 2"),
 ("por","Porte (defesa pessoal)",["PF, excepcional","pessoal, intransferível, revogável","só velado"],"seção 3"),
 ("ved","Vedações",["estádios, escolas, igrejas, bancos","embriaguez","cassação e apreensão"],"seção 3")],
 "Na prova: posse fica em casa; porte circula; guia de tráfego só transporta")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha trata do registro e da posse; a segunda, da cassação, dos prazos e do porte.","Fontes: Edital 02/2026, Anexo I; Decreto 11.615/2023, texto da publicação original, Câmara dos Deputados. Exemplos criados para a aula.")
revisao("armas-3","Decreto 11.615/2023: registro, posse e porte",Q,list(tx),
 cobertura=["Arts. 20 a 29, 46 a 52, 62 e 63."],
 pendencias=["Texto da publicação original (Câmara dos Deputados); conferir alterações posteriores no Planalto.","Questões que citam a Lei 10.826/2003, arts. 12 e 14, usam a remissão do próprio decreto (art. 26, § 1º).","Casos armas3a, armas3b e armas3c fictícios."],
 fontes_conferidas=["Decreto 11.615/2023, arts. 20 a 29, 46 a 52 e 62: copiados por programa de fontes/armas.txt."])
gravar("armas-3",aula_html,banco("armas-3",Q),tx)
