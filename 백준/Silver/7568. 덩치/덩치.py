n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
d = {}
for i in range(n):
    c = 1
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]: c+=1
    print(c, end=' ')