fixedCost,variCost,cost=map(int,input().split())
#fixedCost + variCost*cnt < cost*cnt
#fixedCost < (cost-variCost)*cnt
#fixedCost / (cost-variCost) < cnt : cnt가 손익분기점이 되는 당시
#최초로 이익이 발생하는 때는 손익분기점 바로 이후
if variCost >= cost:
  print(-1)
else:
  print(fixedCost // (cost-variCost)+1)