import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 1

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
    input()
    
s = '''
'''

s = getday(DAY)

s = s.strip()
ll = s.split('\n')
n = len(ll)

print('Lines:', n)
print('Size:' len(s))

l = []
r = []

for g in ll:
    u, v = map(int, g.split())
    l.append(u)
    r.append(v)

l.sort()
r.sort()

out = 0
for u in l:
    out += u * r.count(u)
    
cout(out)

