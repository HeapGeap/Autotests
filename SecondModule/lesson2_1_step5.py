import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    x_field = browser.find_element(By.ID, "answer")
    x_field.send_keys(y)

    check_robo = browser.find_element(By.ID, "robotCheckbox")
    check_robo.click()

    check_radio_robo = browser.find_element(By.ID, "robotsRule")
    check_radio_robo.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
