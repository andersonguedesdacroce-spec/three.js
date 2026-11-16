// Uso: node gerar.cjs <pasta do vídeo> [fotos t1,t2,...]   Gera <pasta>/video.mp4 (ou só fotos de conferência)
const { chromium } = require('playwright'); const { spawn } = require('child_process'); const path=require('path'), fs=require('fs');
(async()=>{ const pasta=path.resolve(process.argv[2]); const fotos=process.argv[3];
 const R=JSON.parse(fs.readFileSync(pasta+'/roteiro.json','utf8')), T=JSON.parse(fs.readFileSync(pasta+'/tempos.json','utf8'));
 const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1920,height:1080}});
 pg.on('pageerror',e=>{console.log('ERRO',e.message);});
 await pg.goto('file://'+path.resolve(__dirname,'player.html')); await pg.evaluate(()=>document.fonts.ready);
 await pg.evaluate(([r,t])=>montar(r,t),[R,T]);
 const fim=T.dur+2.6, fps=30;
 if(fotos){ const ts = fotos==='auto' ? T.cenas.map((c,i)=>(T.cenas[i+1]?T.cenas[i+1].ini:T.dur)-0.6) : fotos.split(',').map(Number);
   let k=0; for(const t of ts){ await pg.evaluate(t=>frame(t),t); await pg.screenshot({path:`${pasta}/foto-${String(k++).padStart(2,'0')}.jpg`,type:'jpeg',quality:60}); } await b.close(); console.log('fotos',ts.length); return; }
 const temVoz=fs.existsSync(pasta+'/voz.mp3');
 const args=['-y','-loglevel','error','-f','image2pipe','-framerate',String(fps),'-c:v','mjpeg','-i','-'].concat(temVoz?['-i',pasta+'/voz.mp3']:[]).concat(['-c:v','libx264','-pix_fmt','yuv420p','-crf','21','-preset','veryfast']).concat(temVoz?['-c:a','aac','-b:a','128k','-af','apad']:[]).concat(['-t',String(fim),'-movflags','+faststart',pasta+'/video.mp4']);
 const ff=spawn('ffmpeg',args,{stdio:['pipe','inherit','inherit']}); const n=Math.round(fim*fps);
 for(let k=0;k<n;k++){ await pg.evaluate(t=>frame(t),k/fps); const buf=await pg.screenshot({type:'jpeg',quality:90}); if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); }
 ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('ok',n,'quadros');
})();
