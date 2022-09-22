#토마토가 있는 모든 지역에서 동시에 인접한 지역으로 영향을 미치기 때문에
#처음 반복문으로 토마토의 정보를 수집하면서 익은 토마토가 있는 지역을 큐에 삽입하고 큐에서 꺼내 bfs를 수행해야한다
#하루가 지날때마다 인접한 토마토가 익으므로 토마토가 안익은 지역을 bfs를 통해 방문할 때마다 +1을 해주고 그래프에서 가장 큰 값을 찾으면 된다

from collections import deque

m,n = map(int, input().split())

min_day = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

tomatos = [] #tomatos의 요소는 몇일만에 토마토가 익었는지에 대한 정보들로 채워질것
q = deque()
#Q: 한 행을 한번에 입력받는데 그 중 1인 것들만 어떻게 큐에 삽입하는지?
#내생각) 우선 한번에 입력을 받고 그 행의 열을 반복문으로 돌아가면서 확인하고 1이라면 큐에 삽입
for i in range(n):
    tomatos.append(list(map(int, input().split())))
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append((i,j))
#print(tomatos)
#print(q)

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                q.append((nx,ny))

bfs()
flag = False

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 0:
            flag = True

if flag:
    print(-1)
else:
    print(max(map(max,tomatos))-1)
    




