def solution(skill, skill_trees):
    answer = 0
    skill_set = set(skill) 
    for tree in skill_trees:
        tree = [alpha for alpha in tree if alpha in skill_set]
        for idx in range(len(tree)):
            if tree[idx] == skill[idx]: continue
            break
        else: answer += 1
    return answer