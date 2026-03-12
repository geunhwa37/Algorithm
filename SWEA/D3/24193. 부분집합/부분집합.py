arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
visited = [0] * 10

ans = []

def rec(n, now):
    # 종료 조건
    if now == 10:
        ans.append(visited[:])
        return

    for i in range(n, 10):
        # 가지 치기
        if now + arr[i] > 10: continue

        visited[i] = 1
        rec(i + 1, now + arr[i])
        visited[i] = 0

rec(0, 0)

# 출력
for a in ans:
    for i in range(10):
        if a[i] == 1: print(arr[i], end=' ')
    print()
