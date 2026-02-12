
def dfs(x):
    # 기저 조건
    if len(x) == 3:
        print(*x)
        return
    else:
        for i in range(1, 7):
            dfs(x + str(i))


dfs("")

