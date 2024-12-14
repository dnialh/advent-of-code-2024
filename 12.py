import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 12

class DisjointSetUnion:
    def __init__(self, a, b):
        n = a * b
        self.parent = list(range(n))
        self.size = [1] * n
        self.per = [4] * n
        self.cor = [DD(int) for _ in range(n)]

        for i, j in P(R(a), R(b)):
            self.cor[m * i + j][(i, j)] = 1
            self.cor[m * i + j][(i, j + 1)] = 2
            self.cor[m * i + j][(i + 1, j + 1)] = 4
            self.cor[m * i + j][(i + 1, j)] = 8
            #self.cor[m * i + j].add((i, j + 1))
            #self.cor[m * i + j].add((i + 1, j))
            #self.cor[m * i + j].add((i + 1, j + 1))
        
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.per[a] += self.per[b]

            for v in self.cor[b]:
                self.cor[a][v] ^= self.cor[b][v]

        self.per[a] -= 2

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


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
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''

s_samp = '''
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''

s_real = getday(DAY)

def lenl(l):
    z = 0
    for u in l:
        x = l[u]
        if x == 0:
            pass
        elif x == 15:
            pass
        elif x == 5:
            z += 2
        elif x == 10:
            z += 2
        elif x in [1,2,4,8]:
            z += 1
        elif 15 - x in [1,2,4,8]:
            z += 1
    return z

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])

    UF = DisjointSetUnion(n, m)

    for i in range(n):
        for j in R(m - 1):
            if ll[i][j] == ll[i][j + 1]:
                UF.union(m * i + j, m * i + j + 1)
    for i in range(n - 1):
        for j in R(m):
            if ll[i][j] == ll[i + 1][j]:
                UF.union(m * i + j, m * i + j + m)

    out = 0
    for i in range(n * m):
        if UF.find(i) == i:
            out += lenl(UF.cor[i]) * UF.size[i]

    cout(out)

