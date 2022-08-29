"""
첫코드
from collections import deque
def solution(queue1, queue2):
    answer = -1
    q1 = deque(queue1)
    q2 = deque(queue2)
    target = (sum(q1)+sum(q2)) // 2
    #sum2를 구할 필요가 없음
    #sum1과 target만 비교해도 되므로 => sum1이 target과 같다면 sum2는 무조건 이와 같아짐 애초에 target이 sum1과 sum2의 1/2이므로
    sum1 = sum(queue1)
    #sum2 = sum(queue2)

    #tmp도 여기서 초기화를 굳이 할 필요없이 if문에서 처음으로 초기화해주면 됨
    #tmp = 0

    #cnt가 곧 answer가 될 것이므로 따로 cnt 변수를 선언하는 것보다 answer를 이용할것!
    #cnt = 0
    
    #**종료조건을 어떻게 설정해야할지?
    #왜 while q1 and q2로 될 수 있는건지 궁금 
    #ex) [1,3] [3,6]의 경우에는 그 어느 경우도 큐가 비지 않고 무한루프를 도는데 이러한 경우 어떻게 종료할 것인지?
    while True:
        if answer == len(q1)*2:
            break
        if sum1 == sum2 and sum1 == target:
            answer = cnt
            break
        #if sum1 < target
        if sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            #sum2는 할 필요 없음
            #sum2 -= tmp
        elif sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
        cnt+=1
    return answer
"""

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    target = (sum1+sum2) // 2


    while True:
        if answer == len(q1)*2:
            return -1
        
        if sum1 == sum2 and sum1 == target:
            return answer

        if sum1 < sum2:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            
        elif sum1 > sum2:
            tmp = q1.popleft()
            q2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
            
        answer+=1
        
    return answer

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))