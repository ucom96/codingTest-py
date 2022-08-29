def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge =[truck_weights[0]]
    truck_weights.pop(0)
    while bridge:
        truck = truck_weights[0]
        if sum(bridge) + truck <= weight:
            bridge.append(truck)
            truck_weights.pop(0)
        else:
            bridge.append(0)
        if len(bridge) == bridge_length:
            bridge.pop(0)
        answer+=1
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))