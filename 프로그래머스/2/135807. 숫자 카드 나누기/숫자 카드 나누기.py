def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(arrayA, arrayB):
    answer = []
    gcd_val = arrayA[0]
    for val in arrayA:
        gcd_val = gcd(val, gcd_val)

    if gcd_val > 1:
        for val in arrayB:
            if val%gcd_val: continue
            break
        else: answer.append(gcd_val)
    
    gcd_val = arrayB[0]
    for val in arrayB:
        gcd_val = gcd(val, gcd_val)
    
    if gcd_val > 1:
        for val in arrayA:
            if val%gcd_val: continue
            break
        else: answer.append(gcd_val)

    if answer: return max(answer)
    return 0