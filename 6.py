f = open(r'C:\Users\Toshiba\Desktop\Advent Code\input.txt','r')
L = f.read().split('\n\n')

tot_yes,total = 0,0
for I in L:
    if len(I.split('\n'))==1:
        total+=len(I.split('\n')[0])
        continue
    D = dict.fromkeys([chr(I) for I in range(97,123)],0)
    yes = 0 
    qs_ans = []
    for J in I:
        if J =='\n':
            continue
        D[J]+=1
        if J in qs_ans:
            continue
        yes+=1
        qs_ans.append(J)
    for key in D:
        if D[key]==len(I.split('\n')):
            total+=1
    tot_yes+=yes

print('Part1',tot_yes)
print('Part2',total)