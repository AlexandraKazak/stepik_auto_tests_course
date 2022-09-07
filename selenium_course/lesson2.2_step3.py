import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    a = (int(num1) + int(num2))

    select = Select(browser.find_element(By.XPATH, "//*[@id='dropdown']"))
    select.select_by_value(str(a))
    browser.find_element(By.XPATH, "//div[1]/form/button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()