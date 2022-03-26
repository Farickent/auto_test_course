from selenium import webdriver
import time

link = "https://badoo.com/ru/signin/"
browser = webdriver.Chrome()
browser.get(link)

try:
    login=browser.find_element_by_name("email")
    login.send_keys("hofebo7654@snece.com")
    passs=browser.find_element_by_name("password")
    passs.send_keys("Fara11111")
    time.sleep(2)
    knopka=browser.find_element_by_name("post").click()
    time.sleep(5)
    capca=browser.find_element_by_xpath("/html/body/aside/section/div[1]/div/div/div[1]/div/section/div/div[3]/div")
    capca.click()
    time.sleep(3)
    total_foto=browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[1]/div/div[4]/div/div[1]/div/span/span[2]').text
    total_foto=int(total_foto)
    like = browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]').click()
    time.sleep(3)
    sms_pop_ap = browser.find_element_by_css_selector("div.btn.btn--monochrome.js-chrome-pushes-deny").click()
    for i in range(100):
        total_foto = browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[1]/div/div[4]/div/div[1]/div/span/span[2]').text
        total_foto = int(total_foto)
        count_foto = 2
        time.sleep(1)
        if total_foto >= count_foto:
            like = browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]').click()

        else:
            dizlike = browser.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(9000)
    # закрываем браузер после всех манипуляций
    browser.quit()
