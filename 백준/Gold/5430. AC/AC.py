for _ in range(int(input())):
    c, n = input().split('R'), input()
    l = eval(input()) + [0]
    st, ed = len(''.join(c[::2])), -1-len(''.join(c[1::2]))
    if st-ed > len(l): print('error')
    else: 
        l = l[st:ed]
        if not len(c)%2: l.reverse()
        print(f'{l}'.replace(' ', ''))