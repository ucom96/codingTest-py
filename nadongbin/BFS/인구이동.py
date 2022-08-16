#12:36~
#1. 연합을 찾는다
#각 나라마다 BFS로 연합(연결된 그래프)를 찾는다
#Q: 매번 각 나라마다 BFS 연산을 수행하면 시간복잡도가 너무 커지진 않을지?
#Q: 연합과 관련된 정보를 어디에 어떻게 저장할지? => 리스트에
#Q: 연합으로 연결된 나라들은 어떻게 표시할 것인지? => 인덱스를 저장
#Q: 연합이 여러개라면 리스트에서 어떻게 구분할건지? => 이중리스트로 저장?
#각 나라마다 BFS로 연합을 찾고 리스트에 인덱스를 저장
#2. (연합총인구수)/(연합개수)로 인구수를 갱신한다
#인덱스를 저장할때마다 총인구수에 계속 더해줘서 구함
#인덱스를 하나씩 꺼내서 인구수를 갱신한 값으로 바꾼다
#3. 1,2에 인구이동이 없을때까지 반복한다
from collections import deque

n,l,r= map(int, input().split())

a=[]
for _ in range(n):
    a.append(list(map(int, input().split())))

def bfs(x,y):
    q=deque([(x,y)])
    
    return True

for i in range(n):
    for j in range(n):
        bfs(i,j)
