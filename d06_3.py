#count_vowels('apple') #=> 2
#count_vowels('banana') #=> 3

def count_vowels(word):
    a = 0
    for i in word:
        if i in ['a', 'e', 'i', 'o', 'u']:
            a += 1

    return a

print(count_vowels('apple'))
print(count_vowels('banana'))