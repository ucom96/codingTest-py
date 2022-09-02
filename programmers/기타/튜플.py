#11:17~
#집합을 집합의 길이별로 정렬한다
#=> 문자열을 정규표현식으로 split하여 각 집합을 배열의 원소형태로 만든다
#정답으로 반환될 튜플에 해당 집합의 요소가 없다면 튜플에 삽입 => n개의 요소를 가지는 집합까지 반복

def solution(s):
    answer = []
    #1)s의 집합들을 배열의 원소로 만들어준다
    s = s[2:-2].split("},{")
    s.sort(key = len)
    for i in s:
        ii = i.split(",")
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    #print(s)


    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))