f = open(r'C:\Users\Toshiba\Desktop\Advent Code\input.txt','r')
L = [int(I) for I in f.read().split('\n')]
L.append(0)
L.sort()
L.append(max(L)+3)

one_diff = 0
three_diff = 0
for I in range(1,len(L)):
    if L[I] - L[I-1] == 1:
        one_diff+=1
    elif L[I] - L[I-1] == 3:
        three_diff+=1

print('Part1',one_diff*three_diff)