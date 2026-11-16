# Revisão do posto cpp-1: Inquérito policial (CPP, arts. 4º a 23)

## Resumo

- Banco: 60 questões (20 fáceis, 20 médias, 20 difíceis); 7 com texto de apoio (cpp1a, cpp1b).
- Questões resolvidas na aula: 4.
- Seções: 1, 2, 3, 4, 5, 6, 8, 9, 10 (questões resolvidas na seção 7).

## Fontes

Fontes: Edital 02/2026, Anexo I; Decreto-Lei 3.689/1941 (Código de Processo Penal), arts. 4º a 23, texto consolidado da Câmara dos Deputados. Exemplos criados para a aula.

Conferidas nesta produção:

- CPP, arts. 4º a 23: texto da Câmara, conferido contra as citações por programa (assert).

## Verificação de cobertura

- Recorte do edital: arts. 4º a 23. Cobertos todos os artigos de 4º a 23, incluindo os arts. 13-A, 13-B e 14-A, que não constam da numeração sequencial mas pertencem ao intervalo.

## Pontos para revisão (não conferidos na fonte)

- Texto-fonte: versão consolidada do site da Câmara dos Deputados (Legin), acessada em 14/11/2026. O Planalto estava inacessível; recomenda-se reconferir a redação vigente no Planalto, principalmente do art. 14-A e do art. 13-B.
- Os trechos transcritos nos quadros de lei foram conferidos por programa contra o texto-fonte salvo em fontes/cpp_arts4-23_301-310A.txt.
- A seção sobre o papel da Guarda Municipal apoia-se em gm-1 (art. 5º, XIV, Lei 13.022/2014), com a pendência de reconferência já registrada em revisao/gm-1.md.
- Os exemplos fictícios das ocorrências (cpp1a, cpp1b) foram criados para a aula.

## Aula

**O inquérito policial é a fase em que a polícia judiciária apura o crime e seu autor antes de o Ministério Público oferecer a denúncia. A Vunesp cobra os arts. 4º a 23 do Código de Processo Penal quase sempre em forma de letra de lei: quem pode abrir o inquérito, o que a autoridade policial deve fazer ao chegar ao local, os prazos de conclusão, quem pode arquivar, o sigilo e a incomunicabilidade. O texto é antigo e minucioso, e a prova costuma trocar um prazo, uma autoridade ou um verbo. Esta aula segue a ordem do próprio Código, com a lei seca citada e a explicação logo abaixo.**

## 1. A polícia judiciária e o inquérito

> A polícia judiciária será exercida pelas autoridades policiais no território de suas respectivas circunscrições e terá por fim a apuração das infrações penais e da sua autoria. *(art. 4º)*

Polícia judiciária é a que investiga, depois do crime, para reunir os elementos que permitam ao titular da ação penal decidir se denuncia. Não se confunde com a polícia ostensiva, que age para prevenir. O inquérito policial é o procedimento escrito em que essa investigação se registra. Ele é dispensável quando o Ministério Público já tem elementos suficientes para denunciar, e não é uma fase do processo: é uma etapa anterior, que serve de base para a denúncia ou a queixa.

> A competência definida neste artigo não excluirá a de autoridades administrativas, a quem por lei seja cometida a mesma função. *(art. 4º, parágrafo único)*

A consequência é que a investigação não é monopólio da polícia civil. Outras autoridades administrativas podem investigar quando a lei lhes der essa função, e é por isso que, por exemplo, comissões parlamentares de inquérito e outros órgãos também apuram fatos.

## 2. Como o inquérito começa

> Nos crimes de ação pública o inquérito policial será iniciado: I - de ofício; II - mediante requisição da autoridade judiciária ou do Ministério Público, ou a requerimento do ofendido ou de quem tiver qualidade para representá-lo. *(art. 5º, I e II)*

Nos crimes de ação pública, o inquérito pode começar de três modos. De ofício, quando a própria autoridade policial toma conhecimento do fato e instaura o procedimento por sua iniciativa, o que ocorre, por exemplo, quando é apresentado um preso em flagrante. Por requisição do juiz ou do Ministério Público, que dão ordem à autoridade e não podem ser recusados, a não ser que a ordem seja manifestamente ilegal. Ou a requerimento do ofendido, ou de quem o represente, que não obriga a autoridade a instaurar.

