import re
f = open('input.txt', 'r')
L  = f.read().splitlines()
fields,my_ticket,tickets = L[:L.index(''):],L[L.index('')+1:L.index('')+3:],L[L.index('')+5::]
ranges = [re.split(': | or ',I) for I in fields]

err_rate = 0
inv = []
for tickett in tickets:
    ticket = [int(I) for I in tickett.split(',')]
    for field in ticket:
        valid = False
        for r in ranges:
            r1 = [int(I) for I in r[1].split('-')]
            r2 = [int(I) for I in r[2].split('-')]
            c1 = eval(f'field in range(r1[0],r1[1])')
            c2 = eval(f'field in range(r2[0],r2[1])')
            if True in [c1,c2]:
                valid = True
                break
        if valid == False:
            err_rate += field
            inv.append(tickets.index(tickett))
            break

print('Part1',err_rate)