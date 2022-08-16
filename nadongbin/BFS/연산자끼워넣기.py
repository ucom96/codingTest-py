n=int(input())

#숫자들의 연결관계(들어오는 순서대로 연결된 것이므로 순차적으로 일차원 배열로 표현)
a = list(map(int, input().split()))

#print(a)

min_value = 1e9
max_value = -1e9

#연산자 정보 담는 배열
plus, minus, multiply, division = map(int, input().split())

#dfs로 모든 경우의 값을 계산하여 최대최소를 비교한다
#num: 계산된 숫자값 i: 연산횟수
def dfs(num, i):
    global plus, minus, multiply, division, min_value, max_value
    print('num', num, 'i', i)
    if i == n:
        min_value = min(min_value, num)
        max_value = max(max_value, num)
    else:
        #if가 아닌 elif로 두게 된다면 끝까지 탐색후 더이상 갈 곳이 없을때 다시 돌아와서 옆으로 갈 수가 없게됨!
        if plus >0:
            plus-=1
            dfs(num+a[i],i+1)
            plus+=1
        if minus >0:
            minus-=1
            dfs(num-a[i],i+1)
            minus+=1
        if multiply >0:
            multiply-=1
            dfs(num*a[i],i+1)
            multiply+=1
        if division >0:
            division-=1
            dfs(num//a[i],i+1)
            division+=1
    

dfs(a[0],1)
print(max_value)
print(min_value)

