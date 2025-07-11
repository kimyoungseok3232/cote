def solution(k, room_number):
    answer = []
    visited = {}
    for n in room_number:
        if n not in visited:
            visited[n] = [[n]]
            
            if n+1 in visited:
                visited[n] = visited[n+1]
                
            if n-1 in visited:
                visited[n-1][0] = visited[n][0]
                
        else:
            while n in visited:
                tmp = n
                n = visited[n][0][0] + 1
                if n in visited:
                    visited[tmp][0] = visited[n][0]
            visited[n] = visited[n-1]
            visited[n][0][0] = n
        answer.append(n)
    return answer