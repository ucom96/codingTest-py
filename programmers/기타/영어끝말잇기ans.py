def solution(n, words):
    answer = []

    #앞 사람의 단어의 끝 문자와 현재 사람의 단어의 앞 문자가 다를 경우
    #이전에 나온 단어일 경우
    #[번호, 차례]를 리턴한다

    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    
    else:
        return [0,0]

n=2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))