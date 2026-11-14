// Teste de fumaça no Chromium headless. Uso: node ferramentas/testar.cjs <index.html> [pasta-de-capturas] [postos,separados,por,vírgula]
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const arq = path.resolve(process.argv[2] || 'public/index.html');
const saida = process.argv[3] ? path.resolve(process.argv[3]) : null;
const postos = (process.argv[4] || 'pt-1,pt-7,gm-1').split(',');
if (saida) fs.mkdirSync(saida, { recursive: true });
(async () => {
  const browser = await chromium.launch();
  let falhas = 0; const erros = [];
  for (const [nome, vp] of [['celular', { width: 390, height: 844 }], ['desktop', { width: 1280, height: 800 }]]) {
    for (const tema of ['light', 'dark']) {
      const ctx = await browser.newContext({ viewport: vp, colorScheme: tema, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      page.on('console', m => { if (['error', 'warning'].includes(m.type())) erros.push(`[${nome}/${tema}] console.${m.type()}: ${m.text()}`); });
      page.on('pageerror', e => erros.push(`[${nome}/${tema}] pageerror: ${e.message}`));
      await page.addInitScript(() => { try { localStorage.setItem('rota-gm-campinas-v2', JSON.stringify({ acesso: true, aprovados: {}, tentativas: {}, vistas: {}, atualizado: 0 })); localStorage.setItem('rota-gm-tema', matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'); } catch (e) {} });
      await page.goto('file://' + arq);
      await page.evaluate(() => ir({ tela: 'painel' }));
      const tag = `${nome}-${tema}`;
      const verifica = async (ok, msg) => { if (!ok) { falhas++; console.log('FALHA', tag, msg); } };
      const larg = async (rot) => { const o = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth); await verifica(o <= 1, `${rot}: rolagem horizontal de ${o}px`); };
      const foto = async (n) => { if (saida) await page.screenshot({ path: `${saida}/${tag}-${n}.png`, fullPage: false }); };
      await foto('painel'); await larg('painel');
      for (const pid of postos) {
        await page.evaluate(id => ir({ tela: 'posto', posto: id, aba: 'aula' }), pid);
        await verifica(await page.locator('article.aula svg').count() > 0, `${pid}: aula sem mapa SVG`);
        await verifica(await page.locator('article.aula h3').count() >= 4, `${pid}: aula com poucas seções`);
        await verifica(await page.locator('article.aula p.ref').count() >= 1, `${pid}: sem linha de fontes`);
        await larg(`aula ${pid}`); await foto(`aula-${pid}`);
        await page.evaluate(id => ir({ tela: 'posto', posto: id, aba: 'questoes' }), pid);
        await page.click('#iniciar');
        await verifica(await page.locator('.alt, .alts button, button.alt, [data-alt]').count() >= 5 || await page.locator('#app button').count() >= 5, `${pid}: tela de questões sem alternativas`);
        await larg(`questões ${pid}`); await foto(`questoes-${pid}`);
        await page.evaluate(() => ir({ tela: 'painel' }));
      }
      await ctx.close();
    }
  }
  await browser.close();
  console.log(erros.length ? erros.join('\n') : 'console limpo (sem erros nem avisos)');
  console.log(falhas ? `${falhas} falha(s)` : 'todas as verificações passaram');
  process.exit(falhas || erros.length ? 1 : 0);
})();
