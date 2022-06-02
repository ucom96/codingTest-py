#2:27~
from collections import deque
import sys
n=int(sys.stdin.readline())

#한줄로 완성하기
#q=deque(range(1,n+1))
q=deque()
for i in range(1,n+1):
  q.append(i)

for _ in range(n-1):
  #가장앞에 있는 카드를 버린다
  q.popleft()
  #그 다음으로 있는 카드를 뒤로 옮긴다
  q.append(q.popleft())
  
print(q.pop())
  