from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("document.querySelector('footer').remove()")

    x_element = browser.find_element(By.ID, "input_value")
    x = calc(x_element.text)

    #browser.execute_script("window.scrollBy(0, 150)", "")

    button = browser.find_element(By.TAG_NAME, "button")

    inp_x = browser.find_element(By.ID, "answer")
    inp_x.send_keys(x)

    robo_Check = browser.find_element(By.ID, "robotCheckbox")
    robo_Check.click()

    robo_radio_check = browser.find_element(By.ID, "robotsRule")
    robo_radio_check.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
