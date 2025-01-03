from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("document.title='Script executing';alert('Robots at work');")  #вызывает браузерное уведомление 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
