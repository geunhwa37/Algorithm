T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # Sample의 길이, PassCode의 길이

    s = list(map(int, input().split())) # Sample
    p = list(map(int, input().split()))  # PassCode

    print(f'#{tc}', end=' ')

    def passcode(K, N, s, p):
        start = 0

        for i in range(K):
            for j in range(start, N):
                if s[j] == p[i]:
                    start = j + 1
                    break
                else:
                    continue
            else:
                return 0
        return 1

    print(passcode(K,N,s,p))
