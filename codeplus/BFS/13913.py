#숨바꼭질4
#알고리즘: BFS & 재귀
#1차시도) Recursion Error: 파이썬이 정한 최대 깊이보다 더 깊은 재귀 발생시
#해결) sys.setrecursionlimit: 최대 재귀 깊이 변경
#2차시도) for문으로 via 추적하여 출력 (시간 감소)

import sys
sys.setrecursionlimit(10**6)
from collections import deque

n,k=map(int, input().split())
MAX = 200000
#방문체크 배열
visited = [False]*(MAX+1)
#최소비용 배열
dist = [0]*(MAX+1)
#이전 노드 저장 배열 (역추적 배열)
via = [0]*(MAX+1)

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
        #역추적 배열에 이전 노드를 저장
        via[nxt]=now
  print(dist[k])

def dist_print(k):
  result =[]
  temp =k
  for i in range(dist[k]+1):
    result.append(temp)
    temp=via[temp]
  return ' '.join(map(str,result[::-1]))


bfs()
print(dist_print(k))