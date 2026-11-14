#!/usr/bin/env python3
"""Baixa o texto consolidado de uma lei (Legin da Câmara) e salva limpo em fontes/<nome>.txt.
Uso: python3 ferramentas/baixar_lei.py <url> <nome> "<descrição da norma>"
Remove as notas de alteração entre parênteses, mantendo [revogado] onde o dispositivo foi revogado."""
import sys, re, html, os, subprocess, datetime
url, nome, desc = sys.argv[1:4]
raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
bruto = subprocess.run(['curl', '-sS', '-m', '90', '-L', url], capture_output=True).stdout.decode('utf-8', 'ignore')
assert len(bruto) > 20000, 'download vazio ou incompleto'
t = re.sub(r'<script.*?</script>|<style.*?</style>', '', bruto, flags=re.S)
t = re.sub(r'<br\s*/?>|</p>|</div>|</tr>', '\n', t)
t = html.unescape(re.sub(r'<[^>]+>', '', t))
t = re.sub(r'\s*\n\s*', ' ', t)
INICIOS = ('Pena', 'Atualização', 'Redação', 'Inciso', 'Alínea', 'Parágrafo', 'Item', 'Nome jurídico', 'Artigo', 'Capítulo', 'Seção', 'Título', 'Expressão', 'Vide', 'Vigência', 'Revogad', '“Caput”', '"Caput"', 'Declarad', 'Texto', 'Incluíd', 'Alterad', 'Suprimid', 'Renumerad', 'Revigorad', 'Regulamento', 'Promulgação', 'Legislação', 'Epígrafe', 'Subseção', 'Rubrica', 'Designação', 'Denominação', 'Parte', 'Livro', 'Veto', 'Disposição', 'Dispositivo', 'Número', 'Nota', 'Alteração', 'Convertid', 'Mensagem', 'Medida Provisória', 'Lei nº', 'Decreto', 'Emenda', 'Ato', 'Retificad', 'Prorrogad', 'Adicionad', 'Reformulad', 'Prazo', 'Efeitos', 'Eficácia', 'Em vigor', 'Cf.', 'Ver ')
def limpa(t):
    out = []; i = 0
    while i < len(t):
        if t[i] == '(' and t.startswith(INICIOS, i + 1):
            j = t.find(')', i)
            m0 = re.search(r'\s(?=§ \d|Art\. \d|Parágrafo único)', t[i:j if j >= 0 else len(t)])
            if m0 and j >= 0: j = i + m0.start() - 1
            if j < 0 or j - i > 500:   # nota sem fecha-parêntese no HTML de origem: corta antes do próximo dispositivo
                m = re.search(r'\s(?=§ |Art\. |Parágrafo único|[IVX]+ - |Pena - )', t[i:])
                j = i + (m.start() if m else 0) - 1
            while j + 1 < len(t) and t[j + 1] == ')': j += 1   # sobra de parêntese aninhado
            nota = t[i:j + 1]
            if re.search(r'vetad', nota, re.I) and not re.search(r'redação dada', nota, re.I):
                out.append('[VETADO: o dispositivo anterior não está em vigor]'); i = j + 1; continue
            out.append('[revogado]' if re.search(r'revogad', nota, re.I) and not re.search(r'redação dada', nota, re.I) else '')
            i = j + 1
        else:
            out.append(t[i]); i += 1
    return ''.join(out)
t = limpa(t)
t = t.replace('[revogado] [revogado]', '[revogado]')
t = re.sub(r'\s+', ' ', t).strip()
cab = f"FONTE: {desc}, texto consolidado da Câmara dos Deputados (Legin, normaatualizada), baixado de {url} em {datetime.date.today()}. Notas de alteração removidas; [revogado] marca dispositivos revogados.\n\n"
open(os.path.join(raiz, 'fontes', nome + '.txt'), 'w', encoding='utf-8').write(cab + t + '\n')
print(nome, len(t), 'caracteres')
