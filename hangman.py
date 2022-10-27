import random

def get_word(word_list):
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    # ru_alphabet_upper = ''.join([chr(i) for i in range(ord('А'), ord('А') + 32)])

    while True:
        input_w = input('Введите слово целиком или букву: ').upper()
        input_word, input_letter = '', ''
        while True:               # проверка введенных данных
            if input_w.isalpha() and input_w not in guessed_words and input_w not in guessed_letters:
                if len(input_w) == 1:
                    input_letter = input_w
                    guessed_letters.append(input_letter)
                else:
                    input_word = input_w
                    guessed_words.append(input_word)
                break
            else:
                if input_w in guessed_words or input_w in guessed_letters:
                    print('Уже было.')
                else:
                    print('Вы ошиблись.')
                input_w = input('Введите слово целиком или букву: ').upper()
        if input_word:
            print(f'Введенное слово: {input_word}')
        else:
            print(f'Введенная буква: {input_letter}')
        
        if input_letter:
            if input_letter in word:
                indexs = []
                for i in range(len(word)):
                    if word[i] == input_letter:
                        indexs.append(i)
                result = '' 
                for i in range(len(word)):
                    if i in indexs:
                        result += input_letter.upper()
                    else:
                        result += word_completion[i]
                word_completion = result
                tries -= 1
                print(word_completion)
                if word_completion == word:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    guessed = True
                else:
                    print(f'Такая буква есть в слове. Осталось попыток: {tries}')
                    print(display_hangman(tries))
            else:
                tries -= 1
                print(f'Вы не угадали. Осталось попыток: {tries}')
                print(display_hangman(tries))
                
        if input_word:
            if input_word == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                guessed = True
            else:
                tries -= 1
                print(f'Вы не угадали. Осталось попыток: {tries}')
                print(display_hangman(tries))

        if tries == 0 and guessed == False:
            print(f'Вы проиграли. Было загадано слово {word}')
            guessed = True

        if guessed == True:
            break
        else:
            continue


word_list = ['комод', 'шарф', 'ленточка', 'планшет', 'окуляр', 'горб', 'видеокассета', 'айсберг', 'столб', 'гравий']

again = 'Да'

while again == 'Да':
    word = get_word(word_list)
    play(word)
    again = input('Хотите сыграть ещё раз? Да/Нет ')
    print()