> O requerimento a que se refere o n. II conterá sempre que possível: a) a narração do fato, com todas as circunstâncias; b) a individualização do indiciado ou seus sinais característicos e as razões de convicção ou de presunção de ser ele o autor da infração, ou os motivos de impossibilidade de o fazer; c) a nomeação das testemunhas, com indicação de sua profissão e residência. *(art. 5º, § 1º)*

> Qualquer pessoa do povo que tiver conhecimento da existência de infração penal em que caiba ação pública poderá, verbalmente ou por escrito, comunicá-la à autoridade policial, e esta, verificada a procedência das informações, mandará instaurar inquérito. *(art. 5º, § 3º)*

É a chamada delatio criminis simples: qualquer pessoa pode noticiar o crime. A autoridade não instaura automaticamente; antes verifica se a informação procede.

> § 4º O inquérito, nos crimes em que a ação pública depender de representação, não poderá sem ela ser iniciado. § 5º Nos crimes de ação privada, a autoridade policial somente poderá proceder a inquérito a requerimento de quem tenha qualidade para intentá-la. *(art. 5º, §§ 4º e 5º)*

Aqui está a regra que a prova mais cobra. Nos crimes de ação pública condicionada à representação, a vítima precisa autorizar a investigação, e sem essa representação o inquérito não nasce. Nos crimes de ação privada, só o requerimento de quem pode propor a ação autoriza a polícia. Já nos crimes de ação pública incondicionada, nada disso é necessário.

> **Nota:** O § 2º do art. 5º prevê recurso, contra o indeferimento do requerimento de abertura, ao “chefe de Polícia”. A expressão é do texto de 1941; na prática, a autoridade superior da polícia judiciária.

## 3. O que a autoridade faz ao tomar conhecimento do crime

> Logo que tiver conhecimento da prática da infração penal, a autoridade policial deverá: I - dirigir-se ao local, providenciando para que não se alterem o estado e conservação das coisas, até a chegada dos peritos criminais; *(art. 6º, I)*

O primeiro dever é preservar o local. Mexer na cena do crime pode destruir vestígios e comprometer a prova técnica. É a regra que explica por que a Guarda Municipal, quando chega antes da perícia, isola a área e impede a entrada de curiosos, e é coerente com o que o Estatuto das Guardas determina quanto a preservar o local do crime quando possível e sempre que necessário.

> II - apreender os objetos que tiverem relação com o fato, após liberados pelos peritos criminais. III - colher todas as provas que servirem para o esclarecimento do fato e suas circunstâncias; IV - ouvir o ofendido; *(art. 6º, II a IV)*

> V - ouvir o indiciado, com observância, no que for aplicável, do disposto no Capítulo III do Título VII, deste Livro, devendo o respectivo termo ser assinado por duas testemunhas que lhe tenham ouvido a leitura; *(art. 6º, V)*

> VI - proceder a reconhecimento de pessoas e coisas e a acareações; VII - determinar, se for caso, que se proceda a exame de corpo de delito e a quaisquer outras perícias; VIII - ordenar a identificação do indiciado pelo processo datiloscópico, se possível, e fazer juntar aos autos sua folha de antecedentes; *(art. 6º, VI a VIII)*

> IX - averiguar a vida pregressa do indiciado, sob o ponto de vista individual, familiar e social, sua condição econômica, sua atitude e estado de ânimo antes e depois do crime e durante ele, e quaisquer outros elementos que contribuírem para a apreciação do seu temperamento e caráter; X - colher informações sobre a existência de filhos, respectivas idades e se possuem alguma deficiência e o nome e o contato de eventual responsável pelos cuidados dos filhos, indicado pela pessoa presa. *(art. 6º, IX e X)*

Repare na ordem lógica: preserva-se o local, apreendem-se os objetos depois de liberados pela perícia, colhem-se as provas, ouve-se a vítima e depois o investigado. O inciso X é o mais recente, e protege os filhos da pessoa presa.

> Para verificar a possibilidade de haver a infração sido praticada de determinado modo, a autoridade policial poderá proceder à reprodução simulada dos fatos, desde que esta não contrarie a moralidade ou a ordem pública. *(art. 7º)*

