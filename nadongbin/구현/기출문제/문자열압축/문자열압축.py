#1. 단위를 1개부터 문자열의 길이가 될때까지 1씩 증감시켜 해당 단위로 나눌 수 있는지 확인한다
#2. 단위를 정했으면 문자열 첫 시작의 해당 단위만큼의 문자열과 그 다음 단위의 문자열이 같은지 확인한다
#3. 문자열이 서로 같다면 cnt를 증감시킨다
#4. 문자열이 서로 다르다면 cnt와 단위를 합쳐 문자열을 바꿔주고 cnt를 0으로 초기화한다
#5. 문자열의 총 길이를 저장한다
#6. 단위마다의 길이중 가장 작은 길이를 리턴한다

def solution(s):
    result = 1e9
    lth = len(s)
    for unit in range(1,lth+1):
        cnt=0
        s_cp = s
        #단위로 인해 인덱싱하면 범위의 예외처리를 어떻게 할것인지
        for i in range(0,lth,unit):
            j = i+unit
            if j+unit < lth:
                tmp = s[i:i+unit]
                if s[i:i+unit] == s[j:j+unit]:
                    cnt+=1
                else:
                    if cnt >0:
                        #반복된 만큼의 문자열을 어떻게 변경해야할지 모르겠음
                        s_cp.replace()
                    cnt=0
        result = min(result, len(s_cp))
    return result


s="aabbaccc"

print(solution(s))

#실패