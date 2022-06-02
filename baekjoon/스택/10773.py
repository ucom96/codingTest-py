from collections import deque
import sys

n=int(sys.stdin.readline())
stack=deque()

for _ in range(n):
  el=int(sys.stdin.readline())
  if el==0:
    stack.pop()
  else:
    stack.append(el)
  
print(sum(stack))

#sum(stack)
#deque가 아니어도 list는 append와 pop이 존재
    