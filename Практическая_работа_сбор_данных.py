import requests, json,re
from collections import defaultdict
# ACCESS_TOKEN = 'vk1.a.u2UIsflZ9waqGFvoDYLsxpadE3yrTcpIiLXTm2mCDV08cINNGNtEkhH7El99v77UjcFgOh7IvRWpawskqaDPnw2qlqB1t4KfzV4rdUGZH3-kVM4OqTIJmm30z3JR9Fl6QbyiOGkzgzAxztv6_V-5lxlDVE-vxEyPHb3ycYKXZmSd8Cy1otApV4_xz72YCkqRB0v5a2BBJyuXx-7qmCFigQ'
# METHOD_NAME = 'database.getSchools'
# URL = f'https://api.vk.com/method/{METHOD_NAME}'
# pattern = r'[/.а-яА-ЯёЁ№()0-9\- ]+'
#
# params = {
#     "access_token": ACCESS_TOKEN,
#     "city_id": 144,
#     "sort": 6,
#     "v": 5.131
# }
# final_res = defaultdict(list)
# res = requests.get(URL, params=params).text
# res1 = re.findall(pattern, res)
# res1 = [i for i in res1 if  any(map(lambda x: x in [(lambda c: chr(c))(i) for i in range(1072, 1104)], i))]
# res = res.split(':')
# res = [i.replace('},{"id"','').replace('}]}}','') for i in res if  any(map(lambda x: x in [(lambda c: chr(c))(i) for i in range(1072, 1104)],i )) ]
# for j in res1:
#     final_res[j[:j.find('№')]].append(j[j.rfind('№'):])
# print(*final_res.items(), sep='\n')
# # with open('kemerovo_schools.json', 'w', encoding='utf8') as file:
# #     json.dump(final_res, file, ensure_ascii=False, indent=2)
#
# # res = requests.get(URL, params=params).json()

# '''задача 2'''
import requests, csv

ACCESS_TOKEN = 'vk1.a.u2UIsflZ9waqGFvoDYLsxpadE3yrTcpIiLXTm2mCDV08cINNGNtEkhH7El99v77UjcFgOh7IvRWpawskqaDPnw2qlqB1t4KfzV4rdUGZH3-kVM4OqTIJmm30z3JR9Fl6QbyiOGkzgzAxztv6_V-5lxlDVE-vxEyPHb3ycYKXZmSd8Cy1otApV4_xz72YCkqRB0v5a2BBJyuXx-7qmCFigQ'
METHOD_NAME = 'groups.getMembers'
URL = f'https://api.vk.com/method/{METHOD_NAME}'


params = {
    "access_token": ACCESS_TOKEN,
    'group_id' : 29534144,
    'fields' : 'sex, city, relation',
    'sort': 'id_asc',
    "v": 5.131
}
relations = {
1 : "не женат/не замужем",
2 : "есть друг/есть подруга",
3 : "помолвлен/помолвлена",
4 : "женат/замужем",
5 : "всё сложно",
6 : "в активном поиске",
7 : "влюблён/влюблена",
8 : "в гражданском браке",
0 : "не указано"
}
seex = {0: 'не указан', 1: 'Ж', 2: 'М'}
res = requests.get(URL, params=params).json()
res = res['response']["items"]
res_list = []
for r in res:
    if 'city' in r:
        city = r['city']['title']
    else: city = 'Город-Герой'
    sex = r.get('sex', 0)
    relation = r.get('relation', 0)
    res_list.append({'city' : city,'sex' : seex[sex], 'ralation' : relations[relation]})


with open('lentach.csv', 'w', encoding='utf8', newline='') as file:
        writer = csv.DictWriter(file,fieldnames=res_list[0])
        writer.writeheader()
        for row in res_list:
            writer.writerow(row)
# import pandas as pd
# f = pd.read_csv("lentach.csv")
# keep_col = ['relation','sex','city']
# new_f = f[keep_col]
# new_f.to_csv("lentach_pd.csv", index=False)
'''ЗАДАЧА 3 СКРЕЩИВАЕМ СЕЛЕНИУМ И БЬЮТИФУЛ СУП '''
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# from random import randint
# service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=chrome_options)
# try:
#     driver.get("https://www.nbcomputers.ru/catalog/noutbuki/")
#     driver.implicitly_wait(10)
#     bt_search = driver.find_element(By.XPATH, '//*[@id="catalog-listing"]/button')
#     while True:
#         bt_search.click()
#         time.sleep(randint(1, 10))
# except Exception as ex:
#     print(f'Error: {ex}')
#
# html = driver.page_source
# driver.quit()