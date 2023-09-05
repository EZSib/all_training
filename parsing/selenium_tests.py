# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     input0 = browser.find_element(By.PARTIAL_LINK_TEXT, '224592')
#     input0.click()
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[3]/input')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, "input")
#     for element in elements:
#         element.send_keys("bI")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# import math
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# link = "http://suninjuly.github.io/explicit_wait2.html?"
# def calc(x):
#     return math.log(abs(12 * math.sin(x)))
#
# try:
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     browser.get(link)
#
#     # input1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
#     # new_www = browser.window_handles[1]
#     # browser.switch_to.new_window(new_www)
#     WebDriverWait(browser,15).until(EC.text_to_be_present_in_element(By.ID, 'price'), '$100')
#     a = browser.find_element(By.ID, 'book')
#     a.click()
#     # input2 = int(browser.find_element(By.ID, 'input_value').text)
#     # answ = calc(input2)
#     # input3 = browser.find_element(By.ID, 'answer').send_keys(answ)
#     # # select = Select(browser.find_element(By.TAG_NAME, 'answer'))
#     # # select.select_by_value(answer)
#     # button = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()
#
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(15)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from random import randint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.nbcomputers.ru/catalog/noutbuki/")
    driver.implicitly_wait(3)
    bt_search = driver.find_element(By.XPATH, '//*[@id="catalog-listing"]/button')
    for i in range(23):
        bt_search.click()
        time.sleep(5)
        # bt_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="catalog-listing"]/button')))
        print(i)
    print(driver.find_elements(By.CSS_SELECTOR, 'div.sc-5133e97-15.buPdmH > a > h2::text'))
except Exception as ex:
    print(f'Error: {ex}')

html = driver.page_source
driver.quit()













