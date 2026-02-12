from collections import deque

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로길이, 세로길이, 배추 개수

    # 배추밭 입력
    arr = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())

        arr[y][x] = 1

    cnt = 0

    # bfs 함수
    def bfs(b, a, arr):
        queue = deque([(b, a)])
        arr[b][a] = 2

        while queue:
            yy, xx = queue.popleft()

            for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                y = yy + dy
                x = xx + dx

                if y < 0 or x < 0 or y >= N or x >= M: continue
                if arr[y][x] == 1:
                    arr[y][x] = 2
                    queue.append((y, x))


    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j, arr)
                cnt += 1

    print(cnt)