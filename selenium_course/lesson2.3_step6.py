import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//form/div/div/button").click()
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    text_field = browser.find_element(By.XPATH, "//*[@id='answer']")
    text_field.send_keys(y)

    browser.find_element(By.XPATH, "//form/div/div/button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()