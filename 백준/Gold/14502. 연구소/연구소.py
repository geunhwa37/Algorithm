from collections import deque
from itertools import combinations

N, M = map(int, input().split())    # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
empty = []

# 바이러스, 빈 칸 기록
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            empty.append((i,j))

# bfs
def bfs(new_arr):
    queue = deque()
    # 모든 바이러스 시작
    for i, j in virus:
        queue.append((i,j))

    while queue:
        y, x = queue.popleft()
        new_arr[y][x] = 2
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            yy = y + dy
            xx = x + dx
            if yy<0 or xx<0 or yy>=N or xx>=M or new_arr[yy][xx] == 1 or new_arr[yy][xx] == 2: continue
            queue.append((yy, xx))

    # 안전 영역 크기 카운트
    cnt = 0
    for i in range(N):
        cnt += new_arr[i].count(0)
    return cnt

ans = 0
# 조합
for comb in combinations(empty, 3):
    tmp = [row[:] for row in arr] # 깊은 복사

    for y,x in comb:
        tmp[y][x] = 1

    # 최댓값 구하기
    ans = max(ans, bfs(tmp))

print(ans)