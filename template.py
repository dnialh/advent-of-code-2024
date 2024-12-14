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
    
s_samp = '''
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

