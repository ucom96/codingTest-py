#words = [input() for _ in range(3)]

#print(words)

'''
str = "hello"
for i,c in enumerate(str):
  print(i,c)
'''
'''
from collections import deque

q=deque([[1,2],[2,3]])
print(q)

#lst = [range(1,4)]
#print(lst)




lst = [i for i in range(1,4)]
print(lst)
'''
'''
lst = [[1,2],[2,3],[4,1],[6,9],[3,1]]

print(lst[0:][0])
print(lst[2:][1])
print(max(lst[0:][0]))
print(max(lst[2:][1]))

lst.pop(0)
print(lst)

print(list(range(1,5)))
'''
'''
graph = [[] for _ in range(4)] #[]를 몇개 만들거냐
graph2 = [0 for _ in range(4)]
print(graph2)
print(graph)
'''

'''
#startswith함수 test
str = "1189"
str2="118"
print(str.startswith(str2))
print(str2.startswith(str))

#sort 함수 길이별로 정렬되는지 확인
#안됨
lst = ["11243","118","200","4444"]
lst.sort()
print(lst)
'''

'''
a={1:"hi",2:"ji",3:"ki"}

for i in a.items():
  print(i)
  
for i in a:
  print(i)
'''

'''
#hash() 사용시 같은 키값에 대해서는 같은 random한 값이 나오게 됨
print(type(hash('hi')))
print(hash('hi'))
print(hash("hello"))

from collections import Counter
lst = ["abc","d","ef"]
lst2= ["abc","df","e"]
#lst에서 lst2와 겹치는 수를 모두 빼냄
#dictionary는 안되지만 Counter 객체는 빼기가 가능
print(Counter(lst))
print(Counter(lst2))
print(Counter(lst)-Counter(lst2))
'''
'''
lst = ["hi","ji","ai"]

print(sum(lst))
'''
'''
from collections import Counter
lst = ["abc","d","ef"]
lst2= ["abc","df","e"]
#lst에서 lst2와 겹치는 수를 모두 빼냄
#dictionary는 안되지만 Counter 객체는 빼기가 가능
print(Counter(lst))
print(Counter(lst2))
print(Counter(lst)-Counter(lst2))
'''

'''
lst = [[1,9],[3,6],[2,2],[4,2],[8,1]]
lst2=lst[1:]
print(max(list(zip(*lst))[1]))
print(lst2)
print(max(lst))
print(max(lst[1:])) #0번째 원소를 기준으로 max를 뽑아냄
print(max(lst[1:])[0]) #9
print(max(lst2)[1]) #6
'''
lst = []
if lst:
  print("hi")
