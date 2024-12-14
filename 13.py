import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 13

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
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''

s_real = getday(DAY)

def get(s, ch = '+'):
    return int(s.split(ch)[1])
def get2(s, ch = '='):
    return int(s.split(ch)[1])

for s in [s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    out = 0

    for l in ll:
        a, b, c = l.split('\n')

        ax, ay = map(get, a.split(','))
        bx, by = map(get, b.split(','))
        cx, cy = map(get2, c.split(','))

        cx += 10000000000000
        cy += 10000000000000

        #print(ax, ay, cx, cy)

        if ay * bx == ax * by:
            assert 0

        off_a = -by * ax + bx * ay
        off_c = -by * cx + bx * cy

        ct_a = off_c//off_a

        if off_c % off_a:
            continue

        cx -= ct_a * ax
        cy -= ct_a * ay

        ct_b = cx // bx

        if cy == by * ct_b and ct_a >= 0 and ct_b >= 0:
            out += 3 * ct_a + ct_b

    cout(out)

