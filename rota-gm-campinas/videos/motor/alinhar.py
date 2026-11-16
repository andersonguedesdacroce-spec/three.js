#!/usr/bin/env python3
"""Alinha a narração ao roteiro. Uso: alinhar.py <pasta do vídeo> [--estimar]
Lê roteiro.json (+ voz.mp3) e grava tempos.json e narracao.txt.
No texto de cada cena ("fala"): {1}, {s}, {p}... marcam o instante em que um elemento entra;
[[316|trezentos e dezesseis]] mostra "316" na legenda e manda "trezentos e dezesseis" para a voz."""
import json, re, subprocess, sys, os
pasta = sys.argv[1]; estimar = '--estimar' in sys.argv
R = json.load(open(f'{pasta}/roteiro.json', encoding='utf-8'))

def partes(fala):
    """devolve (texto falado, texto exibido, mapa falado->exibido, cues {chave: pos no falado})"""
    fal = ''; exi = ''; cues = {}; i = 0
    for m in re.finditer(r'\{(\w+)\}|\[\[(.*?)\|(.*?)\]\]', fala):
        t = fala[i:m.start()]; fal += t; exi += t
        if m.group(1): cues[m.group(1)] = len(fal)
        else: exi += m.group(2); fal += m.group(3)
        i = m.end()
    t = fala[i:]; fal += t; exi += t
    return fal, exi, cues

cenas = []; narr = []; pos = 0
for c in R['cenas']:
    fal, exi, cues = partes(c['fala'])
    cenas.append({'ini': pos, 'fim': pos + len(fal), 'fal': fal, 'exi': exi, 'cues': {k: pos + v for k, v in cues.items()}})
    narr.append(fal); pos += len(fal) + 2
texto = '\n\n'.join(narr)
open(f'{pasta}/narracao.txt', 'w', encoding='utf-8').write(texto)
print('narração:', len(texto), 'caracteres')

peso = [1 if ch.isalnum() else 0 for ch in texto]
acum = [0]
for p in peso: acum.append(acum[-1] + p)
total = acum[-1]
# limites de oração: depois de pontuação
lim = [m.end() for m in re.finditer(r'[,.;:?!]+(?=\s|$)', texto)]
if not lim or lim[-1] < len(texto.rstrip()): lim.append(len(texto))
lim = sorted(set(lim))

if estimar or not os.path.exists(f'{pasta}/voz.mp3'):
    dur = total / 13.5 + 0.35 * len(lim)
    ancoras = [(0, 0.3)]; t = 0.3
    ant = 0
    for l in lim:
        t += (acum[l] - acum[ant]) / 13.5; ancoras.append((l, t)); t += 0.35; ancoras.append((l + 0.001, t)); ant = l
    dur = t + 0.3
else:
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', f'{pasta}/voz.mp3', '-af', 'silencedetect=noise=-35dB:d=0.22', '-f', 'null', '-'], capture_output=True, text=True).stderr
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{pasta}/voz.mp3'], capture_output=True, text=True).stdout)
    ini = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]; fim = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
    sil = [(a, b) for a, b in zip(ini, fim + [dur] * (len(ini) - len(fim)))]
    t0 = 0.0; t1 = dur
    if sil and sil[0][0] < 0.15: t0 = sil[0][1]; sil = sil[1:]
    if sil and sil[-1][1] > dur - 0.15: t1 = sil[-1][0]; sil = sil[:-1]
    M = len(lim)
    while len(sil) + 1 > M: sil.remove(min(sil, key=lambda s: s[1] - s[0]))   # mais pausas que orações: tira as mais curtas
    segs = []; a = t0
    for s in sil: segs.append((a, s[0])); a = s[1]
    segs.append((a, t1)); n = len(segs)
    k = sum(b - a for a, b in segs) / total
    c = [acum[l] for l in lim]
    INF = 1e18
    custo = [[INF] * (M + 1) for _ in range(n + 1)]; de = [[0] * (M + 1) for _ in range(n + 1)]
    custo[0][0] = 0
    for j in range(1, n + 1):
        d = segs[j - 1][1] - segs[j - 1][0]
        for i in range(j, M - (n - j) + 1):
            best = INF; arg = 0
            for i2 in range(j - 1, i):
                if custo[j - 1][i2] >= INF: continue
                ch = c[i - 1] - (c[i2 - 1] if i2 else 0)
                v = custo[j - 1][i2] + (d - k * ch) ** 2
                if v < best: best = v; arg = i2
            custo[j][i] = best; de[j][i] = arg
    cortes = []; i = M
    for j in range(n, 0, -1): cortes.append(i); i = de[j][i]
    cortes = cortes[::-1]
    ancoras = [(0, segs[0][0])]
    for j, i in enumerate(cortes):
        ancoras.append((lim[i - 1], segs[j][1]))
        if j + 1 < n: ancoras.append((lim[i - 1] + 0.001, segs[j + 1][0]))
    print(f'duração {dur:.1f}s; {n} trechos de fala para {M} orações; erro médio {(custo[n][M] / n) ** .5:.2f}s')

def tempo(p):
    for (p0, t0_), (p1, t1_) in zip(ancoras, ancoras[1:]):
        if p0 <= p <= p1:
            if p1 - p0 < 0.01: return t0_
            w0 = acum[int(p0)]; w1 = acum[int(p1)]; w = acum[min(int(p), len(texto))]
            return t0_ + (t1_ - t0_) * ((w - w0) / (w1 - w0) if w1 > w0 else 0)
    return ancoras[-1][1]

saida = {'dur': round(dur, 2), 'cenas': [], 'legendas': []}
for c in cenas:
    saida['cenas'].append({'ini': round(tempo(c['ini']), 2), 'fim': round(tempo(c['fim']), 2), 'cues': {k: round(tempo(v), 2) for k, v in c['cues'].items()}})
    # legendas: por frase, com o texto exibido; frases longas são partidas nas vírgulas
    fal, exi = c['fal'], c['exi']
    fr_f = re.findall(r'[^.?!]+[.?!]+|\S[^.?!]*$', fal); fr_e = re.findall(r'[^.?!]+[.?!]+|\S[^.?!]*$', exi)
    if len(fr_f) != len(fr_e): fr_e = fr_f
    p = c['ini']
    for ff, fe in zip(fr_f, fr_e):
        a = p + (len(ff) - len(ff.lstrip())); b = p + len(ff.rstrip()); p += len(ff)
        pf = re.split(r'(?<=[,;:])\s', ff.strip()); pe = re.split(r'(?<=[,;:])\s', fe.strip())
        if len(fe.strip()) <= 64 or len(pf) != len(pe):
            saida['legendas'].append([round(tempo(a), 2), round(tempo(b), 2), fe.strip()]); continue
        # agrupa pedaços até ~60 caracteres
        q = a; grupo_f = ''; grupo_e = ''; ini_g = a
        for xf, xe in zip(pf, pe):
            if grupo_e and len(grupo_e) + len(xe) > 60:
                saida['legendas'].append([round(tempo(ini_g), 2), round(tempo(q), 2), grupo_e.strip()]); grupo_f = ''; grupo_e = ''; ini_g = q + 1
            grupo_f += xf + ' '; grupo_e += xe + ' '; q += len(xf) + 1
        if grupo_e: saida['legendas'].append([round(tempo(ini_g), 2), round(tempo(b), 2), grupo_e.strip()])
json.dump(saida, open(f'{pasta}/tempos.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('cenas:', [(x['ini'], x['fim']) for x in saida['cenas']])
