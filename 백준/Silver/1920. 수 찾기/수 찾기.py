import sys
print = sys.stdout.write
n, nlist, m = input(), set(input().split()), input()
[print('1\n' if x in nlist else '0\n') for x in input().split()]
