def solution(phone_book):
    answer = True
    phone_book.sort(reverse=True, key=len)
    print('asd' in {'asd':1})
    visited = set()
    for num in phone_book:
        if num in visited:
            answer = False
            break
        for i in range(1,len(num)+1):
            visited.add(num[:i])
            
    return answer

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer