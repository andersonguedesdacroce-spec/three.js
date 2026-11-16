import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEIS
F='amb.txt'
L=lambda ref,a,b=None: LEIS(ref,F,a,b)
Q=[]
def q(n,e,a,c,tx=None):
    assert len(a)==5 and len(set(a))==5,(e,a); Q.append((n,e,a,c,tx))
LEAD="A Lei de Crimes Ambientais (Lei 9.605/1998) começa, nos arts. 29 a 37, pelos crimes contra a fauna. É o conteúdo que o guarda municipal mais encontra: caça, maus-tratos a animais, pesca proibida. A Vunesp cobra a pena de cada crime, as causas de aumento (art. 29, § 4º), o crime de maus-tratos (art. 32, com pena maior para cão e gato, de reclusão de dois a cinco anos) e as hipóteses em que o abate de animal não é crime (art. 37)."
S={}
S[1]="## 1. Caça e fauna silvestre\n\n"+L("art. 29, caput e § 1º","Art. 29. Matar, perseguir","§ 2º No caso de guarda doméstica")+"\n\n"+L("art. 29, §§ 2º e 3º","§ 2º No caso de guarda doméstica","§ 4º A pena é aumentada")+"\n\n"+L("art. 29, §§ 4º a 6º","§ 4º A pena é aumentada de metade","Art. 30.")+"\n\n"+L("arts. 30 e 31","Art. 30. Exportar para o exterior","Art. 32.")+"""

Matar, perseguir, caçar, apanhar ou utilizar espécimes da fauna silvestre, nativos ou em rota migratória, sem permissão, licença ou autorização, ou em desacordo com a obtida, tem detenção de seis meses a um ano e multa. Nas mesmas penas incorre quem impede a procriação da fauna, modifica, danifica ou destrói ninho, abrigo ou criadouro natural, ou vende, expõe à venda, exporta, adquire, guarda, tem em cativeiro, utiliza ou transporta ovos, larvas ou espécimes da fauna silvestre ou produtos dela oriundos, de criadouros não autorizados. Na guarda doméstica de espécie silvestre não ameaçada de extinção, o juiz pode deixar de aplicar a pena.

A pena aumenta de metade se o crime é praticado contra espécie rara ou ameaçada, em período proibido à caça, durante a noite, com abuso de licença, em unidade de conservação ou com métodos capazes de provocar destruição em massa; aumenta até o triplo se decorre de caça profissional. As disposições não se aplicam aos atos de pesca. Exportar peles e couros de anfíbios e répteis em bruto sem autorização tem reclusão de um a três anos e multa; introduzir espécime animal no País sem parecer técnico e licença tem detenção de três meses a um ano e multa.
"""
S[2]="## 2. Maus-tratos a animais\n\n"+L("art. 32","Art. 32. Praticar ato de abuso","Art. 33.")+"""

Praticar ato de abuso, maus-tratos, ferir ou mutilar animais silvestres, domésticos ou domesticados, nativos ou exóticos, tem detenção de três meses a um ano e multa. Incorre nas mesmas penas quem realiza experiência dolorosa ou cruel em animal vivo, ainda que para fins didáticos ou científicos, quando existirem recursos alternativos. Quando se tratar de cão ou gato, a pena é de reclusão de dois a cinco anos, multa e proibição da guarda. Incorre nas mesmas penas quem realiza ou permite tatuagens e piercings em cães e gatos com fins estéticos, ou provoca desastre ambiental que prejudique a vida, a integridade física ou o bem-estar de animais. A pena é aumentada de um sexto a um terço se ocorre a morte do animal.
"""
S[3]="## 3. Fauna aquática, pesca e abate permitido\n\n"+L("art. 33","Art. 33. Provocar, pela emissão","Art. 34.")+"\n\n"+L("art. 34","Art. 34. Pescar em período","Art. 35.")+"\n\n"+L("arts. 35 e 36","Art. 35. Pescar mediante a utilização","Art. 37.")+"\n\n"+L("art. 37, caput e I e II","Art. 37. Não é crime o abate","III - (VETADO)")+"\n\n"+L("art. 37, IV","IV - por ser nocivo","Seção II")+"""

Provocar, pela emissão de efluentes ou carreamento de materiais, o perecimento de espécimes da fauna aquática tem detenção de um a três anos, ou multa, ou ambas cumulativamente. Pescar em período em que a pesca seja proibida ou em lugares interditados tem detenção de um a três anos ou multa, ou ambas; nas mesmas penas incorre quem pesca espécies que devam ser preservadas ou de tamanho inferior ao permitido, em quantidade superior à permitida ou por métodos proibidos, ou transporta e comercializa pescado proveniente de pesca proibida. Pescar com explosivos ou substâncias tóxicas tem reclusão de um a cinco anos.

Não é crime o abate de animal em estado de necessidade, para saciar a fome do agente ou de sua família; para proteger lavouras, pomares e rebanhos da ação predatória, desde que legal e expressamente autorizado; ou por ser nocivo o animal, desde que assim caracterizado pelo órgão competente.
"""
S[5]="""## 5. Na rotina do guarda

- **Maus-tratos a cão ou gato:** crime com reclusão de dois a cinco anos, multa e proibição da guarda; o guarda registra e conduz à autoridade.
- **Caça e pesca ilegais:** a captura sem licença ou em período proibido é crime; o guarda apreende os petrechos e comunica o órgão ambiental.
- **Fauna silvestre em cativeiro:** guardar ou transportar espécimes sem autorização é crime, salvo guarda doméstica de espécie não ameaçada, a critério do juiz.
- **Pesca com explosivos ou substâncias tóxicas:** é o crime mais grave do bloco, com reclusão de um a cinco anos.
- **Abate permitido:** estado de necessidade, defesa de lavouras com autorização e animal nocivo caracterizado pelo órgão competente.
"""
S[6]="""## 6. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Art. 29 (caça) | Detenção de 6 meses a 1 ano e multa |
| Aumento de metade | Espécie rara, período proibido, noite, abuso de licença, unidade de conservação, destruição em massa |
| Caça profissional | Aumento até o triplo |
| Art. 32 (maus-tratos) | Detenção de 3 meses a 1 ano e multa |
| Cão ou gato | Reclusão de 2 a 5 anos, multa e proibição da guarda |
| Morte do animal | Aumento de um sexto a um terço |
| Art. 34 (pesca proibida) | Detenção de 1 a 3 anos ou multa, ou ambas |
| Art. 35 (explosivos, tóxicos) | Reclusão de 1 a 5 anos |
| Art. 37 (abate) | Não é crime: fome, lavouras autorizadas, animal nocivo caracterizado |
| Pesca no art. 29 | As disposições do art. 29 não se aplicam aos atos de pesca |
"""
S[7]="""## 7. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Art. 29 | Caça: detenção de 6 meses a 1 ano e multa |
| Art. 29, § 4º | Aumento de metade |
| Art. 29, § 5º | Caça profissional: até o triplo |
| Art. 30 | Peles e couros: reclusão de 1 a 3 anos |
| Art. 31 | Introduzir espécime: detenção de 3 meses a 1 ano |
| Art. 32 | Maus-tratos: detenção de 3 meses a 1 ano; cão e gato: reclusão de 2 a 5 anos |
| Art. 33 | Fauna aquática: detenção de 1 a 3 anos, ou multa |
| Art. 34 | Pesca proibida: detenção de 1 a 3 anos |
| Art. 35 | Explosivos e tóxicos: reclusão de 1 a 5 anos |
| Art. 37 | Abate que não é crime |
"""
QR=[("Questão 1","Praticar ato de abuso, maus-tratos, ferir ou mutilar animais silvestres, domésticos ou domesticados tem pena de detenção de três meses a um ano e",["multa.","reclusão.","perda de bens.","advertência.","prisão civil."],0,"Art. 32."),
("Questão 2","Quando se tratar de cão ou gato, a pena para as condutas do caput do art. 32 é de reclusão de dois a cinco anos, multa e",["proibição da guarda.","perda do cargo.","prestação de serviços apenas.","suspensão da CNH.","fiança."],1,"Art. 32, § 1º-A."),
("Questão 3","Pescar mediante a utilização de explosivos ou substâncias tóxicas tem pena de",["reclusão de um ano a cinco anos.","detenção de seis meses.","multa apenas.","detenção de um a três anos.","reclusão de cinco a dez anos."],2,"Art. 35."),
("Questão 4","Não é crime o abate de animal em estado de necessidade, para saciar a fome do agente ou de sua",["família.","vizinhança.","empresa.","comunidade.","igreja."],3,"Art. 37, I.")]
t1="<strong>Caçador em reserva</strong><br><br>Uma equipe da Guarda Municipal de Vila Nova, cidade fictícia, encontrou à noite um homem caçando capivaras sem licença numa unidade de conservação do Município."
t2="<strong>Cachorro maltratado</strong><br><br>Em Vila Nova, um morador feriu gravemente o cachorro do vizinho com golpes de barra de ferro, e o animal morreu."
t3="<strong>Pesca com bomba</strong><br><br>Dois homens lançaram explosivos num rio de Vila Nova para pescar peixes, em período de defeso."
tx={"amb1a":t1,"amb1b":t2,"amb1c":t3}
# n=1
q(1,"Matar, perseguir, caçar ou apanhar espécimes da fauna silvestre sem a devida permissão tem pena de detenção de seis meses a",["um ano e multa.","dois anos.","três anos.","cinco anos.","dez anos."],"Art. 29.")
q(1,"A pena do art. 29 é aumentada de metade se o crime é praticado durante a",["noite.","tarde.","manhã.","hora do almoço.","semana."],"Art. 29, § 4º, III.")
q(1,"A pena do art. 29 é aumentada de metade se o crime é praticado em unidade de",["conservação.","comércio.","moradia.","lazer.","transporte."],"Art. 29, § 4º, V.")
q(1,"A pena do art. 29 é aumentada até o triplo se o crime decorre do exercício de caça",["profissional.","esportiva.","ocasional.","científica.","educativa."],"Art. 29, § 5º.")
q(1,"As disposições do art. 29 não se aplicam aos atos de",["pesca.","caça.","captura.","transporte.","venda."],"Art. 29, § 6º.")
q(1,"Exportar para o exterior peles e couros de anfíbios e répteis em bruto, sem autorização, tem pena de reclusão de um a três anos e",["multa.","perda de bens.","detenção.","advertência.","prisão civil."],"Art. 30.")
q(1,"Introduzir espécime animal no País sem parecer técnico oficial favorável e licença tem pena de detenção de três meses a",["um ano e multa.","dois anos.","três anos.","cinco anos.","seis meses."],"Art. 31.")
q(1,"Incorre nas penas do art. 32 quem realiza experiência dolorosa ou cruel em animal vivo, ainda que para fins didáticos ou científicos, quando existirem recursos",["alternativos.","financeiros.","jurídicos.","políticos.","tecnológicos novos."],"Art. 32, § 1º.")
q(1,"A pena do art. 32 é aumentada de um sexto a um terço se ocorre a",["morte do animal.","fuga.","venda.","exposição.","doação."],"Art. 32, § 2º.")
q(1,"Provocar, pela emissão de efluentes, o perecimento de espécimes da fauna aquática tem pena de detenção de um a três anos, ou multa, ou",["ambas cumulativamente.","reclusão.","advertência.","nada.","prisão perpétua."],"Art. 33.")
q(1,"Pescar em período no qual a pesca seja proibida ou em lugares interditados tem pena de detenção de um ano a três anos ou multa, ou",["ambas as penas cumulativamente.","reclusão de cinco anos.","advertência.","nada.","perda do barco apenas."],"Art. 34.")
q(1,"Pescar com explosivos ou substâncias que, em contato com a água, produzam efeito semelhante tem pena de",["reclusão de um ano a cinco anos.","detenção de seis meses a um ano.","multa.","detenção de um a três anos.","advertência."],"Art. 35, I.")
q(1,"Para os efeitos da lei, considera-se pesca todo ato tendente a retirar, extrair, coletar, apanhar, apreender ou capturar espécimes dos grupos dos peixes, crustáceos, moluscos e vegetais",["hidróbios.","terrestres.","aéreos.","fósseis.","exóticos."],"Art. 36.")
q(1,"Não é crime o abate de animal para proteger lavouras, pomares e rebanhos da ação predatória, desde que legal e expressamente autorizado pela autoridade",["competente.","local.","particular.","vizinha.","policial."],"Art. 37, II.")
q(1,"Não é crime o abate de animal por ser nocivo, desde que assim caracterizado pelo órgão",["competente.","privado.","religioso.","partidário.","esportivo."],"Art. 37, IV.")
q(1,"Nas penas do art. 29 incorre quem modifica, danifica ou destrói ninho, abrigo ou criadouro",["natural.","artificial.","privado.","público.","industrial."],"Art. 29, § 1º, II.")
q(1,"Considera-se espécime da fauna silvestre aquele que tenha todo ou parte de seu ciclo de vida dentro dos limites do território",["brasileiro.","europeu.","privado.","estadual.","municipal."],"Art. 29, § 3º.")
q(1,"No texto do caçador em reserva, a caça sem licença configura o crime do art.",["29.","32.","33.","34.","35."],"Art. 29.","amb1a")
q(1,"No texto do cachorro maltratado, ferir gravemente o cachorro configura o crime do art.",["32.","29.","33.","34.","35."],"Art. 32.","amb1b")
q(1,"No texto da pesca com bomba, o uso de explosivos configura o crime do art.",["35.","29.","32.","33.","37."],"Art. 35.","amb1c")
# n=2
q(2,"Nas mesmas penas do art. 29 incorre quem impede a procriação da fauna, sem licença, autorização ou em desacordo com a",["obtida.","norma.","lei.","regra.","ordem."],"Art. 29, § 1º, I.")
q(2,"No caso de guarda doméstica de espécie silvestre não considerada ameaçada de extinção, o juiz pode, considerando as circunstâncias, deixar de aplicar a",["pena.","multa apenas.","sentença.","lei.","prisão preventiva."],"Art. 29, § 2º.")
q(2,"A pena do art. 29 é aumentada de metade se o crime é praticado contra espécie rara ou ameaçada de extinção, ainda que somente no local da",["infração.","residência.","venda.","apreensão.","captura."],"Art. 29, § 4º, I.")
q(2,"A pena do art. 29 é aumentada de metade se o crime é praticado em período proibido à",["caça.","pesca.","venda.","exportação.","importação."],"Art. 29, § 4º, II.")
q(2,"A pena do art. 29 é aumentada de metade se o crime é praticado com abuso de",["licença.","autoridade.","poder.","confiança.","força."],"Art. 29, § 4º, IV.")
q(2,"A pena do art. 29 é aumentada de metade se o crime é praticado com emprego de métodos capazes de provocar destruição em",["massa.","série.","ordem.","cadeia.","rede."],"Art. 29, § 4º, VI.")
q(2,"Quando se tratar de cão ou gato, a pena de reclusão de dois a cinco anos é acrescida de multa e proibição da",["guarda.","venda.","caça.","pesca.","exposição."],"Art. 32, § 1º-A.")
q(2,"Incorre nas penas do art. 32 quem realiza ou permite tatuagens e piercings em cães e gatos com fins",["estéticos.","científicos.","médicos.","legais.","religiosos."],"Art. 32, § 1º-B.")
q(2,"Incorre nas penas do art. 32 quem provoca desastre ambiental que prejudique a vida, a integridade física ou o bem-estar de animais silvestres ou",["domésticos.","apenas aquáticos.","apenas exóticos.","apenas de zoológico.","apenas de fazenda."],"Art. 32, § 1º-C.")
q(2,"Incorre nas penas do art. 33 quem causa degradação em viveiros, açudes ou estações de aquicultura de domínio",["público.","privado.","estrangeiro.","familiar.","religioso."],"Art. 33, parágrafo único, I.")
q(2,"Incorre nas penas do art. 33 quem fundeia embarcações ou lança detritos sobre bancos de moluscos ou corais demarcados em carta",["náutica.","aérea.","rodoviária.","geográfica.","fiscal."],"Art. 33, parágrafo único, III.")
q(2,"Incorre nas penas do art. 34 quem pesca espécimes com tamanhos inferiores aos",["permitidos.","comuns.","esperados.","médios.","máximos."],"Art. 34, parágrafo único, I.")
q(2,"Incorre nas penas do art. 34 quem pesca mediante aparelhos, petrechos, técnicas e métodos não",["permitidos.","comuns.","novos.","antigos.","industriais."],"Art. 34, parágrafo único, II.")
q(2,"Incorre nas penas do art. 34 quem transporta, comercializa, beneficia ou industrializa espécimes provenientes da coleta, apanha e pesca",["proibidas.","permitidas.","esportivas.","científicas.","artesanais."],"Art. 34, parágrafo único, III.")
q(2,"Também configura o art. 35 pescar com substâncias tóxicas, ou outro meio proibido pela autoridade",["competente.","local.","vizinha.","religiosa.","comercial."],"Art. 35, II.")
q(2,"Não é crime o abate de animal em estado de",["necessidade.","embriaguez.","pressa.","dúvida.","festa."],"Art. 37, I.")
q(2,"No texto do caçador em reserva, a caça noturna e em unidade de conservação leva ao aumento da pena de",["metade.","um terço.","um sexto.","dobro.","triplo."],"Art. 29, § 4º.","amb1a")
q(2,"No texto do cachorro maltratado, a morte do animal enseja aumento de pena de",["um sexto a um terço.","metade.","dobro.","triplo.","nenhum."],"Art. 32, § 2º.","amb1b")
q(2,"No texto da pesca com bomba, a pesca em período de defeso também configura o art.",["34.","29.","32.","33.","37."],"Art. 34.","amb1c")
q(2,"Pescar espécies que devam ser preservadas é conduta equiparada ao crime de pescar em período proibido, previsto no art.",["34.","29.","32.","33.","35."],"Art. 34, parágrafo único, I.")
# n=3
q(3,"Assinale a alternativa correta sobre o art. 32.",["O caput tem detenção de três meses a um ano e multa; para cão ou gato, reclusão de dois a cinco anos, multa e proibição da guarda.","Para cão ou gato, a pena é a mesma do caput.","O caput tem reclusão de dois a cinco anos.","A morte do animal não aumenta a pena.","Só abrange animais silvestres."],"Art. 32.")
q(3,"Considere. I. A pesca com explosivos tem reclusão de 1 a 5 anos. II. A caça profissional aumenta a pena até o triplo. III. O art. 29 aplica-se aos atos de pesca. Está correto o que se afirma em",["I e II, apenas.","I, apenas.","II, apenas.","II e III, apenas.","I, II e III."],"O art. 29 não se aplica aos atos de pesca (§ 6º).")
q(3,"Assinale a INCORRETA.",["É crime o abate de animal apenas para proteger lavouras, sem autorização.","Não é crime o abate para saciar a fome.","Não é crime o abate de animal nocivo caracterizado pelo órgão competente.","Não é crime o abate em estado de necessidade.","Não é crime o abate para proteger rebanhos, com autorização."],"A proteção de lavouras exige autorização expressa (art. 37, II).")
q(3,"A pena do art. 33 é de detenção de um a três anos, ou multa, ou ambas cumulativamente, e o crime consiste em provocar o perecimento de espécimes da fauna aquática pela emissão de efluentes ou carreamento de",["materiais.","pescadores.","embarcações.","redes.","iscas."],"Art. 33.")
q(3,"A explotação de campos naturais de invertebrados aquáticos e algas sem licença é conduta equiparada no art.",["33, parágrafo único, II.","29.","32.","34.","35."],"Art. 33, parágrafo único, II.")
q(3,"O art. 34 pune pescar em período no qual a pesca seja proibida ou em lugares",["interditados por órgão competente.","privados.","distantes.","rasos.","urbanos."],"Art. 34.")
q(3,"A pena do art. 34 é de detenção de",["um a três anos ou multa, ou ambas as penas cumulativamente.","seis meses a um ano.","reclusão de dois a cinco anos.","multa apenas.","dez anos."],"Art. 34.")
q(3,"A pena do art. 30 é de reclusão de um a três anos e multa, sendo a conduta a exportação de peles e couros de anfíbios e répteis",["em bruto, sem autorização.","manufaturados.","prontos.","doados.","apreendidos."],"Art. 30.")
q(3,"Entre as condutas equiparadas ao art. 29 está vender, expor à venda, exportar ou adquirir espécimes da fauna silvestre de criadouros",["não autorizados.","autorizados.","públicos.","científicos.","escolares."],"Art. 29, § 1º, III.")
q(3,"O art. 29 pune a conduta de caçar espécimes da fauna silvestre, nativos ou em rota",["migratória.","urbana.","rural.","aquática.","aérea."],"Art. 29.")
q(3,"Nas hipóteses do art. 29, as penas são aplicadas ao agente que mata, persegue, caça, apanha ou utiliza espécimes",["sem permissão, licença ou autorização da autoridade competente.","com licença válida.","em zoológico autorizado.","em criadouro autorizado.","com autorização do vizinho."],"Art. 29.")
q(3,"A pena do art. 32, § 1º-A, é reclusão de dois a cinco anos, multa e proibição da guarda, quando se tratar de",["cão ou gato.","ave.","réptil.","cavalo.","peixe."],"Art. 32, § 1º-A.")
q(3,"O art. 36 define pesca excluindo as espécies ameaçadas de extinção constantes nas listas oficiais da fauna e da",["flora.","pesca.","caça.","mineração.","agricultura."],"Art. 36.")
q(3,"No texto do caçador em reserva, a pena-base é de detenção de seis meses a um ano e multa, aumentada de",["metade, pelas causas do § 4º.","um sexto.","triplo.","dobro.","um terço."],"Art. 29, § 4º.","amb1a")
q(3,"No texto do caçador em reserva, a caça de capivara sem licença, por si, é conduta de",["caça de espécime silvestre sem autorização.","pesca.","maus-tratos.","exportação.","introdução."],"Art. 29.","amb1a")
q(3,"No texto do cachorro maltratado, a conduta é grave porque o animal é cão, e a pena é de",["reclusão de dois a cinco anos, multa e proibição da guarda.","detenção de três meses a um ano.","multa apenas.","detenção de seis meses.","advertência."],"Art. 32, § 1º-A.","amb1b")
q(3,"No texto do cachorro maltratado, o crime é de maus-tratos, previsto também contra animais domésticos ou",["domesticados.","apenas silvestres.","apenas exóticos.","apenas aquáticos.","apenas de zoológico."],"Art. 32.","amb1b")
q(3,"No texto da pesca com bomba, o uso de explosivos tem pena de",["reclusão de um a cinco anos.","detenção de seis meses a um ano.","multa apenas.","detenção de um a três anos.","advertência."],"Art. 35.","amb1c")
q(3,"No texto da pesca com bomba, a pesca em época proibida é punida com detenção de um a três anos ou",["multa, ou ambas cumulativamente.","reclusão de cinco anos.","advertência.","nada.","perda do barco apenas."],"Art. 34.","amb1c")
q(3,"A pena do art. 29 é aumentada de metade, entre outros casos, se o crime é praticado contra espécie rara ou considerada ameaçada de extinção, ainda que somente no",["local da infração.","país.","continente.","mundo.","bioma."],"Art. 29, § 4º, I.")
from collections import Counter; print(Counter(x[0] for x in Q))
assert len(Q)==60,len(Q)
code,svg=mapa("Crimes ambientais: fauna (arts. 29 a 37)",[
 ("caç","Caça (art. 29)",["detenção 6m a 1a","aumento de metade","caça profissional: triplo"],"seção 1"),
 ("exp","Exportar e introduzir",["peles e couros: reclusão","introduzir espécime: detenção"],"seção 1"),
 ("mau","Maus-tratos (art. 32)",["detenção 3m a 1a","cão e gato: reclusão 2 a 5","morte: +1/6 a 1/3"],"seção 2"),
 ("aqu","Fauna aquática",["efluentes: art. 33","pesca proibida: art. 34"],"seção 3"),
 ("exl","Pesca com explosivos",["art. 35","reclusão de 1 a 5 anos"],"seção 3"),
 ("aba","Abate que não é crime",["estado de necessidade","lavouras com autorização","animal nocivo"],"seção 3")],
 "Na prova: penas, aumento de metade e abate permitido")
aula_html=aula(LEAD,S,[1,2,3,'QR',5,6,7],QR,4,svg,"A primeira linha traz a caça; as demais, os maus-tratos, a pesca e as hipóteses em que o abate não é crime.","Fontes: Edital 02/2026, Anexo I; Lei 9.605/1998 (Lei de Crimes Ambientais), arts. 29 a 37, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.")
revisao("amb-1","Crimes ambientais: fauna (arts. 29 a 37)",Q,list(tx),
 cobertura=["Todos os artigos do recorte (29 a 37)."],
 pendencias=["Texto-fonte: consolidação da Câmara dos Deputados (Legin), baixada em 14/11/2026; reconferir no Planalto.","O art. 37, III, aparece vetado e foi omitido.","Trechos de lei copiados de fontes/amb.txt por programa.","Casos amb1a, amb1b e amb1c fictícios."],
 fontes_conferidas=["Lei 9.605/1998, arts. 29 a 37: texto da Câmara, copiado por programa."])
gravar("amb-1",aula_html,banco("amb-1",Q),tx)
