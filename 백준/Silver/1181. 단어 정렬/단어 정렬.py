import sys
input = sys.stdin.readline
n = int(input())
w = sorted(list(set([input() for _ in range(n)])))
w.sort(key = lambda x: (len(x),x))
print(''.join(w))