from collections import deque
for _ in range(int(input())):
    c, n = input(), input()
    l = deque(eval(input()))
    f = False
    for i in c:
        if i == 'R': f = not f
        elif l: 
            if f: l.pop()
            else: l.popleft()
        else: 
            print('error')
            break
    else: 
        if f: l.reverse()
        print(f'{list(l)}'.replace(' ', ''))