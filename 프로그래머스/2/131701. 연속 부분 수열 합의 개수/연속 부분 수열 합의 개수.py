def solution(elements):
    visited = set(elements)
    for i in range(2,1+len(elements)):
        ssum = sum(elements[0:i])
        visited.add(ssum)
        for j in range(len(elements)):
            ssum += elements[(j+i)%len(elements)]-elements[j]
            visited.add(ssum)
        
    return len(visited)