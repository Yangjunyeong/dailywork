str_a = 'apple,rottenBanana,apple,Rottenorange,Orange'

my_list = list(map(str,str_a.lower().split(",")))
lst = []
for i in my_list:
    if 'rotten' in i:
        lst.append(i[6:])
    else:
        lst.append(i)
    
print(lst)
