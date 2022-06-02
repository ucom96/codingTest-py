#'('를 만나면 스택에 넣는다
#')'를 만나면 스택에서 뺀다
#만약 ')'인데 스택이 비어있다면 VPS가 아님
#모든 과정이 끝났는데 스택에 남아있는게 있다면 VPS가 아님
#스택에는 '('만 들어가므로 따로 스택을 만들 필요 없이 스택의 요소 수를 알려주는 cnt 변수만 있으면 됨
import sys
t=int(sys.stdin.readline())

def isVPS(ps):
  cnt=0
  for el in ps:
    if el=="(":
      cnt+=1
    else:
      if cnt==0:
        return False
      cnt-=1
  if cnt>0:
    return False
  else:
    return True

for _ in range(t):
  ps=sys.stdin.readline().strip()
  if isVPS(ps):
    print("YES")
  else:
    print("NO")
  