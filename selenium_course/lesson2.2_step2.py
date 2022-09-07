from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#
# link = "http://suninjuly.github.io/get_attribute.html"
#
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# browser.find_element(By.TAG_NAME, "select").click()
# browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# #последнюю строчку можно записать так: browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
#

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"