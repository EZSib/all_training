from lib2to3.pgen2 import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

# F:\projPY\venv\Scripts\
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://tomsk.zoon.ru/p-doctor/")
print(driver.page_source)
driver.quit()
