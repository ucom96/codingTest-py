#1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 출력하시오.
#단위를 증감시켜갈것
#문자열을 자를 것 => slicing
#압축할것 => 자른 문자열 앞뒤를 서로 비교하여 같다면 같은 문자열 개수 + 해당 문자열로 압축
#압축할때마다 = 단위가 변경될 때마다 문자열의 길이를 비교하여 가장 작은 길이를 리턴

#제출: 성공
#코드가 난잡하고 로직이 탄탄하지 않은듯함
s = input()
result = 1e9 #**result가 가장 큰 값이 될 수 있는 것은 len(s)만큼일테니 1e9로 놓을 필요는 없음! 이렇게 되면 len=1일때도 굳이 line 15-16같은 코드를 넣을 필요가 없음
cnt = 1 #**단위가 갱신될때마다 리셋되어야 하므로 여기가 아닌 Line 18쯤에 넣어줄것

#단위가 계속 바뀔것 => 1.... => for문 반복
for unit in range(1, len(s)//2+1):
  if len(s) == 1: #**필요없는 코드
    result = 1
  compression = "" #**compression을 다 만든뒤에 최종적으로 len를 구해줘도 되지만 매번 이전문자열과 현재문자열이 달라질 때마다 이전문자열의 길이와 카운트의 len를 그때그때 갱신해줘도 좋음!
  #문자열을 단위만큼 잘라서 서로간에 비교
  #비교하는 로직은 똑같이 유지하되 인덱스만 바뀌게 되므로 for문 이용
  for idx in range(0, len(s), unit):
    unit_str = s[idx: idx+unit]
    #Q:중첩된 for문의 끝부분을 어떻게 결정해야될지?
    #앞뒤 비교
    if s[idx:idx+unit] == s[idx+unit: idx+unit+unit]: #**이렇게 비교해도 상관은 없으나 가독성이 더 좋으려면 이전의 값을 저장하는 변수를 따로 생성하여 변수들끼리 비교할것!
      #똑같은 단위의 개수를 셀것
      cnt+=1
    else:
      #압축
      if cnt ==1:
        compression += unit_str
      else:
        compression += str(cnt)+unit_str #**+unit_str처럼 공통된 코드는 위에 따로 빼주고 특수한 케이스에 대해서만 if문의 내용으로 설정할것
      cnt=1

  result = min(result, len(compression))

print(result)