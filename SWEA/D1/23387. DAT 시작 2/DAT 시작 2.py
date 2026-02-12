text = 'ABCDE'

arr = list(input().split())

DAT = [0] * 100

for t in text:
    DAT[ord(t)] = 1

for a in arr:
    if DAT[ord(a)] == 1:
        print('O', end=' ')
    else:
        print('X', end=' ')