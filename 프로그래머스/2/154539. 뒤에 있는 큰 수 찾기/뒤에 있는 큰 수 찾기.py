def solution(numbers):
    answer = [-1] * len(numbers)
    tmp = []
    for idx, num in enumerate(numbers):
        while tmp and numbers[tmp[-1]] < num:
            answer[tmp.pop()] = num
        tmp.append(idx)
    return answer