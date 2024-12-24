import sys
input = sys.stdin.readline
print(''.join(sorted([input() for _ in range(int(input()))], key = lambda x: (int(x.split()[1]), int(x.split()[0])))))