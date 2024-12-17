n = int(input())
for i in range(n):
    o = 0
    for j in input():
        if j == '(': o += 1
        else: 
            o -= 1
            if o < 0: 
                print('NO')
                break
    else: 
        if o: print('NO')
        else: print('YES')