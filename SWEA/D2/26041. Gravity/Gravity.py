T = int(input())

for tc in range(T):
    garo = int(input())
    arr = list(map(int, input().split()))

    ans = 0

    # 오른쪽 숫자가 자신보다 작은 숫자일 경우 카운트
    for i in range(garo):
        cnt = 0
        for j in range(i+1, garo):
            if arr[i] > arr[j]:
                cnt += 1

        if cnt > ans:
            ans = cnt

    print(f'#{tc+1} {ans}')

