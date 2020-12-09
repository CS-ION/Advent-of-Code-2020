f = open(r'C:\Users\Toshiba\Desktop\Advent Code\input.txt','r')
L = f.read().split('\n')

check_list = []
for I in range(25,len(L)):
    for J in range(1,26):
        for M in range(J+1,26):
            if int(L[I-M]) + int(L[I-J]) == int(L[I]):
                check_list.append(L[I])

for I in range(25,len(L)):
    if L[I] not in check_list:
        print('Part1',invalid_no := L[I])
        break

cont_set = []
for I in range(len(L)):
    t = int(L[I])
    for J in range(I+1,len(L)):
        if t == int(invalid_no):
            if len(L[I:J:1])!=1:
                cont_set += [int(M) for M in L[I:J:1]]
        t = t+int(L[J])

print('Part2',max(cont_set) + min(cont_set))