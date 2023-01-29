m = 5
n = 4

for column in range(m):
    for row in range(n):
        print('*',end = '')
        #end의 기본값은 \n임. 그래서 print를 하면 다음 값은 
        #기본적으로 줄바꿈을 해서 출력이 됨.
        #근데''로 설정하면 끝나고 나서 다음값이 바로 옆에 출력이 나옴

    print('') # 줄바굼을 해야 다음 행으로 넘어감
    

#가로의 길이가 n 세로의 길이가 m인 직사각형을 *로 출력하기

