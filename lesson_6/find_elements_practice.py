import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# спобос убрать лишний лог devtools
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--log-level=3")  # Только этот аргумент часто помогает
chrome_options.add_argument("--log-level=0")  # Самый важный параметр
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)
# заканчивается здесь

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/categories/1?utm_source=homepage")

time.sleep(5)

# print(len(driver.find_elements("class name","nav-link")))
driver.find_elements("class name","nav-link")[4].click()
time.sleep(5)
# driver.find_element("id", "loginformsubmit").click()