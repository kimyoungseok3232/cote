def solution(phone_book):
    answer = True
    phone_book.sort(reverse=True, key=len)
    visited = set()
    for num in phone_book:
        if num in visited:
            answer = False
            break
        for i in range(1,len(num)+1):
            visited.add(num[:i])
            
    return answer