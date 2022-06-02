#크로아티아 알파벳
#1차시도) 인풋으로 들어온 str의 길이를 세고 dz=를 제외한 나머지는 발견되면 -1을 해주고 dz=는 세글자이므로 -2를 해준다
#실패) "dz="일때 "z="로 인식되므로
#2차시도) 미리 "dz="를 하나의 문자로 만들어서 "z="와 겹치는 일이 없도록 할것 즉 모든 크로아티아 알파벳을 찾으면 하나의 문자로 바꿔줄것

word = input()

croa_alps = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for croa_alp in croa_alps:
  word=word.replace(croa_alp,"*")

print(len(word))