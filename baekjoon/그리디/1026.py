#2:56~3:07 (11분 소요)
#첫 시도) 성공 / 시간:72ms

#보물
#result가 최솟값이 되기 위해서는 최댓값 * 최솟값 의 형태를 띄어야함
#각 곱을 더하는 것이므로 더하기는 순서에 상관이 없으므로 b배열도 재배열해도 노상관
#b의 0에 가장 큰 값을 곱한다
#b의 값이 클수록 값이 작은 a의 값을 곱해준다
#b의 값이 작을수록 값이 작은 b의 값을 곱해준다
#a를 오름차순으로 정렬한다
#b를 내림차순으로 정렬한다
#각각을 곱해서 더해준다
result = 0
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(n):
    result += a[i] * b[i]

print(result)
