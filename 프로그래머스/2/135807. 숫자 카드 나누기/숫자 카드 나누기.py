def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(arrayA, arrayB):
    answer = [0]
    
    gcd_val = arrayA[0]
    for val in arrayA:
        gcd_val = gcd(val, gcd_val)
    
    if all(val % gcd_val for val in arrayB):
        answer.append(gcd_val)
    
    gcd_val = arrayB[0]
    for val in arrayB:
        gcd_val = gcd(val, gcd_val)
        
    if all(val % gcd_val for val in arrayA):
        answer.append(gcd_val)
    

    return max(answer)
