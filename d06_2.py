grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

def most_high_price(lst):
    a = 0
    
    for i in lst:
        if a < i[1]:
            a = i[1]
    
    for i in lst:
        if a == i[1]:
            return i[0]


print(most_high_price(grain_lst))