def solution(num_list):
    even = sum(map(lambda x: x%2, num_list))
    return [len(num_list)-even,even]