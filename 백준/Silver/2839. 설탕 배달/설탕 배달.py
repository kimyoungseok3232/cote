n = int(input())
if n%5 == 0: n//=5
elif n%5 == 1: n = 2+(n-6)//5
elif n%5 == 2: n = 4+(n-12)//5 if n > 11 else -1
elif n%5 == 3: n = 1+(n-3)//5
elif n%5 == 4: n = 3+(n-9)//5 if n > 8 else -1
print(n)