A reprodução simulada, ou reconstituição, é facultativa, e tem um limite: não pode contrariar a moralidade nem a ordem pública. O investigado não é obrigado a participar, porque ninguém é obrigado a produzir prova contra si mesmo.

## 4. Prazo, relatório e arquivamento

> O inquérito deverá terminar no prazo de 10 dias, se o indiciado tiver sido preso em flagrante, ou estiver preso preventivamente, contado o prazo, nesta hipótese, a partir do dia em que se executar a ordem de prisão, ou no prazo de 30 dias, quando estiver solto, mediante fiança ou sem ela. *(art. 10, caput)*

São dois prazos: 10 dias se o indiciado está preso, 30 se está solto. Para o preso preventivamente, o prazo conta do dia em que a ordem foi cumprida. O motivo é que a prisão é medida excepcional, e quem está preso não pode esperar a investigação por muito tempo.

> § 1º A autoridade fará minucioso relatório do que tiver sido apurado e enviará os autos ao juiz competente. § 2º No relatório poderá a autoridade indicar testemunhas que não tiverem sido inquiridas, mencionando o lugar onde possam ser encontradas. § 3º Quando o fato for de difícil elucidação, e o indiciado estiver solto, a autoridade poderá requerer ao juiz a devolução dos autos, para ulteriores diligências, que serão realizadas no prazo marcado pelo juiz. *(art. 10, §§ 1º a 3º)*

Ao fim, a autoridade faz o relatório e remete os autos ao juiz. Se o fato é de difícil elucidação e o indiciado está solto, pode pedir mais prazo, e quem marca o novo prazo é o juiz. O pedido de dilação só vale para o indiciado solto: com o investigado preso, o prazo de 10 dias é mais rígido.

> O inquérito policial acompanhará a denúncia ou queixa, sempre que servir de base a uma ou outra. *(art. 12)*

> O Ministério Público não poderá requerer a devolução do inquérito à autoridade policial, senão para novas diligências, imprescindíveis ao oferecimento da denúncia. *(art. 16)*

> A autoridade policial não poderá mandar arquivar autos de inquérito. *(art. 17)*

> Depois de ordenado o arquivamento do inquérito pela autoridade judiciária, por falta de base para a denúncia, a autoridade policial poderá proceder a novas pesquisas, se de outras provas tiver notícia. *(art. 18)*

O arquivamento nunca é decidido pela autoridade policial. Ela pode concluir e encaminhar, mas não arquivar. Se o inquérito já foi arquivado por falta de base, a polícia pode voltar a investigar quando surgirem provas novas. Já o Ministério Público só pode pedir a devolução do inquérito para diligências imprescindíveis à denúncia, e não por conveniência.

> Nos crimes em que não couber ação pública, os autos do inquérito serão remetidos ao juízo competente, onde aguardarão a iniciativa do ofendido ou de seu representante legal, ou serão entregues ao requerente, se o pedir, mediante traslado. *(art. 19)*

## 5. Sigilo, incomunicabilidade e demais regras

> A autoridade assegurará no inquérito o sigilo necessário à elucidação do fato ou exigido pelo interesse da sociedade. Parágrafo único. Nos atestados de antecedentes que lhe forem solicitados, a autoridade policial não poderá mencionar quaisquer anotações referentes a instauração de inquérito contra os requerentes. *(art. 20)*

O inquérito é sigiloso, mas o sigilo tem objetivo: apurar o fato ou atender ao interesse da sociedade. O parágrafo único protege o investigado: o atestado de antecedentes não registra a mera instauração de um inquérito.

> A incomunicabilidade do indiciado dependerá sempre de despacho nos autos e somente será permitida quando o interesse da sociedade ou a conveniência da investigação o exigir. Parágrafo único. A incomunicabilidade, que não excederá de três dias, será decretada por despacho fundamentado do Juiz, a requerimento da autoridade policial, ou do órgão do Ministério Público, respeitado, em qualquer hipótese, o disposto no artigo 89, inciso III, do Estatuto da Ordem dos Advogados do Brasil . *(art. 21)*

A incomunicabilidade é exceção: depende de despacho do juiz, dura no máximo três dias e jamais impede o contato com o advogado, que é direito garantido pelo Estatuto da Advocacia.

