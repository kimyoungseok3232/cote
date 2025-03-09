while (n:=input())!='0':
    l = len(n)//2
    if n[:l] == n[::-1][:l]:
        print('yes')
    else:print('no')