T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    # 이진 탐색 함수
    def binary(A, b, l, r, last):

        # 종료 조건
        if l > r:
            return False

        # 이진 탐색
        if A[(l+r) // 2] > b:
            r = (l+r) // 2 - 1
            if last == True:
                return False
            else:
                last = True
            return binary(A, b, l, r, last)
        elif A[(l+r) // 2] == b:
            return True
        else:
            l = (l+r) // 2 + 1
            if last == False:
                return False
            else:
                last = False
            return binary(A, b, l, r, last)

    ans = 0

    for b in B:
        l = 0
        r = N - 1
        last = None # 번갈아 조건 구현

        result = binary(A, b, l, r, last)
        if result == True: ans += 1


    print(f'#{tc} {ans}')
