L = [1,12,0,20,8,16]
D = {L[I] : (I+1,) for I in range(len(L))}

turn = 6
curr_no = 16
while turn!=30000000:
    if turn == 2020:
        print('Part1',curr_no)
    turn += 1
    if len(D[curr_no]) == 1:
        if D[curr_no][0] == turn - 1:
            curr_no = 0
            try:
                D[curr_no]+=(turn,)
            except:
                D[curr_no]=(turn,)
            continue
        else:
            D[curr_no] += (turn,)
            continue
    if len(D[curr_no]) == 2:
        temp = D[curr_no][1]-D[curr_no][0]
        D[curr_no] = (turn-1,)
        try:
            D[temp] += (turn,)
        except:
            D[temp] = (turn,)
        curr_no = temp
        continue
print('Part2',curr_no)