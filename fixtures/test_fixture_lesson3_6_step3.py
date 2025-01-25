import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru",
                                      "en-gb"])  # здесь и ставим - шо тест параметризованный и будет подставлять вместо {language} значения ru и en
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"  # пишем и юзаем f-строкой
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
