#프린터큐

#큐의 가장 앞에 있는 문서의 중요도를 확인한다
#나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면 가장 뒤로 보낸다 그렇지 않으면 바로 인쇄한다

#1차시도) <실패> lst의 1번째 요소들 중 max를 구하지 못함..
#해결) max(lst)[0]: lst의 0번째 요소들 중 max

import sys

result=[]
t=int(sys.stdin.readline())

def print_doc_order(target_idx, doc_infos):
  cnt =0
  while doc_infos:
    #큐의 가장 앞에 있는 문서의 중요도를 확인한다
    first_doc_imp = doc_infos[0][1]
    #큐의 가장 앞에 있는 문서의 인덱스를 확인한다
    first_doc_idx = doc_infos[0][0]
    #가장 앞에 있는 문서 제외한 나머지 문서들 중 가장 높은 중요도를 확인한다
    max_doc_imp = max(list(zip(*doc_infos))[1])
    #나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면 해당 문서를 가장 뒤로 옮긴다
    if first_doc_imp < max_doc_imp:
      doc_infos.append(doc_infos.pop(0))
    #그렇지 않다면 바로 인쇄한다
    else:
      cnt+=1
      doc_infos.pop(0)
      if target_idx == first_doc_idx:
        return cnt

for _ in range(t):
  doc_num, target_idx = map(int, sys.stdin.readline().split())
  #doc_infos에 문서의 중요도와 인덱스를 함께 저장한다
  doc_infos =[[doc_idx, doc_imp] for doc_idx, doc_imp in enumerate(map(int, sys.stdin.readline().split()))]
  result.append(print_doc_order(target_idx, doc_infos))
  
print('\n'.join(map(str,result)))