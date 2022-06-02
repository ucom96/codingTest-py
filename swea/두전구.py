import sys
t=int(sys.stdin.readline())
result =[]

for _ in range(t):
  a,b,c,d = map(int,sys.stdin.readline().split())
  time = min(b,d)-max(c,a)
  if time <=0:
    result.append(0)
  else:
    result.append(time)
    
for i in range(t):
  print(f"#{i+1}",result[i])
