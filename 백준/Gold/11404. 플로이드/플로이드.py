import sys
input = sys.stdin.readline
n, edge = int(input()), int(input())
def solve(n,edge):
    graph = [[10e8 if i!=j else 0 for i in range(n+1)] for j in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u][v] = min(graph[u][v], w)

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n+1):
        print(*map(lambda x: 0 if x == 10e8 else x, graph[i][1:]))
solve(n, edge)