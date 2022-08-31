#4:25~
def solution(n):
    answer = ''
    numbers = ["1","2","4"]

    while n != 0:
        n-=1
        answer = numbers[n%3] + answer
        n = n//3
    
    #이걸 굳이 하지 않고 line 8dptj answer = numbers[n%3] + answer로 하면 끝남!
    #answer = answer[::-1]

    return answer

n=5
print(solution(n))