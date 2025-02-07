l = [1,1,1,2,2]
for _ in range(int(input())):
    n = int(input())
    while len(l) < n:
        l.append(l[-1]+l[-5])
    print(l[n-1])