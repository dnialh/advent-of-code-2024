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


DAY = 25
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
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
'''

s_real = getday(DAY)

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n\n')
    board = ll
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])

    s = []
    out = 0

    for line in ll:
        z = []

        l = line.split('\n')

        o = 0
        m = 1
        for i in range(6):
            for j in range(5):
                if l[i][j] == '#':
                    o += m
                m *= 2

        for v in s:
            if o & v == 0:
                out += 1
        s.append(o)

    print(out)

    

    

