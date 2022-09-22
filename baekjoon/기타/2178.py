#미로탐색
#12:40~
from collections import deque

n,m = map(int, input().split())
result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

#bfs로 (0,0)부터 탐색하여 이동할 수 있는 칸으로 옮겨가서 최단거리르 갱신해준다
#n,m에서 갖게 되는 최단거리를 출력한다

print(miro)
def bfs(x,y):
    q = deque([(x,y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                print(nx,ny)
                if miro[nx][ny] == 1:
                    q.append((nx,ny))
                    miro[nx][ny] = miro[x][y] + 1

bfs(0,0)
print(miro[n-1][m-1])