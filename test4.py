def solution(s):
    answer = len(s)

    for unit in range(1, len(s)//2+1):
        cnt =1 
        compressed = ""
        now_str = s[:unit]
        for idx in range(unit,len(s), unit):
            nxt_str = s[idx: idx+unit]
            if now_str == nxt_str:
                cnt+=1
            else:
                if cnt == 1:
                    compressed += now_str
                else:
                    compressed += str(cnt) + now_str
                now_str = nxt_str
                cnt = 1
        if cnt == 1:
            compressed += now_str
        else:
            compressed += str(cnt) + now_str
    
        if answer > len(compressed):
            answer = len(compressed)
    return answer

s = "abcabcdede"

print(solution(s))

