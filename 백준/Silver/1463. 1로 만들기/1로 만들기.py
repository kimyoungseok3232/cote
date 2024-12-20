n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = min(dp[i//3]+i%3, dp[i//2]+i%2)+1
print(dp[n])