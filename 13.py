f = open('input.txt', 'r')
data = f.read().splitlines()
L = [int(I) for I in data[1].split(',') if I!='x']
L1 = [I for I in data[1].split(',')]
timestamp = int(data[0])

t = []
for I in L:
    t.append(((int(timestamp/I)+1)*I)-timestamp)

print('Part1',L[t.index(min(t))]*min(t))

desired = []
for I in range(len(L1)):
    if L1[I] == 'x':
        continue
    desired.append((int(L1[I]) - I) % int(L1[I]))

curr_timestamp = 400000000000016 #no gotten by trial and error
while True:
    for I in range(len(L)):
        rem = curr_timestamp % L[I]
        if rem != desired[I]:
            break
    else:
        break
    curr_timestamp+=41
print('Part2',curr_timestamp)