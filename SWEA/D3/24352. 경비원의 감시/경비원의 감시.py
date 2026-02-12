T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    y, x = -1, -1

    # 경비원 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                y, x = i, j

    # 방향 벡터
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]


    for j in range(4):
        for i in range(1, N):
            yy = y + dy[j]*i
            xx = x + dx[j]*i

            if yy < 0 or xx < 0 or yy >= N or xx >= N:
                continue

            # 벽을 만날 경우, break
            if arr[yy][xx] == 1:
                break
            arr[yy][xx] = 3

    # 감시 못하는 칸의 개수 카운트
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')