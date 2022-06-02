#현재 가격과 이후의 가격들을 비교한다
#이후의 가격중에 현재 가격보다 작은 것이 있다면 그 가격의 인덱스에서 현재 가격 인덱스를 빼준다
#이후의 가격중에 현재 가격보다 작은 것이 없다면 총 prices 배열 크기에서 현재 가격 인덱스를 빼준다
#1차시도) 실패
#원인) 시간복잡도가 매우 크게 나옴.. min(), indexing, index() 모두 O(N)이 걸리는데 한줄에 쓰면 O(N^3)이 되어 시간이 매우 오래 걸릴것
def solution(prices):
  length = len(prices)
  answer = [0]*length #0을 안넣으면 indexError
  for now_idx in range(length):
    nxt_idx = prices.index(min(prices[now_idx:]),now_idx)
    print(now_idx,nxt_idx)
    if now_idx == nxt_idx:
      answer[now_idx]=length-1-now_idx
    else:
      answer[now_idx]=nxt_idx-now_idx
    
  return answer
  
prices = [1,2,3,2,3]
print(solution(prices))
  
  

  
