def solution(n, wires):
    answer = 100
    nodes = {i:[] for i in range(1, len(wires)+2)}
    for node1, node2 in wires:
        nodes[node1].append(node2)
        nodes[node2].append(node1)
    
    size = len(wires)+1
    stack = []
    for st, cut in wires:
        visited = [True] * (size+1)
        visited[cut] = False
        visited[st] = False
        stack.append(st)
        while stack:
            node = stack.pop()
            for i in nodes[node]:
                if visited[i]:
                    visited[i] = False
                    stack.append(i)
        count = abs(size-sum(visited)*2)
        if answer > count:
            answer = count
            
    return answer