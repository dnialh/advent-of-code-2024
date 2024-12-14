import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 2

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
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

s = getday(DAY)

s = s.strip()
ll = s.split('\n')
n = len(ll)

print('Lines:', n)
print('Size:', len(s))

out = 0
for l in ll:
    u = list(map(int, l.split()))
    #v = sorted(u)

    '''
    if v == u or v == u[::-1]:
        pass
    else:
        continue'''

    g = 0


    for nn in range(len(u) + 1):
        v = u[:]

        if nn < len(u):
            v.pop(nn)

        y = 0
        z = 0
        
        x = len(v)
        for i in range(x - 1):
            # assert v[i] < v[i + 1]
            if -3 <= v[i] - v[i + 1] <= -1:
                pass
            else:
                z += 1

            if -3 <= v[i + 1] - v[i] <= -1:
                pass
            else:
                y += 1

        #print(v, y, z)

        g |= ((z == 0) or (y == 0))

    #(u, g)
    out += g 

cout(out)
            

