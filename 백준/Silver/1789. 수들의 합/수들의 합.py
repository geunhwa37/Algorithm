S = int(input())
s_um = 0
N = 0

for i in range(1, S+1):
    s_um += i
    if s_um <= S:
        N += 1
    else:
        break

print(N)

