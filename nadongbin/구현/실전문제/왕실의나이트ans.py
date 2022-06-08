#시뮬레이션 성격을 가진 브루트포스 문제
#이동할 수 있는 모든 경우의 수를 확인하여 좌표평면을 벗어나느지 확인
input_data = input()
row = int(input_data[1])
#column을 이렇게 구현하는 것이 좀 더 가독성이 있는듯!
column = int(ord(input_data[0])) - int(ord('a')) +1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]
  
  if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
    result+=1
    
print(result)