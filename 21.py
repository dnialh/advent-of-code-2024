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


DAY = 21
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
029A
980A
179A
456A
379A
'''

s_real = getday(DAY)

def get(x):
    if x == 'A':
        return 10
    return int(x)

def sim(s):
    #nex = {'<': 0, '^': 0 , 'v': 0, '>': 0, 'A': 0}
    nex = ''

    cX = 2
    cY = 1

    for c in s:
        #ct = curr[c]

        
        nX = jX[c]
        nY = jY[c]

        while cX < nX:
            #nex['>'] += ct
            nex += '>'
            cX += 1
        while cX > nX:
            #nex['<'] += ct
            nex += '<'
            cX -= 1
        while cY < nY:
            #nex['^'] += ct
            nex += '^'
            cY += 1
        while cY > nY:
            #nex['v'] += ct
            nex += 'v'
            cY -= 1

        #nex['A'] += ct
        nex += 'A'

    return nex

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    board = ll
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])

    iX = [1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 2]
    iY = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0]

    jX = {'<': 0, '^': 1 , 'v': 1, '>': 2, 'A': 2}
    jY = {'<': 0, '^': 1 , 'v': 0, '>': 0, 'A': 1}

    out = 0

    @cache
    def solve(st, it):
        #print(st, it)
        if it == 0:
            return len(st) + 1
        
        cX = 2
        cY = 1

        out = 0
    
        for c in st + 'A':
            ccx, ccy = cX, cY

            best = float('inf')
            nX = jX[c]
            nY = jY[c]

            # print(cX, cY, c)
            
            for i in range(1):
                s = ''
                
                while cX < nX:
                    s += '>'
                    cX += 1
                while cX > nX:
                    s += '<'
                    cX -= 1

                if cX == 0 and cY == 1:
                    break
                    
                while cY < nY:
                    s += '^'
                    cY += 1
                while cY > nY:
                    s += 'v'
                    cY -= 1

                best = min(best, solve(s, it - 1))

            cX, cY = ccx, ccy
            
            for i in range(1):
                s = ''
            
                while cY < nY:
                    s += '^'
                    cY += 1
                while cY > nY:
                    s += 'v'
                    cY -= 1

                if cX == 0 and cY == 1:
                    break
                    
                while cX < nX:
                    s += '>'
                    cX += 1
                while cX > nX:
                    s += '<'
                    cX -= 1

                best = min(best, solve(s, it - 1))

            cX, cY = nX, nY
            out += best

        return out

    #break

    def solve2(st, it):
        assert it != 0
        
        cX = 2
        cY = 0

        poss = ['']
    
        for c in st:
            ccx, ccy = cX, cY

            best = float('inf')
            nX = iX[get(c)]
            nY = iY[get(c)]
            
            nex = []
            
            for i in range(1):
                s = ''
                
                while cX < nX:
                    s += '>'
                    cX += 1
                while cX > nX:
                    s += '<'
                    cX -= 1

                if cX == 0 and cY == 0:
                    break
                    
                while cY < nY:
                    s += '^'
                    cY += 1
                while cY > nY:
                    s += 'v'
                    cY -= 1

                s += 'A'

                for t in poss:
                    nex.append(t + s)



            cX, cY = ccx, ccy
            
            for i in range(1):
                s = ''
            
                while cY < nY:
                    s += '^'
                    cY += 1
                while cY > nY:
                    s += 'v'
                    cY -= 1

                if cX == 0 and cY == 0:
                    break
                    
                while cX < nX:
                    s += '>'
                    cX += 1
                while cX > nX:
                    s += '<'
                    cX -= 1

                s += 'A'


                for t in poss:
                    nex.append(t + s)

            poss = nex

        return min(solve(s[:-1], it) for s in poss)
            
    for line in ll:
        '''
        #curr = {'<': 0, '^': 0 , 'v': 0, '>': 0, 'A': 0}
        s = ''
        
        cX = 2
        cY = 0
        for c in line:
            nX = iX[get(c)]
            nY = iY[get(c)]
            
            while cX < nX:
                #curr['>'] += 1
                s += '>'
                cX += 1
            while cY < nY:
                s += '^'
                #curr['^'] += 1
                cY += 1
            while cX > nX:
                #curr['<'] += 1
                s += '<'
                cX -= 1
            while cY > nY:
                s += 'v'
                #curr['v'] += 1
                cY -= 1

            #curr['A'] += 1
            s += 'A'
    
        print(s)

        for i in range(2):
            s = sim(s)
            print(s)'''

        mov = solve2(line, 25)

        print(line, mov)
        
        out += int(line[:-1]) * mov
    cout(out)
            

