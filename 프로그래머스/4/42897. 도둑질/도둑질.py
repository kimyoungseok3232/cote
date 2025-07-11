def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    dp1[0] = money[0]
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    dp2[-1] = max(dp2[-3], dp2[-4]) + money[-1]
    
    return max(dp1[-1], dp1[-2], dp2[-1], dp2[-2])