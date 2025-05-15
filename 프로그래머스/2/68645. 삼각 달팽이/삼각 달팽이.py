def d(answer, n, m, c, count):
    for i in range(c):
        n += 1
        count += 1
        answer[n][m] = count
    return n, m, count

def l(answer, n, m, c, count):
    for i in range(c):
        m += 1
        count += 1
        answer[n][m] = count
    return n, m, count

def u(answer, n, m, c, count):
    for i in range(c):
        n -= 1
        m -= 1
        count += 1
        answer[n][m] = count
    return n, m, count
            
        
def solution(n):
    tri = [[0]] + [[0]*i for i in range(1,n+1)]
    x, y, count = 0, 0, 0
    c = n
    for i in range(n,-1,-1):
        x, y, count = d(tri, x, y, c, count)
        x, y, count = l(tri, x, y, c-1, count)
        x, y, count = u(tri, x, y, c-2, count)
        c -= 3
    return sum(tri[1:],[])