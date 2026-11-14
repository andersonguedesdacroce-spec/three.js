import re, json, markdown
import os
RAIZ=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
def _lei_html(m):
    ref,txt=m.group(1).strip(),m.group(2).strip()
    return '\n\n<blockquote class="lei"><p>'+txt+'</p><cite>'+ref+'</cite></blockquote>\n\n'
def md(t):
    t=re.sub(r'\[\[LEI\|(.*?)\|(.*?)\]\]', _lei_html, t, flags=re.S)
    notas=[]
    def g(m): notas.append(m.group(1)); return f"\n\nNOTA{len(notas)-1}FIM\n\n"
    t=re.sub(r'\[\[NOTA: (.*?)\]\]', g, t, flags=re.S)
    h=markdown.markdown(t, extensions=['tables'])
    h=h.replace('<h3>','<h4>').replace('</h3>','</h4>').replace('<h2>','<h3>').replace('</h2>','</h3>')
    h=re.sub(r'<table>(.*?)</table>', lambda m:'<div class="tabela"><table>'+m.group(1)+'</table></div>', h, flags=re.S)
    for i,n in enumerate(notas): h=h.replace(f'<p>NOTA{i}FIM</p>', f'<div class="box">{markdown.markdown(n)[3:-4]}</div>')
    return h
def doc_md(t):  # versão para o documento de revisão
    t=re.sub(r'\[\[LEI\|(.*?)\|(.*?)\]\]', lambda m:'> '+m.group(2).strip()+' *('+m.group(1).strip()+')*', t, flags=re.S)
    return re.sub(r'\[\[NOTA: (.*?)\]\]', lambda m:'> **Nota:** '+m.group(1), t, flags=re.S)
