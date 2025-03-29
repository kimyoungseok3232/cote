def backtrack(dungeons, tired, visited = set(), answer = 0):
    tmp = answer
    for idx, (least, loss) in enumerate(dungeons):
        if idx in visited or tired < least: continue
        visited.add(idx)
        tmp = max(tmp, backtrack(dungeons, tired - loss, visited, answer+1))
        visited.remove(idx)
    return tmp
def solution(k, dungeons):
    answer = backtrack(dungeons, k)
    return answer