str_lst = input('문자열을 입력하세요. : ')

p_or_f = list(map(str,str_lst.split()))


if p_or_f[0][-1] == p_or_f[1][0] and p_or_f[1][-1] == p_or_f[2][0]:
    print('Pass')

else:
    print('Fail')