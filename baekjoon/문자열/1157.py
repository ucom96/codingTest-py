#단어공부

#단어에서 사용된 알파벳 개수 배열
alp = [0]*26

word = input().upper()

for i in word:
  alp[ord(i)-65]+=1

if alp.count(max(alp))==1:
  print(chr(alp.index(max(alp))+65))
else:
  print("?")

