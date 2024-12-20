inf = -1

def _min(a, b):
    return a if b == inf or inf != a < b else b

class DistanceKeeper:
    def __init__(self, n):
        self.m = 1
        while self.m < n: self.m *= 2
        self.data = 2 * self.m * [inf]
        self.dist = n * [inf]
        self.__getitem__ = self.dist.__getitem__

    def __setitem__(self, ind, x):
        self.dist[ind] = x
        ind += self.m
        self.data[ind] = x
        ind >>= 1
        while ind:
            self.data[ind] = _min(self.data[2 * ind], self.data[2 * ind + 1])
            ind >>= 1


    def __getitem__(self, ind):
        return self.dist[ind]

    def trav(self):
        while self.data[1] != inf:
            x = self.data[1]

            ind = 1
            while ind < self.m:
                ind = 2 * ind + (self.data[2 * ind] != x)
            ind -= self.m

            self[ind] = inf
            self.dist[ind] = x
            yield ind

def dijkstra(graph, start):
    n = len(graph)

    P = [-1] * n
    D = DistanceKeeper(n)
    D[start] = 0

    for node in D.trav():
        for nei, weight in graph[node]:
            new_dist = D[node] + weight
            if D[nei] == inf or new_dist < D[nei]:
                D[nei] = new_dist
                P[nei] = node

    return D.dist


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


DAY = 20
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
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''

s_real = getday(DAY)

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

    adj = [[] for _ in R(n * m)]
    for i, j in P(R(n), R(m)):
        ind = m * i + j
        
        c = board[i][j]
        if c == 'S':
            si, sj = i, j
            sind = ind
        elif c == 'E':
            eind = ind

        if c != '#':
            for d in [-m, -1, 1, m]:
                adj[ind].append((ind + d, 1))

    d1 = dijkstra(adj, sind)
    d2 = dijkstra(adj, eind)

    assert d1[eind] == d2[sind]
    fair = d1[eind]

    '''
    save = []
    for i, j in P(R(n), R(m)):
        ind = m * i + j
        
        c = board[i][j]
        if c != '#':
            continue
        
        if d1[ind] != -1 and d2[ind] != -1:
            time = d1[ind] + d2[ind]
            save.append(fair - time)
    save.sort()
    #print(save)
    out = 0
    for v in save:
        if v >= 100:
            out += 1
    print(out)
    '''

    out = 0

    save = []
    
    for di, dj in P(R(-20, 21), R(-20, 21)):
        if abs(di) + abs(dj) > 20:
            continue
                
        for i, j in P(R(n), R(m)):
            ii, jj = i + di, j + dj

            if not (0 <= ii < n):
                continue
            if not (0 <= jj < m):
                continue
            
            ind = m * i + j
            ind2 = m * ii + jj

            if board[ii][jj] == '#':
                continue
            if board[i][j] == '#':
                continue

            if d1[ind] == -1 or d2[ind2] == -1:
                continue

            time = d1[ind] + d2[ind2] + abs(di) + abs(dj)

            assert time % 2 == 0

            x = fair - time
            if x >= 100:
                #print(i, j, ii, jj, x)
                save.append(x)
                
    #print(save)
    print(len(save))
