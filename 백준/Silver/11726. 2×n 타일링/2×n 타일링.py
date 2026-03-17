n = int(input()) # 2xn 크기의 직사각형

dp = [0] * (n+1)

dp[1] = 1
if n >= 2: dp[2] = 2

for i in range(3, n+1):
    # 맨 오른쪽 - 세로타일 1개 놓기 + 가로 2개 놓기
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)