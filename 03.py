import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 3

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
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''

s = getday(DAY)

s = s.strip()
ll = s.split('\n')
n = len(ll)

print('Lines:', n)
print('Size:', len(s))

out = 0
on = 1
for l in ll:
    z = len(l)
    print(z)
    
    for i in range(z):
        if l[i:i+4] == 'do()':
            on = 1
        if l[i:i+7] == "don't()":
            on = 0
            
        
        if l[i:i+4] == 'mul('  and on: 
            x = l[i+4:].split(')')[0]
            if x.count(',') != 1:
                continue
            a, b = x.split(',')

            try:
                a = int(a)
                b = int(b)
                out += a * b
                #print(a, b)
            except ValueError:
                continue
                print(e)
            #except ArithmeticException:
            #    pass
            
            #print(z,i)

cout(out)
