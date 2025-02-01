import json
import time

import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def load_config():
    with open('pass.json', 'r') as config_file:
        config = json.load(config_file)
        return config


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links, load_config):
    link = f"{links}"
    browser.get(link)

    time.sleep(2)

    login = load_config['login_stepik']
    password = load_config['password_stepik']

    enter_butt = browser.find_element(By.ID, "ember471")
    enter_butt.click()

    browser.implicitly_wait(10)

    inp_l = browser.find_element(By.NAME, "login")
    inp_p = browser.find_element(By.ID, "id_login_password")
    auth_butt = browser.find_element(By.CSS_SELECTOR, ".button_with-loader")

    inp_l.send_keys(login)
    inp_p.send_keys(password)
    time.sleep(1)
    auth_butt.click()
    time.sleep(1)

    ans_txtfld = browser.find_element(By.TAG_NAME, "textarea")
    ans_txtfld.send_keys(str(math.log(int(time.time()))))

    ans_butt = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )

    ans_butt.click()


    assert_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")

    assert "Correct!" in assert_text.text
