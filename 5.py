f = open('input.txt','r')
L = f.read().split('\n')

L1 = []
for I in L:
    x,w,y,z = 0,0,127,7
    row = 0
    col = 0
    for J in I:
        if J == 'F': 
            if y-x == 1:
                row = x
            y = x + int((y-x)/2)
        elif J == 'B':
            if y-x == 1:
                row = y
            x = x + round((y-x)/2)
        elif J == 'R':
            if z-w == 1:
                col = z
            w = w + round((z-w)/2)
        elif J == 'L':
            if z-w == 1:
                col = w
            z = w + int((z-w)/2)
    L1.append((row*8)+col)

print('Part1',max(L1))
L1.sort()
for I in range(len(L1)):
    if L1[I+1]-L1[I]!=1:
        print('Part2',L1[I]+1)
        break


        
