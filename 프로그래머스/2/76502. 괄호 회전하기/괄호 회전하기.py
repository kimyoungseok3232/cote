def check(s):
    while s:
        if '[]' in s: s = s.replace('[]', '')
        elif '()' in s: s = s.replace('()', '')
        elif '{}' in s: s = s.replace('{}', '')
        else: return False
    return True
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:]+s[:i]): answer += 1
    return answer