result = 0
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#a를 오름차순으로 정렬
a.sort()

for i in range(n):
    x = a[i]
    #b에서 가장 큰 값을 더해준뒤 b라는 배열에서 뺀다
    #따라서 max를 사용할 때마다 b에서 가장 큰 값이 나오도록 한다
    y = b.pop(b.index(max(b)))

    result += x * y

print(result)
