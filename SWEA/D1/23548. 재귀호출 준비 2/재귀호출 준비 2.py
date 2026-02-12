
def dfs(num):
    if len(num) == 4:
        print(*num)
        return

    for i in range(1, 4):
        dfs(num + str(i))

dfs("")
