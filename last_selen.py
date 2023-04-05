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
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service, options=chrome_options)

URL = f'https://www.nbcomputers.ru/catalog/noutbuki/?page=1'

res_name_price_id = []

driver.implicitly_wait(5)


def parse(URL_page):
    driver.get(URL)
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    all_cards = soup.select('article')
    for card in all_cards:
        name = (card.select_one('.iVdSZe').text).split('&')[0]
        price = ''.join(list((i for i in (card.select_one('.sc-96470d6e-2').text) if i.isdigit())))
        id = card.select_one('.cfXmWO').text.split()[1].strip()
        res_name_price_id.append({'name': name, 'price': price, 'id': id})


try:
    parse(URL)
except Exception as ex:
    print(f'Error: {ex}')
parent_element = driver.find_element(By.XPATH, '//*[@id="catalog-listing"]/div[2]/ul/li[8]/a')
end = int(driver.execute_script('return arguments[0].firstChild.textContent;', parent_element).strip())

dict_XPath = {2: 3, 3: 4, 4: 5, 5: 6}
dict_XPath[end] = 8
try:
    for i in range(2, end+1):
        if 5 < i < end:
            j = 7
        else:
            j = dict_XPath[i]
        driver.implicitly_wait(5)
        actions = ActionChains(driver)
        wait = WebDriverWait(driver, timeout=15)

        actions.move_to_element(driver.find_element(By.XPATH, f'//*[@id="catalog-listing"]/div[2]/ul/li[{j}]/a'))
        actions.perform()
        actions.scroll_to_element(driver.find_element(By.XPATH, f'//*[@id="catalog-listing"]/div[2]/ul/li[{j}]/a'))
        actions.perform()
        # link_page = driver.find_element(By.CSS_SELECTOR, f'ul > li.ant-pagination-item.ant-pagination-item-{i} > a').get_attribute('href') #  пытался очень долго, стабильную ссылку получить не выходит
        wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="catalog-listing"]/div[2]/ul/li[{j}]/a'))).click()

        URL = f'{URL[:URL.index("=")+1]}{i}'
        print(URL)
        parse(URL)
except Exception as ex:
    print(f'Error: {ex}')
print(len(res_name_price_id))

driver.quit()

# with open('bs4_selen.css', 'w', encoding='utf8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=res_name_price_id[0])
#     writer.writeheader()
#     for row in res_name_price_id:
#         writer.writerow(row)
