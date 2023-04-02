# import json
# import csv
#
# with open('playgrounds.csv', encoding='utf8') as data, open('addresses.json', 'w', encoding='utf8') as newAdress:
#     rows = list(csv.reader(data, delimiter=';'))[1:]
#     d_w = {}
#     for x in rows:
#         d_w.setdefault(x[1], {}).setdefault(x[2], []).append(x[3])
#     json.dump(d_w, newAdress, ensure_ascii=False, indent=3)

# from zipfile import ZipFile
#
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)         # дата изменения файла
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')
# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()                # получаем названия всех файлов архива
#     last_file = zip_file.getinfo(info[-4])    # получаем информацию об отдельном файле
#     print(last_file.file_size)
#     print(last_file.compress_size)
#     print(last_file.filename)
#     print(last_file.date_time)
# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read().decode('utf-8'))
# import csv
# col = ['domain','count']
# with open('data1.csv', encoding='utf-8') as file:
#     rows = list(csv.reader(file))[1:]
#     d_w = {}
#     for dom in rows:
#         a = dom[2].split('@')
#         d_w.setdefault(a[1],0)
#         d_w[a[1]] += 1
#         d_w = sorted(d_w.items(), key = lambda x: x[1])
#         with open('domain_usage.csv', 'w', encoding='utf-8') as file:
#             writer = csv.writer(file, quoting=csv.QUOTE_NONE)
#             writer.writerow(col)
#             for row in d_w:
#                 print(row)
#                 writer.writerow(row)

# with open('data1.json', encoding='utf8') as data1, open('data2.json', encoding='utf8') as data2:
#     file1, file2 = json.loads(data1.read()), json.loads(data2.read())
#     file1.update(file2)
#     with open('data_merge.json', 'w', encoding='utf8')as result_dct:
#         json.dump(file1, result_dct)
# with open('people.json', encoding='utf8') as people,open('updated_people', 'w', encoding='utf8')as up_people:
#     file1 = json.loads(people.read())
#     key_list = []
#     [[key_list.append(k) for k,v in items.items() if k not in key_list] for items in file1]
#     [[i.setdefault(j) for j in key_list] for i in file1]
#     json.dump(file1, up_people)
# with open('countries.json', encoding='utf8') as countries,open('religion.json', 'w', encoding='utf8')as relig:
#     file1 = json.loads(countries.read())
#     relig_dct =  {}
#     print(file1)
#     for i in file1:
#         relig_dct.setdefault(i['religion'], []).append(i['country'])
#     json.dump(relig_dct, relig,indent=3)


# from zipfile import ZipFile
# from datetime import datetime as dt
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     dates = (list(filter(lambda x: dt(*x.date_time)>dt(2021,11,30,14,22,0), (filter(lambda x:not x.is_dir(), info)))))
#     sorted_files = sorted(dates, key=lambda x:x.filename[x.filename.rfind('/')+1:])
#     for i in sorted_files:
#         print(i.filename[i.filename.rfind('/')+1:])
# , (filter(lambda x: not x.is_dir(), info)))))
# from zipfile import ZipFile
# from datetime import datetime as dt
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     dates = (list(sorted(filter(lambda x:not x.is_dir(), info), key=lambda x:x.filename[x.filename.rfind('/')+1:] )))
#     for i in dates:
#         print(
#             i.filename[i.filename.rfind('/')+1:],'\n',
#             '  Дата модификации файла: ',dt(*i.date_time), '\n',
#             '  Объем исходного файла: ',i.file_size,' байт(а)','\n'
#             '  Объем сжатого файла: ',i.compress_size,' байт(а)','\n',sep='')
#     for i in dates:
#         print(f'{i.filename[i.filename.rfind('/')+1:]}'))
# from zipfile import ZipFile
# def convert_bytes(size):
#     """Конвертер байт в большие единицы"""
#     if size < 1024:
#         return f'{size} B'
#     elif 1024 <= size < 1048576:
#         return f'{round(size / 1024)} KB'
#     elif 1048576 <= size < 1073741824:
#         return f'{round(size / 1048576)} MB'
#     else:
#         return f'{round(size / 1073741824)} GB'
# with ZipFile('desktop.zip') as zip_file:
#     info =  zip_file.infolist()
#     for i in info:
#         j = i.file_size
#         i = i.filename
#         spaces = i.count('/')-1              #отступы для корневых папок не нужны
#         if i.endswith('/'):                  #проверка на файл/папку
#             if i.count('/') == 1:            #вывод корневой папки
#                 i=i.replace('/', '')
#             else:
#                 while i.count('/')>=2:
#                     if i.count('/')<=2:
#                         break
#                     i =  i.replace('/', '', 1)   #убираем лишние /
#                 i = i[i.find('/') + 1:i.rfind('/')]
#         else:
#             spaces = i.count('/')
#             i = i[i.rfind('/')+1:]
#         if j>0:
#             print(f'{spaces*"  "}{i} {convert_bytes(j)}')
#         else:
#             print(f'{spaces * "  "}{i}')
#             # а же задача но с использовнием рекурсии:
# from zipfile import ZipFile
#
# def hr_size(n, k = 0):
#     return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)
#
# with ZipFile('desktop.zip') as z:
#     for i in z.infolist():
#         p = i.filename.strip('/').split('/')
#         print('  ' * (len(p) - 1) + p[-1] + ('' if i.is_dir() else ' ' + hr_size(i.file_size)))

# import csv
#
# with open('prices.csv', encoding='utf8') as file:
#     items, index_item, true_shop, shop_count = 100, 0, 0, 0
#     a = list(row for row in csv.reader(file))
#     for shop in a[1:]:
#         for item in shop:
#             shop_count += 1
#             count = 0
#             for num in item.split(';')[1:]:
#                 count += 1
#                 if int(num) < items:
#                     items, index_item, true_shop = int(num), count, shop_count
#     print(f"{(a[0][0]).split(';')[index_item]}: {(a[true_shop])[0].split(';')[0]}")
#
# list_of_dicts = [
#     {1: 'mango', 2: 'pawpaw'},
#     {'fruit': 'mango', 1: [4, 6, 8]},
#     {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'},
#     {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'},
#     {(1, 2, 3, 4) : [1, 2, 3, 4]}
# ]
# import sys, decimal
# a = decimal.Decimal(10000000000000000000000000000)
# print(sys.getsizeof(a),sys.getsizeof(100_000_00), sys.getsizeof(0,9999999999999999999999999999))

# list1 = ['это', 'ваш', 'список', 'с', 'элементами' ]
# print(*list1, sep='\n')
# print(float(True))
#









