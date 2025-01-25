# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     @pytest.mark.regression
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# тест не запускаю, тк не хочу делать pytest ini и менять общую конфигурацию, для специфики используетс conftest  в основном
# + к маркерам можно приматывать конкретный вызов, например python -s -v -m smoke <имя_файла> будет запускатьс только та маркировка - которая указана.
