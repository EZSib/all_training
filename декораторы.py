# def sample_decorator(func):          # определяем декоратор
#     def wrapper():
#         print('Начало функции')
#         func()
#         print('Конец функции')
#     return wrapper
#
# def say():
#     print('Привет Мир!')
#
# say = sample_decorator(say)          # декорируем функцию
#
# say()
# def uppercase_decorator(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
# @uppercase_decorator
# def greet():
#     return 'Hello world!'
#
# def bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper
#
# def italic(func):
#     def wrapper():
#         return '<i>' + func() + '</i>'
#     return wrapper
# @bold
# @italic
# def greet():
#     return 'Hello world!'
#
# print(greet())
#
# def bold(func):
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper
# @bold
# def greet1(name):
#     return f'Hello {name}!'
#
# @bold
# def greet2():
#     return 'Hello world!'
#
# @bold
# def greet3(name, surname):
#     return f'Hello {name} {surname}!'
#
# print(greet1('Timur'))
# print(greet2())
# print(greet3('Timur', 'Guev'))
# def double(func):
#     def wrapper():
#         return func() * 2
#     return wrapper
#
# @double
# def beegeek():
#     return 'beegeek'
#
# print(beegeek())
# def add_dollar_prefix(func):
#     def wrapper():
#         result = str(func())
#         return '$' + result
#     return wrapper
#
# @add_dollar_prefix
# def get_price(item):
#     prices = {'comic book': 5, 'puzzle': 15}
#     return prices[item]
#
# print(get_price('comic book'))
# def double(func):
# #     def wrapper(*args, **kwargs):
# #         doubled_result = func(*args, **kwargs) * 2
# #     return wrapper
# #
# # @double
# # def get_color_code(color):
# #     color_codes = {'black': '#000000', 'white': '#FFFFFF'}
# #     return color_codes[color]
# #
# # print(get_color_code('white'))

# def dec(func):
#     def wrapper(*args, **kwargs):
#         print('Аргументы: ', args, 'Тип: ', type(args))
#         print('Именованные аргументы: ', kwargs, 'Тип: ', type(kwargs))
#         func(*args, **kwargs)
#     return wrapper
# new_print = dec(print)
# new_print('bee', 'geek', sep='***', end='_LINEEND')

# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args,**kwargs), 'Функция выполнилась без ошибок'
#         except:
#             return (None, 'При вызове функции произошла ошибка')
#     return wrapper
#
#
# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))


# TypeError, если аргумент не является целым числом
# ValueError, если аргумент является целым числом, но отрицательным или равным нулю
# def takes_positive(func):
#     def wrapp(*args,**kwargs):
#         if not all(map(lambda x:isinstance(x, int), args)) and all([isinstance(i, int) for i in kwargs.values()]):
#             raise TypeError
#         else :
#             if not all(map(lambda x:x>0, args)) and all([i > 0 for i in kwargs.values()]):
#                 raise ValueError
#         try:
#             return func(*args, **kwargs)
#         except TypeError:
#             pass
#         except ValueError:
#             pass
#     return wrapp
#
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)

# import functools
#
# def bold(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return '<b>' + func(*args, **kwargs) + '</b>'
#     return wrapper
#
# @bold
# def greet(name):
#     '''Функция приветствие пользователя.'''
#     return f'Hello {name}!'
#
# print(greet.__name__)
# print(greet.__doc__)

# import functools
#
# def make_capitalize(func):
#     @functools.wraps(func)
#     def wrapper():
#         return func().capitalize()
#     return wrapper
#
# @make_capitalize
# def beegeek():
#     '''documentation'''
#     return 'beegeek'
#
# print(beegeek.__name__)
# print(beegeek.__doc__)
# import functools
# def sqare(func):
#     @functools.wraps(func)
#     def wrapper(*a, **kw):
#         value = a**2
#         return value
#     return wrapper
#
# def print_symbols(symbol, length):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(symbol * length)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
# Приведенный ниже код:
#
# @print_symbols('*', 30)
# def add(a, b):
#     return a + b

# def delayed(delay=2):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(f'Спим {delay} сек.')
#             time.sleep(delay)
#             value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
#
#
# @delayed(1)
# def countdown(number):
#     if number < 1:
#         print('Конец!')
#     else:
#         print(number)
#         countdown(number - 1)
#
#
# countdown(5)
#
# import functools, time
#
# def timer(iters=1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             total = 0
#             for i in range(iters):
#                 start = time.perf_counter()
#                 value = func(*args, **kwargs)
#                 end = time.perf_counter()
#                 total += end - start
#             print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
#             return value
#         return wrapper
#     return decorator
# @timer(iters=1000)
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
# res1 = test(10000)
# print(f'Результат функции test = {res1}')
# import functools
#
# def repeater(repeat=1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, repeat + 1):
#                 print(f'{i}-ый запуск функции.')
#                 value = func(*args, **kwargs)
#             return value
#         return wrapper
#     return decorator
# Приведенный ниже код:
#
# @repeater(repeat=5)
# def beegeek():
#     print('beegeek')
#
# beegeek()

# import functools
#
#
# def takes(*types):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = func(*args,**kwargs)
#             if all(map(lambda x: isinstance(x,types), args))+all(map(lambda x: isinstance(x,types), kwargs.values()))+all(map(lambda x: isinstance(x,types), kwargs.keys()))==3 :
#                 return value
#             else:
#                 raise TypeError
#         return wrapper
#     return decorator
#
# @takes(int, str)
# def repeat_string(string, times):
#     return string * times
#
# print(repeat_string('bee', 3))

