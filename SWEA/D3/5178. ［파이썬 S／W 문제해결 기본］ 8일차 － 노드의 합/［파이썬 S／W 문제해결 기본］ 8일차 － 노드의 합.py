T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    arr = [0] * (N+1)

    # 리프 노드 입력
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b

    for i in range(N):
        if arr[N-i] == 0:
            # 자식이 1개인 경우
            if 2 * (N-i) + 1 > N:
                arr[N - i] = arr[2 * (N - i)]
            else:
                arr[N-i] = arr[2 * (N-i)] + arr[2 * (N-i) + 1]

    print(f'#{tc} {arr[L]}')