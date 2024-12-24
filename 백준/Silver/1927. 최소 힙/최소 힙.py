import heapq, sys
input = sys.stdin.readline
print = sys.stdout.write
h = []
for _ in range(int(input())):
    if (i:=int(input())): heapq.heappush(h, i)
    else: print(f'{heapq.heappop(h)}\n' if h else '0\n')