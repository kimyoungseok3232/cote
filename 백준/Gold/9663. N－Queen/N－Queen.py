n = int(input())
res = [0]
row = [0] * n
def lay_queen(num_queen):
    if num_queen == n: res[0] += 1
    else:
        for i in range(n):
            for j in range(num_queen):
                if i == row[j] or abs(i-row[j]) == abs(num_queen-j): break
            else:
                row[num_queen] = i
                lay_queen(num_queen+1)
lay_queen(0)
print(res[0])