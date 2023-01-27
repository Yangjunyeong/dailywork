test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}
a=[]

for i in test_status:
	if test_status[i] == 'cheating':
		a.append(i)
b={}
for i in test_status:
	if test_status[i] != 'cheating':
		b[i] = 'solving'
		


a.sort()
print(a)
print(f'test_status = {b}')
	