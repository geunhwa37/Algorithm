T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # boolean 배열로 전환
    for i in range(N):
        if arr[i] == 1:
            arr[i] = True
        else:
            arr[i] = False

    def light(n):
        on = [n] * N

        if n == True:
            cnt_on = 1 # 킨 상태로 시작하는 경우
        else: cnt_on = 0  # 끈 상태로 시작하는 경우

        for i in range(N):
            # 같지 않은 경우 스위치
            if arr[i] != on[i]:
                # 배수만큼 전환
                for j in range(i, N, i+1):
                    on[j] = not(on[j])
                cnt_on += 1

                # 맞는지 확인
                for k in range(N):
                    if arr[k] != on[k]:
                        break
                else:
                    return cnt_on
        # 불가능한 경우
        return float('inf')

    ans = min(light(True), light(False))


    print(f'#{tc} {ans}')
