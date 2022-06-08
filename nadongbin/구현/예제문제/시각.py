#접근법 - 브루트포스 O(60*60*24)
#1. 시, 분, 초에 대한 for문을 만든다
#2. 각 시, 분 , 초를 문자열로 만들어 3이 있는지 확인후 있다면 cnt를 증감시킨다
#3. cnt를 출력한다

n = int(input())
cnt = 0

#int to string: str(number)
for hour in range(n+1):
  hour = str(hour)
  for minute in range(60):
    minute = str(minute)
    for second in range(60):
      second = str(second)
      #문자열 합치기: + 연산자
      totalTime = hour + minute + second 
      if '3' in totalTime: #문자열 안에 문자 확인: 문자 in 문자열
        cnt+=1
        
print(cnt)
      
#1차시도) 답은 나옴 성공인듯?
#시간) 15분 소요
#답안과 로직과 접근법이 같음 잘했다! 하지만 답안처럼 좀 더 코드를 깔끔하게 작성하면 더 좋을듯