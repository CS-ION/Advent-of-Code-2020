puzzle = '''...#...###......##.#..#.....##.
#.#.......##.....#...##..##.#.#
.......#....#..##...#..#######.
.#...#.#####....##..........##.'''

L = puzzle.split('\n')
for I in range(len(L)):
    L[I] = L[I]*100

def trees(x,y):
    tree = 0
    incriminator = x
    for I in range(0,len(L)-1,y):
        ch = L[I+y][x]
        if ch == '#':
            tree+=1
        x = x + incriminator
    return tree

T = 1
right = [1,3,5,7,1]
down = [1,1,1,1,2]
for I in range(5):
    if I == 1:
        print('Part1',trees(right[I],down[I]))
    T = T * trees(right[I],down[I])
print('Part2',T)
