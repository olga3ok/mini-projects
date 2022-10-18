import string

def ceasar_cipher(direction, language, step, text):
    eng_alphabet_lower = string.ascii_lowercase
    eng_alphabet_upper = string.ascii_uppercase
    ru_alphabet_lower = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
    ru_alphabet_upper = ''.join([chr(i) for i in range(ord('А'), ord('А') + 32)])

    for i in range(len(text)):

        lower_alpha, upper_alpha, count_of_lettes = (eng_alphabet_lower, eng_alphabet_upper, 26) if language else (ru_alphabet_lower, ru_alphabet_upper, 32)

        if text[i].isalpha():
            index = lower_alpha.find(text[i]) if text[i].islower() else upper_alpha.find(text[i])       
            new_index = (index + step) % count_of_lettes if direction else (index - step) % count_of_lettes
            print(lower_alpha[new_index] if text[i].islower() else upper_alpha[new_index], end='')
        else:
            print(text[i], end='')

direction = input('Что нужно сделать: шифровать или дешифровать? 1-шифровать/0-дешифровать:  \n')
while direction != '1' and direction != '0':
    direction = input('Для выбора направления введите цифру 1 или 0. 1-шифровать/0-дешифровать: \n')

language = input('Какой язык нужно использовать? 1-английский/0-русский:  \n')
while language != '1' and language != '0':
    language = input('Для выбора языка введите цифру 1 или 2. 1-английский/2-русский: \n')

step = input('На сколько символов нужно сдвинуть буквы по алфивиту? Введите число: \n')
while step.isdigit() != True:
    step = input('Введите число.  \n')

text = input('Введите текст для работы: \n')
while text.isspace() == True:
    text = input('Введите текст. \n')

direction, language, step = int(direction), int(language), int(step)

ceasar_cipher(direction, language, step, text)

