n, m = map(int, input().split())

def backtracking(n, m, ls, depth, visit):
    if depth == m: 
        print(" ".join(ls))
        return
    for i in range(n):
        if i+1 in visit: continue
        visit.add(i+1)
        ls.append(str(i+1))
        backtracking(n, m, ls, depth+1, visit)
        visit.remove(i+1)
        ls.pop()

backtracking(n, m, [], 0, set())