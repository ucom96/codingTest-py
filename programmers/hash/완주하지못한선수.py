#participant에서 completion에 없는 사람을 골라내기
#1) participant의 이름수를 값으로 저장하여 hash_participant를 만든다
#2) completion과 hash_participant를 대조하여 이름이 있다면 값을 감소시킨다
#3) hash_participant에서 값이 0이 아닌 사람은 완주하지 못했다는 것이므로 출력한다
#1차시도 성공
from collections import defaultdict

def solution(participant, completion):
  answer=''
  hash_participant=defaultdict(int)
  for i in participant:
    hash_participant[i]+=1
  #print(hash_participant)
  for i in completion:
    if i in hash_participant:
      hash_participant[i]-=1
  
  for i in hash_participant:
    if hash_participant[i]!=0:
      answer=i
  
  return answer
  
  

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))