#2:55~
n= int(input())
n_nums = list(map(int, input().split()))

m= int(input())
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
            binary_search(l,mid-1,x)
        elif n_nums[mid]<x:
            binary_search(mid+1,r,x)

for x in m_nums:
    print(binary_search(0,len(n_nums)-1,x))
