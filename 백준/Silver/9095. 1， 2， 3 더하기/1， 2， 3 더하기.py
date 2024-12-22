n = int(input())
d = [1, 2, 4]
for i in range(n):
    v = int(input())
    if len(d)<v:
        for i in range(v-len(d)):
            d.append(d[-1]+d[-2]+d[-3])
    print(d[v-1])