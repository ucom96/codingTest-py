#시작시간: 4:50~
#접근법)
#1. 각각의 공간이 육지인지 바다안지 알기 위해 graph를 만든다
#2. 각 방향을 인덱스로 잡고 해당 방향으로 나아갈때의 dx,dy를 만든다
#3. 왼쪽으로 회전할때의 인덱스를 구할 수 있는 함수를 따로 생성할것
#4. bfs로 그래프를 탐색하며 cnt를 세어간다
#5. 이미 한번 간 육지는 1처리를 하여 못가도록 한다

from collections import deque

n,m=map(int, input().split())
x,y,direction = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
  graph[i]=list(map(int, input().split()))

#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]
result=0

def rotateDirection(direction):
  if direction == 0:
    direction=3
  else:
    direction-=1
  return direction


def bfs(x,y,direction):
  global result #정수형 변수가 전역으로 선언되면 함수안에서 global로 선언해줄것
  q=deque([(x,y,direction)])
  graph[x][y]=1
  result+=1
  while q:
    cnt=0
    now_x, now_y, now_d = q.popleft()
    for _ in range(4):
      now_d = rotateDirection(now_d)
      nx,ny = now_x+dx[now_d], now_y+dy[now_d]
      if graph[nx][ny]==0:
        q.append((nx,ny,now_d))
        graph[x][y]=1
        result+=1
      else:
        cnt+=1
    if cnt==4:
      nx,ny=now_x+(-1)*dx[now_d],now_y+(-1)*dy[now_d]
      if graph[nx][ny]==1:
        return result
      else:
        continue
  return result
    
  
print(bfs(x,y,direction))

#1차시도) 실패 - 무한루프 돔
#원인) 굳이 bfs를 쓸 필요가 없음 bfs는 노드 간 이동을 위해 구현된 알고리즘으로 큐를 사용하는데
#dx와 dy가 이동을 대신하기 때문에 굳이 bfs를 사용하지 않아도됨
