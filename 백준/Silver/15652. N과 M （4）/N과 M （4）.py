n, m = map(int, input().split())

def backtracking(n, m, ls, depth, last):
    if depth == m: 
        print(" ".join(ls))
        return
    for i in range(last, n):
        ls.append(str(i+1))
        backtracking(n, m, ls, depth+1, i)
        ls.pop()

backtracking(n, m, [], 0, 0)