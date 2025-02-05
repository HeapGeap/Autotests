import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_bucket_button(browser):  # поменял название с не очень хорошего, на более сносное)))
    browser.get(link)
    time.sleep(30)
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
        )
    except NoSuchElementException:
        assert False, "NoSuchElementException: Add to cart button is not found on the page"

    # ass_button_busk = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    # assert ass_butt_busk is not None, "Не найдена"   #крайне плохой вариант, не дающий достоверной инфы, к тому же если делать через find_elements - идейность тоже затирается
