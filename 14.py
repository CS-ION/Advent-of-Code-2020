f = open('input.txt', 'r')
data = f.read().splitlines()

mem = {}
curr_mask = ''

for I in data:
    ins,value = I.split(" = ")
    if ins == 'mask':
        curr_mask = value
        continue
    mem_add = ins[4:-1]
    bin_val = str(bin(int(value)))[2::]
    zeroes = '0'*(36 - len(bin_val))
    bin_val = zeroes + bin_val
    new_val = ''
    for I in range(36):
        if curr_mask[I]!='X':
            new_val+=curr_mask[I]
            continue
        new_val+=bin_val[I]
    new_val = '1' + new_val.split('1',1)[1]
    new_val = int(new_val,2)
    mem[mem_add] = new_val

print('Part1',sum(mem.values()))

mem = {}
curr_mask = ''

for I in data:
    ins,value = I.split(" = ")
    if ins == 'mask':
        curr_mask = value
        continue
    mem_add = ins[4:-1]
    bin_val = str(bin(int(int(mem_add))))[2::]
    zeroes = '0'*(36 - len(bin_val))
    bin_val = zeroes + bin_val
    new_val = ''
    for I in range(36):
        if curr_mask[I] in ['1','X']:
            new_val+=curr_mask[I]
            continue
        new_val+=bin_val[I]
    n = new_val.count('X')
    for I in range(2**n):
        temp_val = list(new_val)
        nos = ('0'*(n-len(bin(I)[2:]))) + bin(I)[2:]
        nos_index = 0
        for I in range(36):
            if curr_mask[I] == 'X':
                temp_val[I] = nos[nos_index]
                nos_index+=1
        temp_val = '1' + ''.join(temp_val).split('1',1)[1]
        mem_add = int(temp_val,2)
        mem[mem_add] = int(value)

print('Part2',sum(mem.values()))