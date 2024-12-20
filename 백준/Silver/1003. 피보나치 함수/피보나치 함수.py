for _ in range(int(input())):
    n = int(input())
    a, b = 0, 1
    for j in range(n):
        a, b = b, a+b
    print(b-a, a)