T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N = int(input()) # 하나의 정수
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    P = int(input()) # 하나의 정수
    C = []
    for _ in range(P):
        C.append(int(input()))

    # DAT 사용
    DAT = [0] * 5001

    for i in range(N):
        for j in range(A[i], B[i]+1):
            DAT[j] += 1

    print(f'#{tc}', end=' ')

    for i in C:
        print(DAT[i], end=' ')