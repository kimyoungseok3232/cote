c = []
for i in range(int(input())):
    c.append(int(input()))
c.sort(reverse=True)
i = -1
answer = [0, 0]
ed = min(42, len(c))
while i < ed-1 :
    i += 1
    if c[i] > 249: 
        answer[1] += 5
    elif c[i] > 199: 
        answer[1] += 4
    elif c[i] > 139: 
        answer[1] += 3
    elif c[i] > 99: 
        answer[1] += 2
    elif c[i] > 59: 
        answer[1] += 1
    answer[0] += c[i]
print(*answer)