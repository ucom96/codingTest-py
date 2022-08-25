#bfs로 연결관계를 쭉 탐색후 (네트워크수 + 1)을 해준다
from collections import deque
def solution(n, computers):
    answer = 0

    visited = [False]*n

    def bfs(x):
        q = deque([x])
        visited[x] = True
        
        while q:
            i = q.popleft()
            for j in range(n):
                if computers[i][j] == 1 and visited[j]==False:
                    q.append(j)
                    visited[j]=True

        return 1

    for i in range(n):
        if visited[i]==False:
            answer+=bfs(i)

    return answer

n=3
computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))