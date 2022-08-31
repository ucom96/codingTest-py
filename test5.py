def solution(phone_book):
    answer = True

    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return answer

phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))

print("11901".startswith("119"))
print("911901".startswith("119"))