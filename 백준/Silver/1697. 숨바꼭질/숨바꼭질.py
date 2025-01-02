from collections import deque
n, k = map(int, input().split())
v = [0] * 100001
q = deque([n])
while q:
    t = q.popleft()
    if t == k: break
    for i in [t+1, t-1, t*2]:
        if 0 <= i <= 100000 and v[i] == 0:
            v[i] = v[t] + 1
            q.append(i)
print(v[k])