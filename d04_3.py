# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

d_lst = [1, 1, 3, 3, 0, 1, 1]
result = [d_lst[0]]
for i in range(1, len(d_lst)):
    if d_lst[i] != d_lst[i-1]:
        result.append(d_lst[i])



'''for i in enumerate(d_lst)[:-1]:
    if d_lst[key] == d_lst[key + 1]:
         result.append(value)
    
    else:
        result.append(value)'''

print(result)