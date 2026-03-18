T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 역 개수
    arr = list(map(int,input().split())) # 각 역의 이용자 수

    # 4개 중복 없이 선택
    path = []
    pick = []

    def rec(k, now, path):
        # 4개의 숫자를 다 고른 경우
        if k == 4:
            pick.append(path[:])
            return

        for i in range(now, N):
            path.append(i)
            rec(k+1, i+1, path)
            path.pop() # 백트래킹

    rec(0, 0, path)

    # 조건 확인 후, 제외 시키기
    ans = []

    for a, b, c, d in pick:
        # [1] 2개의 직통 노선은 서로 교차할 수 없다.
        # a-d / b-c or a-b / c-d 엮어주면 교차 안함

        # [2] 인접한 두 역을 연결하는 직통 노선은 건설할 수 없다.
        # [3]인접한 두 역에서 출발하거나, 인접한 두 역으로 도착하는 직통 노선은 건설할 수 없다.
        if b == a+1 or c == b+1 or d == c+1 or (a==0 and d==N-1): continue

        # [4] 1개의 역에 2개의 직통 노선이 있어서는 안 된다.
        # 이미 중복 허용 안되어 있음

        ans.append((a,b,c,d))

    # 타당도 최대값 찾기
    max_ans = 0

    for a, b, c, d in ans:
        tadang1 = (arr[a]+arr[d])**2 + (arr[b]+arr[c])**2
        tadang2 = (arr[a]+arr[b])**2 + (arr[c]+arr[d])**2
        max_ans = max(max_ans, tadang1, tadang2)

    print(f'#{tc} {max_ans}')