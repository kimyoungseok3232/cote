
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
import sys
sys.setrecursionlimit(20000)

def solution(k, room_number):
    answer = []
    p = {}

    def find(a):
        if a not in p:
            p[a] = a
            return a
        if p[a] == a: return a
        p[a] = find(p[a])
        return p[a]

    def union(x):
        answer.append(x)
        p[x] = find(x + 1)

    for request in room_number:
        union(find(request))

    return answer