# with open('data.txt') as file:
#     for line in iter(file.readline, ''):    # читаем, пока не попадется пустая строка
#         # Делаем что-то с line.
# class Counter:
#     def __init__(self, low, high):  # конструктор принимает два аргумента low и high (помимо self)
#         self.low = low
#         self.high = high
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.low > self.high:
#             raise StopIteration
#         else:
#             self.low += 1
#             return self.low - 1
# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return zip(iter(list(self.data)), iter(list([self.data[i] for i in self.data])))
#
# pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
#
# print(*pairs)
#
# from random import choice
#
#
# class RandomNumbers:
#     def __init__(self, l, r, n):
#         self.l, self.r, self.n = l, r, n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return choice(range(self.l, self.r + 1))
# print(next(iter(list(chr(i) for i in range(ord('a'), ord('z') + 1)))))

'''ПРИМЕРЫ ГЕНЕРАТОРОВ'''
#
# def counter(low, high):
#     for num in range(low, high + 1):
#         yield num
# counter1 = counter(3, 10)
#
# for i in counter1:
#     print(i)
#
# counter2 = counter(100, 103)
# print(next(counter2))
# print(next(counter2))
'''бесконечный генератор четных чисел'''
# def even_numbers(begin):
#     begin += begin % 2
#     while True:
#         yield begin
#         begin += 2

'''генератор порождающий посимвольный ввод текста с обрамлением символ'''
# def string_wrapper(text, symbol):
#     for char in text:
#         yield symbol + char + symbol
'''факториалы'''
# def factorials():
#     value = 1
#     index = 1
#     while True:
#         yield value
#         index += 1
#         value *= index
# infinite_factorials = factorials()
#
# for index, num in enumerate(infinite_factorials, 1):
#     if index <= 10:
#         print(f'Факториал числа {index} равен {num}')
'''ITERTOOLS!!!'''
# from itertools import accumulate
# import operator
#
# data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
#
# print(list(accumulate(data)))
# print(list(accumulate(data, operator.mul)))
# print(list(accumulate(data, max)))
# print(list(accumulate(data, min)))

# import itertools as it
# import time
#
# symbols = ['.', '-', "'", '"', "'", '-', '.', '_','|']
#
# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)
# l = [1, 2, 3]
# while l:
#     for i in l:
#         print(i)
'''groupby()'''
# from itertools import groupby
#
# numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]
#
# group_iter = groupby(numbers)
#
# print(type(group_iter))
# print(*group_iter, sep='\n')

# Пример 1. Удалить подряд идущие одинаковые элементы в списке.
#
# Решение. Будем использовать функцию groupby().
#
# Приведенный ниже код:
#
# from itertools import groupby
#
# data = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B']
#
# result = [key for key, group in groupby(data)]
#
# print(result)

# Пример 3. Определить, какой символ встречается чаще всего в строке.
#
# Решение. Будем использовать функцию groupby(), предварительно отсортировав данные.
#
# Приведенный ниже код:
#
# from itertools import groupby
#
# data = 'aaabcdaabcccdddcccccccbrttbcc'
# group_iter = groupby(sorted(data))
#
# max_result = max(group_iter, key=lambda tpl: sum(1 for i in tpl[1]))
#
# print('Символ встречающийся чаще всего в строке:', max_result[0])

# from collections import namedtuple
from itertools import groupby
#
# Person = namedtuple('Person', ['name', 'age', 'height'])
#
# persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
#            Person('Mark', 71, 172), Person('Alex', 45, 193),
#            Person('Jeff', 63, 193), Person('Ryan', 41, 184),
#            Person('Ariana', 28, 158), Person('Liam', 69, 193)]
# for key, name in groupby((sorted((map(lambda x: (x[2],x[0]), persons)),key=lambda x:x[0])),key=lambda x: x[0]):
#     print(key,': '+','.join(sorted(list(str(i[1:]).strip("()',")for i in name ))),sep='')

