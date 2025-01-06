import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = input()
    v = [0, 0, 0, 0]
    for i in zip(map(int,input().split()),map(int,input().split())):
        tmp1, tmp2 = v[0], v[1]
        v[0], v[1] = max(v[1], v[3]) + i[0], max(v[0], v[2]) + i[1]
        v[2], v[3] = tmp1, tmp2
    print(max(v))