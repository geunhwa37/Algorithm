n = int(input())
cnt = 0

def dfs(x, n):
    global cnt

    # 종료 조건
    if len(x) == n:
        if sum(x) <= 10:
            cnt += 1
        return

    for i in range(1, 7):
        x.append(i)
        dfs(x, n)
        x.pop() # 리스트의 경우 pop 필수!

dfs([], n)
print(cnt)
