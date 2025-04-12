def solution(topping):
    answer = 0
    tmp = []
    visited = set()
    for top in topping:
        visited.add(top)
        tmp.append(len(visited))
    tmp.pop()
    visited = set()
    for idx, top in enumerate(topping[::-1]):
        visited.add(top)
        if tmp[-1-idx] == len(visited): answer += 1
        elif tmp[-1-idx] < len(visited): break 
    return answer