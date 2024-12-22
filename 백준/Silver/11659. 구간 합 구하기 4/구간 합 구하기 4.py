import sys
input = sys.stdin.readline
print = sys.stdout.write
v = [0]
def p(x):
    v[0] += int(x)
    return v[0]
n, m = map(int, input().split())
l = [0]+list(map(p, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    print(f'{l[b]-l[a-1]}\n')