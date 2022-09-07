import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[1]/form/div/input[1]")
    input1.send_keys("Жыве")
    input2 = browser.find_element(By.XPATH, "//div[1]/form/div/input[2]")
    input2.send_keys("Беларусь")
    input3 = browser.find_element(By.XPATH, "//div[1]/form/div/input[3]")
    input3.send_keys("freedom to people")

    element = browser.find_element(By.XPATH, "//*[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Song.odt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    browser.find_element(By.XPATH, "//div[1]/form/button").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

