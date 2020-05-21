from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name("firstname")
    name.send_keys("hrayr")

    lname = browser.find_element_by_name("lastname")
    lname.send_keys("sukiasyan")

    mail = browser.find_element_by_name("email")
    mail.send_keys("email@dot.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # get current dir
    file_path   = os.path.join(current_dir, 'test.txt')       # add file name

    file = browser.find_element_by_name("file")
    file.send_keys(file_path)

    submit = browser.find_element_by_tag_name("button")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()