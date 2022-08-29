#성공
'''
1)record를 돌면서 명령이 'enter'혹은 'change'일 경우 각 아이디에 대한 닉네임을 딕셔너리 형태로 저장한다
2)다시 record를 돌면서 'enter' 혹은 'leave'에 해당하는 해당 아이디의 닉네임과 문구를 출력한다
'''
def solution(record):
    answer = []
    
    dic = {}

    #아이디에 대한 닉네임 딕셔너리 형태로 저장하기
    for str in record:
        tmp = str.split()
        if tmp[0] == "Leave":
            continue
        else:
            dic[tmp[1]] = tmp[2]
    
    #명령문에 해당하는 result 출력하기
    for str in record:
        tmp = str.split()
        if tmp[0] == "Enter":
            answer.append("%s님이 들어왔습니다." %dic[tmp[1]])
        elif tmp[0] == "Leave":
            answer.append("%s님이 나갔습니다." %dic[tmp[1]])
    
    #print('dic = ', dic)

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))