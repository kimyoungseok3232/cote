str1 = input()
str2 = input()
dp = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
res = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]: dp[j][i] = dp[j-1][i-1] + 1
        else: dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        res = max(res, dp[j][i])
print(res)