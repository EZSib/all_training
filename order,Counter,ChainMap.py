# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])     # объявляем тип Point именованного кортежа
#
# point = Point(3, 7)                         # создаем именованный кортеж Point
#
# print(point)
# print(point.x, point.y)
# print(point[0], point[1])
# print(type(point))
# Person = namedtuple('Person', ['name', 'children'])
#
# sveta = Person('Sveta Gueva', ['Larisa', 'Timur'])
# print(sveta)
#
# sveta.children.append('Soslan')
# print(sveta)
import json
# from collections import Counter
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
# for k,v in sorted(Counter([i.split('.')[1] for i in files]).items()):
#     print(f'{k}: {v}')
#
# def count_occurences(word, words):
#     return list(map(lambda x:x.lower(),words.split())).count(word.lower())
#
#
# for k,v in sorted(Counter(l:=[i for i in input().split(',')]).items()):
#      print(f'{k.ljust(max(map(len,l)))}: {sum(map(lambda x: ord(x), k.replace(" ", "")))}'
#            f' UC x {v} = {sum(map(lambda x: ord(x), k.replace(" ", "")))*v} UC')
#
# for k,v in sorted(Counter(l:=[i for i in input().split(',')]).items()):
#      o = sum(map(lambda x: ord(x), k.replace(" ", "")))        # sum ord
#      wspace = max(map(len,l))                                  # ljust
#      print(f'{k.ljust(wspace)}: {o} UC x {v} = {o*v} UC')
# with open('pythonzen.txt','rw', encoding='utf8') as file:
#      for k,v in (sorted(Counter([i.lower() for i in file.read() if i.isalpha()]).items())):
#           print(f'{k}: {v}')

# a = Counter(map(len, input().split()))
# for k, v in sorted(a.items(), key=lambda x: (x[1])):
#     print(f'Слов длины {k}: {v}')
from collections import Counter
# import sys
#
# a = Counter({i.split()[0]: int(i.split()[1]) for i in sys.stdin})
# print(a.most_common()[-2:-1][0][0])


# data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
#
# data.__dict__['min_values'] = lambda:  [(k, v) for k,v  in data.items() if v==min(data.values())]
# data.max_values = lambda: [(k, v) for k,v  in data.items() if v==max(data.values())]
# data.clear()
#
# data['a'] = 1
#
# print(data.max_values())
# print(data.min_values())
# # data['t'] += 1
#
# clue = [('b', 2), ('c', 2), ('n', 2), ('t', 2)]
# reply = data.min_values()
#
# print(type(reply))
# print(set(reply) == set(clue))

# with open('name_log (1).csv', encoding='utf8') as file:
#     a =sorted(Counter([i[1] for i in [i.split(',')for i in file.readlines()[1:]]]).items())
#     for i in a:
#         print(f'{i[0]}: {i[1]}')

# def print_bar_chart(all, char):
#     if type(all)==list:
#         for k,v in sorted((Counter(l:=[i for i in all]).items()), key=lambda x:-x[1]):
#
#             print(f'{k.ljust(max(map(len,l)))} |{v*char}')
#     else:
#         for k,v in sorted((Counter(all).items()), key=lambda x:-x[1]):
#             print(f'{k.ljust(max(map(len,all)))} |{v * char}')
# from collections import Counter
# import csv
# import json
# counter = Counter()
# with open ('prices.json', encoding='utf8') as prices:
#     price = json.load(prices)
#     for i in range(1, 5):
#         with open(f'quarter{str(i)}.csv', encoding='utf8') as file:
#             counter.update({i[0]: int(i[1])+int(i[2])+int(i[3]) for i in (list(csv.reader(file))[1:])})
#     print(sum([counter[i]*price[i] for i in counter]))
# books_in_stock, buyers,  = Counter(input().split()), int(input())
# books_in_stock.update('t')
# for i in range(buyers):
#     a = input().split()
#     if a[0] in books_in_stock:
#         books_in_stock[a[0]] -= 1
#         if books_in_stock[a[0]] > -1:
#             books_in_stock['t']+= int(a[1])
# print(books_in_stock['t']-1)
from collections import defaultdict
from collections import ChainMap
from collections import OrderedDict
# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
# prices = ChainMap(bread, meat, sauce, vegetables, toppings)
# a = Counter(i for i in input().split(',')).items()
# b = max(map(lambda x:len(x[0]),a))
# d= []
# total = 0
# for k,v in a:
#     total+= prices[k]*v
#     d.append(f'{k.ljust(b)} x {v}')
# print(*sorted(d),sep='\n')
# d.append(f'ИТОГ: {total}р')
# print(max(map(lambda x:len(x),d))*'-')
# print(d[-1])
# ржаная булочка,ржаная булочка,говяжий бифштекс,сыр,сыр,салат,барбекю,помидор
from collections import ChainMap

# def get_all_values(obj, char):
#     return {i[char] for i in obj.maps if char in i}
# def deep_update(data, key, value):
#     for i in data.maps:
#         if key in i:
#             i[key] = value
#     data.setdefault(key, value)
# def get_value(date, key, bool=True):
#     try:
#         if bool:
#             for i in date.maps:
#                 if key in i:
#                     return i[key]
#         else:
#             for i in date.maps[::-1]:
#                 if key in i:
#                     return i[key]
#     except:
#         return None
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
#
# print(get_value(chainmap, 'name'))
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
#
# print(get_value(chainmap, 'name', False))
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
#
# print(get_value(chainmap, 'age'))