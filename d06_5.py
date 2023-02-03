

def sum_of_digit(n):
    sum_digit = 0
    for i in str(n):
        sum_digit += int(i)

    print (sum_digit)

def sum_of_digit_2(n):
    lst_n = list(map(int,str(n)))
    
    print(sum(lst_n))
sum_of_digit(3904) # 16
sum_of_digit_2(3904)