#1. 연합을 찾는다
#각 나라마다 상하좌우를 탐색하여 국경선을 열 수 있는지를 확인한다
#Q: 매번 각 나라마다 BFS 연산을 수행하면 시간복잡도가 너무 커지진 않을지?
#Q: 연합과 관련된 나라를 어디에 어떻게 저장할지? => 리스트에 인덱스 저장
#Q: 연합으로 연결된 나라들은 어떻게 표시할 것인지? => union이라는 배열을 따로 만들어 연합이 되었으면 index값으로 갱신하여 구분함
#Q: 연합이 여러개라면 리스트에서 어떻게 구분할건지? => 위와 동일
#2. (연합총인구수)/(연합개수)로 인구수를 갱신한다
#bfs로 연합을 탐색할때마다 연합총인구수와 연합개수를 구하여 bfs가 끝날때 갱신해준다
#3. 1,2에 인구이동이 없을때까지 반복한다

from collections import deque

n,l,r = map(int, input().split())

a=[]
for _ in range(n):
    a.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#bfs를 수행하여 연합을 찾고 각 연합의 인구수를 갱신해주는 함수
def process(x,y,index):
    #연합 인덱스를 넣는 리스트
    united=[]
    united.append((x,y))
    union[x][y]=index
    q=deque([x,y])
    t_population = a[x][y]
    t_union = 1
    #bfs 수행
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nxt_x, nxt_y = now_x + dx[i], now_y + dy[i]
            if 0<=nxt_x<n and 0<=nxt_y<n and union[nxt_x][nxt_y]==-1:
                if l<= abs(a[nxt_x][nxt_y]-a[now_x][now_y]) <=r:
                    q.append((nxt_x,nxt_y))
                    union[nxt_x][nxt_y]=index
                    united.append((nxt_x,nxt_y))
                    t_population += a[nxt_x][nxt_y]
                    t_union+=1

    #bfs 수행후 인구수 갱신
    for i,j in united:
        a[i][j]=t_population // t_union

    return True

total_count = 0

while True:
    #연합을 표시하는 배열
    #인구이동 한번할때마다 union이 새롭게 생성되므로 이전 인구이동에 대한 연합번호 기록들이 Reset됨
    union = [[-1]*n for _ in range(n)]
    #연합번호
    index=0
    #인구이동
    #각 나라마다 process 함수를 실행해준다
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1:
                process(i,j,index)
                index+=1
    #Q: 이게 왜 종료조건이 되는지 모르겠음
    if index == n*n:
        break

    total_count += 1

print(total_count)