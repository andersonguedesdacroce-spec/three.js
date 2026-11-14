/* ---------- Índices ---------- */
const POSTOS = [];
TRILHAS.forEach(tr=>tr.postos.forEach((p,i)=>POSTOS.push({id:tr.id+"-"+(i+1), t:p[0], r:p[1], tr, n:i})));
const POSTO = Object.fromEntries(POSTOS.map(p=>[p.id,p]));
const TRILHA = Object.fromEntries(TRILHAS.map(t=>[t.id,t]));
const postosDe = tid => POSTOS.filter(p=>p.tr.id===tid);
const QIDX = {};
Object.keys(BANCO).forEach(pid=>BANCO[pid].forEach(q=>{ QIDX[q.id] = {q, pid}; }));
const TOTAL_Q = Object.keys(QIDX).length;
const BLOCOS = [
  {nome:"Conhecimentos Gerais", q:20, id:"cg"},
  {nome:"Conhecimentos Específicos", q:30, id:"ce"}
];

/* ---------- Estado ---------- */
const KEY = "rota-gm-campinas-v2";
function novoEstado(){ return {acesso:false, aprovados:{}, tentativas:{}, vistas:{}, erros:{}, marcadas:{}, revisoes:{}, correcoes:[], ultimo:null, atualizado:0}; }
function completar(e){ const n = novoEstado(); Object.keys(n).forEach(k=>{ if(!(k in e)) e[k] = n[k]; }); return e; }
let S = (()=>{ try{ return completar(JSON.parse(localStorage.getItem(KEY)) || novoEstado()); }catch(e){ return novoEstado(); } })();
let docRef = null;
let IS_OWNER = false;
async function salvar(){
  S.atualizado = Date.now();
  try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){}
  if(docRef){ try{ await docRef.set({estado: JSON.stringify(S), atualizado: S.atualizado}); }catch(e){} }
}
(async ()=>{
  try{
    if(!window.claude || !window.claude.use) return;
    const db = await claude.use("db"); const user = await claude.use("user");
    if(user){ try{ IS_OWNER = !!(await user.isOwner()); if(IS_OWNER && V.tela==="posto") render(); }catch(e){} }
    if(!db || !user) return;
    const uid = await user.id(); if(!uid) return;
    docRef = db.doc("data/users/" + uid + "/progresso");
    const snap = await docRef.get();
    if(snap.exists){
      const remoto = completar(JSON.parse(snap.data().estado));
      if((remoto.atualizado||0) > (S.atualizado||0)){ S = remoto; try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} render(); }
    } else if(S.atualizado){ salvar(); }
  }catch(e){}
})();

