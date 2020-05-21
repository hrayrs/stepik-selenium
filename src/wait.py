from selenium import webdriver
import time
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "100"))  # ask Selenium check during 5sec untill button became clickable

    bet = browser.find_element_by_id("book")
    bet.click()

    # get calc value from attribute
    #wait = WebDriverWait(browser, 12).until_not(
    #    EC.text_to_be_present_in_element ((By.ID, "input_value"), "N"))  # ask Selenium check during 5sec untill button became clickable

    img_el = browser.find_element_by_id("input_value")
    #print("value wait", wait, "text ", img_el.text)
    print("text ", img_el.text)

    x = int(img_el.text)

    #put answer
    y = calc(x)
    a_el = browser.find_element_by_id("answer")
    a_el.send_keys(y)

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # passing button object
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()