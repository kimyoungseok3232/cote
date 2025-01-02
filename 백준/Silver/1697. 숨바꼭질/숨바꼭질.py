from collections import deque
n, k = map(int, input().split())
v = [True] * 100001
q = deque([(n, 0)])
while q:
    t, c = q.popleft()
    if t == k: break
    for i in [t+1, t*2, t-1]:
        if 0 <= i <= 100000 and v[i]:
            v[i] = False
            q.append((i, c+1))
print(c)