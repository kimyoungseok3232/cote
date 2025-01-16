import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, edge = int(input()), int(input())
graph = [[] for _ in range(n+1)]
for i in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

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

    print(*map(lambda x: 0 if x == 10e9 else x, dist[1:]))