def n_queen(n):
    def solve(row, cols, diags1, diags2):
        if row == n: return 1
        count = 0
        available = ((1 << n) - 1) & ~(cols | diags1 | diags2)
        while available:
            pos = available & -available
            available -= pos
            count += solve(
                row + 1,
                cols | pos,
                (diags1 | pos) << 1,
                (diags2 | pos) >> 1
            )
        return count
    return solve(0, 0, 0, 0)
print(n_queen(int(input())))