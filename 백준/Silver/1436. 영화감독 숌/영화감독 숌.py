n = int(input())
c = set([666])
for i in range(10000):
    t = str(i)
    for j in range(len(t)+1):
        c.add(int(t[:j]+'666'+t[j:]))
for i in range(100): c.add(int('6660'+str(i)))
for i in range(10): c.add(int('66600'+str(i)))
c = sorted(list(c))
print(c[n-1])