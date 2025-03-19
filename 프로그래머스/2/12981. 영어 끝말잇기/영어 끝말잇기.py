def solution(n, words):
    visited = set()
    last = words[0][0]
    for word in words:
        if word in visited:
            return [1+len(visited)%n, 1+len(visited)//n]
        elif word[0] != last:
            visited.add(word)
            return [1+(len(visited)-1)%n, 1+(len(visited)-1)//n]
        visited.add(word)
        last = word[-1]
    return [0, 0]