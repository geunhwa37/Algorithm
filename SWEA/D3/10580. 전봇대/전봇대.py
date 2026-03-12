T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []

    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()  # A 기준 정렬

    cnt = 0

    for i in range(N):
        for j in range(i+1, N):
            if arr[i][1] > arr[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')