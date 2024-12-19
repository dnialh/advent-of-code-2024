import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

dI = {'v' : 1, '^': -1, '<': 0, '>': 0}
dJ = {'v' : 0, '^': 0, '<': -1, '>': 1}

dX = [0, 1, 0, -1]
dY = [1, 0, -1, 0]
#v>^<


DAY = 17

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
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
'''

s_real = getday(DAY)

for s in [s_real]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    a = int(ll[0].split()[2])
    b = int(ll[1].split()[2])
    c = int(ll[2].split()[2])

    prog = list(map(int, ll[4].split()[1].split(',')))
    

    #b = 2024
    #c = 43690
    #prog = [4, 0]

    for aa in range(1):
        a = 105843716614554
        
        out = []
        ptr = 0
        while ptr < len(prog):
            ins = prog[ptr]
            lit = prog[ptr + 1]
            comb = [0, 1, 2, 3, a, b, c, None][lit]
            
            if ins == 0:
                a >>= comb            
                ptr += 2
            elif ins == 1:
                b ^= lit
                ptr += 2
            elif ins == 2:
                b = comb & 7
                ptr += 2
            elif ins == 3:
                if a != 0:
                    ptr = lit
                else:
                    ptr += 2
            elif ins == 4:
                b ^= c
                ptr += 2
            elif ins == 5:
                out.append(comb & 7)
                ptr += 2
                print(b)
            elif ins == 6:
                b = a >> comb
                ptr += 2
            elif ins == 7:
                c = a >> comb
                ptr += 2
            print(a, b, c)

        print(aa)
        print(','.join(map(str, out)))
        print()

def solve(z, prog):
    if prog == []:
        return z

    z *= 8
    
    *pp, v = prog
    for b in range(8):
        poss = (v ^ 3 ^ ((z + b) >> (b ^ 5))) & 7
        if poss == b:
            rec = solve(z + b, pp)
            if rec:
                return rec

print(solve(0, prog))
'''
z = 0
for v in prog[::-1]:
    z *= 8
    for b in range(8):
        poss = (v ^ 3 ^ ((z + b) >> (b ^ 5))) & 7
        if poss == b:
            break
    else:
        assert 0
        
    z += b
    print(z, v, b)'''

