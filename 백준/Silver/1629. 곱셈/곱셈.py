a,b,c = map(int, input().split())
l = [a]
for i in range(31): l.append(l[i]**2%c)
b = f'{b:b}'
r = 1
for i in range(len(b)): 
    if b[-i-1] == '1': r = r*l[i]%c
print(r%c)