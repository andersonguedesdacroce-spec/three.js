# Ativar o login com Gmail e o ranking (Firebase)

O site funciona sem isto, em modo demonstração (progresso só no navegador, sem ranking entre alunos).
Com o Firebase configurado, o aluno cria conta com e-mail **@gmail.com** e senha, confirma o e-mail,
recupera a senha pelo link que o Firebase envia e aparece no ranking. O plano gratuito (Spark) basta para começar.

## Passo a passo (cerca de 15 minutos)

1. Acesse https://console.firebase.google.com, clique em **Adicionar projeto** e dê o nome `rota-gm-campinas`
   (o Google Analytics é opcional).
2. **Authentication** > **Começar** > aba **Método de login** > **E-mail/senha** > ative a primeira opção (não a de link sem senha) > Salvar.
3. **Authentication** > **Configurações** > **Domínios autorizados**: adicione o domínio do site
   (por exemplo `rota-gm-campinas.vercel.app` e o domínio próprio, quando houver).
4. **Authentication** > **Modelos** (Templates): troque o idioma para **Português (Brasil)** no ícone de idioma.
   Os modelos usados são **Verificação de endereço de e-mail** e **Redefinição de senha**; dá para editar o nome do remetente
   para "Rota GM Campinas".
5. **Firestore Database** > **Criar banco de dados** > modo de produção > local `southamerica-east1` (São Paulo).
6. **Firestore Database** > **Regras**: apague o conteúdo, cole o arquivo `firestore.rules` deste repositório e clique em **Publicar**.
7. **Configurações do projeto** (engrenagem) > **Seus apps** > ícone **Web** (`</>`) > registre o app `rota-gm-campinas` (sem Hosting).
   Copie o objeto `firebaseConfig` que aparece.
8. Abra `src/config.js`, troque `const FIREBASE_CONFIG = null;` pelo objeto copiado
   (`const FIREBASE_CONFIG = { apiKey: "...", authDomain: "...", projectId: "...", appId: "..." };`),
   rode `python3 build.py` e publique.

Esses valores do `firebaseConfig` são públicos por natureza (vão para o navegador de todo visitante);
quem protege os dados são as regras do passo 6.

## Como o login funciona

- **Só Gmail:** o formulário recusa endereços que não terminam em `@gmail.com`, e as regras do Firestore negam
  qualquer leitura ou gravação a contas que não sejam Gmail **com e-mail confirmado**. Quem digitar um Gmail que não é seu
  não passa da tela "Confirme o seu e-mail".
- **Recuperação de senha:** "Esqueci minha senha" envia o link do Firebase. A mensagem é a mesma exista ou não a conta,
  para não revelar quem é aluno.
- **Senha:** mínimo de 8 caracteres; o Firebase guarda só o hash.
- **Sair:** botão no topo. O progresso fica no Firestore (`users/<uid>`) e também no navegador, separado por conta.

## Como o ranking funciona

| Ação | Pontos |
| --- | --- |
| Acertar uma questão pela primeira vez | 10 |
| Concluir um posto (7 ou mais acertos) | 100 |
| Concluir uma revisão espaçada (até 3 por posto) | 40 |
| Acertar uma questão que estava no caderno de erros | 20 |

- Repetir questões já acertadas não rende pontos: o ranking premia avançar no edital, não decorar respostas.
- Três listas: **Esta semana** (zera toda segunda-feira, para quem chega depois ter chance), **Geral** e **Sequência** (dias seguidos estudando).
- 12 níveis, de Recruta (0) a Lenda da Rota (35.000 pontos). O máximo teórico fica perto de 184 mil pontos.
- Participar é opcional: o aluno escolhe um apelido; e-mail e nome nunca aparecem. "Sair do ranking" apaga a linha dele.
- Sem prêmios. Como os pontos são calculados no navegador, as regras limitam os valores (até 200.000 pontos e saltos de no máximo 3.000 por gravação),
  o que segura exageros, mas não impede todo tipo de trapaça. Para apagar um apelido ofensivo ou uma linha suspeita:
  Firestore > coleção `ranking` > excluir o documento.

## Ainda falta

- **Pagamento real:** o acesso (`acesso: true`) ainda é marcado pelo botão de demonstração. Com o gateway, a liberação deve vir
  do servidor (webhook) gravando o acesso num documento que o aluno não consiga alterar.
- **Dentro do Claude** (o Artifact), o Firebase não é usado: o Claude bloqueia conexões externas. Lá, a conta é a do Claude
  e o ranking usa o banco da própria página.
