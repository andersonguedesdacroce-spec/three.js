/* ---------- Edital ---------- */
const PROVA = new Date("2027-03-21T13:00:00-03:00");
const FIM_CONTEUDO = new Date("2027-03-14T23:59:00-03:00");
const NOTA_MIN = 7, N_QUESTOES = 10;

/* Cada trilha é uma matéria do Anexo I. Cada posto: [título, recorte do edital]. */
const TRILHAS = [
 {id:"pt", bloco:"Conhecimentos Gerais", nome:"Língua Portuguesa", q:"12 questões", postos:[
  ["Leitura e interpretação de textos literários e não literários","Tipos e gêneros textuais; informações explícitas e implícitas; inferência"],
  ["Sinônimos e antônimos","Substituição de palavras e relações de sentido no contexto"],
  ["Sentido próprio e figurado das palavras","Denotação, conotação e figuras de linguagem"],
  ["Pontuação","Vírgula, ponto e vírgula, dois-pontos, travessão e aspas"],
  ["Substantivo, adjetivo e numeral","Emprego e sentido nas relações que estabelecem"],
  ["Pronome","Emprego, colocação no texto e função de retomada"],
  ["Verbo e advérbio","Tempos, modos, vozes verbais e circunstâncias adverbiais"],
  ["Preposição e conjunção","Emprego e valores semânticos das relações"],
  ["Concordância verbal e nominal","Casos gerais e casos especiais"],
  ["Regência verbal e nominal","Verbos e nomes mais cobrados; relativo com preposição"],
  ["Colocação pronominal","Próclise, mesóclise e ênclise"],
  ["Crase","Casos obrigatórios, proibidos e facultativos"]]},
 {id:"mt", bloco:"Conhecimentos Gerais", nome:"Matemática e Raciocínio Lógico", q:"6 questões", postos:[
  ["Operações com números racionais","Adição a radiciação, em forma fracionária ou decimal"],
  ["Mínimo múltiplo comum e máximo divisor comum","Situações-problema"],
  ["Porcentagem","Aumentos, descontos e variações sucessivas"],
  ["Razão e proporção","Grandezas diretamente e inversamente proporcionais"],
  ["Regra de três simples e composta","Situações-problema"],
  ["Equações do 1º e do 2º graus","Montagem e resolução"],
  ["Sistema de equações do 1º grau","Situações-problema com duas incógnitas"],
  ["Grandezas e medidas","Quantidade, tempo, comprimento, superfície, capacidade e massa"],
  ["Relação entre grandezas e média aritmética","Tabelas, gráficos e média aritmética simples"],
  ["Noções de geometria","Forma, ângulos, área, perímetro, volume, Pitágoras e Tales"],
  ["Estruturas lógicas e lógica de argumentação","Proposições, conectivos, negação e argumentos"],
  ["Diagramas lógicos e sequências","Todo, algum, nenhum; sequências numéricas e de figuras"]]},
 {id:"lm", bloco:"Conhecimentos Gerais", nome:"Legislação Municipal", q:"2 questões", postos:[
  ["Estatuto do Servidor Público de Campinas","Lei Municipal 1.399/1955, art. 15 e arts. 184 a 204"],
  ["Programa de Avaliação Probatória do Servidor","Decreto Municipal 21.019/2020"]]},
 {id:"geo", bloco:"Conhecimentos Específicos", nome:"Aspectos Geográficos e Urbanos de Campinas", postos:[
  ["Região Metropolitana de Campinas","Municípios integrantes, características socioeconômicas e relevância regional"],
  ["Cidades limítrofes de Campinas","Municípios que fazem divisa com Campinas"],
  ["Zonas geográficas de Campinas","Norte, Sul, Leste e Oeste; organização territorial e administrativa"],
  ["Distritos de Campinas","Características, localização e importância administrativa"],
  ["Principais próprios públicos municipais","Sedes administrativas, saúde, educação, segurança e centros de referência"]]},
 {id:"gm", bloco:"Conhecimentos Específicos", nome:"Estatuto Geral das Guardas Municipais", postos:[
  ["Natureza, princípios e competências","Lei 13.022/2014, arts. 1º a 5º"],
  ["Criação, efetivo, requisitos, controle e prerrogativas","Lei 13.022/2014, arts. 6º a 22"]]},
 {id:"cp", bloco:"Conhecimentos Específicos", nome:"Código Penal", postos:[
  ["Crimes contra a vida","Arts. 121 a 128"],
  ["Lesões corporais","Art. 129"],
  ["Periclitação da vida e da saúde e rixa","Arts. 130 a 137"],
  ["Crimes contra a honra","Arts. 138 a 145"],
  ["Crimes contra a liberdade pessoal","Arts. 146 a 149-A"],
  ["Inviolabilidade do domicílio, da correspondência e dos segredos","Arts. 150 a 154-B"],
  ["Furto","Arts. 155 e 156"],
  ["Roubo e extorsão","Arts. 157 a 160"],
  ["Usurpação e dano","Arts. 161 a 167"],
  ["Apropriação indébita","Arts. 168 a 170"],
  ["Estelionato e outras fraudes","Arts. 171 a 179"],
  ["Receptação e disposições gerais","Arts. 180 a 183-A"],
  ["Peculato e crimes afins","Arts. 312 a 315"],
  ["Concussão, corrupção passiva, prevaricação e condescendência","Arts. 316 a 320"],
  ["Demais crimes funcionais e conceito de funcionário público","Arts. 321 a 327"]]},
 {id:"cpp", bloco:"Conhecimentos Específicos", nome:"Código de Processo Penal", postos:[
  ["Inquérito policial","Arts. 4º a 23"],
  ["Prisão em flagrante","Arts. 301 a 310-A"]]},
 {id:"ctb", bloco:"Conhecimentos Específicos", nome:"Código de Trânsito Brasileiro", postos:[
  ["Disposições preliminares e Sistema Nacional de Trânsito","Composição e competências dos órgãos"],
  ["Normas gerais de circulação e conduta","Preferências, ultrapassagem, velocidades e conversões"],
  ["Pedestres, condutores não motorizados e educação para o trânsito","Direitos, deveres e cidadania"],
  ["Sinalização, engenharia, operação e fiscalização","Tipos de sinais e ordem de prevalência"],
  ["Veículos, registro e licenciamento","Classificação, equipamentos e documentação"],
  ["Habilitação","Categorias, permissão para dirigir e exames"],
  ["Infrações","Natureza, pontuação e infrações mais cobradas"],
  ["Penalidades e medidas administrativas","Advertência, multa, suspensão, cassação, retenção e remoção"],
  ["Processo administrativo","Autuação, notificação, defesa e recursos"],
  ["Crimes de trânsito","Disposições gerais e crimes em espécie"],
  ["Demais infrações","Ultrapassagem, preferência, luzes, documentos, motos, celular, pedestres e ciclistas"],
  ["Conceitos e definições","Anexo I: vias, manobras, imobilizações, veículos e agentes"]]},
 {id:"eca", bloco:"Conhecimentos Específicos", nome:"Estatuto da Criança e do Adolescente", postos:[
  ["Disposições preliminares","Arts. 1º a 6º"],
  ["Direito à liberdade, ao respeito e à dignidade","Arts. 15 a 18-B"],
  ["Direito à educação, à cultura, ao esporte e ao lazer","Arts. 53 a 59-A"],
  ["Prevenção geral e especial","Arts. 70 a 82"],
  ["Entidades de atendimento","Arts. 90 a 97"],
  ["Prática de ato infracional","Arts. 103 a 111"]]},
 {id:"idoso", bloco:"Conhecimentos Específicos", nome:"Estatuto da Pessoa Idosa", postos:[
  ["Direitos fundamentais","Arts. 8º a 42"],
  ["Medidas de proteção e política de atendimento","Arts. 43 a 68"],
  ["Crimes em espécie","Arts. 95 a 108"]]},
 {id:"mp", bloco:"Conhecimentos Específicos", nome:"Lei Maria da Penha", postos:[
  ["Disposições gerais e formas de violência","Arts. 1º a 7º"],
  ["Assistência à mulher e atendimento pela autoridade policial","Arts. 8º a 12-C"],
  ["Procedimentos e medidas protetivas de urgência","Arts. 13 a 24-A"]]},
 {id:"dudh", bloco:"Conhecimentos Específicos", nome:"Declaração Universal dos Direitos Humanos", postos:[
  ["Preâmbulo e direitos civis e políticos","Arts. 1º a 21"],
  ["Direitos econômicos, sociais e culturais; deveres","Arts. 22 a 30"]]},
 {id:"racial", bloco:"Conhecimentos Específicos", nome:"Lei contra a Discriminação Racial", postos:[
  ["Lei Estadual 14.187/2010","Condutas, penalidades e procedimento"]]},
 {id:"ctn", bloco:"Conhecimentos Específicos", nome:"Código Tributário Nacional", postos:[
  ["Taxas e poder de polícia","Arts. 77 a 79"]]},
 {id:"susp", bloco:"Conhecimentos Específicos", nome:"Sistema Único de Segurança Pública", postos:[
  ["Política Nacional de Segurança Pública e Defesa Social","Lei 13.675/2018: princípios, diretrizes e objetivos"],
  ["Composição e funcionamento do Susp","Integrantes, governança, conselhos e planos"],
  ["Metas, Sinesp, formação e valorização","Arts. 11 a 14, 24 a 27 e 36 a 45: Sinesp, Sievap e Pró-Vida"]]},
 {id:"amb", bloco:"Conhecimentos Específicos", nome:"Lei de Crimes Ambientais", postos:[
  ["Crimes contra a fauna","Arts. 29 a 37"],
  ["Crimes contra a flora","Arts. 38 a 53"],
  ["Poluição, ordenamento urbano, patrimônio cultural e administração ambiental","Arts. 54 a 69-A"]]},
 {id:"forca", bloco:"Conhecimentos Específicos", nome:"Instrumentos de Menor Potencial Ofensivo", postos:[
  ["Lei 13.060/2014","Uso preferencial dos instrumentos de menor potencial ofensivo"],
  ["Decreto 12.341/2024","Regulamentação do uso da força"]]},
 {id:"abuso", bloco:"Conhecimentos Específicos", nome:"Abuso de Autoridade", postos:[
  ["Disposições gerais, efeitos da condenação e sanções","Lei 13.869/2019, arts. 1º a 8º"],
  ["Crimes em espécie e procedimento","Lei 13.869/2019, arts. 9º em diante"]]},
 {id:"armas", bloco:"Conhecimentos Específicos", nome:"Regulamento do Estatuto do Desarmamento", postos:[
  ["Sinarm e porte funcional das guardas municipais","Decreto 11.615/2023, arts. 1º, 3º, 7º e 53 a 60"],
  ["Classificação e aquisição de armas","Decreto 11.615/2023, arts. 2º e 11 a 19"],
  ["Registro, posse e porte para defesa pessoal","Decreto 11.615/2023, arts. 20 a 29, 46 a 52 e 62"]]}
];
