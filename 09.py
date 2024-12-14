import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 9

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
2333133121414131402
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

    assert n == 1

    x = []
    ii = 0
    for c in ll[0]:
        d = int(c)

        if ii >= 0:
            x.extend([ii] * d)
            ii = -1 - ii
        else:
            x.extend([-1] * d)
            ii = -ii

    gap = [0] * 10

    def sz(i):
        c = x[i]
        #assert i + 1 == len(x) or x[i + 1] != c

        j = i
        while j >= 0 and x[j] == c:
            j -= 1

        return i - j

    y = []
    while x:
        if x[-1] < 0:
            y.append(x.pop())
            continue

        z = sz(len(x)-1)

        while gap[z] < len(x) and sum(x[gap[z]: gap[z] + z]) != -z:
            gap[z] += 1

        if gap[z] < len(x):
            for i in range(gap[z], gap[z] + z):
                x[i] = x.pop()
                y.append(-1)
        else:
            for i in range(z):
                y.append(x.pop())

    x = y[::-1]

    out = 0
    for i in range(len(x)):
        if x[i] >= 0:
            out += i * x[i]

    cout(out)
        
        

