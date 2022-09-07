import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//*[@id='treasure']")
    x = x_element.get_attribute('valuex')
    # x = x_element.text
    y = calc(x)
    print(x)

    text_field = browser.find_element(By.XPATH, "//*[@id='answer']")
    text_field.send_keys(y)

    browser.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//*[@id='robotsRule']").click()
    browser.find_element(By.XPATH, "//div[1]/form/div/div/button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()