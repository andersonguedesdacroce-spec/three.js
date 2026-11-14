#!/usr/bin/env python3
"""Junta src/, aulas/, bancos/ e textos/ em public/index.html (arquivo único, pronto para o Vercel).
Uso: python3 build.py [--sem-validar]"""
import re, json, sys, glob, os, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__))
def ler(p): return open(os.path.join(AQUI, p), encoding='utf-8', newline='').read()

edital = ler('src/edital.js')
trilhas = re.findall(r'\{id:"([a-z]+)"', edital)           # ordem das trilhas no painel
def chave(pid): t, n = pid.rsplit('-', 1); return (trilhas.index(t) if t in trilhas else 99, int(n))
def ids(pasta, ext): return sorted((os.path.basename(f)[:-len(ext)] for f in glob.glob(f'{AQUI}/{pasta}/*{ext}')), key=chave)

PREFIXOS = json.load(open(os.path.join(AQUI, 'prefixos.json')))
aulas = ids('aulas', '.html')
bancos = ids('bancos', '.js')
textos = {}
for f in sorted(glob.glob(f'{AQUI}/textos/*.json')):
    for k, v in json.load(open(f, encoding='utf-8')).items():
        assert k not in textos, f'texto de apoio repetido: {k} ({os.path.basename(f)})'
        textos[k] = v

def validar():
    erros = []; vistos = {}
    for pid in bancos:
        js = ler(f'bancos/{pid}.js')
        # avalia o arquivo com node para ter os objetos reais
        out = subprocess.run(['node', '-e', 'const BANCO={};' + js.replace('\\', '\\\\').replace('`', '\\`') if False else 'const fs=require("fs");const BANCO={};eval(fs.readFileSync(process.argv[1],"utf8"));console.log(JSON.stringify(BANCO))', os.path.join(AQUI, 'bancos', pid + '.js')], capture_output=True, text=True)
        if out.returncode: erros.append(f'{pid}: erro de sintaxe: {out.stderr[:200]}'); continue
        Q = json.loads(out.stdout)[pid]
        if len(Q) != 60: erros.append(f'{pid}: {len(Q)} questões (esperado 60)')
        c = {n: sum(1 for q in Q if q['n'] == n) for n in (1, 2, 3)}
        if c != {1: 20, 2: 20, 3: 20}: erros.append(f'{pid}: níveis {c}')
        for q in Q:
            if q['id'] in vistos: erros.append(f'id repetido {q["id"]} ({pid} e {vistos[q["id"]]})')
            vistos[q['id']] = pid
            if len(q['a']) != 5 or len(set(q['a'])) != 5: erros.append(f'{q["id"]}: precisa de 5 alternativas distintas')
            if not q.get('c'): erros.append(f'{q["id"]}: sem comentário')
            if q.get('tx') and q['tx'] not in textos: erros.append(f'{q["id"]}: texto de apoio inexistente ({q["tx"]})')
        pref = PREFIXOS[pid.rsplit('-', 1)[0]] + pid.rsplit('-', 1)[1] + '-'
        for q in Q:
            if not q['id'].startswith(pref): erros.append(f'{q["id"]}: prefixo esperado {pref}')
    for pid in aulas:
        if pid not in bancos: erros.append(f'{pid}: aula sem banco')
    for pid in bancos:
        if pid not in aulas: erros.append(f'{pid}: banco sem aula')
    return erros

if '--sem-validar' not in sys.argv:
    e = validar()
    if e: print('\n'.join(e)); sys.exit(1)

partes = [ler('src/base.html'), edital.rstrip('\n') + '\n\n/* ---------- Conteúdo pronto ---------- */\nconst AULAS = {\n']
DESTAQUES = json.load(open(os.path.join(AQUI, 'destaques', 'destaques.json'), encoding='utf-8')) if os.path.exists(os.path.join(AQUI, 'destaques', 'destaques.json')) else {}
def conferir_citacoes(pid, h):
    for m in re.finditer(r'<blockquote class="lei"><p>(.*?)</p><cite>(.*?)</cite>', h, re.S):
        assert len(m.group(1)) < 6000, f'{pid}: citação de lei longa demais ({len(m.group(1))} caracteres) em "{m.group(2)}"; o trecho copiado provavelmente começou no artigo errado'
    return h
def com_destaques(pid, h):
    """Insere as caixas Cai muito / Cuidado / Macete no fim da seção indicada (antes do próximo <h3>)."""
    for sec, tipo, txt in DESTAQUES.get(pid, []):
        m = re.search(r'<h3>' + str(sec) + r'\. ', h)
        assert m, f'{pid}: seção {sec} não encontrada para destaque'
        prox = h.find('<h3>', m.end())
        assert prox > 0, f'{pid}: seção {sec} sem seção seguinte'
        corpo = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', txt)
        bloco = f'<blockquote class="dq"><p><strong>{tipo}</strong> {corpo}</p></blockquote>\n\n'
        h = h[:prox] + bloco + h[prox:]
    return h
partes.append(',\n'.join(f'"{p}": `\n' + com_destaques(p, conferir_citacoes(p, ler(f'aulas/{p}.html'))) + '`' for p in aulas) + '\n};\n\n')
partes.append('const BANCO = {};\n\n')
for p in bancos: partes.append(ler(f'bancos/{p}.js').rstrip('\n') + '\n\n')
partes.append('/* ---------- Textos de apoio das questões ---------- */\nconst TEXTOS = {\n' + ',\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in textos.items()) + '\n};\n\n')
import shutil
VIDEOS = json.load(open(os.path.join(AQUI, 'videos', 'videos.json'), encoding='utf-8'))
os.makedirs(f'{AQUI}/public/videos', exist_ok=True)
for pid, v in VIDEOS.items():
    assert pid in aulas, f'vídeo de posto inexistente: {pid}'
    for k in ('arquivo', 'capa'): shutil.copyfile(f'{AQUI}/videos/{v[k]}', f'{AQUI}/public/videos/{v[k]}')
partes.append('const VIDEOS = ' + json.dumps(VIDEOS, ensure_ascii=False) + ';\n\n')
partes.append(ler('src/config.js') + '\n')
partes.append(ler('src/app.js'))
html = ''.join(partes)
os.makedirs(f'{AQUI}/public', exist_ok=True)
open(f'{AQUI}/public/index.html', 'w', encoding='utf-8', newline='').write(html)
print(f'public/index.html: {len(html):,} bytes; {len(aulas)} aulas, {len(bancos)} bancos, {len(textos)} textos')
