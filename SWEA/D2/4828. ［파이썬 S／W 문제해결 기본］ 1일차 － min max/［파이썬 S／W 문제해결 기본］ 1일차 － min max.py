T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최댓값고 최솟값의 차
    ans = max(arr) - min(arr)

    print(f'#{tc} {ans}')
