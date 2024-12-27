import sys
from collections import deque
input = sys.stdin.readline
for i in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    r = 1
    m += 1
    while m:=(m-1-q.index(max(q)))%len(q): 
        q.rotate(-q.index(max(q)))
        q.popleft()
        r += 1
    print(r)