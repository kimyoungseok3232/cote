def s(n, o, r):
    t = [n] + d[n]
    for i in [t[o[0]],t[o[1]],t[o[2]]]:
        if i == n: r.append(i)
        elif i != '.': s(i, o, r)
    return r
d = {}
for _ in range(int(input())):
    p, l, r = input().split()
    d[p] = [l, r]
print(''.join(s('A', (0,1,2), [])))
print(''.join(s('A', (1,0,2), [])))
print(''.join(s('A', (1,2,0), [])))