#8:22~9:02 (40분 소요)
#30/100

#차례를 파악할 수 있도록 할 것
    #=> n단위로 묶어가면 됨
    #=> cnt를 세고 cnt가 n과 같아진다면 차례를 1 올리고 그 후에 다시 cnt를 0으로 초기화
#이전에 나온 단어를 저장할 것
    #=> 이전에 나온 단어라면 탈락시킬것
    #=> words를 하나씩 빼오면서 다른 리스트에 넣어두고 다른 리스트에 같은 단어가 있는지 없는지 확인할 것
#이전의 단어의 끝 문자와 현재 단어의 앞 문자를 비교할것
    #=> 이전 단어의 끝 문자로 시작하는지 startswith함수 사용할 것

def solution(n, words):
    answer = []

    lst = []
    cnt, turn = 2,1
    lst.append(words[0])
    for i in range(1,len(words)):
        tmp = words[i-1][-1]

        print(words[i], cnt, turn)
        if words[i] in lst or words[i].startswith(tmp) == False:
            answer.append(cnt)
            answer.append(turn)
        else:
            lst.append(words[i])
        if cnt == n:
            turn += 1
            cnt = 1
        else:
            cnt += 1

    if not answer:
        return [0,0]
    else:
        return answer

n=2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n,words))