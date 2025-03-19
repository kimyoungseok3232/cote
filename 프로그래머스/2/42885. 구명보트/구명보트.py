def solution(people, limit):
    answer = 0
    people.sort()
    st = 0
    ed = len(people)-1
    while st <= ed:
        if people[st]+people[ed] <= limit: st += 1
        ed -= 1
        answer += 1
    return answer