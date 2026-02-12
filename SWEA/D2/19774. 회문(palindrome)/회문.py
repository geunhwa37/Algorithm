T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{tc}', end=' ')

    # 현재 인덱스와 인덱스 + M - 1이 같을 경우, 회문 검사
    findd = False

    # 가로 검사
    for i in range(N):
        for j in range(N - M + 1):
            new_j = j + M - 1

            if arr[i][j] == arr[i][new_j]:
                if arr[i][j:new_j + 1] == arr[i][j:new_j + 1][::-1]:
                    print(arr[i][j:new_j + 1])
                    findd = True
                    break
        if findd:
            break

    # 세로 검사
    if not findd:
        for j in range(N):
            for i in range(N - M + 1):
                new_i = i + M - 1

                if arr[i][j] == arr[new_i][j]:
                    col = ''.join(arr[x][j] for x in range(i, new_i + 1))
                    if col == col[::-1]:
                        print(col)
                        findd = True
                        break
            if findd:
                break


