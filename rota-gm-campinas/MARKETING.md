# Rota GM Campinas: briefing de marketing

Documento de partida para o trabalho de marketing. Todos os números abaixo saem do próprio produto
(build de 14/11/2026) ou do Edital 02/2026; nada aqui é estimativa de venda.

## 1. O produto em uma frase

Plataforma de estudo para o concurso de **Guarda Municipal 3ª Classe de Campinas** (Vunesp, Edital 02/2026),
com todo o conteúdo programático do Anexo I transformado em postos de estudo: aula baseada no texto da lei,
resumo de uma página e 60 questões comentadas por posto.

## 2. Fatos verificáveis (pode usar em anúncios)

| Item | Valor | Onde conferir |
| --- | --- | --- |
| Matérias do Anexo I cobertas | 19 de 19 | Mapa do edital, no painel |
| Postos de estudo | 91 | `src/edital.js` |
| Questões comentadas | 5.460 (60 por posto: 20 fáceis, 20 médias, 20 difíceis) | `build.py` valida |
| Caixas de destaque (Cai muito, Cuidado, Macete) | em todas as 91 aulas | `destaques/` e aulas |
| Resumo de uma página | em todos os postos (aba Resumo) | painel |
| Revisão espaçada | 1, 7 e 30 dias após concluir o posto | painel |
| Caderno de erros | automático, com treino das erradas | painel |
| Guia do TAF | 5 provas, índices do Anexo II | painel |
| Preço configurado | R$ 97, pagamento único | página de vendas |

**Dados do concurso** (Edital 02/2026): 100 vagas; vencimento base R$ 3.796,61; auxílio-alimentação R$ 2.150,12;
inscrições até 08/01/2027; prova objetiva em 21/03/2027, às 13h; 50 questões (Português 12, Matemática 6,
Legislação Municipal 2, Conhecimentos Específicos 30); TAF vale até 100 pontos e é o 1º critério de desempate;
TAF previsto para 05 e 06/06/2027.

## 3. Público

- Candidatos de Campinas e da Região Metropolitana, em geral de 18 a 35 anos, com ensino médio completo.
- Muitos estudam pelo celular, no intervalo do trabalho: o painel foi desenhado para uso no celular.
- Dor principal: o edital é longo (CTB inteiro, Código Penal, ECA, Estatuto do Desarmamento e mais 15 matérias)
  e mistura legislação com geografia de Campinas, que os cursos genéricos não cobrem.

## 4. Diferenciais (mensagens)

1. **Feito para Campinas.** Geografia da RMC, limítrofes, regiões, distritos e próprios públicos municipais;
   Estatuto do Servidor e decreto de estágio probatório de Campinas.
2. **Edital inteiro, item por item.** O Mapa do edital liga cada item do Anexo I ao posto que o cobre.
3. **Leis citadas pelo artigo.** As aulas trazem o texto da lei com o número do artigo e listam as fontes.
4. **Estudo que não se perde.** Revisão espaçada e caderno de erros até a prova.
5. **O TAF pesa o dobro.** Guia do teste físico com os índices do edital.

## 5. O que não dizer (riscos legais e de reputação)

- Não prometer aprovação nem usar "garantido", "método infalível" ou números de aprovados: o produto ainda não tem histórico.
- Não usar depoimentos até existirem alunos reais que autorizem por escrito.
- Não usar logotipos ou nomes da Prefeitura, da Guarda Municipal de Campinas ou da Vunesp como se houvesse parceria.
  Manter o aviso: "Material preparatório independente, sem vínculo com a Prefeitura de Campinas ou com a Fundação Vunesp".
- Não anunciar "vídeo-aulas" nem "simulado final" como prontos: o simulado está marcado como "em produção".

## 6. Antes de começar a vender (pendências técnicas)

| Pendência | Situação | Próximo passo |
| --- | --- | --- |
| Pagamento real | O checkout é **demonstração** (botão "Simular pagamento aprovado") | Escolher gateway (Pix e cartão) e integrar a liberação do acesso |
| Controle de acesso | Hoje o acesso é marcado no próprio navegador | Login por e-mail ou conta, ligado ao pagamento |
| Hospedagem e domínio | Código pronto para Vercel (`vercel.json`); nenhum projeto criado ainda | Criar o projeto no Vercel a partir do repositório e registrar um domínio |
| Termos de uso e privacidade | Não existem | Redigir (LGPD: o painel guarda progresso e avisos de correção) |
| Revisão humana | Aulas marcadas "Versão 1 · em revisão"; cada posto tem `revisao/<posto>.md` com pendências | Revisar os pontos listados, em especial leis citadas por consolidação da Câmara |
| Canal de correção | Botão "Avise a equipe" em todas as aulas; os avisos ficam no banco do painel | Definir quem lê e com que frequência |

## 7. Calendário sugerido

| Período | Foco |
| --- | --- |
| Agora até 08/01/2027 | Captação durante as inscrições: "o edital saiu, comece pelo mapa" |
| Janeiro a fevereiro | Conteúdo diário por matéria (uma pegadinha da Vunesp por dia) |
| Março (até 21/03) | Reta final: revisão, resumo de uma página, caderno de erros |
| Após a prova até junho | Guia do TAF e preparação física (fase eliminatória e classificatória) |

## 8. Textos prontos para começar

**Título da página:** Guarda Municipal de Campinas: o edital inteiro, estudado item por item

**Anúncio curto:** 19 matérias, 91 postos, 5.460 questões comentadas. Tudo do Edital 02/2026 da Guarda Municipal
de Campinas, com revisão programada e caderno de erros. R$ 97, pagamento único.

**Ideias de post (formato carrossel):**
- "Celular ao volante: média ou gravíssima?" (CTB, art. 252: usar é média; segurar é gravíssima)
- "Concussão x corrupção passiva: o verbo decide" (exigir x solicitar, receber, aceitar)
- "Os 10 municípios que fazem divisa com Campinas" (geo-2)
- "Quanto vale cada parte da prova" (gráfico 12 / 6 / 2 / 30)
- "O TAF vale o dobro da prova escrita" (Anexo II)

Cada post pode terminar com uma questão do banco do posto correspondente e o link para a página.

## 9. Onde está cada coisa

- Página publicada (privada até ser compartilhada): https://claude.ai/artifact/LkJRDY2CeXeQ795tHr6c6T
- Código: repositório `gcm-campinas` (pasta raiz) e `three.js/rota-gm-campinas` (branch de desenvolvimento)
- Conteúdo e fontes: `conteudo/`, `fontes/`, `revisao/`
