#다이얼

alp = input()
dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

answer=0
#알파벳을 하나씩 확인하여 다이얼에서 몇번째 인덱스에 있는지 알아내기
for i in alp:
  for j in dial:
    if i in j:
      answer+=dial.index(j)+3

print(answer)

