import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 6

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
    #input()
    
s_samp = '''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''

s_real = getday(DAY)

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])

    for i in range(n):
        for j in range(m):
            if ll[i][j] == '^':
                ssi = i
                ssj = j

    dX = [-1, 0, 1, 0]
    dY = [0, 1, 0, -1]
    sd = 0

    si = ssi
    sj = ssj
    
    s = set()
    while 0 <= si < n and 0 <= sj < m:
        while True:
            s.add((si, sj))
            ni = si + dX[sd]
            nj = sj + dY[sd]

            if 0 <= ni < n and 0 <= nj < m and ll[ni][nj] == '#':
                sd += 1
                sd %= 4
                continue

            si, sj = ni, nj
            break

    s2 = 0
    for i, j in s:
        if i == si and j == si:
            continue

        sd = 0
        si = ssi
        sj = ssj
        bad = 0

        sz = 0
        
        seen = set()
        while 0 <= si < n and 0 <= sj < m and not bad:
            sz += 1
            while True:
                if (si, sj, sd) in seen:
                    bad = 1
                    break
                
                seen.add((si, sj, sd))
                
                ni = si + dX[sd]
                nj = sj + dY[sd]

                if 0 <= ni < n and 0 <= nj < m and (ll[ni][nj] == '#' or (ni, nj) == (i, j)):
                    sd += 1
                    sd %= 4
                    continue

                si, sj = ni, nj
                break

        #print(sz)

        #print(i, j, (si, sj, sd))
        s2 += bad
        
    
    cout(s2)        
        
