#1차시도) 효율성 테스트에서 실패
#다른 사람 풀이 보고 품

def solution(phone_book):
  phone_book.sort()
  
  for p1,p2 in zip(phone_book, phone_book[1:]):
    if p2.startswith(p1):
      return False
  return True

phone_book = ["123","456","789"]

print(solution(phone_book))