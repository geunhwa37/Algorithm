crime = [[5, 7, 9, 55],[30, 10, 6, 8]]
apart = [[1,2,3,4],[5,7,10,15]]

DAT = [0]*56

for c in crime:
    for d in c:
        DAT[d] = 1

ans = 0
apart_ans = 0

for i in apart:
    for j in i:
        if DAT[j] == 1:
            ans += 1
        else: apart_ans += 1


print(f'{ans} {apart_ans}')