#3:43~4:11 (28분 소요)
#첫시도) 성공 but 코드를 좀더 효율적이고 짧게 구현할 수 있을듯함

#공백 다음을 대문자로 바꿔줄 것
#공백을 인식
#이렇게 코드를 짤 경우 문제점: 연속되서 나온 공백을 알 수 없음 (저장된게 없으므로)
"""
def solution(s):
    answer = ''
    #공백을 기준으로 문자열을 나누어 배열에 저장한다
    str = s.split()
    #나누어진 문자열을 하나씩 확인하며 맨 앞 글자가 숫자인지 아닌지 판별한다
    #만약 숫자가 아니라면 맨 앞 글자를 대문자로 바꾸어 다시 저장해준다
    #Q: 맨 앞 글자가 숫자인지 아닌지 어떻게 판별할 것인가?
    #A: 문자열.isdigit()함수 사용 => 만약 숫자라면 True를 반환
    for st in str:
        if not st[0].isdigit():
            st = st.replace(st[0], st[0].upper()) #for문에서의 st가 아닌 아예 새로운 변수 st로 할당됨
            #st[0] = st[0].upper() => TypeError: 'str' object does not support item assignment

    answer = ''.join(str)


    return answer
"""

#공백이 연속되서 나올 수 있으므로 연속된 공백을 유지하기 위해 문자열 하나씩 탐색해간다
#현재 만난 문자가 첫 문자 혹은 공백 다음 문자라면 해당 문자가 숫자인지 판별한다 => isdigit() 사용
#위의 경우가 아니거나 숫자라면 새로운 문자열 answer에 해당 문자를 그냥 더해준다
#숫자가 아니라면 새로운 문자열 answer에 해당 문자를 대문자로 바꿔 더해준다

def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0:
            if not s[i].isdigit():
                answer += s[i].upper()
            else:
                answer += s[i]
        else:
            if s[i-1] == " " and s[i] != " ":
                if not s[i].isdigit():
                    answer += s[i].upper()
                else:
                    answer += s[i]
            else:
                answer += s[i].lower()
    return answer

s = "3people unFollowed me"

print(solution(s))