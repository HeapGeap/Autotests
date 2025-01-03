from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    f_num = browser.find_element(By.ID, "num1")
    s_num = browser.find_element(By.ID, "num2")

    result = int(f_num.text) + int(
        s_num.text)  # здесь лежит сумма двух спэнов - которую надо сравнить со значением списка
    print(result)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(f"{result}")  # решение через f-строки, так же можно решать через обычную str-оболочку
    # select.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
