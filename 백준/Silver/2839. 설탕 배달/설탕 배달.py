n = int(input())
d = [0,1,2,1,2]
if n%5 == 0: n//=5
elif n%5 == 2: n = 2+n//5 if n > 11 else -1
elif n%5 == 4: n = 2+n//5 if n > 8 else -1
else: n = 1+n//5
print(n)