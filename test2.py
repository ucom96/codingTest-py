#문자열 인덱싱으로 문자열 변경하기

str = "hello"



print(str[4:7])
print(str[6:7])

#str[0]="j"

#print(str)

#str은 immutable한 객체이므로 인덱싱을 통해 변경불가

#str.replace() 사용시 인덱싱을 통해 바꿀수 있는지 확인

#str.replace(str[0:2],'ji')

#print(str)

#안됨

prev = str[0:3] #'hel'
for j in range(3,5,3):
    print('str',str[j:j+3])
    if prev == str[j : j+3]: 
        print("yes")
    print(j, j+3)

  
