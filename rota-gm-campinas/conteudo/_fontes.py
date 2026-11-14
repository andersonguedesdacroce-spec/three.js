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
