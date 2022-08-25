#dfs로 끝까지 계산하여 target이 나온다면 answer+=1을 해주고 아니라면 다시 백트래킹하여 다른 길을 탐색한다
def solution (numbers, target):
    answer = 0
    def dfs(num, idx):
        nonlocal answer
        if idx == len(numbers):
            if num == target:
                answer+=1
            return
        dfs(num + numbers[idx], idx+1)
        dfs(num - numbers[idx], idx+1)
    dfs(0, 0)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))