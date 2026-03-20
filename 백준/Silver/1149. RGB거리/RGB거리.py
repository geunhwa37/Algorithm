N = int(input())  # 집의 수
arr = [0] + [list(map(int, input().split())) for _ in range(N)] # 빨강, 초록, 파랑으로 칠하는 비용

dp = [[0, 0, 0] for _ in range(N+1)]

dp[1] = arr[1][:]

# 점화식
for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[N]))