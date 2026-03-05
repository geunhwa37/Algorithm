T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    def bin(N):
        for i in range(N):
            if M & (1 << i): continue
            else:
                return 'OFF'
        return 'ON'

    print(f'#{tc} {bin(N)}')