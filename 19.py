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


DAY = 19

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
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''

s_real = getday(DAY)

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    pat = list(ll[0].split(', '))

    @cache
    def solve(s):
        if s == '':
            return 1

        out = 0
        
        for p in pat:
            if s[-len(p):] == p:
                out += solve(s[:-len(p)])

        return out

    out = 0
    for s in ll[2:]:
        #print(s, solve(s))
        out += solve(s)

    cout(out)
