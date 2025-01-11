import os.path
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    win_after_but = browser.window_handles[1]
    browser.switch_to.window(win_after_but)

    ans_field = browser.find_element(By.ID, "answer")
    ans_x = browser.find_element(By.ID, "input_value")
    x = calc(ans_x.text)
    ans_field.send_keys(x)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()






finally:
    time.sleep(10)
    browser.quit()
