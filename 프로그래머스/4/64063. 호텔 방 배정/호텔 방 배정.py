def solution(k, room_number):
    answer = []
    visited = {}
    for n in room_number:
        if n not in visited:
            visited[n] = [n]
        else:
            tmp = n
            while n in visited:
                visited[tmp] = visited[n]
                tmp = n
                n = visited[n][0] + 1

            visited[n] = visited[n-1]
            visited[n][0] = n
        answer.append(n)
    return answer