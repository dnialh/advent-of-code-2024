import requests
from secret import session

from functools import cache
from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

dI = {'v' : 1, '^': -1, '<': 0, '>': 0}
dJ = {'v' : 0, '^': 0, '<': -1, '>': 1}

dX = [0, 1, 0, -1]
dY = [1, 0, -1, 0]
#v>^<


DAY = 23
def getday(n):
    return requests.get(f"https://adventofcode.com/2024/day/{n}/input",cookies={'session':session}).text

def med(a,b,c):
    return a + b + c - min(a,b,c) - max(a,b,c)

def sgn(x):
    if x == 0:
        return 0

    return abs(x)//x

def cout(x):
    print(x)
    print('\n\n')
    
s_samp = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
'''

s_real = getday(DAY)

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    board = ll
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])

    seen = set()

    adj = DD(set)
    for line in ll:
        u, v = line.split('-')
        adj[u].add(v)
        adj[v].add(u)

    for u in adj:
        if u[0] != 't':
            continue
        
        for v in adj[u]:
            for w in adj[u]:
                if v in adj[w]:
                    seen.add(tuple(sorted([u, v, w])))

    print(len(seen))


    people = adj.keys()

    def clique(l, f):
        #print(l, f)
        
        ll = []
        for u in l:
            if all (v in adj[u] for v in f):
                ll.append(u)

        if ll == []:
            return f

        best = []
        while ll:
            u = ll.pop()
            rec = clique(ll, f + [u])
            if len(rec) > len(best):
                best = rec

        #print(len(best))
        return best

    x = sorted(clique(people, []))
    print(','.join(x))

