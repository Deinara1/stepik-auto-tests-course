from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath("//span[@id = 'input_value']")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element_by_xpath("//input[@id ='answer']")
    answer_input.send_keys(y)

    button_submit = browser.find_element_by_xpath("//button[text()='Submit']")
    button_submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла