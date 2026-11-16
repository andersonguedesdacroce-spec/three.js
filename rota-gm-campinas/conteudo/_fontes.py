"""Verificador de citações: cada [[LEI|...]] precisa existir literalmente no texto-fonte guardado em fontes/."""
import os, re
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
def _norm(s): return re.sub(r'\s+', ' ', s).strip()
_cache = {}
def fonte(nome):
    if nome not in _cache: _cache[nome] = _norm(open(os.path.join(RAIZ, 'fontes', nome), encoding='utf-8').read())
    return _cache[nome]
def LEI(ref, texto, nome):
    """Devolve o marcador [[LEI|ref|texto]] depois de conferir o texto no arquivo-fonte."""
    assert _norm(texto) in fonte(nome), f'Citação não encontrada na fonte ({ref}): {texto[:80]}'
    return f'[[LEI|{ref}|{texto}]]'

def span(nome, ini, fim=None):
    """Trecho literal do texto-fonte, de `ini` (inclusive) até `fim` (exclusive; None = só `ini`)."""
    t = fonte(nome)
    i = t.find(_norm(ini)); assert i >= 0, f'início não encontrado: {ini[:60]}'
    if fim is None: return _norm(ini)
    j = t.find(_norm(fim), i + len(_norm(ini))); assert j >= 0, f'fim não encontrado: {fim[:60]}'
    return t[i:j].strip()
def LEIS(ref, nome, ini, fim=None):
    """[[LEI|ref|trecho]] copiado do texto-fonte (nunca digitado à mão)."""
    txt = re.sub(r'^Art\. \d+(?:-[A-Z])?º?\.?\s*', '', span(nome, ini, fim))   # o número do artigo já vai na referência
    return f'[[LEI|{ref}|{txt}]]'
