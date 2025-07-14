def solution(n):
    tmp = set(['()'])
    for i in range(n):
        answer = set()
        for s in tmp:
            op = 0
            cl = 0
            for j in range(len(s)):
                if op == cl:
                    ns = '(' + s[:j] + ')' + s[j:]
                    answer.add(ns)
                if s[j] == '(': op += 1
                else: cl += 1
        tmp = answer
    return len(answer)