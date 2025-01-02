n = int(input())
l = {0:0}
for i in map(int, input().split()):
    for j in list(l.keys()):
        if j < i : 
            if not (i in l and l[i] > l[j]): l[i] = l[j]+1
print(max(l.values()))