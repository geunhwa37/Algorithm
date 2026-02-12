
def dfs(x):
    # 기저 조건
    if x > 5: return

    print(x, end=' ')
    dfs(x+1) # 재귀 호출
    print(x, end=' ')

dfs(0)