n = int(input())
l = {0:0}
for i in map(int, input().split()):
    for j in range(len(l)-1,-1,-1):
        if l[j] < i :
            if j+1 not in l or l[j+1] > i :
                l[j+1] = i
                break
print(max(l))