> O ofendido, ou seu representante legal, e o indiciado poderão requerer qualquer diligência, que será realizada, ou não, a juízo da autoridade. *(art. 14)*

> Se o indiciado for menor, ser-lhe-á nomeado curador pela autoridade policial. *(art. 15)*

> No Distrito Federal e nas comarcas em que houver mais de uma circunscrição policial, a autoridade com exercício em uma delas poderá, nos inquéritos a que esteja procedendo, ordenar diligências em circunscrição de outra, independentemente de precatórias ou requisições, e bem assim providenciará, até que compareça a autoridade competente, sobre qualquer fato que ocorra em sua presença, noutra circunscrição. *(art. 22)*

> Ao fazer a remessa dos autos do inquérito ao juiz competente, a autoridade policial oficiará ao Instituto de Identificação e Estatística, ou repartição congênere, mencionando o juízo a que tiverem sido distribuídos, e os dados relativos à infração penal e à pessoa do indiciado. *(art. 23)*

O pedido de diligência do ofendido ou do indiciado não obriga a autoridade a realizar: ela decide se faz ou não. A diligência requisitada pelo juiz ou pelo Ministério Público, ao contrário, é cumprida (art. 13, II).

## 6. Regras novas sobre requisição de dados e defesa do agente de segurança

> Nos crimes previstos nos arts. 148, 149 e 149-A, no § 3º do art. 158 e no art. 159 do Decreto-Lei nº 2.848, de 7 de dezembro de 1940 (Código Penal), e no art. 239 da Lei nº 8.069, de 13 de julho de 1990 (Estatuto da Criança e do Adolescente), o membro do Ministério Público ou o delegado de polícia poderá requisitar, de quaisquer órgãos do poder público ou de empresas da iniciativa privada, dados e informações cadastrais da vítima ou de suspeitos. *(art. 13-A, caput)*

Nos crimes de sequestro, cárcere privado, redução à condição análoga à de escravo, tráfico de pessoas, extorsão com restrição de liberdade, extorsão mediante sequestro e tráfico internacional de criança, o delegado ou o promotor requisitam dados cadastrais diretamente, sem ordem judicial, e a resposta deve vir em 24 horas (parágrafo único). O conteúdo das comunicações, porém, continua dependendo do juiz.

> Nos casos em que servidores vinculados às instituições dispostas no art. 144 da Constituição Federal figurarem como investigados em inquéritos policiais, inquéritos policiais militares e demais procedimentos extrajudiciais, cujo objeto for a investigação de fatos relacionados ao uso da força letal praticados no exercício profissional, de forma consumada ou tentada, incluindo as situações dispostas no art. 23 do Decreto-Lei nº 2.848, de 7 de dezembro de 1940 (Código Penal), o indiciado poderá constituir defensor. *(art. 14-A, caput)*

> § 1º Para os casos previstos no caput deste artigo, o investigado deverá ser citado da instauração do procedimento investigatório, podendo constituir defensor no prazo de até 48 (quarenta e oito) horas a contar do recebimento da citação. § 2º Esgotado o prazo disposto no § 1º deste artigo com ausência de nomeação de defensor pelo investigado, a autoridade responsável pela investigação deverá intimar a instituição a que estava vinculado o investigado à época da ocorrência dos fatos, para que essa, no prazo de 48 (quarenta e oito) horas, indique defensor para a representação do investigado. § 3º Havendo necessidade de indicação de defensor nos termos do § 2º deste artigo, a defesa caberá preferencialmente à Defensoria Pública, e, nos locais em que ela não estiver instalada, a União ou a Unidade da Federação correspondente à respectiva competência territorial do procedimento instaurado deverá disponibilizar profissional para acompanhamento e realização de todos os atos relacionados à defesa administrativa do investigado. *(art. 14-A, §§ 1º a 3º)*

O art. 144 da Constituição lista os órgãos de segurança pública, entre eles as guardas municipais (§ 8º). Quando um agente desses é investigado por fato ligado ao uso da força letal em serviço, ele é citado e tem 48 horas para constituir defensor. Se não o faz, a instituição em que ele trabalhava tem outras 48 horas para indicar um, preferencialmente a Defensoria Pública.

## 7. Questões resolvidas

