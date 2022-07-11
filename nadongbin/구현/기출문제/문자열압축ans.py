#단위마다 문자열을 잘라서 앞뒤 문자열을 각각 비교한다
#sol) 단위를 1부터 문자열길이/2 까지 1씩 증감시키며 확인해간다
#rea) 반복되는 문자열이란건 최소 2개이상의 문자열이 같아지는 것을 말하므로 문자열길이/2를 단위로 하면 최소 2개가 나오는 맥시멈 길이이므로 문자열길이/2로 설정해주었다

#잘라진 문자열의 앞뒤를 비교한다
#sol) 문자열을 자르기 위해서 인덱싱을 사용한다
#sol) 특정 문자열이 반복될 경우 cnt+문자열로 변경되어야하므로 앞의 문자열을 기억하기 위해 prev라는 변수에 저장해둔다
#sol) prev에 저장된 문자열과 인덱싱을 사용하여 잘라낸 문자열이 서로 같은지 확인한다
#sol) 문자열의 앞뒤가 같다면 cnt를 증감해준다
#sol) 문자열의 앞뒤가 다르다면 cnt를 확인한다 cnt가 2 이상이면 반복된 문자열이 있었다는 것이므로 새롭게 생성될 문자열에 cnt+prev를 붙여주고 아니라면 prev만 붙여준다

#단위마다 나온 새롭게 생성된 문자열의 길이를 각각 비교하여 가장 작은 값을 리턴한다
#sol) result를 작은 값들과 비교한다고 매우 큰 값으로 설정하지 않고 len(s)로 설정한다 비교시 가장 크게 나올 값이 len(s)이기 때문에

def solution(s):
    result = len(s)

    for step in range(1,len(s)//2+1):
        #print('step',step)
        #매 단위마다 새롭게 생성될 문자열
        compressed = ''
        #앞뒤 비교시 앞의 문자열
        prev = s[0:step]
        cnt=1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                cnt+=1
            else:
                compressed += str(cnt)+prev if cnt>=2 else prev 
                cnt=1
                prev = s[j:j+step]
        #prev의 마지막 요소로 else문에서 바뀔시 for j 문은 실행되지 않을 것이다. 왜냐하면 prev의 끝 요소에서 step을 더 더한 결과가 나오면 len(s)를 넘어갈 것이므로.
        #따라서 prev의 마지막 요소가 compressed에 더해질 수 있도록 이 부분에서 예외처리를 해줄 것!
        compressed += str(cnt)+prev if cnt>=2 else prev      
        result = min(result, len(compressed))
        #print(compressed)

    return result

strs=["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]

for i in strs:
    print(solution(i))