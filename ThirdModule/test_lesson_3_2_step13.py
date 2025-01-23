# для саморазвития так сказать

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"


def test_reg1():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_fn = browser.find_element(By.TAG_NAME, "input")
        input_fn.send_keys("7126")
        input_ln = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your last name']")
        input_ln.send_keys("91282")
        input_email = browser.find_element(By.CLASS_NAME, "third")
        input_email.send_keys("2112")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        assert "Congratulations! You have successfully registered!" == welcome_text
        #self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Good enough")



    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_reg2():
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля
    input_fn = browser.find_element(By.TAG_NAME, "input")
    input_fn.send_keys("7126")
    input_ln = browser.find_element(By.CSS_SELECTOR, "input[placeholder = 'Input your last name']")
    input_ln.send_keys("91282")
    input_email = browser.find_element(By.CLASS_NAME, "third")
    input_email.send_keys("2112")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Critical")
    assert "Congratulations! You have successfully registered!" == welcome_text
    # закрываем браузер после всех манипуляций
    browser.quit()

# if __name__ == "__main__":
#     unittest.main()
