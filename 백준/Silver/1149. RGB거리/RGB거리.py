import sys
input = sys.stdin.readline
mr, mg, mb = 0, 0, 0
for _ in range(int(input())):
    r, g, b = map(int, input().split())
    mr, mg, mb = min(mg, mb) + r, min(mr, mb) + g, min(mr, mg) + b
print(min(mr, mg, mb))