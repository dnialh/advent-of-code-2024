import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

dI = {'v' : 1, '^': -1, '<': 0, '>': 0}
dJ = {'v' : 0, '^': 0, '<': -1, '>': 1}

dX = [0, 1, 0, -1]
dY = [1, 0, -1, 0]
#v>^<


DAY = 18

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
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
'''

s_real = getday(DAY)

for s in [s_real]:
#for s in [s_samp]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    MX = 70

    lo = 0
    hi = 1024 * 1024 #blocked
    while hi - lo > 1:
        mid = (lo + hi) // 2
        
        blocked = set()
        for l in ll[:mid]:
            x, y = map(int, l.split(','))
            assert 0 <= x <= MX
            blocked.add((x, y))

        dist = {(0, 0): 0}
        q = [(0, 0, 0)]
        while q:
            u, v, di = q.pop(0)

            for d in range(4):
                uu = u + dX[d]
                vv = v + dY[d]

                if 0 <= uu <= MX and 0 <= vv <= MX:
                    if (uu, vv) not in dist and (uu, vv) not in blocked:
                        dist[(uu, vv)] = di + 1
                        q.append((uu, vv, di + 1))

        if (MX, MX) in dist:
            lo = mid
        else:
            hi = mid

    cout(hi)
    print(ll[hi - 1])
        

