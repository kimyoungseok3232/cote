str1 = input()
str2 = input()
dp = [0] * (len(str2)+1)
for i in range(len(str1)):
    tmp = 0
    for j in range(len(str2)):
        if tmp < dp[j]:
            tmp = dp[j]
            continue
        if str1[i] == str2[j]: dp[j] = tmp+1
print(max(dp))