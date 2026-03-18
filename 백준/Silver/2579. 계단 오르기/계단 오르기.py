n = int(input()) # 계단의 개수

score = [0] # 계단 점수
for _ in range(n):
    score.append(int(input()))

dp = [0] * (n+1)

dp[1] = score[1]

if n >= 2:
    dp[2] = score[1] + score[2]
if n >= 3:
    dp[3] = max(score[1] + score[3], score[2] + score[3])
    
    for i in range(4, n+1):
        # 두칸 전 + 지금꺼, 3칸 전 + 1칸 전 + 지금꺼
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
    

print(dp[n])