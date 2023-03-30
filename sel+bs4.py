from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.nbcomputers.ru/catalog/noutbuki/")
    driver.implicitly_wait(10)

    # actions = ActionChains(driver)
    # actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "button.class sc-47746e2f-0 jbrSyR"))
    # actions.perform()
    bt_search = driver.find_element(By.CSS_SELECTOR, 'input.ant-input')

    wait = WebDriverWait(driver, timeout=10)

    while True:
        wait.until(ActionChains(driver).move_to_element(bt_search).click(bt_search))

    # find_element
    # find_elements
except Exception as ex:
    print(f'Error: {ex}')

html = driver.page_source
driver.quit()

# from bs4 import BeautifulSoup
# import csv
#
# soup = BeautifulSoup(html, 'lxml')
# cards_list = soup.select_one('div.class ant-col ant-col-xs-24 ant-col-xl-19 ant-col-xl-offset-1')
# cards = cards_list.select('article.class sc-5133e97-0 biRUmW')
#
# note_info_list = []
# for card in cards:
#     name = card.select('h2.class sc-d9406361-0 iVdSZe')
#
#
#     price = card.select_one('span.class sc-96470d6e-2 chpWFX')
#
#     id = card.select_one("p.class sc-d9406361-0 cfXmWO")
#
#
#     note_info_list.append({
#         "name": name,
#         "price": price,
#         "id": id
#     })
# print(*note_info_list, sep='\n')
# with open("task44.csv", "w", newline='') as f:
#     writer = csv.DictWriter(f, spec_info_list[0].keys())
#     writer.writeheader()
#     for r in spec_info_list:
#         writer.writerow(r)

# spec_list2 = ",".join([spec.text for spec in spec_list])
# print(spec_list2)
