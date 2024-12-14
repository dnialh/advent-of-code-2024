import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

from collections import defaultdict as DD

DAY = 5

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
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''

s = getday(DAY)

s = s.strip()
ll = s.split('\n')
n = len(ll)

print('Lines:', n)
print('Size:', len(s))

rules = DD(set)
out = 0
out2 = 0

import random

from functools import cache

for line in ll:
    if '|' in line:
        l, r = map(int, line.split('|'))
        rules[r].add(l)

    elif ',' in line:
        x = list(map(int, line.split(',')))
        z = len(x)

        bad = set()
        g = 1

        for s in x:
            if s in bad:
                g = 0
            bad |= rules[s]

        y = x[:]
        yy = x[:]

        @cache
        def ct(u):
            z = 1
            for v in rules[u]:
                if v in y:
                    z += ct(v)
            return z
        
        if g:
            out += int(x[z//2])
        else:
            yy.sort(key = lambda i: -ct(i))

            '''
            while True:
                for i in range(z - 1):
                    if x[i] in rules[x[i + 1]]:
                        assert 0
                        x[i], x[i + 1] = x[i + 1], x[i]
                        break
                    
                else:
                    break'''
            
            
            out2 += int(yy[z//2])
            
        #out += g
cout(out2)
cout(out)
        


