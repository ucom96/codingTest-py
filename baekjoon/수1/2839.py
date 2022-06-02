#dp
#c[n]=min(c[a]+c[n-a]) 

n=int(input())
dp=[-1]*(5001)
dp[3]=1
dp[5]=1

for i in range(5,n+1): 
  for j in range(1,i//2+1): 
    a=dp[j] 
    b=dp[i-j] 
    if a==-1 or b==-1: 
      continue
    else:
      if dp[i]==-1:
        dp[i]=a+b
      else:
        dp[i]=min(dp[i],a+b)

print(dp[n])