#덧셈 반복문을 활용할때는 처음에 변수에 0을 할당한다

result = 0
for n in range(1,1000):
    if n % 2 == 0 or n % 7 == 0: #배수는 나머지가 0일떄
        
        result += n

print(result)

# 2와 7의 배수 전부  합하기 (1000미만)





