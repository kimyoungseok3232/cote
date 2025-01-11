n = int(input())
def n_queen(row, cols, diags1, diags2):
    if row == n: return 1
    count = 0
    available = ((1 << n) - 1) & ~(cols | diags1 | diags2)
    while available:
        pos = available & -available
        available -= pos
        count += n_queen(
            row + 1,
            cols | pos,
            (diags1 | pos) << 1,
            (diags2 | pos) >> 1
        )
    return count
print(n_queen(0, 0, 0, 0))