import requests
from secret import session

from collections import defaultdict as DD
from itertools import product as P, combinations as CO, permutations as PE
R = range

DAY = 15

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
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########


<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''

s_2 = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''

s_3 = '''
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
'''

s_real = getday(DAY)

dI = {'v' : 1, '^': -1, '<': 0, '>': 0}
dJ = {'v' : 0, '^': 0, '<': -1, '>': 1}

def fixx(s):
    out = []
    for c in s:
        out += {'#': '##', '.': '..', '@': '@.', 'O': '[]'}[c]

    return list(''.join(out))

def pb(board):
    board[si][sj] = '@'
    for line in board:
        print(''.join(line))
    print()
    board[si][sj] = '.'
        

for s in [s_samp, s_real]:
#for s in [s_samp]:
    s = s.strip()
    ll = s.split('\n')
    n = len(ll)

    if n == 0:
        continue

    print('Lines:', n)
    print('Size:', len(s))

    board = []
    while ll[0] != '':
        board.append(fixx(ll.pop(0)))

    s = ''
    for line in ll:
        s += line

    n = len(board)
    m = len(board[0])

    for si, sj in P(R(n), R(m)):
        if board[si][sj] == '@':
            board[si][sj] = '.'
            break

    for c in s:
        di = dI[c]
        dj = dJ[c]

        '''
        ci, cj = si, sj

        good = 0
        if di == 0:
            while True:
                ci += di
                cj += dj

                if board[ci][cj] == '#':
                    break
                elif board[ci][cj] == '.':
                    good = 1
                    break
                else:
                    assert board[ci][cj] in '[]'
            if good:
                lo = min(cj, sj + 2)
                hi = max(cj + 1, sj - 1)

                assert (hi - lo) % 2 == 0
                for j in range(lo, hi, 2):
                    board[ci][j] = '['
                for j in range(lo + 1, hi, 2):
                    board[ci][j] = ']'

                sj += dj'''

        good = 1
        st = [(si, sj)]
        seen = set()
        while st:
            i, j = st.pop()
            if (i, j) in seen:
                continue

            seen.add((i, j))
            
            if board[i][j] == '#':
                good = 0
                break

            if board[i][j] == '[':
                st.append((i, j + 1))
            if board[i][j] == ']':
                st.append((i, j - 1))

            if board[i][j] == '.' and (i, j) != (si, sj):
                continue

            st.append((i + di, j + dj))

        if good:
            fix = sorted(seen, key = lambda x: x[0] * di + x[1] * dj, reverse = 1)
            for i, j in fix:
                if board[i][j] == '.':
                    pass
                elif board[i][j] in '[]':
                    assert board[i + di][j + dj] == '.'
                    board[i + di][j + dj] = board[i][j]
                    board[i][j] = '.'
                else:
                    assert 0

            si += di
            sj += dj

            assert board[si][sj] == '.'

            

        if 0:
            print(c)
            pb(board)

    out = 0
    for i, j in P(R(n), R(m)):
        if board[i][j] == '[':
            out += 100 * i + j
    pb(board)
    cout(out)
    

