n = int(input())
c = set([666]+[int(str(i)[:j]+'666'+str(i)[j:]) for i in range(min(2800,n)) for j in range(len(str(i))+1)])
for i in range(100): c.add(int('6660'+str(i)))
for i in range(10): c.add(int('66600'+str(i)))
c = sorted(list(c))
print(c[n-1])