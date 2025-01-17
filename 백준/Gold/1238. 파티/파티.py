import sys
from heapq import heappop, heappush
input = sys.stdin.readline
def solve():
    n, edge, end = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(edge):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    to_end = [0] * (n + 1)

    for start in range(1, n+1):
        dist = [10e9] * (n + 1)
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            current_dist, node = heappop(heap)
            if current_dist > dist[node]: continue
            for v, w in graph[node]:
                if current_dist + w < dist[v]:
                    dist[v] = current_dist + w
                    heappush(heap, (dist[v], v))

        if start == end: end_to = dist
        else: to_end[start] = dist[end]    
    print(max(end_to[x]+to_end[x] for x in range(1, n+1)))
solve()