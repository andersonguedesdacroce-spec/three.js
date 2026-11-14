import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'gerador'))
from aulas import *
from _fontes import LEI, LEIS
F='geo.txt'
def C(ref,txt): return LEI(ref,txt,F)
def S_(ref,a,b): return LEIS(ref,F,a,b)
class B:
    def __init__(s): s.Q=[]
    def q(s,n,e,a,c,tx=None):
        assert len(a)==5 and len(set(a))==5,(e,a); s.Q.append((n,e,a,c,tx))
    def fim(s):
        from collections import Counter; c=Counter(x[0] for x in s.Q); print(c); assert c=={1:20,2:20,3:20},c
