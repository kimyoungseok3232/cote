d = {1:0, 2:1, 3:1}
def dp(n):
    if n in d: return d[n]
    return min(dp(n//3)+n%3, dp(n//2)+n%2) + 1
print(dp(int(input())))