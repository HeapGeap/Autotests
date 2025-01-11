import os.path
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math  #

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    confirm_form = browser.switch_to.alert
    confirm_form.accept()

    x_value = browser.find_element(By.ID, "input_value")
    x_value_txt = x_value.text
    y = calc(x_value_txt)

    inp_x = browser.find_element(By.ID, "answer")
    inp_x.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
