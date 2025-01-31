import sys
input = sys.stdin.readline
n, k = map(int, input().split())
pw_dic = {link: password for _ in range(n) for link, password in [input().rstrip().split()]}
print('\n'.join([pw_dic[input().rstrip()] for _ in range(k)]))