n = 3
m = 4
answer = "%d %d" % (n, m)

print(answer)

result = "{} {}".format(n, m)
print(result)

a = [1,2,3,4,5]

a.pop(2) #2가 나가는 것이 아닌 2번째 원소가 나가게됨

print(a)

a = [[1,2,3],[1,4,6],[3,1,6]]
b = [1,2,3,1]

print(max(map(max,a))) #2차원 배열에서 가장 큰 값을 출력
print(b.count(1))

#이중 포문 빠져나가기: exit(0)

arr = []

if not arr:
    print("hi")
else:
    print("h")

fl = [[1,2]]

print(fl.pop()[1])