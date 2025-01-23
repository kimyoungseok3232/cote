import sys
input = sys.stdin.readline
def find_minus_loop(node, edges, dist):    
    for i in range(node):
        for st, ed, w in edges:
            if dist[st] + w < dist[ed]:
                dist[ed] = dist[st] + w
                if i == node-1: 
                    return 'YES'
    return 'NO'

for i in range(int(input())):
    node, edge, hole = map(int, input().split())
    edges = []
    dist = [10e8] * (node+1)
    dist[1] = 0
    for _ in range(edge):
        s, e, t = map(int, input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    for _ in range(hole):
        s, e, t = map(int, input().split())
        edges.append((s,e,-t))
    
    print(find_minus_loop(node, edges, dist))