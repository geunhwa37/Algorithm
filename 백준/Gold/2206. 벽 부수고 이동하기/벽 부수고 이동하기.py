from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque([(0,0,0)])  # y,x,벽부쉈는지
    visited[0][0][0] = 1

    while queue:
        y, x, wall = queue.popleft()

        if y == N-1 and x == M-1:
            return visited[y][x][wall]

        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            yy = y + dy
            xx = x + dx

            if 0 <= yy < N and 0 <= xx < M:

                # 이동 가능 - 벽이 아니고, 방문하지 않았을 경우
                if arr[yy][xx] == 0 and not visited[yy][xx][wall]:
                    visited[yy][xx][wall] = visited[y][x][wall] + 1
                    queue.append((yy,xx,wall))

                # 벽인데 아직 안부쉈다면
                if arr[yy][xx] == 1 and wall == 0:
                    visited[yy][xx][1] = visited[y][x][wall] + 1
                    queue.append((yy,xx,1))

    return -1

print(bfs())