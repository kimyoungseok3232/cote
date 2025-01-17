import sys
from heapq import heappop, heappush
input = sys.stdin.readline
def search(n, graph, end):
    dist = [10e9] * (n + 1)
    dist[end] = 0
    heap = [(0, end)]
    while heap:
        current_dist, node = heappop(heap)
        if current_dist > dist[node]: continue
        for v, w in graph[node]:
            if current_dist + w < dist[v]:
                dist[v] = current_dist + w
                heappush(heap, (dist[v], v))
    return dist

def solve():
    n, edge, end = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reverse_graph[v].append((u, w))

    end_to = search(n, graph, end)
    to_end = search(n, reverse_graph, end)

    print(max(map(lambda x: end_to[x]+to_end[x], range(1, n+1))))
solve()