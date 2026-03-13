T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    def dfs(y,x, dep):
        global ans
        ans = max(ans, dep)

        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            yy = y + dy
            xx = x + dx

            if yy<0 or xx<0 or yy>=N or xx>=N: continue
            # 이동하려는 방의 숫자가 1 더 큰 경우
            if arr[yy][xx] == arr[y][x] + 1:
                dfs(yy, xx, dep+1)

    # 완전 탐색
    dir = []
    for i in range(N):
        for j in range(N):
            ans = 0
            dfs(i, j, 1)
            dir.append((ans, arr[i][j]))

    # 최대인 방이 여럿인 경우, 가장 작은 수를 출력
    ans_min = float('inf')
    dir.sort(key=lambda x:x[0])
    max_len = dir[-1][0]
    
    for a, b in dir:
        if a == dir[-1][0]:
            ans_min = min(ans_min, b)

    print(f'#{tc} {ans_min} {max_len}')