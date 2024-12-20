N, r, c = map(int, input().split())
print(int('0'.join(list(f'{r:b}'))+'0',2)+int('0'.join(list(f'{c:b}')),2))