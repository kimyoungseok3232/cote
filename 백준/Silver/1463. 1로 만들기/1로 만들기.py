n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    l = [dp[i-1]]
    if i%3==0: l.append(dp[i//3])
    if i%2==0: l.append(dp[i//2])
    dp[i] = min(l)+1
print(dp[n])