from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    name_input = browser.find_element_by_xpath("//input[@name ='firstname']")
    name_input.send_keys("Ivan")
    family_input = browser.find_element_by_xpath("//input[@name ='lastname']")
    family_input.send_keys("Ivanov")
    email_input = browser.find_element_by_xpath("//input[@name ='email']")
    email_input.send_keys("test@test.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_xpath("//input[@id ='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("//button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла