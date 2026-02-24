T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 돌의 수, 뒤집기 횟수
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split()) # i번 째 돌을 사이에 두고, 마주보는 j개의 돌에 대해
        
        # 인덱스 맞춰주기 
        i -= 1

        for x in range(1, j+1):
            if i-x < 0 or i+x >= N: break
            if arr[i+x] == arr[i-x]:
                if arr[i+x] == 1:
                    arr[i+x] = 0
                    arr[i - x] = 0
                else:
                    arr[i + x] = 1
                    arr[i - x] = 1
    print(f'#{tc}', end=' ')
    print(*arr)