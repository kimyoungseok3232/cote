import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

start = 1
distance = [-1] * (n+1)
distance[start] = 0
q = [start]
while q:
    tq = []
    while q:
        node = q.pop()
        for neighbor, weight in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + weight
                tq.append(neighbor)
    q = tq

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
q = [start]
while q:
    tq = []
    while q:
        node = q.pop()
        for neighbor, weight in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + weight
                tq.append(neighbor)
    q = tq
print(max(distance))