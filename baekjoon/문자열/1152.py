#단어의 개수
#1차시도) 문자열의 문자를 하나씩 검사하여 공백이 나오면 +1, 문자열의 끝이면 +1
#실패) 문자열의 맨 앞에 공백이 있을 경우 이전에 문자가 없는데도 문자가 하나 나왔다고 인식하기 때문
#2차시도) 공백이 아니면 스택에 넣고 공백이면 스택에서 다 꺼낸 후 카운트 증감
#성공)
#3차시도) 공백으로 나눠서 배열에 넣고 배열의 길이만 구해주면 끝

words = input()
words+='\n'
stack = []
cnt=0

for i in words:
  if i == ' ' or i == '\n':
    if len(stack) >0:
      cnt+=1
      while stack:
        stack.pop()
  else:
    stack.append(i)
    
print(cnt)