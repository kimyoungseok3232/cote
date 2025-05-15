
def solution(arr):
    answer = [0, sum(map(sum, arr))]
    answer[0] = len(arr)**2 - answer[1]
    
    def compression(arr, n, x = 0, y = 0):
        if n == 1: 
            return arr[x][y]
        s = 0
        for i in range(x, x+n, n//2):
            for j in range(y, y+n, n//2):
                s += compression(arr, n//2, i, j)
        if s == n*n: answer[1] -= 3
        elif s == 0: answer[0] -= 3
        return s
    
    compression(arr, len(arr))
    return answer