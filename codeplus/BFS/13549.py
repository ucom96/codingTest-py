#숨바꼭질3
#가중치가 0 혹은 1
#tip 1) 가중치 0에 대한 현재큐, 가중치 1에 대한 다음큐 생성
#tip 2) 덱의 앞에 가중치 0짜리, 덱의 뒤에 가중치 1짜리
from collections import deque
MAX = 200000
#최소비용 배열
answer=[-1]*(MAX+1)
n,k=map(int, input().split())

def bfs():
  #n에 대한 방문처리
  answer[n]=0
  #큐생성
  q=deque([n])
  #큐가 비어있을때까지 반복
  while(q):
    #큐에서 하나 뽑음
    now = q.popleft()
    #뽑은 now 노드에서 갈 수 있는 노드
    for nxt in [now-1, now+1, now*2]:
      #범위체크와 방문체크
      if 0<=nxt<=MAX and answer[nxt]==-1:
        #순간이동시
        if nxt == now*2:
          q.appendleft(nxt)
          answer[nxt]=answer[now]
        #순간이동 아닌시
        else:
          q.append(nxt)
          answer[nxt]=answer[now]+1
  return answer[k]

print(bfs())
#print(answer)
