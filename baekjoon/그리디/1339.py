#단어수학

#시간: 3:44~
#실패

#길이가 가장 1 이상으로 긴 단어의 첫번째 알파벳은 9가 되어야 할 것
#길이가 같다면 가능한 수들중 최대값부터 차례로 해당 번째 수에 배정한다
#위의 로직을 반복한다

#문자열을 길이별로 sort한다
#가장 긴 길이가 1 이상이라면 가장 긴 문자열의 첫번째 알파벳은 9로 부여한다
#가장 긴 길이가 1이라면 가장 긴 문자열의 알파벳을 10으로 부여한다
#그 다음 문자열의 길이와 같아질때까지 9부터 1까지 차례대로 1씩 줄여나가며 수를 부여한다
#만약 다음 수와 길이가 같아진다면 각 수에 가능한 수들 각각 부여한다



n=int(input())
alp = [0] * 7 #A~G의 숫자를 0으로 초기화
result = 0

str = []
for _ in range(n):
    str.append(input())

str.sort(key=len)

#가장 긴 문자열부터 알파벳을 하나씩 확인한다
#다음 문자열의 길이와 비교한다
#다음 문자열의 길이와 같아진다면 다음 문자열과 같은 크기에 숫자를 부여한다

l = 10
for i in range(len(str)):
    j, k = len(str[i]), len(str[i+1])
    if j != k and j > 1:
        l -= 1
        for _ in range(j):
            if j > k:
                if alp[65 - ord(str[i][j])] != 0:
                    result += alp[65 - ord(str[i][j])] * (j-1)
                else:
                    alp[65 - ord(str[i][j])] = l
                    result += alp[65 - ord(str[i][j])] * (j -1)
                    l -= 1
            j -= 1

    else:
        if alp[65 - ord(str[i][j])] != 0:
            result += alp[65 - ord(str[i][j])] * (j - 1)
        else:
            alp[65 - ord(str[i][j])] = l
            result += alp[65 - ord(str[i][j])] * (j -1)
            l -= 1

print(result)

        



        



print(str)