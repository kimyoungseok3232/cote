n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]

preorder = []
tmp = ['A']
while tmp:
    node = tmp.pop()
    if (t:=tree[node][1]) != '.': tmp.append(t)
    if (t:=tree[node][0]) != '.': tmp.append(t)
    preorder.append(node)
print(''.join(preorder))

inorder = []
visited = set()
tmp = ['A']
while tmp:
    if (t:=tree[tmp[-1]][0]) != '.' and t not in visited: 
        tmp.append(t)
        visited.add(t)
    else: 
        node = tmp.pop()
        inorder.append(node)
        if (t:=tree[node][1]) != '.': tmp.append(t)
print(''.join(inorder))

postorder = []
tmp = ['A']
while tmp:
    left, right = tree[tmp[-1]]
    tree[tmp[-1]] = ['.', '.']
    if left == right: 
        postorder.append(tmp.pop())
        continue
    if right != '.': tmp.append(right)
    if left != '.': tmp.append(left)
print(''.join(postorder))