T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    correct = list(map(int, input().split()))

    # 각 학생의 점수 배열
    score_arr = []

    for _ in range(N):
        score = 1
        n = 1 # 추가할 점수
        ans = list(map(int, input().split()))

        for i in range(M):
            if correct[i] == ans[i]:
                score += n
                n += 1
            else:
                n = 1

        score_arr.append(score)

    print(f'#{tc} {max(score_arr) - min(score_arr)}')
