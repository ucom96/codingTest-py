#뒤에 더 크기가 더 작은 원소가 있다면 가격이 떨어진것
#뒤에 크기가 더 작은 원소가 없다면 가격이 떨어지지 않은것
#1차시도) 시간초과 O(n^2)이므로 시간초과가 뜨는데 min()을 쓰지 않고 뒤에 원소들과 비교할 수 있는 방법이 있는건가?

def solution(prices):
    answer = []
    lth = len(prices)
    #가격이 떨어진다 = prices 배열에서 자신 이후의 원소들 중 더 작은 원소가 있을 경우
    #매번 배열의 뒤 원소들의 크기를 체크해야함 = O(n^2)
    for idx, price in enumerate(prices):
      after = prices[idx+1:]
      if idx == lth-1:
        answer.append(lth-(idx+1))
      else:
        smallestPrice = min(after)
        if price > smallestPrice:
          answer.append(prices.index(smallestPrice,idx+1)-idx)
        else:
          answer.append(lth-(idx+1))
        
    return answer
  
prices = [1,2,3,2,3]
print(solution(prices))
  
  

  
