empty = []
board = [list(map(int, input().split())) for _ in range(9)]
low = [set() for _ in range(9)]
col = [set() for _ in range(9)]
block = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j]!=0:
            low[i].add(board[i][j])
            col[j].add(board[i][j])
            block[i//3*3 + j//3].add(board[i][j])
        else: empty.append((i,j))

def backtracking(board, low, col, block):
    if len(empty)==0: return True
    i, j = empty.pop()
    check = low[i] | col[j] | block[i//3*3+j//3]
    for val in range(1,10):
        if val in check: continue
        board[i][j] = val
        low[i].add(val)
        col[j].add(val)
        block[i//3*3+j//3].add(val)
        if backtracking(board, low, col, block): return True
        board[i][j] = 0
        low[i].remove(val)
        col[j].remove(val)
        block[i//3*3+j//3].remove(val)
    empty.append((i,j))
    return False

backtracking(board, low, col, block)

for i in range(9):
    print(*board[i])