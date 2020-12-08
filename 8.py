f = open('input.txt','r')
L = f.read().split('\n')

def running_code():
    visited = []
    acc = 0
    I = 0
    terminating = False
    while I not in visited:
        visited.append(I)
        if I >= len(L):
            terminating = True
            break
        if 'nop' in L[I]:
            I+=1
        elif 'jmp' in L[I]:
            I = I + int(L[I].split(' ')[1])
        elif 'acc' in L[I]:
            acc = acc + int(L[I].split(' ')[1])
            I+=1
    return acc,terminating

print('Part1',running_code()[0])

for I in range(len(L)):
    line = L[I]
    if 'jmp' in L[I]:
        L[I] = 'nop' + ' ' + L[I].split(' ')[1]
    elif 'nop' in L[I]:
        L[I] = 'jmp' + ' ' + L[I].split(' ')[1]
    if running_code()[1]==True:
        print('Part2',running_code()[0])
        break
    else:
        L[I] = line

