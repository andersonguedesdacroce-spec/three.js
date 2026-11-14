/* ---------- Índices ---------- */
const POSTOS = [];
TRILHAS.forEach(tr=>tr.postos.forEach((p,i)=>POSTOS.push({id:tr.id+"-"+(i+1), t:p[0], r:p[1], tr, n:i})));
const POSTO = Object.fromEntries(POSTOS.map(p=>[p.id,p]));
const TRILHA = Object.fromEntries(TRILHAS.map(t=>[t.id,t]));
const postosDe = tid => POSTOS.filter(p=>p.tr.id===tid);

/* ---------- Estado ---------- */
const KEY = "rota-gm-campinas-v2";
function novoEstado(){ return {acesso:false, aprovados:{}, tentativas:{}, vistas:{}, atualizado:0}; }
let S = (()=>{ try{ return JSON.parse(localStorage.getItem(KEY)) || novoEstado(); }catch(e){ return novoEstado(); } })();
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
      const remoto = JSON.parse(snap.data().estado);
      if((remoto.atualizado||0) > (S.atualizado||0)){ S = remoto; try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} render(); }
    } else if(S.atualizado){ salvar(); }
  }catch(e){}
})();

/* ---------- Utilidades ---------- */
const $app = document.getElementById("app");
const LETRAS = ["A","B","C","D","E"];
const embaralhar = arr => { const a = arr.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
const diasAte = d => Math.max(0, Math.ceil((d - new Date())/86400000));
const feitos = tid => postosDe(tid).filter(p=>S.aprovados[p.id]).length;
const MODO_REVISAO = true; // true = todos os postos liberados, sem nota mínima. Voltar para false para reativar a trava.
function liberado(pid){ const p = POSTO[pid]; if(!S.acesso) return false; if(MODO_REVISAO || p.n===0) return true; return !!S.aprovados[p.tr.id+"-"+p.n]; }
function proximo(tid){ return postosDe(tid).find(p=>!S.aprovados[p.id]) || null; }
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
function render(){
  const t = V.tela;
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
}

/* ---------- Página de vendas ---------- */
function telaHome(){
  const blocos = ["Conhecimentos Gerais","Conhecimentos Específicos"].map(b=>{
    const trs = TRILHAS.filter(t=>t.bloco===b);
    const cab = b==="Conhecimentos Gerais" ? "Conhecimentos Gerais — 20 questões" : "Conhecimentos Específicos — 30 questões";
    return `<p class="bloco-tit">${cab}</p><ul class="lista-materias">${trs.map(t=>`<li><span>${t.nome}</span><span>${t.postos.length} ${t.postos.length===1?"posto":"postos"}</span></li>`).join("")}</ul>`;
  }).join("");
  $app.innerHTML = `
  <section class="lp-hero">
    <h1>Guarda Municipal de Campinas: todo o edital em trilhas que você conclui uma a uma</h1>
    <p>Cada matéria do edital vira uma trilha com aula escrita, vídeo e questões no estilo Vunesp. Você só avança no assunto quando acerta pelo menos 7 de 10.</p>
    <div class="cta-row">
      ${S.acesso ? `<button class="btn" data-go="painel">Ir para o meu painel</button>` : `<button class="btn amber" data-go="checkout">Quero meu acesso</button>`}
      <a class="btn sec" href="#materias">Ver as trilhas</a>
    </div>
    <div class="credencial" aria-label="Dados do concurso">
      <div class="faixa"><strong>Edital 02/2026 · Prefeitura de Campinas</strong><span>Vunesp</span></div>
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

  <section class="lp-sec" id="materias">
    <h2>Todas as matérias do edital, sem exceção</h2>
    <p>${TRILHAS.length} trilhas e ${POSTOS.length} postos de estudo, montados a partir do Anexo I. Cada trilha corresponde a uma matéria cobrada na prova objetiva.</p>
    ${blocos}
  </section>

  <section class="lp-sec">
    <h2>Como funciona</h2>
    <ol class="passos">
      <li><strong>Escolha a trilha.</strong> Todas as matérias ficam abertas desde o primeiro dia; você alterna entre elas como preferir.</li>
      <li><strong>Estude o posto.</strong> Aula escrita com os artigos da lei, vídeo explicativo e quadro-resumo.</li>
      <li><strong>Faça as 10 questões.</strong> Acertou 7 ou mais, o próximo posto da trilha é liberado.</li>
      <li><strong>Errou? Tente de novo.</strong> A nova tentativa traz questões diferentes e a correção comentada mostra onde ajustar.</li>
    </ol>
  </section>

  <section class="lp-sec">
    <div class="destaque">
      <h2>O teste físico vale o dobro da prova escrita</h2>
      <p>Pelo edital, a nota final é a soma da prova objetiva, que vale até 50 pontos, com o TAF, que vale até 100. O TAF também é o primeiro critério de desempate.</p>
      <p>O painel traz o guia do TAF com as cinco provas, os índices mínimos e o cálculo da nota, tudo conforme o Anexo II.</p>
    </div>
  </section>

  <section class="lp-sec">
    <div class="oferta-box">
      <h2>Acesso completo até a prova</h2>
      <ul>
        <li>${TRILHAS.length} trilhas cobrindo todo o conteúdo programático</li>
        <li>Questões que se renovam a cada tentativa</li>
        <li>Guia do Teste de Aptidão Física</li>
        <li>Simulado final no formato da prova: 50 questões em 3 horas</li>
        <li>Progresso salvo, no celular ou no computador</li>
      </ul>
      <div class="preco"><b>R$ 97</b><span>pagamento único, no Pix ou no cartão</span></div>
      ${S.acesso ? `<button class="btn full" data-go="painel">Ir para o meu painel</button>` : `<button class="btn amber full" data-go="checkout">Quero meu acesso</button>`}
    </div>
  </section>

  <section class="lp-sec faq">
    <h2>Perguntas frequentes</h2>
    <details><summary>Quando o acesso é liberado?</summary><p>No Pix, logo após a confirmação do pagamento. No cartão, assim que a operadora aprovar.</p></details>
    <details><summary>Posso estudar pelo celular?</summary><p>Sim. O painel funciona no navegador do celular e do computador, e o progresso fica salvo.</p></details>
    <details><summary>E se uma lei mudar até a prova?</summary><p>O edital diz que alterações legais posteriores à sua publicação não serão cobradas. O material segue o texto vigente em 11/11/2026.</p></details>
    <details><summary>Posso desistir da compra?</summary><p>Sim. Você tem 7 dias para exercer o direito de arrependimento, conforme o Código de Defesa do Consumidor.</p></details>
  </section>
  <p class="aviso">Material preparatório independente, sem vínculo com a Prefeitura de Campinas ou com a Fundação Vunesp.</p>`;
  bindGo();
}
function bindGo(){ $app.querySelectorAll("[data-go]").forEach(b=>b.onclick=()=>ir({tela:b.dataset.go})); }

/* ---------- Checkout (demonstração) ---------- */
let modoPag = null;
function telaCheckout(){
  $app.innerHTML = `
  <section class="topico">
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
  const meta = Math.ceil(restantes / Math.max(1, Math.ceil(diasAte(FIM_CONTEUDO)/7)));
  const card = tr => {
    const f = feitos(tr.id), n = tr.postos.length, px = proximo(tr.id);
    return `<button class="tcard ${f===n?"feita":""}" data-tr="${tr.id}">
      <span class="nome">${tr.nome}</span>
      <span class="bar fina" aria-hidden="true"><i style="width:${(f/n*100).toFixed(0)}%"></i></span>
      <span class="info">${f} de ${n} postos${px ? ` · próximo: ${px.t}` : " · trilha concluída"}</span>
    </button>`;
  };
  const tudo = restantes===0;
  $app.innerHTML = `
  <section class="hero">
    <h1>Seu painel</h1>
    <p>${restantes ? `Para fechar o edital até 14/03, conclua cerca de ${meta} ${meta===1?"posto":"postos"} por semana, alternando as trilhas.` : "Você concluiu todas as trilhas. Faça o simulado final."}</p>
    <div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="${total}" aria-valuenow="${ok}"><i style="width:${(ok/total*100).toFixed(1)}%"></i></div>
    <div class="stats"><span>${ok} de ${total} postos</span><span>Prova em 21/03/2027</span></div>
  </section>
  <div class="trilhas" style="margin-top:14px">
    <button class="tcard taf" data-go="taf"><span class="nome">Guia do Teste de Aptidão Física</span><span class="info">Vale até 100 pontos na classificação final</span></button>
  </div>
  <p class="bloco-tit">Conhecimentos Gerais — 20 questões</p>
  <div class="trilhas">${TRILHAS.filter(t=>t.bloco==="Conhecimentos Gerais").map(card).join("")}</div>
  <p class="bloco-tit">Conhecimentos Específicos — 30 questões</p>
  <div class="trilhas">${TRILHAS.filter(t=>t.bloco==="Conhecimentos Específicos").map(card).join("")}</div>
  <p class="bloco-tit">Reta final</p>
  <div class="trilhas">
    <button class="tcard ${tudo?"":"trava"}" ${tudo?"":'aria-disabled="true"'}><span class="nome">Simulado final no formato Vunesp</span><span class="info">${tudo ? "50 questões em 3 horas · em produção" : "Libera ao concluir todas as trilhas"}</span></button>
  </div>
  <div class="rodape"><button id="reset">Reiniciar demonstração</button></div>`;
  bindGo();
  $app.querySelectorAll("[data-tr]").forEach(b=>b.onclick=()=>ir({tela:"trilha", trilha:b.dataset.tr}));
  document.getElementById("reset").onclick = async ()=>{ if(confirm("Apagar o progresso e voltar à página de vendas?")){ S = novoEstado(); modoPag=null; await salvar(); ir({tela:"home"}); } };
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
  let corpo;
  if(V.aba==="aula"){
    corpo = temAula ? `<article class="aula">${AULAS[p.id]}</article>` : `<div class="vazio"><strong>Aula em produção</strong><br>Este posto será liberado aqui assim que o conteúdo estiver revisado.</div>`;
  } else if(V.aba==="video"){
    corpo = `<div class="vazio"><strong>Vídeo em produção</strong><br>Aqui entra a aula animada deste posto, com os artigos da lei na tela.</div>`;
  } else {
    corpo = `<div class="regra"><strong>Como funciona:</strong> ${N_QUESTOES} questões sorteadas do banco deste posto. Com nota ${NOTA_MIN} ou mais, o próximo posto da trilha é liberado. Se não passar, a nova tentativa traz questões diferentes.</div>
      ${temQ ? `<button class="btn full" id="iniciar">${aprov ? "Treinar de novo" : (tent.length ? "Tentar de novo com questões novas" : "Começar as questões")}</button>` : `<div class="vazio"><strong>Banco de questões em produção</strong></div>`}
      ${tent.length ? `<p class="historico">Tentativas: ${tent.map(x=>x.nota).join(" · ")}${aprov ? " — posto concluído" : ""}</p>` : ""}
      ${IS_OWNER && temQ ? `<p style="margin-top:14px"><button class="btn sec full" id="banco">Revisar banco de questões (${BANCO[p.id].length})</button></p>` : ""}`;
  }
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" id="voltar">‹ ${p.tr.nome}</button>
    <p class="meta">Posto ${p.n+1} de ${p.tr.postos.length}</p>
    <h2>${p.t}</h2>
    <p class="meta">${p.r}</p>
    <div class="abas" role="tablist">
      <button role="tab" aria-selected="${V.aba==="aula"}" data-aba="aula">Aula</button>
      <button role="tab" aria-selected="${V.aba==="video"}" data-aba="video">Vídeo</button>
      <button role="tab" aria-selected="${V.aba==="questoes"}" data-aba="questoes">Questões</button>
    </div>
    <div class="painel">${corpo}</div>
  </section>`;
  if(V.aba==="aula" && temAula) montarAula($app.querySelector("article.aula"), p.id);
  document.getElementById("voltar").onclick = ()=>ir({tela:"trilha", trilha:p.tr.id});
  $app.querySelectorAll("[data-aba]").forEach(b=>b.onclick=()=>ir({aba:b.dataset.aba}));
  const ini = document.getElementById("iniciar"); if(ini) ini.onclick = ()=>iniciarProva(p.id);
  const bb = document.getElementById("banco"); if(bb) bb.onclick = ()=>ir({tela:"banco"});
}

/* ---------- Aula: formato apostila ---------- */
function txtDe(el){ return (el.textContent||"").replace(/\s+/g," ").trim(); }
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
  art.querySelectorAll(".box").forEach(b=>{ const a = document.createElement("aside"); a.className = "nota"; a.innerHTML = b.innerHTML; b.replaceWith(a); });
  art.querySelectorAll("ol.alts").forEach(ol=>{
    let n = ol.nextElementSibling;
    if(n && n.tagName==="P" && /^Resposta:/.test(txtDe(n))){ const d = document.createElement("details"); d.className = "gab"; d.innerHTML = "<summary>Ver resposta comentada</summary>"; n.before(d); d.appendChild(n); }
  });
  if(window.innerWidth <= 520) art.querySelectorAll(".fig").forEach(f=>{ const d = document.createElement("p"); d.className = "ref"; d.textContent = "Arraste o esquema para o lado para ver tudo."; f.insertBefore(d, f.firstChild); });
  const nq = (BANCO[pid]||[]).length;
  if(nq){ const fim = document.createElement("p"); fim.className = "fim-aula"; fim.innerHTML = `Terminou a leitura? <a href="#">Faça as questões deste posto</a>: são ${nq}, e cada tentativa sorteia ${N_QUESTOES}.`; fim.querySelector("a").onclick = e=>{ e.preventDefault(); ir({aba:"questoes"}); }; art.appendChild(fim); }
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
function iniciarProva(pid){
  Q = {pid, i:0, itens: sortear(pid).map(q=>({q, ordem: embaralhar(q.a.map((txt,i)=>({txt, certa:i===0}))), escolha:null}))};
  ir({tela:"prova"});
}

/* ---------- Prova ---------- */
function telaProva(){
  const it = Q.itens[Q.i], ultima = Q.i===Q.itens.length-1;
  $app.innerHTML = `
  <section class="topico">
    <button class="voltar" id="sair">‹ Sair das questões</button>
    <div class="qtopo"><span>Questão ${Q.i+1} de ${Q.itens.length}</span><span>Nota mínima: ${NOTA_MIN}</span></div>
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
  document.getElementById("ant").onclick = ()=>{ Q.i--; telaProva(); };
  document.getElementById("prox").onclick = ()=>{ if(ultima) corrigir(); else { Q.i++; telaProva(); } };
  document.getElementById("sair").onclick = ()=>{ if(confirm("Sair agora descarta esta tentativa. Continuar?")){ const pid=Q.pid; Q=null; ir({tela:"posto", posto:pid, aba:"questoes"}); } };
}
async function corrigir(){
  const nota = Q.itens.filter(it=>it.ordem[it.escolha].certa).length;
  (S.tentativas[Q.pid] = S.tentativas[Q.pid] || []).push({nota, data:Date.now(), ids:Q.itens.map(it=>it.q.id)});
  Q.itens.forEach(it=>{ S.vistas[it.q.id] = (S.vistas[it.q.id]||0)+1; });
  if(nota>=NOTA_MIN && !S.aprovados[Q.pid]) S.aprovados[Q.pid] = {nota, data:Date.now()};
  Q.nota = nota;
  await salvar();
  ir({tela:"resultado"});
}

/* ---------- Resultado ---------- */
function telaResultado(){
  const ok = Q.nota>=NOTA_MIN, p = POSTO[Q.pid], prox = POSTO[p.tr.id+"-"+(p.n+2)];
  const revisao = Q.itens.map((it,n)=>{
    const acertou = it.ordem[it.escolha].certa, certa = it.ordem.findIndex(o=>o.certa);
    return `<div class="rev ${acertou?"ok":"bad"}"><div class="st">Questão ${n+1}: ${acertou?"acertou":"errou"}</div>
      <p>${it.q.e}</p>${acertou ? "" : `<p>Sua resposta: ${LETRAS[it.escolha]}) ${it.ordem[it.escolha].txt}</p>`}
      <p><strong>Correta: ${LETRAS[certa]}) ${it.ordem[certa].txt}</strong></p><p class="ref">${it.q.c}</p></div>`;
  }).join("");
  $app.innerHTML = `
  <section class="topico">
    <div class="res ${ok?"ok":"bad"}">
      <div class="nota">${Q.nota}/10</div>
      <h2>${ok ? (prox ? "Posto concluído. O próximo foi liberado." : "Trilha concluída.") : "Ainda não foi desta vez."}</h2>
      <p>${ok ? (prox ? `Próximo: ${prox.t}.` : `Você terminou a trilha de ${p.tr.nome}.`) : `Você precisa de ${NOTA_MIN} acertos. Revise a correção abaixo e tente de novo: as questões serão outras.`}</p>
      <div class="acoes">
        ${ok && prox ? `<button class="btn" id="seguir">Ir para o próximo posto</button>` : (ok ? "" : `<button class="btn" id="denovo">Tentar de novo</button>`)}
        <button class="btn sec" id="trilha">Ver a trilha</button>
      </div>
    </div>
    <h2 style="font-size:24px;margin:8px 0">Correção comentada</h2>
    ${revisao}
  </section>`;
  const s = document.getElementById("seguir"); if(s) s.onclick = ()=>ir({tela:"posto", posto:prox.id, aba:"aula"});
  const d = document.getElementById("denovo"); if(d) d.onclick = ()=>iniciarProva(p.id);
  document.getElementById("trilha").onclick = ()=>ir({tela:"trilha", trilha:p.tr.id});
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
      <div class="box"><strong>Atenção às regras de execução:</strong> sem luvas na barra; na flexão masculina na barra não valem impulso, balanço ou kipping; repetições fora do padrão do Anexo II não contam.</div>
      <p class="ref">Fonte: Edital 02/2026 da Guarda Municipal de Campinas, Anexo II. Confira sempre o texto oficial.</p>
    </article>
  </section>`;
  bindGo();
}

render();
</script>
</body>
</html>
