n, k = map(int, input().split())
y, p, l = [i+1 for i in range(n)], 0, []
while y: 
    p = (p+k-1)%len(y)
    l.append(f'{y.pop(p)}')
print(f'<{', '.join(l)}>')