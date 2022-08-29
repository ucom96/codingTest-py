#요약) 자를 수 있는 단위별로 문자열을 압축하여 가장 짧은 길이를 리턴한다
#자를 수 있는 단위를 설정한다
#=> 작게는 1부터 가장 긴 단위는 문자열길이의 1/2이 될 것이다 왜냐하면 문자열길이의 1/2을 넘어가면 단위가 같으며 앞뒤로 똑같은 문자열이 있을 수 없기 때문
#단위별로 문자열을 자른다
#=> 슬라이싱을 통하여 문자열을 자른다
#문자열이 앞뒤로 같다면 카운트를 증감시킨다 (앞으로 같은 문자열이 더 나올 수 있으므로)
#문자열이 앞뒤로 다르다면 더이상 같은 문자열로 압축할 수 없다는 뜻이므로 이전 문자열을 압축하여 새로 압축되는 문자열에 넣어준다
#=> 이 경우 카운트를 확인하여야 한다 카운트가 1일때와 아닐때가 압축형태가 달라지기 때문
#=> 카운트가 1이라면 문자열만 추가해주고 1이상이라면 카운트와 문자열을 함께 넣어준다
#=> 단위가 달라질 때마다 이전 단위에서의 문자열 길이와 함께 비교하여 가장 작은 길이를 result에 넣는다
def solution(s):
    result = len(s)
    
    for unit in range(1, len(s)//2+1):
        cnt = 1
        compressed = ""
        for idx in range(0, len(s), unit):
            now_str = s[idx:idx+unit]
            nxt_str = s[idx+unit:idx+unit*2]

            if now_str == nxt_str:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += now_str
                else:
                    compressed += str(cnt) + now_str
                cnt = 1
        result = min(result, len(compressed))

    return result

s = "abcabcabcabcdededededede"

print(solution(s))