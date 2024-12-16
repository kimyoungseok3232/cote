h, w = map(int, input().split())
map = [list(input()) for _ in range(h)]
cal = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if (i+j)%2 == 0 and map[i][j] == 'W': map[i][j] = 0
        elif (i+j)%2 == 1 and map[i][j] == 'B': map[i][j] = 0
        else: map[i][j] = 1
    cal.append([])
    for j in range(len(map[i])-7):
        cal[i].append(sum(map[i][j:j+8]))
cal = [[cal[j][i] for j in range(len(cal))] for i in range(len(cal[0]))]
res = []
for i in range(len(cal)):
    for j in range(len(cal[i])-7):
        s = sum(cal[i][j:j+8])
        res.append(min(s, 64-s))
print(min(res))