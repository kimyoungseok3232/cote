import sys
print = sys.stdout.write
m, n = map(int, input().split())
t = []
for i in range(2, m):
    for j in t: 
        if i**(1/2) < j:
            t.append(i)
            break
        elif i % j == 0: break
    else: t.append(i)

for i in range(max(2,m), n+1):
    for j in t: 
        if i**(1/2) < j:
            t.append(i)
            print(f'{i}\n')
            break
        elif i % j == 0: break
    else: 
        t.append(i)
        print(f'{i}\n')