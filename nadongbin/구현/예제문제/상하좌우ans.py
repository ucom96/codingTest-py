#시뮬레이션 문제: 명령에 따라 개체를 차례대로 이동시키는 문제

n=int(input())
x,y =1,1

plans = input().split()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_types = ['L','R','U','D'] #내가 놓친 점) move_types를 만들어 dx,dy와 대응시키기

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      
  if nx<1 or nx>n or ny<1 or ny>n: #공간을 벗어나면 무시
    continue
  x,y = nx,ny
  
print(x,y)