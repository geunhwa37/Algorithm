T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split()) # 점원 수, 선반 높이

    arr = list(map(int, input().split())) # 각 점원의 키

    path = []
    ans = float('inf')

    # depth : N명의 점원을 검토(N)
    # branch : 집합에 현재 원소가 포함 O X (2가지)
    def rec(now, i):
        global ans

        # 종료 조건 - 탑의 높이에 도달한 경우
        if now >= B:
            ans = min(ans, now-B)
            return

        for j in range(i, N):
            rec(now + arr[j], j+1)

    rec(0, 0)

    print(f'#{tc} {ans}')