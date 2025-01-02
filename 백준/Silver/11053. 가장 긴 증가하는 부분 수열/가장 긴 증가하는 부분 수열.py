n = int(input())
l = {0:0}
for i in map(int, input().split()):
    for j in list(l.keys()):
        if j < i : 
            if i in l and l[i] > l[j]: continue
            l[i] = l[j]+1
print(max(l.values()))