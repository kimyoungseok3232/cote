import heapq
from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1 and scoville[0] < K:
        heappush(scoville, heappop(scoville) + heappop(scoville)*2)
        answer += 1
    if len(scoville) == 1 and scoville[0] < K: return -1
    return answer