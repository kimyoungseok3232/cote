import sys
input = sys.stdin.readline
n = int(input())
words = set()
for i in range(n):
    words.add(input().strip())
words = sorted(list(words),key = lambda x: (len(x),x))
print('\n'.join(words))