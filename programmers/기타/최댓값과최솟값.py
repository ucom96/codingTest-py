#3:06~3:14 (8분 소요)
#첫시도) 성공은 했으나 코드가 너무 지저분하고 살짝 비효율적인 느낌이 남


def solution(s):
    #공백으로 구분된 숫자들을 공백으로 나누어 배열에 저장한다
    #배열에서 min, max 함수를 이용하여 최소값과 최댓값을 찾는다
    #최소, 최댓값을 찾기 위해서는 배열의 원소 타입이 int 형태이어야한다
    #최소 최대를 공백으로 구분하여 answer라는 문자열에 저장한다
    answer = ''
    tmp = list(map(int,s.split()))
    answer = "%d %d" %(min(tmp), max(tmp))
    #answer = str(min(tmp)) + " " + str(max(tmp))로 해도됨
    #join은 배열의 원소들 타입이 str 형태이어야함
    return answer

s = "-1 -2 -3 -4"
print(solution(s))