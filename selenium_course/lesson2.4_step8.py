from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 7).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

browser.find_element(By.ID, "book").click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

text_field = browser.find_element(By.XPATH, "//*[@id='answer']")
text_field.send_keys(y)

browser.find_element(By.XPATH, "//*[@id='solve']").click()

