def solution(n):
    answer = 0
    for i in range(1,n+1,2):
        if n%i == 0: answer+=1
    return answer
# (end-start+1)(end+start)/2