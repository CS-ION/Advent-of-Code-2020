puzzle = '''1
2
3
4
5'''

#copy paste your puzzle input as multiline string

L = puzzle.split('\n')
L1 = []
for I in L:
    L1.append(int(I))
X = len(L1)

#part1
for I in range(X):
    for J in range(I,X):
        if L1[I]+L1[J] == 2020:
            print('Part1',L1[I]*L1[J])

#part2
for I in range(X):
    for J in range(I,X):
        for M in range(J,X):
            if L1[I]+L1[J]+L1[M] == 2020:
                print('Part2',L1[I]*L1[J]*L1[M])
