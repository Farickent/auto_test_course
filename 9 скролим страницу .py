from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

try:
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1=browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    link=browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);",link)
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()