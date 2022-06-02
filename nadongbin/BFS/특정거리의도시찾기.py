from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for row in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  #graph[b].append(a) (간선은 단방향임!) 

dist = [-1]*(n+1)
result = []

def bfs(x):
  dist[x]=0
  q= deque([x])
  while(q):
    now = q.popleft()
    if dist[now]==k:
      result.append(now)
    elif dist[now]>k:
      break
    for nxt in graph[now]:
      if dist[nxt]==-1:
        q.append(nxt)
        dist[nxt]=dist[now]+1
  print('\n'.join(sorted(map(str,result))))

bfs(x)