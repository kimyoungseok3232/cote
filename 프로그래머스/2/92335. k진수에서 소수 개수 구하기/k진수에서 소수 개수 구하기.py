def trans(n, k):
    st = ''
    while n:
        n, mod = divmod(n, k)
        st = str(mod)+st
    return st

def is_frime(n):
    if n == 1: return False
    for i in range(2, int(1+n**0.5)):
        if n%i == 0: return False
    return True

def solution(n, k):
    answer = 0
    st = trans(n, k)
    for v in st.split('0'):
        if v and is_frime(int(v)):
            answer += 1
    return answer