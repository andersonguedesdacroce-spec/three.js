import json
TITLE="O verbo diz quando e como; o advérbio, em que circunstância"
boxes=[ # (slug, x, y, w, name, lines, tag)
 ("modos",40,96,216,"Modos",["indicativo: certeza","subjuntivo: hipótese","imperativo: ordem"],"seções 2, 4 e 5"),
 ("tempos",272,96,216,"Tempos",["perfeito: concluído","imperfeito: hábito","teria fugido: não confirmado"],"seções 3 e 4"),
 ("vozes",40,216,216,"Vozes",["ativa: o guarda deteve","passiva: foi detido","sintética: detiveram-se"],"seção 7"),
 ("formas",272,216,216,"Formas e impessoais",["particípio: foi preso","gerúndio: chegou correndo","houve, faz: no singular"],"seções 6 e 8"),
 ("circ",536,96,184,"Circunstâncias",["tempo, lugar, modo","intensidade, dúvida","afirmação, negação"],"seção 9"),
 ("expr",536,216,184,"Expressões",["por causa de: causa","apesar de: concessão","com: instrumento"],"seção 9"),
]
conts=[("verbo",24,48,480,"Verbo"),("adverbio",520,48,216,"Advérbio")]
H=104; VB=352
# ---- widget (Doc)
w=[]
w.append(f"<text data-claude-text-id='title' x='24' y='28' fontSize='15' fontWeight='600' fill={{ink}}>{TITLE}</text>")
for slug,x,y,wd,name in conts:
    w.append(f"<g data-claude-anchor='{slug}'><rect x='{x}' y='{y}' width='{wd}' height='288' rx='12' fill={{accent}} fillOpacity='0.08' stroke={{accent}} strokeWidth='2'/><text data-claude-text-id='{slug}-nome' x='{x+16}' y='{y+30}' fontSize='15' fontWeight='600' fill={{ink}}>{name}</text></g>")
for slug,x,y,wd,name,lines,tag in boxes:
    cx=x+wd//2
    g=f"<g data-claude-anchor='box-{slug}'><rect x='{x}' y='{y}' width='{wd}' height='{H}' rx='8' fill='var(--cds-surface-primary, none)' stroke={{edge}} strokeWidth='1.25'/>"
    g+=f"<text data-claude-text-id='{slug}-n' x='{cx}' y='{y+24}' textAnchor='middle' fontWeight='600' fill={{ink}}>{name}</text>"
    for k,l in enumerate(lines):
        g+=f"<text data-claude-text-id='{slug}-l{k+1}' x='{cx}' y='{y+44+16*k}' textAnchor='middle' fontSize='12' fill={{ink}}>{l}</text>"
    g+=f"<text data-claude-text-id='{slug}-tag' x='{cx}' y='{y+94}' textAnchor='middle' fontSize='11.5' fill={{quiet}}>{tag}</text></g>"
    w.append(g)
code="export default () => { const edge = 'var(--cds-chart-axis)', accent = 'var(--cds-chart-categorical-1)', ink = 'var(--cds-text-primary)', quiet = 'var(--cds-text-secondary)'; return <svg viewBox='0 0 760 %d' role='img' aria-label='%s' fontSize='13'>%s</svg>; };"%(VB,TITLE,''.join(w))
open('widget.js','w').write(code)
# ---- painel SVG
s=[f'<svg viewBox="0 0 760 {VB}" role="img" aria-label="{TITLE}" font-size="13">',f'<text x="24" y="28" font-size="16" font-weight="600">{TITLE}</text>']
for slug,x,y,wd,name in conts:
    s.append(f'<rect class="ac" x="{x}" y="{y}" width="{wd}" height="288" rx="12"/><text x="{x+16}" y="{y+30}" font-size="16" font-weight="600">{name}</text>')
for slug,x,y,wd,name,lines,tag in boxes:
    cx=x+wd//2
    s.append(f'<rect x="{x}" y="{y}" width="{wd}" height="{H}" rx="8" style="fill:var(--surface);stroke:var(--muted);stroke-width:1.25"/>')
    s.append(f'<text x="{cx}" y="{y+24}" text-anchor="middle" font-weight="600">{name}</text>')
    for k,l in enumerate(lines): s.append(f'<text x="{cx}" y="{y+44+16*k}" text-anchor="middle" font-size="12">{l}</text>')
    s.append(f'<text class="q" x="{cx}" y="{y+94}" text-anchor="middle" font-size="12">{tag}</text>')
s.append('</svg>')
open('mapa.svg','w').write('\n'.join(s))
print(code)
