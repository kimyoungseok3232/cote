def solution(order):
    belt = [i for i in range(len(order),0,-1)]
    ex_belt = [belt.pop() for i in range(order[0])]
    st = 0
    while 1:
        if ex_belt and ex_belt[-1] == order[st]:
            ex_belt.pop()
        elif belt and belt[-1] <= order[st]:
            for i in range(order[st]-belt[-1]):
                ex_belt.append(belt.pop())
            belt.pop()
        else: break
        st += 1
    return st