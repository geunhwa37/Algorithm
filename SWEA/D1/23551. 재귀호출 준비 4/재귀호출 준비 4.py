def dfs(x):
    if x > 2: return

    dfs(x + 1)
    dfs(x + 1)
    print(x)

dfs(0)