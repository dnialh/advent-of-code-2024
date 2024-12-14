import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 10

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
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''

dX = [0, 0, -1, 1]
dY = [1, -1, 0, 0]

tst = 0

s_real = getday(DAY)
if tst:
    s_real = ''

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])
    curr = DD(int)
    for i, j in P(R(n), R(m)):
        if ll[i][j] == '9':
            #curr[(i, j)].add((i, j))
            curr[(i, j)] = 1
    
    for c in '876543210':
        nex = DD(int)
        for i, j in P(R(n), R(m)):
            if ll[i][j] == c:
                for d in range(4):
                    nex[(i, j)] += curr[(i + dX[d], j + dY[d])]
        curr = nex

    out = 0
    for i, j in curr:
        out += curr[(i, j)]

    cout(out)

