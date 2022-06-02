#그룹 단어 체커
#2차시도) 구글링 => 현재 요소와 다음 요소 비교하여 다를시 현재요소 다음~끝까지 새 문자열 만들어서 그 안에 현재요소가 하나라도 있다면 그룹단어 안됨

def isGroupWord(word):
  for i in range(len(word)-1):
    if word[i]!=word[i+1]:
      new_word = word[i+1:]
      if new_word.count(word[i])>=1:
        return False
  return True

n=int(input())
words = [input() for _ in range(n)]
cnt =0
for word in words:
  if isGroupWord(word):
    cnt+=1
print(cnt)
