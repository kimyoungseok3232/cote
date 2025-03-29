answer = 0

def dfs(target, val, numbers, now):
    global answer
    if now == len(numbers):
        if val == target: answer += 1
        return 0
    dfs(target, val+numbers[now], numbers, now+1)
    dfs(target, val-numbers[now], numbers, now+1)
    
def solution(numbers, target):
    dfs(target, 0, numbers, 0)
    return answer