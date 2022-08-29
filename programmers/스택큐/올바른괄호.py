def solution(s):
    answer = True
    
    cnt = 0 #'('를 세어줄 카운트

    for paren in s:
        if paren == '(':
            #'('를 스택에 넣어준다
            cnt+=1
        else:
            #')'에 맞는 '('가 없는 경우 (스택이 비어있는 경우)는 올바른 괄호가 될 수 없다
            if cnt == 0: 
                return False
            #'('를 스택에서 빼준다
            cnt-=1

    #문자열을 모두 탐색한 뒤에도 '('가 남아있는 경우 올바른 괄호가 될 수 없다
    if cnt > 0:
        return False
    
    return True

s="(())()"
print(solution(s))