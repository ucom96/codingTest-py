#문제가 요구하는 사항들만 잘 이해하고 체크하면 어려울 것 없는 문제
#처음에 짰던 코드와 로직은 비슷
#다만 bfs를 쓰지 않아도 되므로 dx,dy를 통해 공간이동을 함
n,m=map(int, input().split())
x,y,d=map(int, input().split())

graph=[]
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
turn_time = 0
result = 1

#d를 인자로 주기보다 global d를 설정하여 함수로 리턴된 d를 담는 변수를 따로 만들기보다 전역변수 d를 가지고 더 편리하고 깔끔하게 코딩할것
def rotateDirection():
  global d
  if d == 0:
    d=3
  else:
    d-=1

#현재 있는 공간에 방문했음을 표시한다
graph[x][y]=2
while True:
  #1단계) 방향을 왼쪽 방향으로 돌린다
  rotateDirection()
  #왼쪽방향의 좌표를 체크한다
  nx,ny = x+dx[d], y+dy[d]
  #2단계) 왼쪽 방향에 가보지 않은 칸이 존재한다면 왼쪽으로 한칸 전진한다
  if graph[nx][ny] == 0:
    x,y=nx,ny
    graph[x][y]=2
    result+=1
    turn_time=0
  #가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 한다
  else:
    turn_time+=1
  #3단계) 네방향 모두 가본 칸이거나 바다로 되어있다면 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
  if turn_time == 4:
    nx,ny=x-dx[d], y-dy[d]
    if graph[nx][ny]==2:
      x,y=nx,ny
      turn_time=0
      continue
    else:
      break

print(result)
#3단계에서 바라보는 방향을 유지한채로 한칸 뒤로 가는 경우는
#뒤가 바다가 아닌 이미 가본 칸인 경우에 해당하므로
#따라서 바다칸과 이미 가본 칸을 따로 구분해주어야한다
#나의 해결법) 이미 가본 칸은 2로 만든다