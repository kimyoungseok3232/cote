import sys
input = sys.stdin.readline
print = sys.stdout.write
A=int(input())
user = []
for _ in range(A):
    age, name = input().strip().split()
    user.append([int(age),name])

for i in sorted(user,key=lambda x : x[0]):
    print(f'{i[0]} {i[1]}\n')