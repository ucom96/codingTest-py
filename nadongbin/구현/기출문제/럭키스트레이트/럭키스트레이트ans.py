#파이썬은 데이터를 문자열 형태로 받으므로 len()를 쉽게 구할 수 있다
#len//2를 기준으로 왼쪽과 오른쪽의 합을 구한다
#다만, 왼쪽의 합을 구한 후 오른쪽에서 빼주면 값이 같았는지 아닌지 확인할 수 있고 로직이 더욱 간단해진다
#그렇게 구한 결과값이 0이 된다면 LUCKY를 출력, 아니라면 READY를 출력

score = input()

length = len(score)

summary = 0

#왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
    summary += int(score[i])

#오른쪽 부분의 자릿수 합 빼기
for i in range(length//2,length):
    summary -= int(score[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")