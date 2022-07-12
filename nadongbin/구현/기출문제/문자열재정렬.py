#2:35~45 (10분 소요)
#90% 통과

#1. 모든 알파벳을 오름차순으로 정렬하여 출력한다
#2. 모든 숫자를 더한 값을 이어서 출력한다

#알파벳과 숫자를 구분한다 (아스키코드 이용)
#알파벳의 아스키코드: 65~90
#숫자의 아스키코드: 48~57
#문자열의 문자를 하나씩 돌아가며 알파벳인지 숫자인지 탐색한다
#알파벳이라면 배열에 넣어둔다
#숫자라면 int형으로 바꾼뒤 cnt라는 변수에 넣어두고 계속 더해준다
#배열을 문자열로 바꾼뒤 숫자 역시 문자 형태로 바꾸어 둘을 이어준다
#결과값을 출력한다

s=input()
result = ''
ch=[]
num=0
for i in s:
    if 65<=ord(i)<=90:
        ch.append(i)
    else:
        num+=int(i)

result = ''.join(sorted(ch))+str(num)
print(result)

#놓친부분)
#알파벳과 숫자를 구분하는데에는 아스키코드도 좋지만 문자.isalpha()라는 함수를 사용할것!
#숫자가 존재하지 않을수도 있으므로 그럴경우에 num=0이 아닐 경우에만 result의 뒤에 붙여주도록 할 것!
