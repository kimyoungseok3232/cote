def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.reverse()
    bridge = [0] * bridge_length
    weight_sum = 0
    while truck_weights:
        st = answer%bridge_length
        weight_sum -= bridge[st]
        bridge[st] = 0
        if weight_sum+truck_weights[-1] <= weight:
            bridge[st] = truck_weights.pop()
            weight_sum += bridge[st]
        answer += 1
    return answer+bridge_length