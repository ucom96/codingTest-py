#게임

#먼저, 절대로 z가 바뀔 수 없는 히든 케이스를 특정할 것
#1) 이긴 횟수 = 경기 횟수, 승률이 100%이므로 승률이 더 오를 수 없다
#2) 승률이 99%인 경우 한번이라도 졌으므로 승률이 100%가 될 수 없다

#위의 두 예외 케이스를 제외하고는 이진 탐색으로 접근 가능하다
#총 게임횟수가 1~10억 까지 이므로 이 중에서 승률이 오르는 최소 횟수를 구한다
#mid값을 승률이 오르는 최소횟수(new_z)로 설정하고 새롭게 승률을 구하여 기존의 승률(z)와 비교한다
#new_z <= z인 경우, start를 mid+1로 만들어 오른쪽 영역을 탐색하도록 한다
#new_z > z인 경우, end를 mid-1로 만들어 왼쪽 영역을 탐색하고 new_z가 z보다 크므로 answer에 mid값을 넣어준다
#위와 같은 과정을 start > end가 될때까지 반복하면 answer에는 승률이 오르는 최소 횟수가 들어가게 된다
import sys

x,y = map(int, sys.stdin.readline().split())
#z = (y / x) * 100
z = y * 100 // x
answer = 0

#예외 케이스
if x == y or z == 99:
    answer = -1

start, end = 1, 1000000000

while start <= end:
    mid = (start + end) // 2
    new_z = (y + mid) * 100 // (x + mid)

    if new_z > z:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)


