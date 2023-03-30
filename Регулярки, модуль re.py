"""Поиск почты в тексте"""
email = r'[\w.]+@[\w.]+\.\w+'
'''Поиска url'''
url = r'https?://[\w./]+'
RGB = r'[0-9A-Fa-f]{6}'
date_format = r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}'
more_100_dol = r'\d+: \$\d{3,}\.\d{2}'
ords_hunter = r'\b\w+\b'
ip_bad_too = r'(\d{1,3}\.){3}\d{1,3}'
ip_0nly_good = r'((2[0-4]\d)|(25[0-5])|(1\d{2})|(\d{1,2}))'
or_ip = r'\b(((25[0-5])|(2[0-4]\d)|(1\d\d)|\d{1,2})\.){3}((25[0-5])|(2[0-4]\d)|(1\d\d)|\d{1,2})\b'
'''Поиск повторяющихся слов сслыками назад '''
back_to_words = r'(\b\w+\b)[ ]+\1'
'''Поиск HTML тегов в тесте, с помощью ссылок назад'''
html_tag = r'<[Hh]([1-6])>.*</[Hh]\1>'
'''Пример использования именнованого паттерна '''
# from re import search
#
# match = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')
#
# print(match.group())
# print(match.group('w1'))
# print(match.group('w2'))
# print(match.group('w3'))
# print(match.group('w1', 'w2', 'w3', 'w2', 'w3'))
# from re import search
#
# match = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')
#
# print(match.groupdict())

# from re import search
#
# text = 'foo123bar456baz'
#
# match = search('(\d+)\D+(?P<num>\d+)', text)
#
# print(match)
# print(match.group(), match.start(), match.end())
# print(match.group(1), match.start(1), match.end(1))
# print(match.group('num'), match.start('num'), match.end('num'))

# from re import fullmatch
#
# match1 = fullmatch(r'(-)?(\d+)', '2077')
# match2 = fullmatch(r'(-)?(\d+)', '-1337')
#
# print(match1.group(1))
# print(match1.group(2))
# print(match2.group(1, 2))

'''Примеры использования флагов'''
# import re
#
# match1 = re.search('[a-z]+', 'aBcDeF')
# match2 = re.search('[a-z]+', 'aBcDeF', re.I)
#
# print(match1)
# print(match2)

# import re
#
# text = 'foo\nbar\nbaz'
#
# print(re.search('^foo', text, re.MULTILINE))
# print(re.search('^bar', text, re.MULTILINE))
# print(re.search('^baz', text, re.MULTILINE))
# print(re.search('foo$', text, re.M))
# print(re.search('bar$', text, re.M))
# print(re.search('baz$', text, re.M))

# import re
#
# print(re.search('foo.bar', 'foo\nbar'))
# print(re.search('foo.bar', 'foo\nbar', re.DOTALL))
# print(re.search('foo.bar', 'foo\nbar', re.S))

# import re
#
# match = re.search('''\d +  # целая часть
#                      \.    # десятичная точка
#                      \d *  # дробная часть''', 'Десятичное число равно 123.7', re.VERBOSE)
#
# print(match)
# import re
#
# print(re.search('x[123]{2,4}y', 'x222y', re.DEBUG))

'''sub() если используется стр. в repl'''
# import re
#
# text = 'foo.123.bar.456.baz.789.geek'
#
# result1 = re.sub(r'\d+', r'#', text)
# result2 = re.sub(r'[a-z]+', r'(*)', text)
#
# print(result1)
# print(result2)
'''sub() использование пронумерованных обратных ссылок, именованных обратных ссылок'''
# import re
#
# result = re.sub(r'(\w+),bar,baz,(\w+)', r'\2,bar,baz,\1', r'foo,bar,baz,qux')
#
# print(result)
# import re
#
# result = re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', r'foo,\g<w2>,\g<w1>,qux', r'foo,bar,baz,qux')
#
# print(result)
# import re
#
# result = re.sub(r'foo,(\w+),(\w+),qux', r'foo,\g<2>,\g<1>,qux', 'foo,bar,baz,qux')
#
# print(result)
# import re
#
# result = re.sub(r'(\d+)', r'\g<1>0', 'foo 123 bar')
#
# print(result)
'''sub() замена с использованием функции в repl'''
# import re
# def func(match_obj):
#     s = match_obj.group(0)         # строка совпадения
#     if s.isdigit():
#         return str(int(s) * 10)
#     else:
#         return s.upper()
#
# result = re.sub(r'\w+', func, r'foo.10.bar.20.baz30.40')
#
# print(result)
'''split() разбиение строки, где разделитель регулярка '''
# import re
#
# result = re.split(r'[,;.]', 'foo,bar.baz;qux;stepik,beegeek')
#
# print(result)
#
# import re
#
# string = 'foo,bar.baz;  qux;stepik,    beegeek'
# regex = r'(\s*[,;.]\s*)'
#
# result = re.split(regex, string)
#
# for index, value in enumerate(result):
#     if not re.fullmatch(regex, value):
#         result[index] = f'[{value}]'
#
# new_string = ''.join(result)
#
# print(string)
# print(new_string)

"""Если нам нужно использовать группы, но мы не хотим, чтобы разделители включались
 в результирующий список, то можно использовать группы без захвата, используя синтаксис (?:<regex>).
Приведенный ниже код:"""
# import re
# result = re.split(r'(?:\s*[,;.]\s*)', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')
# print(result)

