a,b,c = map(int, input().split())
r = 1
while b:
    if b%2: r = r*a%c
    a = a*a%c
    b //= 2
print(r)