def solution(A, B):
    A.sort()
    B.sort()
    answer = len(A)
    count = 0
    for i in range(len(B)):
        if B[i] > A[i-count]: continue
        A.pop()
        count += 1
            
    return answer-count