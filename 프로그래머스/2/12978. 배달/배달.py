from heapq import heappop, heappush
def solution(N, road, K):
    answer = 0
    dist = [10e9] * (N+1)
    node = {}
    for st, ed, w in road:
        if st not in node:
            node[st] = []
        if ed not in node:
            node[ed] = []
        node[st].append((ed,w))
        node[ed].append((st,w))
    
    visited = set()
    heap = [(0,1)]
    dist[1] = 0
    while heap:
        w, no = heappop(heap)
        visited.add(no)
        for n, w in node[no]:
            if n in visited: continue
            if dist[n] > dist[no] + w:
                dist[n] = dist[no] + w
                heappush(heap, (dist[no]+w,n))

    return sum(1 for i in dist if i <= K)