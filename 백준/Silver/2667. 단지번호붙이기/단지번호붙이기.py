N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
num = 2 # 대신 입력할 수

# dfs 함수
def dfs(y, x, visited):
    visited[y][x] = True
    arr[y][x] = num

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        yy = y + dy
        xx = x + dx

        if yy < 0 or xx < 0 or yy >= N or xx >= N: continue

        if (visited[yy][xx] == False) and (arr[yy][xx] == 1):
            dfs(yy, xx, visited)
    return
# dfs 수행
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j, visited)
            num += 1

# 총 단지수 출력
print(num - 2)

# 개수 카운트, 리스트에 저장
c = []
for j in range(num - 2):
    cnt = 0
    for i in range(N):
        cnt += arr[i].count(j+2)
    c.append(cnt)

# 오름차순 정렬해서 출력
for i in sorted(c):
    print(i)
