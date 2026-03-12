from collections import deque

T = int(input())

# 터널 방향
pipe = {
    1: [(0,1), (0,-1), (1,0), (-1,0)],
    2: [(1,0), (-1,0)],
    3: [(0,1), (0,-1)],
    4: [(0,1), (-1,0)],
    5: [(0,1), (1,0)],
    6: [(0,-1), (1,0)],
    7: [(0,-1), (-1,0)]
}

for tc in range(1, T+1):

    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]

    q = deque()
    q.append((R, C))
    visited[R][C] = 1

    while q:
        y, x = q.popleft()

        if visited[y][x] == L:
            continue

        for dy,dx in pipe[arr[y][x]]:
            ny = y + dy
            nx = x + dx

            if ny<0 or nx<0 or ny>=N or nx>=M: continue
            if arr[ny][nx] == 0: continue
            if visited[ny][nx]: continue

            # 반대 방향 연결 확인
            if (-dy,-dx) in pipe[arr[ny][nx]]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] and visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')