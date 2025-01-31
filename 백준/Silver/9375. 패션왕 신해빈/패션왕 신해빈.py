for _ in range(int(input())):
    d = {}
    for _ in range(int(input())):
        k = input().split()[1]
        d[k] = d.get(k, 1) + 1

    total = 1
    for count in d.values():
        total *= count

    print(total - 1)