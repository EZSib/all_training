# создание ф-ции с рекурсией и использованием механизма замыкания :
# def draw_rect(width, height):
#     def rec(step):
#         if step < height:
#             print('*' * width)
#             rec(step + 1)
#     rec(0)\
# def bee(n):
#     if n < 5:
#         print(n)
#     else:
#         bee(n + 1)
#
# bee(0)
# def score(n):
#     if n<101:
#         print(n)
#         score(n+1)
#     else: return
# score(1)
# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
# def numb(n):
#     if n< len(numbers):
#         print(numbers[n])
#         numb(n+1)
#     else: return
# numb(0)
# import sys
# def seq(n):
#     def ind(m):
#         if abs(m) != len(n):
#             print(n[m])
#             ind(m-1)
#     ind(-1)
# seq([int(i) for i in sys.stdin])
# def sand_clock(n):
#     def forward(grade,index):
#         if grade > 1:
#             print(f'{str(n[index]) * grade : ^16}')
#             forward(grade-4,index+1)
#     forward(16,0)
#     def back(grade, index):
#         if grade < 17:
#             print(f'{str(n[index]) * grade: ^16}')
#             back(grade + 4, index - 1)
#     back(8,-2)
# sand_clock([1,2,3,4])
g = '123456'


# def sums(nums):
#     if not nums:
#         return 0  # базовый случай
#     return nums[0] + sums(nums[1:])
#
#
# print(sums(list(map(int, g))))
# (5).isint
# import sys
#
# print(sys.getrecursionlimit())
# def get_all_values(nested_dicts, key):
#     s = set()
#     if key in nested_dicts:
#         if isinstance(nested_dicts[key], list):
#             s.update(set(nested_dicts[key]))
#         else:
#             s.add(nested_dicts[key])
#     for elem in nested_dicts.values():
#         if isinstance(elem, dict):
#             s.update(get_all_values(elem, key))
#     return s

# names = ['-*- coding: utf-8 -*-','ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
# print(*sorted(map(lambda x: x.capitalize(), (filter(lambda x: x[0].lower() in ('а','м') and len(x) > 4, names)))))
# fib = lambda x: 1 if x ==1 or x ==2 else (fib(x - 1)+fib(x - 2)) fib from lambda and rec
