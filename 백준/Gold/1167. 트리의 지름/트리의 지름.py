import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        ip = input().split()[:-1]
        start = int(ip[0])
        for end, weight in zip(map(int, ip[1::2]), map(int, ip[2::2])):
            graph[start].append((end, weight))

    def maxdist(start):
        distance = [-1] * (n+1)
        distance[start] = 0
        q = [start]
        while q:
            node = q.pop()
            for neighbor, weight in graph[node]:
                if distance[neighbor] == -1:
                    distance[neighbor] = distance[node] + weight
                    q.append(neighbor)
        max_dist = max(distance)
        max_idx = distance.index(max_dist)
        return max_dist, max_idx

    print(maxdist(maxdist(1)[1])[0])
solve()