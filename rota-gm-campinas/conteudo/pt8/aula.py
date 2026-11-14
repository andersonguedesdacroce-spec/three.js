import re, markdown
exec(open('secoes.py').read())
def md(t):
    notas=[]
    def guarda(m): notas.append(m.group(1)); return f"\n\nNOTA{len(notas)-1}FIM\n\n"
    t=re.sub(r'\[\[NOTA: (.*?)\]\]', guarda, t, flags=re.S)
    h=markdown.markdown(t, extensions=['tables'])
    h=h.replace('<h3>','<h4>').replace('</h3>','</h4>').replace('<h2>','<h3>').replace('</h2>','</h3>')
    h=re.sub(r'<table>(.*?)</table>', lambda m:'<div class="tabela"><table>'+m.group(1)+'</table></div>', h, flags=re.S)
    for i,n in enumerate(notas):
        nh=markdown.markdown(n)[3:-4]
        h=h.replace(f'<p>NOTA{i}FIM</p>', f'<div class="box">{nh}</div>')
    return h
H='\n<span class="status">Versão 1 · em revisão</span>\n<p>'+LEAD+'</p>\n\n<h3>Mapa do assunto</h3>\n<figure class="fig">\n'+open('mapa.svg').read()+'\n<figcaption>As duas classes fazem o mesmo trabalho em escalas diferentes: ligar e dar sentido à ligação. A pergunta da prova é sempre qual sentido.</figcaption>\n</figure>\n'
for k in range(1,8): H+=md(S[k])+'\n'
H+='<h3>8. Questões resolvidas</h3>\n'
for tit,e,alts,pos,com in QR:
    certa=alts[0]; o=alts[1:]; ordem=o[:pos]+[certa]+o[pos:]
    H+=f'<h4>{tit}</h4>\n<p>{e}</p>\n<ol class="alts" type="A">'+''.join(f'<li>{a}</li>' for a in ordem)+f'</ol>\n<p><strong>Resposta: {"ABCDE"[pos]}.</strong> {com}</p>\n'
for k in (9,10,11): H+=md(S[k])+'\n'
H+='<p class="ref">Fontes: Edital 02/2026, Anexo I. Referências de base: Bechara, <em>Moderna Gramática Portuguesa</em>; Cunha e Cintra, <em>Nova Gramática do Português Contemporâneo</em>; ABL, VOLP. Exemplos criados para a aula.</p>\n'
assert '`' not in H and '${' not in H and 'NOTA' not in H
open('aula.html','w').write(H); print(len(H), H.count('class="box"'))
