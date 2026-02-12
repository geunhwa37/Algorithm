T = int(input())

for tc in range(1, T+1):
    # 2차원 배열 0 생성
    # 각 사각형 범위에 1,2 넣기
    # 2넣을때, 이미 존재하면 -> 1
    # 완전탐색 상하좌우에 2 존재 -> 2
    # 완전탐색 대각선에 2 존재 -> 3
    # 완전탐색 해당하지 않은 경우 -> 4
    def airview():
        x1_1, y1_1, x1_2, y1_2 = map(int, input().split())
        x2_1, y2_1, x2_2, y2_2 = map(int, input().split())

        arr = [[0] * 1001 for _ in range(1001)]

        # 1번째 직사각형 입력
        for i in range(y1_1, y1_2):
            for j in range(x1_1, x1_2):
                arr[i][j] = 1

        # 방향 벡터
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        dxx = [1, 1, -1, -1]
        dyy = [1, -1, 1, -1]

        # 2번째 직사각형 입력
        for i in range(y2_1, y2_2):
            for j in range(x2_1, x2_2):
                # 이미 존재하면 -> 1번 상태
                if arr[i][j] == 1:
                    return 1
                arr[i][j] = 2

        for i in range(y2_1, y2_2):
            for j in range(x2_1, x2_2):
                # 상하좌우 겹칠 경우 -> 2번 상태
                for k in range(4):
                    yy = i + dy[k]
                    xx = j + dx[k]

                    if xx < 0 or yy < 0 or xx >= 1001 or yy >= 1001: continue

                    if arr[yy][xx] == 1: return 2

                # 대각선 겹칠 경우 -> 3번 상태
                for k in range(4):
                    yy = i + dyy[k]
                    xx = j + dxx[k]

                    if xx < 0 or yy < 0 or xx >= 1001 or yy >= 1001: continue

                    if arr[yy][xx] == 1: return 3

        return 4

    print(f'#{tc} {airview()}')









