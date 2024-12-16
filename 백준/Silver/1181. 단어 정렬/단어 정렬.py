import sys
input = sys.stdin.readline
n = int(input())
words = sorted(list(set([input() for _ in range(n)])))
words.sort(key = lambda x: (len(x),x))
print(''.join(words))