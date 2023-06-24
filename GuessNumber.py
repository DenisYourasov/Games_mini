# Игра на угадывание загаданного числа из заданного диапазона.
# При ответах программа дает подсказку введенное число больше или меньше загаданного.

from random import *

def max_range():
    while True:
        n = input('Please enter a range of numbers from 1 to ...: ')
        if not n.isdigit():
            print('Please enter an integer number: ')
            continue
        elif not int(n) > 0:
            print('Please enter an integer greater than zero: ')
            continue
        else:
            return int(n)

def enter_number():
    while True:
        num = input(f'Please enter an integer number in range from 1 to {N}: ')
        if not num.isdigit():
            print('Please enter an integer number: ')
            continue
        elif not 0 < int(num) <= N:
            print(f'Please enter an integer number in range from 1 to {N}: ')
            continue
        else:
            return int(num)

def compare():
    num_generate = randint(1, N)
    counter_attempt = 0
    x = 0
    while x != num_generate:
        x = enter_number()
        counter_attempt += 1
        if x < num_generate:
            print('Your number is less than expected, choose another number.')
            continue
        elif x > num_generate:
            print('Your number is higher than the one you predicted, please choose another number.')
            continue
        print('You guessed correctly in', counter_attempt, 'attempts. Congratulations!')

print('Welcom to the game!')

N = max_range()

compare()

while True:
    
    answer = input('Do you want to play again? - Y or N :')
    if answer in ('y', 'Y', 'yes', 'Yes', 'YES'):
        N = max_range()
        compare()
        continue
    else:
        print('Thank you for game! See you.')
        break 