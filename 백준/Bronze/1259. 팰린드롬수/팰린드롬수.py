while (n:=input())!='0':
    l = len(n)//2
    for i in range(l):
        if n[i] != n[-i-1]:
            print('no')
            break
    else: print('yes')