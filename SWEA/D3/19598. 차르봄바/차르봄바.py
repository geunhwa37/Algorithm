T = int(input())

for tc in range(1, T+1):

    # 입력 처리
    N, P = map(int, input().split())

    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 방향 벡터
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    sumMax = 0

    # 완전 탐색
    for i in range(N):
        for j in range(N):
            virusSum = arr[i][j]
            for k in range(4):
                for a in range(1, P+1):
                    x = i + a*dx[k]
                    y = j + a*dy[k]

                    if (x < 0) or (x >= N) or (y < 0) or (y >= N):
                        continue

                    virusSum += arr[x][y]

            if sumMax < virusSum:
                sumMax = virusSum

    print(f'#{tc} {sumMax}')