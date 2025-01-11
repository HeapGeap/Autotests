import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    button.click()

    ans_field = browser.find_element(By.ID, "answer")
    x_value = browser.find_element(By.ID, "input_value")
    x = calc(x_value.text)
    ans_field.send_keys(x)

    solve = browser.find_element(By.ID , "solve")
    solve.click()



finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
