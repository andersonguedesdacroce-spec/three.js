TITLE="A preposição liga termos; a conjunção liga orações"
# elementos: (tipo, id, x, y, texto, attrs)
T=[]  # textos: id,x,y,txt,size,weight,anchor,quiet
def t(i,x,y,s,size=13,w=None,anchor='middle',quiet=False): T.append((i,x,y,s,size,w,anchor,quiet))
t('title',24,28,TITLE,15,'600','start')
t('prep-nome',40,78,'Preposição',15,'600','start')
t('prep-def',40,102,'liga um termo a outro',12.5,None,'start',True)
t('prep-ex1',174,138,'a viatura da Guarda',13.5)
t('prep-ex2',174,160,'preso por furto',13.5)
t('prep-ex3',174,182,'ficou para preservar a cena',13.5)
t('prep-rel',174,212,'posse, causa, finalidade...',12)
t('prep-tag',174,234,'seções 1 a 3',11.5,quiet=True)
t('conj-nome',356,78,'Conjunção',15,'600','start')
t('conj-def',356,102,'liga orações',12.5,None,'start',True)
t('coord-n',443,140,'Coordenativas',13,'600')
t('coord-l1',443,160,'orações independentes',12)
t('coord-l2',443,176,'e, mas, ou',12)
t('coord-l3',443,192,'portanto, pois',12)
t('coord-tag',443,218,'seção 4',11.5,quiet=True)
t('sub-n',633,140,'Subordinativas',13,'600')
t('sub-l1',633,160,'uma depende da outra',12)
t('sub-l2',633,176,'porque, embora, se',12)
t('sub-l3',633,192,'conforme, quando',12)
t('sub-tag',633,218,'seções 5 e 6',11.5,quiet=True)
t('prova',380,291,'Na prova: que relação a palavra cria e por qual outra ela pode ser trocada (seções 6 e 7)',13)
VB=328
R=[('prep',24,48,300,200,'ac'),('conj',340,48,396,200,'ac'),('coord',356,116,174,116,'bx'),('sub',546,116,174,116,'bx'),('prova',24,264,712,44,'tint')]
# widget
def wtext(i,x,y,s,size,w,anchor,quiet):
    a=f"data-claude-text-id='{i}' x='{x}' y='{y}'"+(" textAnchor='middle'" if anchor=='middle' else '')+f" fontSize='{size}'"+(f" fontWeight='{w}'" if w else '')+(" fill={quiet}" if quiet else " fill={ink}")
    return f"<text {a}>{s}</text>"
g=[]
for nome,x,y,w,h,k in R:
    if k=='ac': rect=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='12' fill={{accent}} fillOpacity='0.08' stroke={{accent}} strokeWidth='2'/>"
    elif k=='bx': rect=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='none' stroke={{edge}} strokeWidth='1.25'/>"
    else: rect=f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='var(--cds-chart-reference-tint)' stroke={{edge}} strokeWidth='1.25'/>"
    mine=[tt for tt in T if tt[0].startswith(nome+'-') or (nome=='prova' and tt[0]=='prova') or (nome=='coord' and tt[0].startswith('coord')) or (nome=='sub' and tt[0].startswith('sub'))]
    g.append(f"<g data-claude-anchor='{nome}'>"+rect+''.join(wtext(*tt) for tt in mine)+"</g>")
code="export default () => { const edge = 'var(--cds-chart-axis)', accent = 'var(--cds-chart-categorical-1)', ink = 'var(--cds-text-primary)', quiet = 'var(--cds-text-secondary)'; return <svg viewBox='0 0 760 %d' role='img' aria-label='%s' fontSize='13'>%s%s</svg>; };"%(VB,TITLE,wtext(*T[0]),''.join(g))
open('widget.js','w').write(code)
# painel
s=[f'<svg viewBox="0 0 760 {VB}" role="img" aria-label="{TITLE}" font-size="13">']
for nome,x,y,w,h,k in R:
    if k=='bx': s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" style="fill:var(--surface);stroke:var(--muted);stroke-width:1.25"/>')
    else: s.append(f'<rect class="{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{12 if k=="ac" else 8}"/>')
for i,x,y,txt,size,w,anchor,quiet in T:
    s.append(f'<text x="{x}" y="{y}"'+(' text-anchor="middle"' if anchor=='middle' else '')+f' font-size="{size}"'+(f' font-weight="{w}"' if w else '')+(' class="q"' if quiet else '')+f'>{txt}</text>')
s.append('</svg>')
open('mapa.svg','w').write('\n'.join(s))
print(code)
