from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    first_name=browser.find_element_by_name("firstname")
    first_name.send_keys("Vlad")
    last_name=browser.find_element_by_name("lastname")
    last_name.send_keys("Fara")
    email=browser.find_element_by_name("email")
    email.send_keys("Fara@proger.ua")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Допустим ето етот док .txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector("input#file")
    element.send_keys(file_path)
    sumbit=browser.find_element_by_tag_name("button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