### Questão 1

De acordo com o Código de Processo Penal, o inquérito policial, nos crimes de ação pública condicionada à representação,

- (A) não poderá ser iniciado sem a representação.
- (B) pode ser iniciado de ofício, independentemente de representação.
- (C) é dispensado quando há flagrante.
- (D) depende de requisição do juiz.
- (E) só pode ser instaurado pelo Ministério Público.

**Resposta: A.** Art. 5º, § 4º.

### Questão 2

O prazo para terminar o inquérito, quando o indiciado está preso em flagrante, é de

- (A) 30 dias.
- (B) 10 dias.
- (C) 15 dias.
- (D) 5 dias.
- (E) 60 dias.

**Resposta: B.** Art. 10: 10 dias com preso, 30 dias com solto.

### Questão 3

A autoridade policial, ao concluir o inquérito, pode

- (A) mandar arquivar os autos.
- (B) enviar os autos diretamente ao tribunal.
- (C) manter os autos com a polícia até a denúncia.
- (D) destruir peças que considere irrelevantes.
- (E) fazer minucioso relatório e enviar os autos ao juiz competente.

**Resposta: E.** Art. 10, § 1º. O arquivamento é vedado à autoridade policial pelo art. 17.

### Questão 4

A incomunicabilidade do indiciado

- (A) pode durar até 10 dias, por despacho da autoridade policial.
- (B) é automática quando o indiciado está preso.
- (C) não excederá três dias e depende de despacho fundamentado do juiz.
- (D) impede o contato com o advogado.
- (E) não depende de decisão fundamentada.

**Resposta: C.** Art. 21 e parágrafo único.

## 8. Na rotina do guarda

- **Local de crime:** isolar a área e preservá-la até a chegada da perícia e da autoridade policial, o que concretiza o art. 6º, I, do CPP.
- **Comunicação do fato:** qualquer pessoa pode comunicar crime de ação pública à autoridade policial, e o guarda o faz por dever de ofício, registrando as circunstâncias para o boletim.
- **Relato por escrito:** o inquérito é escrito (art. 9º), e a qualidade do boletim do guarda determina o que a autoridade terá em mãos.
- **Crime que depende de representação:** diante de crime de ação pública condicionada, a vítima precisa ser orientada a representar, porque sem a representação não se instaura inquérito.
- **Cautela com o sigilo:** não divulgar o conteúdo do que apurou, porque o sigilo protege a investigação (art. 20).

## 9. Onde a Vunesp pega

| Armadilha | Como escapar |
| --- | --- |
| Dizer que a autoridade policial pode arquivar o inquérito | Nunca: só o juiz ordena o arquivamento (art. 17) |
| Trocar os prazos de 10 e 30 dias | Preso: 10 dias. Solto: 30 dias |
| Achar que o requerimento do ofendido obriga a instaurar | Obriga a requisição do juiz ou do MP; o requerimento não |
| Dizer que a representação é dispensável em crime que a exige | Sem representação, o inquérito não pode ser iniciado (art. 5º, § 4º) |
| Esquecer que o indiciado menor tem curador | O curador é nomeado pela autoridade policial (art. 15) |
| Dar mais de três dias para a incomunicabilidade | Máximo de três dias, por despacho fundamentado do juiz |
| Atestado de antecedentes mencionando o inquérito | A autoridade não pode mencionar a instauração (art. 20, parágrafo único) |
| Permitir reprodução simulada ofensiva à moralidade | O limite é a moralidade e a ordem pública (art. 7º) |

## 10. Quadro-resumo

| Ponto | O essencial |
| --- | --- |
| Início (ação pública) | De ofício; requisição do juiz ou do MP; requerimento do ofendido |
| Representação | Sem ela, o inquérito de ação condicionada não pode começar |
| Local | Preservar até a chegada dos peritos (art. 6º, I) |
| Prazo | 10 dias com preso; 30 dias com solto |
| Dilação | Só com indiciado solto e fato de difícil elucidação; o juiz marca o prazo |
| Arquivamento | Nunca pela autoridade policial |
| Incomunicabilidade | Até três dias, despacho fundamentado do juiz |
| Menor indiciado | Curador nomeado pela autoridade |
| Antecedentes | Sem menção à instauração de inquérito |
