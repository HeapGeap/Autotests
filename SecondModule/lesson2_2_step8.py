import os.path
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fn_input = browser.find_element(By.CSS_SELECTOR, ".form-group :nth-child(2)")
    fn_input.send_keys("@#$%^&*")

    ln_input = browser.find_element(By.CSS_SELECTOR, ".form-group :nth-child(4)")
    ln_input.send_keys("))*&^%@#$FDKD")

    em_input = browser.find_element(By.CSS_SELECTOR, ".form-group :nth-child(6)")
    em_input.send_keys("wedmwoe")

    # inp_elements = browser.find_elements(By.TAG_NAME, "input")
    # for x in inp_elements:
    #     variable = random.randint(1, 1000)
    #     x.send_keys(variable)      #такое заполнение, конечно cool, но в рамках текущей задачи оно затрагивает не только поля ввода, но и то - куда нами надо грузить файл (получим ошибку по исполнению)

    element = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем текущую рабочую директорию
    file_path = os.path.join(current_dir, "MyFile.txt")  # приклеиваем к текущей директории наш файл MyFile.txt

    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
