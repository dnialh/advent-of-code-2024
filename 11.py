import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

from functools import cache

DAY = 11

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
125 17
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

    #l = list(map(int, ll[0].split()))

    @cache
    def ct(s, times):
        #print(s, times)
        
        if times == 0:
            return 1

        while s[0] == '0' and len(s) > 1:
            s = s[1:]

        if s == '0':
            return ct('1', times - 1)

        z = len(s)
        if len(s) % 2 == 0:
            l = s[:z//2]
            r = s[z//2:]

            return ct(l, times - 1) + ct(r, times - 1)

        t = int(s) * 2024
        return ct(str(t), times - 1)

    out = 0
    for v in ll[0].split():
        out += ct(v, 75)

    cout(out)
            

    

