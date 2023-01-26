blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

dic_abo = {'A':0,
'B':0,
'O':0,
'AB':0
}

for i in blood_types:
    dic_abo[i] += 1
print(dic_abo)
