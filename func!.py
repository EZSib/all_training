# def print_operation_table(op, row, col):
#     for i in range(1, 1+row):
#         for j in range(1, 1+col):
#             print(str(op(i, j)).ljust(3), end=' ')
#         print()
#
# print_operation_table(pow, 5, 4)

import string


# low = string.ascii_lowercase
# upp =string.ascii_uppercase
# def verification(login, password, success, failure):
#     if any(( i in low) for i in password) and any(( i in upp) for i in password):
#         if any(i.isdigit() for i in password) and any(i.isalpha() for i in password):
#             return success(login)
#     else:
#         a = (all(i.isdigit() for i in password if i in low or i in upp ), all(( i in low) for i in password if i.isalpha()), all(( i in upp) for i in password if i.isalpha()), all(i.isalpha() for i in password))
#         text = ('в пароле нет ни одной буквы', 'в пароле нет ни одной заглавной буквы', 'в пароле нет ни одной строчной буквы', 'в пароле нет ни одной цифры')[a.index(True)]
#         return failure(login, text)
#
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'мойпароль123', success, failure)

# def func(name, language='Python', year=1992):
#     pass
#
# print(func.__name__)          # имя функции
# print(func.__doc__)           # строка документирования
# print(func.__defaults__)      # кортеж с аргументами по умолчанию




#
# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     if step > 0:
#         for _ in range(step):
#             a = numbers.pop(-1)
#             numbers.insert(0,a)
#     else:
#         for _ in range(abs(step)):
#             a = numbers.pop(0)
#             numbers.append(a)