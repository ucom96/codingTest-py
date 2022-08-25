#언더프라임 (시간초과)

#1) 자연수 X를 소인수분해한다
#2) 소인수분해해서 구한 소수의 개수를 구한다
#3) 개수가 소수라면 X를 언더프라임이라고 칭한다
#4) A와 B 사이에서 언더프라임의 개수를 구한다

import math

a,b = map(int, input().split())

#소수판별 함수
def isPrime(n):
    #약수가 하나라도 있다면 소수가 아님!
    #약수의 유무를 검사
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#소인수분해한 후 소수의 개수 구하는 함수
def fact(n):
    cnt =0
    while n>1:
        #print('n=',n)
        for i in range(2,n+1):
            if n % i == 0 and isPrime(i):
                n = n//i
                cnt+=1
                break
    return cnt

result = 0

for i in range(a,b+1): 
    if isPrime(fact(i)):
        result+=1

print(result)