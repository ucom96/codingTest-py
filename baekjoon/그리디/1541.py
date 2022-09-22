#잃어버린 괄호
#3:32~

#첫시도) 모르겠음 로직이 전혀 안떠오름
#구글링) 마이너스를 만날 때 가장 큰 수를 뺄것
#마이너스 기호를 만날 때 다음 마이너스까지, 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한번에 빼줄것

str = input().split("-")

result = 0

#마이너스 단위로 문자열을 나눈다
#마이너스 단위로 나눠진 문자열들끼리는 서로 -를 해준다
#마이너스 단위로 나눠진 문자열 안에서는 각자를 +로 나누고 모두 더해준다

for i in range(len(str)):
    tmp = sum(list(map(int, str[i].split("+"))))
    if i < 1:
        result += tmp
    else:
        result -= tmp

print(result)
