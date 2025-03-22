for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    xd, yd = x1-x2, y1-y2
    sd = xd*xd+yd*yd
    if sd == 0 and r1 == r2: print(-1)
    elif sd > r1*r1+r2*r2+2*r1*r2: print(0)
    elif sd == r1*r1+r2*r2+2*r1*r2: print(1)
    elif r1*r1+r2*r2-2*r1*r2 < sd < r1*r1+r2*r2+2*r1*r2: print(2)
    elif sd == r1*r1+r2*r2-2*r1*r2: print(1)
    elif sd < r1*r1+r2*r2-2*r1*r2: print(0)
   