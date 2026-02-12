arr = [[1, 5, 10, 15], [15, 15, 20, 30]]

n = int(input())

DAT = [0] * 31

for i in range(2):
    for j in range(4):
        DAT[arr[i][j]] += 1

print(DAT[n])