def p(a): return ord(a)-ord('a')+1
n, s, res = input(), map(p, input()), 0
for i, a in enumerate(s): res += a*(31**i)%1234567891
print(res%1234567891)