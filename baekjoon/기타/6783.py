#English or French?
#구현 문제

#t 혹은 T가 s 혹은 S보다 많다면 영어 텍스트로 분리
#s 혹은 S가 t 혹은 T보다 같거나 많다면 프랑스어 텍스트로 분리

n = int(input())

s_num, t_num = 0,0

result = ""

for _ in range(n):
    sentence = input()

    s_num += sentence.count("s") + sentence.count("S")
    t_num += sentence.count("t") + sentence.count("T")

if s_num < t_num:
    print("English")
else:
    print("French")