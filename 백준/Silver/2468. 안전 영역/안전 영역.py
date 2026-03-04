from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# bfs
def bfs(n, y, x, visited):
    visited[y][x] = 1
    queue = deque([(y, x)])

    while queue:
        b, a = queue.popleft()

        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            yy = b + dy
            xx = a + dx

            if yy<0 or xx<0 or yy>=N or xx>=N: continue
            # 물에 잠기는 지점 제외
            if arr[yy][xx] > n and not visited[yy][xx]:
                queue.append((yy,xx))
                visited[yy][xx] = 1

# 안전영역 개수 구하기 함수
def safe(n):
    # visited 초기화
    visited = [[0]*N for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > n and not visited[i][j]:
                bfs(n, i, j, visited)
                cnt += 1
    return cnt

# 깊이별 안전 영역 개수 최댓값 구하기
dep_max = 0
for i in range(1, 101):
    dep_max = max(dep_max, safe(i))

if dep_max == 0: print(1)
else:
    print(dep_max)