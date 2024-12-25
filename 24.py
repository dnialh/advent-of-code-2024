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


DAY = 24
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
    
s_samp = '''
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
'''

s_samp2 = '''
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00'''

s_real = getday(DAY)

import random

def get(u):
    if u < 10:
        return '0' + str(u)
    return str(u)

def simul(x, y):
    z = x + y
    
    wrong = []

    known = {}
    for i in range(SZ):
        known['x' + get(i)] = 1 & (x >> i)
        known['y' + get(i)] = 1 & (y >> i)

    ops = baseops[:]
    while ops:
        nex = []
        for a, o, c, r in ops:
            if a in known and c in known:
                if o == 'XOR':
                    known[r] = known[a] ^ known[c]
                elif o == 'AND':
                    known[r] = known[a] & known[c]
                elif o == 'OR':
                    known[r] = known[a] | known[c]
                else:
                    assert 0
            else:
                nex.append((a, o, c, r))

        assert len(nex) < len(ops)
        ops = nex

    c6 = set()
    for s in known:
        if known[s] == 1 & (z >> 6):
            c6.add(s)
    
    for i in range(SZ + 1):
        if known['z' + get(i)] != 1 & (z >> i):
            wrong.append(i)

    return wrong, c6
    
    

for s in [s_real]:
    s = s.strip()
    ll = s.split('\n')
    board = ll
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    SZ = 0
    m = len(ll[0])

    known = {}
    imp = {}
    rev = {}
    sz = {}

    swap = {'z06': 'ksv', 'ksv': 'z06'}

    def asw(x, y):
        swap[x] = y
        swap[y] = x

    asw('kbs', 'nbd')
    #jwh = carry 9
    #hfc = carry 19
    asw('tqq', 'z20')
    asw('ckb', 'z39')
    
    ops = []
    for line in ll:
        if ':' in line:
            l, r = line.split(':')
            known[l] = int(r)
            imp[l] = set([l])
            sz[l] = 1
            if l[0] == 'x':
                SZ += 1
                
            continue

        if line.strip() == '':
            continue

        assert '->' in line

        l, r = line.split('->')
        r = r.strip()

        if r in swap:
            r = swap[r]
        
        a, o, c = l.split()

        ops.append((a, o, c, r))
        rev[r] = l

    baseops = ops[:]

    x = 0
    
    while ops:
        nex = []
        for a, o, c, r in ops:
            x += 1
            if a in known and c in known:
                if o == 'XOR':
                    known[r] = known[a] ^ known[c]
                elif o == 'AND':
                    known[r] = known[a] & known[c]
                elif o == 'OR':
                    known[r] = known[a] | known[c]
                else:
                    assert 0

                imp[r] = imp[a] | imp[c]
                imp[r].add(r)
                sz[r] = sz[a] + sz[c] + 1
            else:
                nex.append((a, o, c, r))

        assert len(nex) < len(ops)
        ops = nex

    out = 0
    for s in known:
        if s[0] == 'z':
            out += known[s] << (int(s[1:]))

    for j in range(SZ):
        assert ('x' + get(j)) in imp['z' + get(j)]
        assert ('y' + get(j)) in imp['z' + get(j)]

        assert ('x' + get(j + 1)) not in imp['z' + get(j)]
        assert ('y' + get(j + 1)) not in imp['z' + get(j)]

    #print(x)
    cout(out)

    c6a = set(known.keys())
    wrong = set()
    for i in range(100):
        x = random.randint(0, (1 << SZ) - 1)
        y = random.randint(0, (1 << SZ) - 1)

        ww, c6 = simul(x, y)

        wrong |= set(ww)
        c6a &= c6

    print(wrong)
    # print(c6a)
    print(','.join(sorted(swap.keys())))
