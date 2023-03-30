# ''' partial()'''
# from functools import partial
#
# def pretty_print(text, symbol, count):
#     print(symbol * count)
#     print(text)
#     print(symbol * count)
#
# star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')
#
# star_pretty_print(count=7)
#
# print(star_pretty_print.args)
# print(star_pretty_print.keywords)
#
# star_pretty_print.func('Исходная функция', symbol='~', count=20)

# '''update_wrapper()'''
# from functools import partial, update_wrapper
#
# def multiply(a, b):
#     '''Функция перемножает два числа и возвращает вычисленное значение.'''
#     return a * b
#
# double = partial(multiply, 2)
#
# update_wrapper(double, multiply)   # копируем информацию из функции multiply в partial объект double
#
# print(double.__name__)
# print(double.__doc__)
from functools import lru_cache as lru
from sys import stdin
@lru
def return_this(a):
    a = map(lambda x: ''.join(sorted(list(x.replace('\n', '')))), list(a))
    print(*a, sep='\n')
return_this(stdin)

