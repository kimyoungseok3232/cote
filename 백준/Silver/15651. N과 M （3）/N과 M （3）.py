n, m = map(int, input().split())

def backtracking(n, m, ls, depth):
    if depth == m: 
        print(" ".join(ls))
        return
    for i in range(n):
        ls.append(str(i+1))
        backtracking(n, m, ls, depth+1)
        ls.pop()

backtracking(n, m, [], 0)