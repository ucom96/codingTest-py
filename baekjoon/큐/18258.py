#1:50~1:58
#주의) for문에서 입력을 받으면서 출력까지 할 경우 시간소요 더 커짐
#해결) 배열에 넣어서 한번에 출력하거나 출력문은 다른 for문에서 진행할것

import sys
from collections import deque
n=int(sys.stdin.readline())
q=deque()
answer=[]

for _ in range(n):
  command = sys.stdin.readline().split()
  if command[0]=="push":
    q.append(command[1])
  elif command[0]=="pop":
    if q:
      answer.append(q.popleft())
    else:
      answer.append(-1)
  elif command[0]=="size":
    answer.append(len(q))
  elif command[0]=="empty":
    if q:
      answer.append(0)
    else:
      answer.append(1)
  elif command[0]=="front":
    if q:
      answer.append(q[0])
    else:
      answer.append(-1)
  elif command[0]=="back":
    if q:
      answer.append(q[-1])
    else:
      answer.append(-1)
      
print('\n'.join(map(str,answer)))

