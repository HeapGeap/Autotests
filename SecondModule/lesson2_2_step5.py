from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Исполняемый JS который фиксит ошибку, скроллит страницу
button.click()
