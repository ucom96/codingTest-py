#1차시도) 답은 잘 나오나 조금 느린 것 같음
#백준 성공
from itertools import combinations
from collections import deque
import copy

n,m=map(int, input().split())

space =[]
for _ in range(n):
    space.append(list(map(int, input().split())))

wall = []
for i in range(n):
    for j in range(m):
        if space[i][j]==0:
            wall.append((i,j))

#print(wall)

#print(space)

#1. 벽의 조합을 구한다
#벽은 0이 있는 곳에 둘 수 있으므로 0이 있는 곳의 좌표들의 모음을 알아야할 것임 (line9-13)
wall_combis = list(combinations(wall, 3))
#print(wall_combi)

#2. 벽의 조합들 중 하나를 뽑아 벽을 세운 뒤 bfs로 바이러스가 퍼지도록 한다
#벽을 세운 뒤 다시 초기화를 해야함 왜냐하면 초기화된 상태에서 다른 벽 조합을 둬야하기 때문에 (line31-34)
def makeWall(wall_combi,space_cp):
    for i in wall_combi:
        x,y=i
        space_cp[x][y]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,space_cp):
    #Q: 해당 노드에 방문했었음을 어떻게 표시할 것인지?
    #매번 bfs 함수때마다 visited 배열을 만들어도 괜찮은것인지?
    #visited=[[0]*m for _ in range(n)]
    #space의 요소가 0일때만 이동하면 되므로 굳이 visited를 만들지 않음
    #Q: visited는 어떤 경우에 만드는 것인가?
    q=deque([(x,y)])

    while q:
        x,y = q.popleft()
        for i in range(4):
          nx = x+dx[i]
          ny = y+dy[i]
          if 0<=nx<n and 0<=ny<m:
            if space_cp[nx][ny]==0:
              q.append((nx,ny))
              space_cp[nx][ny]=2

#중요한점: 원본배열인 space에 표시를 하게 될 경우 다른 조합에서 초기화된 상태로 만들어야하기 때문에 다시 지워야하는 번거로운 일 발생
#원본배열의 복사본을 만들어서 진행하는 것이 어떨런지?
#우선 space의 복사본을 만든다
#복사본에 벽의 조합을 세운다
#bfs로 바이러스를 퍼뜨린다
#안전영역을 계산한다
#안정영역 크기를 배열에 넣는다
#가장 값이 큰 안전영역 크기를 출력한다

result=0
for i in wall_combis:
  cnt=0
  space_cp = copy.deepcopy(space)
  #print('before',space_cp)
  makeWall(i,space_cp)
  for i in range(n):
    for j in range(m):
      if space_cp[i][j]==2:
        bfs(i,j,space_cp)
  for i in range(n):
    for j in range(m):
      if space_cp[i][j]==0:
        cnt+=1
  result = max(result, cnt)
  #print('after',space_cp)

print(result)