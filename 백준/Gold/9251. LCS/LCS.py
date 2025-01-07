str1 = input()
str2 = input()
dp = [0] * (len(str2)+1)
for i in range(len(str1)):
    tmp = dp.copy()
    for j in range(len(str2)):
        if str1[i] == str2[j]: dp[j] = tmp[j-1]+1
        else: dp[j] = max(tmp[j], dp[j-1])
print(max(dp))