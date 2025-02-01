import time
import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="session")
def load_config():

    with open('pass.json', 'r') as config_file:

        config = json.load(config_file)
        return config


def test_stepik(load_config):
    wd = webdriver.Chrome()
    wd.get(link)

    login = load_config['login_stepik']
    password = load_config['password_stepik']

    time.sleep(10)

    enter_butt = wd.find_element(By.ID, "ember471")
    time.sleep(1)
    enter_butt.click()
    time.sleep(3)
    inp_l = wd.find_element(By.NAME, "login")

    inp_l.send_keys(login)

    wd.quit()


