import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# настройка chrome для отключения логов
chrome_options = Options()
chrome_options.add_argument("--log-level=0")  # Самый важный параметр
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--disable-dev-shm-usage")

# создаем сервис и драйвер
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)

# поиск и вывод в лог информации об элементах
print("=== Найденные элементы ===")

# # print(len(driver.find_elements("class name","nav-link")))
# driver.find_element("class name","wikipedia-icon").click()
# time.sleep(5)
# driver.find_element("id", "Wikipedia1_wikipedia-search-input").click()
# driver.find_element("class name","wikipedia-search-button").click()

# 1. найти иконку wikipedia по классу
try:
    wikipedia_icon = driver.find_element("class name", "wikipedia-icon")
    print("Найти иконку wikipedia - Успех")
    print(f"Элемент: {wikipedia_icon.tag_name}, видимый: {wikipedia_icon.is_displayed()}")
except Exception as e:
    print (f"Найти иконку wikipedia_icon - Ошибка: {e}")

# 2. найти поле ввода Wikipedia по id
try:
    search_input = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
    print("Найти поле ввода Wikipedia по id - Успех")
    print(f"Элемент: {search_input.tag_name}, placeholder: {search_input.get_attribute('placeholder')}")
except Exception as e:
    print (f"Найти поле ввода Wikipedia по id - Ошибка: {e}")

# 3. Найти кнопку поиска Wikipedia по классу 
try:
    search_button = driver.find_element("class name", "wikipedia-search-button")
    print("Найти кнопку Wikipedia по классу - Успех")
    print(f"Элемент: {search_button.tag_name}, текст: {search_button.get_attribute('value')}")
except Exception as e:
    print (f"Найти кнопку поиска Wikipedia по классу - Ошибка: {e}")    

# 4. Найти любой другой элемент на странице  
try:
    buttons = driver.find_elements("tag name", "button")
    print(f"Найти элементы по тегу 'button' - Успех")
    print(f"Найдено кнопок: {len(buttons)}")
    for i, button in enumerate(buttons[:14]):
        print(f"Кнопка {i+1}: текст='{button.text}', тип='{button.get_attribute('type')}'")
except Exception as e:
    print (f"Найти элементы по тегу 'button' - Ошибка: {e}")   