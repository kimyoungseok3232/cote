def solution(s):
    answer = []
    find = set()
    data = [val.replace('{', '').replace('}', '').split(',') for val in s.split('},')]
    data.sort(key=len)
    for tup in data:
        for val in tup:
            if val in find: continue
            find.add(val)
            answer.append(int(val))
    return answer