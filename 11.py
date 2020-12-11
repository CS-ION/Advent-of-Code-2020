f = open(r'C:\Users\Toshiba\Desktop\Advent Code\input.txt', 'r')
L = [list(I)for I in f.read().split('\n')]

def part1():
    global equilibrium
    new_list = []
    for I in range(len(L)):
        temp_list = []
        for J in range(len(L[0])):
            adj_seats = []
            if J-1 >= 0:
                adj_seats.append(L[I][J-1])
            if I-1 >= 0:
                adj_seats.append(L[I-1][J])
            if J+1 < len(L[0]):
                adj_seats.append(L[I][J+1])
            if I+1 < len(L):
                adj_seats.append(L[I+1][J])
            if J-1 >= 0 and I-1 >= 0:
                adj_seats.append(L[I-1][J-1])
            if J-1 >= 0 and I+1 < len(L):
                adj_seats.append(L[I+1][J-1])
            if J+1 < len(L[0]) and I-1 >= 0:
                adj_seats.append(L[I-1][J+1])
            if J+1 < len(L[0]) and I+1 < len(L):
                adj_seats.append(L[I+1][J+1])
            appendix = L[I][J]
            adj_seats = [I for I in adj_seats if I == '#']
            if L[I][J] == 'L' and len(adj_seats) == 0:
                appendix = '#'
            if L[I][J] == '#' and len(adj_seats) >= 4:
                appendix = 'L'
            temp_list.append(appendix)
        new_list.append(temp_list)
    if new_list == L:
        equilibrium = False
    return new_list
    
equilibrium = True
while equilibrium:
    L1 = part1()
    L = L1

count = 0
for I in L:
    count += len([J for J in I if J == '#'])
print('Part1',count)

def part2():
    global equilibrium
    new_list = []
    for I in range(len(L)):
        temp_list = []
        for J in range(len(L[0])):
                adj_seats = []
                x = J-1
                while x>=0:
                    if L[I][x]!='.':
                        adj_seats.append(L[I][x])
                        break
                    x=x-1
                y = I-1
                while y>=0:
                    if L[y][J]!='.':
                        adj_seats.append(L[y][J])
                        break
                    y=y-1
                x = J+1
                while x<len(L[0]):
                    if L[I][x]!='.':
                        adj_seats.append(L[I][x])
                        break
                    x=x+1
                y = I+1
                while y<len(L):
                    if L[y][J]!='.':
                        adj_seats.append(L[y][J])
                        break
                    y=y+1
                x,y = J-1,I-1
                while x>=0 and y>=0:
                    if L[y][x]!='.':
                        adj_seats.append(L[y][x])
                        break
                    x = x-1
                    y = y-1
                x,y = J-1,I+1
                while x>=0 and y<len(L):
                    if L[y][x]!='.':
                        adj_seats.append(L[y][x])
                        break
                    x = x-1
                    y = y+1
                x,y = J+1,I-1
                while x<len(L[0]) and y>=0:
                    if L[y][x]!='.':
                        adj_seats.append(L[y][x])
                        break
                    x = x+1
                    y = y-1
                x,y = J+1,I+1
                while x<len(L[0]) and y<len(L):
                    if L[y][x]!='.':
                        adj_seats.append(L[y][x])
                        break
                    x = x+1
                    y = y+1
                appendix = L[I][J]
                adj_seats = [I for I in adj_seats if I == '#']
                if L[I][J] == 'L' and len(adj_seats) == 0:
                    appendix = '#'
                if L[I][J] == '#' and len(adj_seats) >= 5:
                    appendix = 'L'
                temp_list.append(appendix)
        new_list.append(temp_list)
    if new_list == L:
        equilibrium = False
    return new_list

equilibrium = True
while equilibrium:
    L1 = part2()
    L = L1

count = 0
for I in L:
    count += len([J for J in I if J == '#'])
print('Part2',count)