def solution(k, room_number):
    answer = []
    visited = {}
    for n in room_number:
        if n not in visited:
            visited[n] = [n]
        else:
            while n in visited:
                tmp = n
                n = visited[n][0] + 1
                if n in visited:
                    visited[tmp][0] = visited[n][0]
            visited[n] = visited[n-1]
            visited[n][0] = n
        answer.append(n)
    return answer