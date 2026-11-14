"""Ajudas para os postos de Matemática: formatação pt-BR e conferência do gabarito com Fraction."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'gerador'))
from aulas import *
from fractions import Fraction as Fr
from decimal import Decimal

def s(x):
    """Fração ou inteiro em texto: 3/4, 5."""
    x = Fr(x); return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
def dc(x, casas=None):
    """Decimal finito com vírgula: 0,75. Aceita Fraction, int, float, str."""
    x = Fr(str(x)) if not isinstance(x, Fr) else x
    den = x.denominator
    while den % 2 == 0: den //= 2
    while den % 5 == 0: den //= 5
    assert den == 1, f"{x} não é decimal finito"
    t = format(Decimal(x.numerator) / Decimal(x.denominator), 'f')
    if '.' in t: t = t.rstrip('0').rstrip('.')
    if casas is not None: t = format(Decimal(t), f'.{casas}f')
    return t.replace('.', ',')
def rs(x):
    """Dinheiro: R$ 1.234,50"""
    t = f"{Fr(str(x)):.2f}" if False else format(Decimal(Fr(str(x)).numerator)/Decimal(Fr(str(x)).denominator), '.2f')
    i, f = t.split('.'); i = f"{int(i):,}".replace(',', '.'); return f"R$ {i},{f}"
def misto(x):
    x = Fr(x); i, r = divmod(x.numerator, x.denominator)
    return f"{i} {r}/{x.denominator}" if r and i else (s(x))

Q = []
def q(n, e, a, c, tx=None):
    assert len(a) == 5 and len(set(a)) == 5, (e, a)
    Q.append((n, e, a, c, tx))
def fechar():
    """Ordena por nível (fáceis, médias, difíceis), mantendo a ordem de escrita dentro de cada nível."""
    global Q
    Q = sorted(Q, key=lambda t: t[0]); return Q