# Student = namedtuple('Student', ['surname', 'name', 'grade'])
#
# students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
#             Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
#             Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
#             Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
#             Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
#             Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
#             Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
#             Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
#             Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]
# print(max(groupby(sorted(map(lambda x: x[1], students))), key=lambda y: sum(1 for i in y[1]))[0])

# from itertools import groupby
#
# tasks = [('Отдых', 'поспать днем', 3),
#         ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
#         ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
#         ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
#         ('Отдых', 'погулять вечером', 4),
#         ('Курс по ооп', 'обсудить темы', 1),
#         ('Урок по groupby', 'добавить задачи на программирование', 3),
#         ('Урок по groupby', 'написать конспект', 1),
#         ('Отдых', 'погулять днем', 2),
#         ('Урок по groupby', 'добавить тестовые задачи', 2),
#         ('Уборка', 'убраться в ванной', 2),
#         ('Уборка', 'убраться в комнате', 1),
#         ('Уборка', 'убраться на кухне', 3),
#         ('Отдых', 'погулять утром', 1),
#         ('Курс по ооп', 'обсудить задачи', 2)]
# sorted_tasks = sorted(tasks, key=lambda x: x[0])
# gropped = groupby(sorted_tasks, key=lambda x: x[0])
# for bus,task in  gropped:
#         print(f'{bus}:')
#         for j in sorted(list(task),key= lambda x: x[2]):
#             print(f'    {j[2]}. {j[1]}')
#         print()
# from itertools import groupby
#
# def group_anagrams(words):
#     for key, word in groupby(sorted(words, key=lambda x: (len(x), sorted(x), x)), key=lambda x: sorted(x)):
#         yield  tuple(word)
#
#
# groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
#
# print(*groups)

# from itertools import groupby
#
# def ranges(nu):
#         a = [list(group) for i, group in groupby(nu, key= lambda x: nu.index(x)-x)]
#         return a
#
# numbers = [1, 2, 3, 4, 7, 8, 10]
#
# ranges(numbers)

# wallet = [100, 50, 20, 10, 5]
# from itertools import combinations_with_replacement
# counter = 0
# for i in range(1,21):
#     counter +=len(list(filter(lambda x: sum(x)== 100,set(combinations_with_replacement(wallet,i)))))
# print(counter)
'''ЗАДАЧА НА КОМБИНАТОРИКУ (СОБИРАЕМ РЮКЗАК С ОГРАНИЧЕННЫМ ВЕСОМ И МАКСИМАЛЬНОЙ ЦЕННОСТЬЮ)'''
# from collections import namedtuple
# import itertools as it
# 
# Item = namedtuple('Item', ['name', 'mass', 'price'])
#
# items = [Item('Обручальное кольцо', 7, 49_000),
#          Item('Мобильный телефон', 200, 110_000),
#          Item('Ноутбук', 2000, 150_000),
#          Item('Ручка Паркер', 20, 37_000),
#          Item('Статуэтка Оскар', 4000, 28_000),
#          Item('Наушники', 150, 11_000),
#          Item('Гитара', 1500, 32_000),
#          Item('Золотая монета', 8, 140_000),
#          Item('Фотоаппарат', 720, 79_000),
#          Item('Лимитированные кроссовки', 300, 80_000)]
# mass_li, asd, lol = [], [], []
# weith = int(input())
# try:
#     dict_mass_key = {b: (a, c) for a, b, c in items}
#     for i in range(1, 11):
#         for mass_comb in it.combinations((c[1] for c in items), r=i):
#             if sum(mass_comb) <= weith:
#                 mass_li.append((list(map(int, (mass_comb)))))
#     for i in mass_li:
#         asd.append(list(map(lambda x: dict_mass_key[x], i)))
#     for i in asd:
#         lol.append(list(map(lambda x: x[1], i)))
#     max_sum = list((map(sum, lol)))
#     finnaly = max_sum.index(max(list((map(sum, lol)))))
#     for i, j in sorted((asd[finnaly]), key=lambda x: x[0]):
#         print(i)
# except ValueError:
#     print('Рюкзак собрать не удастся')