/* ---------- Utilidades ---------- */
const $app = document.getElementById("app");
const LETRAS = ["A","B","C","D","E"];
const DIA = 86400000;
const INTERVALOS = [1, 7, 30]; // revisão espaçada: 1 dia, 7 dias e 30 dias após concluir o posto
const embaralhar = arr => { const a = arr.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
const diasAte = d => Math.max(0, Math.ceil((d - new Date())/DIA));
const feitos = tid => postosDe(tid).filter(p=>S.aprovados[p.id]).length;
const fmt = n => n.toLocaleString("pt-BR");
const norm = s => (s||"").normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase();
const MODO_REVISAO = true; // true = todos os postos liberados, sem nota mínima. Voltar para false para reativar a trava.
function liberado(pid){ const p = POSTO[pid]; if(!S.acesso) return false; if(MODO_REVISAO || p.n===0) return true; return !!S.aprovados[p.tr.id+"-"+p.n]; }
function proximo(tid){ return postosDe(tid).find(p=>!S.aprovados[p.id]) || null; }
function revisoesHoje(){ const agora = Date.now(); return Object.entries(S.revisoes).filter(([pid,r])=>POSTO[pid] && r.etapa < INTERVALOS.length && r.prox <= agora).map(([pid])=>POSTO[pid]); }
function proximaRevisao(){ const fut = Object.entries(S.revisoes).filter(([pid,r])=>POSTO[pid] && r.etapa < INTERVALOS.length && r.prox > Date.now()).sort((a,b)=>a[1].prox-b[1].prox); return fut.length ? fut[0] : null; }
function nErros(){ return Object.keys(S.erros).filter(k=>QIDX[k]).length; }
function nMarcadas(){ return Object.keys(S.marcadas).filter(k=>QIDX[k]).length; }
function respondidas(){ let r=0, c=0; Object.values(S.tentativas).forEach(ts=>ts.forEach(t=>{ r += (t.ids||[]).length; c += t.nota; })); return {r, c}; }
function sugestao(){
  if(S.ultimo && POSTO[S.ultimo] && !S.aprovados[S.ultimo]) return POSTO[S.ultimo];
  // alterna as matérias: escolhe a trilha com menor proporção concluída
  const abertas = TRILHAS.filter(t=>proximo(t.id)).sort((a,b)=>feitos(a.id)/a.postos.length - feitos(b.id)/b.postos.length);
  return abertas.length ? proximo(abertas[0].id) : null;
}
const ICONE = {
  cuidado:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 2 20h20L12 3z"/><path d="M12 10v4M12 17.5v.01"/></svg>',
  caimuito:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21l1.4-7L2 9.3l7-.8z"/></svg>',
  macete:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg>',
  conceito:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.01"/></svg>',
  "regra-p":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg>'
};
const ROTULO = {cuidado:"Cuidado", caimuito:"Cai muito", macete:"Macete", conceito:"Conceito", "regra-p":"Regra"};
document.getElementById("dias").textContent = diasAte(PROVA);

/* ---------- Modo claro e escuro ---------- */
const TEMA_KEY = "rota-gm-tema";
const SOL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg>';
const LUA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>';
function temaAtual(){ const t = document.documentElement.dataset.theme; if(t) return t; return (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light"; }
function aplicarTema(t){
  document.documentElement.dataset.theme = t;
  const b = document.getElementById("tema");
  b.innerHTML = t==="dark" ? SOL : LUA;
  b.title = t==="dark" ? "Mudar para modo claro" : "Mudar para modo escuro";
  b.setAttribute("aria-label", b.title);
}
(()=>{
  let salvo = null; try{ salvo = localStorage.getItem(TEMA_KEY); }catch(e){}
  aplicarTema(salvo || temaAtual());
  document.getElementById("tema").onclick = ()=>{ const novo = temaAtual()==="dark" ? "light" : "dark"; aplicarTema(novo); try{ localStorage.setItem(TEMA_KEY, novo); }catch(e){} };
})();

/* ---------- Navegação ---------- */
let V = {tela:"home"};
let Q = null;
function ir(v){ if(v.posto && !("modo" in v)) v = Object.assign({modo:undefined}, v); V = Object.assign({}, V, v); render(); window.scrollTo(0,0); }
document.getElementById("brand").onclick = ()=>ir({tela: S.acesso ? "painel" : "home"});
const LARGAS = new Set(["home","painel","checkout"]);
function render(){
  const t = V.tela;
  $app.classList.toggle("largo", LARGAS.has(t) || (t==="checkout"));
  if(t==="home") return telaHome();
  if(t==="checkout") return S.acesso ? telaPainel() : telaCheckout();
  if(!S.acesso) return telaHome();
  if(t==="painel") return telaPainel();
  if(t==="trilha") return telaTrilha();
  if(t==="posto") return telaPosto();
  if(t==="prova") return telaProva();
  if(t==="resultado") return telaResultado();
  if(t==="taf") return telaTAF();
  if(t==="banco") return telaBanco();
  if(t==="erros") return telaErros();
  if(t==="edital") return telaEdital();
}
function bindGo(){ $app.querySelectorAll("[data-go]").forEach(b=>b.onclick=()=>ir({tela:b.dataset.go})); }
function bindPostos(){ $app.querySelectorAll("[data-abrir]").forEach(b=>b.onclick=()=>ir({tela:"posto", posto:b.dataset.abrir, aba:b.dataset.aba||"aula"})); }

/* ---------- Peso da prova ---------- */
function pesoProva(){
  const partes = [["pt","Língua Portuguesa",12],["mt","Matemática e Raciocínio Lógico",6],["lm","Legislação Municipal",2],["ce","Conhecimentos Específicos",30]];
  return `<div class="peso" role="img" aria-label="Distribuição das 50 questões: Português 12, Matemática 6, Legislação Municipal 2, Conhecimentos Específicos 30">
    <div class="barra">${partes.map(([c,n,q])=>`<span class="${c}" style="flex:${q}">${q}</span>`).join("")}</div>
    <ul>${partes.map(([c,n,q])=>`<li><i class="${c}"></i>${n}: ${q} questões</li>`).join("")}</ul>
  </div>`;
}

/* ---------- Página de vendas ---------- */
function telaHome(){
  const blocos = BLOCOS.map(b=>{
    const trs = TRILHAS.filter(t=>t.bloco===b.nome);
    return `<p class="bloco-tit">${b.nome} · ${b.q} questões</p><ul class="lista-materias">${trs.map(t=>`<li><span>${t.nome}</span><span>${t.postos.length} ${t.postos.length===1?"posto":"postos"}${t.q ? " · " + t.q : ""}</span></li>`).join("")}</ul>`;
  }).join("");
  const cta = S.acesso ? `<button class="btn" data-go="painel">Ir para o meu painel</button>` : `<button class="btn amber" data-go="checkout">Quero meu acesso</button>`;
  $app.innerHTML = `
  <div class="lp">
  <section class="lp-hero">
    <div>
      <p class="eyebrow">Edital 02/2026 · Vunesp · prova em 21/03/2027</p>
      <h1>Guarda Municipal de Campinas: o edital inteiro, estudado item por item</h1>
      <p class="sub">Cada item do conteúdo programático virou um posto de estudo, com aula baseada no texto da lei, resumo de uma página e 60 questões comentadas no estilo Vunesp. O painel mostra o que estudar hoje, o que revisar e onde você mais erra.</p>
      <div class="cta-row">${cta}<a class="btn sec" href="#materias">Ver o conteúdo</a></div>
    </div>
    <div class="credencial" aria-label="Dados do concurso">
      <div class="faixa"><strong>Prefeitura de Campinas</strong><span>Edital 02/2026</span></div>
      <dl>
        <div><dt>Cargo</dt><dd>Guarda Municipal 3ª Classe</dd></div>
        <div><dt>Vagas</dt><dd>100</dd></div>
        <div><dt>Vencimento base</dt><dd>R$ 3.796,61</dd></div>
        <div><dt>Auxílio-alimentação</dt><dd>R$ 2.150,12 por mês</dd></div>
        <div><dt>Inscrições</dt><dd>até 08/01/2027</dd></div>
        <div><dt>Prova objetiva</dt><dd>21/03/2027, às 13h</dd></div>
      </dl>
    </div>
  </section>
  <div class="numeros">
    <div><b>${TRILHAS.length}</b><span>matérias do Anexo I</span></div>
    <div><b>${POSTOS.length}</b><span>postos de estudo</span></div>
    <div><b>${fmt(TOTAL_Q)}</b><span>questões comentadas</span></div>
    <div><b>${diasAte(PROVA)}</b><span>dias até a prova</span></div>
  </div>

  <section class="lp-sec">
    <h2>Quanto vale cada parte da prova objetiva</h2>
    <p>São 50 questões. Os Conhecimentos Específicos respondem por 30 delas, e é nessa parte que estão as leis que o guarda usa no serviço.</p>
    ${pesoProva()}
  </section>

  <section class="lp-sec duas">
    <div>
      <h2>Aulas que mostram, pela cor, o que é regra e o que é pegadinha</h2>
      <p style="color:var(--muted)">Toda aula segue a mesma ordem: mapa do assunto, texto da lei, explicação em linguagem simples, caso da rotina do guarda, armadilhas da banca e quadro-resumo. As caixas coloridas têm sempre a mesma função.</p>
      <div class="legenda-cores">
        <span><i style="background:var(--blue)"></i>Conceito</span>
        <span><i style="background:var(--ok)"></i>Regra</span>
        <span><i style="background:var(--bad)"></i>Cuidado, exceção</span>
        <span><i style="background:var(--amber)"></i>Cai muito</span>
        <span><i style="background:var(--violet)"></i>Macete</span>
      </div>
    </div>
    <div class="amostra"><p class="eyebrow">Trecho da aula de CTB · demais infrações</p><article class="aula apostila" id="amostra">
      <p><strong>O que é, em uma frase:</strong> o art. 252 pune quem dirige sem atenção total ao volante.</p>
      <blockquote><p><strong>Cai muito:</strong> dirigir com fone ou usando o celular é infração <strong>média</strong>; <strong>segurando ou manuseando</strong> o aparelho, é <strong>gravíssima</strong>.</p></blockquote>
      <blockquote><p><strong>Macete:</strong> "segurou, gravíssima".</p></blockquote>
      <blockquote><p><strong>Cuidado!</strong> Esquecer a CNH em casa é infração leve (art. 232). Recusar-se a entregá-la ao agente é gravíssima (art. 238).</p></blockquote>
    </article></div>
  </section>

  <section class="lp-sec">
    <h2>Como o estudo funciona</h2>
    <ol class="passos">
      <li><strong>Escolha a matéria</strong>Todas ficam abertas desde o primeiro dia, e o painel sugere a próxima para você alternar.</li>
      <li><strong>Leia a aula</strong>Texto da lei citado com o artigo, explicação, caso prático e quadro-resumo.</li>
      <li><strong>Faça 10 questões</strong>Sorteadas entre 60 do posto: fáceis, médias e difíceis. Com 7 acertos, o posto conta como concluído.</li>
      <li><strong>Revise no tempo certo</strong>O posto volta para revisão após 1, 7 e 30 dias, e cada erro vai para o seu caderno.</li>
    </ol>
  </section>

  <section class="lp-sec">
    <h2>O que você encontra no painel</h2>
    <div class="recursos">
      <div class="recurso"><h3>Mapa do edital</h3><p>Cada item do Anexo I ligado ao posto que o cobre, com o seu progresso em cada um.</p></div>
      <div class="recurso"><h3>Caderno de erros</h3><p>As questões que você errou e as que marcou ficam guardadas para treinar de novo até acertar.</p></div>
      <div class="recurso"><h3>Revisão espaçada</h3><p>O painel avisa quais postos revisar hoje, para o conteúdo não se perder até março.</p></div>
      <div class="recurso"><h3>Resumo de uma página</h3><p>Mapa, armadilhas da banca e quadro-resumo de cada posto, para a revisão da véspera.</p></div>
      <div class="recurso"><h3>Guia do TAF</h3><p>As cinco provas físicas, os índices mínimo e máximo e o cálculo da nota, conforme o Anexo II.</p></div>
      <div class="recurso"><h3>Fontes à vista</h3><p>Cada aula cita a lei e o artigo usados. Achou um erro? Há um botão para avisar em todas as aulas.</p></div>
    </div>
  </section>

  <section class="lp-sec" id="materias">
    <h2>Todas as matérias do edital, sem exceção</h2>
    <p>${TRILHAS.length} matérias e ${POSTOS.length} postos de estudo, montados a partir do Anexo I do edital.</p>
    <div class="duas">${blocos.replace(/(<p class="bloco-tit">Conhecimentos Específicos)/, '</div><div>$1').replace(/^/, '<div>')}</div></div>
  </section>

  <section class="lp-sec">
    <div class="destaque">
      <h2>O teste físico vale o dobro da prova escrita</h2>
      <p>A nota final é a soma da prova objetiva, que vale até 50 pontos, com o TAF, que vale até 100. A nota do TAF também é o primeiro critério de desempate.</p>
    </div>
  </section>

  <section class="lp-sec">
    <div class="oferta-box">
      <div>
        <h2>Acesso completo até a prova</h2>
        <ul>
          <li>${POSTOS.length} postos cobrindo todo o conteúdo programático</li>
          <li>${fmt(TOTAL_Q)} questões comentadas, com sorteio que evita repetir</li>
          <li>Caderno de erros, revisão espaçada e resumo de cada posto</li>
          <li>Guia do Teste de Aptidão Física</li>
          <li>Progresso salvo no celular e no computador</li>
        </ul>
      </div>
      <div>
        <div class="preco"><b>R$ 97</b><span>pagamento único, no Pix ou no cartão</span></div>
        ${S.acesso ? `<button class="btn full" data-go="painel">Ir para o meu painel</button>` : `<button class="btn amber full" data-go="checkout">Quero meu acesso</button>`}
        <p class="demo">Garantia de 7 dias pelo Código de Defesa do Consumidor.</p>
      </div>
    </div>
  </section>

  <section class="lp-sec faq">
    <h2>Perguntas frequentes</h2>
    <details><summary>Quando o acesso é liberado?</summary><p>No Pix, logo após a confirmação do pagamento. No cartão, assim que a operadora aprovar.</p></details>
    <details><summary>Posso estudar pelo celular?</summary><p>Sim. O painel funciona no navegador do celular e do computador, e o progresso fica salvo.</p></details>
    <details><summary>De onde vem o conteúdo?</summary><p>Do texto das leis e decretos cobrados no edital, citados com o número do artigo. Os temas de Campinas usam fontes oficiais do Município, da Câmara e da Região Metropolitana; cada aula traz a lista das fontes usadas.</p></details>
    <details><summary>E se uma lei mudar até a prova?</summary><p>O edital manda considerar a legislação vigente até a data da sua publicação. O material segue esse texto e aponta, em cada aula, os pontos que estão sendo conferidos.</p></details>
    <details><summary>Posso desistir da compra?</summary><p>Sim. Você tem 7 dias para exercer o direito de arrependimento, conforme o Código de Defesa do Consumidor.</p></details>
  </section>
  <p class="aviso">Material preparatório independente, sem vínculo com a Prefeitura de Campinas ou com a Fundação Vunesp.</p>
  </div>`;
  montarCaixas(document.getElementById("amostra"));
  bindGo();
}

/* ---------- Checkout (demonstração) ---------- */
let modoPag = null;
function telaCheckout(){
  $app.innerHTML = `
  <section class="topico" style="max-width:560px">
    <button class="voltar" data-go="home">‹ Voltar</button>
    <h2>Finalize seu acesso</h2>
    <p class="meta">Rota GM Campinas · acesso completo até a prova · R$ 97</p>
    <div class="pag">
      <button class="btn full" data-pag="pix">Pagar com Pix</button>
      <button class="btn sec full" data-pag="cartao">Pagar com cartão</button>
    </div>
    <div id="pagbox"></div>
    <p class="demo">Demonstração: nenhum valor é cobrado. Na versão final, o gateway confirma o pagamento e o acesso é liberado automaticamente.</p>
  </section>`;
  bindGo();
  $app.querySelectorAll("[data-pag]").forEach(b=>b.onclick=()=>{ modoPag=b.dataset.pag; pagamento(); });
  if(modoPag) pagamento();
}
function pagamento(){
  const box = document.getElementById("pagbox");
  const quadro = modoPag==="pix"
    ? `<p><strong>Escaneie o QR Code no app do seu banco</strong></p>${qrFake()}<p class="ref">Código válido por 30 minutos</p>`
    : `<p><strong>Pagamento com cartão</strong></p><p class="ref">Na versão final, aqui entra o formulário seguro do gateway.</p>`;
  box.innerHTML = `<div class="pix">${quadro}<button class="btn full" id="aprovar">Simular pagamento aprovado</button></div>`;
  document.getElementById("aprovar").onclick = async ()=>{ S.acesso = true; await salvar(); ir({tela:"painel"}); };
}
function qrFake(){
  let r=""; const n=21; let seed=7;
  const rnd=()=>{ seed=(seed*9301+49297)%233280; return seed/233280; };
  const olho=(x,y,ox,oy)=>{ const dx=x-ox, dy=y-oy; if(dx<0||dy<0||dx>6||dy>6) return null; return (dx===0||dy===0||dx===6||dy===6||(dx>1&&dx<5&&dy>1&&dy<5)); };
  for(let y=0;y<n;y++) for(let x=0;x<n;x++){
    let v = olho(x,y,0,0); if(v===null) v = olho(x,y,n-7,0); if(v===null) v = olho(x,y,0,n-7);
    if(v===null) v = rnd()>.5;
    if(v) r+=`<rect x="${x}" y="${y}" width="1" height="1"/>`;
  }
  return `<svg viewBox="-1 -1 ${n+2} ${n+2}" role="img" aria-label="QR Code de demonstração" fill="currentColor">${r}</svg>`;
}

/* ---------- Painel ---------- */
function telaPainel(){
  const total = POSTOS.length, ok = Object.keys(S.aprovados).filter(k=>POSTO[k]).length;
  const restantes = total - ok;
  const semanas = Math.max(1, Math.ceil(diasAte(FIM_CONTEUDO)/7));
  const meta = Math.ceil(restantes / semanas);
  const {r, c} = respondidas();
  const rev = revisoesHoje(), prox = proximaRevisao(), sug = sugestao();
  const ne = nErros(), nm = nMarcadas();
  const card = tr => {
    const f = feitos(tr.id), n = tr.postos.length, px = proximo(tr.id);
    return `<button class="tcard ${f===n?"feita":""}" data-tr="${tr.id}">
      <span class="linha"><span class="nome">${tr.nome}</span>${tr.q ? `<span class="q">${tr.q}</span>` : ""}</span>
      <span class="bar fina" aria-hidden="true"><i style="width:${(f/n*100).toFixed(0)}%"></i></span>
      <span class="info">${f} de ${n} ${n===1?"posto":"postos"}${px ? ` · próximo: ${px.t}` : " · matéria concluída"}</span>
    </button>`;
  };
  const tudo = restantes===0;
  $app.innerHTML = `
  <section class="hero">
    <div>
      <p class="eyebrow">Seu plano até 21/03/2027</p>
      <h1>${tudo ? "Edital concluído" : "Seu painel de estudo"}</h1>
      <p>${tudo ? "Você concluiu todos os postos. Mantenha as revisões e treine o caderno de erros." : `Para fechar o edital até 14/03, conclua cerca de ${meta} ${meta===1?"posto":"postos"} por semana, alternando as matérias.`}</p>
    </div>
  </section>
  <div class="kpis">
    <div class="kpi"><b>${ok}<small style="font-size:18px;color:var(--muted)">/${total}</small></b><span>postos concluídos</span></div>
    <div class="kpi"><b>${fmt(r)}</b><span>questões respondidas</span></div>
    <div class="kpi"><b>${r ? Math.round(c/r*100)+"%" : "—"}</b><span>de acerto geral</span></div>
    <div class="kpi"><b>${diasAte(PROVA)}</b><span>dias até a prova</span></div>
  </div>
  <div class="bar" role="progressbar" aria-label="Progresso no edital" aria-valuemin="0" aria-valuemax="${total}" aria-valuenow="${ok}"><i style="width:${(ok/total*100).toFixed(1)}%"></i></div>

  ${sug ? `<div class="continuar">
        <div><p class="eyebrow">${S.ultimo===sug.id ? "Continue de onde parou" : "Sugestão para agora"}</p><h2>${sug.t}</h2><p>${sug.tr.nome} · posto ${sug.n+1} de ${sug.tr.postos.length}</p></div>
        <button class="btn" data-abrir="${sug.id}">Estudar</button>
      </div>` : ""}
  <div class="grade">
    <div>

      ${BLOCOS.map(b=>`<div class="bloco-cab"><h2>${b.nome}</h2><span>${b.q} questões na prova</span></div>
        <div class="trilhas">${TRILHAS.filter(t=>t.bloco===b.nome).map(card).join("")}</div>`).join("")}
      <div class="bloco-cab"><h2>Teste físico e reta final</h2></div>
      <div class="trilhas">
        <button class="tcard taf" data-go="taf"><span class="nome">Guia do Teste de Aptidão Física</span><span class="info">Vale até 100 pontos na classificação final</span></button>
        <button class="tcard ${tudo?"":"trava"}" ${tudo?"":'aria-disabled="true"'}><span class="nome">Simulado final no formato Vunesp</span><span class="info">${tudo ? "50 questões em 3 horas · em produção" : "Libera ao concluir todos os postos"}</span></button>
      </div>
    </div>
    <aside class="lado" aria-label="Revisão e ferramentas">
      <div class="caixa busca">
        <label for="busca" class="eyebrow">Buscar no edital</label>
        <input id="busca" type="search" placeholder="Ex.: crase, flagrante, celular" autocomplete="off" style="margin-top:6px">
        <ul class="res-busca" id="res-busca"></ul>
      </div>
      <div class="caixa">
        <h3>Revisões de hoje <span class="pill ${rev.length?"amb":"ok"}">${rev.length}</span></h3>
        ${rev.length ? `<ul>${rev.slice(0,6).map(p=>`<li><button data-abrir="${p.id}" data-aba="resumo">${p.t}</button><small>${p.tr.nome} · revisão ${S.revisoes[p.id].etapa+1} de ${INTERVALOS.length}</small></li>`).join("")}</ul>${rev.length>6?`<p>E mais ${rev.length-6}.</p>`:""}`
          : `<p>${prox ? `Nada para hoje. A próxima revisão é de <strong>${POSTO[prox[0]].t}</strong>, em ${Math.max(1,Math.ceil((prox[1].prox-Date.now())/DIA))} ${Math.ceil((prox[1].prox-Date.now())/DIA)>1?"dias":"dia"}.` : "Quando você concluir um posto, ele volta aqui para revisão após 1, 7 e 30 dias."}</p>`}
      </div>
      <div class="caixa">
        <h3>Caderno de erros <span class="pill ${ne?"bad":"ok"}">${ne}</span></h3>
        <p>${ne||nm ? `${ne} ${ne===1?"questão errada":"questões erradas"} e ${nm} ${nm===1?"marcada":"marcadas"} para revisar. Quando você acerta, a questão sai do caderno.` : "As questões que você errar ou marcar ficam aqui para treinar de novo."}</p>
        <button class="btn peq ${ne||nm?"":"sec"}" data-go="erros">${ne||nm ? "Abrir o caderno" : "Ver como funciona"}</button>
      </div>
      <div class="caixa">
        <h3>Mapa do edital</h3>
        <p>Cada item do Anexo I e o posto que o cobre, com o seu progresso.</p>
        <button class="btn sec peq" data-go="edital">Abrir o mapa</button>
      </div>
      <div class="caixa"><p class="eyebrow" style="margin:0 0 8px">Peso na prova objetiva</p>${pesoProva()}</div>
    </aside>
  </div>
  <div class="rodape" id="rodape"><button id="reset">Reiniciar demonstração</button></div>`;
  bindGo(); bindPostos();
  $app.querySelectorAll("[data-tr]").forEach(b=>b.onclick=()=>ir({tela:"trilha", trilha:b.dataset.tr}));
  const busca = document.getElementById("busca"), rb = document.getElementById("res-busca");
  busca.oninput = ()=>{
    const termos = norm(busca.value).split(/\s+/).filter(Boolean);
    if(!termos.length){ rb.innerHTML = ""; return; }
    const achados = POSTOS.filter(p=>{ const h = norm(p.t+" "+p.r+" "+p.tr.nome); return termos.every(t=>h.includes(t)); }).slice(0,8);
    rb.innerHTML = achados.length ? achados.map(p=>`<li><button data-abrir="${p.id}">${p.t}<small>${p.tr.nome} · ${p.r}</small></button></li>`).join("") : `<li><button disabled>Nenhum posto encontrado<small>Tente outro termo, como o nome da lei ou do assunto.</small></button></li>`;
    bindPostos();
  };
  document.getElementById("reset").onclick = ()=>{
    const r = document.getElementById("rodape");
    r.innerHTML = `<div class="confirma"><p>Apagar todo o progresso e voltar à página de vendas?</p><button class="btn peq" id="sim">Apagar</button><button class="btn sec peq" id="nao">Cancelar</button></div>`;
    document.getElementById("nao").onclick = ()=>render();
    document.getElementById("sim").onclick = async ()=>{ S = novoEstado(); modoPag=null; await salvar(); ir({tela:"home"}); };
  };
}

/* ---------- Mapa do edital ---------- */
function telaEdital(){
  const ok = Object.keys(S.aprovados).filter(k=>POSTO[k]).length;
  const linha = p => {
    const a = S.aprovados[p.id], tent = (S.tentativas[p.id]||[]).length;
    const st = a ? `<span class="pill ok">Concluído · ${a.nota}/10</span>` : (tent ? `<span class="pill amb">Em andamento</span>` : `<span class="pill">A estudar</span>`);
    return `<tr><td><button data-abrir="${p.id}">${p.t}</button></td><td>${p.r}</td><td>${st}</td></tr>`;
  };
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" data-go="painel">‹ Voltar ao painel</button>
    <p class="eyebrow">Anexo I do Edital 02/2026</p>
    <h2>Mapa do edital</h2>
    <p class="meta">Cada matéria do conteúdo programático, com os postos que cobrem seus itens. ${ok} de ${POSTOS.length} postos concluídos.</p>
    <div class="legenda"><span class="pill ok">Concluído</span><span class="pill amb">Em andamento</span><span class="pill">A estudar</span></div>
    <div class="mapa-ed">
    ${BLOCOS.map(b=>`<h3 style="font-size:24px;margin:22px 0 6px">${b.nome} · ${b.q} questões</h3>` + TRILHAS.filter(t=>t.bloco===b.nome).map(t=>`
      <details ${V.trilha===t.id?"open":""}><summary>${t.nome}<span>${feitos(t.id)}/${t.postos.length}${t.q ? " · " + t.q : ""}</span></summary>
      <div class="tabela"><table><tr><th>Posto</th><th>Item do edital</th><th>Situação</th></tr>${postosDe(t.id).map(linha).join("")}</table></div></details>`).join("")).join("")}
    </div>
  </section>`;
  bindGo(); bindPostos();
}

/* ---------- Trilha ---------- */
function telaTrilha(){
  const tr = TRILHA[V.trilha], ps = postosDe(tr.id), px = proximo(tr.id);
  const itens = ps.map(p=>{
    const ok = !!S.aprovados[p.id], lib = liberado(p.id), cur = px && px.id===p.id;
    const cls = ok ? "ok" : (cur ? "atual" : (lib ? "" : "bloq"));
    const sub = ok ? `Concluído com nota ${S.aprovados[p.id].nota}` : (lib ? p.r : "Libera com nota 7 no posto anterior");
    return `<li class="posto ${cls}"><span class="pin" aria-hidden="true">${ok?"✓":p.n+1}</span>
      <button class="card" data-p="${p.id}" ${lib?"":'aria-disabled="true"'}><span class="tit">${p.t}</span><span class="sub">${sub}</span></button></li>`;
  }).join("");
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" data-go="painel">‹ Voltar ao painel</button>
    <p class="meta">${tr.bloco}${tr.q ? " · " + tr.q : ""}</p>
    <h2>${tr.nome}</h2>
    <div class="bar" aria-hidden="true"><i style="width:${(feitos(tr.id)/ps.length*100).toFixed(0)}%"></i></div>
    <p class="meta">${feitos(tr.id)} de ${ps.length} postos concluídos</p>
    <ol class="rota">${itens}</ol>
  </section>`;
  bindGo();
  $app.querySelectorAll("[data-p]").forEach(b=>b.onclick=()=>{ if(liberado(b.dataset.p)) ir({tela:"posto", posto:b.dataset.p, aba:"aula"}); });
}

/* ---------- Posto ---------- */
function telaPosto(){
  const p = POSTO[V.posto], temAula = !!AULAS[p.id], temQ = !!BANCO[p.id];
  const tent = S.tentativas[p.id] || [], aprov = S.aprovados[p.id];
  if(S.ultimo !== p.id){ S.ultimo = p.id; salvar(); }
  const rv = S.revisoes[p.id];
  let corpo;
  if(V.aba==="aula"){
    corpo = temAula ? `<article class="aula">${AULAS[p.id]}</article>` : `<div class="vazio"><strong>Aula em produção</strong><br>Este posto será liberado aqui assim que o conteúdo estiver revisado.</div>`;
  } else if(V.aba==="resumo"){
    corpo = temAula ? `<div class="resumo-topo">Resumo de uma página: mapa do assunto, destaques da aula, armadilhas da banca e quadro-resumo. Use na revisão e na véspera da prova.</div><article class="aula" id="resumo"></article>` : `<div class="vazio">Resumo em produção.</div>`;
  } else {
    const revHoje = rv && rv.etapa < INTERVALOS.length && rv.prox <= Date.now();
    corpo = `<div class="regra"><strong>Como funciona:</strong> ${N_QUESTOES} questões sorteadas entre as ${temQ?BANCO[p.id].length:0} do posto (fáceis, médias e difíceis). Com ${NOTA_MIN} acertos ou mais, o posto conta como concluído e entra na revisão espaçada. Cada nova tentativa prioriza questões que você ainda não viu.</div>
      ${revHoje ? `<p class="historico" style="margin:0 0 10px"><span class="pill amb">Revisão ${rv.etapa+1} de ${INTERVALOS.length} pendente</span> Faça as questões para registrar a revisão.</p>` : ""}
      ${temQ ? `<button class="btn full" id="iniciar">${aprov ? (revHoje ? "Fazer a revisão" : "Treinar de novo") : (tent.length ? "Tentar de novo com questões novas" : "Começar as questões")}</button>` : `<div class="vazio"><strong>Banco de questões em produção</strong></div>`}
      ${tent.length ? `<p class="historico">Tentativas: ${tent.map(x=>x.nota).join(" · ")}${aprov ? " — posto concluído" : ""}</p>` : ""}
      ${IS_OWNER && temQ ? `<p style="margin-top:14px"><button class="btn sec full" id="banco">Revisar banco de questões (${BANCO[p.id].length})</button></p>` : ""}`;
  }
  const idx = POSTOS.indexOf(p), ant = POSTOS[idx-1], seg = POSTOS[idx+1];
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" id="voltar">‹ ${p.tr.nome}</button>
    <p class="meta">Posto ${p.n+1} de ${p.tr.postos.length}${aprov ? ` · <span class="pill ok">Concluído · ${aprov.nota}/10</span>` : ""}</p>
    <h2>${p.t}</h2>
    <p class="meta">${p.r}</p>
    <div class="abas" role="tablist">
      <button role="tab" aria-selected="${V.aba==="aula"}" data-aba="aula">Aula</button>
      <button role="tab" aria-selected="${V.aba==="resumo"}" data-aba="resumo">Resumo</button>
      <button role="tab" aria-selected="${V.aba==="questoes"}" data-aba="questoes">Questões</button>
    </div>
    <div class="painel">${corpo}</div>
    <div class="acoes" style="margin:0 0 40px">
      ${ant && ant.tr===p.tr ? `<button class="btn sec peq" data-abrir="${ant.id}">‹ Posto anterior</button>` : "<span></span>"}
      ${seg && seg.tr===p.tr ? `<button class="btn sec peq" data-abrir="${seg.id}">Próximo posto ›</button>` : ""}
    </div>
  </section>`;
  if(V.aba==="aula" && temAula) montarAula($app.querySelector("article.aula"), p.id);
  if(V.aba==="resumo" && temAula) montarResumo(document.getElementById("resumo"), p.id);
  document.getElementById("voltar").onclick = ()=>ir({tela:"trilha", trilha:p.tr.id});
  $app.querySelectorAll("[data-aba]").forEach(b=>{ if(b.getAttribute("role")==="tab") b.onclick=()=>ir({aba:b.dataset.aba}); });
  bindPostos();
  const ini = document.getElementById("iniciar"); if(ini) ini.onclick = ()=>iniciarProva(p.id);
  const bb = document.getElementById("banco"); if(bb) bb.onclick = ()=>ir({tela:"banco"});
}

/* ---------- Aula: formato apostila ---------- */
function txtDe(el){ return (el.textContent||"").replace(/\s+/g," ").trim(); }
const TIPOS = [
  [/^cuidado/i, "cuidado"], [/^cai muito/i, "caimuito"], [/^macete/i, "macete"],
  [/^o que é, em uma frase/i, "conceito"], [/^regra principal/i, "regra-p"]
];
function tipoDe(el){ const s = el.querySelector(":scope > p:first-child > strong:first-child, :scope > strong:first-child"); if(!s) return null; const t = txtDe(s); for(const [re,k] of TIPOS) if(re.test(t)) return [k, s]; return null; }
function rotulo(k){ const sp = document.createElement("span"); sp.className = "rot"; sp.innerHTML = ICONE[k] + ROTULO[k]; return sp; }
function montarCaixas(art){
  if(!art) return;
  // caixas seguidas no Markdown viram um só blockquote: separa em um bloco por rótulo
  art.querySelectorAll("blockquote:not(.lei)").forEach(bq=>{
    const ps = [...bq.children]; let alvo = bq;
    ps.forEach((el,i)=>{
      if(i===0) return;
      const s = el.tagName==="P" && el.querySelector(":scope > strong:first-child");
      if(s && el.firstChild===s && TIPOS.slice(0,3).some(([re])=>re.test(txtDe(s)))){ const nb = document.createElement("blockquote"); alvo.after(nb); alvo = nb; }
      if(alvo!==bq) alvo.appendChild(el);
    });
  });
  art.querySelectorAll("blockquote:not(.lei)").forEach(bq=>{
    const r = tipoDe(bq); if(!r) return; const [k, s] = r;
    s.remove();
    const p = bq.querySelector("p"); if(p) p.innerHTML = p.innerHTML.replace(/^\s*[:!]?\s*/,"");
    bq.classList.add("callout", k); bq.prepend(rotulo(k));
  });
  art.querySelectorAll(":scope > p").forEach(p=>{
    const s = p.querySelector(":scope > strong:first-child"); if(!s || p.firstChild!==s) return;
    const t = txtDe(s);
    for(const [re,k] of TIPOS.slice(3)) if(re.test(t)){
      s.remove(); p.innerHTML = p.innerHTML.replace(/^\s*/,"");
      const d = document.createElement("div"); d.className = "callout " + k; p.before(d); d.append(rotulo(k), p); break;
    }
  });
}
function montarAula(art, pid){
  if(!art) return;
  art.classList.add("apostila");
  const hs = [...art.querySelectorAll(":scope > h3")];
  if(hs.length > 2){
    const nav = document.createElement("nav"); nav.className = "sumario"; nav.setAttribute("aria-label","Sumário da aula");
    nav.innerHTML = '<p>Nesta aula</p><ul>' + hs.map((h,i)=>`<li><a href="#" data-i="${i}">${txtDe(h)}</a></li>`).join("") + '</ul>';
    nav.querySelectorAll("a").forEach(a=>a.onclick = e=>{ e.preventDefault(); hs[+a.dataset.i].scrollIntoView({block:"start"}); });
    hs[0].before(nav);
  }
  formatarTabelas(art);
  montarCaixas(art);
  art.querySelectorAll(".box").forEach(b=>{ const a = document.createElement("aside"); a.className = "nota"; a.innerHTML = b.innerHTML; b.replaceWith(a); });
  art.querySelectorAll("ol.alts").forEach(ol=>{
    let n = ol.nextElementSibling;
    if(n && n.tagName==="P" && /^Resposta:/.test(txtDe(n))){ const d = document.createElement("details"); d.className = "gab"; d.innerHTML = "<summary>Ver resposta comentada</summary>"; n.before(d); d.appendChild(n); }
  });
  if(window.innerWidth <= 520) art.querySelectorAll(".fig").forEach(f=>{ const d = document.createElement("p"); d.className = "ref"; d.textContent = "Arraste o esquema para o lado para ver tudo."; f.insertBefore(d, f.firstChild); });
  const nq = (BANCO[pid]||[]).length;
  if(nq){ const fim = document.createElement("p"); fim.className = "fim-aula"; fim.innerHTML = `Terminou a leitura? <a href="#">Faça as questões deste posto</a>: são ${nq}, e cada tentativa sorteia ${N_QUESTOES}. Para revisar depois, use a aba <a href="#" data-r="1">Resumo</a>.`; fim.querySelector("a").onclick = e=>{ e.preventDefault(); ir({aba:"questoes"}); }; fim.querySelector("[data-r]").onclick = e=>{ e.preventDefault(); ir({aba:"resumo"}); }; art.appendChild(fim); }
  art.appendChild(caixaReportar(pid));
}
function formatarTabelas(art){
  art.querySelectorAll(".tabela > table").forEach(tb=>{
    const rows = [...tb.rows].map(r=>[...r.cells]); if(rows.length < 2) return;
    const head = rows[0].map(txtDe), box = tb.parentElement, corpo = rows.slice(1);
    if(head.length !== 2) return;
    const w = document.createElement("div");
    if(/^armadilha/i.test(head[0])){
      w.innerHTML = '<ul class="pegas">' + corpo.map(r=>`<li><span class="pg-t">${r[0].innerHTML}</span> — ${r[1].innerHTML}</li>`).join("") + '</ul>';
    } else if(/fala corrente|errad|evite|não diga/i.test(head[0]) && /norma|cert|use|padrão/i.test(head[1])){
      w.innerHTML = '<ol class="exs">' + corpo.map(r=>`<li><span class="rej">${r[0].innerHTML}</span>${r[1].innerHTML}</li>`).join("") + '</ol>' + (art.querySelector(".exs") ? "" : '<p class="exs-nota">O asterisco marca a forma que a norma-padrão não aceita.</p>');
    } else {
      w.innerHTML = '<dl class="pares">' + (head[0]||head[1] ? `<div class="pares-h"><dt>${head[0]}</dt><dd>${head[1]}</dd></div>` : "") + corpo.map(r=>`<div><dt>${r[0].innerHTML}</dt><dd>${r[1].innerHTML}</dd></div>`).join("") + '</dl>';
    }
    box.replaceWith(...w.childNodes);
  });
}
function montarResumo(art, pid){
  if(!art) return;
  const tmp = document.createElement("div"); tmp.innerHTML = AULAS[pid];
  const secoes = {}; let atual = null;
  [...tmp.children].forEach(el=>{
    if(el.tagName==="H3"){ atual = txtDe(el); secoes[atual] = [el]; } else if(atual) secoes[atual].push(el);
  });
  const pega = re => Object.keys(secoes).find(k=>re.test(k));
  const partes = [];
  const kMapa = pega(/mapa do assunto/i); if(kMapa) partes.push(...secoes[kMapa].filter(e=>e.tagName!=="P" || !/^Versão/.test(txtDe(e))));
  const destaques = [...tmp.querySelectorAll("blockquote:not(.lei)")].filter(b=>tipoDe(b));
  if(destaques.length){ const h = document.createElement("h3"); h.textContent = "Destaques da aula"; partes.push(h, ...destaques); }
  const kArm = pega(/onde a vunesp|pegadinhas/i); if(kArm) partes.push(...secoes[kArm]);
  const kRes = pega(/quadro-resumo/i); if(kRes) partes.push(...secoes[kRes]);
  partes.forEach(e=>art.appendChild(e));
  art.classList.add("apostila");
  formatarTabelas(art); montarCaixas(art);
  const fim = document.createElement("p"); fim.className = "fim-aula"; fim.innerHTML = `Revisou? <a href="#">Teste-se com as questões</a> ou volte para a <a href="#" data-a="1">aula completa</a>.`;
  fim.querySelector("a").onclick = e=>{ e.preventDefault(); ir({aba:"questoes"}); };
  fim.querySelector("[data-a]").onclick = e=>{ e.preventDefault(); ir({aba:"aula"}); };
  art.appendChild(fim);
}
function caixaReportar(pid){
  const d = document.createElement("div"); d.className = "reportar";
  d.innerHTML = `<p><strong>Encontrou um erro ou uma lei desatualizada?</strong> <button class="link" type="button">Avise a equipe</button></p>`;
  d.querySelector("button").onclick = ()=>{
    d.innerHTML = `<label for="corr-${pid}"><strong>O que precisa ser corrigido nesta aula?</strong></label>
      <textarea id="corr-${pid}" placeholder="Ex.: na seção 2, o prazo citado mudou com a Lei nº ..."></textarea>
      <button class="btn peq" type="button" id="enviar-corr">Enviar</button>`;
    d.querySelector("#enviar-corr").onclick = async ()=>{
      const txt = d.querySelector("textarea").value.trim();
      if(txt.length < 5){ d.querySelector("textarea").focus(); return; }
      S.correcoes.push({pid, texto: txt.slice(0,2000), data: Date.now()}); await salvar();
      d.innerHTML = `<p><strong>Recebido.</strong> O aviso foi registrado e será conferido na fonte oficial antes da próxima atualização do material.</p>`;
    };
  };
  return d;
}

/* ---------- Sorteio: evita repetir a última tentativa e prioriza as menos vistas ---------- */
const POR_NIVEL = {1:3, 2:4, 3:3}; // fáceis, médias, difíceis em cada tentativa
function sortear(pid){
  const tent = S.tentativas[pid] || [];
  const ultima = new Set(tent.length ? tent[tent.length-1].ids : []);
  const peso = q => (S.vistas[q.id]||0)*10 + (ultima.has(q.id) ? 100 : 0) + Math.random();
  const banco = BANCO[pid].slice().sort((a,b)=>peso(a)-peso(b));
  if(!banco.some(q=>q.n)) return banco.slice(0, N_QUESTOES);
  let sel = [];
  [1,2,3].forEach(n=>{ sel = sel.concat(banco.filter(q=>q.n===n).slice(0, POR_NIVEL[n])); });
  if(sel.length < N_QUESTOES) sel = sel.concat(banco.filter(q=>!sel.includes(q)).slice(0, N_QUESTOES-sel.length));
  return sel.sort((a,b)=>(a.n||0)-(b.n||0));
}
function montarItens(qs){ return qs.map(q=>({q, ordem: embaralhar(q.a.map((txt,i)=>({txt, certa:i===0}))), escolha:null})); }
function iniciarProva(pid){
  const rv = S.revisoes[pid];
  const modo = (S.aprovados[pid] && rv && rv.etapa < INTERVALOS.length && rv.prox <= Date.now()) ? "revisao" : "posto";
  Q = {pid, modo, i:0, itens: montarItens(sortear(pid))};
  ir({tela:"prova"});
}
function iniciarErros(){
  const ids = [...new Set([...Object.keys(S.erros), ...Object.keys(S.marcadas)])].filter(k=>QIDX[k]);
  const ord = ids.sort((a,b)=>((S.erros[b]||{}).vezes||0)-((S.erros[a]||{}).vezes||0) || Math.random()-.5).slice(0, N_QUESTOES);
  Q = {pid:null, modo:"erros", i:0, itens: montarItens(embaralhar(ord.map(k=>QIDX[k].q)))};
  ir({tela:"prova"});
}

/* ---------- Prova ---------- */
function telaProva(){
  const it = Q.itens[Q.i], ultima = Q.i===Q.itens.length-1, marc = !!S.marcadas[it.q.id];
  const origem = Q.modo==="erros" ? `Caderno de erros · ${POSTO[QIDX[it.q.id].pid].t}` : (Q.modo==="revisao" ? `Revisão · ${POSTO[Q.pid].t}` : POSTO[Q.pid].t);
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" id="sair">‹ Sair das questões</button>
    <div id="conf-sair"></div>
    <p class="meta">${origem}</p>
    <div class="qtopo"><span class="num">Questão ${Q.i+1} de ${Q.itens.length}</span><button class="marcar" id="marcar" aria-pressed="${marc}">${marc ? "Marcada para revisar" : "Marcar para revisar"}</button></div>
    <div class="bar" aria-hidden="true"><i style="width:${(Q.i/Q.itens.length*100)}%"></i></div>
    <div class="qcard">
      ${it.q.tx ? `<blockquote class="txt">${TEXTOS[it.q.tx]}</blockquote>` : ""}<p class="enun">${it.q.e}</p>
      ${it.ordem.map((o,k)=>`<button class="alt" data-k="${k}" aria-pressed="${it.escolha===k}"><span class="l">${LETRAS[k]}</span><span>${o.txt}</span></button>`).join("")}
    </div>
    <div class="acoes">
      <button class="btn sec" id="ant" ${Q.i===0?"disabled":""}>Anterior</button>
      <button class="btn" id="prox" ${it.escolha===null?"disabled":""}>${ultima ? "Corrigir" : "Próxima"}</button>
    </div>
  </section>`;
  $app.querySelectorAll(".alt").forEach(b=>b.onclick=()=>{ it.escolha = +b.dataset.k; telaProva(); });
  document.getElementById("marcar").onclick = ()=>{ if(S.marcadas[it.q.id]) delete S.marcadas[it.q.id]; else S.marcadas[it.q.id] = {pid: QIDX[it.q.id].pid, data: Date.now()}; salvar(); telaProva(); };
  document.getElementById("ant").onclick = ()=>{ Q.i--; telaProva(); };
  document.getElementById("prox").onclick = ()=>{ if(ultima) corrigir(); else { Q.i++; telaProva(); } };
  document.getElementById("sair").onclick = ()=>{
    const c = document.getElementById("conf-sair");
    c.innerHTML = `<div class="confirma"><p>Sair agora descarta esta tentativa.</p><button class="btn peq" id="sair-sim">Sair</button><button class="btn sec peq" id="sair-nao">Continuar respondendo</button></div>`;
    document.getElementById("sair-nao").onclick = ()=>{ c.innerHTML = ""; };
    document.getElementById("sair-sim").onclick = ()=>{ const pid=Q.pid, m=Q.modo; Q=null; if(m==="erros") ir({tela:"erros"}); else ir({tela:"posto", posto:pid, aba:"questoes"}); };
  };
}
async function corrigir(){
  const nota = Q.itens.filter(it=>it.ordem[it.escolha].certa).length;
  Q.itens.forEach(it=>{
    const id = it.q.id; S.vistas[id] = (S.vistas[id]||0)+1;
    if(it.ordem[it.escolha].certa){ delete S.erros[id]; if(Q.modo==="erros") delete S.marcadas[id]; }
    else { const e = S.erros[id] || {pid: QIDX[id].pid, vezes:0}; e.vezes++; e.data = Date.now(); S.erros[id] = e; }
  });
  if(Q.modo!=="erros"){
    (S.tentativas[Q.pid] = S.tentativas[Q.pid] || []).push({nota, data:Date.now(), ids:Q.itens.map(it=>it.q.id)});
    if(nota>=NOTA_MIN && !S.aprovados[Q.pid]){ S.aprovados[Q.pid] = {nota, data:Date.now()}; S.revisoes[Q.pid] = {etapa:0, prox: Date.now() + INTERVALOS[0]*DIA}; }
    else if(Q.modo==="revisao"){
      const rv = S.revisoes[Q.pid];
      if(nota>=NOTA_MIN){ rv.etapa++; rv.prox = rv.etapa < INTERVALOS.length ? Date.now() + INTERVALOS[rv.etapa]*DIA : Infinity; }
      else rv.prox = Date.now() + DIA;
      Q.revEtapa = rv.etapa;
    }
  }
  Q.nota = nota;
  await salvar();
  ir({tela:"resultado"});
}

/* ---------- Resultado ---------- */
function telaResultado(){
  const ok = Q.modo==="erros" ? Q.nota >= Math.ceil(Q.itens.length*NOTA_MIN/N_QUESTOES) : Q.nota>=NOTA_MIN;
  const revisao = Q.itens.map((it,n)=>{
    const acertou = it.ordem[it.escolha].certa, certa = it.ordem.findIndex(o=>o.certa);
    return `<div class="rev ${acertou?"ok":"bad"}"><div class="st"><span>Questão ${n+1}: ${acertou?"acertou":"errou"}</span>${acertou ? "" : `<span class="pill bad">Foi para o caderno de erros</span>`}</div>
      ${it.q.tx ? `<blockquote class="txt">${TEXTOS[it.q.tx]}</blockquote>` : ""}<p>${it.q.e}</p>${acertou ? "" : `<p>Sua resposta: ${LETRAS[it.escolha]}) ${it.ordem[it.escolha].txt}</p>`}
      <p><strong>Correta: ${LETRAS[certa]}) ${it.ordem[certa].txt}</strong></p><p class="ref">${it.q.c}</p></div>`;
  }).join("");
  let titulo, texto, botoes = "";
  if(Q.modo==="erros"){
    const restam = nErros();
    titulo = ok ? "Bom treino." : "Continue treinando.";
    texto = `As questões que você acertou saíram do caderno. Restam ${restam} ${restam===1?"questão":"questões"} erradas.`;
    botoes = `${nErros()||nMarcadas() ? `<button class="btn" id="mais-erros">Treinar mais 10</button>` : ""}<button class="btn sec" data-go="painel">Voltar ao painel</button>`;
  } else {
    const p = POSTO[Q.pid], prox = POSTO[p.tr.id+"-"+(p.n+2)];
    if(Q.modo==="revisao"){
      titulo = ok ? "Revisão registrada." : "Revise o resumo e tente amanhã.";
      texto = ok ? (Q.revEtapa < INTERVALOS.length ? `A próxima revisão deste posto será em ${INTERVALOS[Q.revEtapa]} dias.` : "Você concluiu as três revisões deste posto.") : "O posto volta para a lista de revisões amanhã.";
      botoes = `${ok ? "" : `<button class="btn" id="resumo">Ler o resumo</button>`}<button class="btn sec" data-go="painel">Voltar ao painel</button>`;
    } else {
      titulo = ok ? (prox ? "Posto concluído." : "Matéria concluída.") : "Ainda não foi desta vez.";
      texto = ok ? `${prox ? `Próximo: ${prox.t}. ` : `Você terminou ${p.tr.nome}. `}Este posto volta para revisão amanhã.` : `Você precisa de ${NOTA_MIN} acertos. Revise a correção abaixo e tente de novo: as questões serão outras.`;
      botoes = `${ok && prox ? `<button class="btn" id="seguir">Ir para o próximo posto</button>` : (ok ? "" : `<button class="btn" id="denovo">Tentar de novo</button>`)}<button class="btn sec" id="trilha">Ver a matéria</button>`;
    }
  }
  $app.innerHTML = `
  <section class="topico">
    <div class="res ${ok?"ok":"bad"}">
      <div class="nota num">${Q.nota}/${Q.itens.length}</div>
      <h2>${titulo}</h2>
      <p>${texto}</p>
      <div class="acoes">${botoes}</div>
    </div>
    <h2 style="font-size:24px;margin:8px 0">Correção comentada</h2>
    ${revisao}
  </section>`;
  bindGo();
  const s = document.getElementById("seguir"); if(s){ const p = POSTO[Q.pid]; s.onclick = ()=>ir({tela:"posto", posto:POSTO[p.tr.id+"-"+(p.n+2)].id, aba:"aula"}); }
  const d = document.getElementById("denovo"); if(d) d.onclick = ()=>iniciarProva(Q.pid);
  const t = document.getElementById("trilha"); if(t) t.onclick = ()=>ir({tela:"trilha", trilha:POSTO[Q.pid].tr.id});
  const r = document.getElementById("resumo"); if(r) r.onclick = ()=>ir({tela:"posto", posto:Q.pid, aba:"resumo"});
  const m = document.getElementById("mais-erros"); if(m) m.onclick = iniciarErros;
}

/* ---------- Caderno de erros ---------- */
function telaErros(){
  const ids = [...new Set([...Object.keys(S.erros), ...Object.keys(S.marcadas)])].filter(k=>QIDX[k]);
  const porPosto = {};
  ids.forEach(k=>{ const pid = QIDX[k].pid; (porPosto[pid] = porPosto[pid] || []).push(k); });
  const grupos = Object.keys(porPosto).sort((a,b)=>POSTOS.indexOf(POSTO[a])-POSTOS.indexOf(POSTO[b]));
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" data-go="painel">‹ Voltar ao painel</button>
    <h2>Caderno de erros</h2>
    <p class="meta">${nErros()} ${nErros()===1?"questão errada":"questões erradas"} · ${nMarcadas()} ${nMarcadas()===1?"marcada":"marcadas"} para revisar</p>
    ${ids.length ? `<p style="margin:14px 0"><button class="btn full" id="treinar">Treinar ${Math.min(N_QUESTOES, ids.length)} questões do caderno</button></p>
      <p class="historico">Ao acertar uma questão no treino, ela sai do caderno. As que você errou mais vezes aparecem primeiro.</p>
      ${grupos.map(pid=>`<h3 style="font-size:22px;margin:22px 0 4px">${POSTO[pid].t}</h3><p class="meta">${POSTO[pid].tr.nome} · <button class="link" data-abrir="${pid}" data-aba="resumo">ler o resumo</button></p>
        ${porPosto[pid].map(k=>{ const q = QIDX[k].q, e = S.erros[k];
          return `<details class="rev ${e?"bad":"ok"}"><summary class="st" style="cursor:pointer"><span>${e ? `Errou ${e.vezes} ${e.vezes===1?"vez":"vezes"}` : "Marcada"}</span><span style="color:var(--ink);font-weight:500;flex:1 1 100%">${q.e}</span></summary>
            ${q.tx ? `<blockquote class="txt">${TEXTOS[q.tx]}</blockquote>` : ""}<p><strong>Correta: ${q.a[0]}</strong></p><p class="ref">${q.c}</p></details>`; }).join("")}`).join("")}`
    : `<div class="vazio" style="margin-top:16px"><strong>Seu caderno está vazio.</strong><br>Toda questão que você errar entra aqui automaticamente. Durante as questões, use “Marcar para revisar” para guardar também as que acertou no chute.</div>`}
  </section>`;
  bindGo(); bindPostos();
  const t = document.getElementById("treinar"); if(t) t.onclick = iniciarErros;
}

/* ---------- Revisão do banco (visível só para o dono) ---------- */
function telaBanco(){
  const p = POSTO[V.posto], qs = BANCO[p.id] || [];
  const nome = {1:"Fácil",2:"Média",3:"Difícil"};
  const cont = [1,2,3].map(n=>`${nome[n]}: ${qs.filter(q=>q.n===n).length}`).join(" · ");
  $app.innerHTML = `<section class="topico"><button class="voltar" id="voltar">‹ ${p.t}</button><h2>Banco de questões</h2><p class="meta">${qs.length} questões · ${cont} · a alternativa correta aparece em negrito</p>${qs.map((q,i)=>`<div class="rev ok"><div class="st">${i+1}. ${nome[q.n]||""} · ${q.id}</div>${q.tx?`<blockquote class="txt">${TEXTOS[q.tx]}</blockquote>`:""}<p>${q.e}</p><ol class="alts" type="A">${q.a.map((x,k)=>`<li>${k===0?`<strong>${x}</strong>`:x}</li>`).join("")}</ol><p class="ref">${q.c}</p></div>`).join("")}</section>`;
  document.getElementById("voltar").onclick = ()=>ir({tela:"posto", aba:"questoes"});
}

/* ---------- Guia do TAF (Anexo II do edital) ---------- */
function telaTAF(){
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" data-go="painel">‹ Voltar ao painel</button>
    <h2>Guia do Teste de Aptidão Física</h2>
    <p class="meta">Edital 02/2026, Capítulo XIII e Anexo II · previsto para 05 e 06/06/2027</p>
    <article class="aula">
      <h3>Por que o TAF pesa tanto</h3>
      <p>A nota final é a soma da prova objetiva (até 50 pontos) com a nota do TAF (até 100 pontos), e a maior nota no TAF é o primeiro critério de desempate. <span class="ref">(itens 13.31, 15.1 e 15.2)</span></p>
      <h3>Como a nota é calculada</h3>
      <p>Cada uma das cinco provas vale de 20 a 100 pontos, e a nota do TAF é a média das cinco. Para seguir no concurso, é preciso média de pelo menos 50 e no mínimo 20 pontos em cada prova. Não há segunda tentativa. <span class="ref">(itens 13.27 a 13.30)</span></p>
      <h3>Índices mínimo (20 pontos) e máximo (100 pontos)</h3>
      <div class="tabela"><table>
        <tr><th>Prova</th><th>Feminino</th><th>Masculino</th></tr>
        <tr><td>Barra fixa (isometria F / flexão M)</td><td>5 s a 45 s</td><td>3 a 11 repetições</td></tr>
        <tr><td>Abdominal com flexão dos joelhos, 1 min</td><td>22 a 38</td><td>30 a 46</td></tr>
        <tr><td>Flexão de braço, 1 min</td><td>12 a 28 (joelhos apoiados)</td><td>14 a 30</td></tr>
        <tr><td>Corrida de 50 m</td><td>9”50 a 7”50</td><td>8”25 a 6”25</td></tr>
        <tr><td>Corrida de 12 minutos</td><td>1.800 m a 2.600 m</td><td>2.200 m a 3.000 m</td></tr>
      </table></div>
      <blockquote><p><strong>Cuidado!</strong> Sem luvas na barra; na flexão masculina na barra não valem impulso, balanço ou kipping; repetições fora do padrão do Anexo II não contam.</p></blockquote>
      <p class="ref">Fonte: Edital 02/2026 da Guarda Municipal de Campinas, Anexo II. Confira sempre o texto oficial.</p>
    </article>
  </section>`;
  montarCaixas($app.querySelector("article.aula"));
  bindGo();
}

render();
</script>
</body>
</html>
