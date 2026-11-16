#!/bin/bash
# Uso: motor/produzir.sh <posto> "<url do mp3>"   (rodar dentro de videos/)
set -e
P=$1; D=fonte/$P
[ -n "$2" ] && curl -sS -f -o $D/voz.mp3 "$2"
python3 motor/alinhar.py $D
node motor/gerar.cjs $D
cp $D/video.mp4 $P.mp4
ffmpeg -v error -y -ss 4 -i $P.mp4 -frames:v 1 -vf scale=1280:-1 -q:v 4 $P.jpg
python3 - "$P" <<'PY'
import json,sys,subprocess
p=sys.argv[1]; r=json.load(open(f'fonte/{p}/roteiro.json',encoding='utf-8'))
d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{p}.mp4'],capture_output=True,text=True).stdout)
v=json.load(open('videos.json',encoding='utf-8'))
v[p]={"titulo":r['titulo'],"duracao":f"{int(d//60)}min{int(d%60):02d}","arquivo":f"{p}.mp4","capa":f"{p}.jpg"}
json.dump(v,open('videos.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(p,v[p]['duracao'])
PY
rm -f $D/foto-*.jpg $D/m?.jpg $D/video.mp4
