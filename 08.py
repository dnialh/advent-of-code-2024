import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 8

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
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

sd = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower() + '0123456789'

s_real = getday(DAY)

from math import gcd

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)
    b = ll

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    out = 0

    m = len(ll[0])

    s = set()
    for c in sd:
        loc = []
        for i, j in P(R(n), R(m)):
            assert b[i][j] == '.' or b[i][j] in sd
            if b[i][j] == c:
                for ii, jj in loc:
                    di, dj = ii - i, jj - j
                    assert gcd(di, dj) == 1

                    i0, j0 = i, j
                    while 0 <= i0 < n and 0 <= j0 < m:
                        s.add((i0, j0))

                        i0 += di
                        j0 += dj

                    i0, j0 = i, j
                    while 0 <= i0 < n and 0 <= j0 < m:
                        s.add((i0, j0))

                        i0 -= di
                        j0 -= dj
                        
                loc.append((i, j))
                s.add((i, j))

    cout(len(s))
        

