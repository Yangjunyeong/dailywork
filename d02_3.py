str_lst = input('문자열을 입력하세요. : ')
# 입력받은 세 단어를 전부 소문자로 변환 후 list에 담기
p_or_f = list(map(str,str_lst.lower().split()))

# 앞 단어의 끝문자와 뒷 단어의 첫 단어가 같으면 Pass
if p_or_f[0][-1] == p_or_f[1][0] and p_or_f[1][-1] == p_or_f[2][0]:
    print('Pass')
# 다르다면 Fail
else:
    print('Fail')

# 세 단어가 주어지고 끝말잇기를 할떄 옳으면 Pass 아니면 Fail
# saFe eMotion Nail 일 경우는 pass
