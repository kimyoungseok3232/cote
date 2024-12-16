n = int(input())
c, i = 0, 0
while c != n:
    if i%10 != 6:
        t = i*1000 + 666
        c += 1
    else:
        six, tmp = 1, i
        while tmp%10 == 6:
            six *= 10
            tmp //= 10
        
        for j in range(six):
            t = i*1000 + 666//six*six + j
            c += 1
            if c == n: break
    i += 1
print(t)