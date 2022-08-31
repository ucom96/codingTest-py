#2:55~3:23
#성공
n = int(input())
n_nums = list(map(int, input().split()))

m = int(input())
m_nums = list(map(int, input().split()))

n_nums.sort()

def binary_search(l,r,x):
    if l > r:
        return 0
    mid = (l + r)//2
    if n_nums[mid] == x:
        return 1
    else:
        if n_nums[mid]>x:
            #주의)여기서 return을 꼭 붙여줄것! 다음 호출의 반환값이 반환되어야 하기 때문에
            return binary_search(l,mid-1,x)
        elif n_nums[mid]<x:
            return binary_search(mid+1,r,x)

for x in m_nums:
    print(binary_search(0,len(n_nums)-1,x))
