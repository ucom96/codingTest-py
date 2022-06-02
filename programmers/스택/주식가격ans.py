#2차시도) 성공
#스택 사용시 시간복잡도가 O(N)에 가깝게 나오므로
def solution(prices):
  length = len(prices)
  answer=[0]*length #[0]으로 초기화 안해놓으면 [] 상태에서는 = 으로 값이 변경되지 않음 append면 몰라도..
  stack=[]
  
  for i in range(length):
    while stack and prices[stack[-1]] > prices[i]:
      j=stack.pop()
      answer[j] = i - j
      
    stack.append(i)
    
  while stack:
    j=stack.pop()
    answer[j] = length -1 - j
  
  
  return answer
  
prices=[1,2,3,2,3]
print(solution(prices))