#코드플러스 참고
#그래프를 통해 연결된 노드들을 표시후 루트노드부터 시작하여 부모노드 탐색
import sys
from collections import deque

n=int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  
parentInfo = [0]*(n+1)
visited=[False]*(n+1)

def bfs(v):
  q=deque([v])
  visited[v]=True
  
  while q:
    now = q.popleft()
    for nxt in graph[now]:
      if visited[nxt]==False:
        q.append(nxt)
        visited[nxt]=True
        parentInfo[nxt]=now
 
bfs(1)
for i in range(2,n+1):
  print(parentInfo[i])

