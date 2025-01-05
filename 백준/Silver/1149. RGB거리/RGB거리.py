import sys
input = sys.stdin.readline
v = [0, 0, 0]
for _ in range(int(input())):
    c = list(map(int, input().split()))
    v[0], v[1], v[2] = min(v[1], v[2]) + c[0], min(v[0], v[2]) + c[1], min(v[0], v[1]) + c[2]
print(min(v))