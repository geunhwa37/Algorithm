T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split()) # 점원 수, 선반 높이

    arr = list(map(int, input().split())) # 각 점원의 키

    path = []
    ans = float('inf')

    def rec(now, i):
        global ans

        # 종료 조건 - 탑의 높이에 도달한 경우
        if now >= B:
            ans = min(ans, now-B)
            return

        for j in range(i, N):
            path.append(arr[j])
            rec(now + arr[j], j+1)
            path.pop()

    rec(0, 0)

    print(f'#{tc} {ans}')