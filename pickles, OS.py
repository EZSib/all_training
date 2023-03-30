import pickle

# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
#
# with open('file.pkl', 'wb') as file:
#     pickle.dump(obj, file)
# with open('file.pkl', 'rb') as file:     # используется файл полученный на предыдущем шаге
#     obj = pickle.load(file)
#     print(obj)
#     print(type(obj))
#
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
#
# new_obj = pickle.loads(binary_obj)
#
# print(new_obj)
# print(obj == new_obj)
# print(obj is new_obj)


# def filter_dump(filename, objects, typename):
#      with open(filename, 'wb') as file:
#          objects = [i for i in objects if type(i) == typename]
#          pickle.dump(objects,file)
# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
# import pickle
# with open(input(), 'rb') as file:
#     c_s = int(input())
#     if type(pickle.load(file)) == list:
#         if min(pickle.load(file)) * max(pickle.load(file)) == c_s:
#             print('Контрольные суммы совпадают')
#         else: print('Контрольные суммы не совпадают')
#     else:
#         print('Контрольные суммы совпадают' if sum([a for a in pickle.load(file) if type(a)==int])==c_s else 'Контрольные суммы не совпадают')
#
# <Краткий конспект>
#
# import os
# print(os.environ) # Получить сведения, которые касаются конфигурации компьютера
#
# os.chdir(r"E:\WB") # Задаёт новую рабочую директорию
#
# print(os.getcwd()) # E:\WB
# print(os.path.exists("E:/WB/test.txt")) # True Файл существует
# print(os.path.isfile("E:/WB/test.txt")) # True Это файл, а не папка
# #os.mkdir(r"E:\folder\1")  # Создаёт новую папку
# print(os.path.basename("E:/WB/test.txt")) # test.txt Выводит название файла
# print(os.path.getsize("E:/")) # Считает размер файла или директории
# # os.renames(r"E:\catalog\one",r"E:\folder\1" ) # - Работает 1 раз ! переименовывает папку
# print(os.listdir(r"E:\WB")) # Выводит список фалов и папок в директории
#
# for root, directories, files in os.walk(r"E:\Видеотека"): # метод walk обходит все папки и печатает название папок и файлов
#        print(root) # название папки
#        for directory in directories:
#                   print(directory) # название папки в папке
#       for file in files:
#                   print(file) # названия файлов в папке