#공유기 설치
#가장 인접한 두 공유기 사이의 최대 거리 구하기
#선형 탐색으로 한다면 최대 10억번 탐색하게 되므로 이분탐색으로 최대거리를 구하고자 한다

#알고리즘: 이분탐색 이용
#최대거리를 mid로 잡은후
#mid를 기준으로 공유기를 설치할 수 있는 집의 개수가 c보다 작다면 공유기를 설치할 여유가 없으므로 왼쪽 영역을 탐색한다
#mid를 기준으로 공유기를 설치할 수 있는 집의 개수가 c보다 큰 경우 공유기를 설치할 여유가 있으므로 오른쪽 영역을 탐색한다
 
import sys

answer = 0
n,c = map(int, sys.stdin.readline().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))

houses.sort()
start, end = 1, houses[-1]-houses[0]

while start <= end:
    mid = (start + end) // 2
    cur = houses[0] #맨 왼쪽 집에 무조건 공유기 1개를 설치한다 그래야만 인접한 두 공유기 사이가 최대가 될 수 있으므로
    count = 1 #공유기를 설치한 집의 개수

    for i in range(1, len(houses)):
        #houses에 있는 집에 공유기를 설치할 수 있다면
        if houses[i] >= cur + mid:
            count += 1 #공유기를 설치한다
            cur = houses[i] #해당 집을 기준으로 mid이상의 거리에 공유기를 또 설치할 수 있는지 알아본다

    #공유기 설치가능한 집의 개수가 c보다 크거나 같다면 공유기를 설치하는 거리의 여유가 있으므로 mid 값을 늘리기 위해 오른쪽 영역을 탐색한다
    if count >= c:
        start = mid + 1
        answer = mid
    #공유기 설치가능한 집의 개수가 c보다 작다면 공유기 설치에 여유가 없으므로 더 작은 mid 값을 만들기 위해 왼쪽 영역을 탐색한다
    else:
        end = mid - 1

print(answer)