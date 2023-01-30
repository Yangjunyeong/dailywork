# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(num):
    not_repeat = {}
    lst=[]
    for i in num:
        if i in not_repeat:
            not_repeat[i] += 1
        else:
            not_repeat[i] = 1
    
    for i in not_repeat:
        if not_repeat[i] == 1:
            lst.append(i)

    return sum(lst)
    
        

num_list = [4, 4, 7, 8, 10, 4]

print(sum_of_repeat_number(num_list))

