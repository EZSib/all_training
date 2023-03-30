def get_max_index(numbers):
    max_index = -1
    max_value = 0

    for index, value in enumerate(numbers, 0):
        print(index,value)
        if value > max_value:
            max_index = index
            max_value = value

    return max_index
print(get_max_index([1,23,4,5,656,34,1,0,12]))

import sys
ml = [c.strip() for c in sys.stdin]
total, count = 0, 0
for c in ml:
    try:
        total += float(c)
    except ValueError:
        count+=1
print(max(int(total), total), count, sep='\n')
from collections import defaultdict as dd
try:
    with open(input(), encoding='utf8') as file:
        print(file.read())
except:
    print('Файл не найден')
import calendar, locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
def get_weekday(number):
    if type(number)!=int and number < float(number):
        raise TypeError('Аргумент не является целым числом')
    if number not in [1,2,3,4,5,6,7]:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return list(calendar.day_name)[int(number)-1]

def get_id(names, name):
    if type(name) !=str:
        raise TypeError('Имя не является строкой')
    else:
        if (name[0].isupper() and name.isalpha() and name[1:].islower())==False:
            raise ValueError('Имя не является корректным')
        else:
            return len(names)+1

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)
x ='123456789A'
print( any(i.lower() for i in filter(lambda x:not x.isdigit(),x)) )


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(x):
    try:
        if len(x) < 9:
            raise LengthError
    except LengthError:
        print(LengthError)
        x = input()
    try:
        if x.upper() == x or x.lower() == x:
            raise LetterError
    except LetterError:
        print(LetterError)
        x = input()
    try:
        if any(i.isdigit() for i in x) + any(i.isalpha() for i in x) < 2:
            raise DigitError
    except DigitError:
        print(DigitError)
        x = input()

    else:
        print('Success!')


numbers = [1, 2, 3, 4, 5]


def append_zero():
    numbers.append(0)
    append_zero()
    assert len(numbers) <= 5, 'Длина списка должна быть не больше пяти'