#2차시도) 스택 사용
#시간복잡도) O(N)
#주식가격이 떨어진다는 것은 현재원소 다음의 원소들에서 현재원소보다 값이 작은 원소가 있다는 것
#각 가격들을 비교해가야함
#현재원소와 다음원소를 비교 - for문으로 반복할때 i는 시간
#매 초마다 비교하는 로직
#스택에 주식가격이 떨어지지 않은 price들을 넣어두고 매번 해당 초의 price와 비교하여 주식가격이 떨어졌는지 비교해갈것
#만약 현재원소보다 다음원소가 크다면 주식가격이 현재 시간에서는 아직 떨어지지 않은 것이므로 현재 원소를 스택에 넣는다
#만약 현재원소보다 다음원소가 작다면 주식가격이 떨어진 것이므로 스택에서 빼고 주식가격이 떨어진 시간을 구한다

#2차시도) 구현력이 안좋은가봄 로직은 구글링과 같은데 런타임에러로 통과못함
def solution(prices):
  total_time = len(prices)
  retention_time=[0]*(total_time) #매초에 대한 주식가격 유지시간
  stack=[]
  #top=-1 #굳이 top을 설정해줄 필요가 없음 왜냐면 인덱스를 -1로 하면 언제든 top에 접근가능
  for now_time in range(total_time): #0초~4초 실제시간은 +1을 해줄것
    if stack:
      while prices[stack[-1]] > prices[now_time]: 
        retention_time[stack[-1]] = now_time - stack[-1]
        stack.pop()
      
    stack.append(now_time)
    top+=1
  
  while stack:
    retention_time[stack[-1]]=total_time-1-stack[-1]
    stack.pop()
    top-=1
       
  return retention_time
  
prices= [1, 2, 3, 2, 3]
print(solution(prices))