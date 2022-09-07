import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    text_field = browser.find_element(By.XPATH, "//*[@id='answer']")
    text_field.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    browser.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//*[@id='robotsRule']").click()
    browser.find_element(By.XPATH, "//div[1]/form/button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
