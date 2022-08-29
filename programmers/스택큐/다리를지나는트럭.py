#다리의 길이는 bridge_legnth만큼의 크기를 가지고 이를 넘어서는 안된다
#=> bridge를 다리길이만큼 설정한다
#=> bridge라는 리스트를 다리길이만큼 0으로 초기화한다
#다리 위에는 weight만큼의 트럭만 올라갈 수 있다
#=> bridge에 있는 트럭의 무게와 truck_weights의 맨앞 트럭 무게가 weight를 넘는지 검사한다
#=> **만약 둘의 합이 weight를 넘어서 bridge에 있는 트럭이 나가기 전에 truck_weights의 트럭이 다리를 지날 수 없다면 우선 bridge를 0으로 대신 메꿔준다
#매 초마다 트럭들은 다리에서 한칸 앞으로 나아간다
#=> 매 초가 증감될때마다 bridge에서 맨 앞 트럭이 pop된다
#다리를 모두 건너는 최소 시간을 구하라
#bridge가 비는 때 반복문을 멈추고 시간을 리턴한다
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        time += 1
        bridge.pop(0)
        #line20) line19를 넣지 않으면 list index error: truck_weights가 다 빠져나가면 인덱스로 접근시 에러가 나기 때문
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))