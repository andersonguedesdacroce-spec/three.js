const { chromium } = require('playwright'); const { spawn } = require('child_process'); const path=require('path');
(async()=>{const fps=30, fim=88.5;
 const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1920,height:1080}});
 await pg.goto('file://'+path.resolve(__dirname,'aula.html')); await pg.evaluate(()=>document.fonts.ready);
 const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(fps),'-c:v','mjpeg','-i','-','-i','voz.mp3','-c:v','libx264','-pix_fmt','yuv420p','-crf','19','-preset','veryfast','-c:a','aac','-b:a','160k','-af','apad','-t',String(fim),'-movflags','+faststart','aula-fable.mp4'],{stdio:['pipe','inherit','inherit'],cwd:__dirname});
 const n=Math.round(fim*fps);
 for(let k=0;k<n;k++){ await pg.evaluate(t=>frame(t), k/fps); const buf=await pg.screenshot({type:'jpeg',quality:92}); if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); }
 ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('ok',n);})();
