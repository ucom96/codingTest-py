#8:40~
#현재 요소의 이후 요소들중 자신보다 작은 요소가 있는지 확인해야함
#더 작은 요소가 있다면 그 요소의 인덱스 - 현재 인덱스
#더 작은 요소가 없다면 맨 끝 요소의 인덱스 - 현재 인덱스

#뒤의 요소가 중요하다면 스택을 이용!
#prices의 값과 인덱스 모두를 알고 있어야 함 => 튜플로 저장할것
#현재 요소보다 더 큰 요소가 있다면 그 요소를 스택위에 쌓음
#현재 요소보다 더 작은 요소가 있다면 현재 요소를 스택에서 빼내고 인덱스를 계산할것 그리고 더 작은 요소를 스택에 넣어준다
#만약 prices를 다 돌았다면 끝 인덱스 - 스택 요소의 인덱스 로 각각을 계산해준다
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            #스택의 요소가 현재 요소보다 크다면 스택 요소를 스택에서 빼내고 answer에 값을 계산하여 넣어준다
            #그리고 현재 요소를 스택에 넣어준다
            j = stack.pop()[0]
            answer[j] = i - j
        stack.append((i,prices[i]))
    #끝내 가격이 떨어지지 않은 price들, 즉 스택에 계속 있는 price들은 끝 인덱스에서 자신의 인덱스를 뺀 값을 계산하여 answer에 넣어준다
    while stack:
        j = stack.pop()[0]
        answer[j] = len(prices) - j - 1

    #print(stack)
    return answer    

prices = [1,2,3,2,3]

print(solution(prices))

#내가 틀린 이유
#스택의 요소들 중 현재 요소보다 큰 요소가 하나 이상일 수 있기 때문에 스택을 반복문으로 요소 하나씩 돌아가며 확인해주어야함

