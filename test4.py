from collections import deque

n,m,k,x = map(int, input().split())
#그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

#distance가 k인 노드들을 담을 배열
result = []
#방문한 노드들에 대한 방문처리
visited = [False for _ in range(n+1)]

#distance와 노드의 번호를 튜플로 묶어 함께 큐에 넣어주고 distance가 k인 노드들을 따로 리스트에 담아둔다
#만약 리스트가 비어있을 경우 최단거리가 존재하지 않으므로 -1을 출력
def bfs(x):
    q=deque([(x,0)])
    visited[x] = True

    while q:
        now, d = q.popleft()
        d+=1
        for nxt in graph[now]:
            if visited[nxt]==False:
                if d == k:
                    result.append(nxt)
                q.append((nxt,d))
                visited[nxt]=True

    if len(result)==0:
        print(-1)
    else:
        result.sort()
        for node in result:
            print(node)

bfs(x)
