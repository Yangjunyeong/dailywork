word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

ord_word1 = 0
ord_word2 = 0

for i in word1:
    ord_word1 += ord(i)

for j in word2:
    ord_word2 += ord(j)

if ord_word1 > ord_word2:
    print(word1)
else:
    print(word2)
