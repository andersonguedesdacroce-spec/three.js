"""Uso único: separa o index.html monolítico em src/, aulas/, bancos/ e textos/."""
import re, sys, os, json
orig, raiz = sys.argv[1], sys.argv[2]
L = open(orig, encoding='utf-8').read().split('\n')
def ln(n): return n-1  # linhas 1-based
def w(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline='').write(txt)
i_aulas = next(i for i,l in enumerate(L) if l.startswith('const AULAS = {'))
i_banco = next(i for i,l in enumerate(L) if l.startswith('const BANCO = {'))
i_textos = next(i for i,l in enumerate(L) if l.startswith('const TEXTOS = {'))
i_ind = next(i for i,l in enumerate(L) if l.startswith('/* ---------- Índices'))
# 1) base (HTML+CSS até <script>) e edital (constantes+TRILHAS), app (da seção Índices ao fim)
i_script = next(i for i,l in enumerate(L) if l.strip()=='<script>')
i_cont = next(i for i,l in enumerate(L) if l.startswith('/* ---------- Conteúdo pronto'))
w(f'{raiz}/src/base.html', '\n'.join(L[:i_script+1])+'\n')
w(f'{raiz}/src/edital.js', '\n'.join(L[i_script+1:i_cont]).rstrip('\n')+'\n')
w(f'{raiz}/src/app.js', '\n'.join(L[i_ind:]))
# 2) aulas
i=i_aulas+1
while not L[i].startswith('};'):
    m = re.match(r'^"([a-z]+-\d+)": `$', L[i]); assert m, (i, L[i][:60])
    j=i+1
    while not (L[j].endswith('`,') or L[j].endswith('`')): j+=1
    fim = L[j][:-2] if L[j].endswith('`,') else L[j][:-1]
    corpo = L[i+1:j]+[fim]            # a última linha pode trazer conteúdo antes do acento grave
    w(f'{raiz}/aulas/{m.group(1)}.html', '\n'.join(corpo))
    i=j+1
# 3) bancos gm-* (dentro do objeto) e pt-* (atribuições)
i=i_banco+1
while not L[i].startswith('};'):
    m = re.match(r'^"([a-z]+-\d+)": \[$', L[i]); assert m, L[i][:60]
    j=i+1
    while not L[j].startswith(']'): j+=1
    w(f'{raiz}/bancos/{m.group(1)}.js', f'BANCO["{m.group(1)}"] = [\n'+'\n'.join(L[i+1:j])+'\n];\n')
    i=j+1
for k in range(i_textos, i_ind):
    m = re.match(r'^BANCO\["([a-z]+-\d+)"\] = \[$', L[k])
    if m:
        j=k+1
        while not L[j].startswith('];'): j+=1
        w(f'{raiz}/bancos/{m.group(1)}.js', '\n'.join(L[k:j+1])+'\n')
# 4) textos: um arquivo JSON por chave (agrupado por posto no futuro); aqui, um único textos/_base.json
i=i_textos+1; T={}
while not L[i].startswith('};'):
    m = re.match(r'^([a-z0-9]+): (".*"),?$', L[i]); assert m, L[i][:60]
    T[m.group(1)] = json.loads(m.group(2)); i+=1
w(f'{raiz}/textos/base.json', json.dumps(T, ensure_ascii=False, indent=0).replace('\n','\n')+'\n')
print(len(T), 'textos')
