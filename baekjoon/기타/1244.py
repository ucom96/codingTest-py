#스위치 켜고 끄기
#구현 문제

#남학생: 스위치 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꾼다
#여학생: 받은수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 구간의 스위치 상태를 모두 바꾼다
#2:38~3:10 (30분 이상 소요) - 실패

switch_num = int(input())
switch_state = [-1] + list(map(int, input().split()))
student_num = int(input())

info = []
for _ in range(student_num):
    info.append(list(map(int, input().split())))

def change_state(x):
    if x == 1:
        return 0
    else:
        return 1

#성별에 따른 로직을 짠다
#info의 첫 요소가 남학생이라면 이에 대한 배수의 상태를 모두 반대로 바꾼다
#info의 두번째 요소가 여학생이라면 좌우 요소의 상태를 비교한다 만약 같다면 옆으로 더 확장하고 다르다면 더 확장하지 않고 해당 요소만 바꿔준다
#Q: 어떻게 좌우 요소의 상태를 비교하고 더 확장해나갈 것인가?
#A: 수를 1부터 하나씩 늘려가면서 양옆을 그 수만큼 뺀다

for i in range(student_num):
    #만약 남학생이라면 range를 이용하여 배수인 부분의 상태를 바꿔준다
    if info[i][0] == 1:
        for j in range(info[i][1], switch_num+1, info[i][1]):
            switch_state[j] = change_state(switch_state[j])
    #만약 여학생이라면 길이를 1/2로 나눠서 좌우의 상태가 더이상 같아지지 않을때까지 상태를 바꿔준다
    if info[i][0] == 2:
        change_state(switch_state[info[i][1]])
        for j in range(1,len(switch_state)//2+1):
            if switch_state[info[i][1]-j] == switch_state[info[i][1]+j]:
                change_state(switch_state[info[i][1]-j])
                change_state(switch_state[info[i][1]+j])
            else:
                break
    print(switch_state)

for i in range(1, switch_num+1):
    print(switch_state[i], end = ' ')

        


        