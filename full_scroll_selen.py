from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = f'https://www.nbcomputers.ru/catalog/noutbuki'
driver.get(URL)
driver.implicitly_wait(5)
footer = driver.find_element(By.CSS_SELECTOR, ".jbrSyR")


last_height = driver.execute_script("return document.body.scrollHeight")
actions = ActionChains(driver)
wait = WebDriverWait(driver, timeout=15)

res_name_price_id = []
try:
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, 3240);")
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        wait.until(EC.element_to_be_clickable(footer)).click()

except Exception as ex:
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    all_cards = soup.select('article')
    for card in all_cards:
        name = (card.select_one('.iVdSZe').text).split('&')[0]
        price = ''.join(list((i for i in (card.select_one('.sc-96470d6e-2').text) if i.isdigit())))
        id = card.select_one('.cfXmWO').text.split()[1].strip()
        res_name_price_id.append({'name': name, 'price': price, 'id': id})

print(len(res_name_price_id))

driver.quit()

with open('full_scroll_selen.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=res_name_price_id[0])
    writer.writeheader()
    for row in res_name_price_id:
        writer.writerow(row)

