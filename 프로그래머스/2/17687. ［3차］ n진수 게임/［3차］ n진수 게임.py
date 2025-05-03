def njin(num, n):
    d = '0123456789ABCDEF'
    ans = ''
    while num:
        num, mod = divmod(num, n)
        ans = d[mod] + ans
        
    return ans
def solution(n, t, m, p):
    answer = []
    st = p-1
    num = 0
    string = '0'
    while len(answer) < t:
        while st >= len(string):
            st -= len(string)
            num += 1
            string = njin(num, n)
        answer.append(string[st])
        st += m
    return ''.join(answer)