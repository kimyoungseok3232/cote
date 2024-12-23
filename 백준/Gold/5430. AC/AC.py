for _ in range(int(input())):
    c, n = input().split('R'), int(input())
    l = input().strip('[]').split(',')
    st, ed = len(''.join(c[::2])), n-len(''.join(c[1::2]))
    if st>ed: print('error')
    else: 
        l = l[st:ed]
        if not len(c)%2: l.reverse()
        print(f'[{','.join(l)}]')