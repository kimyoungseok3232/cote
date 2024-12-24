import heapq, sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    i = int(input())
    if i: heapq.heappush(h, i)
    else: print(heapq.heappop(h) if h else 0)