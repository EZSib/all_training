import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://vsezhurnaly.com/?page={}.html"

def get_html(page):
  """Собирает html"""
  # Инициализация сессии
  session = requests.session()
  # Указание заголовков сессии
  session.headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
      "Accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
  }

  try:
    # Указание заголовков сессии
    res = session.get(URL.format(page))
    # Проверка на ошибку
    res.raise_for_status()
  except Exception as ex:
    print(ex)
    return

  return res.text

get_html('https://vsezhurnaly.com/?page=2.html')
def get_soup(page):
  """ Варит суп """
  # Получаем исходный код
  html = get_html(page)
  # Если нету страницы, то выходим
  if not html: return
  # Начинаем варить суп (Инициализируем bs)
  soup = BeautifulSoup(html, "lxml")
  return soup

lii = []
def get_book_info(li):
  """ Собирает информацию о книге """
  # Получаем название книги, которое находится в теге <a> внутри <h3>
  title = li.select_one("h3 a")
  if not title:
    print("Error find title!")
    return
  title = title["title"]

  # Получаем рейтинг книги, которое находится в теге <p> с классом "star-rating"
  rating = li.select_one("p.star-rating")
  if not rating:
    print("Error find rating!")
    return
  rating = rating["class"][1]

  # Словарь, который сопостовляет слово с цифрой
  WORD_TO_NUM = {
      "One": 1,
      "Two": 2,
      "Three": 3,
      "Four": 4,
      "Five": 5
  }
  rating = WORD_TO_NUM.get(rating, 0)

  # Получаем рейтинг книги, которое находится в теге <p> обернутым в тег
  # <div> с классом "product_price"
  price = li.select_one("div.product_price p")
  if not price:
    print("Error find price!")
    return
  # Получаем часть текста до знака £
  price = price.text.split("£")[1]

  # Возвращаем информацию о книге
  return {
      "title": title,
      "rating": rating,
      "price": price
  }

def get_books_info(soup):
  """ Информация о книгах на странице """
  # Получаем список книг со страницы в теге <ol> с классом "row"
  list_rows = soup.select_one("ol.row")
  # Получаем карточки о книгах из списка в теге <li>
  all_li = list_rows.select("li")
  result = []
  # Проходимся по каждой карточке и достаем из нее информацию
  for li in all_li:
    result.append(get_book_info(li))
  # Краткая запись
  # result = [get_book_info(li) for li in all_li]
  return result
try:
    i = 1
    while True:
        print(*get_books_info(get_soup((i))), sep='\n')
        print('*' * 100)
        i += 1
except:
  print('8cir')


# import requests
# from bs4 import BeautifulSoup
# import lxml
#
# URL = "https://books.toscrape.com/catalogue/page-{}.html"
#
# def get_html(page):
#   """Собирает html"""
#   # Инициализация сессии
#   session = requests.session()
#   # Указание заголовков сессии
#   session.headers = {
#       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
#       "Accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
#   }
#
#   try:
#     # Указание заголовков сессии
#     res = session.get(URL.format(page))
#     # Проверка на ошибку
#     res.raise_for_status()
#   except Exception as ex:
#     print(ex)
#     return
#
#   return res.text
#
#
# def get_soup(page):
#   """ Варит суп """
#   # Получаем исходный код
#   html = get_html(page)
#   # Если нету страницы, то выходим
#   if not html: return
#   # Начинаем варить суп (Инициализируем bs)
#   soup = BeautifulSoup(html, "lxml")
#   return soup
#
#
# def get_book_info(li):
#   """ Собирает информацию о книге """
#   # Получаем название книги, которое находится в теге <a> внутри <h3>
#   title = li.select_one("h3 a")
#   if not title:
#     print("Error find title!")
#     return
#   title = title["title"]
#
#   # Получаем рейтинг книги, которое находится в теге <p> с классом "star-rating"
#   rating = li.select_one("p.star-rating")
#   if not rating:
#     print("Error find rating!")
#     return
#   rating = rating["class"][1]
#
#   # Словарь, который сопостовляет слово с цифрой
#   WORD_TO_NUM = {
#       "One": 1,
#       "Two": 2,
#       "Three": 3,
#       "Four": 4,
#       "Five": 5
#   }
#   rating = WORD_TO_NUM.get(rating, 0)
#
#   # Получаем рейтинг книги, которое находится в теге <p> обернутым в тег
#   # <div> с классом "product_price"
#   price = li.select_one("div.product_price p")
#   if not price:
#     print("Error find price!")
#     return
#   # Получаем часть текста до знака £
#   price = price.text.split("£")[1]
#
#   # Возвращаем информацию о книге
#   return {
#       "title": title,
#       "rating": rating,
#       "price": price
#   }
#
# def get_books_info(soup):
#   """ Информация о книгах на странице """
#   # Получаем список книг со страницы в теге <ol> с классом "row"
#   list_rows = soup.select_one("ol.row")
#   # Получаем карточки о книгах из списка в теге <li>
#   all_li = list_rows.select("li")
#   result = []
#   # Проходимся по каждой карточке и достаем из нее информацию
#   for li in all_li:
#     result.append(get_book_info(li))
#   # Краткая запись
#   # result = [get_book_info(li) for li in all_li]
#   return result
