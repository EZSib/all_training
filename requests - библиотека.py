import requests

# res = requests.get("http://httpbin.org/")
# print(res)
# from requests.exceptions import HTTPError
#
# for url in ['http://httpbin.org/status/400', 'http://httpbin.ru', 'http://httpbin.org/status/200']:
#   try:
#     res = requests.get(url)
#     res.raise_for_status()
#   except HTTPError as ex:
#     print("HTTPError: {}".format(ex))
#   except Exception as ex:
#     print("Exception: {}".format(ex))
#   else:
#     print("Success!")
# import requests
# url = 'https://rickandmortyapi.com/api/character?page=1'
# res = requests.get(url)
# print(res.text, sep='\n')
# print(requests.status_codes)
# import requests
# url = 'https://rickandmortyapi.com/api/character?page=1'
# res = requests.get(url)
# print(res.text, sep='\n')
# string = str(res.text)
# print(string.count('Male'), string.count('Female'))
import requests
import json


ACCESS_TOKEN = 'vk1.a.u2UIsflZ9waqGFvoDYLsxpadE3yrTcpIiLXTm2mCDV08cINNGNtEkhH7El99v77UjcFgOh7IvRWpawskqaDPnw2qlqB1t4KfzV4rdUGZH3-kVM4OqTIJmm30z3JR9Fl6QbyiOGkzgzAxztv6_V-5lxlDVE-vxEyPHb3ycYKXZmSd8Cy1otApV4_xz72YCkqRB0v5a2BBJyuXx-7qmCFigQ'
# METHOD_NAME = 'groups.search'
# URL = f'https://api.vk.com/method/{METHOD_NAME}'
#
# params = {
#     "access_token": ACCESS_TOKEN,
#     "q": "косметика",
#     "country_id": 1,
#     "city_id": 73,
#     "sort": 6,
#     "count": 100,
#     "v": 5.131
# }
#
# res = requests.get(URL, params=params).json()
#
# if res.get("response"):
#   result_list = []
#   items = res["response"]["items"]
#   if items:
#     for item in items:
#       screen_name = item['screen_name']
#       result_list.append({
#           "id": item['id'],
#           "name": item['name'],
#           "url": f"https://vk.com/{screen_name}",
#           "type": item['type']
#       })
#       with open("task.json", "w", encoding='utf8') as f:
#         result = {"result": result_list}
#         json.dump(result, f, ensure_ascii=False)
# else:
#   error_message = res.get("error")
#   print(f"ERROR: {error_message}")
'''СБОР ДАННЫХ ТЕМА 8'''
import vk_api
import requests
import json

# database.getCities
# groups.getById
# groups.search
# database.getCountries
# vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
# vk = vk_session.get_api()
# try:
#     coutry_id = vk.database.getCountries(code='RU', count=1)['items'][0]['id']
#     city_id = vk.database.getCities(coutry_id=coutry_id,q='Омск')['items'][0]['id']
# except Exception as err:
#     print(f'Error: {err}')
# # print(vk.wall.post(message='Hello world!'))
# print(coutry_id, city_id)
# import csv
# vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
# vk = vk_session.get_api()
#
# # Получение ID города Омск
# city = vk.database.getCities(country_id=1, q="Омск", count=1)
# city_id = city["items"][0]["id"] if city["count"] > 0 else None
#
# # Получение данных о сообществах
# if city_id:
#     key_words = ["цветы", "флористика", "магазин цветов"]
#     for word in key_words:
#         # Получение ID сообществ, которые соответсвуют ключевому слову
#         groups_ids = [
#             group["id"]
#             for group in vk.groups.search(
#                 country_id=1, city_id=city_id, sort=6, q=word, count=500
#             )["items"]
#         ]
#
#         # Получение расширенной информации об указанных группах
#         groups = vk.groups.getById(
#             group_ids=groups_ids, fields="contacts,members_count,description"
#         )
#
#         filename = "{}_data.csv".format(word)
#         f = open(filename, "w", encoding='utf8')
#         # Запись данных в CSV файл
#         writer = csv.DictWriter(f, fieldnames=groups[0].keys())
#         writer.writeheader()
#         for group in groups:
#             writer.writerow(group)

# from random import randint
# import matplotlib.pyplot as plt
#
#
# class Dice:
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def throw(self, number_of_throws=100, number_of_dices=10):
#         dice_values = [0] * number_of_throws
#         for i in range(number_of_throws):
#             for j in range(number_of_dices):
#                 dice_values[i] += randint(1, self.sides)
#         values_range = range(min(dice_values), max(dice_values)+1)
#         return {i: dice_values.count(i) for i in values_range}
#
#
# def gist_plot(data):
#     sort = sorted(data)
#     y = tuple(data[i] for i in sort)
#     x = range(sort[0], sort[-1]+1)
#     ax = plt.gca()
#     ax.bar(x, y, align='center')
#     ax.set_xticks(x)
#     ax.set_xticklabels(x)
#     plt.show()
#
# dice = Dice()
# gist_plot(dice.throw())


