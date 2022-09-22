#4:15~

def solution(relation):
    answer = 0

    #후보키의 조건
    #1) 유일성: 후보키로 인해서 각 튜플이 식별될 수 있어야함
    #=> 해당 속성의 튜플이 모두 다르다면 유일성
    #=> 해당 속성의 튜플 중 중복되는 튜플이 있고 이와 다른 속성을 매칭했을 시 중복되는 튜플이 식별된다면 유일성을 지니는 후보키
    #2) 최소성: 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성할 것
    #=> 유일성이 확보된다면 속성을 더 추가하지 말것

    



    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))