from collections import deque
n = int(input())
mat = [deque(map(int,input().split())) for _ in range(n)]
for _ in range(int(input())):
    command = list(map(int, input().split()))
    if command[0] == 1:
        mat[command[1]-1].rotate()
    else:
        tmp = [deque([0]*n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp[j][n-i-1] = mat[i][j]
        mat = tmp
for i in range(n):
    print(*mat[i])