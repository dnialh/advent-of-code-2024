import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 14

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
    
s_samp = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''

s_real = getday(DAY)

#W = 11
#H = 7

W = 101
H = 103

for s in [s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    ct = [0] * 4
    rob = []

    for line in ll:
        pp, vv = line.split(' ')
        pp = pp.split('=')[1]
        vv = vv.split('=')[1]

        px, py = map(int, pp.split(','))
        vx, vy = map(int, vv.split(','))

        rob.append((px, py, vx, vy))

    def ct(t):
        line = [0] * W
        for px, py, vx, vy in rob:
            xx = (px + t * vx) % W
            yy = (py + t * vy) % H

            line[xx] += 1

        return max(line)

    def ctV(t):
        line = [0] * H
        for px, py, vx, vy in rob:
            xx = (px + t * vx) % W
            yy = (py + t * vy) % H

            line[yy] += 1

        return max(line)
                
    def test(t):
        board = [[' '] * W for _ in range(H)]
        
        for px, py, vx, vy in rob:
            xx = (px + t * vx) % W
            yy = (py + t * vy) % H

            board[yy][xx] = '*'

        lines = [''.join(l) for l in board]
        print('\n'.join(lines))

    '''
        xx = (px + 100 * vx) % W
        yy = (py + 100 * vy) % H

        if xx == W // 2:
            continue
        if yy == H // 2:
            continue

        ind = (xx > (W // 2)) + 2 * (yy > (H // 2))
        ct[ind] += 1'''

    runW = [ct(i) for i in range(200)]
    runH = [ctV(i) for i in range(200)]

    i = runW.index(max(runW))
    j = runH.index(max(runH))

    while i % H != j:
        i += W

    cout(i)

