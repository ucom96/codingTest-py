def solution(record):
    answer =[]

    #아이디와 닉네임을 저장할 딕셔너리
    namespace = {}
    #명령에 대한 문구를 출력해줄 딕셔너리
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

    for str in record:
        tmp = str.split()
        #'enter' 혹은 'change' 명령이라면 닉네임을 저장 및 갱신해준다
        if tmp[0] in ['Enter', 'Change']:
            namespace[tmp[1]] = tmp[2]

    for str in record:
        #'enter' 혹은 'leave' 명령이라면 해당 명령에 대한 문구를 출력한다
        if str.split()[0] != 'Change':
            answer.append(namespace[str.split()[1]] + printer[str.split()[0]])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))