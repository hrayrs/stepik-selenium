from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    # time.sleep(1)

    # alert case
    #modal = browser.switch_to.alert
    #modal.accept()  # alert type

    # redirect case
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    # robot captcha
    # get calc value from attribute
    img_el = browser.find_element_by_id("input_value")
    x = int(img_el.text)
    print("value of iput value is: ", x)
    y = calc(x)
    # put answer
    a_el = browser.find_element_by_id("answer")
    a_el.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()