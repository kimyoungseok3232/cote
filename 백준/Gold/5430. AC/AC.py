for _ in range(int(input())):
    c, n = input().split('R'), int(input())
    l = input().strip('[]').split(',')
    st, ed = len(''.join(c[::2])), n-len(''.join(c[1::2]))
    if st>ed: print('error')
    else: 
        l = l[st:ed]
        print(f'[{','.join(l if len(c)%2 else reversed(l))}]')