#트리의 부모 찾기
#Q) 부모노드와 자식노드의 연결을 어떻게 구현할 것인가?
#A) 현재노드가 트리의 노드중 하나라면 1로 표시하고 1로 표시되어있는 노드를 부모노드로 인식한다
#실패) 입력받을때 트리에 연결되지 않은 노드들이 주어질 수도 있으므로

import sys

n=int(sys.stdin.readline())

treeInfo = [0]*(n+1) #부모노드를 저장할 배열
treeInfo[1]=1 #루트노드 표시
parentInfo=[0]*(n+1)

for _ in range(n-1):
  a,b= map(int, input().split())
  if treeInfo[a]==1:
    parentInfo[b]=a #b노드의 부모는 a노드
    treeInfo[b]=1 #b노드가 a노드와 연결되었으므로 트리의 구성원이됨
  else:
    parentInfo[a]=b
    treeInfo[a]=1
  
#print(parentInfo)

for i in range(2,n+1):
  print(parentInfo[i])

