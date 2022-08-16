from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)


#방문처리 & 최단거리에 대한 정보를 담은 배열
distance = [-1]*(n+1)

#도로의 거리 비용이 모두 1이므로 bfs를 사용해서 최단거리를 구할 수 있음
#각 도시의 최단거리를 모두 구한 후 k인 최단거리가 있다면 도시의 번호를 정렬하여 출력, 없다면 -1 출력
def bfs(x):
    q=deque([x])
    distance[x]=0

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if distance[nxt]==-1:
                q.append(nxt)
                distance[nxt]=distance[now]+1

bfs(x)

check = False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True

if check == False:
    print(-1)
