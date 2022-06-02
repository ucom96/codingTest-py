#해결) 식을 도출할 것
#a*days - b*(days-1) >= v
#a*days -b*days +b >= v
#(a-b)*days >=v-b
#days>=(v-b)/(a-b)
#days = (v-b)/(a-b) (나누어떨어지면)
#days = (v-b)/(a-b)+1
import sys
a,b,v= map(int, sys.stdin.readline().split())

days = 0

if (v-b)%(a-b)==0:
  days = (v-b)//(a-b)
else:
  days = (v-b)//(a-b)+1
  
print(days)