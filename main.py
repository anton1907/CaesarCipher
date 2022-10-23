print('Здраствуйте')
print('Напишите "Ш" Если шифрование или "Д" в противном случае дешифрование')
direction = input().lower()
print('Напишите "РУС" если русский язык или "АНГЛ" если английский язык')
alphabet_language = input()
print('Укажите на сколько произвести сдвиг русский 1-32 сдвига а английский 1-25')
shift_step = int(input())
print('Введите текст шифрование или дешифрование')
text = input().lower()
russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
alphabet = ''
if alphabet_language == 'рус':
    if direction == 'ш':
        for i in text:
            position = russian_alphabet.find(i)
            newposition = position + shift_step
            if i in russian_alphabet:
                alphabet = alphabet + russian_alphabet[newposition]
            else:
                alphabet = alphabet + i
        print(alphabet.capitalize())
    else:
        for i in text:
            position = russian_alphabet.find(i)
            newposition = position - shift_step
            if i in russian_alphabet:
                alphabet = alphabet + russian_alphabet[newposition]
            else:
                alphabet = alphabet + i
    print(alphabet.capitalize())
else:
    if direction == 'ш':
        for i in text:
            position = english_alphabet.find(i)
            newposition = position + shift_step
            if i in english_alphabet:
                alphabet = alphabet + english_alphabet[newposition]
            else:
                alphabet = alphabet + i
        print(alphabet.capitalize())
    else:
        for i in text:
            position = english_alphabet.find(i)
            newposition = position - shift_step
            if i in english_alphabet:
                alphabet = alphabet + english_alphabet[newposition]
            else:
                alphabet = alphabet + i
    print(alphabet.capitalize())
