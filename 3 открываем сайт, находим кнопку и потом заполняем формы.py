from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link=browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
    input1.send_keys("Fara Bog")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
    input2.send_keys("Farisey")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[3]/input")
    input3.send_keys("Kiev")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

