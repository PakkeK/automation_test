import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://vk.com/")
current_title_vk = driver.title
print("Title страницы: ", current_title_vk)
assert current_title_vk == "ВКонтакте | Добро пожаловать", "Неверное название страницы"
time.sleep(2)

driver.get("https://ya.ru/")
current_title_ya = driver.title
print("Title страницы: ", current_title_ya)
# assert current_title_ya == "Яндекс — быстрый поиск в интернете", "Неверное название страницы"
time.sleep(2)

driver.back()
print("Выполнен возврат назад")
assert current_title_vk != current_title_ya, "Вы не вернулись назад"
time.sleep(2)

driver.refresh()
print("Перезагрузка страницы")
time.sleep(2)

current_url_vk = driver.current_url
print("Текущий URL страницы: ", current_url_vk)
assert current_url_vk == "https://vk.com/", "Неверный формат URL"

driver.forward()
print("Выполнен переход вперед")
time.sleep(2)

current_url_ya = driver.current_url
print("Текущий URL страницы: ", current_url_ya)
assert current_url_ya == "https://ya.ru/", "Неверный формат URL"

print("Проверка что URL адресс изменился")
assert current_url_ya != current_url_vk, "URL не изменнен"
time.sleep(3)

print("Проверка окончена")

time.sleep(10)

