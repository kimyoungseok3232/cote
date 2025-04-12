def solution(topping):
    answer = 0
    dic = {}
    for top in topping:
        dic[top] = dic.get(top, 0) + 1
    visited = set()
    
    for top in topping:
        visited.add(top)
        dic[top] -= 1
        if dic[top] == 0: dic.pop(top)
        if len(dic) == len(visited): answer+=1
    
    return answer