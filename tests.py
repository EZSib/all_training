# # Библиотека для работы с HTTP
# import requests
# # Библиотека для работы с JSON
# import json
#
# # (Комментарий): Стоит сначала выписать все константные немутабельные переменные в ВЕРХНЕМ РЕГИСТРЕ (UPPERCASE)
# # (Комментарий): (к ним относятся строки, числа и тд, т.е то, что не изменяются),
# # (Комментарий): а потом мутабельные (списки, словари, кортежи и т.д)
#
# # Константы
# ACCESS_TOKEN = "vk1.a.u2UIsflZ9waqGFvoDYLsxpadE3yrTcpIiLXTm2mCDV08cINNGNtEkhH7El99v77UjcFgOh7IvRWpawskqaDPnw2qlqB1t4KfzV4rdUGZH3-kVM4OqTIJmm30z3JR9Fl6QbyiOGkzgzAxztv6_V-5lxlDVE-vxEyPHb3ycYKXZmSd8Cy1otApV4_xz72YCkqRB0v5a2BBJyuXx-7qmCFigQ"
# COUNTRY_CODE = "BY"
#
# # (Комментарий:) Ссылки являются константами, так что их тоже стоит вынести наверх
# URL_COUNTRY = "https://api.vk.com/method/database.getCountries"
# URL_CITY = "https://api.vk.com/method/database.getCities"
# URL_SCHOOL = "https://api.vk.com/method/database.getSchools"
#
# # (Комментарий): Так как у нас во всех запросах будет повторяться токен и версия,
# # (Комментарий): то стоит их так же вынести в константы и далее просто объединять
# # (Комментарий): с другими словарями(параметрами)
# const_params = {"access_token": ACCESS_TOKEN, "v": "5.131"}
#
# # (Комментарий:) Крайне не рекомендую использовать вложенности.
# # (Комментарий:) Многочисленные if усложняют дебаг кода и его расширение,
# # (Комментарий:) а это особенно важно, если нужно будет расширить парсер
# # (Комментарий:) под доп.функционал, поэтому лучше использовать функции
#
# # (Комментарий:) Так как это не функция, из которой можно было бы просто
# # (Комментарий:) return прописать и выйти при ошибке, то нужно использовать try-exception
# try:
#     # Параметры запроса к методу database.getCountries
#     params = {
#         # (Комментарий): две звездочки просто разворачивают словарь
#         # (Комментарий): (в плане как конфетку из фантика)
#         **const_params,
#         "code": COUNTRY_CODE,
#         "count": 1
#     }
#     # Вызов метода API ВКонтакте database.getCountries
#     resp = requests.get(URL_COUNTRY, params=params).json()
#
#     # (Комментарий:) Стоит идти от обратного, если ошибка - то вылетаем из try
#     # (Комментарий:) так у нас уходит вложенность
#     if resp.get("error"): raise ("Get country error!")
#
#     # (Комментарий:) Необходимо проверять, что список не пустой, иначе выскочит
#     # (Комментарий:) ошибка о неправильном индексе списка.
#     country = resp['response']['items']
#     if len(country) < 1: raise ("No country was found!")
#
#     country_id = country[0]['id']
#     country_name = country[0]['title']
#
#     # Подготавливаем шаблон записи результатов
#     results = {
#         "id": country_id,
#         "name": country_name,
#         "cities": []
#     }
#
#     # Параметры запроса к методу database.getCities
#     params = {**const_params, "country_id": country_id, 'count': 10}
#
#     # Вызов метода API ВКонтакте database.getCities
#     resp = requests.get(URL_CITY, params=params).json()
#
#     if resp.get("error"): raise ("Get cities error!")
#     cities = resp['response']['items']
#
#     # (Комментарий:) Проверка на пустой массив
#     if len(cities) < 1: raise ("No city was found!")
#
#     # (Комментарий:) Лучше не использовать i, j и тд, т.к усложняет чтение
#     for city in cities:
#         city_id = city['id']
#         city_title = city['title']
#
#         # Параметры запроса к методу database.getSchools
#         params = {**const_params, "city_id": city_id}
#
#         # Вызов метода API ВКонтакте database.getSchools
#         resp = requests.get(URL_SCHOOL, params=params).json()
#         if resp.get("error"): raise ("Get schools error!")
#
#         schools = resp['response']['items']
#         if len(schools) < 1: raise ("No school was found!")
#
#         school_titles = []
#         for school in schools:
#             school_titles.append(school['title'])
#
#         # Запись результатов
#         data = {
#             "id": city_id,
#             "name": city_title,
#             "schools": school_titles
#         }
#
#         results['cities'].append(data)
#
# except Exception as ex:
#     print(f"{ex}")
#
# finally:
#     with open("SchoolsSimple.json", "w", encoding='utf8') as created_file:
#         json.dump(results, created_file, ensure_ascii=False, indent=1)

