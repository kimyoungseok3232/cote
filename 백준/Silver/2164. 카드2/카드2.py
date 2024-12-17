from collections import deque
q = deque(i+1 for i in range(int(input())))
while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q.pop())