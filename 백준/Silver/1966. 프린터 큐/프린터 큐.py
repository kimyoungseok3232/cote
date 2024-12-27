import sys
from collections import deque
input = sys.stdin.readline
for i in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    r = 1
    v = q.index(max(q))
    m = (m-v)%len(q)
    q.rotate(-v)
    q.popleft()
    while m: 
        r += 1
        v = q.index(max(q))
        m = (m-1-v)%len(q)
        q.rotate(-v)
        q.popleft()
    print(r)