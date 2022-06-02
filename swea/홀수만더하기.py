t=int(input())

def isOdd(num):
  if num%2!=0:
    return True
  else:
    return False
  
for i in range(1,t+1):
  result=0
  nums = map(int, input().split())
  for num in nums:
    if isOdd(num):
      result+=num
  print("#{} {}".format(i,result))
