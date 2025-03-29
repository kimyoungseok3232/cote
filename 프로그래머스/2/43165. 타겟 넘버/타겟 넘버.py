def dfs(target, val, numbers, now, ed, answer):
    if now == ed:
        if val == target: answer.append('C')
        return 0
    dfs(target, val+numbers[now], numbers, now+1, ed, answer)
    dfs(target, val-numbers[now], numbers, now+1, ed, answer)
    
def solution(numbers, target):
    answer = []
    
    dfs(target, 0, numbers, 0, len(numbers), answer)
    
    return len(answer)