import heapq, sys
input = sys.stdin.readline
h = []
for _ in range(int(input())):
    if (i:=int(input())): heapq.heappush(h, i)
    else: print(heapq.heappop(h) if h else 0)