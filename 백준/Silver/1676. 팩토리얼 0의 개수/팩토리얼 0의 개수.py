n = int(input())
d, r = 5, 0
while n//d: d, r = d*5, r+n//d
print(r)