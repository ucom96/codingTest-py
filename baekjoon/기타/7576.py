#토마토
#12:33~

#하루 지나면 익은 토마토들의 상하좌우에 있는 익지 않은 토마토들은 익게됨
#며칠이 지나야 다 익게되는지
#익은 토마토:1 익지 않은 토마토:0 토마토안들어있음:-1
#저장될떄부터 모든 토마토가 익어있는 상태라면 0, 모두 익지 못하는 상황이면 -1


from collections import deque

m,n = map(int, input().split())

min_day = -1
tomatos = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    tomatos.append(list(map(int, input().split())))

#반복적으로(하루마다) 익은 토마토들에 인접한 익지 않은 토마토들을 익은 토마토로 바꿔가야함
#bfs를 적용하여 매번 상하좌우를 탐색할때마다 min_day를 올려주면됨

def bfs(x,y):
    q = deque([(x,y)])

    while q:
        #min_day += 1
        x, y = q.popleft()
        for i in range(4):
            #x,y에서 상하좌우로 갈 수 있는 다음 좌표 nx,ny
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<=n and 0<=ny<=m and tomatos[nx][ny] == 0:
                #익지 않은 토마토를 익은 토마토로 바꿔준다
                tomatos[nx][ny] = 1
                q.append((nx,ny))

bfs(0,0)

#Q: 모두 익지 못하는 상황임을 어떻게 알건가?
print(min_day)
            
