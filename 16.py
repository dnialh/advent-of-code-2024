import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

dI = [0, 1, 0, -1]
dJ = [1, 0, -1, 0]

DAY = 16

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


samp = '''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
'''

s_samp = '''
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
'''

s_real = getday(DAY)

from heapq import heappush, heappop

for s in [samp, s_samp, s_real]:
    s = s.strip()
    ll = s.split('\n')
    board = [list(l) for l in ll]
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    m = len(ll[0])
    
    for i, j in P(R(n), R(m)):
        if ll[i][j] == 'S':
            si, sj = i, j
        if ll[i][j] == 'E':
            ei, ej = i, j

    #incorrect - can only start east - wasted 10 minutes :cry:
    q = [(0, si, sj, z, None) for z in range(4)]
    
    seen = {}
    good = {}

    best = 10 ** 10

    while q:
        cost, i, j, d, prev = heappop(q)

        if (i, j, d) in seen:
            if (prev != None) and seen[(i, j, d)] == cost:
                good[(i, j, d)] |= good[(prev)]
            continue

        if (i, j) == (ei, ej):
            best = min(cost, best)

        seen[(i, j, d)] = cost
        good[(i, j, d)] = set([(i, j)])
        
        if prev:
            good[(i, j, d)] |= good[(prev)]

        heappush(q, (cost + 1000, i, j, (d + 1) % 4, (i, j, d)))
        heappush(q, (cost + 1000, i, j, (d - 1) % 4, (i, j, d)))

        ii, jj = i + dI[d], j + dJ[d]

        if board[ii][jj] != '#':
            heappush(q, (cost + 1, ii, jj, (d) % 4, (i, j, d)))

    out = set()
    for d in range(4):
        if seen[(ei, ej, d)] == best:
            print(len(good[(ei, ej, d)]))
            out |= good[(ei, ej, d)]

    zz = ''
    for i, j in out:
        board[i][j] = 'O'
    for line in board:
        print(''.join(line))
        zz += ''.join(line)

    cout(best + 1000)
    cout(len(out))

