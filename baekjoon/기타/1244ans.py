n = int(input())
#스위치가 1부터 시작하므로 0번째에는 -1을 넣어준다
state = [-1] + list(map(int, input().split()))
student_n = int(input())

def change(x):
    if x == 1:
        return 0
    else:
        return 1

for _ in range(student_n):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num, n+1,num):
            state[i] = change(state[i])

    else:
        state[num] = change(state[num])
        for i in range(1,n//2):
            if num - i < 1 or num + i > n:
                break
            if state[num + i] == state[num - i]:
                state[num - i] = change(state[num - i])
                state[num + i] = change(state[num + i])
            else:
                break
    
    #print(state)

for i in range(1, n+1):
    print(state[i], end = ' ')
    if i % 20 == 0:
        print()
