#그룹 단어 체커
#1차시도) 알파벳 배열을 만들고 word의 알파벳을 하나씩 확인해간다 알파벳의 인덱스를 배열에 넣고 만약 현재 알파벳의 인덱스가 저장된 안덱스와 1이상 차이가 나면 그룹단어가 아닌것으로 판별
#성공

n=int(input())

def isGroupWord(word):
  alp=[-1]*26
  for i in range(len(word)):
    past = alp[ord(word[i])-97]
    now = i
    if past!=-1 and now-past>1:
      return False
    if past ==-1 or now-past==1:
      alp[ord(word[i])-97]=now
  return True

cnt =0
for _ in range(n):
  word=input()
  if isGroupWord(word):
    cnt+=1

print(cnt)

  