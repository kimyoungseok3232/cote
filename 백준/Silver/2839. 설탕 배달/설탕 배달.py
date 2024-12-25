n = int(input())
d = [0,1,2,1,2]
if n%5 == 0: n//=5
elif n%5%2: n = 1+n//5
elif n > 7: n = 2+n//5
else: n = -1
print(n)