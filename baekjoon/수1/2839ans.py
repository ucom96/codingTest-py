#봉지수와 설탕무게를 따로 변수로 생성하여
#먼저 설탕무게를 5로 나눈 후 5로 나눠떨어지면(5의배수라면) 봉지수를 해당 몫만큼 더해준다
#5로 나눠지지 않으면 3을 빼서 5로 나눠떨어질 숫자가 나올때까지 반복한다
#몫이 0이면 3 혹은 5중 어느 수든 나눠져 떨어졌다는 것이므로 봉지수를 출력
#몫이 0이 아니면 3 혹은 5중 어느 수로도 나눠 떨어지지 않았다는 것이므로 -1 출력

import sys
kilo = int(sys.stdin.readline())

bag_num = 0 #봉지수

while kilo >0:
  if kilo % 5 ==0:
    bag_num += kilo //5
    kilo=0
  else:
    kilo-=3
    bag_num+=1
    
if kilo ==0:
  print(bag_num)
else:
  print(-1)