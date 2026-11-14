// Compara o painel original com o gerado: extrai o <script> e avalia AULAS, BANCO, TEXTOS, TRILHAS.
const fs=require('fs'),vm=require('vm');
function dados(f){const h=fs.readFileSync(f,'utf8');const i=h.indexOf('<script>')+8,j=h.lastIndexOf('</script>');
 const js=h.slice(i,j); const cut=js.indexOf('/* ---------- Índices');
 const ctx={Date};vm.createContext(ctx);vm.runInContext(js.slice(0,cut)+';this.R={AULAS,BANCO,TEXTOS,TRILHAS,PROVA:+PROVA};',ctx);
 return {R:ctx.R,app:js.slice(cut),css:h.slice(0,i)};}
const a=dados(process.argv[2]),b=dados(process.argv[3]);
const ord=o=>JSON.stringify(o,(k,v)=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.entries(v).sort()):v);
for(const k of Object.keys(a.R)) console.log(k, ord(a.R[k])===ord(b.R[k])?'igual':'DIFERENTE');
console.log('app.js', a.app===b.app?'igual':'DIFERENTE'); console.log('html/css', a.css===b.css?'igual':'DIFERENTE');
