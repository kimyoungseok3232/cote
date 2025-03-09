import sys
while (n:=input())!='0':
    l = len(n)//2
    front = sys.intern(n[:l])
    back = sys.intern(n[::-1][:l])
    if front == back:
        print('yes')
    else:print('no')