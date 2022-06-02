#숨바꼭질
#알고리즘: BFS
#사용이유
#1) 최소비용을 찾는 문제
#2) 하나의 정점에서 다른 정점으로 이동시
#3) 최소비용과 가중치가 갖는 의미가 같음
#4) 가중치가 1임

from collections import deque

n,k=map(int, input().split())
MAX = 200000
#방문체크 배열
visited = [False]*(MAX+1)
#최소비용 배열
dist = [0]*(MAX+1)


def bfs():
  q=deque([n])
  visited[n]=True
  while(q):
    now=q.popleft()
    #now에서 갈 수 있는 곳 (후보)
    for nxt in [now-1,now+1,now*2]:
      #아직 방문하지 않았고 범위안에 있다면 방문
      if 0 <= nxt <= MAX and visited[nxt]==False:
        q.append(nxt)
        visited[nxt]=True
        dist[nxt]=dist[now]+1
  return dist[k]


print(bfs())

#노드: 인덱스
#가중치: 값