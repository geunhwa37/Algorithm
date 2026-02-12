N = int(input())

def dfs(now, N, k):
    # 종료 조건
    if len(now) == N:
        print(*now)
        return

    for i in range(k, 7):
        dfs(now+str(i), N, i)

dfs("", N, 1)