import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 4

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
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

s = getday(DAY)

s = s.strip()
ll = s.split('\n')
n = len(ll)

print('Lines:', n)
print('Size:', len(s))

m = len(ll[0])

trans = [''] * m

out = 0
'''
for line in ll:
    out += line.count('XMAS')
    out += line[::-1].count('XMAS')

    assert len(line) == m
    for i in range(m):
        trans[i] += line[i]
        
for line in trans:
    out += line.count('XMAS')
    out += line[::-1].count('XMAS')
'''

for i in range(n - 2):
    for j in range(m - 2):
        s = ''
        for k in range(3):
            for kk in range(3):
                if (k + kk) % 2 == 0:
                    s += ll[i + k][j + kk]

        if s in ['MMASS', 'MSAMS', 'SMASM', 'SSAMM']:
            out += 1

            

cout(out)
