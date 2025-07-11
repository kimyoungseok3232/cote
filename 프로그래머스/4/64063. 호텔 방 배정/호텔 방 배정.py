def solution(k, room_number):
    answer = []
    visited = {}
    for n in room_number:
        if n not in visited:
            visited[n] = n
        else:
            while n in visited:
                tmp = n
                n = visited[n] + 1
                if n in visited:
                    visited[tmp] = visited[n]
            visited[n] = visited[n-1]
            visited[n] = n
        answer.append(n)
    return answer