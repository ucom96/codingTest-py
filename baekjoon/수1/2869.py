#1차시도) 시간초과
#실패이유) 1차때 짠 코드로 실행하면 시간이 10초 걸린다
a,b,v=map(int,input().split())
m=0 #현재미터
days=0
#반복문: 정상에 올라갈때까지
#현재미터(m미터) >= v미터

while m < v:
  days+=1
  #낮에 올라간 미터
  m+=a
  #낮에 올라갔는데 정상에 다다른 경우 days를 출력하고 반복을 멈춘다
  if m >= v:
    break
  #밤에 올라간 미터
  m-=b
  
print(days)

#해결) 식을 도출할 것
#a*days - b*(days-1) >= v
#a*days -b*days +b >= v
#(a-b)*days >=v-b
#days>=(v-b)/(a-b)
#days = (v-b)/(a-b) (나누어떨어지면)
#days = (v-b)/(a-b)+1
  