#3:20~
def solution(s):
    answer = -1
    #스택 이용
    #붙어있는 두개의 알파벳을 알아내기 위해 매번 처음부터 끝까지 간다면 시간초과가 남
    #두개의 알파벳 중 마지막 알파벳으로 두 알파벳이 붙어있음을 알아낼 수 있으므로 마지막이 중요한 스택을 이용함을 캐치한다
    #스택을 이용하게 되면 총 O(n)만큼의 시간만 소요되므로 매우 효율적으로 해결할 수 있다

    stack = []
    
    #스택을 확인한다
    #스택에 자신과 똑같은 알파벳이 있다면 해당 알파벳을 빼고 그 다음으로 넘어간다
    #스택이 비어있거나 자신과 똑같은 알파벳이 없다면 현재의 알파벳을 스택에 넣어준다
    #최종적으로 모든 문자열을 돌았는데 스택이 비어있다면 1 비어있지 않다면 0

    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        print(stack)

    if not stack:
        answer = 1
    else:
        answer = 0

    return answer

s = "cdcd"

print(solution(s))