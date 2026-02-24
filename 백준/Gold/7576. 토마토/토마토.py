from collections import deque

M, N = map(int, input().split()) # 상자의 가로칸 수, 세로칸 수

arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
# 멀티 시작 BFS -> 시작점 전부 넣기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))

# BFS 한 번만
while queue:
    y, x = queue.popleft()

    for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
        yy = y + dy
        xx = x + dx
        # 상하좌우 토마토 영향
        if 0 <= yy < N and 0 <= xx < M:
            if arr[yy][xx] == 0:
                # 거리로 일수 계산
                arr[yy][xx] = arr[y][x] + 1
                queue.append((yy, xx))

# 결과 확인
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, arr[i][j])

print(ans - 1)
