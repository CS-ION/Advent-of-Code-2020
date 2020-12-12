f = open('input.txt', 'r')
L = [I for I in f.read().split('\n')]

directions = ['N','W','S','E']
values = dict.fromkeys(directions,0)

curr_dir = 'E'
for I in L:
    if 'L' in I:
        x = int(I[1::]) // 90
        index = directions.index(curr_dir)+x
        if index >= len(directions):
            index = int(index % 4)
        curr_dir = directions[index]
        continue
    if 'R' in I:
        x = int(I[1::]) // 90
        index = directions.index(curr_dir)-x
        curr_dir = directions[index]
        continue
    if 'F' in I:
        values[curr_dir] += int(I[1::])
        continue
    values[I[0]] += int(I[1::])

print('Part1',abs(values['E']-values['W']) + abs(values['N']-values['S']))

values = dict.fromkeys(directions,0)
curr_dir = ['N1','E10']

for I in L:
    if 'L' in I:
        x = int(I[1::]) // 90
        for J in range(2):
            index = directions.index(curr_dir[J][0])+x
            if index >= len(directions):
                index = int(index % 4)
            dire = directions[index]
            curr_dir.append(dire + curr_dir[J][1::])
        del curr_dir[0:2:1]
        continue
    if 'R' in I:
        x = int(I[1::]) // 90
        for J in range(2):
            index = directions.index(curr_dir[J][0])-x
            dire = directions[index]
            curr_dir.append(dire + curr_dir[J][1::])
        del curr_dir[0:2:1]
        continue
    if 'F' in I:
        for J in curr_dir:
            temp = int(I[1::])*int(J[1::])
            values[J[0]] += temp
        continue
    for J in range(2):
        if curr_dir[J][0] == I[0]:
            new_val = int(curr_dir[J][1::])+int(I[1::])
            curr_dir[J] = curr_dir[J][0] + str(new_val)

print('Part2',abs(values['E']-values['W']) + abs(values['N']-values['S']))