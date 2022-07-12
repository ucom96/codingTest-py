#4:10~4:25 (15분 소요)
#성공 - 테스트케이스 값들은 잘 나옴
#1. 현재 점수를 자릿수를 기준으로 반으로 나눈다
#2. 나눠진 자릿수들의 합을 구해서 비교한다
#3. 자릿수의 합이 같다면 LUCKY를 출력한다
#4. 아니라면 READY를 출력한다

#자릿수를 기준으로 반으로 나누기 위해 인덱싱을 사용한다
#인덱싱을 사용하고 그로 인한 sum()함수를 사용하기 위해 score를 int형 원소들을 가진 배열로 바꿔주었다
#배열이므로 길이를 구할 수 있어 배열길이 // 2 의 길이를 기준으로 하여 인덱싱을 한후 sum 값을 구하여 비교하였다

score = list(map(int,[i for i in str(int(input()))]))

#print(score)

j = len(score)//2

if sum(score[0:j]) == sum(score[j:]):
    print("LUCKY")
else:
    print("READY")



