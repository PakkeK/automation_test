import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

# url = driver.current_url
# print("URL страницы: ", url)
# assert url == "https://www.wikipedia.org/", "Ошибка в URL"

# current_title = driver.title
# print("Title страницы: ", current_title)
# assert current_title == "wikipedia", "Некорректный заголовок страницы"

print(driver.page_source)
time.sleep(3)