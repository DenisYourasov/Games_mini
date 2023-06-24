# Игра виселица

from random import *

word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар']

def get_word():
    return choice(word_list).upper()

def print_word(word, guessed_letters):
    for i in word:
        if i in guessed_letters:
            print(i, end = ' ')
        else:
            print('_', end = ' ')
    print()

def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''']
    return stages[tries]

def play(word):
    # print(word)
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play!")
    print(word_completion)
    print(display_hangman(tries))
    while True:
        guess_wold = input('Enter you letter or word: ').upper()
        
        # проверка ввода буквы или слова на корректность ввода
        if guess_wold == '':
            print('Please enter a letter or a word.')
            continue
        if len(guess_wold) == 1 and guess_wold not in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
            print('Please enter a letter.')
            continue
        if not guess_wold.isalpha():
            print('Please enter a letter or a word.')
            continue
        if guess_wold in guessed_letters or guess_wold in guessed_words:
            print('You have entered it before.')
            continue
        
        # процесс угадывания слова и сохранение слов в список
        if len(guess_wold) > 1:
            if guess_wold == word:
                print('Congrat! You win!!!')
                break
            else:
                guessed_words.append(guess_wold)
                tries -= 1
                print(f'You wrong. Remaining attempts {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print(f'You lost! Hidden word: {word}')
                    break
                continue
        
        # процесс угадывания букв и сохранения их в список
        if guess_wold in word:
            guessed_letters.append(guess_wold)
            for i in word:
                if i not in guessed_letters:
                    print('You guessed letter!')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print_word(word, guessed_letters)
                print('Congratilation!!! You win! You guessed word!')
                break
        else:
            guessed_letters.append(guess_wold)
            tries -= 1
            print(f'You wrong. Remaining attempts {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)            
        if tries == 0:
            print(f'You lost! Hidden word: {word}')
            break

while True:
    game = input('Want you play "HANGMAN"? - "y" yes or "n" no: ')
    if game == 'y':
        play(get_word())
    else:
        break


