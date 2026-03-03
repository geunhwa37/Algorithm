from collections import deque

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

# 처음 익은 토마토 전부 큐에 넣기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                queue.append((i,j,k))

# 6방향
dirs = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]

# bfs
while queue:
    z,y,x = queue.popleft()

    for dz,dy,dx in dirs:
        zz = z+dz
        yy = y+dy
        xx = x+dx

        if 0<=zz<H and 0<=yy<N and 0<=xx<M:
            if arr[zz][yy][xx] == 0:
                arr[zz][yy][xx] = arr[z][y][x] + 1
                queue.append((zz,yy,xx))

ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            ans = max(ans, arr[i][j][k])

print(ans-1)