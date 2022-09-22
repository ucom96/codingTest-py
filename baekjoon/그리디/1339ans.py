#A~G의 값을 0으로 초기화하여 딕셔너리 형태로 저장한다

alp = {"A":0, "B":0, "C":0, "D":0, "E":0,"F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0,"M":0, "N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}

n = int(input())

str = []
str_list = []
answer = 0

for _ in range(n):
    str.append(input())

#str의 문자열을 하나씩 확인하며 각 알파벳이 몇개 있고 얼마 크기로 나오는지 확인하여 alp에 저장할것
for s in str:
    for j in range(len(s)):
        alp[s[j]] += 10 ** (len(s) - j - 1)

#0이 아닌 값들을 모두 저장하여 큰 수부터 나올 수 있도록 내림차순 정렬한다
for i in alp.values():
    if i > 0:
        str_list.append(i)
sorted_list = sorted(str_list, reverse=True)

#큰 수부터 9...1로 곱하여 answer에 더해준다
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)