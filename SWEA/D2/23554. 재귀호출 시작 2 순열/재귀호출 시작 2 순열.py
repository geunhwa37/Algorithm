
n = int(input())


def dfs(x, n):
    # 기저 조건
    if len(x) == n:
        print(*x)

    for i in range(1, 7):
        # 이미 존재할 경우 제외
        if str(i) not in x:
            dfs(x+str(i), n)




dfs("", n)