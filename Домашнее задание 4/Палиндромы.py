palindroms = []

while True:
    word = input('Введите слово: ')
    reverse_word = word[::-1]
    print(reverse_word)
    if word == reverse_word:
        print('Ваше слово палиндром.')
        palindroms.append(word)
        print(palindroms)
    elif word != reverse_word:
        print('Ваше слово не палиндром.')
        print(palindroms)