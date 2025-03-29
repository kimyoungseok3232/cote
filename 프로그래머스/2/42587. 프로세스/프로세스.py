from collections import deque
def solution(priorities, location):
    answer = 0
    sorted_list = sorted(priorities)
    priorities = deque(priorities)
    while priorities:
        max_pr = sorted_list.pop()
        while priorities[0] != max_pr:
            priorities.rotate(-1)
            location = (location-1)%len(priorities)
            print(location)
        priorities.popleft()
        location = location-1
        answer += 1
        if location == -1: break
    return answer