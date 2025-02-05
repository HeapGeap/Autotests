import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_bucket_butt(browser):

    browser.get(link)
    time.sleep(30)
    ass_butt_busk = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    assert ass_butt_busk is not None, "Не найдена"

