#브루트포스 문제: 전체 데이터 개수가 100만 개 이하일시 가능한 경우의 수를 모두 검사하는 탐색 방법
h = int(input())
cnt = 0

#int to string: str(number)
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        cnt +=1
        
print(cnt)
      