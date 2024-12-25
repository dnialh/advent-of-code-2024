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


DAY = 22
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
1
2
3
2024
'''

s_real = getday(DAY)

MOD = 16777216

def f(x):
    x ^= (x << 6)
    x %= MOD

    x ^= (x >> 5)

    x ^= (x << 11)
    x %= MOD

    return x
    

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

    dd = DD(int)

    out = 0
    for xx in ll:

        seen = set()
        x = int(xx)
        last = [x % 10]
        for _ in range(2000):
            x = f(x)
            last.append(x % 10)

            if len(last) >= 5:
                delta = tuple([last[i + 1] - last[i] for i in range(4)])
                if delta not in seen:
                    #if delta == (-2, 1, -1, 3):
                    #    print(xx, last)
                    dd[delta] += last[-1]
                    seen.add(delta)
                    
                last.pop(0)
            assert len(last) <= 4
            
        out += x
        
    print(out)
    print(max(dd[v] for v in dd))

    #break

    

