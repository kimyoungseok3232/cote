import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, a, b = int(input()), 0, 1
    for j in range(n): a, b = b, a+b
    print(b-a, a)