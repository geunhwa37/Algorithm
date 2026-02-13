T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    
    # 완전 탐색
    for i in range(N):
        for j in range(N):
            # 죽은 파리 갯수 세기
            pari_sum = 0
            for k in range(M):
                for l in range(M):
                    y = i+k
                    x = j+l
                    if y < 0 or x < 0 or y >= N or x >= N: continue
                    pari_sum += arr[y][x]
            # 최댓값 구하기
            ans = max(ans, pari_sum)

    print(f'#{tc} {ans}')