# import requests
# import json
#
#
# ACCESS_TOKEN = "vk1.a.u2UIsflZ9waqGFvoDYLsxpadE3yrTcpIiLXTm2mCDV08cINNGNtEkhH7El99v77UjcFgOh7IvRWpawskqaDPnw2qlqB1t4KfzV4rdUGZH3-kVM4OqTIJmm30z3JR9Fl6QbyiOGkzgzAxztv6_V-5lxlDVE-vxEyPHb3ycYKXZmSd8Cy1otApV4_xz72YCkqRB0v5a2BBJyuXx-7qmCFigQ"
# COUNTRY_CODE = "BY"
#
# URL_COUNTRY = "https://api.vk.com/method/database.getCountries"
# URL_CITY = "https://api.vk.com/method/database.getCities"
# URL_SCHOOL = "https://api.vk.com/method/database.getSchools"
#
# CONST_PARAMS = {"access_token": ACCESS_TOKEN, "v": "5.131"}
#
#
# def handle_response(resp, item_name):
#     if resp.get("error"):
#       print(f"Get {item_name} error!")
#       return
#
#     items = resp['response']['items']
#     if len(items) < 1:
#       print(f"No {item_name} was found!")
#       return
#
#     return items
#
# def get_country(code):
#     """
#         Получение страны по заданному коду
#     """
#     params = {**CONST_PARAMS, "code": code, "count": 1}
#
#     country = handle_response(
#         requests.get(URL_COUNTRY, params=params).json(),
#         "country"
#     )
#
#     if not country: return
#     return country[0]
#
# def get_cities(country_id):
#     """
#         Получение города по заданной стране
#     """
#     params = {**CONST_PARAMS, "country_id": country_id, "count": 10}
#
#     cities = handle_response(
#         requests.get(URL_CITY, params=params).json(),
#         "cities"
#     )
#     if not cities: return
#
#     return cities
#
# def get_schools_titles(city_id):
#     """
#         Получение название школ в заданном городе
#     """
#     params = {**CONST_PARAMS, "city_id": city_id}
#
#     schools = handle_response(
#         requests.get(URL_SCHOOL, params=params).json(),
#         "schools"
#     )
#     if not schools: return
#
#     return [school['title'] for school in schools]
#
#
#
# def main():
#     # Объявляем результативный словарь
#     results = {}
#
#     # Получаем данные о стране
#     country = get_country(COUNTRY_CODE)
#     if not country: return
#     results["id"] = country["id"]
#     results["name"] = country["title"]
#
#     # Получаем список городов страны
#     cities = get_cities(country["id"])
#     if not cities: return
#
#     # Получаем список названий школ в городе
#     city_data = []
#     for city in cities:
#       city_id = city['id']
#       city_title = city['title']
#       school_titles_list = get_schools_titles(city_id)
#       city_data.append({
#         "id": city_id,
#         "name": city_title,
#         "schools": school_titles_list
#       })
#     results["cities"] = city_data
#
#     # Записываем все в JSON файл
#     with open("Schools2.json", "w", encoding='utf8') as created_file:
#         json.dump(results, created_file, ensure_ascii=False, indent=1)
#
# main()

import requests
import json
import csv


