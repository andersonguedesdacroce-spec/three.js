import re, markdown, json
exec(open('secoes.py').read())
def md(t):
    h=markdown.markdown(t, extensions=['tables'])
    h=h.replace('<h3>','<h4>').replace('</h3>','</h4>').replace('<h2>','<h3>').replace('</h2>','</h3>')
    h=re.sub(r'<table>(.*?)</table>', lambda m:'<div class="tabela"><table>'+m.group(1)+'</table></div>', h, flags=re.S)
    return h
pos={0:2,1:1,2:3,3:4}  # índice da correta
qr_html='<h3>10. Questões resolvidas</h3>\n'; qr_md='## 10. Questões resolvidas\n\n'
for i,(tit,e,alts,_,com) in enumerate(QR):
    certa=alts[0]; outras=alts[1:]; p=pos[i]
    ordem=outras[:p]+[certa]+outras[p:]
    L="ABCDE"[p]
    # ajustar letras citadas no comentário (B)/(C)/(D) se houver
    com2=com
    if i==1: com2="Apreendeu (pretérito perfeito) vira foram apreendidas: ser no mesmo tempo e particípio concordando com “motos”. As alternativas com eram e serão mudam o tempo; a com “apreendido” não concorda."
    qr_html+=f'<h4>{tit}</h4>\n<p>{e}</p>\n<ol class="alts" type="A">'+''.join(f'<li>{a}</li>' for a in ordem)+f'</ol>\n<p><strong>Resposta: {L}.</strong> {com2}</p>\n'
    qr_md+=f'### {tit}\n\n{e}\n\n'+''.join(f'- ({"ABCDE"[k]}) {a}\n' for k,a in enumerate(ordem))+f'\n**Resposta: {L}.** {com2}\n\n'
open('qr_doc.md','w').write(qr_md.strip())
svg=open('mapa.svg').read()
H='\n<span class="status">Versão 1 · em revisão</span>\n<p>'+LEAD+'</p>\n\n<h3>Mapa do assunto</h3>\n<figure class="fig">\n'+svg+'\n<figcaption>O verbo situa o fato no tempo e diz como ele é apresentado (certo, hipotético, ordenado, sofrido); o advérbio acrescenta a circunstância.</figcaption>\n</figure>\n'
for k in range(1,10): H+=md(S[k])+'\n'
H+=qr_html
for k in (11,12,13): H+=md(S[k])+'\n'
H+='<p class="ref">Fontes: Edital 02/2026, Anexo I. Referências de base: Bechara, <em>Moderna Gramática Portuguesa</em>; Cunha e Cintra, <em>Nova Gramática do Português Contemporâneo</em>; ABL, VOLP. Exemplos criados para a aula.</p>\n'
assert '`' not in H and '${' not in H
open('aula.html','w').write(H)
print(len(H)); print(qr_md[:600])
