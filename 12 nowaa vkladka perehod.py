from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    knopka=browser.find_element_by_css_selector("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    forma = browser.find_element_by_name("text")
    forma.send_keys(y)
    sumbit = browser.find_element_by_css_selector(".btn.btn-primary").click()
    time.sleep(2)
    confirm = browser.switch_to.alert
    confirm.accept()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
