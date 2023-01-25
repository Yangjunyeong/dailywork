# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(num):
    a = ''
    if len(num) == 14:
        for i in range(14):
            if i in range(0,6):
        
                a = a + num[i]
            elif i in range(6,13):
                a = a + '*'

    if len(num) == 13:
        for i in range(13):
            if i in range(0,6):
                a = a + num[i]
            else:
                a = a + '*'

    return a