def mapa(title, boxes, band=None):
    """boxes: lista de (slug, nome, [l1,l2,l3], tag), 3 por linha"""
    xs=[24,268,512]; W=224; H=112
    rows=(len(boxes)+2)//3; yb=48+rows*128
    VB=(yb+44+20) if band else (yb+4)
    wd=[f"<text data-claude-text-id='title' x='24' y='28' fontSize='15' fontWeight='600' fill={{ink}}>{title}</text>"]
    sv=[f'<svg viewBox="0 0 760 {VB}" role="img" aria-label="{title}" font-size="13">',f'<text x="24" y="28" font-size="16" font-weight="600">{title}</text>']
    for k,(slug,nome,ls,tag) in enumerate(boxes):
        x=xs[k%3]; y=48+(k//3)*128; cx=x+W//2
        g=f"<g data-claude-anchor='{slug}'><rect x='{x}' y='{y}' width='{W}' height='{H}' rx='8' fill={{accent}} fillOpacity='0.08' stroke={{accent}} strokeWidth='1.5'/>"
        g+=f"<text data-claude-text-id='{slug}-n' x='{cx}' y='{y+26}' textAnchor='middle' fontWeight='600' fill={{ink}}>{nome}</text>"
        sv.append(f'<rect class="ac" x="{x}" y="{y}" width="{W}" height="{H}" rx="8" style="stroke-width:1.5"/><text x="{cx}" y="{y+26}" text-anchor="middle" font-weight="600">{nome}</text>')
        for j,l in enumerate(ls):
            g+=f"<text data-claude-text-id='{slug}-l{j+1}' x='{cx}' y='{y+48+16*j}' textAnchor='middle' fontSize='12' fill={{ink}}>{l}</text>"
            sv.append(f'<text x="{cx}" y="{y+48+16*j}" text-anchor="middle" font-size="12">{l}</text>')
        g+=f"<text data-claude-text-id='{slug}-tag' x='{cx}' y='{y+100}' textAnchor='middle' fontSize='11.5' fill={{quiet}}>{tag}</text></g>"
        sv.append(f'<text class="q" x="{cx}" y="{y+100}" text-anchor="middle" font-size="12">{tag}</text>')
        wd.append(g)
    if band:
        wd.append(f"<g data-claude-anchor='prova'><rect x='24' y='{yb}' width='712' height='44' rx='8' fill='var(--cds-chart-reference-tint)' stroke={{edge}} strokeWidth='1.25'/><text data-claude-text-id='prova' x='380' y='{yb+27}' textAnchor='middle' fontSize='13' fill={{ink}}>{band}</text></g>")
        sv.append(f'<rect class="tint" x="24" y="{yb}" width="712" height="44" rx="8"/><text x="380" y="{yb+27}" text-anchor="middle" font-size="13">{band}</text>')
    sv.append('</svg>')
    code="export default () => { const edge = 'var(--cds-chart-axis)', accent = 'var(--cds-chart-categorical-1)', ink = 'var(--cds-text-primary)', quiet = 'var(--cds-text-secondary)'; return <svg viewBox='0 0 760 %d' role='img' aria-label='%s' fontSize='13'>%s</svg>; };"%(VB,title,''.join(wd))
    return code,'\n'.join(sv)
ULTIMA={}
def aula(LEAD, S, ordem, QR, qr_num, svg, caption, fontes):
    ULTIMA.update(LEAD=LEAD,S=S,ordem=ordem,QR=QR,qr_num=qr_num,fontes=fontes)
    H='\n<span class="status">Versão 1 · em revisão</span>\n<p>'+LEAD+'</p>\n\n<h3>Mapa do assunto</h3>\n<figure class="fig">\n'+svg+f'\n<figcaption>{caption}</figcaption>\n</figure>\n'
    for k in ordem:
        if k=='QR':
            H+=f'<h3>{qr_num}. Questões resolvidas</h3>\n'
            for tit,e,alts,pos,com in QR:
                o=alts[1:]; ordem2=o[:pos]+[alts[0]]+o[pos:]
                H+=f'<h4>{tit}</h4>\n<p>{e}</p>\n<ol class="alts" type="A">'+''.join(f'<li>{a}</li>' for a in ordem2)+f'</ol>\n<p><strong>Resposta: {"ABCDE"[pos]}.</strong> {com}</p>\n'
        else: H+=md(S[k])+'\n'
    H+=f'<p class="ref">{fontes}</p>\n'
    assert '`' not in H and '${' not in H and 'NOTA' not in H
    return H
def qr_md(QR, qr_num):
    out=f'## {qr_num}. Questões resolvidas\n\n'
    for tit,e,alts,pos,com in QR:
        o=alts[1:]; ordem=o[:pos]+[alts[0]]+o[pos:]
        out+=f'### {tit}\n\n{e}\n\n'+''.join(f'- ({"ABCDE"[k]}) {a}\n' for k,a in enumerate(ordem))+f'\n**Resposta: {"ABCDE"[pos]}.** {com}\n\n'
    return out.strip()
def banco(pid, Q):
    from collections import Counter
    assert len(Q)==60, len(Q); c=Counter(x[0] for x in Q); assert c=={1:20,2:20,3:20}, c
    pre=('p' if pid.startswith('pt') else pid.split('-')[0][0])+pid.split('-')[1]
    L=[]
    for i,(n,e,a,cm,tx) in enumerate(Q,1):
        assert len(a)==5 and len(set(a))==5, e
        L.append('{id:"%s-%02d",n:%d,'%(pre,i,n)+('tx:"%s",'%tx if tx else '')+'e:%s,a:%s,c:%s}'%(json.dumps(e,ensure_ascii=False),json.dumps(a,ensure_ascii=False),json.dumps(cm,ensure_ascii=False)))
    return f'BANCO["{pid}"] = [\n'+',\n'.join(L)+'\n];'
def gravar(pid, aula_html, banco_js, textos=None):
    """Grava os arquivos do posto: aulas/<pid>.html, bancos/<pid>.js e textos/<pid>.json (textos de apoio novos).
    Depois rode `python3 build.py`, que valida e monta public/index.html."""
    def w(rel, txt): open(os.path.join(RAIZ, rel), 'w', encoding='utf-8', newline='').write(txt)
    w(f'aulas/{pid}.html', aula_html[1:] if aula_html.startswith('\n') else aula_html)
    w(f'bancos/{pid}.js', banco_js.rstrip('\n') + '\n')
    if textos: w(f'textos/{pid}.json', json.dumps(textos, ensure_ascii=False, indent=0) + '\n')

def revisao(pid, titulo, Q, textos=None, cobertura=None, pendencias=None, fontes_conferidas=None):
    """Grava revisao/<pid>.md: a aula em Markdown, as fontes, a cobertura e os pontos para revisão.
    Chame logo depois de aula(). `pendencias`: lista do que NÃO foi conferido na fonte."""
    from collections import Counter
    u=ULTIMA; c=Counter(x[0] for x in Q); com_tx=sum(1 for x in Q if x[4])
    o=[f'# Revisão do posto {pid}: {titulo}\n', '## Resumo\n',
       f'- Banco: {len(Q)} questões ({c[1]} fáceis, {c[2]} médias, {c[3]} difíceis); {com_tx} com texto de apoio'+(f' ({", ".join(textos)})' if textos else '')+'.',
       f'- Questões resolvidas na aula: {len(u["QR"])}.',
       f'- Seções: '+', '.join(f'{k}' for k in u['ordem'] if k!='QR')+f' (questões resolvidas na seção {u["qr_num"]}).\n',
       '## Fontes\n', u['fontes']+'\n']
    if fontes_conferidas: o+=['Conferidas nesta produção:\n']+['- '+f for f in fontes_conferidas]+['']
    o+=['## Verificação de cobertura\n']
    o+=['- '+x for x in (cobertura or ['Cobertura do recorte do edital não registrada para este posto.'])]
    o+=['','## Pontos para revisão (não conferidos na fonte)\n']
    o+=['- '+x for x in (pendencias or ['Nenhum ponto pendente registrado.'])]
    o+=['','## Aula\n','**'+u['LEAD']+'**\n']
    for k in u['ordem']:
        o.append(qr_md(u['QR'],u['qr_num']) if k=='QR' else doc_md(u['S'][k]).strip())
        o.append('')
    open(os.path.join(RAIZ,'revisao',f'{pid}.md'),'w',encoding='utf-8').write('\n'.join(o).strip()+'\n')
