#Q: 정사각형 공간 즉 배열을 구현해야할 필요성이 있을까?
#A: 어차피 인덱스 즉 좌표만 알면 되므로 굳이 그 공간 자체를 구현할 필요는 없을듯

#접근법
#1. planner를 반복문을 돌려 순서대로 내용을 확인한다
#2. dx와 dy를 통하여 LRUD 가 나오면 해당 좌표로 이동한다 (좌표는 nx, ny로 계속 업데이트한다)
#3. 범위를 체크하여 공간을 벗어나면 무시한다
#4. 최종적으로 nx, ny를 출력한다

n=int(input())
planner = input().split()

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

x,y = 1,1

for plan in planner:
  if plan == "L":
    nx = x+ dx[0]
    ny = y+ dy[0]
  elif plan == "R":
    nx = x+dx[1] 
    ny = y+dy[1] 
  elif plan == "U":
    nx = x+dx[2] 
    ny = y+dy[2] 
  else:
    nx = x+dx[3]
    ny = y+dy[3]
  if 1<=nx<=n and 1<=ny<=n:
    x,y=nx,ny
    
print(x, y)

#1차시도) 성공
#부족한점) L, R, U, D를 모두 조건문으로 구현하기 보다 따로 리스트를 만들어 dx,dy와 대응하게 만든다면 좀 더 깔끔한 코드가 될것
#시간) 15분 소요