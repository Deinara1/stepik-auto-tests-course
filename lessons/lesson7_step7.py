from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    find_img = browser.find_element_by_xpath("//img")
    x_element = find_img.get_attribute("valuex")
    y = calc(x_element)
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)
    checkbox_robot = browser.find_element_by_xpath("//input[@id= 'robotCheckbox']")
    checkbox_robot.click()
    radio_robot = browser.find_element_by_xpath("//input[@id= 'robotsRule']")
    radio_robot.click()
    button = browser.find_element_by_xpath("//button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла