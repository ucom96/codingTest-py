t=int(input())
#가장 많은 차이가 나는 날의 매매가에 팔아야 최대 이익을 볼 수 있음
#인덱싱해서 최대값을 구해나가는 식으로 풀 것

for i in range(1,t+1):
  result=0
  n=int(input())
  cost=list(map(int,input().split()))
  for j in range(n-1):
    biggestCost=max(cost[j+1:])
    nowCost=cost[j]
    if biggestCost <= nowCost:
      continue
    else:
      result+=biggestCost-nowCost
  
  print("#{} {}".format(i,result))
  