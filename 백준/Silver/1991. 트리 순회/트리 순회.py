def search(node, order, res):
    t = [node] + tree[node]
    t = [t[order[0]],t[order[1]],t[order[2]]]
    for i in t:
        if i == '.': continue
        if i == node: res.append(i)
        else: search(i, order, res)
    return res
n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]
print(''.join(search('A', (0,1,2), [])))
print(''.join(search('A', (1,0,2), [])))
print(''.join(search('A', (1,2,0), [])))