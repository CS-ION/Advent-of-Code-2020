puzzle = '''2-4 p: vpkpp
1-8 r: mrrrrrrrrrf
1-3 w: wwww
5-6 d: qldxdsdk'''

L = puzzle.split('\n')
for I in range(len(L)):
    L[I] = L[I].split(' ')    
#L = [['4-5', 's:', 'rsssw']]

#part1
valid = 0
for I in L:
    count = 0 
    start_val = int(I[0].split('-')[0])
    stop_val = int(I[0].split('-')[1]) + 1
    for J in I[2]:
        if I[1][0] == J:
            count+=1
    if count in range(start_val,stop_val):
        valid+=1
print(valid)

#part2
valid = 0
for I in L:
    pos1 = int(I[0].split('-')[0]) - 1
    pos2 = int(I[0].split('-')[1]) - 1
    if I[2][pos1]==I[1][0] and I[2][pos2]==I[1][0]:
        continue
    elif I[2][pos1]!=I[1][0] and I[2][pos2]!=I[1][0]:
        continue
    else:
        valid+=1
print(valid)