class VkAPI():
    """
        Класс родитель, через который осуществляются все запросы к API
        (можно расширить и добавить свои методы)
    """
    URL_COUNTRY = "https://api.vk.com/method/database.getCountries"
    URL_CITY = "https://api.vk.com/method/database.getCities"
    URL_SCHOOL = "https://api.vk.com/method/database.getSchools"

    def __init__(self, token):
        self.ACCESS_TOKEN = token or VkAPI.ACCESS_TOKEN
        self.VERSION = "5.131"

    def __handle_response(self, resp, item_name):
        """
            Обработка ответа на запрос (наличие ошибок)
        """
        if resp.get("error"):
            print(f"Get {item_name} error!")
            return

        items = resp['response']['items']
        if len(items) < 1:
            print(f"No {item_name} was found!")
            return

        return items

    def __get_params(self, meta_data):
        """
            Формирование запроса на основе константных значений в родителе
        """
        return {
            "access_token": self.ACCESS_TOKEN,
            "v": self.VERSION,
            **meta_data
        }

    def get_country(self, code):
        """
            Получение страны по заданному коду
        """
        params = self.__get_params({"code": code, "count": 1})
        country = self.__handle_response(
            requests.get(VkAPI.URL_COUNTRY, params=params).json(),
            "country"
        )
        return country[0] if country else None

    def get_country_cities(self, country_id):
        """
            Получение всех городов заданной страны
        """
        params = self.__get_params({"country_id": country_id, "count": 10})
        cities = self.__handle_response(
            requests.get(VkAPI.URL_CITY, params=params).json(),
            "cities"
        )
        return cities if cities else None

    def get_city_schools(self, city_id):
        """
            Получение всех школ в заданном городе
        """
        params = self.__get_params({"city_id": city_id})

        schools = self.__handle_response(
            requests.get(VkAPI.URL_SCHOOL, params=params).json(),
            "schools"
        )
        return schools if schools else None


class SchoolsVkAPI(VkAPI):
    """
        Класс, который работает со школами из базы данных ВКонтакте
        (можно расширить и добавить свои методы)
    """

    def __init__(self, access_token):
        # Инициализация родительского класса
        super(SchoolsVkAPI, self).__init__(access_token)

    def __get_country_info(self, needble_param_names):
        """
            Получение информации о стране по заданым параметрам
        """
        country = self.get_country(self.COUNTRY_CODE)
        if not country: return

        # Словарь информации о стране
        country_info = {}
        # Получение переданных в метод параметров
        for param_name in needble_param_names:
            country_info[param_name] = country.get(param_name, None)

        return country_info

    def __get_schools_titles(self, city_id):
        """
            Получение название школ в заданном городе
        """
        schools = self.get_city_schools(city_id)
        return [school['title'] for school in schools]

    def __get_city_info(self, country_id, needble_param_names):
        """
            Получение информации о городе по заданным параметрам и его школах
        """
        cities = self.get_country_cities(country_id)
        # Список городов
        city_list = []
        # Словарь информации о городе
        city_data = {}

        # Получение переданных в метод параметров
        for city in cities:
            for param_name in needble_param_names:
                city_data[param_name] = city.get(param_name, None)

            school_titles_list = self.__get_schools_titles(city["id"])
            city_list.append({**city_data, "schools": school_titles_list})

        return city_list

    def get_all_in_country(self, country_code, as_file=True):
        """
            Получение информации о всех школах в стране
            as_file - флаг, который указывает, нужно ли записывать результат в файл
        """
        self.COUNTRY_CODE = country_code

        country_info = self.__get_country_info(["id", "title"])
        if not country_info: return

        city_info = self.__get_city_info(country_info["id"], ["id", "title"])
        if not city_info: return

        # Полученную информацию разворачиваем с результативный словарь
        results = {
            **country_info,
            "cities": city_info,
        }
        if as_file:
            # Записываем все в JSON файл
            with open("Schools3.json", "w", encoding='utf8') as f:
                writer = csv.DictWriter(f, fieldnames=results.keys())
                writer.writeheader()

                writer.writerow(results)

        return results
ACCESS_TOKEN = "vk1.a.u2UIsflZ9waqGFvoDYLsxpadE3yrTcpIiLXTm2mCDV08cINNGNtEkhH7El99v77UjcFgOh7IvRWpawskqaDPnw2qlqB1t4KfzV4rdUGZH3-kVM4OqTIJmm30z3JR9Fl6QbyiOGkzgzAxztv6_V-5lxlDVE-vxEyPHb3ycYKXZmSd8Cy1otApV4_xz72YCkqRB0v5a2BBJyuXx-7qmCFigQ"
SchoolsVkAPI(ACCESS_TOKEN).get_all_in_country("BY")